"""Language-aware ScriptWriter tests — pure helpers, no Gemini call.

Verifies the language → prompt-file routing, the English / Korean
estimate-seconds heuristic, and the front-matter / excerpt parsing
without invoking the live Gemini CLI.
"""
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from scripts.agents.script_writer import ScriptWriterAgent, _LANG_CONFIG


# ----------------------------------------------------------------------
# _LANG_CONFIG sanity
# ----------------------------------------------------------------------


def test_lang_config_has_ko_and_en_with_distinct_prompt_files():
    assert "ko" in _LANG_CONFIG
    assert "en" in _LANG_CONFIG
    assert _LANG_CONFIG["en"]["prompt_file"] != _LANG_CONFIG["ko"]["prompt_file"]
    assert _LANG_CONFIG["en"]["prompt_file"].endswith("_en_system.md")


# ----------------------------------------------------------------------
# _estimate_seconds language switching
# ----------------------------------------------------------------------


def test_estimate_seconds_korean_uses_4_chars_per_sec():
    text = "안녕하세요" * 20  # 100 chars
    sec = ScriptWriterAgent._estimate_seconds(text, "ko")
    assert 20 <= sec <= 30  # ~25s


def test_estimate_seconds_english_is_faster_per_char():
    text = "Good evening." * 20  # ~260 chars including spaces
    sec = ScriptWriterAgent._estimate_seconds(text, "en")
    assert sec < ScriptWriterAgent._estimate_seconds(text, "ko")


# ----------------------------------------------------------------------
# Excerpt header stripping by language
# ----------------------------------------------------------------------


def test_excerpt_strips_korean_references_when_korean_headers_passed():
    agent = ScriptWriterAgent()
    body = """## 본론
첫 번째 섹션 내용입니다.

## 참고자료
[링크](https://example.com)
"""
    out = agent._extract_body_excerpt(body, ref_headers=("## 참고자료",))
    assert "참고자료" not in out
    assert "첫 번째" in out


def test_excerpt_strips_english_references_when_en_headers_passed():
    agent = ScriptWriterAgent()
    body = """## Body
First section content here.

## References
- [link](https://example.com)
"""
    out = agent._extract_body_excerpt(body, ref_headers=("## References",))
    assert "References" not in out
    assert "First section" in out


# ----------------------------------------------------------------------
# Run() routes to the right prompt builder
# ----------------------------------------------------------------------


def _write_post(tmp_path: Path, slug: str, body_lang: str) -> Path:
    """Write a minimal valid post markdown for the given language."""
    if body_lang == "en":
        text = """---
title: "Sample English Post"
description: "A short summary."
ai_opinion: "Editor commentary."
---

## Background

Section one body content with detail.

## Development

Section two body content with detail.
"""
    else:
        text = """---
title: "샘플 한국어 포스트"
description: "짧은 요약."
ai_opinion: "에디터 의견."
---

## 배경

섹션 1 본문.

## 본론

섹션 2 본문.
"""
    path = tmp_path / f"{slug}.md"
    path.write_text(text, encoding="utf-8")
    return path


def test_run_uses_english_prompt_when_language_en(tmp_path):
    agent = ScriptWriterAgent()
    post = _write_post(tmp_path, "sample", "en")

    captured = {}

    def fake_call(prompt: str) -> str:
        captured["prompt"] = prompt
        # Return a long enough English script to pass min_chars=200.
        return (
            "Tonight a major AI lab announced something. "
            "Good evening, I'm your anchor for MindTickleBytes. "
            "Background context here. Development sentence one. "
            "Development sentence two. Development sentence three. "
            "Development sentence four. Why it matters explained here. "
            "Stakeholder impact explained here. Outlook sentence here. "
            "For MindTickleBytes, I'm your anchor. Stay curious."
        )

    with patch.object(agent.gemini, "call", side_effect=fake_call):
        result = agent.run(post, channel_name="MindTickleBytes", language="en")

    assert result is not None
    assert "Channel name" in captured["prompt"]  # English prompt body
    assert "MindTickleBytes" in captured["prompt"]
    assert "MindTickleBytes" in result


def test_run_uses_korean_prompt_when_language_ko(tmp_path):
    agent = ScriptWriterAgent()
    post = _write_post(tmp_path, "sample", "ko")

    captured = {}

    def fake_call(prompt: str) -> str:
        captured["prompt"] = prompt
        return (
            "안녕하세요, MindTickleBytes입니다. 오늘의 핵심 소식을 전해드립니다. "
            "이것은 충분히 긴 한국어 스크립트입니다. 본문 내용이 이어집니다. "
            "추가 문장이 들어갑니다. 마지막 문장입니다."
        )

    with patch.object(agent.gemini, "call", side_effect=fake_call):
        result = agent.run(post, channel_name="MindTickleBytes", language="ko")

    assert result is not None
    assert "채널명" in captured["prompt"]  # Korean prompt body


def test_run_rejects_too_short_english_output(tmp_path):
    agent = ScriptWriterAgent()
    post = _write_post(tmp_path, "sample", "en")
    with patch.object(agent.gemini, "call", return_value="Just a tiny thing."):
        result = agent.run(post, language="en")
    assert result is None


def test_run_returns_none_for_missing_post(tmp_path):
    agent = ScriptWriterAgent()
    result = agent.run(tmp_path / "nope.md", language="en")
    assert result is None
