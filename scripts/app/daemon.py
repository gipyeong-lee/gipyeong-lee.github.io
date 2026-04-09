"""SchedulerLoop — the heart of the continuous AI blog daemon.

Runs as an asyncio task inside the FastAPI process (started by
`main.py`'s lifespan hook). Can also be invoked standalone as
`python -m scripts.app.daemon` for headless / Phase-A testing.
"""
from __future__ import annotations

import asyncio
import json
import logging
import random
from datetime import datetime, timedelta, timezone
from typing import Optional

from sqlalchemy import func, select

from .config import (
    DEFAULTS,
    TICK_INTERVAL_SECONDS,
)
from . import diagnostics
from .db import init_db, session_scope
from .logging_bus import ObserverImpl, log_bus
from .models_db import PostHistory, Run, SourceState, Topic
from .pipeline_runner import PipelineRunner
from .publisher import PublishError, publish
from .queue_service import (
    add_manual,
    enqueue_new,
    mark_status,
    peek_top_score,
    pick_next,
)
from .schemas import PipelineResult, StreamEvent
from .scoring import score_batch
from .settings_store import get_settings
from .sources import ALL_SOURCES
from .sources.base import SourceAdapter

log = logging.getLogger("aiblog.daemon")

# Module-level state (one daemon instance per process)
_pipeline_lock = asyncio.Lock()
_stop_event = asyncio.Event()
_state = {"running": False, "last_run_at": None, "current_run_id": None}


def is_running() -> bool:
    return _state["running"]


def get_last_run_at() -> Optional[datetime]:
    return _state["last_run_at"]


def current_run_id() -> Optional[int]:
    return _state["current_run_id"]


def stop() -> None:
    _stop_event.set()


def reset_stop() -> None:
    _stop_event.clear()


def pipeline_locked() -> bool:
    return _pipeline_lock.locked()


# -- Source helpers ------------------------------------------------------


def _build_enabled_sources() -> list[SourceAdapter]:
    settings = get_settings()
    enabled = settings.sources_enabled
    out: list[SourceAdapter] = []
    for cls in ALL_SOURCES:
        name = getattr(cls, "name", cls.__name__)
        if enabled.get(name, True):
            try:
                out.append(cls())
            except Exception as e:
                log.warning("failed to init source %s: %s", name, e)
    return out


def _get_or_create_source_state(session, name: str) -> SourceState:
    st = session.get(SourceState, name)
    if st is None:
        st = SourceState(source=name)
        session.add(st)
        session.flush()
    return st


def _next_poll_with_backoff(state: SourceState, base_interval: int) -> datetime:
    errs = state.consecutive_errors or 0
    multiplier = min(16, 2 ** errs) if errs > 0 else 1
    interval = base_interval * multiplier
    interval = min(interval, 4 * 60 * 60)  # cap at 4h
    return datetime.now(timezone.utc) + timedelta(seconds=interval)


async def _poll_source(src: SourceAdapter, base_interval: int) -> int:
    """Poll a single source; persist state and enqueue new topics."""
    now = datetime.now(timezone.utc)
    try:
        raws = await src.poll()
    except Exception as e:
        log.warning("source %s poll failed: %s", src.name, e)
        with session_scope() as s:
            st = _get_or_create_source_state(s, src.name)
            st.last_poll_at = now
            st.consecutive_errors = (st.consecutive_errors or 0) + 1
            st.last_error = str(e)[:1000]
            st.next_poll_at = _next_poll_with_backoff(st, base_interval)
        return 0

    scored = score_batch(raws)
    inserted = enqueue_new(scored)

    with session_scope() as s:
        st = _get_or_create_source_state(s, src.name)
        st.last_poll_at = now
        st.last_success_at = now
        st.consecutive_errors = 0
        st.last_error = None
        st.next_poll_at = _next_poll_with_backoff(st, base_interval)

    if inserted:
        log.info("source %s: +%d new topics", src.name, inserted)
        log_bus.publish(
            StreamEvent(
                kind="source_polled",
                meta={"source": src.name, "new": inserted, "total": len(scored)},
            )
        )
    return inserted


def _as_utc(dt: Optional[datetime]) -> Optional[datetime]:
    """Normalize a (possibly-naive) SQLite datetime to UTC-aware."""
    if dt is None:
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt


