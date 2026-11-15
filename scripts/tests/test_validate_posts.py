"""Dangling audio: contract for scripts/validate_posts.py.

_layouts/default.html renders the audio player whenever page.audio is set,
and js/audio-player.js loads audio/<value> from jsDelivr's mirror of this
repo. When git does not track that mp3 the request 404s and the play button
silently does nothing. On 2026-11-15, 656 posts (655 en, 1 ko, all dated
2026-04..07) were in that state: the publisher wrote `audio:` into the post
but left the mp3 uncommitted (fixed in mindtickle-studio b54972c).

CI runs validate_posts.py before the Jekyll build, so the check fails the
build instead of shipping a dead player. It reads the tracked set from git's
index (`git ls-files`), not from the disk: the build job's checkout leaves
audio/ (4 GB) out of the working tree with a sparse checkout. If an
assertion here breaks, that guard is void.

Run from the repo root with PyYAML installed:
    python3 -m unittest scripts.tests.test_validate_posts
"""
from __future__ import annotations

import contextlib
import io
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

from scripts import validate_posts


def _git(repo: Path, *args: str) -> None:
    subprocess.run(
        ["git", "-C", str(repo), "-c", "user.name=test", "-c", "user.email=test@example.invalid", *args],
        check=True,
        capture_output=True,
    )


def _write(repo: Path, relative: str, text: str = "") -> None:
    path = repo / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _post(audio_line: str | None) -> str:
    lines = ["---", "layout: post", 'title: "T"']
    if audio_line is not None:
        lines.append(audio_line)
    return "\n".join(lines + ["---", "body", ""])


def _front_matter(text: str) -> dict:
    data, err = validate_posts.load_front_matter(text)
    assert err is None, err
    return data


