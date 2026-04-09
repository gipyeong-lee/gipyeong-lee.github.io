"""Video worker — asyncio loop that turns published posts into YouTube videos.

Lives alongside `daemon.scheduler_loop` in the same FastAPI process but
uses its own lock (`_video_lock`) so the video pipeline never blocks
blog publishing and vice versa.

Pick policy (daily broadcast mode):
    The worker fires **once per local broadcast day**, at the configured
    `broadcast_hour_local` o'clock in `broadcast_timezone` (default
    18:00 America/New_York — the US "evening news" slot). Each tick:
    - If a video has already been uploaded on the current broadcast
      date, sleep until the next slot.
    - Otherwise, after the broadcast hour has been reached for the day,
      pick the freshest published post that has no successful video and
      run the full pipeline + upload.

Failure isolation:
    A video run failure only updates the `videos` row (status=failed,
    fail_count++, last_error). It never touches blog pipeline state or
    marks the underlying post as broken. Diagnostics categories for
    video failures are added in diagnostics.py.

Config:
    settings.video_generation_enabled — master switch
    settings.video_pipeline_timeout_seconds — per-run cap
    settings.video_max_retries — max fail_count before auto-block
    settings.youtube_upload_daily_cap — hard cap on uploads per local day
    settings.broadcast_hour_local — broadcast slot hour (0-23)
    settings.broadcast_timezone — IANA timezone for the broadcast slot
"""
from __future__ import annotations

import asyncio
import logging
import re
from datetime import date, datetime, time, timedelta, timezone
from typing import Optional
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from sqlalchemy import func, select

from .config import (
    IMAGES_DIR,
    POSTS_DIR,
    TICK_INTERVAL_SECONDS,
    YOUTUBE_CLIENT_SECRETS,
    YOUTUBE_TOKEN_PATH,
)
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

    # If auto-upload is on but OAuth is not yet completed, refuse to
    # fire — the daemon's uploader would otherwise try to spawn its own
    # browser-based OAuth flow inside the daemon process, which would
    # silently hang and burn pipeline state. The Admin UI shows a
    # warning so the user knows to run `python -m scripts.app.youtube_login`.
    if settings.video_auto_upload and not _youtube_oauth_ready():
        log.debug("video_worker: skipping — youtube OAuth not yet completed")
        return

    # --- Broadcast slot gate ----------------------------------------
    # The daily broadcast slot is the *only* trigger for new uploads.
    # `should_run_broadcast` is pure / testable: it answers "is the
    # local broadcast hour already reached for a day on which we have
    # not yet uploaded?"
    decision = should_run_broadcast(
        now_utc=datetime.now(timezone.utc),
        broadcast_hour=settings.broadcast_hour_local,
        broadcast_tz_name=settings.broadcast_timezone,
        last_broadcast_date=_last_broadcast_local_date(settings.broadcast_timezone),
    )
    if not decision.run:
        return

    # Daily cap acts as a hard belt-and-suspenders second check (defends
    # against a bug in the slot logic accidentally double-firing).
    if settings.video_auto_upload and _reached_daily_upload_cap(
        settings.youtube_upload_daily_cap, settings.broadcast_timezone
    ):
        return

    candidate = _pick_next_post_slug(
        settings.video_max_retries,
        language=settings.video_language,
    )
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


def _pick_next_post_slug(
    max_retries: int, *, language: str = "ko"
) -> Optional[tuple[str, str]]:
    """Return (slug, title) for the newest post without a usable video row.

    Newest-first ordering prioritizes fresh content (which is what a news
    channel cares about) and matches the blog pipeline's own ordering.
    We also filter out posts that have no hero image on disk *and* have
    no published translation in the requested language — composing a
    video without either is a non-starter and would just waste a retry.
    """
    lang = (language or "ko").lower()
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
            if _has_hero_image(slug) and _has_post_translation(slug, lang):
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
            if _has_hero_image(slug) and _has_post_translation(slug, lang):
                return (slug, title or slug)

    return None


def _has_post_translation(slug: str, language: str) -> bool:
    """True if `<slug>.<lang>.md` (or `<slug>.md` for ko) exists on disk."""
    try:
        from pathlib import Path as _P
        if not language or language == "ko":
            return (_P(POSTS_DIR) / f"{slug}.md").exists()
        return (_P(POSTS_DIR) / f"{slug}.{language}.md").exists()
    except Exception:
        return False


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


def _reached_daily_upload_cap(cap: int, tz_name: str = "America/New_York") -> bool:
    """True if `cap` uploads have already happened on the current local day."""
    if cap <= 0:
        return False
    tz = _resolve_timezone(tz_name)
    today_local_start = (
        datetime.now(tz)
        .replace(hour=0, minute=0, second=0, microsecond=0)
        .astimezone(timezone.utc)
        .replace(tzinfo=None)
    )
    with session_scope() as s:
        count = s.execute(
            select(func.count(Video.id))
            .where(Video.uploaded_at != None)  # noqa: E711
            .where(Video.uploaded_at >= today_local_start)
        ).scalar_one()
    return int(count or 0) >= cap


