#!/usr/bin/env python3
"""Validate (and optionally repair) YAML front matter across _posts/.

Usage:
    python3 scripts/validate_posts.py           # report problems, exit 1 if any
    python3 scripts/validate_posts.py --fix     # auto-repair known corruption patterns

Repair strategies (each result is re-validated before being written):
  1. permalink splice — the historic pipeline bug that inserted
     "permalink: ...\n" mid-line inside another field value (it matched the
     "---" dash run inside slugified image filenames instead of the closing
     front-matter delimiter).
  2. broken quiz block — LLM output truncation leaves an unterminated quiz
     entry; the quiz field is optional, so drop the whole block.

It also fails when a post's `audio:` names an mp3 that git does not track
under audio/: the player still renders, requests the file from jsDelivr,
gets a 404 and its play button silently does nothing. --fix leaves those
alone; commit the mp3 or remove the line.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "_posts"

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
SPLICE_RE = re.compile(
    r"^(?P<pre>[A-Za-z_]+: \S*?)permalink: (?P<plink>/\S+/)\s*\n(?P<post>\S+)$",
    re.MULTILINE,
)
QUIZ_BLOCK_RE = re.compile(
    r"^quiz:\s*\n(?:^(?:[ \t]+\S.*)?\n?)*", re.MULTILINE
)


def load_front_matter(content: str) -> tuple[dict | None, str | None]:
    """Return (front matter, None) when valid, else (None, the problem)."""
    m = FRONT_MATTER_RE.match(content)
    if not m:
        return None, "no closed front matter block"
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return None, f"invalid YAML: {str(e).splitlines()[0]}"
    if not isinstance(data, dict):
        return None, "front matter is not a mapping"
    for key, value in data.items():
        if isinstance(value, str) and re.search(r"\b(permalink|image):", value):
            return None, f"spliced field inside '{key}'"
    return data, None


def parse_error(content: str) -> str | None:
    """Return a description of the front-matter problem, or None if valid."""
    return load_front_matter(content)[1]


def tracked_audio(repo: Path) -> set[str]:
    """Names, relative to audio/, of the files git tracks there.

    Read from the index, not the disk: jsDelivr serves only what git has, and
    a checkout that leaves audio/ out of the working tree (sparse checkout)
    still lists every path. -z stops git from octal-quoting non-ASCII names.
    """
    out = subprocess.run(
        ["git", "-C", str(repo), "ls-files", "-z", "--", "audio/"],
        capture_output=True,
        check=True,
    ).stdout.decode("utf-8")
    return {path.removeprefix("audio/") for path in out.split("\0") if path}


def renders_player(data: dict) -> bool:
    """Whether _layouts/default.html renders the audio player for this post.

    It does whenever page.audio is truthy in Liquid: anything but nil and
    false, so an empty string or 0 still renders it.
    """
    value = data.get("audio")
    return value is not None and value is not False


def audio_error(data: dict, tracked: set[str]) -> str | None:
    """Return the problem with a post's `audio:` value, or None if it plays.

    js/audio-player.js fetches audio/<value> from jsDelivr, which serves only
    what git tracks.
    """
    if not renders_player(data):
        return None
    value = data["audio"]
    # str() of a YAML date is the same text Jekyll renders for it.
    if str(value) in tracked:
        return None
    return f"audio/{value} is not tracked in git"


def repair(content: str) -> str | None:
    """Return the first repaired variant whose front matter parses, or None."""
    strategies = (
        fix_splice,
        fix_quiz,
        fix_preamble,
        fix_duplicate_front_matter,
        lambda c: fix_quiz(fix_splice(c)),
        lambda c: fix_duplicate_front_matter(fix_preamble(c)),
        lambda c: fix_quiz(fix_splice(fix_duplicate_front_matter(fix_preamble(c)))),
        fix_glued_header,
        lambda c: fix_quiz(fix_splice(fix_glued_header(c))),
    )
    for strategy in strategies:
        candidate = strategy(content)
        if candidate != content and parse_error(candidate) is None:
            return candidate
    return None


def fix_splice(content: str) -> str:
    def repair(m: re.Match) -> str:
        return f"{m.group('pre')}{m.group('post')}\npermalink: {m.group('plink')}"

    return SPLICE_RE.sub(repair, content)


def fix_preamble(content: str) -> str:
    """Strip leaked LLM commentary before the front matter opens."""
    if content.startswith("---"):
        return content
    idx = content.find("\n---\n")
    if idx != -1:
        return content[idx + 1:]
    return content


def fix_glued_header(content: str) -> str:
    """Recover when the real front matter's opening '---' is glued to the end
    of leaked text (e.g. '...final string.---\\nlayout: post')."""
    idx = content.find("---\nlayout: post\n", 1)
    if idx > 0:
        return content[idx:]
    return content


def fix_duplicate_front_matter(content: str) -> str:
    """Drop a corrupt leading front-matter block when a full one follows.

    Pattern: broken partial block, then a '---' line immediately followed by
    'layout: post' — i.e. the delimiter doubles as the opener of the good copy.
    """
    m = re.search(r"^---\s*\n(?=layout: post\n)", content, re.MULTILINE)
    if m and m.start() > 0:
        return content[m.start():]
    return content


def fix_quiz(content: str) -> str:
    m = FRONT_MATTER_RE.match(content)
    if m:
        fm = QUIZ_BLOCK_RE.sub("", m.group(0))
        return fm + content[m.end():]
    # Unclosed front matter: quiz truncation ate the delimiter. Strip the quiz
    # block and re-close before the body (body is unrecoverable in that case,
    # so only do this when a delimiter exists later on).
    return content


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="attempt auto-repair")
    args = ap.parse_args(argv)

    try:
        tracked = tracked_audio(REPO_ROOT)
    except (OSError, subprocess.CalledProcessError) as e:
        if isinstance(e, subprocess.CalledProcessError):
            detail = e.stderr.decode("utf-8", "replace").strip()
        else:
            detail = str(e)
        print(f"ERROR: git ls-files could not list the tracked audio files: {detail}")
        return 1

    posts = sorted(POSTS_DIR.glob("*.md"))
    broken: list[tuple[Path, str]] = []
    fixed: list[Path] = []
    unfixable: list[tuple[Path, str]] = []
    dangling: list[tuple[Path, str]] = []
    audio_count = 0

    for path in posts:
        content = path.read_text(encoding="utf-8")
        data, err = load_front_matter(content)
        if err:
            broken.append((path, err))
            if args.fix:
                repaired = repair(content)
                if repaired is None:
                    unfixable.append((path, err))
                else:
                    path.write_text(repaired, encoding="utf-8")
                    fixed.append(path)
                    data, _ = load_front_matter(repaired)
        if data is None:
            continue
        audio_count += renders_player(data)
        problem = audio_error(data, tracked)
        if problem:
            dangling.append((path, problem))

    status = 0
    if not broken:
        print(f"OK: all {len(posts)} posts have valid front matter")
    elif args.fix:
        for p in fixed:
            print(f"FIXED: {p.name}")
        for p, err in unfixable:
            print(f"UNFIXABLE: {p.name} — {err}")
        status = 1 if unfixable else 0
    else:
        for p, err in broken:
            print(f"BROKEN: {p.name} — {err}")
        print(f"\n{len(broken)} post(s) with invalid front matter. Run with --fix to repair.")
        status = 1

    if not dangling:
        print(f"OK: {audio_count} audio: values, each naming a file git tracks under audio/")
        return status
    for p, problem in dangling:
        print(f"DANGLING AUDIO: {p.name} — {problem}")
    print(
        f"\n{len(dangling)} post(s) name an audio file git does not track; their "
        "player would 404 on jsDelivr. Commit the mp3 or remove the audio: line."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
