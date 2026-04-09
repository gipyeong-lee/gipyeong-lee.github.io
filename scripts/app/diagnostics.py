"""Failure diagnosis + auto-healing agent.

This module implements a rule-based agent that:
  1. Reads a failed `runs` row and its associated `logs` entries.
  2. Classifies the root cause into one of several categories.
  3. Writes a `diagnoses` row with root cause + suggested fix.
  4. Optionally applies safe automatic fixes (block a bad topic, reset a
     transient failure back to the queue, disable a repeatedly-failing source).

The design is deliberately NOT an LLM agent — it's rule-based because:
  - We already know the pipeline's stage boundaries and possible errors.
  - LLM diagnosis adds latency + cost + unpredictability.
  - Each rule is testable and auditable.

Future enhancement: add an LLM "explanation" layer on top that takes the
structured diagnosis and writes it up in natural language for the admin UI.
"""
from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Optional

from sqlalchemy import desc, select

from .db import session_scope
from .models_db import Diagnosis, LogEntry, Run, SourceState, Topic
from .settings_store import get_settings, set_setting

log = logging.getLogger("aiblog.diagnostics")


# -- Result type ---------------------------------------------------------


@dataclass
class DiagnosisResult:
    category: str           # e.g. "fact_check_max_revisions"
    root_cause: str         # human-readable explanation
    evidence: dict[str, Any] = field(default_factory=dict)
    suggested_fix: str = ""
    auto_apply: bool = False
    fix_fn: Optional[str] = None   # name of method on this module to apply


# -- Diagnosis rules -----------------------------------------------------


def _load_run_context(run_id: int) -> Optional[dict]:
    """Pull the run row + its logs + the associated topic in one shot."""
    with session_scope() as s:
        r = s.get(Run, run_id)
        if r is None:
            return None
        logs = s.execute(
            select(LogEntry).where(LogEntry.run_id == run_id).order_by(LogEntry.ts.asc())
        ).scalars().all()
        topic = s.get(Topic, r.topic_id) if r.topic_id else None
        # expunge so we can safely read after session close
        s.expunge(r)
        if topic is not None:
            s.expunge(topic)
        log_dicts = [
            {
                "ts": l.ts,
                "level": l.level,
                "stage": l.stage,
                "message": l.message or "",
                "meta": json.loads(l.meta) if l.meta else {},
            }
            for l in logs
        ]
    return {"run": r, "topic": topic, "logs": log_dicts}


def _last_stage_end(logs: list[dict]) -> Optional[dict]:
    for l in reversed(logs):
        if "stage end" in (l["message"] or "").lower():
            return l
    return None


def _revision_logs(logs: list[dict]) -> list[dict]:
    return [l for l in logs if "revision round" in (l.get("message") or "").lower()]


def _aggregated_issues(logs: list[dict]) -> list[str]:
    """Collect all distinct issue strings from revision + stage_end meta."""
    seen: list[str] = []
    for l in logs:
        meta = l.get("meta") or {}
        for issue in (meta.get("issues") or []):
            issue = str(issue).strip()
            if issue and issue not in seen:
                seen.append(issue)
    return seen[:20]


def _dead_links(logs: list[dict]) -> list[str]:
    out: list[str] = []
    for l in logs:
        meta = l.get("meta") or {}
        for link in (meta.get("dead_links") or []):
            if link and link not in out:
                out.append(link)
    return out[:20]


