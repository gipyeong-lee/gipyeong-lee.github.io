"""Videos routes — episode generation, list, manual trigger, upload, publish.

All operations are local-only (127.0.0.1 admin). Episodes are the primary
unit now: auto-pick groups N unused posts into a single 50-min newscast
video. Single-post generation is still supported for backward compat.

Manual triggers run the pipeline in a background task. Progress is
observable via the video card's status badge + stage display.
"""
from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, BackgroundTasks, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import delete, desc, select

from ..config import IMAGES_DIR, POSTS_DIR, VIDEOS_DIR
from ..db import session_scope
from ..models_db import EpisodeTopic, PostHistory, Video, VideoRun
from ..settings_store import get_settings
from ..video_pipeline import VideoPipeline
from ..video_worker import (
    _finish_video_run,
    _has_hero_image,
    _has_post_translation,
    _pick_next_episode,
    _read_post_meta,
    _resolve_hero_path,
    _resolve_post_path,
    _start_video_run,
    _upsert_video_row,
)

router = APIRouter(prefix="/videos")


# ----------------------------------------------------------------------
# List page
# ----------------------------------------------------------------------


@router.get("", response_class=HTMLResponse)
async def list_videos(request: Request) -> HTMLResponse:
    from ..main import templates

    with session_scope() as s:
        rows = (
            s.execute(select(Video).order_by(desc(Video.created_at)).limit(100))
            .scalars()
            .all()
        )
        slugs = [r.post_slug for r in rows]
        title_map: dict[str, str] = {}
        if slugs:
            title_rows = s.execute(
                select(PostHistory.slug, PostHistory.title).where(
                    PostHistory.slug.in_(slugs)
                )
            ).all()
            title_map = {row[0]: (row[1] or row[0]) for row in title_rows}

        # Episode topic lists (for episode cards).
        episode_topics_map: dict[str, list[dict]] = {}
        for slug in slugs:
            if slug.startswith("episode-"):
                et_rows = s.execute(
                    select(EpisodeTopic.post_slug, EpisodeTopic.position)
                    .where(EpisodeTopic.episode_slug == slug)
                    .order_by(EpisodeTopic.position.asc())
                ).all()
                if et_rows:
                    topics_list = []
                    for et_slug, pos in et_rows:
                        et_title = title_map.get(et_slug)
                        if not et_title:
                            ph = s.execute(
                                select(PostHistory.title).where(PostHistory.slug == et_slug)
                            ).first()
                            et_title = ph[0] if ph else et_slug
                        topics_list.append({"slug": et_slug, "title": et_title, "position": pos})
                    episode_topics_map[slug] = topics_list

        # Latest VideoRun per video for stage display.
        run_stage_map: dict[int, str] = {}
        for r in rows:
            if r.status == "running":
                latest_run = s.execute(
                    select(VideoRun.stage)
                    .where(VideoRun.video_id == r.id)
                    .order_by(desc(VideoRun.id))
                    .limit(1)
                ).first()
                if latest_run and latest_run[0]:
                    run_stage_map[r.id] = latest_run[0]

        # Published posts without a video or episode.
        used_in_episodes = set(
            r[0] for r in s.execute(select(EpisodeTopic.post_slug).distinct()).all()
        )
        all_video_slugs = set(
            r[0] for r in s.execute(select(Video.post_slug)).all()
        )
        excluded = all_video_slugs | used_in_episodes
        missing = (
            s.execute(
                select(PostHistory.slug, PostHistory.title, PostHistory.published_at)
                .where(~PostHistory.slug.in_(excluded) if excluded else True)
                .order_by(PostHistory.published_at.asc())
                .limit(50)
            )
            .all()
        )

        videos_view = []
        for r in rows:
            dur_display = None
            if r.duration_seconds:
                mins = int(r.duration_seconds // 60)
                secs = int(r.duration_seconds % 60)
                dur_display = f"{mins}:{secs:02d}"
            videos_view.append(
                {
                    "id": r.id,
                    "slug": r.post_slug,
                    "title": title_map.get(r.post_slug, r.post_slug),
                    "status": r.status,
                    "duration": r.duration_seconds,
                    "duration_display": dur_display,
                    "youtube_video_id": r.youtube_video_id,
                    "youtube_url": r.youtube_url,
                    "youtube_privacy": r.youtube_privacy,
                    "uploaded_at": r.uploaded_at.isoformat() if r.uploaded_at else None,
                    "created_at": r.created_at.isoformat() if r.created_at else None,
                    "last_error": (r.last_error or "")[:200],
                    "thumb_url": _thumb_url(r.thumbnail_path),
                    "fail_count": r.fail_count or 0,
                    "is_episode": r.post_slug.startswith("episode-"),
                    "episode_topics": episode_topics_map.get(r.post_slug, []),
                    "current_stage": run_stage_map.get(r.id, ""),
                }
            )
        missing_view = [
            {
                "slug": m[0],
                "title": m[1] or m[0],
                "published_at": m[2].isoformat() if m[2] else None,
            }
            for m in missing
        ]

    settings = get_settings()
    return templates.TemplateResponse(
        request,
        "videos.html",
        {
            "page": "videos",
            "videos": videos_view,
            "missing": missing_view,
            "enabled": settings.video_generation_enabled,
            "reference_voice_path": settings.video_reference_voice_path,
            "auto_upload": settings.video_auto_upload,
            "default_privacy": settings.youtube_default_privacy,
            "channel_name": settings.youtube_channel_name,
            "daily_cap": settings.youtube_upload_daily_cap,
            "topics_per_episode": settings.topics_per_episode,
        },
    )


# ----------------------------------------------------------------------
# Episode generation
# ----------------------------------------------------------------------


@router.post("/episodes/auto-pick")
async def auto_pick_episode(
    request: Request,
    background: BackgroundTasks,
) -> HTMLResponse:
    """Auto-pick next N unused posts and queue a newscast episode."""
    settings = get_settings()
    episode = _pick_next_episode(
        n=settings.topics_per_episode,
        language=settings.video_language,
        freshness_hours=settings.topics_freshness_hours,
    )
    if episode is None:
        return HTMLResponse(
            '<div class="bg-amber-50 border border-amber-200 p-3 rounded text-sm">'
            "All posts have been broadcast. No unused topics remaining."
            "</div>"
        )

    episode_slug = episode["episode_slug"]
    episode_title = episode["episode_title"]
    topics = episode["topics"]

    video_id = _upsert_video_row(episode_slug)
    run_id = _start_video_run(video_id, trigger="manual-episode")
    background.add_task(
        _run_episode_in_background,
        episode_slug, episode_title, topics, video_id, run_id,
    )

    topic_list_html = "".join(
        f'<li class="text-slate-700">{t["title"][:50]}</li>' for t in topics
    )
    return HTMLResponse(
        f'<div class="bg-blue-50 border border-blue-200 p-4 rounded text-sm">'
        f'<strong>Episode queued!</strong> '
        f'<span class="font-mono text-xs">{episode_slug}</span>'
        f'<p class="text-xs text-slate-500 mt-1">{len(topics)} topics selected '
        f'(oldest-first). 60-120 min estimated.</p>'
        f'<ul class="mt-2 text-xs list-disc list-inside">{topic_list_html}</ul>'
        f"</div>"
    )


@router.post("/episodes/custom")
async def custom_episode(
    request: Request,
    background: BackgroundTasks,
    post_slugs: str = Form(...),
    episode_title: str = Form(""),
) -> HTMLResponse:
    """Create an episode from user-selected posts."""
    slugs = [s.strip() for s in post_slugs.split(",") if s.strip()]
    if len(slugs) < 2:
        return HTMLResponse(
            '<div class="bg-rose-50 border border-rose-200 p-3 rounded text-sm">'
            "Select at least 2 posts to create an episode."
            "</div>",
            status_code=400,
        )

    settings = get_settings()
    language = settings.video_language or "en"

    topics = []
    errors = []
    for slug in slugs:
        with session_scope() as s:
            row = s.execute(
                select(PostHistory).where(PostHistory.slug == slug)
            ).scalar_one_or_none()
        if row is None:
            errors.append(f"Post not found: {slug}")
            continue
        if not _has_hero_image(slug):
            errors.append(f"No hero image: {slug}")
            continue
        if not _has_post_translation(slug, language):
            errors.append(f"No {language} translation: {slug}")
            continue
        post_path = _resolve_post_path(slug, language)
        hero_path = _resolve_hero_path(slug)
        if not post_path or not hero_path:
            errors.append(f"Missing files: {slug}")
            continue
        meta = _read_post_meta(slug, language=language)
        topics.append(
            {
                "slug": slug,
                "title": row.title or slug,
                "description": meta.get("description", ""),
                "post_path": str(post_path),
                "hero_path": str(hero_path),
                "tags": meta.get("tags", []),
            }
        )

    if errors:
        err_html = "<br>".join(errors)
        return HTMLResponse(
            f'<div class="bg-rose-50 border border-rose-200 p-3 rounded text-sm">'
            f"{err_html}</div>",
            status_code=400,
        )
    if len(topics) < 2:
        return HTMLResponse(
            '<div class="bg-rose-50 border border-rose-200 p-3 rounded text-sm">'
            "Not enough valid posts after filtering.</div>",
            status_code=400,
        )

    now = datetime.now(timezone.utc)
    ep_slug = f"episode-custom-{now:%Y%m%d-%H%M%S}"
    ep_title = episode_title.strip() or f"AI News Daily — {now:%B %d, %Y}"

    video_id = _upsert_video_row(ep_slug)
    run_id = _start_video_run(video_id, trigger="manual-custom")
    background.add_task(
        _run_episode_in_background,
        ep_slug, ep_title, topics, video_id, run_id,
    )

    topic_list_html = "".join(
        f'<li class="text-slate-700">{t["title"][:50]}</li>' for t in topics
    )
    return HTMLResponse(
        f'<div class="bg-blue-50 border border-blue-200 p-4 rounded text-sm">'
        f'<strong>Custom episode queued!</strong> '
        f'<span class="font-mono text-xs">{ep_slug}</span>'
        f'<p class="text-xs text-slate-500 mt-1">{len(topics)} topics. '
        f'60-120 min estimated.</p>'
        f'<ul class="mt-2 text-xs list-disc list-inside">{topic_list_html}</ul>'
        f"</div>"
    )


# ----------------------------------------------------------------------
# Single-post actions (backward compat)
# ----------------------------------------------------------------------


@router.post("/trigger")
async def trigger_video(
    request: Request,
    background: BackgroundTasks,
    slug: str = Form(...),
) -> HTMLResponse:
    """Manually kick off video generation for a single published post."""
    slug = slug.strip()
    post_path = Path(POSTS_DIR) / f"{slug}.md"
    if not post_path.exists():
        raise HTTPException(status_code=404, detail=f"post {slug} not found")

    video_id = _upsert_video_row(slug)
    run_id = _start_video_run(video_id, trigger="manual")
    background.add_task(_run_single_in_background, slug, video_id, run_id)

    return HTMLResponse(
        f'<div class="bg-blue-50 border border-blue-200 p-3 rounded text-sm">'
        f'Video generation queued for <span class="font-mono">{slug}</span>.'
        f"</div>"
    )


@router.post("/{video_id}/regenerate")
async def regenerate_video(video_id: int, background: BackgroundTasks) -> HTMLResponse:
    with session_scope() as s:
        row = s.get(Video, video_id)
        if row is None:
            raise HTTPException(status_code=404, detail="video not found")
        slug = row.post_slug
        row.status = "running"
        row.last_error = None

    for ext in ("wav", "mp4", "jpg", "srt"):
        p = Path(VIDEOS_DIR) / f"{slug}.{ext}"
        try:
            p.unlink(missing_ok=True)
        except Exception:
            pass

    run_id = _start_video_run(video_id, trigger="retry")

    # Episode regeneration: re-pick the same topics.
    if slug.startswith("episode-"):
        with session_scope() as s:
            et_rows = s.execute(
                select(EpisodeTopic.post_slug)
                .where(EpisodeTopic.episode_slug == slug)
                .order_by(EpisodeTopic.position.asc())
            ).all()
        if et_rows:
            settings = get_settings()
            language = settings.video_language or "en"
            topics = []
            for (et_slug,) in et_rows:
                post_path = _resolve_post_path(et_slug, language)
                hero_path = _resolve_hero_path(et_slug)
                meta = _read_post_meta(et_slug, language=language)
                if post_path and hero_path:
                    with session_scope() as s:
                        ph = s.execute(
                            select(PostHistory.title).where(PostHistory.slug == et_slug)
                        ).first()
                    topics.append({
                        "slug": et_slug,
                        "title": (ph[0] if ph else et_slug) or et_slug,
                        "description": meta.get("description", ""),
                        "post_path": str(post_path),
                        "hero_path": str(hero_path),
                        "tags": meta.get("tags", []),
                    })
            if topics:
                background.add_task(
                    _run_episode_in_background,
                    slug, f"AI News Daily (regen)", topics, video_id, run_id,
                )
                return HTMLResponse(
                    f'<div class="bg-blue-50 border border-blue-200 p-3 rounded text-sm">'
                    f'Episode regeneration queued ({len(topics)} topics).</div>'
                )

    background.add_task(_run_single_in_background, slug, video_id, run_id)
    return HTMLResponse(
        f'<div class="bg-blue-50 border border-blue-200 p-3 rounded text-sm">'
        f'Regeneration queued for <span class="font-mono">{slug}</span>.</div>'
    )


@router.post("/{video_id}/upload")
async def upload_only(video_id: int, background: BackgroundTasks) -> HTMLResponse:
    with session_scope() as s:
        row = s.get(Video, video_id)
        if row is None:
            raise HTTPException(status_code=404, detail="video not found")
        if not row.mp4_path or not Path(row.mp4_path).exists():
            raise HTTPException(status_code=400, detail="mp4 missing; regenerate first")
        if row.youtube_video_id:
            return HTMLResponse(
                f'<div class="bg-amber-50 p-3 rounded text-sm">Already uploaded: '
                f'<a href="{row.youtube_url}" class="text-indigo-600">{row.youtube_url}</a></div>'
            )

    background.add_task(_upload_in_background, video_id)
    return HTMLResponse(
        '<div class="bg-blue-50 border border-blue-200 p-3 rounded text-sm">'
        "Upload to YouTube queued.</div>"
    )


@router.post("/{video_id}/publish")
async def publish_public(video_id: int) -> HTMLResponse:
    result = await _change_privacy(video_id, "public")
    return HTMLResponse(
        '<div class="bg-emerald-50 border border-emerald-200 p-3 rounded text-sm">'
        "Video set to public.</div>"
    )


@router.post("/{video_id}/unpublish")
async def unpublish(video_id: int) -> HTMLResponse:
    await _change_privacy(video_id, "unlisted")
    return HTMLResponse(
        '<div class="bg-amber-50 border border-amber-200 p-3 rounded text-sm">'
        "Video set to unlisted.</div>"
    )


@router.delete("/{video_id}")
async def delete_video(video_id: int) -> HTMLResponse:
    with session_scope() as s:
        row = s.get(Video, video_id)
        if row is None:
            raise HTTPException(status_code=404, detail="video not found")
        slug = row.post_slug
        had_youtube = bool(row.youtube_video_id)
        s.execute(delete(VideoRun).where(VideoRun.video_id == video_id))
        s.execute(delete(Video).where(Video.id == video_id))

    for ext in ("wav", "mp4", "jpg", "srt"):
        p = Path(VIDEOS_DIR) / f"{slug}.{ext}"
        try:
            p.unlink(missing_ok=True)
        except Exception:
            pass

    note = "YouTube video NOT deleted" if had_youtube else "no YouTube upload"
    return HTMLResponse(
        f'<div class="bg-slate-50 border border-slate-200 p-3 rounded text-sm">'
        f'Deleted <span class="font-mono">{slug}</span>. {note}.</div>'
    )


# ----------------------------------------------------------------------
# Background wrappers
# ----------------------------------------------------------------------


def _run_single_in_background(slug: str, video_id: int, run_id: int) -> None:
    """Execute single-post video pipeline in background."""
    from ..video_worker import _run_video_pipeline_sync

    try:
        with session_scope() as s:
            row = s.execute(
                select(PostHistory).where(PostHistory.slug == slug)
            ).scalar_one_or_none()
            title = (row.title if row else slug) or slug

        settings = get_settings()
        language = settings.video_language or "en"
        post_path = _resolve_post_path(slug, language)
        hero_path = _resolve_hero_path(slug)
        meta = _read_post_meta(slug, language=language)

        topics = [
            {
                "slug": slug,
                "title": title,
                "description": meta.get("description", ""),
                "post_path": str(post_path) if post_path else "",
                "hero_path": str(hero_path) if hero_path else "",
                "tags": meta.get("tags", []),
            }
        ]
        result = _run_video_pipeline_sync(slug, title, topics, video_id, run_id)
        _finish_video_run(
            video_id, run_id,
            success=bool(result and result.success),
            error=None if result and result.success else (result.error if result else "unknown"),
            result=result,
        )
    except Exception as e:
        _finish_video_run(
            video_id, run_id, success=False,
            error=f"{type(e).__name__}: {e}", result=None,
        )


def _run_episode_in_background(
    episode_slug: str,
    episode_title: str,
    topics: list[dict],
    video_id: int,
    run_id: int,
) -> None:
    """Execute the full episode pipeline synchronously in background."""
    from ..video_worker import _run_video_pipeline_sync

    try:
        result = _run_video_pipeline_sync(
            episode_slug, episode_title, topics, video_id, run_id,
        )
        _finish_video_run(
            video_id, run_id,
            success=bool(result and result.success),
            error=None if result and result.success else (result.error if result else "unknown"),
            result=result,
        )
    except Exception as e:
        _finish_video_run(
            video_id, run_id, success=False,
            error=f"{type(e).__name__}: {e}", result=None,
        )


def _upload_in_background(video_id: int) -> None:
    from scripts.agents.youtube_uploader import YouTubeUploaderAgent

    with session_scope() as s:
        row = s.get(Video, video_id)
        if row is None or not row.mp4_path:
            return
        slug = row.post_slug
        mp4 = row.mp4_path
        thumb = row.thumbnail_path

        meta = _read_post_meta(slug)
        title = meta.get("title") or slug
        desc = meta.get("description") or ""
        tags = meta.get("tags") or []

    settings = get_settings()
    run_id = _start_video_run(video_id, trigger="manual-upload")
    uploader = YouTubeUploaderAgent()
    try:
        up = uploader.run(
            mp4_path=mp4,
            title=title,
            description=desc,
            tags=tags + ["AI", "AINews"],
            privacy=settings.youtube_default_privacy,
            thumbnail_path=thumb,
        )
    except Exception as e:
        with session_scope() as s:
            row = s.get(Video, video_id)
            if row is not None:
                row.last_error = f"upload error: {e}"[:2000]
            r = s.get(VideoRun, run_id)
            if r is not None:
                r.status = "failed"
                r.ended_at = datetime.utcnow()
                r.error = f"{type(e).__name__}: {e}"[:2000]
        return

    with session_scope() as s:
        row = s.get(Video, video_id)
        if row is None:
            return
        if up is not None:
            row.youtube_video_id = up.video_id
            row.youtube_url = up.url
            row.youtube_privacy = up.privacy
            row.uploaded_at = datetime.utcnow()
            row.status = "uploaded"
            row.last_error = None
        else:
            row.last_error = "upload returned None"
        r = s.get(VideoRun, run_id)
        if r is not None:
            r.status = "success" if up else "failed"
            r.ended_at = datetime.utcnow()


async def _change_privacy(video_id: int, privacy: str) -> None:
    from scripts.agents.youtube_uploader import YouTubeUploaderAgent

    with session_scope() as s:
        row = s.get(Video, video_id)
        if row is None:
            raise HTTPException(status_code=404, detail="video not found")
        yt_id = row.youtube_video_id
    if not yt_id:
        raise HTTPException(status_code=400, detail="video not uploaded yet")

    uploader = YouTubeUploaderAgent()
    ok = await asyncio.to_thread(uploader.update_privacy, yt_id, privacy)
    if not ok:
        raise HTTPException(status_code=500, detail="privacy update failed")

    with session_scope() as s:
        row = s.get(Video, video_id)
        if row is not None:
            row.youtube_privacy = privacy


# ----------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------


def _thumb_url(thumbnail_path: Optional[str]) -> Optional[str]:
    if not thumbnail_path:
        return None
    try:
        name = Path(thumbnail_path).name
        return f"/videos-data/{name}"
    except Exception:
        return None
