"""Async wrapper around `scripts.pipeline.Pipeline`.

Responsibilities:
- Inject an observer that routes stage events to the logging_bus + DB.
- Optionally inject a seeded researcher when the topic has a source URL.
- Run the synchronous pipeline via `asyncio.to_thread` with a timeout.
- Discover the output post files after the pipeline finishes so the
  publisher knows what to stage.
"""
from __future__ import annotations

import asyncio
import datetime
import re
from pathlib import Path
from typing import Iterable

from ..pipeline import Pipeline
from ..agents import ResearcherAgent
from ..agents.fact_checker import FactCheckerAgent, FactCheckerConfig
from .config import IMAGES_DIR, POSTS_DIR
from .logging_bus import ObserverImpl
from .models_db import Topic
from .schemas import PipelineResult
from .settings_store import get_settings

_LANG_SUFFIX_RE = re.compile(r"\.(en|ja|zh-cn|zh-tw)\.md$")


class _SeededResearcher(ResearcherAgent):
    """ResearcherAgent variant that prepends a known-good source URL.

    We don't subclass `_search` internals because the base class API
    isn't guaranteed to stay the same — instead, we override `run` and
    monkeypatch the source list after the fact. If the parent signature
    changes, we fall back to the base agent transparently.
    """

    def __init__(self, seed_url: str, seed_title: str):
        super().__init__()
        self.seed_url = seed_url
        self.seed_title = seed_title

    def run(self, topic: str):  # type: ignore[override]
        try:
            brief = super().run(topic)
        except Exception:
            return super().run(topic)
        if brief is None:
            return None
        # Best-effort: ensure seed url is in verified_sources if not already.
        try:
            existing_urls = {s.url for s in brief.verified_sources}
            if self.seed_url not in existing_urls:
                from ..models import Source

                seed = Source(
                    title=self.seed_title or topic,
                    url=self.seed_url,
                    snippet=None,
                )
                brief.verified_sources.insert(0, seed)
        except Exception:
            pass
        return brief


def _collect_output_files(slug: str) -> tuple[list[str], str | None, list[str]]:
    """Find all files written for this slug.

    Returns (post_file_basenames, image_basename_or_None, languages_found).
    """
    post_files: list[str] = []
    langs: list[str] = []
    posts_path = Path(POSTS_DIR)
    if posts_path.exists():
        for p in posts_path.iterdir():
            if not p.is_file() or not p.name.startswith(slug):
                continue
            if not p.name.endswith(".md"):
                continue
            post_files.append(p.name)
            m = _LANG_SUFFIX_RE.search(p.name)
            if m:
                langs.append(m.group(1))
            elif p.name == f"{slug}.md":
                langs.append("ko")
    image_file: str | None = None
    images_path = Path(IMAGES_DIR)
    if images_path.exists():
        for ext in ("jpg", "jpeg", "png", "webp"):
            candidate = images_path / f"{slug}.{ext}"
            if candidate.exists():
                image_file = candidate.name
                break
    return sorted(post_files), image_file, sorted(set(langs))


class PipelineRunner:
    """Runs one pipeline cycle for a given topic."""

    def __init__(self, observer: ObserverImpl):
        self.observer = observer

    async def run(
        self,
        topic: Topic | None,
        *,
        run_id: int,
        custom_topic: str | None = None,
        custom_url: str | None = None,
        source_label: str | None = None,
        timeout_seconds: int = 20 * 60,
    ) -> PipelineResult:
        topic_text, seed_url, seed_title = self._resolve_topic(topic, custom_topic, custom_url)

        researcher = None
        if seed_url:
            try:
                researcher = _SeededResearcher(seed_url, seed_title or topic_text)
            except Exception:
                researcher = None

        # Build a fact-checker with current runtime thresholds so Admin UI
        # tuning takes effect on the next run without a restart.
        settings = get_settings()
        fc_config = FactCheckerConfig(
            fail_ratio=settings.fact_check_fail_ratio,
            revision_ratio=settings.fact_check_revision_ratio,
            dead_link_tolerance=settings.fact_check_dead_link_tolerance,
            relaxation_per_round=settings.fact_check_relaxation_per_round,
        )
        fact_checker = FactCheckerAgent(config=fc_config)

        pipeline = Pipeline(
            observer=self.observer,
            researcher=researcher,
            fact_checker=fact_checker,
            max_revision_rounds=settings.max_revision_rounds,
        )

        def _run_sync() -> bool:
            return pipeline.run(topic_text)

        try:
            success: bool = await asyncio.wait_for(
                asyncio.to_thread(_run_sync),
                timeout=timeout_seconds,
            )
        except asyncio.TimeoutError:
            return PipelineResult(
                success=False,
                error=f"pipeline timeout after {timeout_seconds}s",
                run_id=run_id,
                source=source_label or (topic.source if topic else "manual"),
            )
        except Exception as e:
            return PipelineResult(
                success=False,
                error=f"{type(e).__name__}: {e}",
                run_id=run_id,
                source=source_label or (topic.source if topic else "manual"),
            )

        slug = self.observer.last_slug or ""
        files, image_file, languages = _collect_output_files(slug)

        if not success or not files:
            return PipelineResult(
                success=False,
                slug=slug or None,
                files=files,
                image_file=image_file,
                languages=languages,
                error=None if success else (self.observer.last_error or "pipeline returned False"),
                run_id=run_id,
                source=source_label or (topic.source if topic else "manual"),
            )

        return PipelineResult(
            success=True,
            slug=slug,
            title_ko=topic.title if topic else (custom_topic or topic_text),
            files=files,
            image_file=image_file,
            languages=languages,
            revision_count=self.observer.revision_count,
            run_id=run_id,
            source=source_label or (topic.source if topic else "manual"),
        )

    def _resolve_topic(
        self,
        topic: Topic | None,
        custom_topic: str | None,
        custom_url: str | None,
    ) -> tuple[str, str | None, str | None]:
        if custom_topic:
            return custom_topic.strip(), (custom_url or None), custom_topic
        if topic is None:
            raise ValueError("either topic or custom_topic is required")
        return topic.title, topic.url, topic.title