def _classify(ctx: dict) -> DiagnosisResult:
    run: Run = ctx["run"]
    topic: Optional[Topic] = ctx["topic"]
    logs: list[dict] = ctx["logs"]

    error = (run.error or "").lower()
    stage_at_fail = run.stage or ""
    topic_title = (topic.title if topic else run.final_slug) or "unknown"

    # --- (1) fact-check: max revisions exceeded ---------------------------
    if error == "max_revisions":
        issues = _aggregated_issues(logs)
        dead = _dead_links(logs)
        rev_rounds = len(_revision_logs(logs))
        return DiagnosisResult(
            category="fact_check_max_revisions",
            root_cause=(
                f"Fact-checker could not validate the draft after {rev_rounds} "
                f"revision rounds. The researcher provided enough sources, but the "
                f"writer kept producing claims the fact-checker flagged as "
                f"unverified. This usually means (a) the topic is too niche for "
                f"reliable web sourcing, or (b) the researcher returned mostly "
                f"marketing pages rather than primary sources."
            ),
            evidence={
                "topic": topic_title,
                "revisions": rev_rounds,
                "issues": issues,
                "dead_links": dead,
            },
            suggested_fix=(
                "Block this topic (fail_count already exhausted) and let the "
                "scheduler pick a different topic next cycle."
            ),
            auto_apply=True,
            fix_fn="block_topic",
        )

    # --- (2) fact-check verdict FAIL (too many unverified claims) ---------
    if error == "fact_check_fail":
        issues = _aggregated_issues(logs)
        return DiagnosisResult(
            category="fact_check_verdict_fail",
            root_cause=(
                "Fact-checker returned FAIL on the first pass — the draft had "
                "too many unverified claims (>30%). Topic likely lacks enough "
                "primary sources on the open web."
            ),
            evidence={"topic": topic_title, "issues": issues},
            suggested_fix="Block topic.",
            auto_apply=True,
            fix_fn="block_topic",
        )

    # --- (3) research stage failed ---------------------------------------
    if error == "research_failed" or stage_at_fail == "research":
        return DiagnosisResult(
            category="research_failed",
            root_cause=(
                "Researcher could not find 5+ live sources for this topic. "
                "This is expected for very new announcements (no third-party "
                "coverage yet) or niche company product pages with no press."
            ),
            evidence={"topic": topic_title},
            suggested_fix="Block topic — insufficient web presence.",
            auto_apply=True,
            fix_fn="block_topic",
        )

    # --- (4) writer failed ------------------------------------------------
    if error in ("write_failed", "revision_failed"):
        # Look at recent write-stage failures to decide: transient or systemic?
        recent_write_fails = _count_recent_failures_by_error(["write_failed", "revision_failed"], limit=10)
        if recent_write_fails >= 3:
            return DiagnosisResult(
                category="writer_systemic",
                root_cause=(
                    f"Writer agent has failed {recent_write_fails} times recently. "
                    "This is likely a systemic issue: Gemini CLI auth expired, "
                    "quota exceeded, or a prompt formatting regression."
                ),
                evidence={"recent_failures": recent_write_fails},
                suggested_fix=(
                    "Check Gemini CLI authentication (`gemini` in a shell). "
                    "Review scripts/agents/writer.py. Pausing auto-publish is "
                    "recommended until resolved."
                ),
                auto_apply=False,  # no safe auto-fix
            )
        return DiagnosisResult(
            category="writer_transient",
            root_cause=(
                "Writer agent failed on this single draft — likely a transient "
                "Gemini CLI hiccup (retry should succeed)."
            ),
            evidence={"topic": topic_title, "recent_failures": recent_write_fails},
            suggested_fix="Reset topic to queued (one retry).",
            auto_apply=True,
            fix_fn="reset_topic_once",
        )

    # --- (5) editor failed ------------------------------------------------
    if error == "edit_failed":
        return DiagnosisResult(
            category="editor_failed",
            root_cause=(
                "Editor rejected the draft — usually because the final post "
                "was too short (<5000 chars) or the references section was "
                "missing/malformed after edit."
            ),
            evidence={"topic": topic_title},
            suggested_fix="Reset topic (one retry).",
            auto_apply=True,
            fix_fn="reset_topic_once",
        )

    # --- (6) pipeline timeout --------------------------------------------
    if "timeout" in error:
        return DiagnosisResult(
            category="pipeline_timeout",
            root_cause=(
                "Pipeline exceeded its wall-clock timeout. Most likely a hung "
                "Gemini CLI subprocess or very slow DDGS search."
            ),
            evidence={"topic": topic_title, "error": run.error},
            suggested_fix=(
                "Block this topic. If this recurs, increase pipeline_timeout_seconds "
                "in Settings or investigate Gemini CLI responsiveness."
            ),
            auto_apply=True,
            fix_fn="block_topic",
        )

    # --- (7) publish failed (git push etc.) ------------------------------
    if error.startswith("publish_failed"):
        return DiagnosisResult(
            category="publish_failed",
            root_cause=(
                "Pipeline produced a valid post but the git publisher failed "
                "during commit/push. Common causes: pre-commit hook rejection, "
                "remote rebase conflict, or authentication issue."
            ),
            evidence={"topic": topic_title, "error": run.error},
            suggested_fix=(
                "Check `git status`, resolve any conflicts, and re-run. "
                "The post files are already on disk — no regeneration needed."
            ),
            auto_apply=False,
        )

    # --- (8) process restart (recovered) ---------------------------------
    if "recovered" in error or "process restarted" in error:
        return DiagnosisResult(
            category="process_restarted",
            root_cause=(
                "This run was killed mid-execution by a process restart. "
                "Not a real failure — the topic is already back in the queue "
                "and will retry on the next scheduler tick."
            ),
            evidence={},
            suggested_fix="No action needed.",
            auto_apply=False,
        )

    # --- (9) unknown ------------------------------------------------------
    return DiagnosisResult(
        category="unknown",
        root_cause=(
            f"Run failed at stage '{stage_at_fail}' with error '{run.error}'. "
            f"No matching diagnostic rule — please inspect the live log."
        ),
        evidence={"stage": stage_at_fail, "error": run.error},
        suggested_fix="Manual review required.",
        auto_apply=False,
    )


