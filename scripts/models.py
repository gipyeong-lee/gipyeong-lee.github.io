"""Data models for the fact-checked blog post pipeline."""

from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum


@dataclass
class Source:
    """A verified web source."""
    index: int
    title: str
    url: str
    snippet: str
    is_live: bool = False
    http_status: Optional[int] = None


@dataclass
class KeyFact:
    """A fact extracted from research sources."""
    statement: str
    source_indices: List[int]  # References to Source.index


@dataclass
class ResearchBrief:
    """Output of the ResearcherAgent."""
    topic: str
    summary: str
    verified_sources: List[Source]
    key_facts: List[KeyFact]
    statistics: List[KeyFact]
    expert_quotes: List[KeyFact]

    def get_source_by_index(self, idx: int) -> Optional[Source]:
        for s in self.verified_sources:
            if s.index == idx:
                return s
        return None

    def get_source_urls(self) -> set:
        return {s.url for s in self.verified_sources}


@dataclass
class Claim:
    """A factual claim extracted from a draft post."""
    text: str
    cited_url: Optional[str] = None
    matches_source: Optional[bool] = None
    source_index: Optional[int] = None
    issue: Optional[str] = None


class Verdict(Enum):
    PASS = "PASS"
    NEEDS_REVISION = "NEEDS_REVISION"
    FAIL = "FAIL"


@dataclass
class FactCheckReport:
    """Output of the FactCheckerAgent."""
    verdict: Verdict
    claims_checked: int
    claims_verified: int
    claims_unverified: int
    dead_links: List[str] = field(default_factory=list)
    issues: List[str] = field(default_factory=list)
    revision_instructions: Optional[str] = None
