"""Scoring + keyword + canonicalization tests."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from scripts.app.schemas import RawTopic
from scripts.app.scoring import (
    canonicalize_url,
    freshness_score,
    score_batch,
    score_topic,
)
from scripts.app.sources.keywords import compute_keyword_hits, is_ai_relevant


def test_canonicalize_drops_utm_and_trailing_slash():
    # Scheme and host are lowercased; path case is preserved (RFC 3986 says
    # paths are case-sensitive — /About and /about are different resources).
    url = "HTTPS://Example.com/Foo/?utm_source=x&ref=nav"
    assert canonicalize_url(url) == "https://example.com/Foo"


def test_canonicalize_none_for_bad_input():
    assert canonicalize_url(None) is None
    assert canonicalize_url("") is None
    assert canonicalize_url("not a url") is None


def test_freshness_decays_with_age():
    now = datetime.now(timezone.utc)
    fresh = freshness_score(now)
    old = freshness_score(now - timedelta(hours=72))
    assert fresh > 0.9
    assert old < fresh
    assert 0.0 <= old <= 1.0


def test_keyword_hits_finds_multiple():
    hits, bonus = compute_keyword_hits("OpenAI released GPT-5 with agentic tool calling")
    assert "openai" in hits
    assert any("gpt" in h for h in hits)
    assert bonus > 0


def test_keyword_word_boundary_does_not_match_substring():
    # "rag" should not match "dragon" — word boundary guard
    hits, _ = compute_keyword_hits("dragon age rpg")
    assert "rag" not in hits


def test_is_ai_relevant_requires_hit():
    assert is_ai_relevant("Anthropic Claude 4 hits benchmark record")
    assert not is_ai_relevant("Local bakery opens new branch downtown")


def test_score_hackernews_uses_points_and_keywords():
    raw = RawTopic(
        source="hackernews",
        source_id="1",
        title="GPT-5 is here",
        url="https://news.ycombinator.com/item?id=1",
        raw_payload={"score": 500, "descendants": 200},
    )
    scored = score_topic(raw)
    assert 0.0 <= scored.score <= 1.0
    assert scored.score > 0.5  # high points + keyword hit


def test_score_arxiv_depends_on_freshness():
    now = datetime.now(timezone.utc)
    raw = RawTopic(
        source="arxiv",
        source_id="2501.01234",
        title="Scaling Laws for Frontier Models",
        url="https://arxiv.org/abs/2501.01234",
        published_at=now,
    )
    scored = score_topic(raw)
    assert scored.score > 0.3


def test_score_corporate_blog_is_high():
    raw = RawTopic(
        source="anthropic_blog",
        source_id="x",
        title="Introducing Claude 4.5 Sonnet",
        url="https://www.anthropic.com/news/claude-4-5-sonnet",
        published_at=datetime.now(timezone.utc),
    )
    scored = score_topic(raw)
    assert scored.score >= 0.75


def test_score_batch_preserves_order():
    raws = [
        RawTopic(source="arxiv", source_id=str(i), title=f"Paper {i}", url=f"http://a/{i}")
        for i in range(5)
    ]
    scored = score_batch(raws)
    assert len(scored) == 5
    assert [s.raw.source_id for s in scored] == [str(i) for i in range(5)]
