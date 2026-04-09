"""FastAPI entrypoint — mounts routers, spawns the scheduler via lifespan.

Bind to 127.0.0.1 only (local-only admin). Launch with:

  python -m uvicorn scripts.app.main:app --host 127.0.0.1 --port 7001
"""
from __future__ import annotations

import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .config import STATIC_DIR, TEMPLATES_DIR, VIDEOS_DIR
from .daemon import reset_stop, scheduler_loop, stop
from .db import init_db
from .deploy_watcher import (
    deploy_watcher_loop,
    reset_stop as deploy_reset_stop,
    stop as deploy_stop,
)
from .video_worker import (
    reset_stop as video_reset_stop,
    stop as video_stop,
    video_worker_loop,
)

logger = logging.getLogger("aiblog.main")

# Global so routes can render templates without re-importing
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    init_db()
    # One-shot history.csv migration (safe/idempotent)
    try:
        from . import history_import

        result = history_import.run()
        logger.info("history_import: %s", result)
    except Exception:
        logger.exception("history_import failed (non-fatal)")

    reset_stop()
    video_reset_stop()
    deploy_reset_stop()
    task = asyncio.create_task(scheduler_loop(), name="scheduler_loop")
    video_task = asyncio.create_task(video_worker_loop(), name="video_worker_loop")
    deploy_task = asyncio.create_task(deploy_watcher_loop(), name="deploy_watcher_loop")
    logger.info("scheduler + video_worker + deploy_watcher tasks started")
    try:
        yield
    finally:
        logger.info("shutting down scheduler, video worker, deploy watcher")
        stop()
        video_stop()
        deploy_stop()
        for t, label in (
            (task, "scheduler"),
            (video_task, "video_worker"),
            (deploy_task, "deploy_watcher"),
        ):
            try:
                await asyncio.wait_for(t, timeout=10)
            except asyncio.TimeoutError:
                logger.warning(f"{label} did not stop within 10s; cancelling")
                t.cancel()


app = FastAPI(
    title="aiblog admin",
    version="0.1.0",
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
)

# Static + routers
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Serve generated video files (mp4/wav/jpg) so the Admin UI can preview them.
# Local-only admin, so no auth needed; the directory is gitignored.
if VIDEOS_DIR.exists():
    app.mount("/videos-data", StaticFiles(directory=str(VIDEOS_DIR)), name="videos_data")

# Import routers here to avoid circular imports
from .routes import dashboard as r_dashboard  # noqa: E402
from .routes import daemon as r_daemon        # noqa: E402
from .routes import deploy as r_deploy        # noqa: E402
from .routes import diagnoses as r_diagnoses  # noqa: E402
from .routes import pipeline as r_pipeline    # noqa: E402
from .routes import posts as r_posts          # noqa: E402
from .routes import settings as r_settings    # noqa: E402
from .routes import topics as r_topics        # noqa: E402
from .routes import videos as r_videos        # noqa: E402

app.include_router(r_dashboard.router)
app.include_router(r_pipeline.router)
app.include_router(r_posts.router)
app.include_router(r_videos.router)
app.include_router(r_topics.router)
app.include_router(r_diagnoses.router)
app.include_router(r_deploy.router)
app.include_router(r_settings.router)
app.include_router(r_daemon.router)
