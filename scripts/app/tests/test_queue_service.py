"""queue_service: enqueue/dedup/pick_next/transitions."""
from __future__ import annotations

from datetime import datetime, timezone

import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker


@pytest.fixture
def temp_db(tmp_path, monkeypatch):
    """Create an isolated SQLite DB for this test and swap the global engine."""
    db_path = tmp_path / "aiblog_test.db"
    test_url = f"sqlite:///{db_path}"
    test_engine = create_engine(
        test_url, connect_args={"check_same_thread": False}, future=True
    )

    @event.listens_for(test_engine, "connect")
    def _pragmas(dbapi_conn, _rec):
        cur = dbapi_conn.cursor()
        cur.execute("PRAGMA journal_mode=WAL")
        cur.execute("PRAGMA foreign_keys=ON")
        cur.close()

    TestSession = sessionmaker(
        bind=test_engine, autoflush=False, autocommit=False, future=True
    )

    from scripts.app import db as app_db
    from scripts.app import models_db
    from scripts.app import settings_store
    from scripts.app import queue_service

    # Swap engine + session on the db module used everywhere.
    monkeypatch.setattr(app_db, "engine", test_engine, raising=False)
    monkeypatch.setattr(app_db, "SessionLocal", TestSession, raising=False)

    # Recreate schema on the fresh engine
    models_db.Base.metadata.create_all(bind=test_engine)
    settings_store.seed_defaults_if_empty()

    yield queue_service

    test_engine.dispose()


def _make_scored(raw_kwargs):
    from scripts.app.schemas import RawTopic
    from scripts.app.scoring import score_topic

    return score_topic(RawTopic(**raw_kwargs))


def test_enqueue_dedup_by_source_pair(temp_db):
    qs = temp_db
    a = _make_scored(
        dict(
            source="hackernews",
            source_id="123",
            title="GPT news",
            url="https://news.ycombinator.com/item?id=123",
            raw_payload={"score": 100},
        )
    )
    assert qs.enqueue_new([a]) == 1
    assert qs.enqueue_new([a]) == 0  # same (source, source_id) → skipped


def test_enqueue_dedup_by_canonical_url(temp_db):
    qs = temp_db
    a = _make_scored(
        dict(
            source="hackernews",
            source_id="1",
            title="GPT news",
            url="https://example.com/ai?utm_source=hn",
            raw_payload={"score": 100},
        )
    )
    b = _make_scored(
        dict(
            source="arxiv",
            source_id="2",
            title="GPT paper",
            url="https://example.com/ai/?utm_source=rss",
        )
    )
    # Both canonicalize to the same URL → only the first is inserted.
    assert qs.enqueue_new([a, b]) == 1


def test_pick_next_returns_highest_scored(temp_db):
    qs = temp_db
    low = _make_scored(
        dict(
            source="hackernews",
            source_id="low",
            title="LLM news",
            url="https://ex.com/low",
            raw_payload={"score": 10},
        )
    )
    high = _make_scored(
        dict(
            source="anthropic_blog",
            source_id="high",
            title="Claude release",
            url="https://ex.com/high",
            published_at=datetime.now(timezone.utc),
        )
    )
    qs.enqueue_new([low, high])

    picked = qs.pick_next(cooldown_seconds=3600, max_fail_count=3)
    assert picked is not None
    assert picked.source == "anthropic_blog"

    picked2 = qs.pick_next(cooldown_seconds=3600, max_fail_count=3)
    assert picked2 is not None
    assert picked2.source == "hackernews"

    assert qs.pick_next(cooldown_seconds=3600, max_fail_count=3) is None


def test_pick_next_skips_blocklist(temp_db):
    qs = temp_db
    bad = _make_scored(
        dict(
            source="hackernews",
            source_id="bad",
            title="NFT crypto pump launches",
            url="https://ex.com/bad",
            raw_payload={"score": 500},
        )
    )
    good = _make_scored(
        dict(
            source="hackernews",
            source_id="good",
            title="LLM inference speedup",
            url="https://ex.com/good",
            raw_payload={"score": 100},
        )
    )
    qs.enqueue_new([bad, good])
    picked = qs.pick_next(
        cooldown_seconds=3600, max_fail_count=3, blocklist=["NFT"]
    )
    assert picked is not None
    assert "LLM" in picked.title


def test_mark_failed_engages_cooldown(temp_db):
    qs = temp_db
    t = _make_scored(
        dict(
            source="hackernews",
            source_id="fail",
            title="GPT fail topic",
            url="https://ex.com/fail",
            raw_payload={"score": 200},
        )
    )
    qs.enqueue_new([t])
    picked = qs.pick_next(cooldown_seconds=3600, max_fail_count=3)
    assert picked is not None
    # Reset to queued with fail_count=1 — selected_at stays set so cooldown applies
    qs.mark_status(picked.id, "queued", fail_count_delta=1)
    # Within cooldown window → no topic returned
    picked2 = qs.pick_next(cooldown_seconds=3600, max_fail_count=3)
    assert picked2 is None


def test_manual_topic_is_high_priority(temp_db):
    qs = temp_db
    low = _make_scored(
        dict(
            source="hackernews",
            source_id="low2",
            title="LLM news again",
            url="https://ex.com/low2",
            raw_payload={"score": 10},
        )
    )
    qs.enqueue_new([low])
    qs.add_manual("Urgent: New GPT-5 details", url="https://ex.com/manual")
    picked = qs.pick_next(cooldown_seconds=3600, max_fail_count=3)
    assert picked is not None
    assert picked.source == "manual"
