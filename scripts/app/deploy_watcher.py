"""Deploy watcher — autonomous GitHub Pages deploy failure recovery.

Runs as an asyncio task inside the daemon process, alongside the blog
scheduler and the video worker. Every tick, it asks `gh` for the most
recent workflow runs on the main branch, looks for failures we haven't
already recorded, fetches the failing job's log, classifies the error,
and (when the category has an auto-fix handler) applies the fix, stages
the modified files, and pushes a commit. GitHub then retriggers the
deploy on its own, closing the loop.

Design notes
------------

- **Polling over webhooks**: we don't expose the admin UI to the public
  internet, so a webhook receiver isn't feasible. `gh run list` is
  cheap and already authenticated on this machine.
- **Idempotency**: every GH run id goes into `deploy_incidents` exactly
  once (`UNIQUE` constraint on gh_run_id). If the watcher restarts, it
  won't re-fix already-handled incidents.
- **Safety**: we refuse to auto-fix if the previous commit on main is
  ALREADY one of our auto-fix commits. That prevents a runaway
  fix→fail→fix loop when our repair is wrong.
- **Failure isolation**: any exception in the watcher is logged and
  swallowed — it never takes down the blog or video pipelines.
"""
from __future__ import annotations

import asyncio
import json
import logging
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from sqlalchemy import select

from .config import REPO_ROOT
from .db import session_scope
from .diagnostics import DeployDiagnosis, classify_deploy_error
from .models_db import DeployIncident

log = logging.getLogger("aiblog.deploy_watcher")

# Loop tick — 2 min is frequent enough to catch failures quickly without
# hammering the GitHub API (well under the 5,000/hr authenticated limit).
_DEPLOY_TICK_SECONDS = 120

# Marker put in the commit message for our auto-fix commits so the watcher
# can recognize and refuse to stack fixes on top of its own previous fix.
_AUTO_FIX_MARKER = "[deploy-auto]"

_stop_event = asyncio.Event()
_state: dict[str, Any] = {
    "running": False,
    "last_tick_at": None,
    "last_incident_id": None,
}


def stop() -> None:
    _stop_event.set()


def reset_stop() -> None:
    _stop_event.clear()


def is_running() -> bool:
    return _state["running"]


# ----------------------------------------------------------------------
# Main loop
# ----------------------------------------------------------------------


async def deploy_watcher_loop() -> None:
    """Poll GH Actions and self-heal known deploy failure categories."""
    log.info("deploy_watcher_loop starting")
    _state["running"] = True
    reset_stop()
    try:
        while not _stop_event.is_set():
            try:
                await _tick()
            except Exception:
                log.exception("deploy_watcher tick failed")
            try:
                await asyncio.wait_for(
                    _stop_event.wait(), timeout=_DEPLOY_TICK_SECONDS
                )
            except asyncio.TimeoutError:
                pass
    finally:
        _state["running"] = False
        log.info("deploy_watcher_loop stopped")


async def _tick() -> None:
    _state["last_tick_at"] = datetime.now(timezone.utc)

    failed = await asyncio.to_thread(_fetch_latest_failed_run)
    if failed is None:
        return

    gh_run_id = str(failed.get("databaseId") or failed.get("id") or "")
    if not gh_run_id:
        return

    if _already_recorded(gh_run_id):
        return

    log.info(f"new deploy failure detected: gh_run_id={gh_run_id}")
    log_text = await asyncio.to_thread(_fetch_failed_logs, gh_run_id)
    diagnosis = classify_deploy_error(log_text or "")

    # Record the incident immediately (even before trying to fix) so a
    # subsequent tick won't re-attempt. We update the row after the fix.
    incident_id = _record_incident(gh_run_id, failed, diagnosis, log_text)

    if not diagnosis.auto_apply or not diagnosis.fix_fn:
        log.info(
            f"incident {incident_id}: category={diagnosis.category} "
            "— no auto-fix; leaving for manual review"
        )
        return

    if _latest_commit_is_auto_fix():
        log.warning(
            f"incident {incident_id}: previous commit is already an auto-fix, "
            "refusing to stack another auto-fix on top (loop guard)"
        )
        _update_incident_fix_error(
            incident_id,
            "auto-fix loop guard: previous commit already [deploy-auto]",
        )
        return

    ok, detail, modified_file = await asyncio.to_thread(
        _run_fix, diagnosis.fix_fn, diagnosis.fix_params
    )
    if not ok:
        log.warning(f"incident {incident_id}: auto-fix failed: {detail}")
        _update_incident_fix_error(incident_id, detail)
        return

    pushed, commit_sha, push_detail = await asyncio.to_thread(
        _commit_and_push_fix, diagnosis.category, detail, modified_file or ""
    )
    if not pushed:
        log.warning(f"incident {incident_id}: git push failed: {push_detail}")
        _update_incident_fix_error(incident_id, f"push failed: {push_detail}")
        return

    log.info(
        f"incident {incident_id}: auto-fix committed as {commit_sha}, "
        "GitHub will re-run the workflow"
    )
    _mark_incident_applied(incident_id, commit_sha, detail)


# ----------------------------------------------------------------------
# gh / git shell helpers (sync — called via asyncio.to_thread)
# ----------------------------------------------------------------------


