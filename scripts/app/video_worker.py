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
from datetime import datetime, timedelta, timezone
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

    # --- Slot gate ---------------------------------------------------
    # We compute N evenly-spaced slots across the local broadcast day
    # (N = youtube_upload_daily_cap). Each slot fires at most once
    # within its 24/N-hour window. This caps daily uploads at the
    # YouTube quota limit while spreading them evenly so no two
    # uploads hit the channel within minutes of each other.
    decision = should_run_broadcast(
        now_utc=datetime.now(timezone.utc),
        cap_per_day=settings.youtube_upload_daily_cap,
        anchor_hour=settings.broadcast_hour_local,
        broadcast_tz_name=settings.broadcast_timezone,
        last_upload_at_utc=_last_upload_at_utc(),
    )
    if not decision.run:
        return

    # Belt-and-suspenders: hard daily cap on top of slot logic to defend
    # against a bug accidentally double-firing within a window.
    if settings.video_auto_upload and _reached_daily_upload_cap(
        settings.youtube_upload_daily_cap, settings.broadcast_timezone
    ):
        return

    # Pick the next episode (newscast: N topics; legacy: 1 topic).
    episode = _pick_next_episode(
        n=settings.topics_per_episode,
        language=settings.video_language,
        freshness_hours=settings.topics_freshness_hours,
    )
    if episode is None:
        return

    episode_slug = episode["episode_slug"]
    episode_title = episode["episode_title"]
    topics = episode["topics"]

    async with _video_lock:
        _state["current_video_id"] = None
        video_id = _upsert_video_row(episode_slug)
        _state["current_video_id"] = video_id
        run_id = _start_video_run(video_id, trigger="auto")

        try:
            result = await asyncio.wait_for(
                asyncio.to_thread(
                    _run_video_pipeline_sync,
                    episode_slug,
                    episode_title,
                    topics,
                    video_id,
                    run_id,
                ),
                timeout=settings.video_pipeline_timeout_seconds,
            )
        except asyncio.TimeoutError:
            log.warning(f"video pipeline timeout for {episode_slug}")
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


def _pick_next_episode(
    *,
    n: int,
    language: str,
    freshness_hours: int,
) -> Optional[dict]:
    """Pick the freshest N posts for the upcoming episode.

    Returns ``None`` if fewer than 1 post is available within the
    freshness window. The episode slug is synthetic and unique per UTC
    hour, so re-running the worker tick within an hour does not
    accidentally start a duplicate episode.

    Returned dict shape:
        {
            "episode_slug": "episode-2026-04-10-04",
            "episode_title": "AI News Daily — April 10, 2026",
            "topics": [
                {
                    "slug": "<post-slug>",
                    "title": "<post-title>",
                    "description": "<post-description>",
                    "post_path": "<absolute path to .{lang}.md>",
                    "hero_path": "<absolute path to hero image>",
                    "tags": ["..."],
                },
                ...
            ],
        }
    """
    lang = (language or "ko").lower()
    n = max(1, int(n or 1))
    cutoff_utc = datetime.utcnow() - timedelta(hours=max(1, int(freshness_hours)))

    candidates: list[dict] = []
    with session_scope() as s:
        rows = s.execute(
            select(PostHistory.slug, PostHistory.title, PostHistory.published_at)
            .where(PostHistory.published_at >= cutoff_utc)
            .order_by(PostHistory.published_at.desc())
            .limit(n * 4)  # over-fetch for hero/translation filtering
        ).all()
    for slug, title, _published_at in rows:
        if len(candidates) >= n:
            break
        if not _has_hero_image(slug) or not _has_post_translation(slug, lang):
            continue
        post_path = _resolve_post_path(slug, lang)
        hero_path = _resolve_hero_path(slug)
        if post_path is None or hero_path is None:
            continue
        meta = _read_post_meta(slug, language=lang)
        candidates.append(
            {
                "slug": slug,
                "title": title or slug,
                "description": meta.get("description", "") if isinstance(meta, dict) else "",
                "post_path": str(post_path),
                "hero_path": str(hero_path),
                "tags": meta.get("tags", []) if isinstance(meta, dict) else [],
            }
        )

    if not candidates:
        return None

    now_utc = datetime.now(timezone.utc)
    episode_slug = f"episode-{now_utc:%Y-%m-%d-%H}"
    episode_title = f"AI News Daily — {now_utc:%B %d, %Y}"
    return {
        "episode_slug": episode_slug,
        "episode_title": episode_title,
        "topics": candidates,
    }


