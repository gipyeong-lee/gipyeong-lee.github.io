"""Script Writer Agent — Korean blog post → 1~2 min narration script.

Reads a published Korean post's front matter + body, extracts the parts
that matter for a news-anchor style summary, and asks Gemini CLI to
collapse it into a narration script suitable for TTS.

The agent is a sibling of the blog pipeline agents (writer/editor/...),
but it operates on an already-published file instead of a ResearchBrief.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

from .base import BaseAgent


class ScriptWriterAgent(BaseAgent):
    """Turn a Korean blog post into a news-briefing narration script."""

    name = "ScriptWriter"
    prompt_file = "script_writer_system.md"

    # We only need the first N body sections to keep prompt + Gemini latency low.
    BODY_SECTIONS_TO_KEEP = 2

    def run(
        self,
        post_path: str | Path,
        *,
        channel_name: str = "Antigravity News",
        target_duration_seconds: int = 90,
    ) -> Optional[str]:
        """Return plain narration text for the post at `post_path`, or None."""
        path = Path(post_path)
        if not path.exists():
            self.log(f"Post not found: {path}")
            return None

        raw = path.read_text(encoding="utf-8")
        meta, body = self._split_front_matter(raw)
        if not meta:
            self.log(f"Front matter not found in {path.name}")
            return None

        title = meta.get("title") or ""
        description = meta.get("description") or ""
        ai_opinion = meta.get("ai_opinion") or ""
        body_excerpt = self._extract_body_excerpt(body)

        self.log(f"Composing script for: {title[:60]}")

        system_prompt = self.get_system_prompt().replace("{channel_name}", channel_name)

        prompt = f"""{system_prompt}

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

        narration = self.gemini.call(prompt)
        if not narration:
            self.log("Gemini returned no script.")
            return None

        cleaned = self._clean(narration)
        if len(cleaned) < 80:
            self.log(f"Script too short ({len(cleaned)} chars). Rejecting.")
            return None

        self.log(f"Script: {len(cleaned)} chars, ~{self._estimate_seconds(cleaned)}s narration")
        return cleaned

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

    def _extract_body_excerpt(self, body: str) -> str:
        """Keep only the first few `##` sections; strip reference sections."""
        # Drop everything from the references section onward (Korean + fallbacks).
        for header in ("## 참고자료", "## 참고 자료", "## References"):
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
    def _estimate_seconds(text: str) -> int:
        """Very rough heuristic: ~4 Korean chars/sec for anchor pace."""
        chars = len(re.sub(r"\s+", "", text))
        return max(1, chars // 4)