def _count_recent_failures_by_error(errors: list[str], limit: int = 20) -> int:
    """Count how many of the last `limit` runs failed with one of these errors."""
    with session_scope() as s:
        rows = s.execute(
            select(Run).order_by(desc(Run.started_at)).limit(limit)
        ).scalars().all()
        return sum(
            1
            for r in rows
            if r.status == "failed" and any(e in (r.error or "") for e in errors)
        )


# -- Auto-fix actions ----------------------------------------------------


def _fix_block_topic(run: Run) -> str:
    if not run.topic_id:
        return "no topic to block"
    with session_scope() as s:
        t = s.get(Topic, run.topic_id)
        if t is None:
            return "topic not found"
        t.status = "blocked"
        t.last_error = (t.last_error or "") + " [diagnosis: auto-blocked]"
    return f"blocked topic #{run.topic_id}"


def _fix_reset_topic_once(run: Run) -> str:
    """Reset a topic to queued, but only if fail_count <= 1 (one retry total)."""
    if not run.topic_id:
        return "no topic to reset"
    with session_scope() as s:
        t = s.get(Topic, run.topic_id)
        if t is None:
            return "topic not found"
        if (t.fail_count or 0) > 1:
            t.status = "blocked"
            return f"exhausted retries, blocked #{run.topic_id}"
        t.status = "queued"
        t.selected_at = None
        t.last_error = (t.last_error or "") + " [diagnosis: retry scheduled]"
    return f"requeued topic #{run.topic_id} for one retry"


_FIX_DISPATCH = {
    "block_topic": _fix_block_topic,
    "reset_topic_once": _fix_reset_topic_once,
}


def _apply_fix(result: DiagnosisResult, run: Run) -> tuple[bool, str]:
    if not result.auto_apply or not result.fix_fn:
        return False, ""
    fn = _FIX_DISPATCH.get(result.fix_fn)
    if fn is None:
        return False, f"unknown fix_fn: {result.fix_fn}"
    try:
        detail = fn(run)
        return True, detail
    except Exception as e:
        log.exception("auto-fix crashed for run #%s: %s", run.id, e)
        return False, f"fix crashed: {e}"


# -- Public API: diagnose + sweep ---------------------------------------


