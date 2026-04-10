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

# Newscast (multi-topic, ~50min) uses a separate, much beefier prompt.
_NEWSCAST_PROMPT_FILE_EN = "script_writer_newscast_en_system.md"

# Marker the newscast script emits between every structural section.
# The composer parses on it to switch hero images per segment, and
# the captioner uses it to anchor chapter timestamps.
SEGMENT_BREAK_MARKER = "--- SEGMENT BREAK ---"


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

    # ------------------------------------------------------------------
    # Newscast (multi-topic, ~50 min) mode
    # ------------------------------------------------------------------

    def run_newscast(
        self,
        post_paths: list[str | Path],
        *,
        channel_name: str = "MindTickleBytes",
        anchor_name: str = "Alex Rivera",
        target_duration_seconds: int = 50 * 60,
        episode_date: str = "",
        language: str = "en",
    ) -> Optional[str]:
        """Weave N posts into a single ~50 min broadcast newscast script.

        Builds the script with **chunked Gemini calls** — one per section
        of the spine — instead of a single mega-prompt. Empirically a
        single Gemini call caps around 2.5–3k spoken words; a chunked
        run reliably hits 7–8k words (the full 50 min target) without
        any individual call running out of capacity.

        Returns the concatenated narration text with
        ``--- SEGMENT BREAK ---`` markers between sections, or None on
        catastrophic failure (no topics, all chunks empty).
        """
        if not post_paths:
            self.log("run_newscast: no post paths provided")
            return None

        topics: list[dict] = []
        for p in post_paths:
            path = Path(p)
            if not path.exists():
                self.log(f"newscast: skipping missing post {path.name}")
                continue
            raw = path.read_text(encoding="utf-8")
            meta, body = self._split_front_matter(raw)
            if not meta:
                self.log(f"newscast: no front matter in {path.name}")
                continue
            ref_headers = _LANG_CONFIG.get(
                language, _LANG_CONFIG["en"]
            )["ref_headers"]
            excerpt = self._extract_body_excerpt(body, ref_headers=ref_headers)
            topics.append(
                {
                    "slug": path.stem,
                    "title": (meta.get("title") or path.stem).strip(),
                    "description": (meta.get("description") or "").strip(),
                    "ai_opinion": (meta.get("ai_opinion") or "").strip(),
                    "excerpt": excerpt,
                }
            )

        if not topics:
            self.log("newscast: no usable topics after filtering")
            return None

        self.log(
            f"Composing newscast (chunked): {len(topics)} topics, "
            f"~{target_duration_seconds // 60}min target"
        )

        # Load the heavy newscast prompt as the per-section system prompt.
        self.prompt_file = _NEWSCAST_PROMPT_FILE_EN
        system_prompt = self.get_system_prompt()

        # Per-section word budgets distribute the 7500-word target so
        # the sum lands close to the 50-min spoken time. The midpoint
        # is short, segments do most of the heavy lifting.
        n = len(topics)
        # Default 7500 words for 50 min @ 150 wpm.
        total_words = max(2000, int(target_duration_seconds * 150 / 60))
        cold_open_words = 60
        intro_words = 130
        midpoint_words = 180
        closing_words = 240
        signoff_words = 40
        used = (
            cold_open_words + intro_words + midpoint_words
            + closing_words + signoff_words
        )
        # 2-5 min per segment. 150 wpm → 300-750 words. We target the
        # upper end so the script writer has room, then let the prompt's
        # "expand with analogies if thin" directive fill any gaps.
        per_segment_words = max(450, min(750, (total_words - used) // max(1, n)))

        # Pre-compute the 1-line theme. We feed it back into every
        # segment prompt so the bridges and anchor lead-ins all hook
        # into the same editorial throughline.
        theme = self._generate_episode_theme(
            system_prompt=system_prompt,
            topics=topics,
            channel_name=channel_name,
        )
        if theme:
            self.log(f"theme: {theme[:80]}")

        sections: list[str] = []

        # 1. COLD OPEN
        cold = self._generate_section(
            system_prompt=system_prompt,
            section_name="cold_open",
            section_brief=(
                f"Write the COLD OPEN — {cold_open_words} words. One or two "
                "punchy sentences that hook the viewer with the most arresting "
                "beat from the topic stack. Do NOT greet the viewer yet. The "
                f"channel name {channel_name!r} appears exactly once at the "
                "very end of the cold open."
            ),
            channel_name=channel_name,
            anchor_name=anchor_name,
            theme=theme,
            topics=topics,
            extra_context="",
        )
        if cold:
            sections.append(cold)

        # 2. ANCHOR INTRO
        intro = self._generate_section(
            system_prompt=system_prompt,
            section_name="anchor_intro",
            section_brief=(
                f"Write the ANCHOR INTRODUCTION — {intro_words} words. Open "
                f"with 'Good evening. I'm {anchor_name}, and this is "
                f"{channel_name}.' (this is the second time the channel name "
                "appears in the episode — DO NOT use it elsewhere). Then state "
                "tonight's episode theme in one sentence and tease 2-3 of the "
                "upcoming stories by name."
            ),
            channel_name=channel_name,
            anchor_name=anchor_name,
            theme=theme,
            topics=topics,
            extra_context="",
        )
        if intro:
            sections.append(intro)

        # 3. SEGMENTS — one per topic
        for i, topic in enumerate(topics):
            position = "OPENING SEGMENT" if i == 0 else (
                "CLOSING SEGMENT" if i == n - 1 else "MIDDLE SEGMENT"
            )
            # Gauge content depth: short excerpts get a "expand" nudge.
            content_len = len(topic.get("excerpt", "")) + len(topic.get("description", ""))
            depth_note = ""
            if content_len < 800:
                depth_note = (
                    " The source material for this topic is SHORT. Compensate "
                    "by explaining the underlying concept from scratch using "
                    "analogies, real-world scenarios, and 'what this means for "
                    "a normal person' framing. Do NOT pad with filler — teach."
                )
            seg = self._generate_section(
                system_prompt=system_prompt,
                section_name=f"segment_{i + 1}",
                section_brief=(
                    f"Write SEGMENT {i + 1} of {n} ({position}) — "
                    f"{per_segment_words} words (2-5 min spoken). Cover ONLY "
                    "the topic below. Follow the segment arc: anchor lead-in "
                    "(tie to theme) → 'what you need to know' with analogy → "
                    "development → 'what this means for you' → reality check → "
                    "bridge. Do NOT mention the channel name. Cover ONLY this "
                    f"topic.{depth_note}"
                ),
                channel_name=channel_name,
                anchor_name=anchor_name,
                theme=theme,
                topics=[topic],
                extra_context=(
                    f"Position in episode: {position} (segment {i + 1} of {n}).\n"
                    f"Next topic in the lineup: "
                    f"{topics[i + 1]['title'] if i + 1 < n else 'closing commentary'}"
                ),
            )
            if seg:
                sections.append(seg)
            # Insert the midpoint AFTER the middle segment.
            if n >= 3 and i == n // 2:
                mid = self._generate_section(
                    system_prompt=system_prompt,
                    section_name="midpoint",
                    section_brief=(
                        f"Write the MIDPOINT 'AT THE HALFWAY MARK' beat — "
                        f"{midpoint_words} words. The anchor steps back, "
                        "synthesizes how the first half of the episode fits "
                        "tonight's theme in one or two sentences, then teases "
                        "the back half. Do NOT recap the theme verbatim. Do "
                        "NOT mention the channel name."
                    ),
                    channel_name=channel_name,
                    anchor_name=anchor_name,
                    theme=theme,
                    topics=topics,
                    extra_context="",
                )
                if mid:
                    sections.append(mid)

        # 4. CLOSING — "the bigger picture"
        closing = self._generate_section(
            system_prompt=system_prompt,
            section_name="closing",
            section_brief=(
                f"Write the CLOSING 'BIGGER PICTURE' commentary — "
                f"{closing_words} words. Name the through-line that connects "
                "every segment, then give one specific falsifiable prediction "
                "or watchpoint for the coming week. Sober broadcast tone — no "
                "cheerleading, no doomerism. Do NOT mention the channel name."
            ),
            channel_name=channel_name,
            anchor_name=anchor_name,
            theme=theme,
            topics=topics,
            extra_context="",
        )
        if closing:
            sections.append(closing)

        # 5. SIGN-OFF
        signoff = self._generate_section(
            system_prompt=system_prompt,
            section_name="signoff",
            section_brief=(
                f"Write the SIGN-OFF — {signoff_words} words. Exactly: "
                f"'I'm {anchor_name}. Stay curious. Goodnight.' followed by "
                f"the channel name {channel_name!r} ONCE (this is the third "
                "and FINAL time the channel name appears in the episode)."
            ),
            channel_name=channel_name,
            anchor_name=anchor_name,
            theme=theme,
            topics=topics,
            extra_context="",
        )
        if signoff:
            sections.append(signoff)

        if not sections:
            self.log("newscast: every chunked section returned empty")
            return None

        full = ("\n" + SEGMENT_BREAK_MARKER + "\n").join(sections)
        cleaned = self._clean_newscast(full)

        # Soft floor: a chunked 50-min episode should be 25k+ chars.
        # Anything tinier means most chunks failed silently — reject so
        # we don't waste 50 min of TTS on a 5-minute script.
        min_chars = max(8000, int(target_duration_seconds * 8))
        if len(cleaned) < min_chars:
            self.log(
                f"newscast: script too short ({len(cleaned)} chars, "
                f"need {min_chars}+). Rejecting."
            )
            return None

        marker_count = cleaned.count(SEGMENT_BREAK_MARKER)
        self.log(
            f"Newscast script: {len(cleaned)} chars in {marker_count + 1} "
            f"sections, ~{self._estimate_seconds(cleaned, language) // 60}"
            "min narration"
        )
        return cleaned

    def _generate_episode_theme(
        self,
        *,
        system_prompt: str,
        topics: list[dict],
        channel_name: str,
    ) -> str:
        """Ask Gemini for a one-sentence editorial theme tying topics together."""
        topic_titles = "\n".join(
            f"- {t['title']}: {t.get('description', '')[:120]}"
            for t in topics
        )
        prompt = f"""You are the editorial director for {channel_name}, an
AI-and-tech evening news magazine. Read the topic list below and write
ONE editorial theme sentence (no more than 20 words) that ties them
together as tonight's episode through-line. Be specific and grounded —
no platitudes like "the rapid pace of AI". Output the sentence only,
plain text, no quotes, no markdown.

## Tonight's topics
{topic_titles}
"""
        out = self.gemini.call(prompt)
        if not out:
            return ""
        line = out.strip().splitlines()[0].strip()
        # Strip outer quotes / markdown if any.
        line = re.sub(r'^["\'`]+|["\'`]+$', "", line).strip()
        return line[:200]

    def _generate_section(
        self,
        *,
        system_prompt: str,
        section_name: str,
        section_brief: str,
        channel_name: str,
        anchor_name: str,
        theme: str,
        topics: list[dict],
        extra_context: str,
    ) -> str:
        """Generate one section via a focused Gemini call."""
        topic_blocks = self._format_topics_for_newscast(topics)
        prompt = f"""{system_prompt}

You are writing only ONE section of the broadcast spine for tonight's
episode. The other sections are written separately and concatenated.

## Section to write
{section_name}

## Channel name
{channel_name}

## Anchor name
{anchor_name}

## Episode theme (must be the through-line)
{theme}

## Brief
{section_brief}

{extra_context}

## Source material for this section
{topic_blocks}

Write ONLY this section's prose. Plain text. No headers, no markdown,
no quotes, no stage directions, no segment break markers — those are
inserted by the orchestrator between sections. Begin immediately with
the first sentence of the section.
"""
        out = self.gemini.call(prompt)
        if not out:
            self.log(f"section {section_name}: empty Gemini response")
            return ""
        cleaned = self._clean_section_chunk(out)
        if len(cleaned) < 80:
            self.log(
                f"section {section_name}: too short ({len(cleaned)} chars)"
            )
            return ""
        self.log(f"section {section_name}: {len(cleaned)} chars")
        return cleaned

    @staticmethod
    def _clean_section_chunk(text: str) -> str:
        """Strip code fences / markdown headers / segment markers from a chunk."""
        text = (text or "").strip()
        if text.startswith("```"):
            text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
            text = re.sub(r"\n?```$", "", text)
        if len(text) >= 2 and text[0] == text[-1] and text[0] in ('"', "'"):
            text = text[1:-1]
        # Remove any segment markers the model emitted (orchestrator inserts).
        text = text.replace(SEGMENT_BREAK_MARKER, "")
        # Remove markdown headers but keep their text content.
        text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
        # Remove leading bullets.
        text = re.sub(r"^[\-\*•]\s+", "", text, flags=re.MULTILINE)
        # Collapse whitespace.
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()

    def _format_topics_for_newscast(self, topics: list[dict]) -> str:
        """Format topic dicts as a numbered list for the Gemini prompt."""
        out: list[str] = []
        for i, t in enumerate(topics, 1):
            block = (
                f"### Topic {i}: {t['title']}\n"
                f"slug: {t['slug']}\n"
                f"description: {t['description']}\n"
            )
            if t["ai_opinion"]:
                block += f"author commentary: {t['ai_opinion']}\n"
            if t["excerpt"]:
                # Truncate per-topic excerpt so the full prompt stays
                # bounded across 8 topics × ~2k chars = ~16k char prompt.
                excerpt = t["excerpt"][:1800]
                block += f"excerpt:\n{excerpt}\n"
            out.append(block)
        return "\n".join(out)

    def _clean_newscast(self, text: str) -> str:
        """Like `_clean` but preserves the SEGMENT BREAK marker layout.

        The default `_clean` collapses every `\\n{2,}` to a single newline,
        which would mash all the segment markers together. The newscast
        composer needs the markers to remain on their own lines so it
        can split on them cleanly.
        """
        text = text.strip()
        # Strip any code fence wrapping the whole thing.
        if text.startswith("```"):
            text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
            text = re.sub(r"\n?```$", "", text)
        # Strip outer quotation wrapper if Gemini added one.
        if len(text) >= 2 and text[0] == text[-1] and text[0] in ('"', "'"):
            text = text[1:-1]
        # Strip stray markdown headers but never the segment marker line.
        cleaned_lines: list[str] = []
        for line in text.splitlines():
            stripped = line.strip()
            if stripped == SEGMENT_BREAK_MARKER:
                cleaned_lines.append(SEGMENT_BREAK_MARKER)
                continue
            # Drop "##" / "###" markdown headers (the model sometimes
            # echoes the spine names) but keep their text content.
            stripped = re.sub(r"^#{1,6}\s*", "", stripped)
            # Strip any inline emoji / list bullets.
            stripped = re.sub(r"^[\-\*•]\s+", "", stripped)
            cleaned_lines.append(stripped)
        text = "\n".join(cleaned_lines).strip()
        # Collapse runs of blank lines to a single blank, but keep the
        # marker on its own paragraph by re-anchoring on it.
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text
