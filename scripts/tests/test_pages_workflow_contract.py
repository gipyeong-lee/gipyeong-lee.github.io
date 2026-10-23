"""Pages build workflow contract.

The build job installs Gemfile.lock with ruby/setup-ruby on a hosted runner.
When ubuntu-latest moved to ubuntu-26.04, every deploy from 2026-10-21 19:52Z
failed: setup-ruby had no Ruby 3.2.0 build for 26.04 (ruby-builder builds
only the newest patch of each series for new images), and google-protobuf
3.21.12, compiled from source with -std=gnu99, died on `bool` inside the
headers of the Ruby 3.2.x built there with GCC 15 (no HAVE_STDBOOL_H under
C23).

The job now runs Ruby 4.0 (the series of the local Homebrew Ruby) on
ubuntu-26.04, and Gemfile.lock carries x86_64-linux-gnu builds of
google-protobuf, sass-embedded, nokogiri and ffi, so the runner's compiler
only builds small extensions (bigdecimal, eventmachine, http_parser.rb,
prism, racc). Those precompiled builds cover Ruby up to 4.0 (google-protobuf
4.36.2: >= 3.2, < 4.1.dev); Ruby 4.1 needs a lockfile update first.
Verified 2026-10-23 with a cold deployment-mode `bundle install` and
`jekyll build` in an amd64 ubuntu:26.04 container (ruby-builder 4.0.8) and
on the runner. If an assertion here breaks, that conclusion is void.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = (ROOT / ".github/workflows/jekyll.yml").read_text(encoding="utf-8")
LOCKFILE = (ROOT / "Gemfile.lock").read_text(encoding="utf-8")

# Native gems whose source builds are slow or compiler-sensitive; the
# google-protobuf one is what broke on 26.04.
PRECOMPILED_ON_RUNNER = ("google-protobuf", "sass-embedded", "nokogiri", "ffi")


def _job(name: str) -> str:
    """Text of one job under `jobs:`, up to the next 2-space-indented line."""
    match = re.search(rf"^  {name}:\n(.*?)(?=^  \S|\Z)", WORKFLOW, re.M | re.S)
    if match is None:
        raise AssertionError(f"job {name!r} not found in jekyll.yml")
    return match.group(1)


def _locked_platforms(gem: str) -> set[str]:
    """Platforms `gem` is locked for under GEM specs ("ruby" = source gem)."""
    versions = re.findall(rf"^    {re.escape(gem)} \(([^)]+)\)$", LOCKFILE, re.M)
    return {version.partition("-")[2] or "ruby" for version in versions}


class PagesWorkflowContractTest(unittest.TestCase):
    def test_build_job_pins_a_runner_image(self):
        """A floating label swaps the toolchain under the lockfile without a
        commit; moving image must be a deliberate, re-verified change."""
        runs_on = re.search(r"^    runs-on:\s*(\S+)", _job("build"), re.M)
        self.assertIsNotNone(runs_on, "build job lost its runs-on")
        self.assertRegex(runs_on.group(1), r"^ubuntu-\d+\.\d+$")

    def test_build_job_requests_a_ruby_series_not_a_patch(self):
        """An exact patch can vanish on the next image (3.2.0 had no 26.04
        build); a series resolves to the newest patch, which ruby-builder
        does build for new images."""
        version = re.search(r"^\s+ruby-version:\s*['\"]?([^'\"\s]+)", _job("build"), re.M)
        self.assertIsNotNone(version, "build job lost its ruby-version")
        self.assertRegex(version.group(1), r"^\d+\.\d+$")

    def test_compiler_sensitive_gems_are_locked_precompiled_for_the_runner(self):
        """Locked x86_64-linux-gnu builds install without compiling, so a new
        image's compiler (GCC 15/C23 on 26.04) cannot break them."""
        platforms = re.search(r"^PLATFORMS\n((?:  \S+\n)+)", LOCKFILE, re.M)
        self.assertIsNotNone(platforms, "Gemfile.lock lost its PLATFORMS")
        self.assertIn("x86_64-linux", platforms.group(1).split())
        for gem in PRECOMPILED_ON_RUNNER:
            with self.subTest(gem=gem):
                self.assertIn("x86_64-linux-gnu", _locked_platforms(gem))


if __name__ == "__main__":
    unittest.main()
