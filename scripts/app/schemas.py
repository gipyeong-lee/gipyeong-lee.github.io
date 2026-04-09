"""Pydantic DTOs for the admin API + inter-module messages.

Kept intentionally small — the admin is CRUD-ish and the templates do
most of the rendering, so most responses are just dicts. These DTOs are
used where shape matters (events pushed over SSE, topic seed objects,
pipeline results).
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field


# -- Topic seed from sources --------------------------------------------


class RawTopic(BaseModel):
    """A topic discovered by a SourceAdapter, pre-dedup, pre-persistence."""

    source: str
    source_id: Optional[str] = None
    title: str
    url: Optional[str] = None
    summary: Optional[str] = None
    published_at: Optional[datetime] = None
    raw_payload: dict[str, Any] = Field(default_factory=dict)


class ScoredTopic(BaseModel):
    """RawTopic after the scorer has assigned a score + canonical url."""

    raw: RawTopic
    canonical_url: Optional[str]
    score: float
    keyword_hits: list[str] = Field(default_factory=list)


# -- Pipeline result -----------------------------------------------------


class PipelineResult(BaseModel):
    success: bool
    slug: Optional[str] = None
    title_ko: Optional[str] = None
    files: list[str] = Field(default_factory=list)         # basenames in _posts/
    image_file: Optional[str] = None                        # basename in images/
    languages: list[str] = Field(default_factory=list)
    revision_count: int = 0
    error: Optional[str] = None
    run_id: Optional[int] = None
    source: Optional[str] = None


# -- SSE events ----------------------------------------------------------

EventKind = Literal[
    "run_start",
    "stage_start",
    "stage_end",
    "revision",
    "log",
    "run_end",
    "queue_updated",
    "source_polled",
]


class StreamEvent(BaseModel):
    kind: EventKind
    run_id: Optional[int] = None
    stage: Optional[str] = None
    level: Optional[str] = None
    message: Optional[str] = None
    meta: dict[str, Any] = Field(default_factory=dict)
    ts: datetime = Field(default_factory=datetime.utcnow)


# -- Manual trigger request ----------------------------------------------


class ManualTriggerRequest(BaseModel):
    topic_id: Optional[int] = None
    custom_topic: Optional[str] = None
    custom_url: Optional[str] = None
