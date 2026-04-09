"""Video pipeline module tests — pure-Python helpers, no ML stack needed.

These tests exercise:
- diagnostics.classify_video_error: error text → category mapping
- diagnostics.video_category_should_block: block-decision for quota/oauth
- video_pipeline._build_description: description composer
- video_worker._read_post_meta: front matter parser
"""
from __future__ import annotations

from pathlib import Path

import pytest

from scripts.app.diagnostics import (
    classify_video_error,
    video_category_should_block,
    VIDEO_CATEGORIES,
)
from scripts.app.video_pipeline import _build_description
from scripts.app.video_worker import _read_post_meta, _has_hero_image


# ----------------------------------------------------------------------
# classify_video_error
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "error,category",
    [
        ("pipeline timeout after 900s", "video_timeout"),
        ("quotaExceeded when calling videos.insert", "video_upload_quota"),
        ("daily upload cap reached (5)", "video_upload_quota"),
        ("invalid_grant: Token has been expired or revoked", "video_oauth_expired"),
        ("refresh token missing", "video_oauth_expired"),
        ("client_secrets.json not at ...", "video_oauth_expired"),
        ("tts runner stderr: missing model", "video_tts_failed"),
        ("melo.api import failed", "video_tts_failed"),
        ("tts crashed: out of memory", "video_tts_failed"),
        ("compose crashed: moviepy", "video_compose_failed"),
        ("no mp4 output", "video_compose_failed"),
        ("hero image not found for slug foo", "video_compose_failed"),
        ("ffmpeg exited 1", "video_compose_failed"),
        ("script writer returned empty", "video_script_failed"),
        ("post file not found for slug foo", "video_script_failed"),
        ("upload returned None", "video_upload_failed"),
        ("", "video_unknown"),
        (None, "video_unknown"),
        ("some completely unrelated text", "video_unknown"),
    ],
)
def test_classify_video_error(error, category):
    assert classify_video_error(error) == category
    assert category in VIDEO_CATEGORIES


def test_video_category_should_block_only_quota_and_oauth():
    assert video_category_should_block("video_upload_quota") is True
    assert video_category_should_block("video_oauth_expired") is True
    assert video_category_should_block("video_tts_failed") is False
    assert video_category_should_block("video_compose_failed") is False
    assert video_category_should_block("video_unknown") is False


# ----------------------------------------------------------------------
# _build_description
# ----------------------------------------------------------------------


def test_description_embeds_permalink_and_channel_hashtag():
    desc = _build_description(
        description="AI 음성 혁명",
        permalink="/2026/04/09/gemini/",
        tags=["Gemini", "Voice AI"],
        channel="Antigravity News",
    )
    assert "AI 음성 혁명" in desc
    assert "https://gipyeong-lee.github.io/2026/04/09/gemini/" in desc
    # Channel hashtag — spaces stripped.
    assert "#AntigravityNews" in desc
    # Tag hashtags preserved (minus spaces).
    assert "#Gemini" in desc
    assert "#VoiceAI" in desc


def test_description_ok_without_permalink():
    desc = _build_description(
        description="summary", permalink="", tags=None, channel="X Y"
    )
    assert "summary" in desc
    # No link line when permalink empty.
    assert "원문:" not in desc
    assert "#XY" in desc


def test_description_handles_absolute_permalink():
    desc = _build_description(
        description="d", permalink="https://example.com/a", tags=None, channel="N"
    )
    assert "https://example.com/a" in desc


# ----------------------------------------------------------------------
# _read_post_meta
# ----------------------------------------------------------------------


def test_read_post_meta_parses_front_matter(tmp_path, monkeypatch):
    posts_dir = tmp_path / "_posts"
    posts_dir.mkdir()
    slug = "2026-01-01-sample"
    (posts_dir / f"{slug}.md").write_text(
        """---
layout: post
title: "테스트 제목"
description: "요약 설명"
tags: [AI, "Claude 4.6", "Sonnet"]
permalink: /2026/01/01/sample/
lang: ko
ref: 2026-01-01-sample
---

# 본문
""",
        encoding="utf-8",
    )
    monkeypatch.setattr("scripts.app.video_worker.POSTS_DIR", posts_dir)

    meta = _read_post_meta(slug)
    assert meta["title"] == "테스트 제목"
    assert meta["description"] == "요약 설명"
    assert meta["permalink"] == "/2026/01/01/sample/"
    # Tags parse: list with spaces+quotes stripped.
    assert meta["tags"] == ["AI", "Claude 4.6", "Sonnet"]


def test_read_post_meta_missing_file_returns_empty(tmp_path, monkeypatch):
    monkeypatch.setattr("scripts.app.video_worker.POSTS_DIR", tmp_path)
    assert _read_post_meta("nope") == {}


# ----------------------------------------------------------------------
# _has_hero_image
# ----------------------------------------------------------------------


def test_has_hero_image_detects_jpg(tmp_path, monkeypatch):
    monkeypatch.setattr("scripts.app.video_worker.IMAGES_DIR", tmp_path)
    (tmp_path / "slug-a.jpg").write_bytes(b"\xff\xd8")  # fake JPEG magic
    assert _has_hero_image("slug-a") is True
    assert _has_hero_image("slug-b") is False
