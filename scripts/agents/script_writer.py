"""Script Writer Agent — blog post → 1~2 min broadcast narration.

Reads a published post's front matter + body, extracts the parts that
matter for a news-anchor style segment, and asks Gemini CLI to collapse
it into a narration script suitable for TTS. The agent supports both
Korean (legacy briefing) and English (broadcast story-arc) modes.

The agent is a sibling of the blog pipeline agents (writer/editor/...),
but it operates on an already-published file instead of a ResearchBrief.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

from .base import BaseAgent


# Language → (system prompt file, target words/sec heuristic, opening fields,
# section header keywords for excerpt cleanup).
_LANG_CONFIG: dict[str, dict] = {
    "ko": {
        "prompt_file": "script_writer_system.md",
        "ref_headers": ("## 참고자료", "## 참고 자료", "## References"),
        "estimate_chars_per_sec": 4,  # Korean
    },
    "en": {
        "prompt_file": "script_writer_broadcast_en_system.md",
        "ref_headers": ("## References", "## Sources", "## 참고자료"),
        "estimate_chars_per_sec": 14,  # English ~150 wpm @ 5 chars/word
    },
}


class ScriptWriterAgent(BaseAgent):
    """Turn a published blog post into a news-anchor narration script."""

    name = "ScriptWriter"
    prompt_file = "script_writer_system.md"  # default; overridden per-language

    # We only need the first N body sections to keep prompt + Gemini latency low.
    BODY_SECTIONS_TO_KEEP = 2

    def run(
        self,
        post_path: str | Path,
        *,
        channel_name: str = "MindTickleBytes",
        target_duration_seconds: int = 90,
        language: str = "ko",
    ) -> Optional[str]:
        """Return plain narration text for the post at `post_path`, or None."""
        path = Path(post_path)
        if not path.exists():
            self.log(f"Post not found: {path}")
            return None

        lang = (language or "ko").lower()
        cfg = _LANG_CONFIG.get(lang, _LANG_CONFIG["ko"])
        # Override the BaseAgent prompt_file lookup just for this call.
        self.prompt_file = cfg["prompt_file"]

        raw = path.read_text(encoding="utf-8")
        meta, body = self._split_front_matter(raw)
        if not meta:
            self.log(f"Front matter not found in {path.name}")
            return None

        title = meta.get("title") or ""
        description = meta.get("description") or ""
        ai_opinion = meta.get("ai_opinion") or ""
        body_excerpt = self._extract_body_excerpt(body, ref_headers=cfg["ref_headers"])

        self.log(
            f"Composing {lang.upper()} script for: {title[:60]}"
        )

        system_prompt = self.get_system_prompt().replace("{channel_name}", channel_name)

        if lang == "en":
            prompt = self._build_en_prompt(
                system_prompt=system_prompt,
                channel_name=channel_name,
                target_duration_seconds=target_duration_seconds,
                title=title,
                description=description,
                ai_opinion=ai_opinion,
                body_excerpt=body_excerpt,
            )
        else:
            prompt = self._build_ko_prompt(
                system_prompt=system_prompt,
                channel_name=channel_name,
                target_duration_seconds=target_duration_seconds,
                title=title,
                description=description,
                ai_opinion=ai_opinion,
                body_excerpt=body_excerpt,
            )

        narration = self.gemini.call(prompt)
        if not narration:
            self.log("Gemini returned no script.")
            return None

        cleaned = self._clean(narration)
        min_chars = 200 if lang == "en" else 80
        if len(cleaned) < min_chars:
            self.log(f"Script too short ({len(cleaned)} chars, min {min_chars}). Rejecting.")
            return None

        self.log(
            f"Script: {len(cleaned)} chars, ~{self._estimate_seconds(cleaned, lang)}s narration"
        )
        return cleaned

    # ------------------------------------------------------------------
    # prompt builders (per language)
    # ------------------------------------------------------------------

    @staticmethod
    def _build_ko_prompt(
        *,
        system_prompt: str,
        channel_name: str,
        target_duration_seconds: int,
        title: str,
        description: str,
        ai_opinion: str,
        body_excerpt: str,
    ) -> str:
        return f"""{system_prompt}

