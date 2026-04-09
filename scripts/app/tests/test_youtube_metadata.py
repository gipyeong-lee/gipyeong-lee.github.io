"""Pure-Python tests for YouTubeMetadataAgent helpers + SRT builder.

No network, no subprocess. We call the public YouTubeMetadataAgent.run()
only by monkeypatching `gemini.call_json` to return a canned payload,
which exercises the parse + placeholder resolution code paths without
needing the real Gemini CLI.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from scripts.agents.youtube_metadata import (
    YouTubeMetadata,
    YouTubeMetadataAgent,
    _format_timestamp,
    _parse_timestamp_to_seconds,
    _sanitize_tags,
    _split_sentences,
    _srt_timestamp,
    build_srt_captions,
)


# ----------------------------------------------------------------------
# Timestamp helpers
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "seconds,expected",
    [
        (0, "00:00"),
        (5, "00:05"),
        (65, "01:05"),
        (3600, "01:00:00"),
        (3725, "01:02:05"),
    ],
)
def test_format_timestamp(seconds, expected):
    assert _format_timestamp(seconds) == expected


def test_parse_timestamp_roundtrip():
    for s in (0, 59, 60, 125, 3725):
        assert _parse_timestamp_to_seconds(_format_timestamp(s)) == s


def test_srt_timestamp_format():
    assert _srt_timestamp(0) == "00:00:00,000"
    assert _srt_timestamp(1.5) == "00:00:01,500"
    assert _srt_timestamp(65.25) == "00:01:05,250"


# ----------------------------------------------------------------------
# Tag sanitizer
# ----------------------------------------------------------------------


def test_sanitize_tags_dedup_and_trim():
    tags = ["AI", "ai", "#Claude", "  Claude ", "A" * 40, ""]
    cleaned = _sanitize_tags(tags)
    # Case-insensitive dedup → only one 'AI' and one 'Claude'.
    assert len(cleaned) == 3
    # Leading '#' stripped.
    assert all(not t.startswith("#") for t in cleaned)
    # Length cap of 30.
    assert all(len(t) <= 30 for t in cleaned)


def test_sanitize_tags_hard_cap_25():
    tags = [f"tag{i}" for i in range(40)]
    assert len(_sanitize_tags(tags)) == 25


# ----------------------------------------------------------------------
# Sentence splitter / SRT builder
# ----------------------------------------------------------------------


def test_split_sentences_basic():
    text = "안녕하세요. 오늘의 AI 뉴스입니다. 첫 소식을 전해드립니다."
    s = _split_sentences(text)
    assert len(s) == 3
    assert s[0].startswith("안녕")


def test_split_sentences_empty():
    assert _split_sentences("") == []


def test_build_srt_captions_structure():
    script = "안녕하세요. 오늘의 AI 뉴스입니다. 첫 소식을 전해드립니다."
    srt = build_srt_captions(script, narration_duration_seconds=9.0, intro_offset_seconds=3.0)
    # Three blocks, 1-indexed numbering.
    assert srt.startswith("1\n")
    assert "\n2\n" in srt
    assert "\n3\n" in srt
    # First caption must start at intro offset (03.000).
    assert "00:00:03,000 -->" in srt
    # Last caption ends ≈ intro_offset + narration_duration = 12s.
    assert "00:00:12,000" in srt


def test_build_srt_captions_empty_returns_blank():
    assert build_srt_captions("", narration_duration_seconds=5.0) == ""
    assert build_srt_captions("text", narration_duration_seconds=0.0) == ""


# ----------------------------------------------------------------------
# YouTubeMetadata.from_fallback
# ----------------------------------------------------------------------


def test_fallback_caps_title_at_90_chars():
    long = "x" * 200
    meta = YouTubeMetadata.from_fallback(
        title=long,
        description="d",
        tags=[],
        permalink="",
        channel_name="N",
    )
    assert len(meta.title) == 90


# ----------------------------------------------------------------------
# YouTubeMetadataAgent.run with stubbed Gemini
# ----------------------------------------------------------------------


def _make_post(tmp_path: Path) -> Path:
    p = tmp_path / "_posts" / "2026-04-09-sample.md"
    p.parent.mkdir(parents=True)
    p.write_text(
        '---\n'
        'layout: post\n'
        'title: "샘플 포스트"\n'
        'description: "요약"\n'
        'ai_opinion: "AI 관점"\n'
        'tags: [AI, Claude]\n'
        'lang: ko\n'
        '---\n'
        '\n'
        '## 시장의 상황\n본문 1\n\n## 기술적 배경\n본문 2\n',
        encoding="utf-8",
    )
    return p


def test_metadata_agent_happy_path(tmp_path, monkeypatch):
    post_path = _make_post(tmp_path)

    def fake_call_json(self, prompt):  # noqa: ANN001
        return {
            "title": "🤖 샘플 뉴스 — 클로드 소넷 4.6",
            "description": (
                "첫 훅 문장입니다.\n\n"
                "__CHAPTERS__\n\n"
                "📌 이 영상에서 다루는 내용\n"
                "• 포인트 1\n• 포인트 2\n• 포인트 3\n\n"
                "🔗 원문 기사\n__PERMALINK__\n\n"
                "🏷 관련 해시태그\n#AI #클로드"
            ),
            "tags": ["AI", "Claude", "Anthropic", "클로드", "AI 뉴스"],
            "chapters": [
                {"label": "오프닝", "section": "opening"},
                {"label": "핵심 요약", "section": "intro"},
                {"label": "기술 배경", "section": "body"},
                {"label": "마무리", "section": "closing"},
            ],
            "keywords": ["#AI", "#Claude"],
        }

    from scripts.agents.base import GeminiCLI

    monkeypatch.setattr(GeminiCLI, "call_json", fake_call_json)

    agent = YouTubeMetadataAgent()
    meta = agent.run(
        post_path=post_path,
        narration_script="문장 하나. 문장 둘. 문장 셋.",
        narration_duration_seconds=60.0,
        intro_seconds=3.0,
        permalink="/2026/04/09/sample/",
    )
    assert "샘플 뉴스" in meta.title
    # Chapters placeholder resolved into timestamps.
    assert "__CHAPTERS__" not in meta.description
    assert "00:00 오프닝" in meta.description
    # Permalink placeholder resolved.
    assert "__PERMALINK__" not in meta.description
    assert "https://gipyeong-lee.github.io/2026/04/09/sample/" in meta.description
    # Tags sanitized.
    assert "AI" in meta.tags
    assert all(not t.startswith("#") for t in meta.tags)


def test_metadata_agent_falls_back_on_bad_json(tmp_path, monkeypatch):
    post_path = _make_post(tmp_path)
    from scripts.agents.base import GeminiCLI

    monkeypatch.setattr(GeminiCLI, "call_json", lambda self, prompt: None)

    agent = YouTubeMetadataAgent()
    meta = agent.run(
        post_path=post_path,
        narration_script="문장.",
        narration_duration_seconds=10.0,
        permalink="/a/b/",
        fallback_title="원본 제목",
        fallback_description="요약",
        fallback_tags=["X"],
    )
    # Fallback used → no chapter placeholder would remain.
    assert "__CHAPTERS__" not in meta.description
    assert "요약" in meta.description
    assert meta.title == "원본 제목"
    assert "원문:" in meta.description


def test_metadata_agent_rejects_missing_required_fields(tmp_path, monkeypatch):
    post_path = _make_post(tmp_path)
    from scripts.agents.base import GeminiCLI

    # Gemini returns JSON but with no title → _parse returns None → fallback.
    monkeypatch.setattr(
        GeminiCLI,
        "call_json",
        lambda self, prompt: {"description": "d", "tags": [], "chapters": []},
    )

    agent = YouTubeMetadataAgent()
    meta = agent.run(
        post_path=post_path,
        narration_script="s",
        narration_duration_seconds=5.0,
        permalink="",
        fallback_title="FB",
        fallback_description="FD",
        fallback_tags=[],
    )
    assert meta.title == "FB"
    assert "FD" in meta.description