def _resolve_post_path(slug: str, language: str) -> Optional["object"]:
    from pathlib import Path as _P
    if language and language != "ko":
        translated = _P(POSTS_DIR) / f"{slug}.{language}.md"
        if translated.exists():
            return translated
    korean = _P(POSTS_DIR) / f"{slug}.md"
    return korean if korean.exists() else None


def _resolve_hero_path(slug: str) -> Optional["object"]:
    from pathlib import Path as _P
    for ext in ("jpg", "jpeg", "png", "webp"):
        cand = _P(IMAGES_DIR) / f"{slug}.{ext}"
        if cand.exists():
            return cand
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
    """Result of deciding whether a broadcast slot is currently open.

    Tiny class instead of dataclass for zero-import overhead in tests.
    """

    __slots__ = ("run", "reason", "local_now", "next_run_at", "active_slot_hour")

    def __init__(
        self,
        run: bool,
        reason: str,
        local_now: datetime,
        next_run_at: Optional[datetime] = None,
        active_slot_hour: Optional[int] = None,
    ):
        self.run = run
        self.reason = reason
        self.local_now = local_now
        self.next_run_at = next_run_at
        self.active_slot_hour = active_slot_hour

    def __repr__(self) -> str:  # pragma: no cover - debug only
        return (
            f"BroadcastDecision(run={self.run}, reason={self.reason!r}, "
            f"slot={self.active_slot_hour})"
        )


def _resolve_timezone(name: str):
    try:
        return ZoneInfo(name)
    except (ZoneInfoNotFoundError, Exception):
        log.warning(f"Unknown timezone {name!r}, falling back to UTC")
        return ZoneInfo("UTC")


def compute_broadcast_slots(cap_per_day: int, anchor_hour: int = 0) -> list[int]:
    """Return the list of local hours (0-23) at which slots fire.

    For ``cap_per_day == 1`` we honour ``anchor_hour`` so the legacy
    "single 18:00 ET broadcast" behavior is preserved verbatim. For
    higher caps we evenly distribute slots starting from local midnight,
    centered within their interval — this gives a clean, predictable
    grid that does not depend on the anchor hour::

        N=2 → [ 6, 18]
        N=3 → [ 4, 12, 20]
        N=4 → [ 3,  9, 15, 21]
        N=5 → [ 2,  7, 12, 17, 22]
        N=6 → [ 2,  6, 10, 14, 18, 22]

    The (k + 0.5) offset centers each slot within its window, so the
    user never sees an awkward 00:00 broadcast and the gaps stay
    symmetric across midnight.
    """
    n = max(1, min(24, int(cap_per_day or 1)))
    if n == 1:
        return [max(0, min(23, int(anchor_hour)))]
    return sorted({round((k + 0.5) * 24 / n) % 24 for k in range(n)})


def find_active_slot(
    local_now: datetime, slot_hours: list[int]
) -> Optional[int]:
    """Return the most recent slot whose start hour has already passed today.

    Returns the hour-of-day (0-23) of the active slot, or None if the
    current local time is earlier than every slot of the day.
    """
    if not slot_hours:
        return None
    now_h = local_now.hour + local_now.minute / 60.0 + local_now.second / 3600.0
    passed = [h for h in sorted(slot_hours) if h <= now_h]
    return passed[-1] if passed else None


