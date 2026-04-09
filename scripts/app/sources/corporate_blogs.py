"""Corporate AI lab blog sources.

Each source has a stable `name` used as the DB source key. We try RSS
first, and fall back to HTML scraping for labs without a reliable feed.
All labs are treated as 1st-party AI sources → keyword gate is skipped.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, ClassVar

import feedparser
import httpx
from bs4 import BeautifulSoup

from ..schemas import RawTopic
from .base import USER_AGENT, SourceAdapter
from .keywords import is_ai_relevant

# Common navigation / menu text that shows up when scraping corporate sites
# with no real article feed. Filter these out pre-emptively.
_NAV_BLOCKLIST = {
    "research", "customers", "contact", "contact sales", "try studio",
    "products", "pricing", "about", "careers", "blog", "news", "home",
    "sign in", "log in", "get started", "learn more", "read more",
    "documentation", "docs", "api", "developers", "partners", "company",
    "solutions", "use cases", "resources", "support", "community",
    "privacy", "terms", "cookie", "legal",
}


class _RssBlogSource(SourceAdapter):
    feed_url: ClassVar[str] = ""
    html_fallback_url: ClassVar[str | None] = None

    def __init__(self, client: httpx.AsyncClient | None = None) -> None:
        self._client = client

    async def poll(self) -> list[RawTopic]:
        own = self._client is None
        client = self._client or httpx.AsyncClient(
            timeout=20.0, headers={"user-agent": USER_AGENT}
        )
        try:
            if self.feed_url:
                try:
                    r = await client.get(self.feed_url)
                    r.raise_for_status()
                    feed = feedparser.parse(r.text)
                    if feed.entries:
                        return self._entries_to_raw(feed.entries)
                except Exception:
                    pass
            if self.html_fallback_url:
                return await self._html_scrape(client)
            return []
        finally:
            if own:
                await client.aclose()

    def _entries_to_raw(self, entries: list[Any]) -> list[RawTopic]:
        out: list[RawTopic] = []
        for e in entries:
            title = (e.get("title") or "").strip()
            link = e.get("link") or ""
            if not title or not link:
                continue
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
                    source_id=link,
                    title=title,
                    url=link,
                    summary=e.get("summary", ""),
                    published_at=published,
                    raw_payload={},
                )
            )
        return out

    async def _html_scrape(self, client: httpx.AsyncClient) -> list[RawTopic]:
        try:
            r = await client.get(self.html_fallback_url or "")
            r.raise_for_status()
        except Exception:
            return []
        soup = BeautifulSoup(r.text, "html.parser")
        out: list[RawTopic] = []
        seen: set[str] = set()
        for a in soup.find_all("a", href=True):
            href = a["href"]
            title = a.get_text(strip=True)
            if not title or len(title) < 12:
                continue
            # Skip common nav/menu text
            if title.lower().strip() in _NAV_BLOCKLIST:
                continue
            # For HTML scrapes we require AI-relevance since we can't
            # trust that a random anchor represents a blog post.
            if not is_ai_relevant(title):
                continue
            if href.startswith("/"):
                from urllib.parse import urljoin
                href = urljoin(self.html_fallback_url or "", href)
            if not href.startswith("http"):
                continue
            if href in seen:
                continue
            seen.add(href)
            out.append(
                RawTopic(
                    source=self.name,
                    source_id=href,
                    title=title,
                    url=href,
                    summary=None,
                    raw_payload={"scrape": True},
                )
            )
            if len(out) >= 30:
                break
        return out


class OpenAIBlogSource(_RssBlogSource):
    name = "openai_blog"
    feed_url = "https://openai.com/blog/rss.xml"
    html_fallback_url = "https://openai.com/news/"


class AnthropicBlogSource(_RssBlogSource):
    name = "anthropic_blog"
    feed_url = "https://www.anthropic.com/news/rss.xml"
    html_fallback_url = "https://www.anthropic.com/news"


class DeepMindBlogSource(_RssBlogSource):
    name = "deepmind_blog"
    feed_url = "https://deepmind.google/blog/rss.xml"
    html_fallback_url = "https://deepmind.google/discover/blog/"


class MetaAIBlogSource(_RssBlogSource):
    name = "meta_ai_blog"
    feed_url = "https://ai.meta.com/blog/rss/"
    html_fallback_url = "https://ai.meta.com/blog/"


class XAIBlogSource(_RssBlogSource):
    name = "xai_blog"
    feed_url = ""
    html_fallback_url = "https://x.ai/blog"


class MistralBlogSource(_RssBlogSource):
    name = "mistral_blog"
    feed_url = ""
    html_fallback_url = "https://mistral.ai/news/"


ALL_CORPORATE_SOURCES: list[type[SourceAdapter]] = [
    OpenAIBlogSource,
    AnthropicBlogSource,
    DeepMindBlogSource,
    MetaAIBlogSource,
    XAIBlogSource,
    MistralBlogSource,
]