def diagnose_run(run_id: int, apply_fix: bool = True) -> Optional[Diagnosis]:
    """Diagnose a single run. Idempotent — returns existing diagnosis if present."""
    with session_scope() as s:
        existing = s.execute(
            select(Diagnosis).where(Diagnosis.run_id == run_id)
        ).scalar_one_or_none()
        if existing is not None:
            s.expunge(existing)
            return existing

    ctx = _load_run_context(run_id)
    if ctx is None:
        log.warning("diagnose_run: run #%s not found", run_id)
        return None
    run: Run = ctx["run"]
    if run.status != "failed":
        log.debug("diagnose_run: run #%s status=%s, skipping", run_id, run.status)
        return None

    result = _classify(ctx)
    applied, fix_detail = (False, "")
    if apply_fix:
        applied, fix_detail = _apply_fix(result, run)

    with session_scope() as s:
        diag = Diagnosis(
            run_id=run_id,
            category=result.category,
            root_cause=result.root_cause,
            evidence=json.dumps(result.evidence, default=str),
            suggested_fix=(
                (result.suggested_fix or "")
                + (f"\n[applied] {fix_detail}" if applied and fix_detail else "")
            ),
            auto_applied=1 if applied else 0,
            applied_at=datetime.now(timezone.utc) if applied else None,
        )
        s.add(diag)
        s.flush()
        s.expunge(diag)

    log.info(
        "diagnosed run #%s: %s (auto_applied=%s detail=%s)",
        run_id,
        result.category,
        applied,
        fix_detail,
    )
    return diag


# ------------------------------------------------------------------
# Video pipeline error classification (Phase E)
# ------------------------------------------------------------------

# Categories for failures from scripts/app/video_worker.py. These are
# returned as lightweight strings (not Diagnosis rows) because the video
# pipeline has its own (video_runs) table and per-run logs are not dense
# enough to justify a full DiagnosisResult pass.

VIDEO_CATEGORIES = (
    "video_script_failed",
    "video_tts_failed",
    "video_compose_failed",
    "video_thumbnail_failed",
    "video_upload_quota",
    "video_oauth_expired",
    "video_upload_failed",
    "video_timeout",
    "video_unknown",
)

# Markers (case-insensitive) → category. First match wins, so more
# specific checks precede generic ones.
_VIDEO_ERROR_MARKERS: list[tuple[str, str]] = [
    ("pipeline timeout",            "video_timeout"),
    ("quotaexceeded",               "video_upload_quota"),
    ("quota exceeded",              "video_upload_quota"),
    ("daily upload",                "video_upload_quota"),
    ("invalid_grant",               "video_oauth_expired"),
    ("refresh token",               "video_oauth_expired"),
    ("oauth",                       "video_oauth_expired"),
    ("client_secrets",              "video_oauth_expired"),
    ("tts runner",                  "video_tts_failed"),
    ("melo",                        "video_tts_failed"),
    ("openvoice",                   "video_tts_failed"),
    ("no wav output",               "video_tts_failed"),
    ("tts crashed",                 "video_tts_failed"),
    ("compose crashed",             "video_compose_failed"),
    ("no mp4 output",               "video_compose_failed"),
    ("video render timed out",      "video_compose_failed"),
    ("moviepy",                     "video_compose_failed"),
    ("ffmpeg",                      "video_compose_failed"),
    ("thumbnail",                   "video_thumbnail_failed"),
    ("script writer returned empty", "video_script_failed"),
    ("post file not found",         "video_script_failed"),
    ("hero image not found",        "video_compose_failed"),
    ("upload returned none",        "video_upload_failed"),
    ("resumable upload",            "video_upload_failed"),
    ("videos().insert",             "video_upload_failed"),
]


def classify_video_error(error: Optional[str]) -> str:
    """Map a raw error string from the video pipeline into a category.

    Returns one of VIDEO_CATEGORIES. Used by `video_worker._finish_video_run`
    so the Admin UI + operators can see _why_ a video failed at a glance.

    Defaults to `video_unknown` when nothing matches. Never raises.
    """
    if not error:
        return "video_unknown"
    haystack = error.lower()
    for marker, category in _VIDEO_ERROR_MARKERS:
        if marker in haystack:
            return category
    return "video_unknown"


def video_category_should_block(category: str) -> bool:
    """Categories that should NOT be auto-retried by the worker.

    quota and oauth issues require human intervention (either waiting for
    midnight UTC or redoing the OAuth dance). Retrying them just eats
    quota on more failures.
    """
    return category in ("video_upload_quota", "video_oauth_expired")


# ------------------------------------------------------------------
# Deploy failure classification (GitHub Pages builds)
# ------------------------------------------------------------------
#
# Failure categories emitted by `scripts/app/deploy_watcher.py` after
# fetching the failing Actions run logs. Each category optionally has an
# auto-fix handler registered in `scripts/agents/deploy_fixer.py` — the
# watcher dispatches based on the category to decide if the failure is
# self-healable or needs human review.