def should_run_broadcast(
    *,
    now_utc: datetime,
    cap_per_day: int,
    anchor_hour: int,
    broadcast_tz_name: str,
    last_upload_at_utc: Optional[datetime],
) -> BroadcastDecision:
    """Decide whether the active slot is open and unfilled.

    Pure function. Returns ``run=True`` only when:
    - the current local time is past at least one slot for today, AND
    - no upload has happened inside that slot's window yet.

    A slot's window is ``[slot_start, slot_start + 24/N hours)`` so each
    slot can fire at most once. The next-run-at field tells the caller
    when the next opportunity arrives if we declined this tick.
    """
    tz = _resolve_timezone(broadcast_tz_name)
    if now_utc.tzinfo is None:
        now_utc = now_utc.replace(tzinfo=timezone.utc)
    local_now = now_utc.astimezone(tz)

    slots = compute_broadcast_slots(cap_per_day, anchor_hour)
    n = len(slots)
    window_hours = 24.0 / n if n > 0 else 24.0

    active_hour = find_active_slot(local_now, slots)

    # Pre-day case: no slot has started yet today.
    if active_hour is None:
        first_slot_today = local_now.replace(
            hour=slots[0], minute=0, second=0, microsecond=0
        )
        return BroadcastDecision(
            run=False,
            reason="before_first_slot",
            local_now=local_now,
            next_run_at=first_slot_today,
        )

    slot_start_local = local_now.replace(
        hour=active_hour, minute=0, second=0, microsecond=0
    )
    slot_end_local = slot_start_local + timedelta(hours=window_hours)

    # Did any upload land inside [slot_start, slot_end)?
    already_filled = False
    if last_upload_at_utc is not None:
        last_local = last_upload_at_utc.astimezone(tz)
        if slot_start_local <= last_local < slot_end_local:
            already_filled = True

    if already_filled:
        # Next slot today, or first slot tomorrow if we're on the last one.
        try:
            idx = slots.index(active_hour)
        except ValueError:  # pragma: no cover - active_hour came from slots
            idx = -1
        if idx + 1 < n:
            next_local = local_now.replace(
                hour=slots[idx + 1], minute=0, second=0, microsecond=0
            )
        else:
            next_local = (
                local_now.replace(hour=slots[0], minute=0, second=0, microsecond=0)
                + timedelta(days=1)
            )
        return BroadcastDecision(
            run=False,
            reason="slot_already_filled",
            local_now=local_now,
            next_run_at=next_local,
            active_slot_hour=active_hour,
        )

    return BroadcastDecision(
        run=True,
        reason="slot_open",
        local_now=local_now,
        next_run_at=None,
        active_slot_hour=active_hour,
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


def _last_upload_at_utc() -> Optional[datetime]:
    """Return the UTC timestamp of the most recent upload, or None."""
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
    return uploaded_at


# ----------------------------------------------------------------------
# Synchronous pipeline runner (executes inside asyncio.to_thread)
# ----------------------------------------------------------------------


def _run_video_pipeline_sync(
    episode_slug: str,
    episode_title: str,
    topics: list[dict],
    video_id: int,
    run_id: int,
) -> VideoPipelineResult:
    """Run the appropriate pipeline variant for an episode.

    - Multi-topic episodes (``len(topics) > 1``) call ``run_newscast``,
      which weaves a 50-min broadcast script + multi-hero composer.
    - Single-topic episodes fall through to the legacy single-post
      ``run`` so that user-triggered "Regenerate" of an old single
      video still works without surprise.
    """
    pipeline = VideoPipeline()

    def stage_hook(stage: str, status: str, _meta: dict) -> None:
        try:
            with session_scope() as s:
                run = s.get(VideoRun, run_id)
                if run is not None and status == "start":
                    run.stage = stage
        except Exception:
            log.exception("stage hook write failed")

    if len(topics) > 1:
        return pipeline.run_newscast(
            episode_slug=episode_slug,
            episode_title=episode_title,
            topics=topics,
            stage_hook=stage_hook,
        )

    # Single-topic fallback (legacy mode + manual regenerate of old rows).
    only = topics[0]
    return pipeline.run(
        slug=only["slug"],
        title=only.get("title") or only["slug"],
        description=only.get("description", ""),
        tags=only.get("tags") or [],
        permalink="",
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
