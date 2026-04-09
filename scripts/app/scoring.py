"""Topic scoring.

Each source contributes a score in [0, 1]:
- HackerNews: normalized points + comments + AI keyword bonus.
- arXiv: freshness + AI keyword bonus (most cs.* entries are AI-relevant).
- Corporate blogs: fixed 0.75 base + freshness boost (1st-party = high signal).

The scorer also computes `canonical_url` used by queue_service for dedup.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from ..url_validator import canonicalize_url  # re-export for backward compat
from .schemas import RawTopic, ScoredTopic
from .sources.keywords import compute_keyword_hits

__all__ = ["canonicalize_url", "freshness_score", "score_topic", "score_batch"]


# -- Freshness helper ----------------------------------------------------


def freshness_score(published_at: datetime | None, half_life_hours: float = 36.0) -> float:
    if published_at is None:
        return 0.5  # unknown age → neutral
    if published_at.tzinfo is None:
        published_at = published_at.replace(tzinfo=timezone.utc)
    age_hours = (
        datetime.now(timezone.utc) - published_at
    ).total_seconds() / 3600.0
    if age_hours < 0:
        age_hours = 0.0
    # exponential decay: 1.0 at t=0, 0.5 at one half-life, etc.
    import math
    return math.pow(0.5, age_hours / half_life_hours)


def _normalize_count(n: int | float | None, cap: float) -> float:
    if not n:
        return 0.0
    return min(1.0, float(n) / cap)


# -- Main scorer ---------------------------------------------------------


def score_topic(raw: RawTopic) -> ScoredTopic:
    text = f"{raw.title} {raw.summary or ''}"
    hits, kw_bonus = compute_keyword_hits(text)

    if raw.source == "hackernews":
        pts = raw.raw_payload.get("score") or 0
        comments = raw.raw_payload.get("descendants") or 0
        score = (
            0.40 * _normalize_count(pts, 400.0)
            + 0.30 * _normalize_count(comments, 200.0)
            + 0.30 * kw_bonus
        )
    elif raw.source == "arxiv":
        score = 0.60 * freshness_score(raw.published_at) + 0.40 * kw_bonus
    elif raw.source.endswith("_blog"):
        # 1st-party corporate sources: base 0.75 + freshness bump
        score = min(1.0, 0.75 + 0.25 * freshness_score(raw.published_at))
    else:
        score = 0.5 * kw_bonus + 0.5 * freshness_score(raw.published_at)

    return ScoredTopic(
        raw=raw,
        canonical_url=canonicalize_url(raw.url),
        score=round(max(0.0, min(1.0, score)), 4),
        keyword_hits=hits,
    )


def score_batch(raws: list[RawTopic]) -> list[ScoredTopic]:
    return [score_topic(r) for r in raws]