def _fetch_latest_failed_run() -> Optional[dict]:
    """Return the most recent failed workflow run (or None)."""
    try:
        out = subprocess.run(
            [
                "gh", "run", "list",
                "--branch", "main",
                "--workflow", "jekyll.yml",
                "--status", "failure",
                "--limit", "1",
                "--json", "databaseId,headSha,displayTitle,createdAt,updatedAt,url,workflowName,conclusion",
            ],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=30,
        )
    except Exception as e:
        log.warning(f"gh run list failed: {e}")
        return None
    if out.returncode != 0:
        log.warning(f"gh run list exit={out.returncode} stderr={out.stderr[:200]}")
        return None
    try:
        rows = json.loads(out.stdout or "[]")
    except json.JSONDecodeError:
        return None
    return rows[0] if rows else None


def _fetch_failed_logs(gh_run_id: str) -> Optional[str]:
    """Return the `--log-failed` output for the given run id."""
    try:
        out = subprocess.run(
            ["gh", "run", "view", gh_run_id, "--log-failed"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=60,
        )
    except Exception as e:
        log.warning(f"gh run view failed: {e}")
        return None
    if out.returncode != 0:
        log.warning(
            f"gh run view exit={out.returncode} stderr={out.stderr[:200]}"
        )
        return None
    return out.stdout or ""


def _run_fix(fix_fn: str, fix_params: dict) -> tuple[bool, str, Optional[str]]:
    """Invoke the deploy_fixer dispatcher. Returns (ok, detail, modified_file)."""
    try:
        from ..agents.deploy_fixer import DeployFixerAgent
    except Exception as e:
        return False, f"failed to import deploy_fixer: {e}", None

    agent = DeployFixerAgent()
    result = agent.dispatch(fix_fn, fix_params)
    return result.ok, result.detail, result.modified_file


def _commit_and_push_fix(
    category: str, detail: str, modified_file: str
) -> tuple[bool, str, str]:
    """Stage the modified file + push. Returns (ok, commit_sha, message)."""
    if not modified_file:
        return False, "", "no file to commit"

    msg = f"{_AUTO_FIX_MARKER} fix({category}): {detail[:120]}"

    try:
        # Stage only the specific file (no wildcard globs).
        add = subprocess.run(
            ["git", "add", modified_file],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=30,
        )
        if add.returncode != 0:
            return False, "", f"git add failed: {add.stderr[:200]}"

        # Check there's actually a diff staged.
        diff = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=30,
        )
        # --quiet exit 0 means NO diff, exit 1 means diff present.
        if diff.returncode == 0:
            return False, "", "no staged changes after git add"

        commit = subprocess.run(
            ["git", "commit", "-m", msg],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=60,
        )
        if commit.returncode != 0:
            return False, "", f"git commit failed: {commit.stderr[:200]}"

        sha = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=30,
        ).stdout.strip()

        push = subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=120,
        )
        if push.returncode != 0:
            return False, sha, f"git push failed: {push.stderr[:200]}"

        return True, sha, "pushed"
    except Exception as e:
        return False, "", f"commit/push crashed: {e}"


def _latest_commit_is_auto_fix() -> bool:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=10,
        )
    except Exception:
        return False
    if out.returncode != 0:
        return False
    return _AUTO_FIX_MARKER in (out.stdout or "")


# ----------------------------------------------------------------------
# DB helpers
# ----------------------------------------------------------------------


def _already_recorded(gh_run_id: str) -> bool:
    with session_scope() as s:
        existing = s.execute(
            select(DeployIncident.id).where(DeployIncident.gh_run_id == gh_run_id)
        ).scalar_one_or_none()
        return existing is not None


def _record_incident(
    gh_run_id: str,
    run_meta: dict,
    diagnosis: DeployDiagnosis,
    log_text: Optional[str],
) -> int:
    """Insert a new DeployIncident row. Returns the new id."""
    started = _parse_iso(run_meta.get("createdAt"))
    ended = _parse_iso(run_meta.get("updatedAt"))
    evidence_blob = json.dumps(
        {
            "title": run_meta.get("displayTitle"),
            "url": run_meta.get("url"),
            "head_sha": run_meta.get("headSha"),
            "diagnosis_evidence": diagnosis.evidence,
            "log_tail": (log_text or "")[-1500:],
        },
        default=str,
    )
    with session_scope() as s:
        row = DeployIncident(
            gh_run_id=gh_run_id,
            workflow_name=run_meta.get("workflowName"),
            branch="main",
            commit_sha=run_meta.get("headSha"),
            started_at=started,
            ended_at=ended,
            category=diagnosis.category,
            root_cause=diagnosis.root_cause[:4000],
            evidence=evidence_blob,
            suggested_fix=diagnosis.suggested_fix[:4000],
            auto_applied=0,
        )
        s.add(row)
        s.flush()
        _state["last_incident_id"] = row.id
        return row.id


def _mark_incident_applied(incident_id: int, commit_sha: str, detail: str) -> None:
    with session_scope() as s:
        row = s.get(DeployIncident, incident_id)
        if row is None:
            return
        row.auto_applied = 1
        row.applied_at = datetime.utcnow()
        row.fix_commit_sha = commit_sha
        row.suggested_fix = (
            (row.suggested_fix or "") + f"\n[applied] {detail[:400]}"
        )[:4000]
        row.fix_error = None


def _update_incident_fix_error(incident_id: int, error: str) -> None:
    with session_scope() as s:
        row = s.get(DeployIncident, incident_id)
        if row is None:
            return
        row.fix_error = (error or "")[:2000]


def _parse_iso(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    try:
        # gh emits RFC3339 with Z suffix; convert to naive UTC.
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        dt = datetime.fromisoformat(value)
        if dt.tzinfo is not None:
            dt = dt.astimezone(timezone.utc).replace(tzinfo=None)
        return dt
    except Exception:
        return None
