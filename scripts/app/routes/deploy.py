"""Deploy incidents admin page.

GET /deploy                 — list recent DeployIncident rows
POST /deploy/scan           — manual trigger of one deploy_watcher tick
POST /deploy/{id}/retry     — re-run the auto-fix handler for an incident
"""
from __future__ import annotations

import asyncio
import json
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import desc, select

from ..db import session_scope
from ..models_db import DeployIncident

router = APIRouter(prefix="/deploy")


@router.get("", response_class=HTMLResponse)
async def list_incidents(request: Request) -> HTMLResponse:
    from ..main import templates

    with session_scope() as s:
        rows = (
            s.execute(
                select(DeployIncident)
                .order_by(desc(DeployIncident.created_at))
                .limit(50)
            )
            .scalars()
            .all()
        )
        view = [
            {
                "id": r.id,
                "gh_run_id": r.gh_run_id,
                "category": r.category,
                "auto_applied": bool(r.auto_applied),
                "fix_commit_sha": (r.fix_commit_sha or "")[:12],
                "commit_sha": (r.commit_sha or "")[:12],
                "root_cause": (r.root_cause or "")[:300],
                "suggested_fix": (r.suggested_fix or "")[:400],
                "fix_error": (r.fix_error or "")[:400],
                "created_at": r.created_at.isoformat() if r.created_at else None,
                "started_at": r.started_at.isoformat() if r.started_at else None,
                "evidence": _parse_evidence(r.evidence),
            }
            for r in rows
        ]

    return templates.TemplateResponse(
        request,
        "deploy.html",
        {"page": "deploy", "incidents": view},
    )


@router.post("/scan")
async def manual_scan() -> JSONResponse:
    """Force one tick of the deploy watcher immediately."""
    from ..deploy_watcher import _tick

    try:
        await _tick()
        return JSONResponse({"status": "ok"})
    except Exception as e:
        return JSONResponse(
            {"status": "error", "error": str(e)}, status_code=500
        )


@router.post("/{incident_id}/retry")
async def retry_fix(incident_id: int) -> JSONResponse:
    """Manually re-dispatch the fix handler for a given incident."""
    from ..deploy_watcher import (
        _commit_and_push_fix,
        _mark_incident_applied,
        _run_fix,
        _update_incident_fix_error,
    )
    from ..diagnostics import classify_deploy_error

    with session_scope() as s:
        row = s.get(DeployIncident, incident_id)
        if row is None:
            raise HTTPException(status_code=404, detail="incident not found")
        category = row.category
        evidence = _parse_evidence(row.evidence)

    # Reconstruct fix params by re-classifying from the stored log tail.
    log_tail = (evidence or {}).get("log_tail") or ""
    diagnosis = classify_deploy_error(log_tail)
    if not diagnosis.auto_apply or not diagnosis.fix_fn:
        raise HTTPException(
            status_code=400, detail=f"category {category} has no auto-fix handler"
        )

    ok, detail, modified_file = await asyncio.to_thread(
        _run_fix, diagnosis.fix_fn, diagnosis.fix_params
    )
    if not ok:
        await asyncio.to_thread(_update_incident_fix_error, incident_id, detail)
        return JSONResponse({"status": "fix_failed", "detail": detail}, status_code=500)

    pushed, sha, push_detail = await asyncio.to_thread(
        _commit_and_push_fix, category, detail, modified_file or ""
    )
    if not pushed:
        await asyncio.to_thread(_update_incident_fix_error, incident_id, push_detail)
        return JSONResponse(
            {"status": "push_failed", "detail": push_detail}, status_code=500
        )

    await asyncio.to_thread(_mark_incident_applied, incident_id, sha, detail)
    return JSONResponse(
        {"status": "applied", "commit_sha": sha, "detail": detail}
    )


def _parse_evidence(blob: Optional[str]) -> Optional[dict]:
    if not blob:
        return None
    try:
        return json.loads(blob)
    except json.JSONDecodeError:
        return None
