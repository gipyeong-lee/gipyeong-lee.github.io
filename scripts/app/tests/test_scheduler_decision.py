"""Trigger decision logic (_decide_trigger) — hybrid min/max/event window."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest


class _FakeSettings:
    def __init__(self, min_s, max_s, thr):
        self.min_interval_seconds = min_s
        self.max_interval_seconds = max_s
        self.event_trigger_threshold = thr
        self.keyword_blocklist = []


class _FakeTopic:
    def __init__(self, score, boost=0.0):
        self.score = score
        self.priority_boost = boost


@pytest.fixture
def daemon_module(monkeypatch):
    """Import daemon.py with peek_top_score and get_settings patchable."""
    from scripts.app import daemon as d

    # Reset state between tests
    d._state["last_run_at"] = None
    d._state["current_run_id"] = None
    yield d
    d._state["last_run_at"] = None


def test_below_min_interval_returns_none(daemon_module, monkeypatch):
    d = daemon_module
    d._state["last_run_at"] = datetime.now(timezone.utc) - timedelta(seconds=60)
    monkeypatch.setattr(d, "get_settings", lambda: _FakeSettings(3600, 7200, 0.85))
    assert d._decide_trigger() is None


def test_above_max_interval_returns_timer(daemon_module, monkeypatch):
    d = daemon_module
    d._state["last_run_at"] = datetime.now(timezone.utc) - timedelta(seconds=10_000)
    monkeypatch.setattr(d, "get_settings", lambda: _FakeSettings(3600, 7200, 0.85))
    assert d._decide_trigger() == "timer"


def test_window_with_high_score_returns_event(daemon_module, monkeypatch):
    d = daemon_module
    d._state["last_run_at"] = datetime.now(timezone.utc) - timedelta(seconds=5000)
    monkeypatch.setattr(d, "get_settings", lambda: _FakeSettings(3600, 7200, 0.85))
    monkeypatch.setattr(d, "peek_top_score", lambda _bl: _FakeTopic(score=0.90))
    assert d._decide_trigger() == "event"


def test_window_with_low_score_returns_none(daemon_module, monkeypatch):
    d = daemon_module
    d._state["last_run_at"] = datetime.now(timezone.utc) - timedelta(seconds=5000)
    monkeypatch.setattr(d, "get_settings", lambda: _FakeSettings(3600, 7200, 0.85))
    monkeypatch.setattr(d, "peek_top_score", lambda _bl: _FakeTopic(score=0.50))
    assert d._decide_trigger() is None


def test_never_ran_returns_timer(daemon_module, monkeypatch):
    d = daemon_module
    d._state["last_run_at"] = None
    monkeypatch.setattr(d, "_bootstrap_last_run_at", lambda: None)
    monkeypatch.setattr(d, "get_settings", lambda: _FakeSettings(3600, 7200, 0.85))
    assert d._decide_trigger() == "timer"
