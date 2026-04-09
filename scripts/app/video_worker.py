"""Video worker — asyncio loop that turns published posts into YouTube videos.

Lives alongside `daemon.scheduler_loop` in the same FastAPI process but
uses its own lock (`_video_lock`) so the video pipeline never blocks
blog publishing and vice versa.

Pick policy:
    Every tick, fetch published `post_history` rows that do NOT have a
    matching `videos` row (by slug), ordered newest-first. If the video
    pipeline is idle, claim the first one, create a `videos` row with
    status=running, then off-load the synchronous pipeline to a thread.

Failure isolation:
    A video run failure only updates the `videos` row (status=failed,
    fail_count++, last_error). It never touches blog pipeline state or
    marks the underlying post as broken. Diagnostics categories for
    video failures are added in diagnostics.py.

Config:
    settings.video_generation_enabled — master switch (default False)
    settings.video_pipeline_timeout_seconds — per-run cap
    settings.video_max_retries — max fail_count before auto-block
    settings.youtube_upload_daily_cap — hard cap on uploads per calendar day
"""
from __future__ import annotations

import asyncio
import logging
import re
from datetime import datetime, timedelta, timezone
from typing import Optional

from sqlalchemy import func, select

from .config import IMAGES_DIR, POSTS_DIR, TICK_INTERVAL_SECONDS
from .db import session_scope
from .diagnostics import classify_video_error, video_category_should_block
from .models_db import PostHistory, Video, VideoRun
from .settings_store import get_settings
from .video_pipeline import VideoPipeline, VideoPipelineResult

log = logging.getLogger("aiblog.video_worker")

_video_lock = asyncio.Lock()
_stop_event = asyncio.Event()
_state: dict = {
    "running": False,
    "current_video_id": None,
    "last_run_at": None,
}

_LANG_SUFFIX_RE = re.compile(r"\.(en|ja|zh-cn|zh-tw)\.md$")

# Video worker tick: faster than blog scheduler since runs are short.
_VIDEO_TICK_SECONDS = 30


def stop() -> None:
    _stop_event.set()


def reset_stop() -> None:
    _stop_event.clear()


def video_locked() -> bool:
    return _video_lock.locked()


def current_video_id() -> Optional[int]:
    return _state["current_video_id"]


def is_running() -> bool:
    return _state["running"]


# ----------------------------------------------------------------------
# Main loop
# ----------------------------------------------------------------------


async def video_worker_loop() -> None:
    """Poll post_history and render pending videos. Cancel-safe."""
    log.info("video_worker_loop starting")
    _state["running"] = True
    reset_stop()
    try:
        while not _stop_event.is_set():
            try:
                await _tick()
            except Exception:
                log.exception("video_worker tick failed")
            # Sleep with cancellation support.
            try:
                await asyncio.wait_for(_stop_event.wait(), timeout=_VIDEO_TICK_SECONDS)
            except asyncio.TimeoutError:
                pass
    finally:
        _state["running"] = False
        log.info("video_worker_loop stopped")


async def _tick() -> None:
    settings = get_settings()
    if not settings.video_generation_enabled:
        return
    if _video_lock.locked():
        return

    # Daily upload cap defense: if we've already uploaded cap videos today
    # and auto upload is on, stop picking until midnight UTC rolls over.
    if settings.video_auto_upload and _reached_daily_upload_cap(
        settings.youtube_upload_daily_cap
    ):
        return

    candidate = _pick_next_post_slug(settings.video_max_retries)
    if candidate is None:
        return

    slug, title = candidate
    async with _video_lock:
        _state["current_video_id"] = None
        video_id = _upsert_video_row(slug)
        _state["current_video_id"] = video_id
        run_id = _start_video_run(video_id, trigger="auto")

        try:
            result = await asyncio.wait_for(
                asyncio.to_thread(_run_video_pipeline_sync, slug, title, video_id, run_id),
                timeout=settings.video_pipeline_timeout_seconds,
            )
        except asyncio.TimeoutError:
            log.warning(f"video pipeline timeout for {slug}")
            _finish_video_run(
                video_id,
                run_id,
                success=False,
                error=f"pipeline timeout after {settings.video_pipeline_timeout_seconds}s",
                result=None,
            )
            return
        except Exception as e:
            log.exception("video pipeline crashed")
            _finish_video_run(
                video_id,
                run_id,
                success=False,
                error=f"crash: {type(e).__name__}: {e}",
                result=None,
            )
            return
        finally:
            _state["current_video_id"] = None
            _state["last_run_at"] = datetime.now(timezone.utc)

        _finish_video_run(
            video_id,
            run_id,
            success=bool(result and result.success),
            error=None if result and result.success else (result.error if result else "unknown"),
            result=result,
        )