async def _poll_all_if_due() -> None:
    settings = get_settings()
    base = settings.source_poll_interval_seconds
    now = datetime.now(timezone.utc)

    due: list[SourceAdapter] = []
    with session_scope() as s:
        for src in _build_enabled_sources():
            st = _get_or_create_source_state(s, src.name)
            next_poll = _as_utc(st.next_poll_at)
            if next_poll is None or next_poll <= now:
                due.append(src)

    if not due:
        return

    # Poll in parallel
    await asyncio.gather(*(_poll_source(src, base) for src in due))


# -- Trigger decision ----------------------------------------------------


def _decide_trigger() -> Optional[str]:
    settings = get_settings()
    last = _state["last_run_at"] or _bootstrap_last_run_at()
    if last is None:
        # never run before → trigger a timer run immediately if we have a topic
        return "timer"

    last = _as_utc(last)
    elapsed = (datetime.now(timezone.utc) - last).total_seconds()
    if elapsed < settings.min_interval_seconds:
        return None
    if elapsed >= settings.max_interval_seconds:
        return "timer"

    top = peek_top_score(settings.keyword_blocklist)
    if top is not None and (top.score + (top.priority_boost or 0)) >= settings.event_trigger_threshold:
        return "event"

    return None


def _bootstrap_last_run_at() -> Optional[datetime]:
    """Compute last_run_at from runs table on cold start.

    All terminal states count (including aborted) so a crash doesn't
    cause the scheduler to immediately fire another run on restart.
    """
    with session_scope() as s:
        row = s.execute(
            select(func.max(Run.started_at)).where(
                Run.status.in_(["success", "failed", "aborted"])
            )
        ).first()
    if row and row[0]:
        val = _as_utc(row[0])
        _state["last_run_at"] = val
        return val
    return None


# -- Run execution -------------------------------------------------------


def _create_run_row(topic_id: Optional[int], trigger: str) -> int:
    with session_scope() as s:
        r = Run(
            topic_id=topic_id,
            trigger=trigger,
            status="running",
            stage="queued",
        )
        s.add(r)
        s.flush()
        return r.id


def _finish_run(
    run_id: int,
    success: bool,
    slug: str | None = None,
    sha: str | None = None,
    error: str | None = None,
    verdict: str | None = None,
) -> None:
    with session_scope() as s:
        r = s.get(Run, run_id)
        if r is None:
            return
        r.status = "success" if success else "failed"
        r.ended_at = datetime.now(timezone.utc)
        if slug:
            r.final_slug = slug
        if sha:
            r.git_commit_sha = sha
        if error:
            r.error = error[:2000]
        if verdict:
            r.fact_check_verdict = verdict


def _insert_post_history(result: PipelineResult, run_id: int, sha: str | None) -> None:
    if not result.slug:
        return
    with session_scope() as s:
        existing = s.execute(
            select(PostHistory).where(PostHistory.slug == result.slug)
        ).scalar_one_or_none()
        if existing is not None:
            return
        s.add(
            PostHistory(
                slug=result.slug,
                title=result.title_ko,
                topic=result.title_ko or result.slug,
                published_at=datetime.now(timezone.utc),
                run_id=run_id,
                git_commit_sha=sha,
                languages=json.dumps(result.languages),
            )
        )


async def _run_one(
    topic: Topic | None,
    trigger: str,
    *,
    custom_topic: str | None = None,
    custom_url: str | None = None,
) -> PipelineResult:
    settings = get_settings()
    run_id = _create_run_row(topic.id if topic else None, trigger)
    _state["current_run_id"] = run_id
    observer = ObserverImpl(run_id=run_id)
    runner = PipelineRunner(observer=observer)

    try:
        result = await runner.run(
            topic,
            run_id=run_id,
            custom_topic=custom_topic,
            custom_url=custom_url,
            source_label=(topic.source if topic else "manual"),
            timeout_seconds=settings.pipeline_timeout_seconds,
        )
    finally:
        _state["current_run_id"] = None

    sha: str | None = None
    if result.success and settings.auto_publish:
        try:
            sha = publish(result, push=settings.git_push)
        except PublishError as e:
            log.error("publish failed: %s", e)
            result.error = f"publish_failed: {e}"
            result.success = False

    if result.success:
        if topic is not None:
            mark_status(topic.id, "published", used_at=datetime.now(timezone.utc))
        _insert_post_history(result, run_id, sha)
        _finish_run(run_id, success=True, slug=result.slug, sha=sha, verdict="PASS")
        _state["last_run_at"] = datetime.now(timezone.utc)
    else:
        if topic is not None:
            mark_status(
                topic.id,
                "failed",
                error=result.error,
                fail_count_delta=1,
            )
            # Auto-block after too many failures
            with session_scope() as s:
                t = s.get(Topic, topic.id)
                if t and t.fail_count >= settings.max_fail_count_before_block:
                    t.status = "blocked"
        _finish_run(run_id, success=False, slug=result.slug, error=result.error)
        # Kick the diagnostics agent immediately on a failed run so any
        # safe auto-fix (block topic, reset for retry, etc.) lands before
        # the next scheduler tick.
        try:
            diagnostics.diagnose_run(run_id, apply_fix=True)
        except Exception:
            log.exception("diagnose_run crashed after failed run #%s", run_id)

    return result


