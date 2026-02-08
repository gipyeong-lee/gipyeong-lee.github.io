"""Researcher Agent — searches the web, validates URLs, extracts structured facts."""

from typing import List, Optional

from duckduckgo_search import DDGS

from .base import BaseAgent
from ..models import Source, KeyFact, ResearchBrief
from ..url_validator import validate_urls


class ResearcherAgent(BaseAgent):
    name = "Researcher"
    prompt_file = "researcher_system.md"

    MIN_LIVE_SOURCES = 5

    def run(self, topic: str) -> Optional[ResearchBrief]:
        """Research a topic and return a verified ResearchBrief."""
        self.log(f"Starting research on: {topic}")

        # 1. Search with query variations
        raw_results = self._search(topic)
        if not raw_results:
            self.log("Search returned no results. Aborting.")
            return None

        # 2. Build source list and validate URLs
        sources = self._build_sources(raw_results)
        sources = self._validate_sources(sources)

        live_sources = [s for s in sources if s.is_live]
        self.log(f"Live sources: {len(live_sources)} / {len(sources)}")

        if len(live_sources) < self.MIN_LIVE_SOURCES:
            self.log(
                f"Insufficient live sources ({len(live_sources)} < {self.MIN_LIVE_SOURCES}). "
                "Aborting pipeline."
            )
            return None

        # 3. Extract structured facts via Gemini
        brief = self._extract_facts(topic, live_sources)
        return brief

    def _search(self, topic: str) -> List[dict]:
        """Search DuckDuckGo with 3 query variations."""
        queries = [
            topic,
            f"{topic} 기술 분석",
            f"{topic} latest news 2025",
        ]
        all_results = []
        seen_urls = set()

        for query in queries:
            self.log(f"Searching: {query}")
            try:
                with DDGS() as ddgs:
                    results = list(ddgs.text(query, max_results=7))
                for r in results:
                    url = r.get("href", "")
                    if url and url not in seen_urls:
                        seen_urls.add(url)
                        all_results.append(r)
            except Exception as e:
                self.log(f"Search failed for '{query}': {e}")

        self.log(f"Total unique results: {len(all_results)}")
        return all_results

    def _build_sources(self, raw_results: List[dict]) -> List[Source]:
        """Convert raw search results to Source objects."""
        sources = []
        for i, r in enumerate(raw_results, start=1):
            sources.append(
                Source(
                    index=i,
                    title=r.get("title", ""),
                    url=r.get("href", ""),
                    snippet=r.get("body", ""),
                )
            )
        return sources

    def _validate_sources(self, sources: List[Source]) -> List[Source]:
        """Validate all source URLs in parallel."""
        self.log(f"Validating {len(sources)} URLs...")
        urls = [s.url for s in sources]
        results = validate_urls(urls, max_workers=5)

        url_status = {url: (is_live, code) for url, is_live, code in results}
        for s in sources:
            is_live, code = url_status.get(s.url, (False, 0))
            s.is_live = is_live
            s.http_status = code

        return sources

    def _extract_facts(self, topic: str, live_sources: List[Source]) -> Optional[ResearchBrief]:
        """Use Gemini to extract structured facts from source snippets."""
        self.log("Extracting structured facts from sources...")

        # Build source reference text
        source_text = ""
        for s in live_sources:
            source_text += (
                f"[Source {s.index}] {s.title}\n"
                f"URL: {s.url}\n"
                f"Snippet: {s.snippet}\n\n"
            )

        system_prompt = self.get_system_prompt()
        prompt = f"""{system_prompt}

## TOPIC
{topic}

## SOURCE SNIPPETS
{source_text}

Extract structured facts from ONLY the above source snippets. Return valid JSON."""

        data = self.gemini.call_json(prompt)
        if not data or not isinstance(data, dict):
            self.log("Failed to extract facts from Gemini response.")
            return None

        # Parse into ResearchBrief
        def parse_facts(items: list) -> List[KeyFact]:
            facts = []
            for item in (items or []):
                if isinstance(item, dict):
                    facts.append(
                        KeyFact(
                            statement=item.get("statement", ""),
                            source_indices=item.get("source_indices", []),
                        )
                    )
            return facts

        brief = ResearchBrief(
            topic=topic,
            summary=data.get("summary", ""),
            verified_sources=live_sources,
            key_facts=parse_facts(data.get("key_facts")),
            statistics=parse_facts(data.get("statistics")),
            expert_quotes=parse_facts(data.get("expert_quotes")),
        )

        self.log(
            f"Extracted {len(brief.key_facts)} facts, "
            f"{len(brief.statistics)} statistics, "
            f"{len(brief.expert_quotes)} quotes"
        )
        return brief
