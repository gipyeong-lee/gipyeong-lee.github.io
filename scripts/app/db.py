"""SQLAlchemy engine + session factory.

Sync engine is intentional: the admin is single-user and sync sessions
compose cleanly with both FastAPI's threadpool dependencies and the
scheduler's `asyncio.to_thread` pipeline execution.
"""
from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from .config import DB_URL


def _make_engine() -> Engine:
    eng = create_engine(
        DB_URL,
        connect_args={"check_same_thread": False},
        future=True,
    )

    @event.listens_for(eng, "connect")
    def _set_sqlite_pragmas(dbapi_connection, _conn_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.execute("PRAGMA synchronous=NORMAL")
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    return eng


engine: Engine = _make_engine()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def init_db() -> None:
    """Create all tables + seed default settings. Idempotent."""
    from . import models_db  # noqa: F401 — register models on Base
    from .models_db import Base
    from .settings_store import seed_defaults_if_empty

    Base.metadata.create_all(bind=engine)
    seed_defaults_if_empty()


@contextmanager
def session_scope() -> Iterator[Session]:
    """Context-managed session with automatic commit/rollback."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def get_session() -> Iterator[Session]:
    """FastAPI dependency: yields a session and closes it on teardown."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
