"""Diagnosis admin routes — view auto-generated failure analyses."""
from __future__ import annotations

import json

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse

from ..diagnostics import diagnose_run, list_diagnoses, sweep_recent_failures

router = APIRouter(prefix="/diagnoses")


@router.get("", response_class=HTMLResponse)
async def diagnoses_page(request: Request) -> HTMLResponse:
    from ..main import templates

    rows = list_diagnoses(limit=100)
    view = []
    for d in rows:
        try:
            evidence = json.loads(d.evidence) if d.evidence else {}
        except Exception:
            evidence = {"_raw": d.evidence}
        view.append(
            {
                "id": d.id,
                "run_id": d.run_id,
                "category": d.category,
                "root_cause": d.root_cause,
                "evidence": evidence,
                "suggested_fix": d.suggested_fix,
                "auto_applied": bool(d.auto_applied),
                "created_at": d.created_at.isoformat() if d.created_at else None,
            }
        )
    return templates.TemplateResponse(
        request,
        "diagnoses.html",
        {"page": "diagnoses", "diagnoses": view},
    )


@router.post("/sweep")
async def sweep() -> JSONResponse:
    """Manually trigger a diagnosis sweep (normally runs every tick)."""
    new_ids = sweep_recent_failures(limit=100)
    return JSONResponse({"status": "ok", "diagnosed": new_ids})


@router.post("/{run_id}")
async def diagnose_one(run_id: int) -> JSONResponse:
    diag = diagnose_run(run_id, apply_fix=True)
    if diag is None:
        raise HTTPException(status_code=404, detail="run not found or not failed")
    return JSONResponse(
        {
            "id": diag.id,
            "run_id": diag.run_id,
            "category": diag.category,
            "root_cause": diag.root_cause,
            "suggested_fix": diag.suggested_fix,
            "auto_applied": bool(diag.auto_applied),
        }
    )