# ----------------------------------------------------------------------
# Selection
# ----------------------------------------------------------------------


def _pick_next_post_slug(max_retries: int) -> Optional[tuple[str, str]]:
    """Return (slug, title) for the newest post without a usable video row.

    Newest-first ordering prioritizes fresh content (which is what a news
    channel cares about) and matches the blog pipeline's own ordering.
    We also filter out posts that have no hero image on disk — composing
    a video without a hero is a non-starter and would just waste a retry.
    """
    with session_scope() as s:
        # Posts that have no videos row at all → highest priority, newest first.
        # We fetch a small candidate window, then filter in Python by hero image
        # existence (SQL can't express that cheaply).
        missing_stmt = (
            select(PostHistory.slug, PostHistory.title)
            .where(
                ~PostHistory.slug.in_(select(Video.post_slug))
            )
            .order_by(PostHistory.published_at.desc())
            .limit(20)
        )
        for slug, title in s.execute(missing_stmt).all():
            if _has_hero_image(slug):
                return (slug, title or slug)

        # Otherwise: any failed video with fail_count < max_retries,
        # at least 1h since its last attempt. Blocked videos are skipped
        # (quota/oauth issues; admin must Regenerate manually).
        now = datetime.utcnow()
        backoff = now - timedelta(hours=1)
        retry_stmt = (
            select(Video.post_slug, PostHistory.title)
            .join(PostHistory, PostHistory.slug == Video.post_slug)
            .where(Video.status == "failed")  # blocked videos are excluded
            .where(Video.fail_count < max_retries)
            .where((Video.updated_at == None) | (Video.updated_at < backoff))  # noqa: E711
            .order_by(Video.updated_at.asc().nullsfirst())
            .limit(1)
        )
        for slug, title in s.execute(retry_stmt).all():
            if _has_hero_image(slug):
                return (slug, title or slug)

    return None


def _has_hero_image(slug: str) -> bool:
    """Fast check: does a jpg/jpeg/png/webp exist for this slug?"""
    try:
        from pathlib import Path as _P
        for ext in ("jpg", "jpeg", "png", "webp"):
            if (_P(IMAGES_DIR) / f"{slug}.{ext}").exists():
                return True
    except Exception:
        pass
    return False


def _upsert_video_row(slug: str) -> int:
    """Ensure a videos row exists for this slug; return its id."""
    with session_scope() as s:
        row = s.execute(select(Video).where(Video.post_slug == slug)).scalar_one_or_none()
        if row is None:
            row = Video(post_slug=slug, status="running")
            s.add(row)
            s.flush()
        else:
            row.status = "running"
            row.last_error = None
        s.flush()
        return row.id


def _start_video_run(video_id: int, trigger: str) -> int:
    with session_scope() as s:
        run = VideoRun(video_id=video_id, trigger=trigger, status="running")
        s.add(run)
        s.flush()
        return run.id


