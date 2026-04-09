"""In-memory pub/sub for pipeline events + SQLite persistence.

Two layers:
1. `LogBus` — fan-out asyncio.Queue per subscriber. Used by SSE.
2. `ObserverImpl` — the concrete observer the pipeline calls into. It
   writes to the DB, updates the current `runs.stage`, and publishes
   events to the LogBus so the admin UI can stream them live.

The pipeline runs in a worker thread (`asyncio.to_thread`), so the
observer must schedule asyncio operations onto the main loop.
"""
from __future__ import annotations

import asyncio
import json
import logging
import threading
from datetime import datetime
from typing import Any

from sqlalchemy import select

from .db import session_scope
from .models_db import LogEntry, Run
from .schemas import StreamEvent

log = logging.getLogger("aiblog.logbus")


# -- LogBus --------------------------------------------------------------


class LogBus:
    """Async fan-out of StreamEvent to every subscriber."""

    def __init__(self) -> None:
        self._subs: list[asyncio.Queue[StreamEvent]] = []
        self._lock = threading.Lock()

    def subscribe(self) -> asyncio.Queue[StreamEvent]:
        q: asyncio.Queue[StreamEvent] = asyncio.Queue(maxsize=1000)
        with self._lock:
            self._subs.append(q)
        return q

    def unsubscribe(self, q: asyncio.Queue[StreamEvent]) -> None:
        with self._lock:
            try:
                self._subs.remove(q)
            except ValueError:
                pass

    def publish(self, event: StreamEvent) -> None:
        """Publish from any thread. Safe to call from pipeline worker."""
        with self._lock:
            subs = list(self._subs)
        for q in subs:
            try:
                q.put_nowait(event)
            except asyncio.QueueFull:
                # drop oldest to stay recent
                try:
                    q.get_nowait()
                    q.put_nowait(event)
                except Exception:
                    pass


# Global singleton — the FastAPI app wires it into observers + SSE routes.
log_bus = LogBus()


# -- ObserverImpl --------------------------------------------------------


class ObserverImpl:
    """Concrete pipeline observer.

    The pipeline calls these methods synchronously from a worker thread.
    We persist to SQLite (sync session) and publish to `log_bus`.
    """

    def __init__(self, run_id: int, bus: LogBus = log_bus):
        self.run_id = run_id
        self.bus = bus
        self.last_slug: str = ""
        self.last_error: str | None = None
        self.revision_count: int = 0

    # -- pipeline callbacks ---------------------------------------------

    def on_run_start(self, topic: str, slug: str) -> None:
        self.last_slug = slug
        self._log("info", f"pipeline start: {topic}", stage=None, meta={"slug": slug})
        self._update_run(stage="research", status="running")
        self._publish(StreamEvent(kind="run_start", run_id=self.run_id, meta={"topic": topic, "slug": slug}))

    def on_stage_start(self, stage: str) -> None:
        self._log("info", f"stage start: {stage}", stage=stage)
        self._update_run(stage=stage)
        self._publish(StreamEvent(kind="stage_start", run_id=self.run_id, stage=stage))

    def on_stage_end(self, stage: str, ok: bool, meta: dict | None = None) -> None:
        self._log(
            "info" if ok else "warn",
            f"stage end: {stage} ({'ok' if ok else 'fail'})",
            stage=stage,
            meta=meta,
        )
        self._publish(
            StreamEvent(
                kind="stage_end",
                run_id=self.run_id,
                stage=stage,
                meta={"ok": ok, **(meta or {})},
            )
        )

    def on_revision(self, round_num: int, verdict: str, report=None) -> None:
        self.revision_count = round_num
        # Extract structured report data (if available) so diagnostics can
        # later read it from the logs table.
        report_meta: dict = {}
        if report is not None:
            try:
                report_meta = {
                    "claims_checked": report.claims_checked,
                    "claims_verified": report.claims_verified,
                    "claims_unverified": report.claims_unverified,
                    "dead_links": list(report.dead_links or []),
                    "issues": list(report.issues or [])[:20],
                    "revision_instructions": (report.revision_instructions or "")[:2000],
                }
            except Exception:
                report_meta = {}
        issues_str = "; ".join(report_meta.get("issues") or [])[:500]
        msg = f"fact-check revision round {round_num}: {verdict}"
        if issues_str:
            msg += f" — issues: {issues_str}"
        self._log(
            "warn",
            msg,
            stage="fact_check",
            meta={"round": round_num, "verdict": verdict, **report_meta},
        )
        with session_scope() as s:
            r = s.get(Run, self.run_id)
            if r is not None:
                r.revision_count = round_num
        self._publish(
            StreamEvent(
                kind="revision",
                run_id=self.run_id,
                stage="fact_check",
                meta={"round": round_num, "verdict": verdict},
            )
        )

    def on_log(self, level: str, message: str, stage: str | None = None) -> None:
        self._log(level, message, stage=stage)
        self._publish(
            StreamEvent(
                kind="log", run_id=self.run_id, stage=stage, level=level, message=message
            )
        )

    def on_run_end(self, success: bool, slug: str, error: str | None = None) -> None:
        if error:
            self.last_error = error
        self._log(
            "info" if success else "error",
            f"pipeline end: success={success}" + (f" error={error}" if error else ""),
            stage=None,
        )
        self._publish(
            StreamEvent(
                kind="run_end",
                run_id=self.run_id,
                meta={"success": success, "slug": slug, "error": error},
            )
        )

    # -- internals -------------------------------------------------------

    def _log(
        self, level: str, message: str, stage: str | None, meta: dict | None = None
    ) -> None:
        try:
            with session_scope() as s:
                s.add(
                    LogEntry(
                        run_id=self.run_id,
                        level=level,
                        stage=stage,
                        agent=None,
                        message=message[:4000],
                        meta=json.dumps(meta, default=str) if meta else None,
                    )
                )
        except Exception as e:
            log.exception("failed to persist log entry: %s", e)

    def _update_run(self, stage: str | None = None, status: str | None = None) -> None:
        try:
            with session_scope() as s:
                r = s.get(Run, self.run_id)
                if r is None:
                    return
                if stage is not None:
                    r.stage = stage
                if status is not None:
                    r.status = status
        except Exception as e:
            log.exception("failed to update run: %s", e)

    def _publish(self, event: StreamEvent) -> None:
        self.bus.publish(event)


# -- Utility helpers for routes -----------------------------------------


def logs_for_run(run_id: int, limit: int = 500) -> list[dict[str, Any]]:
    with session_scope() as s:
        rows = (
            s.execute(
                select(LogEntry)
                .where(LogEntry.run_id == run_id)
                .order_by(LogEntry.ts.asc())
                .limit(limit)
            )
            .scalars()
            .all()
        )
        return [
            {
                "ts": r.ts.isoformat() if r.ts else None,
                "level": r.level,
                "stage": r.stage,
                "agent": r.agent,
                "message": r.message,
                "meta": r.meta,
            }
            for r in rows
        ]
