"""Tests for the daily broadcast slot scheduler in video_worker.

Pure-function coverage for `compute_broadcast_slots`,
`find_active_slot`, and `should_run_broadcast`. The decision is the
single chokepoint that prevents the worker from double-firing or
missing a slot, so it earns its own focused test file.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from scripts.app.video_worker import (
    BroadcastDecision,
    compute_broadcast_slots,
    find_active_slot,
    should_run_broadcast,
)


def _utc(year, month, day, hour, minute=0):
    return datetime(year, month, day, hour, minute, tzinfo=timezone.utc)


# ----------------------------------------------------------------------
# compute_broadcast_slots
# ----------------------------------------------------------------------


def test_compute_slots_n1_uses_anchor():
    assert compute_broadcast_slots(1, 18) == [18]
    assert compute_broadcast_slots(1, 0) == [0]
    assert compute_broadcast_slots(1, 23) == [23]


def test_compute_slots_evenly_distributed_for_higher_n():
    assert compute_broadcast_slots(2, 0) == [6, 18]
    assert compute_broadcast_slots(3, 0) == [4, 12, 20]
    assert compute_broadcast_slots(4, 0) == [3, 9, 15, 21]
    # N=6 happens to include 18 — coincidentally aligning with US 6pm news.
    assert compute_broadcast_slots(6, 0) == [2, 6, 10, 14, 18, 22]


def test_compute_slots_anchor_ignored_when_n_gt_1():
    # Anchor argument is intentionally ignored for N>1; the grid is
    # always anchored to local midnight for predictability.
    assert compute_broadcast_slots(4, 18) == compute_broadcast_slots(4, 0)
    assert compute_broadcast_slots(6, 7) == compute_broadcast_slots(6, 0)


def test_compute_slots_clamps_extreme_inputs():
    assert compute_broadcast_slots(0, 18) == [18]   # zero falls back to 1
    assert compute_broadcast_slots(-3, 18) == [18]
    # Massive caps clamp to 24 max — ensures no slot collision.
    huge = compute_broadcast_slots(50, 0)
    assert len(huge) <= 24
    assert all(0 <= h <= 23 for h in huge)


# ----------------------------------------------------------------------
# find_active_slot
# ----------------------------------------------------------------------


def test_find_active_slot_returns_most_recent_passed_slot():
    slots = [4, 12, 20]
    # 13:30 → most recent passed is 12:00.
    now = datetime(2026, 4, 10, 13, 30, tzinfo=timezone.utc)
    assert find_active_slot(now, slots) == 12

    now = datetime(2026, 4, 10, 19, 59, tzinfo=timezone.utc)
    assert find_active_slot(now, slots) == 12

    now = datetime(2026, 4, 10, 20, 0, tzinfo=timezone.utc)
    assert find_active_slot(now, slots) == 20


def test_find_active_slot_returns_none_before_first_slot():
    slots = [4, 12, 20]
    now = datetime(2026, 4, 10, 3, 0, tzinfo=timezone.utc)
    assert find_active_slot(now, slots) is None


def test_find_active_slot_handles_empty_list():
    assert find_active_slot(datetime(2026, 4, 10), []) is None


# ----------------------------------------------------------------------
# should_run_broadcast — single-slot mode (cap=1)
# ----------------------------------------------------------------------


def test_single_slot_before_anchor_does_not_fire():
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 21, 0),  # 17:00 ET
        cap_per_day=1,
        anchor_hour=18,
        broadcast_tz_name="America/New_York",
        last_upload_at_utc=None,
    )
    assert decision.run is False
    assert decision.reason == "before_first_slot"


def test_single_slot_after_anchor_fires():
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 22, 30),  # 18:30 ET
        cap_per_day=1,
        anchor_hour=18,
        broadcast_tz_name="America/New_York",
        last_upload_at_utc=None,
    )
    assert decision.run is True
    assert decision.reason == "slot_open"
    assert decision.active_slot_hour == 18


def test_single_slot_filled_does_not_fire():
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 23, 0),  # 19:00 ET
        cap_per_day=1,
        anchor_hour=18,
        broadcast_tz_name="America/New_York",
        last_upload_at_utc=_utc(2026, 4, 10, 22, 15),  # 18:15 ET, in window
    )
    assert decision.run is False
    assert decision.reason == "slot_already_filled"


# ----------------------------------------------------------------------
# should_run_broadcast — multi-slot mode (cap=3)
# ----------------------------------------------------------------------


def test_multi_slot_before_first_does_not_fire():
    # cap=3 → slots [4, 12, 20] ET. At 03:00 ET nothing has fired yet.
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 7, 0),  # 03:00 ET
        cap_per_day=3,
        anchor_hour=18,
        broadcast_tz_name="America/New_York",
        last_upload_at_utc=None,
    )
    assert decision.run is False
    assert decision.reason == "before_first_slot"


def test_multi_slot_open_when_slot_unfilled():
    # 13:30 ET, slots [4, 12, 20]. Active slot is 12:00. No upload yet.
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 17, 30),
        cap_per_day=3,
        anchor_hour=18,
        broadcast_tz_name="America/New_York",
        last_upload_at_utc=None,
    )
    assert decision.run is True
    assert decision.active_slot_hour == 12


def test_multi_slot_filled_in_current_window_skips():
    # 13:30 ET, slots [4, 12, 20]. Window for slot 12 = [12, 20).
    # An upload at 12:30 ET → already filled.
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 17, 30),
        cap_per_day=3,
        anchor_hour=18,
        broadcast_tz_name="America/New_York",
        last_upload_at_utc=_utc(2026, 4, 10, 16, 30),  # 12:30 ET
    )
    assert decision.run is False
    assert decision.reason == "slot_already_filled"
    assert decision.active_slot_hour == 12
    # Next slot is 20:00 ET today.
    assert decision.next_run_at is not None
    assert decision.next_run_at.hour == 20


def test_multi_slot_previous_window_upload_does_not_block_current():
    # 13:30 ET, active slot is 12. An upload at 05:00 ET (previous slot)
    # is OUTSIDE the current window [12, 20), so we should fire.
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 17, 30),
        cap_per_day=3,
        anchor_hour=18,
        broadcast_tz_name="America/New_York",
        last_upload_at_utc=_utc(2026, 4, 10, 9, 0),  # 05:00 ET
    )
    assert decision.run is True


def test_multi_slot_last_window_advances_to_tomorrow_first_slot():
    # 21:00 ET, slots [4, 12, 20]. Active slot 20 already filled.
    # Next opportunity is tomorrow's 04:00 ET slot.
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 11, 1, 0),  # 21:00 ET on 4/10
        cap_per_day=3,
        anchor_hour=18,
        broadcast_tz_name="America/New_York",
        last_upload_at_utc=_utc(2026, 4, 11, 0, 30),  # 20:30 ET on 4/10
    )
    assert decision.run is False
    assert decision.next_run_at is not None
    assert decision.next_run_at.hour == 4
    assert decision.next_run_at.date().day == 11


# ----------------------------------------------------------------------
# Robustness
# ----------------------------------------------------------------------


def test_unknown_timezone_falls_back_to_utc():
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 19, 0),
        cap_per_day=1,
        anchor_hour=18,
        broadcast_tz_name="Mars/Phobos",
        last_upload_at_utc=None,
    )
    assert decision.run is True
    assert decision.local_now.tzinfo is not None


def test_naive_datetime_is_treated_as_utc():
    naive = datetime(2026, 4, 10, 22, 30)  # 18:30 ET
    decision = should_run_broadcast(
        now_utc=naive,
        cap_per_day=1,
        anchor_hour=18,
        broadcast_tz_name="America/New_York",
        last_upload_at_utc=None,
    )
    assert decision.run is True


@pytest.mark.parametrize("hour", [-5, 25, 99])
def test_invalid_anchor_hour_is_clamped(hour):
    decision = should_run_broadcast(
        now_utc=_utc(2026, 4, 10, 23, 0),
        cap_per_day=1,
        anchor_hour=hour,
        broadcast_tz_name="America/New_York",
        last_upload_at_utc=None,
    )
    assert isinstance(decision, BroadcastDecision)