DEPLOY_CATEGORIES = (
    "yaml_parse_error",         # Jekyll YAML front matter error
    "liquid_nil_method",        # Liquid template: undefined method X for nil
    "liquid_render_error",      # Other Liquid render error
    "bundle_install_failed",    # `bundle install` failed in CI
    "ruby_syntax_error",        # Ruby `syntax error, unexpected ...`
    "jekyll_build_failed",      # Jekyll exit != 0 with no specific signature
    "actions_infrastructure",   # Runner/network/tooling issue — not actionable
    "unknown_deploy_failure",
)


@dataclass
class DeployDiagnosis:
    """Lightweight classification result for a failing GH Actions deploy run."""

    category: str
    root_cause: str
    evidence: dict[str, Any] = field(default_factory=dict)
    suggested_fix: str = ""
    auto_apply: bool = False
    fix_fn: Optional[str] = None  # key into deploy_fixer dispatcher
    # Parameters passed to the fix handler — extracted from the log.
    fix_params: dict[str, Any] = field(default_factory=dict)


# Regex for the YAML exception Jekyll emits when a post's front matter is
# unterminated or otherwise malformed. Captures the full file path so the
# fixer knows which file to patch.
_YAML_EXC_RE = re.compile(
    r"YAML Exception reading\s+(?P<path>[^:]+):\s*(?P<detail>[^\n]+)"
)

# Liquid nil-method error: "undefined method `X' for nil:NilClass in FILE"
_LIQUID_NIL_RE = re.compile(
    r"Liquid Exception:\s*undefined method\s*[`']?(?P<method>\w+)[`']?"
    r"\s+for nil:NilClass\s+in\s+(?P<file>[^\s]+)"
)

# Ruby syntax error fallback.
_RUBY_SYNTAX_RE = re.compile(r"syntax error,\s*unexpected\s+(?P<token>[^\n]+)")


