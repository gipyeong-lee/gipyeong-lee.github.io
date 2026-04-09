"""Language-aware path resolution tests for video pipeline + worker."""
from __future__ import annotations

from pathlib import Path

from scripts.app import video_worker
from scripts.app.video_pipeline import _find_post_for_language


def test_find_post_for_language_picks_translation(tmp_path, monkeypatch):
    posts = tmp_path
    (posts / "2026-04-10-sample.md").write_text("ko", encoding="utf-8")
    (posts / "2026-04-10-sample.en.md").write_text("en", encoding="utf-8")
    monkeypatch.setattr("scripts.app.video_pipeline.POSTS_DIR", posts)

    p = _find_post_for_language("2026-04-10-sample", "en")
    assert p is not None
    assert p.name.endswith(".en.md")


def test_find_post_for_language_falls_back_to_korean(tmp_path, monkeypatch):
    posts = tmp_path
    (posts / "2026-04-10-sample.md").write_text("ko", encoding="utf-8")
    monkeypatch.setattr("scripts.app.video_pipeline.POSTS_DIR", posts)

    p = _find_post_for_language("2026-04-10-sample", "en")
    assert p is not None
    assert p.name == "2026-04-10-sample.md"


def test_find_post_for_language_returns_none_when_missing(tmp_path, monkeypatch):
    monkeypatch.setattr("scripts.app.video_pipeline.POSTS_DIR", tmp_path)
    assert _find_post_for_language("nope", "en") is None


def test_has_post_translation_korean_default(tmp_path, monkeypatch):
    monkeypatch.setattr(video_worker, "POSTS_DIR", tmp_path)
    (tmp_path / "slug-a.md").write_text("ko")
    assert video_worker._has_post_translation("slug-a", "ko") is True
    assert video_worker._has_post_translation("slug-b", "ko") is False


def test_has_post_translation_english(tmp_path, monkeypatch):
    monkeypatch.setattr(video_worker, "POSTS_DIR", tmp_path)
    (tmp_path / "slug-a.en.md").write_text("en")
    assert video_worker._has_post_translation("slug-a", "en") is True
    # Korean version absence does NOT block English video.
    assert video_worker._has_post_translation("slug-b", "en") is False