# ----------------------------------------------------------------------
# Broadcast slot decision (pure / unit-testable)
# ----------------------------------------------------------------------


class BroadcastDecision:
    """Result of deciding whether the daily broadcast slot is open.

    Tiny class instead of dataclass for zero-import overhead in tests.
    """

    __slots__ = ("run", "reason", "local_now", "next_run_at")

    def __init__(
        self,
        run: bool,
        reason: str,
        local_now: datetime,
        next_run_at: Optional[datetime] = None,
    ):
        self.run = run
        self.reason = reason
        self.local_now = local_now
        self.next_run_at = next_run_at

    def __repr__(self) -> str:  # pragma: no cover - debug only
        return f"BroadcastDecision(run={self.run}, reason={self.reason!r})"


def _resolve_timezone(name: str):
    try:
        return ZoneInfo(name)
    except (ZoneInfoNotFoundError, Exception):
        log.warning(f"Unknown timezone {name!r}, falling back to UTC")
        return ZoneInfo("UTC")


def should_run_broadcast(
    *,
    now_utc: datetime,
    broadcast_hour: int,
    broadcast_tz_name: str,
    last_broadcast_date: Optional[date],
) -> BroadcastDecision:
    """Decide whether to fire today's broadcast slot.

    Pure function — takes the current UTC time and the most recent
    broadcast date and returns a yes/no answer plus a human reason.

    Logic:
    - If we already broadcast on the local-day for `now_utc`, do not fire.
    - If the local clock has not yet reached `broadcast_hour`, do not
      fire (wait for tonight's slot).
    - Otherwise fire.
    """
    tz = _resolve_timezone(broadcast_tz_name)
    if now_utc.tzinfo is None:
        now_utc = now_utc.replace(tzinfo=timezone.utc)
    local_now = now_utc.astimezone(tz)
    today_local = local_now.date()
    slot_start = local_now.replace(
        hour=max(0, min(23, broadcast_hour)),
        minute=0,
        second=0,
        microsecond=0,
    )

    if last_broadcast_date == today_local:
        # Already done today — next slot is tomorrow at broadcast hour.
        next_local = slot_start + timedelta(days=1)
        return BroadcastDecision(
            run=False,
            reason="already_broadcast_today",
            local_now=local_now,
            next_run_at=next_local,
        )

    if local_now < slot_start:
        return BroadcastDecision(
            run=False,
            reason="before_slot",
            local_now=local_now,
            next_run_at=slot_start,
        )

    return BroadcastDecision(
        run=True,
        reason="slot_open",
        local_now=local_now,
        next_run_at=None,
    )


def _youtube_oauth_ready() -> bool:
    """True only if both client_secrets.json and youtube_token.json exist.

    The token is the proof of completed OAuth consent — without it the
    uploader would block on `flow.run_local_server` inside the daemon.
    """
    try:
        return YOUTUBE_CLIENT_SECRETS.exists() and YOUTUBE_TOKEN_PATH.exists()
    except Exception:
        return False


def _last_broadcast_local_date(tz_name: str) -> Optional[date]:
    """Return the local-day of the most recent successful upload, or None."""
    tz = _resolve_timezone(tz_name)
    with session_scope() as s:
        row = s.execute(
            select(Video.uploaded_at)
            .where(Video.uploaded_at != None)  # noqa: E711
            .order_by(Video.uploaded_at.desc())
            .limit(1)
        ).first()
    if row is None or row[0] is None:
        return None
    uploaded_at = row[0]
    if uploaded_at.tzinfo is None:
        uploaded_at = uploaded_at.replace(tzinfo=timezone.utc)
    return uploaded_at.astimezone(tz).date()


# ----------------------------------------------------------------------
# Synchronous pipeline runner (executes inside asyncio.to_thread)
# ----------------------------------------------------------------------


def _run_video_pipeline_sync(
    slug: str, title: str, video_id: int, run_id: int
) -> VideoPipelineResult:
    pipeline = VideoPipeline()
    # Resolve post description/permalink/tags by reading the front matter.
    settings = get_settings()
    meta = _read_post_meta(slug, language=settings.video_language)

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


def _read_post_meta(slug: str, *, language: str = "ko") -> dict:
    """Best-effort front matter read for description/permalink/tags.

    Prefers the `<slug>.<lang>.md` translation when `language` is set
    and the file exists; otherwise falls back to the Korean source.
    """
    path = None
    if hasattr(POSTS_DIR, "__truediv__"):
        if language and language != "ko":
            translated = POSTS_DIR / f"{slug}.{language}.md"
            if translated.exists():
                path = translated
        if path is None:
            korean = POSTS_DIR / f"{slug}.md"
            if korean.exists():
                path = korean
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
