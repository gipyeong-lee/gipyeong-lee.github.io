"""Pipeline monitor + manual trigger + SSE stream."""
from __future__ import annotations

import asyncio
import html
import json
from typing import Optional

from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import select
from sse_starlette.sse import EventSourceResponse

from ..daemon import (
    current_run_id,
    is_running,
    pipeline_locked,
    trigger_manual,
)
from ..db import session_scope
from ..logging_bus import log_bus, logs_for_run
from ..models_db import Run
from ..queue_service import pick_next
from ..settings_store import get_settings

router = APIRouter(prefix="/pipeline")


_STAGE_ORDER = ["research", "write", "fact_check", "edit", "image", "translate"]


def _compute_initial_stage_states(logs: list[dict]) -> dict[str, str]:
    """Replay persisted logs to figure out each stage's current state.

    Returns a dict like {'research': 'ok', 'write': 'ok', 'fact_check': 'running', ...}
    so the initial HTML render matches the truth without waiting for an SSE event.
    """
    states: dict[str, str] = {s: "idle" for s in _STAGE_ORDER}
    for entry in logs:
        msg = (entry.get("message") or "").lower()
        stage = entry.get("stage")
        if not stage or stage not in states:
            continue
        if "stage start" in msg:
            states[stage] = "running"
        elif "stage end" in msg:
            # Check if it ended ok or fail — heuristic on the rendered message
            states[stage] = "fail" if "fail" in msg else "ok"
    return states


@router.get("", response_class=HTMLResponse)
async def pipeline_page(request: Request) -> HTMLResponse:
    from ..main import templates

    run_id = current_run_id()
    logs: list = []
    run_row = None
    if run_id:
        logs = logs_for_run(run_id, limit=500)
        with session_scope() as s:
            r = s.get(Run, run_id)
            if r is not None:
                s.expunge(r)
                run_row = r

    stage_states = _compute_initial_stage_states(logs)

    return templates.TemplateResponse(
        request,
        "pipeline.html",
        {
            "page": "pipeline",
            "current_run_id": run_id,
            "current_run": run_row,
            "logs": logs,
            "stage_order": _STAGE_ORDER,
            "stage_states": stage_states,
            "locked": pipeline_locked(),
            "running": is_running(),
        },
    )


@router.get("/stream")
async def pipeline_stream(request: Request):
    """SSE stream of pipeline events."""

    async def event_generator():
        q = log_bus.subscribe()
        try:
            while True:
                if await request.is_disconnected():
                    break
                try:
                    event = await asyncio.wait_for(q.get(), timeout=15.0)
                except asyncio.TimeoutError:
                    # keepalive comment line
                    yield {"event": "ping", "data": ""}
                    continue
                yield {
                    "event": event.kind,
                    "data": json.dumps(
                        {
                            "run_id": event.run_id,
                            "stage": event.stage,
                            "level": event.level,
                            "message": event.message,
                            "meta": event.meta,
                            "ts": event.ts.isoformat(),
                        },
                        default=str,
                    ),
                }
        finally:
            log_bus.unsubscribe(q)

    return EventSourceResponse(event_generator())


def _toast(message: str, kind: str = "info") -> HTMLResponse:
    """Return a small HTMX-swappable toast fragment."""
    colors = {
        "info": "bg-blue-100 text-blue-800 border-blue-300",
        "ok": "bg-emerald-100 text-emerald-800 border-emerald-300",
        "warn": "bg-amber-100 text-amber-800 border-amber-300",
        "error": "bg-rose-100 text-rose-800 border-rose-300",
    }
    cls = colors.get(kind, colors["info"])
    # Auto-hide after 6s via inline script on the toast element itself.
    html = (
        f'<div class="px-3 py-2 border rounded text-sm {cls}" '
        f'x-data style="animation: fadeout 6s forwards">'
        f'{message}'
        f'</div>'
        f'<style>@keyframes fadeout {{ 0%,80% {{opacity:1}} 100% {{opacity:0}} }}</style>'
    )
    return HTMLResponse(html)


def _is_htmx(request: Request) -> bool:
    return request.headers.get("hx-request", "").lower() == "true"


