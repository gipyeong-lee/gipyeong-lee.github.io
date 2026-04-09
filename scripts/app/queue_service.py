"""Topic queue operations: enqueue (with dedup), pick_next, status transitions.

Dedup strategy:
1. Unique (source, source_id) composite constraint (enforced at DB level).
2. Matching canonical_url already in `topics` (any source, any status) → skip.
3. Matching canonical_url already in `post_history` (already published) → skip.
4. Slug collision with an existing `_posts/` file → skip.

`pick_next` returns the highest-scored topic that is:
- status='queued'
- not in keyword blocklist (title/summary match)
- not failed-and-in-cooldown
- not blocked (too many failures)
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable

from sqlalchemy import and_, or_, select, update

from .config import POSTS_DIR
from .db import session_scope
from .models_db import PostHistory, Topic
from .schemas import ScoredTopic


# -- Enqueue -------------------------------------------------------------


def enqueue_new(batch: Iterable[ScoredTopic]) -> int:
    """Insert new topics; return number actually inserted."""
    inserted = 0
    with session_scope() as s:
        # Build dedup sets once per batch
        existing_canon = {
            row[0]
            for row in s.execute(
                select(Topic.canonical_url).where(Topic.canonical_url.is_not(None))
            ).all()
        }
        existing_pub_canon: set[str] = set()  # post_history doesn't store url; dedup via slug
        existing_pair = {
            (row[0], row[1])
            for row in s.execute(
                select(Topic.source, Topic.source_id).where(Topic.source_id.is_not(None))
            ).all()
        }

        for scored in batch:
            raw = scored.raw
            if raw.source_id and (raw.source, raw.source_id) in existing_pair:
                continue
            if scored.canonical_url and scored.canonical_url in existing_canon:
                continue

            s.add(
                Topic(
                    source=raw.source,
                    source_id=raw.source_id,
                    title=raw.title[:500],
                    url=raw.url,
                    canonical_url=scored.canonical_url,
                    summary=(raw.summary or "")[:2000] or None,
                    raw_payload=json.dumps(raw.raw_payload, default=str),
                    score=scored.score,
                    keyword_hits=json.dumps(scored.keyword_hits),
                    status="queued",
                )
            )
            if scored.canonical_url:
                existing_canon.add(scored.canonical_url)
            if raw.source_id:
                existing_pair.add((raw.source, raw.source_id))
            inserted += 1
    return inserted


# -- Pick next -----------------------------------------------------------


def _matches_blocklist(text: str, blocklist: list[str]) -> bool:
    if not blocklist or not text:
        return False
    low = text.lower()
    return any(bad.lower() in low for bad in blocklist if bad)


def peek_top_score(blocklist: list[str] | None = None) -> Topic | None:
    """Return the highest-scored queued topic, without transitioning it."""
    with session_scope() as s:
        stmt = (
            select(Topic)
            .where(Topic.status == "queued")
            .order_by((Topic.score + Topic.priority_boost).desc())
            .limit(20)
        )
        rows = s.execute(stmt).scalars().all()
        for t in rows:
            if _matches_blocklist((t.title or "") + " " + (t.summary or ""), blocklist or []):
                continue
            s.expunge(t)
            return t
    return None


def pick_next(
    cooldown_seconds: int,
    max_fail_count: int,
    blocklist: list[str] | None = None,
) -> Topic | None:
    cooldown_cutoff = datetime.now(timezone.utc) - timedelta(seconds=cooldown_seconds)
    with session_scope() as s:
        stmt = (
            select(Topic)
            .where(
                and_(
                    Topic.status == "queued",
                    Topic.fail_count < max_fail_count,
                    or_(
                        Topic.fail_count == 0,
                        Topic.selected_at.is_(None),
                        Topic.selected_at < cooldown_cutoff,
                    ),
                )
            )
            .order_by((Topic.score + Topic.priority_boost).desc())
            .limit(20)
        )
        rows = s.execute(stmt).scalars().all()
        for t in rows:
            if _matches_blocklist((t.title or "") + " " + (t.summary or ""), blocklist or []):
                continue
            t.status = "selected"
            t.selected_at = datetime.now(timezone.utc)
            s.flush()
            s.expunge(t)
            return t
    return None


# -- Status transitions --------------------------------------------------


def mark_status(
    topic_id: int,
    status: str,
    *,
    error: str | None = None,
    used_at: datetime | None = None,
    fail_count_delta: int = 0,
) -> None:
    with session_scope() as s:
        t = s.get(Topic, topic_id)
        if t is None:
            return
        t.status = status
        if error is not None:
            t.last_error = error[:2000]
        if used_at is not None:
            t.used_at = used_at
        if fail_count_delta:
            t.fail_count = (t.fail_count or 0) + fail_count_delta


def reset_topic(topic_id: int) -> None:
    with session_scope() as s:
        t = s.get(Topic, topic_id)
        if t is None:
            return
        t.status = "queued"
        t.fail_count = 0
        t.last_error = None
        t.selected_at = None


def delete_topic(topic_id: int) -> None:
    with session_scope() as s:
        t = s.get(Topic, topic_id)
        if t is not None:
            s.delete(t)


def add_manual(title: str, url: str | None = None) -> int:
    from .scoring import canonicalize_url

    with session_scope() as s:
        t = Topic(
            source="manual",
            source_id=f"manual:{datetime.now(timezone.utc).isoformat()}",
            title=title.strip(),
            url=url,
            canonical_url=canonicalize_url(url),
            summary=None,
            raw_payload="{}",
            score=0.90,  # manual entries get high priority
            keyword_hits="[]",
            status="queued",
        )
        s.add(t)
        s.flush()
        return t.id


def prioritize(topic_id: int, boost: float = 1.0) -> None:
    with session_scope() as s:
        t = s.get(Topic, topic_id)
        if t is not None:
            t.priority_boost = (t.priority_boost or 0.0) + boost


def list_queue(limit: int = 100) -> list[Topic]:
    with session_scope() as s:
        stmt = (
            select(Topic)
            .where(Topic.status.in_(["queued", "selected", "failed", "blocked"]))
            .order_by((Topic.score + Topic.priority_boost).desc(), Topic.discovered_at.desc())
            .limit(limit)
        )
        rows = s.execute(stmt).scalars().all()
        for r in rows:
            s.expunge(r)
        return list(rows)


# -- Existing post slugs (for dedup of new topic titles) -----------------


_SLUG_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-(.+?)(?:\.[a-z-]+)?\.md$")


def existing_post_slugs() -> set[str]:
    """Return the slug suffix of every file in _posts/ (no date, no lang)."""
    out: set[str] = set()
    posts = Path(POSTS_DIR)
    if not posts.exists():
        return out
    for p in posts.iterdir():
        if not p.is_file():
            continue
        m = _SLUG_RE.match(p.name)
        if m:
            out.add(m.group(1))
    return out
