"""Topic queue routes."""
from __future__ import annotations

import html
import json
from typing import Optional

from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse

from ..queue_service import (
    add_manual,
    delete_topic,
    list_queue,
    prioritize,
    reset_topic,
)

router = APIRouter(prefix="/topics")


def _is_htmx(request: Request) -> bool:
    return request.headers.get("hx-request", "").lower() == "true"


def _toast(message: str, kind: str = "ok") -> HTMLResponse:
    colors = {
        "info": "bg-blue-100 text-blue-800 border-blue-300",
        "ok": "bg-emerald-100 text-emerald-800 border-emerald-300",
        "warn": "bg-amber-100 text-amber-800 border-amber-300",
        "error": "bg-rose-100 text-rose-800 border-rose-300",
    }
    cls = colors.get(kind, colors["ok"])
    return HTMLResponse(
        f'<div class="px-3 py-2 border rounded text-sm {cls}" '
        f'style="animation: fadeout 5s forwards">{message}</div>'
        f'<style>@keyframes fadeout {{ 0%,70% {{opacity:1}} 100% {{opacity:0}} }}</style>'
    )


@router.get("", response_class=HTMLResponse)
async def topics_page(request: Request) -> HTMLResponse:
    from ..main import templates

    topics = list_queue(limit=200)
    # Parse keyword_hits JSON for display
    view = []
    for t in topics:
        hits = []
        if t.keyword_hits:
            try:
                hits = json.loads(t.keyword_hits)
            except Exception:
                hits = []
        view.append(
            {
                "id": t.id,
                "source": t.source,
                "title": t.title,
                "url": t.url,
                "score": round((t.score or 0) + (t.priority_boost or 0), 3),
                "raw_score": round(t.score or 0, 3),
                "boost": round(t.priority_boost or 0, 3),
                "status": t.status,
                "fail_count": t.fail_count,
                "keyword_hits": hits[:5],
                "last_error": t.last_error,
                "discovered_at": t.discovered_at.isoformat() if t.discovered_at else None,
            }
        )
    return templates.TemplateResponse(
        request,
        "topics.html",
        {"page": "topics", "topics": view},
    )


@router.post("")
async def add_topic(
    request: Request,
    title: str = Form(...),
    url: Optional[str] = Form(None),
):
    if not title.strip():
        if _is_htmx(request):
            return _toast("❌ 제목이 필요합니다", "error")
        raise HTTPException(status_code=400, detail="title required")
    tid = add_manual(title.strip(), url=url)
    if _is_htmx(request):
        safe = html.escape(title.strip()[:80])
        return _toast(f"➕ 토픽 추가됨 #{tid}: <b>{safe}</b>", "ok")
    return JSONResponse({"status": "added", "topic_id": tid})


@router.delete("/{topic_id}")
async def remove_topic(request: Request, topic_id: int):
    delete_topic(topic_id)
    if _is_htmx(request):
        return _toast(f"🗑 topic #{topic_id} 삭제됨", "ok")
    return JSONResponse({"status": "deleted"})


@router.post("/{topic_id}/prioritize")
async def bump_topic(request: Request, topic_id: int):
    prioritize(topic_id, 1.0)
    if _is_htmx(request):
        return _toast(f"⬆ topic #{topic_id} 우선순위 +1", "ok")
    return JSONResponse({"status": "prioritized"})


@router.post("/{topic_id}/reset")
async def reset(request: Request, topic_id: int):
    reset_topic(topic_id)
    if _is_htmx(request):
        return _toast(f"🔄 topic #{topic_id} 재활성화됨", "ok")
    return JSONResponse({"status": "reset"})
