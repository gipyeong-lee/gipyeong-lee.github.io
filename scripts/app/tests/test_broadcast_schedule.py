"""Tests for the daily broadcast slot decision in video_worker.

Pure-function coverage for `should_run_broadcast`. The decision is the
single chokepoint that prevents the worker from double-firing or
missing the daily slot, so it earns its own focused test file.
"""
from __future__ import annotations

from datetime import date, datetime, timezone

import pytest

from scripts.app.video_worker import (
    BroadcastDecision,
    should_run_broadcast,
)


# ----------------------------------------------------------------------
# Decision logic
# ----------------------------------------------------------------------


def _utc(year, month, day, hour, minute=0):
    return datetime(year, month, day, hour, minute, tzinfo=timezone.utc)


def test_before_local_slot_does_not_fire():
    # 2026-04-10 17:00 ET = 21:00 UTC. Slot is 18:00 ET.
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 21, 0),
        broadcast_hour=18,
        broadcast_tz_name="America/New_York",
        last_broadcast_date=None,
    )
    assert isinstance(decision, BroadcastDecision)
    assert decision.run is False
    assert decision.reason == "before_slot"
    assert decision.next_run_at is not None
    assert decision.next_run_at.hour == 18


def test_after_local_slot_fires_when_no_prior_broadcast():
    # 2026-04-10 18:30 ET = 22:30 UTC. Slot is 18:00 ET.
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 22, 30),
        broadcast_hour=18,
        broadcast_tz_name="America/New_York",
        last_broadcast_date=None,
    )
    assert decision.run is True
    assert decision.reason == "slot_open"


def test_after_local_slot_skips_if_already_broadcast_today():
    # Same day in ET — last_broadcast_date matches today.
    today_local = date(2026, 4, 10)
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 23, 0),  # 19:00 ET
        broadcast_hour=18,
        broadcast_tz_name="America/New_York",
        last_broadcast_date=today_local,
    )
    assert decision.run is False
    assert decision.reason == "already_broadcast_today"
    assert decision.next_run_at is not None
    assert decision.next_run_at.date() == date(2026, 4, 11)


def test_yesterday_broadcast_does_not_block_today():
    # Last broadcast was yesterday, slot is open today.
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 23, 0),  # 19:00 ET on 4/10
        broadcast_hour=18,
        broadcast_tz_name="America/New_York",
        last_broadcast_date=date(2026, 4, 9),
    )
    assert decision.run is True


def test_unknown_timezone_falls_back_to_utc():
    # The helper logs a warning and uses UTC. Slot 18:00 UTC.
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 19, 0),
        broadcast_hour=18,
        broadcast_tz_name="Mars/Phobos",
        last_broadcast_date=None,
    )
    assert decision.run is True
    assert decision.local_now.tzinfo is not None


def test_naive_datetime_is_treated_as_utc():
    naive = datetime(2026, 4, 10, 22, 30)  # 18:30 ET
    decision = should_run_broadcast(
        now_utc=naive,
        broadcast_hour=18,
        broadcast_tz_name="America/New_York",
        last_broadcast_date=None,
    )
    assert decision.run is True


def test_broadcast_date_boundary_crosses_midnight():
    # 2026-04-11 02:00 UTC = 22:00 ET on 4/10. The local date is still
    # 4/10, so a 4/10 last_broadcast_date should still block.
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 11, 2, 0),
        broadcast_hour=18,
        broadcast_tz_name="America/New_York",
        last_broadcast_date=date(2026, 4, 10),
    )
    assert decision.run is False
    assert decision.reason == "already_broadcast_today"


def test_broadcast_date_boundary_after_local_midnight():
    # 2026-04-11 05:00 UTC = 01:00 ET on 4/11. Last broadcast on 4/10
    # should NOT block — it's a new local day.
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 11, 5, 0),
        broadcast_hour=18,
        broadcast_tz_name="America/New_York",
        last_broadcast_date=date(2026, 4, 10),
    )
    assert decision.run is False  # Before today's slot
    assert decision.reason == "before_slot"


@pytest.mark.parametrize("hour", [-5, 25, 99])
def test_invalid_broadcast_hour_is_clamped(hour):
    # Out-of-range hours get clamped into [0, 23] without crashing.
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 23, 0),
        broadcast_hour=hour,
        broadcast_tz_name="America/New_York",
        last_broadcast_date=None,
    )
    assert isinstance(decision, BroadcastDecision)
