"""Videos routes — list, detail, manual trigger, upload, publish/unpublish.

All operations are local-only (127.0.0.1 admin) and reference video rows
by primary key. The generated mp4/wav/jpg files live under
`scripts/app/data/videos/` which is mounted at `/videos-data/` by main.py.

Manual triggers run the video pipeline in a background task instead of
holding the request open, because the pipeline can take 2-3 minutes.
Progress is observable via polling the video row status.
"""
from __future__ import annotations

import asyncio
from datetime import datetime
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, BackgroundTasks, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import delete, desc, select

from ..config import POSTS_DIR, VIDEOS_DIR
from ..db import session_scope
from ..models_db import PostHistory, Video, VideoRun
from ..settings_store import get_settings
from ..video_pipeline import VideoPipeline
from ..video_worker import _read_post_meta, _start_video_run, _upsert_video_row, _finish_video_run

router = APIRouter(prefix="/videos")


# ----------------------------------------------------------------------
# List + detail pages
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
        # Attach post titles via a separate lookup (simpler than a join).
        slugs = [r.post_slug for r in rows]
        title_map: dict[str, str] = {}
        if slugs:
            title_rows = s.execute(
                select(PostHistory.slug, PostHistory.title).where(PostHistory.slug.in_(slugs))
            ).all()
            title_map = {row[0]: (row[1] or row[0]) for row in title_rows}

        # Also find published posts that do NOT have a video row yet — the user
        # can trigger them from the UI.
        missing = (
            s.execute(
                select(PostHistory.slug, PostHistory.title, PostHistory.published_at)
                .where(~PostHistory.slug.in_(select(Video.post_slug)))
                .order_by(desc(PostHistory.published_at))
                .limit(20)
            )
            .all()
        )
        videos_view = [
            {
                "id": r.id,
                "slug": r.post_slug,
                "title": title_map.get(r.post_slug, r.post_slug),
                "status": r.status,
                "duration": r.duration_seconds,
                "youtube_video_id": r.youtube_video_id,
                "youtube_url": r.youtube_url,
                "youtube_privacy": r.youtube_privacy,
                "uploaded_at": r.uploaded_at.isoformat() if r.uploaded_at else None,
                "created_at": r.created_at.isoformat() if r.created_at else None,
                "last_error": (r.last_error or "")[:200],
                "thumb_url": _thumb_url(r.thumbnail_path),
                "fail_count": r.fail_count or 0,
            }
            for r in rows
        ]
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
        },
    )


# ----------------------------------------------------------------------
# Manual actions
# ----------------------------------------------------------------------


@router.post("/trigger")
async def trigger_video(
    request: Request,
    background: BackgroundTasks,
    slug: str = Form(...),
) -> JSONResponse:
    """Manually kick off video generation for a specific published slug."""
    slug = slug.strip()
    post_path = Path(POSTS_DIR) / f"{slug}.md"
    if not post_path.exists():
        raise HTTPException(status_code=404, detail=f"post {slug} not found")

    video_id = _upsert_video_row(slug)
    run_id = _start_video_run(video_id, trigger="manual")

    background.add_task(_run_in_background, slug, video_id, run_id)

    return JSONResponse(
        {"status": "queued", "video_id": video_id, "run_id": run_id, "slug": slug}
    )


@router.post("/{video_id}/regenerate")
async def regenerate_video(video_id: int, background: BackgroundTasks) -> JSONResponse:
    with session_scope() as s:
        row = s.get(Video, video_id)
        if row is None:
            raise HTTPException(status_code=404, detail="video not found")
        slug = row.post_slug
        row.status = "running"
        row.last_error = None

    # Remove stale output files so compose/tts produce fresh ones.
    for ext in ("wav", "mp4", "jpg"):
        p = Path(VIDEOS_DIR) / f"{slug}.{ext}"
        try:
            p.unlink(missing_ok=True)
        except Exception:
            pass

    run_id = _start_video_run(video_id, trigger="retry")
    background.add_task(_run_in_background, slug, video_id, run_id)
    return JSONResponse({"status": "queued", "video_id": video_id, "slug": slug})


@router.post("/{video_id}/upload")
async def upload_only(video_id: int, background: BackgroundTasks) -> JSONResponse:
    """Upload an existing (success) video that wasn't auto-uploaded."""
    with session_scope() as s:
        row = s.get(Video, video_id)
        if row is None:
            raise HTTPException(status_code=404, detail="video not found")
        if not row.mp4_path or not Path(row.mp4_path).exists():
            raise HTTPException(status_code=400, detail="mp4 missing; regenerate first")
        if row.youtube_video_id:
            return JSONResponse({"status": "already_uploaded", "url": row.youtube_url})

    background.add_task(_upload_in_background, video_id)
    return JSONResponse({"status": "upload_queued", "video_id": video_id})


@router.post("/{video_id}/publish")
async def publish_public(video_id: int) -> JSONResponse:
    return await _change_privacy(video_id, "public")


@router.post("/{video_id}/unpublish")
async def unpublish(video_id: int) -> JSONResponse:
    return await _change_privacy(video_id, "unlisted")


@router.delete("/{video_id}")
async def delete_video(video_id: int) -> JSONResponse:
    """Delete local files + DB rows. Does NOT delete from YouTube."""
    with session_scope() as s:
        row = s.get(Video, video_id)
        if row is None:
            raise HTTPException(status_code=404, detail="video not found")
        slug = row.post_slug
        had_youtube = bool(row.youtube_video_id)
        s.execute(delete(VideoRun).where(VideoRun.video_id == video_id))
        s.execute(delete(Video).where(Video.id == video_id))

    for ext in ("wav", "mp4", "jpg"):
        p = Path(VIDEOS_DIR) / f"{slug}.{ext}"
        try:
            p.unlink(missing_ok=True)
        except Exception:
            pass

    return JSONResponse({
        "status": "deleted",
        "slug": slug,
        "note": "YouTube video NOT deleted" if had_youtube else "no YouTube upload to remove",
    })


# ----------------------------------------------------------------------
# Background wrappers
# ----------------------------------------------------------------------


def _run_in_background(slug: str, video_id: int, run_id: int) -> None:
    """Execute the full video pipeline synchronously in the request worker thread."""
    from ..video_worker import _run_video_pipeline_sync

    try:
        with session_scope() as s:
            row = s.execute(
                select(PostHistory).where(PostHistory.slug == slug)
            ).scalar_one_or_none()
            title = (row.title if row else slug) or slug

        result = _run_video_pipeline_sync(slug, title, video_id, run_id)
        _finish_video_run(
            video_id,
            run_id,
            success=bool(result and result.success),
            error=None if result and result.success else (result.error if result else "unknown"),
            result=result,
        )
    except Exception as e:
        _finish_video_run(
            video_id,
            run_id,
            success=False,
            error=f"{type(e).__name__}: {e}",
            result=None,
        )


def _upload_in_background(video_id: int) -> None:
    from ..agents.youtube_uploader import YouTubeUploaderAgent

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
            tags=tags + ["AI", "AI뉴스"],
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


async def _change_privacy(video_id: int, privacy: str) -> JSONResponse:
    from ..agents.youtube_uploader import YouTubeUploaderAgent

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

    return JSONResponse({"status": "ok", "video_id": video_id, "privacy": privacy})


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
