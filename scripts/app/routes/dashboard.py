"""Dashboard route: overview of daemon status, recent runs, counts."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from sqlalchemy import func, select

from ..daemon import current_run_id, get_last_run_at, is_running, pipeline_locked
from ..db import session_scope
from ..models_db import PostHistory, Run, Topic
from ..settings_store import get_settings

router = APIRouter()


def _counts() -> dict:
    since_24h = datetime.now(timezone.utc) - timedelta(hours=24)
    with session_scope() as s:
        posts_24h = s.execute(
            select(func.count(PostHistory.id)).where(PostHistory.published_at >= since_24h)
        ).scalar_one()
        posts_total = s.execute(select(func.count(PostHistory.id))).scalar_one()
        queue_size = s.execute(
            select(func.count(Topic.id)).where(Topic.status == "queued")
        ).scalar_one()
        failed_topics = s.execute(
            select(func.count(Topic.id)).where(Topic.status.in_(["failed", "blocked"]))
        ).scalar_one()
        runs_recent = (
            s.execute(
                select(Run).order_by(Run.started_at.desc()).limit(5)
            )
            .scalars()
            .all()
        )
        for r in runs_recent:
            s.expunge(r)
    return {
        "posts_24h": posts_24h,
        "posts_total": posts_total,
        "queue_size": queue_size,
        "failed_topics": failed_topics,
        "runs_recent": runs_recent,
    }


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request) -> HTMLResponse:
    from ..main import templates

    data = _counts()
    settings = get_settings()
    last_run = get_last_run_at()
    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {
            "page": "dashboard",
            "data": data,
            "settings": settings,
            "daemon": {
                "running": is_running(),
                "pipeline_locked": pipeline_locked(),
                "last_run_at": last_run.isoformat() if last_run else None,
                "current_run_id": current_run_id(),
            },
        },
    )