@router.post("/trigger")
async def pipeline_trigger(
    request: Request,
    topic_id: Optional[int] = Form(None),
    custom_topic: Optional[str] = Form(None),
    custom_url: Optional[str] = Form(None),
):
    """Trigger a pipeline run.

    Resolution order:
      1. `topic_id` if supplied → run that specific queued topic.
      2. `custom_topic` if supplied → run with custom title (+ optional url).
      3. Neither supplied → auto-pick highest-scored queued topic that
         hasn't been published yet. The `pick_next` helper already excludes
         topics in cooldown, blocked, or matching the blocklist, and
         `mark_status` ensures it won't be picked again.
    """
    htmx = _is_htmx(request)

    if pipeline_locked():
        msg = (
            f"⏳ 이미 파이프라인이 실행 중입니다 (run #{current_run_id()}). "
            f"<a class='underline' href='/pipeline'>모니터 보기</a>"
        )
        if htmx:
            return _toast(msg, "warn")
        raise HTTPException(status_code=409, detail="pipeline already running")

    # Normalize "empty string" custom_topic → None (HTML forms may send "")
    custom_topic = (custom_topic or "").strip() or None
    custom_url = (custom_url or "").strip() or None

    auto_picked_title: Optional[str] = None
    if not topic_id and not custom_topic:
        settings = get_settings()
        topic = pick_next(
            cooldown_seconds=settings.cooldown_after_fail_seconds,
            max_fail_count=settings.max_fail_count_before_block,
            blocklist=settings.keyword_blocklist,
        )
        if topic is None:
            msg = "🚫 큐가 비어있습니다. Topics 페이지에서 수동 추가하거나 소스 폴링을 기다리세요."
            if htmx:
                return _toast(msg, "warn")
            raise HTTPException(status_code=400, detail="queue empty")
        topic_id = topic.id
        auto_picked_title = topic.title

    # Fire-and-forget — the scheduler loop will observe the lock.
    asyncio.create_task(
        _trigger_bg(topic_id, custom_topic, custom_url),
        name="manual_trigger",
    )

    if htmx:
        if auto_picked_title:
            safe = html.escape(auto_picked_title[:80])
            label = f"자동 선택 토픽: <b>{safe}</b>"
        elif topic_id:
            label = f"topic #{int(topic_id)} 파이프라인 시작됨"
        else:
            safe = html.escape((custom_topic or "")[:80])
            label = f"커스텀 토픽: <b>{safe}</b>"
        return _toast(
            f"🚀 파이프라인 실행 시작. "
            f"<a class='underline' href='/pipeline'>실시간 모니터</a><br>"
            f"<span class='text-xs opacity-75'>{label}</span>",
            "ok",
        )

    return JSONResponse(
        {
            "status": "accepted",
            "topic_id": topic_id,
            "auto_picked_title": auto_picked_title,
        },
        status_code=202,
    )


async def _trigger_bg(topic_id, custom_topic, custom_url):
    try:
        await trigger_manual(
            topic_id=topic_id, custom_topic=custom_topic, custom_url=custom_url
        )
    except Exception as e:
        import logging

        logging.getLogger("aiblog.trigger").exception("manual trigger failed: %s", e)


@router.get("/runs")
async def list_runs(limit: int = 20) -> JSONResponse:
    with session_scope() as s:
        rows = (
            s.execute(select(Run).order_by(Run.started_at.desc()).limit(limit))
            .scalars()
            .all()
        )
        return JSONResponse(
            [
                {
                    "id": r.id,
                    "topic_id": r.topic_id,
                    "trigger": r.trigger,
                    "stage": r.stage,
                    "status": r.status,
                    "started_at": r.started_at.isoformat() if r.started_at else None,
                    "ended_at": r.ended_at.isoformat() if r.ended_at else None,
                    "revision_count": r.revision_count,
                    "final_slug": r.final_slug,
                    "error": r.error,
                    "fact_check_verdict": r.fact_check_verdict,
                    "git_commit_sha": r.git_commit_sha,
                }
                for r in rows
            ]
        )