## 채널명
{channel_name}

## 목표 낭독 시간
{target_duration_seconds}초 (250~400자)

## 포스트 제목
{title}

## 포스트 설명
{description}

## AI 의견
{ai_opinion}

## 본문 발췌 (앞부분)
{body_excerpt}

위 입력을 기반으로 뉴스 나레이션 스크립트를 작성하세요.
출력은 순수 텍스트 한 블록만, 마크다운이나 따옴표 없이.
"""

    @staticmethod
    def _build_en_prompt(
        *,
        system_prompt: str,
        channel_name: str,
        target_duration_seconds: int,
        title: str,
        description: str,
        ai_opinion: str,
        body_excerpt: str,
    ) -> str:
        return f"""{system_prompt}

## Channel name
{channel_name}

## Target spoken duration
{target_duration_seconds} seconds (about 220-290 words)

## Post title
{title}

## Post description
{description}

## Author commentary
{ai_opinion}

## Post excerpt (first sections)
{body_excerpt}

Write the broadcast narration only. Plain text. No markdown, no quotes,
no headings, no stage directions. Channel name appears exactly twice.
"""

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------

    _FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)", re.DOTALL)

    def _split_front_matter(self, raw: str) -> tuple[dict[str, str], str]:
        match = self._FRONT_MATTER_RE.match(raw)
        if not match:
            return {}, raw
        fm_text, body = match.group(1), match.group(2)
        meta: dict[str, str] = {}
        # Simple key: "value" parser — covers our post format.
        for line in fm_text.splitlines():
            kv = re.match(r'^([a-zA-Z_][\w-]*)\s*:\s*(.*)$', line)
            if not kv:
                continue
            key, val = kv.group(1), kv.group(2).strip()
            # Strip surrounding quotes.
            if (val.startswith('"') and val.endswith('"')) or (
                val.startswith("'") and val.endswith("'")
            ):
                val = val[1:-1]
            meta[key] = val
        return meta, body

    def _extract_body_excerpt(
        self, body: str, *, ref_headers: tuple[str, ...] = ("## 참고자료", "## References")
    ) -> str:
        """Keep only the first few `##` sections; strip reference sections."""
        # Drop everything from the references section onward.
        for header in ref_headers:
            idx = body.find(header)
            if idx != -1:
                body = body[:idx]

        # Split into sections by `## ` headers. Keep the intro + first N sections.
        sections = re.split(r"\n(?=## )", body.strip())
        kept = sections[: self.BODY_SECTIONS_TO_KEEP + 1]  # +1 for pre-`##` intro
        excerpt = "\n\n".join(kept).strip()

        # Strip inline source links: [title](url) → title
        excerpt = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", excerpt)
        # Strip naked URLs
        excerpt = re.sub(r"https?://\S+", "", excerpt)
        # Collapse repeated whitespace.
        excerpt = re.sub(r"\n{3,}", "\n\n", excerpt)
        # Hard cap to keep prompt bounded.
        if len(excerpt) > 3500:
            excerpt = excerpt[:3500] + "\n..."
        return excerpt

    def _clean(self, text: str) -> str:
        """Strip markdown fences, quote wrappers, stray headers."""
        text = text.strip()
        # Fenced code blocks
        if text.startswith("```"):
            text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
            text = re.sub(r"\n?```$", "", text)
        # Surrounding quotes
        if len(text) >= 2 and text[0] == text[-1] and text[0] in ('"', "'"):
            text = text[1:-1]
        # Any leading header that the model might have inserted despite rules
        text = re.sub(r"^#+\s.*\n?", "", text)
        # Collapse excessive whitespace but preserve sentence breaks.
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{2,}", "\n", text)
        return text.strip()

    @staticmethod
    def _estimate_seconds(text: str, language: str = "ko") -> int:
        """Rough heuristic per language for anchor pace."""
        chars = len(re.sub(r"\s+", "", text))
        per_sec = _LANG_CONFIG.get(language, _LANG_CONFIG["ko"])["estimate_chars_per_sec"]
        return max(1, chars // per_sec)
