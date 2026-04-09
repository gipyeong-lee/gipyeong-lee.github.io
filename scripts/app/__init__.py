"""Always-on AI news blog daemon + local admin dashboard.

Phase A: core scheduler loop (daemon.py, sources/, scoring, queue, pipeline_runner, publisher).
Phase B: FastAPI admin UI (main.py, routes/, templates/, logging_bus).
Phase C: arXiv + corporate blog sources, settings UI, topics management.
Phase D: launchd install, git push hardening, retention, timeouts.

Entry points:
  python -m uvicorn scripts.app.main:app --host 127.0.0.1 --port 7001
  python -m scripts.app.daemon          # headless fallback (no HTTP)
  python -m scripts.app.history_import  # one-shot CSV migration
"""
