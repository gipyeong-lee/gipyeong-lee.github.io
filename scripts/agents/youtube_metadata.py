"""YouTube Metadata Agent — generates SEO-rich upload metadata from a post.

Reads a published Korean post and the narration script, asks Gemini CLI
for a structured JSON metadata bundle (title, description, tags,
chapters, keywords), then resolves the two description placeholders
`__CHAPTERS__` and `__PERMALINK__` using real values from the pipeline
context. Chapter timestamps are computed from the narration duration
plus intro offset so the description shows clickable chapter markers in
YouTube.

Design notes
------------
- Uses Gemini CLI (per user policy: no Claude at runtime).
- Returns a dataclass so the video_pipeline can hand it straight to the
  uploader without extra parsing.
- If Gemini returns garbage or times out, `run()` returns a
  `YouTubeMetadata.from_fallback(...)` — a plain concatenation of the
  existing post description + source link, matching the legacy behavior
  so the upload always has *something* to submit.
- SRT caption generation is separate (see `build_srt_captions`) so it
  can be reused by tests and the video_pipeline independently of Gemini.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .base import BaseAgent


# ----------------------------------------------------------------------
# Result dataclass
# ----------------------------------------------------------------------


@dataclass
class YouTubeMetadata:
    title: str
    description: str
    tags: list[str] = field(default_factory=list)
    chapters: list[dict] = field(default_factory=list)
    keywords: list[str] = field(default_factory=list)

    @classmethod
    def from_fallback(
        cls,
        title: str,
        description: str,
        tags: list[str],
        permalink: str,
        channel_name: str,
    ) -> "YouTubeMetadata":
        """Legacy-format fallback when Gemini fails or returns invalid JSON."""
        parts: list[str] = []
        if description:
            parts.append(description.strip())
        if permalink:
            origin = "https://gipyeong-lee.github.io"
            if permalink.startswith("http"):
                parts.append(f"\n원문: {permalink}")
            else:
                parts.append(f"\n원문: {origin}{permalink}")
        hash_tail = " ".join(
            f"#{t.replace(' ', '')}" for t in (tags or [])[:8]
        )
        parts.append(f"\n#{channel_name.replace(' ', '')} #AI #AI뉴스 {hash_tail}".rstrip())
        return cls(
            title=title[:90],
            description="\n".join(parts).strip(),
            tags=list(tags or [])[:25],
            chapters=[],
            keywords=[],
        )


# ----------------------------------------------------------------------
# Agent
# ----------------------------------------------------------------------


class YouTubeMetadataAgent(BaseAgent):
    """Generates YouTube upload metadata from a published post + narration."""

    name = "YouTubeMetadata"
    prompt_file = "youtube_metadata_system.md"

    def run(
        self,
        *,
        post_path: str | Path,
        narration_script: str,
        narration_duration_seconds: float,
        intro_seconds: float = 3.0,
        channel_name: str = "Antigravity News",
        permalink: str = "",
        fallback_title: str = "",
        fallback_description: str = "",
        fallback_tags: Optional[list[str]] = None,
    ) -> YouTubeMetadata:
        """Return a fully-resolved YouTubeMetadata. Never raises."""
        post = Path(post_path)
        post_excerpt = self._read_post_excerpt(post) if post.exists() else ""

        system_prompt = self.get_system_prompt()
        prompt = self._build_prompt(
            system_prompt=system_prompt,
            post_excerpt=post_excerpt,
            narration=narration_script or "",
            channel_name=channel_name,
        )

        parsed = self.gemini.call_json(prompt)
        meta = self._parse(parsed)
        if meta is None:
            self.log("Gemini returned no / invalid JSON, using fallback.")
            return YouTubeMetadata.from_fallback(
                title=fallback_title or post.stem,
                description=fallback_description or "",
                tags=fallback_tags or [],
                permalink=permalink,
                channel_name=channel_name,
            )

        # Resolve placeholders in description.
        chapter_block = self._build_chapter_block(
            meta.chapters,
            narration_duration_seconds=narration_duration_seconds,
            intro_seconds=intro_seconds,
        )
        permalink_line = self._build_permalink_line(permalink)
        meta.description = (
            meta.description
            .replace("__CHAPTERS__", chapter_block)
            .replace("__PERMALINK__", permalink_line)
        )

        # Final sanity limits: YouTube caps title @ 100, description @ 5000,
        # each tag @ 30 chars, total tags cumulative <= 500 chars.
        meta.title = meta.title[:95]
        meta.description = meta.description[:4800]
        meta.tags = _sanitize_tags(meta.tags)

        self.log(
            f"Metadata ready: {len(meta.title)}-char title, "
            f"{len(meta.description)}-char description, "
            f"{len(meta.tags)} tags, {len(meta.chapters)} chapters"
        )
        return meta

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    _FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)", re.DOTALL)
    _LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
    _URL_RE = re.compile(r"https?://\S+")

    def _read_post_excerpt(self, path: Path) -> str:
        """Return front-matter summary + first 2 body sections, stripped of URLs."""
        try:
            raw = path.read_text(encoding="utf-8")
        except Exception:
            return ""
        match = self._FRONT_MATTER_RE.match(raw)
        if not match:
            return raw[:2000]
        fm_text, body = match.group(1), match.group(2)
        # Pick the interesting fields from front matter.
        header_lines: list[str] = []
        for key in ("title", "description", "ai_opinion", "tags"):
            m = re.search(rf'^{key}:\s*"?(.*?)"?\s*$', fm_text, re.MULTILINE)
            if m:
                header_lines.append(f"{key}: {m.group(1).strip()}")
        # Drop reference sections and anything after them.
        for header in ("## 참고자료", "## References"):
            idx = body.find(header)
            if idx != -1:
                body = body[:idx]
        # Keep only the first 2 body sections.
        sections = re.split(r"\n(?=## )", body.strip())
        kept = "\n\n".join(sections[:3]).strip()
        kept = self._LINK_RE.sub(r"\1", kept)
        kept = self._URL_RE.sub("", kept)
        if len(kept) > 3000:
            kept = kept[:3000] + "\n..."
        return "\n".join(header_lines) + "\n\n" + kept

    def _build_prompt(
        self,
        *,
        system_prompt: str,
        post_excerpt: str,
        narration: str,
        channel_name: str,
    ) -> str:
        return f"""{system_prompt}

