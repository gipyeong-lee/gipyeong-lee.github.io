"""HackerNews Firebase API source.

Fetches top stories, filters by AI keywords, returns as RawTopic[].
"""
from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from typing import Any

import httpx

from ..schemas import RawTopic
from .base import USER_AGENT, SourceAdapter
from .keywords import is_ai_relevant

TOP_ENDPOINT = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_ENDPOINT = "https://hacker-news.firebaseio.com/v0/item/{id}.json"
TOP_N = 100
CONCURRENT_FETCHES = 10


class HackerNewsSource(SourceAdapter):
    name = "hackernews"

    def __init__(self, client: httpx.AsyncClient | None = None) -> None:
        self._client = client

    async def poll(self) -> list[RawTopic]:
        own = self._client is None
        client = self._client or httpx.AsyncClient(
            timeout=15.0,
            headers={"user-agent": USER_AGENT},
            http2=True,
        )
        try:
            resp = await client.get(TOP_ENDPOINT)
            resp.raise_for_status()
            ids = resp.json()[:TOP_N]
            items = await self._fetch_items(client, ids)
            return self._to_raw_topics(items)
        finally:
            if own:
                await client.aclose()

    async def _fetch_items(
        self, client: httpx.AsyncClient, ids: list[int]
    ) -> list[dict[str, Any]]:
        sem = asyncio.Semaphore(CONCURRENT_FETCHES)

        async def _fetch(iid: int) -> dict[str, Any] | None:
            async with sem:
                try:
                    r = await client.get(ITEM_ENDPOINT.format(id=iid))
                    r.raise_for_status()
                    return r.json()
                except Exception:
                    return None

        results = await asyncio.gather(*(_fetch(i) for i in ids))
        return [r for r in results if r]

    def _to_raw_topics(self, items: list[dict[str, Any]]) -> list[RawTopic]:
        topics: list[RawTopic] = []
        for it in items:
            if it.get("type") not in ("story", "ask"):
                continue
            if it.get("dead") or it.get("deleted"):
                continue
            title = (it.get("title") or "").strip()
            if not title:
                continue
            text = title + " " + (it.get("text") or "")
            if not is_ai_relevant(text):
                continue
            url = it.get("url") or f"https://news.ycombinator.com/item?id={it.get('id')}"
            ts = it.get("time")
            published = (
                datetime.fromtimestamp(ts, tz=timezone.utc) if isinstance(ts, int) else None
            )
            topics.append(
                RawTopic(
                    source=self.name,
                    source_id=str(it.get("id")),
                    title=title,
                    url=url,
                    summary=it.get("text"),
                    published_at=published,
                    raw_payload={
                        "score": it.get("score"),
                        "descendants": it.get("descendants"),
                        "by": it.get("by"),
                        "type": it.get("type"),
                    },
                )
            )
        return topics