def classify_deploy_error(log_text: Optional[str]) -> DeployDiagnosis:
    """Classify a GitHub Actions deploy failure log into a category.

    Takes the raw `gh run view --log-failed` output (potentially very
    long) and returns a DeployDiagnosis. Picks the *most specific*
    actionable category it finds — if both a YAML error and a Liquid
    error are present (the Liquid usually cascades from the YAML), the
    YAML one is returned as the root cause.

    Returns a DeployDiagnosis with `category='unknown_deploy_failure'`
    when nothing matches. Never raises.
    """
    if not log_text:
        return DeployDiagnosis(
            category="unknown_deploy_failure",
            root_cause="No log content was captured for this failed run.",
            suggested_fix="Re-run the job manually and check GitHub Actions UI.",
        )

    # --- (1) YAML front matter error ------------------------------------
    yaml_match = _YAML_EXC_RE.search(log_text)
    if yaml_match:
        path = yaml_match.group("path").strip()
        detail = yaml_match.group("detail").strip()
        return DeployDiagnosis(
            category="yaml_parse_error",
            root_cause=(
                f"Jekyll failed to parse the YAML front matter of "
                f"`{path}`. Parser message: {detail}"
            ),
            evidence={"path": path, "detail": detail},
            suggested_fix=(
                "Likely an unterminated quoted string (the translator "
                "agent occasionally drops the closing \" on long titles). "
                "The deploy_fixer agent can auto-repair unterminated "
                "string fields in the front matter."
            ),
            auto_apply=True,
            fix_fn="fix_yaml_front_matter",
            fix_params={"path": path, "detail": detail},
        )

    # --- (2) Liquid nil method -----------------------------------------
    liquid_match = _LIQUID_NIL_RE.search(log_text)
    if liquid_match:
        method = liquid_match.group("method")
        file = liquid_match.group("file")
        return DeployDiagnosis(
            category="liquid_nil_method",
            root_cause=(
                f"Liquid template `{file}` called `{method}` on a nil "
                f"value. This almost always means a post has a missing "
                f"field that the template assumes exists (e.g. `post.tags` "
                f"on a translation post with `_strip_tags`)."
            ),
            evidence={"file": file, "method": method},
            suggested_fix=(
                f"Wrap the offending expression in `{{% if post.X %}}`. "
                f"Auto-fix is disabled because editing templates without "
                f"human review is risky."
            ),
            auto_apply=False,
        )

    # --- (3) bundle install --------------------------------------------
    if "Bundler::" in log_text or "Could not find gem" in log_text:
        return DeployDiagnosis(
            category="bundle_install_failed",
            root_cause=(
                "`bundle install` failed in CI. Usually a Gemfile.lock "
                "mismatch or upstream RubyGems outage."
            ),
            evidence={},
            suggested_fix=(
                "Run `bundle install` locally, commit the updated "
                "Gemfile.lock, and push. No safe auto-fix."
            ),
            auto_apply=False,
        )

    # --- (4) Ruby syntax error -----------------------------------------
    ruby_match = _RUBY_SYNTAX_RE.search(log_text)
    if ruby_match:
        return DeployDiagnosis(
            category="ruby_syntax_error",
            root_cause=(
                f"A Ruby file in the theme / plugins has a syntax error "
                f"near `{ruby_match.group('token')}`."
            ),
            evidence={"token": ruby_match.group("token")},
            suggested_fix="Manual Ruby fix required.",
            auto_apply=False,
        )

    # --- (5) Actions infrastructure ------------------------------------
    infra_markers = (
        "the runner has received a shutdown signal",
        "lost connection with the runner",
        "EAI_AGAIN",
        "dial tcp: lookup",
    )
    low = log_text.lower()
    if any(m.lower() in low for m in infra_markers):
        return DeployDiagnosis(
            category="actions_infrastructure",
            root_cause=(
                "GitHub-hosted runner infrastructure problem "
                "(network/shutdown/DNS). Not a repo issue."
            ),
            suggested_fix="Re-run the workflow. No code change needed.",
            auto_apply=False,
        )

    # --- (6) Generic Jekyll build failure ------------------------------
    if "Jekyll" in log_text and ("Error" in log_text or "exit code 1" in log_text):
        # Extract a short evidence line near the first "Error"
        snippet = _extract_snippet(log_text, "Error", context=2)
        return DeployDiagnosis(
            category="jekyll_build_failed",
            root_cause=(
                "Jekyll build exited non-zero but no specific signature "
                "matched. See the snippet in evidence."
            ),
            evidence={"snippet": snippet},
            suggested_fix="Manual investigation via `gh run view --log-failed`.",
            auto_apply=False,
        )

    # --- (7) Unknown ---------------------------------------------------
    return DeployDiagnosis(
        category="unknown_deploy_failure",
        root_cause="No classifier rule matched the failure log.",
        evidence={"head": log_text[:400]},
        suggested_fix="Manual investigation required.",
        auto_apply=False,
    )


def _extract_snippet(text: str, marker: str, context: int = 2) -> str:
    """Return ~2 lines of context around the first line containing `marker`."""
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if marker in ln:
            lo = max(0, i - context)
            hi = min(len(lines), i + context + 1)
            return "\n".join(lines[lo:hi])[:800]
    return text[:400]


def sweep_recent_failures(limit: int = 50) -> list[int]:
    """Diagnose all failed runs that don't yet have a diagnosis.

    Called from the daemon's scheduler tick.
    Returns the list of run_ids that were newly diagnosed.
    """
    new_ids: list[int] = []
    with session_scope() as s:
        # Find failed runs without a diagnosis
        failed = s.execute(
            select(Run.id)
            .where(Run.status == "failed")
            .order_by(desc(Run.started_at))
            .limit(limit)
        ).scalars().all()
        already = set(
            s.execute(select(Diagnosis.run_id)).scalars().all()
        )
        targets = [rid for rid in failed if rid not in already]

    for rid in targets:
        try:
            diag = diagnose_run(rid, apply_fix=True)
            if diag is not None:
                new_ids.append(rid)
        except Exception:
            log.exception("sweep: diagnose_run #%s crashed", rid)
    return new_ids


def list_diagnoses(limit: int = 50) -> list[Diagnosis]:
    with session_scope() as s:
        rows = s.execute(
            select(Diagnosis).order_by(desc(Diagnosis.created_at)).limit(limit)
        ).scalars().all()
        for r in rows:
            s.expunge(r)
        return list(rows)
