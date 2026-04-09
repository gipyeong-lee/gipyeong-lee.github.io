"""Daemon control routes (in-process stop/resume + launchctl lifecycle)."""
from __future__ import annotations

import asyncio
import os
import subprocess
from typing import Literal

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from ..config import LAUNCHD_LABEL, LAUNCHD_PLIST_PATH
from ..daemon import (
    current_run_id,
    get_last_run_at,
    is_running,
    pipeline_locked,
    reset_stop,
    scheduler_loop,
    stop,
)

router = APIRouter(prefix="/daemon")


_scheduler_task: asyncio.Task | None = None


@router.get("/status")
async def status() -> JSONResponse:
    last = get_last_run_at()
    launchd_loaded = _launchctl_is_loaded()
    return JSONResponse(
        {
            "running": is_running(),
            "pipeline_locked": pipeline_locked(),
            "current_run_id": current_run_id(),
            "last_run_at": last.isoformat() if last else None,
            "launchd_loaded": launchd_loaded,
            "launchd_plist": str(LAUNCHD_PLIST_PATH),
        }
    )


@router.post("/stop")
async def stop_scheduler() -> JSONResponse:
    """Pause the in-process scheduler (does NOT stop the launchd process)."""
    stop()
    return JSONResponse({"status": "stopping"})


@router.post("/start")
async def start_scheduler() -> JSONResponse:
    """Resume the in-process scheduler if previously paused."""
    global _scheduler_task
    if is_running():
        return JSONResponse({"status": "already_running"})
    reset_stop()
    _scheduler_task = asyncio.create_task(scheduler_loop(), name="scheduler_loop")
    return JSONResponse({"status": "started"})


@router.post("/restart")
async def restart_launchd() -> JSONResponse:
    """Bootout + bootstrap the launchd plist (replaces the whole process)."""
    if not LAUNCHD_PLIST_PATH.exists():
        raise HTTPException(
            status_code=400,
            detail=f"launchd plist missing at {LAUNCHD_PLIST_PATH}. Run launchd/install.sh first.",
        )
    uid = os.getuid()
    target = f"gui/{uid}/{LAUNCHD_LABEL}"
    try:
        subprocess.run(["launchctl", "bootout", target], check=False)
        subprocess.run(
            ["launchctl", "bootstrap", f"gui/{uid}", str(LAUNCHD_PLIST_PATH)],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"launchctl failed: {e}")
    return JSONResponse({"status": "restarted"})


def _launchctl_is_loaded() -> bool:
    try:
        out = subprocess.run(
            ["launchctl", "list", LAUNCHD_LABEL],
            capture_output=True,
            text=True,
        )
        return out.returncode == 0
    except Exception:
        return False
