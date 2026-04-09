"""publisher: commit message format + safety checks."""
from __future__ import annotations

from scripts.app.publisher import _build_commit_message
from scripts.app.schemas import PipelineResult


def test_commit_message_contains_key_fields():
    r = PipelineResult(
        success=True,
        slug="2026-04-09-gpt5-analysis",
        title_ko="GPT-5 심층 분석",
        files=["2026-04-09-gpt5-analysis.md", "2026-04-09-gpt5-analysis.en.md"],
        image_file="2026-04-09-gpt5-analysis.jpg",
        languages=["ko", "en", "ja"],
        revision_count=1,
        run_id=42,
        source="hackernews",
    )
    msg = _build_commit_message(r)
    assert "GPT-5 심층 분석" in msg
    assert "2026-04-09-gpt5-analysis" in msg
    assert "hackernews" in msg
    assert "Run ID: 42" in msg
    assert "ko,en,ja" in msg
    assert "Fact-check revisions: 1" in msg