class TrackedAudioTest(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.repo = Path(self._tmp.name)
        _git(self.repo, "init", "-q")

    def tearDown(self):
        self._tmp.cleanup()

    def test_reads_the_index_not_the_disk(self):
        """An mp3 that exists locally but was never committed is exactly what
        the publisher left behind; jsDelivr serves only what git has."""
        _write(self.repo, "audio/kept.mp3", "id3")
        _git(self.repo, "add", "audio/kept.mp3")
        _git(self.repo, "commit", "-qm", "add")
        _write(self.repo, "audio/stray.mp3", "id3")

        self.assertEqual(validate_posts.tracked_audio(self.repo), {"kept.mp3"})

    def test_survives_the_build_checkout_without_audio(self):
        """The patterns the build job's Checkout step uses (jekyll.yml)."""
        _write(self.repo, "audio/kept.mp3", "id3")
        _write(self.repo, "_posts/2026-01-01-a.md", _post("audio: kept.mp3"))
        _git(self.repo, "add", ".")
        _git(self.repo, "commit", "-qm", "add")
        _git(self.repo, "sparse-checkout", "set", "--no-cone", "/*", "!/audio/")
        # The simulation only proves something if audio/ really left the disk.
        self.assertFalse((self.repo / "audio/kept.mp3").exists())

        self.assertEqual(validate_posts.tracked_audio(self.repo), {"kept.mp3"})

    def test_keeps_non_ascii_names_unquoted(self):
        """Without -z, git octal-escapes non-ASCII paths (core.quotepath) and a
        Korean-slug mp3 would never match its post."""
        _git(self.repo, "config", "core.quotepath", "true")  # git's default
        name = "2026-06-05-환율-1550원.mp3"
        _write(self.repo, f"audio/{name}", "id3")
        _git(self.repo, "add", ".")
        _git(self.repo, "commit", "-qm", "add")

        self.assertEqual(validate_posts.tracked_audio(self.repo), {name})


class AudioErrorTest(unittest.TestCase):
    TRACKED = {"2026-04-13-a.en.mp3"}

    def problem(self, audio_line: str | None) -> str | None:
        return validate_posts.audio_error(_front_matter(_post(audio_line)), self.TRACKED)

    def test_accepts_a_tracked_file(self):
        self.assertIsNone(self.problem("audio: 2026-04-13-a.en.mp3"))
        self.assertIsNone(self.problem('audio: "2026-04-13-a.en.mp3"'))

    def test_accepts_values_that_render_no_player(self):
        """Liquid treats only nil and false as false, so these hide the player."""
        self.assertIsNone(self.problem(None))
        self.assertIsNone(self.problem("audio:"))
        self.assertIsNone(self.problem("audio: null"))
        self.assertIsNone(self.problem("audio: false"))

    def test_rejects_a_file_git_does_not_track(self):
        """What the 655 en posts did: each named its own <stem>.en.mp3, which
        was generated but never committed."""
        problem = self.problem("audio: 2026-04-20-a.en.mp3")
        self.assertIsNotNone(problem)
        self.assertIn("audio/2026-04-20-a.en.mp3", problem)

    def test_rejects_a_value_cut_down_to_a_date(self):
        """A value cut to its date prefix (how the permalink-splice bug
        mangled Korean-slug names, 925669a5) loads as a YAML date, not a str."""
        problem = self.problem("audio: 2026-05-20")
        self.assertIsNotNone(problem)
        self.assertIn("audio/2026-05-20", problem)

    def test_rejects_an_empty_string(self):
        """'' is truthy in Liquid: the player renders and requests audio/."""
        self.assertIsNotNone(self.problem('audio: ""'))


class MainTest(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.repo = Path(self._tmp.name)
        _git(self.repo, "init", "-q")
        _write(self.repo, "audio/2026-01-01-a.mp3", "id3")
        _write(self.repo, "_posts/2026-01-01-a.md", _post("audio: 2026-01-01-a.mp3"))
        _write(self.repo, "_posts/2026-01-01-a.en.md", _post(None))
        _git(self.repo, "add", ".")
        _git(self.repo, "commit", "-qm", "add")

    def tearDown(self):
        self._tmp.cleanup()

    def run_main(self, *argv: str) -> tuple[int, str]:
        out = io.StringIO()
        with mock.patch.object(validate_posts, "REPO_ROOT", self.repo), \
                mock.patch.object(validate_posts, "POSTS_DIR", self.repo / "_posts"), \
                contextlib.redirect_stdout(out):
            code = validate_posts.main(list(argv))
        return code, out.getvalue()

    def test_passes_when_every_audio_is_tracked(self):
        code, out = self.run_main()
        self.assertEqual(code, 0, out)
        self.assertIn("1 audio", out)

    def test_fails_on_a_post_whose_mp3_is_not_tracked(self):
        _write(self.repo, "_posts/2026-01-01-a.en.md", _post("audio: 2026-01-01-a.en.mp3"))
        _write(self.repo, "audio/2026-01-01-a.en.mp3", "uncommitted")

        code, out = self.run_main()
        self.assertEqual(code, 1, out)
        self.assertIn("2026-01-01-a.en.md", out)
        self.assertIn("audio/2026-01-01-a.en.mp3", out)
        self.assertNotIn("2026-01-01-a.md ", out)

    def test_fix_leaves_dangling_audio_failing(self):
        """--fix repairs YAML only. Deleting the line would hide a publisher
        that stopped committing mp3s, so the post stays red."""
        post = self.repo / "_posts/2026-01-01-a.en.md"
        post.write_text(_post("audio: 2026-01-01-a.en.mp3"), encoding="utf-8")
        before = post.read_text(encoding="utf-8")

        code, out = self.run_main("--fix")
        self.assertEqual(code, 1, out)
        self.assertEqual(post.read_text(encoding="utf-8"), before)

    def test_fails_loudly_when_git_cannot_list_audio(self):
        """No git index means no answer, never a silent pass."""
        with TemporaryDirectory() as not_a_repo:
            not_a_repo = Path(not_a_repo)
            _write(not_a_repo, "_posts/2026-01-01-a.md", _post("audio: 2026-01-01-a.mp3"))
            self.repo = not_a_repo
            code, out = self.run_main()
        self.assertEqual(code, 1, out)
        self.assertIn("git ls-files", out)


if __name__ == "__main__":
    unittest.main()
