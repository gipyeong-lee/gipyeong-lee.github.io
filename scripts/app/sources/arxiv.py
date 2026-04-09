"""arXiv RSS source (cs.AI, cs.CL, cs.LG).

Fetched via httpx + parsed with feedparser. The arXiv RSS is naturally
AI-relevant given the category filter, so we skip the keyword gate and
keep everything from the target categories.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import feedparser
import httpx

from ..schemas import RawTopic
from .base import USER_AGENT, SourceAdapter

CATEGORIES = ("cs.AI", "cs.CL", "cs.LG")
FEED_URL = "http://export.arxiv.org/rss/{cat}"


class ArxivSource(SourceAdapter):
    name = "arxiv"

    def __init__(self, client: httpx.AsyncClient | None = None) -> None:
        self._client = client

    async def poll(self) -> list[RawTopic]:
        own = self._client is None
        client = self._client or httpx.AsyncClient(
            timeout=20.0, headers={"user-agent": USER_AGENT}
        )
        try:
            topics: list[RawTopic] = []
            for cat in CATEGORIES:
                try:
                    r = await client.get(FEED_URL.format(cat=cat))
                    r.raise_for_status()
                    feed = feedparser.parse(r.text)
                    topics.extend(self._entries_to_raw(cat, feed.entries))
                except Exception:
                    # One category failing shouldn't doom the whole poll.
                    continue
            return topics
        finally:
            if own:
                await client.aclose()

    def _entries_to_raw(self, cat: str, entries: list[Any]) -> list[RawTopic]:
        out: list[RawTopic] = []
        for e in entries:
            title = (e.get("title") or "").strip()
            link = e.get("link") or ""
            if not title or not link:
                continue
            summary = e.get("summary") or e.get("description") or ""
            arxiv_id = e.get("id") or link
            published = None
            if getattr(e, "published_parsed", None):
                try:
                    published = datetime(
                        *e.published_parsed[:6], tzinfo=timezone.utc
                    )
                except Exception:
                    published = None
            out.append(
                RawTopic(
                    source=self.name,
                    source_id=arxiv_id,
                    title=title,
                    url=link,
                    summary=summary,
                    published_at=published,
                    raw_payload={"category": cat},
                )
            )
        return out
