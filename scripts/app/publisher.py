"""Git publisher.

Stages the post + image files, creates a commit, and (optionally) pushes
to origin/main. Safety guardrails:

- Only stage files we generated this run (explicit list, never `git add .`).
- Never use `--no-verify` → pre-commit hooks run normally.
- On push failure: one `git pull --rebase` + retry. If rebase fails,
  leave the local commit in place (do NOT revert) and return error so
  the daemon can surface it on the dashboard.
"""
from __future__ import annotations

import logging
import subprocess
from pathlib import Path
from typing import Iterable

from .config import REPO_ROOT
from .schemas import PipelineResult

log = logging.getLogger("aiblog.publisher")


class PublishError(Exception):
    pass


def _run(cmd: list[str], check: bool = True) -> str:
    """Run a git command inside the repo root, return stdout."""
    proc = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if check and proc.returncode != 0:
        raise PublishError(
            f"{' '.join(cmd)} failed ({proc.returncode}): {proc.stderr.strip()}"
        )
    return (proc.stdout or "").strip()


def _build_commit_message(result: PipelineResult) -> str:
    title = result.title_ko or result.slug or "auto post"
    langs = ",".join(result.languages) if result.languages else "ko"
    lines = [
        f"post: {title}",
        "",
        "Auto-published by AI blog daemon.",
        f"Slug: {result.slug}",
        f"Source: {result.source or 'unknown'}",
        f"Languages: {langs}",
        f"Fact-check revisions: {result.revision_count}",
        f"Run ID: {result.run_id}",
    ]
    return "\n".join(lines)


def _verify_only_expected(files: Iterable[str]) -> None:
    """Sanity check: `git status --porcelain` should only show our files."""
    expected = {str(Path(f).as_posix()) for f in files}
    out = _run(["git", "status", "--porcelain"], check=True)
    dirty: set[str] = set()
    for line in out.splitlines():
        # porcelain v1: two status chars + space + path
        if len(line) < 4:
            continue
        path = line[3:].strip()
        # handle renames "old -> new"
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        dirty.add(Path(path).as_posix())
    unexpected = dirty - expected
    if unexpected:
        # not fatal — we just warn and continue; the user may have
        # other in-progress edits. We still only add the expected files.
        log.warning("publisher: extra dirty paths ignored: %s", unexpected)


def publish(result: PipelineResult, push: bool = True) -> str:
    """Stage, commit, optionally push. Returns the commit SHA."""
    if not result.success or not result.files:
        raise PublishError("nothing to publish (result.success=False or no files)")

    files: list[str] = [f"_posts/{f}" for f in result.files]
    if result.image_file:
        files.append(f"images/{result.image_file}")

    # Ensure files exist before staging (safety)
    for f in files:
        if not (REPO_ROOT / f).exists():
            raise PublishError(f"expected file missing: {f}")

    _verify_only_expected(files)

    _run(["git", "add", *files])

    # Nothing staged? (could happen if files were already committed)
    diff_cached = _run(["git", "diff", "--cached", "--name-only"], check=True)
    if not diff_cached:
        raise PublishError("no staged changes after git add")

    msg = _build_commit_message(result)
    _run(["git", "commit", "-m", msg])

    sha = _run(["git", "rev-parse", "HEAD"], check=True)

    if push:
        try:
            _run(["git", "push", "origin", "main"])
        except PublishError as e:
            log.warning("push failed, retrying with rebase: %s", e)
            _run(["git", "fetch", "origin", "main"], check=True)
            try:
                _run(["git", "pull", "--rebase", "origin", "main"], check=True)
                _run(["git", "push", "origin", "main"], check=True)
            except PublishError as e2:
                raise PublishError(
                    f"push failed after rebase: {e2}. Commit {sha} is local."
                ) from e2

    return sha
