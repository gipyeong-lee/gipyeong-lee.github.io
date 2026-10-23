"""Pages build workflow contract.

The build job's Ruby/native-gem stack (Ruby 3.2.0 + google-protobuf
3.21.12 compiled from source, see Gemfile.lock) installs on ubuntu-24.04
only. When ubuntu-latest moved to ubuntu-26.04 (from 2026-10-19), every
deploy from 2026-10-21 19:52Z failed: setup-ruby has no 3.2.0 build for
26.04 (ruby-builder 404), and the Ruby 3.2.x built there lacks
HAVE_STDBOOL_H, so protobuf's -std=gnu99 compile dies on `bool` inside
Ruby's own headers. If an assertion here breaks, that conclusion is void.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = (ROOT / ".github/workflows/jekyll.yml").read_text(encoding="utf-8")


def _job(name: str) -> str:
    """Text of one job under `jobs:`, up to the next 2-space-indented line."""
    match = re.search(rf"^  {name}:\n(.*?)(?=^  \S|\Z)", WORKFLOW, re.M | re.S)
    if match is None:
        raise AssertionError(f"job {name!r} not found in jekyll.yml")
    return match.group(1)


class PagesWorkflowContractTest(unittest.TestCase):
    def test_build_job_pins_a_runner_image(self):
        """A floating label swaps the toolchain under the lockfile without a
        commit; moving image must be a deliberate, re-verified change."""
        runs_on = re.search(r"^    runs-on:\s*(\S+)", _job("build"), re.M)
        self.assertIsNotNone(runs_on, "build job lost its runs-on")
        self.assertRegex(runs_on.group(1), r"^ubuntu-\d+\.\d+$")


if __name__ == "__main__":
    unittest.main()