## 채널명
{channel_name}

## 블로그 포스트 발췌
{post_excerpt}

## 영상 나레이션 스크립트 (TTS 원문)
{narration}

위 입력을 바탕으로 JSON 객체 하나만 출력하세요.
"""

    def _parse(self, raw: object) -> Optional[YouTubeMetadata]:
        if not isinstance(raw, dict):
            return None
        title = (raw.get("title") or "").strip()
        description = (raw.get("description") or "").strip()
        tags = raw.get("tags") or []
        chapters_raw = raw.get("chapters") or []
        keywords = raw.get("keywords") or []

        if not title or not description:
            return None
        if not isinstance(tags, list) or not isinstance(chapters_raw, list):
            return None
        if not isinstance(keywords, list):
            keywords = []

        chapters: list[dict] = []
        for ch in chapters_raw:
            if not isinstance(ch, dict):
                continue
            label = (ch.get("label") or "").strip()
            section = (ch.get("section") or "").strip().lower()
            if not label:
                continue
            if section not in ("opening", "intro", "body", "closing"):
                section = "body"
            chapters.append({"label": label, "section": section})

        return YouTubeMetadata(
            title=title,
            description=description,
            tags=[str(t).strip() for t in tags if str(t).strip()],
            chapters=chapters,
            keywords=[str(k).strip() for k in keywords if str(k).strip()],
        )

    # ------------------------------------------------------------------
    # Chapter / permalink resolution
    # ------------------------------------------------------------------

    def _build_chapter_block(
        self,
        chapters: list[dict],
        *,
        narration_duration_seconds: float,
        intro_seconds: float,
    ) -> str:
        """Return multiline text:
            00:00 오프닝
            00:15 핵심 요약
            ...
        YouTube parses this and renders chapter markers automatically.
        First line MUST start at 00:00 and labels must be >= 10 chars apart.
        """
        if not chapters or narration_duration_seconds <= 0:
            # No chapters → nothing to render. Caller decides what to do.
            return ""

        # Give each chapter an equal slice of the narration portion.
        # Intro sits at 0:00; first chapter = intro, subsequent chapters
        # distributed across the narration body + outro.
        total_duration = intro_seconds + narration_duration_seconds
        count = len(chapters)
        # Chapter 0 is at 0:00 (intro / opening). The remaining count-1
        # chapters share the body duration equally.
        slice_len = (
            (narration_duration_seconds / max(1, count - 1)) if count > 1 else 0
        )

        lines: list[str] = []
        for i, ch in enumerate(chapters):
            if i == 0:
                t = 0.0
            else:
                # Start slightly after intro ends.
                t = intro_seconds + slice_len * (i - 1)
            # YouTube requires monotonically increasing timestamps >= 10s apart.
            if lines and t - _parse_timestamp_to_seconds(lines[-1]) < 10:
                t = _parse_timestamp_to_seconds(lines[-1]) + 10
            lines.append(f"{_format_timestamp(t)} {ch['label']}")

        return "\n".join(lines)

    @staticmethod
    def _build_permalink_line(permalink: str) -> str:
        if not permalink:
            return ""
        origin = "https://gipyeong-lee.github.io"
        if permalink.startswith("http"):
            return permalink
        return f"{origin}{permalink}"


# ----------------------------------------------------------------------
# SRT caption builder (standalone helper for video_pipeline + tests)
# ----------------------------------------------------------------------


def build_srt_captions(
    script: str,
    *,
    narration_duration_seconds: float,
    intro_offset_seconds: float = 3.0,
) -> str:
    """Return an SRT-format caption string synced to the narration.

    Reuses the same sentence-split heuristic as
    `scripts/local_video_compose.py::split_sentences` and distributes the
    narration duration evenly over the sentences. Each caption starts
    at `intro_offset_seconds` (the video intro pad) + its share of
    the narration window.

    Produces a standards-compliant SRT that YouTube accepts via
    `captions().insert()`.
    """
    sentences = _split_sentences(script)
    if not sentences or narration_duration_seconds <= 0:
        return ""

    per = narration_duration_seconds / len(sentences)
    blocks: list[str] = []
    for i, sentence in enumerate(sentences):
        start = intro_offset_seconds + i * per
        end = start + per
        blocks.append(
            f"{i + 1}\n"
            f"{_srt_timestamp(start)} --> {_srt_timestamp(end)}\n"
            f"{sentence}\n"
        )
    return "\n".join(blocks).strip() + "\n"


_SENTENCE_END_RE = re.compile(r"(?<=[.!?。！？])\s+|(?<=다\.)\s+|\n+")


def _split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return []
    parts = _SENTENCE_END_RE.split(text)
    out: list[str] = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if len(p) > 60:
            chunks = re.split(r",\s*", p)
            for c in chunks:
                c = c.strip()
                if c:
                    out.append(c)
        else:
            out.append(p)
    return out


def _srt_timestamp(seconds: float) -> str:
    if seconds < 0:
        seconds = 0.0
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    whole = int(secs)
    millis = int(round((secs - whole) * 1000))
    if millis == 1000:  # rounding edge
        millis = 0
        whole += 1
    return f"{hours:02d}:{minutes:02d}:{whole:02d},{millis:03d}"


def _format_timestamp(seconds: float) -> str:
    """MM:SS or HH:MM:SS (YouTube chapter convention)."""
    if seconds < 0:
        seconds = 0.0
    total = int(round(seconds))
    hours = total // 3600
    minutes = (total % 3600) // 60
    secs = total % 60
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def _parse_timestamp_to_seconds(line: str) -> float:
    """Inverse of _format_timestamp, used to enforce monotonic spacing."""
    m = re.match(r"^(\d{1,2}):(\d{2})(?::(\d{2}))?", line.strip())
    if not m:
        return 0.0
    if m.group(3):
        return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
    return int(m.group(1)) * 60 + int(m.group(2))


def _sanitize_tags(tags: list[str]) -> list[str]:
    """Trim, dedup case-insensitively, cap at 25 items × 30 chars each."""
    seen: set[str] = set()
    out: list[str] = []
    for t in tags:
        tt = t.strip().lstrip("#")
        if not tt:
            continue
        key = tt.lower()
        if key in seen:
            continue
        seen.add(key)
        if len(tt) > 30:
            tt = tt[:30]
        out.append(tt)
        if len(out) >= 25:
            break
    return out
