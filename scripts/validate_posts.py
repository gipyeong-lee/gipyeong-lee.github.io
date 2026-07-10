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
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

POSTS_DIR = Path(__file__).resolve().parent.parent / "_posts"

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
SPLICE_RE = re.compile(
    r"^(?P<pre>[A-Za-z_]+: \S*?)permalink: (?P<plink>/\S+/)\s*\n(?P<post>\S+)$",
    re.MULTILINE,
)
QUIZ_BLOCK_RE = re.compile(
    r"^quiz:\s*\n(?:^(?:[ \t]+\S.*)?\n?)*", re.MULTILINE
)


def parse_error(content: str) -> str | None:
    """Return a description of the front-matter problem, or None if valid."""
    m = FRONT_MATTER_RE.match(content)
    if not m:
        return "no closed front matter block"
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return f"invalid YAML: {str(e).splitlines()[0]}"
    if not isinstance(data, dict):
        return "front matter is not a mapping"
    for key, value in data.items():
        if isinstance(value, str) and re.search(r"\b(permalink|image):", value):
            return f"spliced field inside '{key}'"
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="attempt auto-repair")
    args = ap.parse_args()

    broken: list[tuple[Path, str]] = []
    fixed: list[Path] = []
    unfixable: list[tuple[Path, str]] = []

    for path in sorted(POSTS_DIR.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        err = parse_error(content)
        if not err:
            continue
        broken.append((path, err))

        if not args.fix:
            continue

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
                path.write_text(candidate, encoding="utf-8")
                fixed.append(path)
                break
        else:
            unfixable.append((path, err))

    if not broken:
        print(f"OK: all {len(list(POSTS_DIR.glob('*.md')))} posts have valid front matter")
        return 0

    if args.fix:
        for p in fixed:
            print(f"FIXED: {p.name}")
        for p, err in unfixable:
            print(f"UNFIXABLE: {p.name} — {err}")
        return 1 if unfixable else 0

    for p, err in broken:
        print(f"BROKEN: {p.name} — {err}")
    print(f"\n{len(broken)} post(s) with invalid front matter. Run with --fix to repair.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