# -- Public API: manual trigger -----------------------------------------


async def trigger_manual(
    topic_id: int | None = None,
    custom_topic: str | None = None,
    custom_url: str | None = None,
) -> PipelineResult:
    """Called by /pipeline/trigger. Errors if a run is in progress."""
    if _pipeline_lock.locked():
        raise RuntimeError("a pipeline run is already in progress")

    topic: Topic | None = None
    if topic_id:
        with session_scope() as s:
            t = s.get(Topic, topic_id)
            if t is None:
                raise ValueError(f"topic {topic_id} not found")
            t.status = "selected"
            t.selected_at = datetime.now(timezone.utc)
            s.flush()
            s.expunge(t)
            topic = t

    async with _pipeline_lock:
        return await _run_one(topic, trigger="manual",
                              custom_topic=custom_topic, custom_url=custom_url)


# -- Scheduler tick ------------------------------------------------------


async def tick() -> None:
    await _poll_all_if_due()

    # Sweep any un-diagnosed failed runs (e.g. from before the diagnostics
    # agent existed, or from a prior crash). Safe to run every tick — it's
    # idempotent and skips runs that already have a diagnosis.
    try:
        newly = diagnostics.sweep_recent_failures(limit=20)
        if newly:
            log.info("diagnostics swept %d new failed runs: %s", len(newly), newly)
    except Exception:
        log.exception("diagnostics sweep crashed")

    if _pipeline_lock.locked():
        return

    trigger = _decide_trigger()
    if trigger is None:
        return

    settings = get_settings()
    topic = pick_next(
        cooldown_seconds=settings.cooldown_after_fail_seconds,
        max_fail_count=settings.max_fail_count_before_block,
        blocklist=settings.keyword_blocklist,
    )
    if topic is None:
        log.debug("scheduler: no eligible topic")
        return

    async with _pipeline_lock:
        await _run_one(topic, trigger=trigger)


# -- Main loop -----------------------------------------------------------


def _recover_crashed_state() -> None:
    """Clean up state left behind by a crashed / killed prior process.

    Called once at scheduler startup. Marks any in-flight runs as aborted
    and resets any topics stuck in 'selected' or 'running' back to 'queued'
    so they can be picked again.
    """
    with session_scope() as s:
        for r in s.execute(
            select(Run).where(Run.status == "running")
        ).scalars().all():
            r.status = "aborted"
            r.ended_at = datetime.now(timezone.utc)
            r.error = (r.error or "") + " [recovered: process was restarted]"
            log.warning("recovered crashed run #%s", r.id)
        for t in s.execute(
            select(Topic).where(Topic.status.in_(["selected", "running"]))
        ).scalars().all():
            t.status = "queued"
            t.selected_at = None
            log.warning("recovered stuck topic #%s", t.id)


async def scheduler_loop() -> None:
    _state["running"] = True
    _recover_crashed_state()
    _bootstrap_last_run_at()
    log.info(
        "scheduler loop started (last_run_at=%s)", _state["last_run_at"]
    )
    try:
        while not _stop_event.is_set():
            try:
                await tick()
            except Exception:
                log.exception("scheduler tick crashed")
            try:
                await asyncio.wait_for(
                    _stop_event.wait(), timeout=TICK_INTERVAL_SECONDS
                )
                break  # stop_event was set
            except asyncio.TimeoutError:
                continue
    finally:
        _state["running"] = False
        log.info("scheduler loop stopped")


# -- Standalone entrypoint (headless mode) -------------------------------


def main() -> None:
    import logging as _logging

    _logging.basicConfig(
        level=_logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    init_db()
    asyncio.run(scheduler_loop())


if __name__ == "__main__":
    main()