def _finish_video_run(
    video_id: int,
    run_id: int,
    *,
    success: bool,
    error: Optional[str],
    result: Optional[VideoPipelineResult],
) -> None:
    with session_scope() as s:
        run = s.get(VideoRun, run_id)
        if run is not None:
            run.status = "success" if success else "failed"
            run.ended_at = datetime.utcnow()
            run.error = (error or "")[:2000] if not success else None
            if result and result.failed_stage:
                run.stage = result.failed_stage
            if run.started_at and run.ended_at:
                run.duration_seconds = (run.ended_at - run.started_at).total_seconds()

        video = s.get(Video, video_id)
        if video is None:
            return
        if success and result is not None:
            video.status = (
                "uploaded" if result.youtube_video_id else "success"
            )
            video.script = result.script
            video.duration_seconds = result.duration_seconds
            video.mp4_path = result.mp4_path
            video.thumbnail_path = result.thumbnail_path
            video.audio_path = result.wav_path
            video.youtube_video_id = result.youtube_video_id
            video.youtube_url = result.youtube_url
            video.youtube_privacy = result.youtube_privacy
            if result.youtube_video_id:
                video.uploaded_at = datetime.utcnow()
            video.last_error = None
        else:
            category = classify_video_error(error)
            should_block = video_category_should_block(category)
            video.fail_count = (video.fail_count or 0) + 1
            # Block status stops the worker from retrying; admin can still
            # manually Regenerate from the UI.
            video.status = "blocked" if should_block else "failed"
            # Prefix last_error with the category for at-a-glance diagnosis.
            prefix = f"[{category}] "
            msg = (error or "unknown")
            video.last_error = (prefix + msg)[:2000]
            # Also tag the most recent VideoRun with the category.
            if run is not None:
                run.stage = run.stage or category


def _reached_daily_upload_cap(cap: int) -> bool:
    if cap <= 0:
        return False
    since = datetime.utcnow() - timedelta(hours=24)
    with session_scope() as s:
        count = s.execute(
            select(func.count(Video.id))
            .where(Video.uploaded_at != None)  # noqa: E711
            .where(Video.uploaded_at >= since)
        ).scalar_one()
    return int(count or 0) >= cap


# ----------------------------------------------------------------------
# Synchronous pipeline runner (executes inside asyncio.to_thread)
# ----------------------------------------------------------------------


def _run_video_pipeline_sync(
    slug: str, title: str, video_id: int, run_id: int
) -> VideoPipelineResult:
    pipeline = VideoPipeline()
    # Resolve post description/permalink/tags by reading the front matter.
    meta = _read_post_meta(slug)

    def stage_hook(stage: str, status: str, meta: dict) -> None:
        # Keep it light: only bump the runs.stage field.
        try:
            with session_scope() as s:
                run = s.get(VideoRun, run_id)
                if run is not None and status == "start":
                    run.stage = stage
        except Exception:
            log.exception("stage hook write failed")

    return pipeline.run(
        slug=slug,
        title=title,
        description=meta.get("description", ""),
        tags=meta.get("tags") or [],
        permalink=meta.get("permalink", ""),
        stage_hook=stage_hook,
    )


def _read_post_meta(slug: str) -> dict:
    """Best-effort front matter read for description/permalink/tags."""
    path = (POSTS_DIR / f"{slug}.md") if hasattr(POSTS_DIR, "__truediv__") else None
    if path is None or not path.exists():
        return {}
    try:
        raw = path.read_text(encoding="utf-8")
    except Exception:
        return {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", raw, re.DOTALL)
    if not match:
        return {}
    fm = match.group(1)
    meta: dict = {}
    for line in fm.splitlines():
        kv = re.match(r"^([a-zA-Z_][\w-]*)\s*:\s*(.*)$", line)
        if not kv:
            continue
        key, val = kv.group(1), kv.group(2).strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        elif val.startswith("'") and val.endswith("'"):
            val = val[1:-1]
        meta[key] = val

    # Parse tags: "[a, b, c]" → list[str]
    tags_raw = meta.get("tags", "")
    tags_list: list[str] = []
    m = re.match(r"\[(.*)\]", tags_raw)
    if m:
        tags_list = [t.strip().strip('"').strip("'") for t in m.group(1).split(",") if t.strip()]
    meta["tags"] = tags_list
    return meta
