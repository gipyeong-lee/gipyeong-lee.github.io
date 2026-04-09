"""ScriptWriterAgent.run_newscast — multi-topic 50-min broadcast tests.

We don't call Gemini here. The agent is patched so we can verify:
- multi-post input is correctly assembled into the prompt
- topic count + word budget show up in the rendered prompt
- segment-break markers are preserved by the cleaner
- short Gemini output is rejected
- the newscast prompt file (broadcast_en) is selected, not the legacy
"""
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from scripts.agents.script_writer import (
    ScriptWriterAgent,
    SEGMENT_BREAK_MARKER,
    _NEWSCAST_PROMPT_FILE_EN,
)


def _write_post(tmp_path: Path, slug: str, title: str) -> Path:
    text = f"""---
title: "{title}"
description: "Summary for {title}"
ai_opinion: "Editor commentary for {title}"
---

## Background

Background section content for {title}. Two sentences. More words here.

## Development

Development section content for {title}. More detail here.
"""
    p = tmp_path / f"{slug}.md"
    p.write_text(text, encoding="utf-8")
    return p


# ----------------------------------------------------------------------
# Plumbing
# ----------------------------------------------------------------------


def test_run_newscast_returns_none_with_empty_input():
    agent = ScriptWriterAgent()
    assert agent.run_newscast([]) is None


def test_run_newscast_returns_none_when_all_paths_missing(tmp_path):
    agent = ScriptWriterAgent()
    with patch.object(agent.gemini, "call", return_value="x" * 5000):
        result = agent.run_newscast([tmp_path / "nope.md"])
    assert result is None


def test_run_newscast_uses_newscast_prompt_file_and_chunks_calls(tmp_path):
    """Newscast mode loads the heavy prompt and issues one Gemini call per section."""
    agent = ScriptWriterAgent()
    posts = [
        _write_post(tmp_path, f"2026-04-10-topic{i}", f"Topic {i}")
        for i in range(3)
    ]
    captured: list[str] = []
    section_text = (
        "Lengthy section paragraph that exceeds the minimum chunk threshold. " * 35
    )

    def fake_call(prompt: str) -> str:
        captured.append(prompt)
        # First call is the theme builder; subsequent calls are sections.
        return section_text if len(captured) > 1 else "the through-line theme"

    with patch.object(agent.gemini, "call", side_effect=fake_call):
        result = agent.run_newscast(
            posts,
            channel_name="MindTickleBytes",
            target_duration_seconds=60,  # short for test
            language="en",
        )

    assert result is not None
    assert agent.prompt_file == _NEWSCAST_PROMPT_FILE_EN
    # 1 theme + cold_open + anchor_intro + 3 segments + 1 midpoint + closing + signoff
    assert len(captured) == 1 + 8
    # Topic titles must show up in at least one section prompt.
    joined = "\n".join(captured)
    assert "Topic 0" in joined
    assert "Topic 1" in joined
    assert "Topic 2" in joined
    assert "MindTickleBytes" in joined
    # The orchestrator inserts the marker between sections.
    assert SEGMENT_BREAK_MARKER in result


def test_run_newscast_inserts_markers_between_sections(tmp_path):
    """The orchestrator joins chunks with `--- SEGMENT BREAK ---` markers."""
    agent = ScriptWriterAgent()
    posts = [_write_post(tmp_path, f"topic-{i}", f"Topic {i}") for i in range(3)]
    section_text = (
        "Lengthy section paragraph that exceeds the minimum chunk threshold. " * 35
    )
    with patch.object(agent.gemini, "call", return_value=section_text):
        result = agent.run_newscast(
            posts, target_duration_seconds=60, language="en"
        )
    assert result is not None
    # Sections: cold_open + intro + 3 segments + midpoint + closing + signoff = 8.
    # Marker count = sections - 1 = 7.
    assert result.count(SEGMENT_BREAK_MARKER) == 7


def test_run_newscast_rejects_when_all_chunks_empty(tmp_path):
    agent = ScriptWriterAgent()
    posts = [_write_post(tmp_path, "topic-a", "Topic A")]
    # Empty Gemini responses → every section drops → final script empty.
    with patch.object(agent.gemini, "call", return_value=""):
        result = agent.run_newscast(
            posts, target_duration_seconds=60, language="en"
        )
    assert result is None


def test_run_newscast_strips_markdown_headers_inside_chunks(tmp_path):
    """Inside each chunk the cleaner removes ## headers but body survives."""
    agent = ScriptWriterAgent()
    posts = [_write_post(tmp_path, f"topic-{i}", f"Topic {i}") for i in range(3)]
    chunk = (
        "## Cold Open\n"
        + "First sentence here making sense and reasonable in length. " * 35
    )
    with patch.object(agent.gemini, "call", return_value=chunk):
        result = agent.run_newscast(
            posts, target_duration_seconds=60, language="en"
        )
    assert result is not None
    assert SEGMENT_BREAK_MARKER in result
    assert "## Cold Open" not in result
    assert "First sentence" in result


# ----------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------


def _make_long_script(num_segments: int = 4) -> str:
    """Build a Gemini-style newscast response with N segments."""
    body_sentence = "This is a long sentence with enough characters to pass the minimum length test for newscast scripts and contains substantive broadcast content. "
    parts = []
    for i in range(num_segments):
        parts.append(body_sentence * 5)
        if i < num_segments - 1:
            parts.append(SEGMENT_BREAK_MARKER)
    return "\n\n".join(parts)
