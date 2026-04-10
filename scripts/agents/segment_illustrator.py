"""Segment Illustrator — Steve Jobs keynote-style slides.

Design philosophy: every slide should look like it came from an Apple
keynote. The rules are extreme minimalism:

- **ONE idea per slide** (3-5 words max, or a single number)
- **190pt titles** on gradient black background
- **30%+ negative space** — most of the slide is empty
- **No bullet points ever** — single statements only
- **Maximum 2 visual elements per slide** (text + accent, or image + label)
- **White text (#FFFFFF) on dark gradient** for maximum contrast
- **Center everything** horizontally and vertically

Slide types mirror actual Jobs keynote patterns:
- "hero_number": One massive number + tiny label ("3 billion")
- "hero_word": One word or phrase filling the screen ("Revolutionary.")
- "statement": Short declarative sentence centered
- "versus": Two items contrasted left/right
- "reveal": Question or mystery → answer below (two-line)

Output: 1920x1080 JPEG slides rendered via Pillow. No SDXL.
"""
from __future__ import annotations

import json
import math
import os
import re
from pathlib import Path
from typing import Optional

from .base import BaseAgent

WIDTH = 1920
HEIGHT = 1080

# Apple keynote gradient: charcoal top → near-black bottom.
BG_TOP = (55, 55, 62)
BG_BOTTOM = (18, 18, 24)

# Color palette — minimal like Apple.
WHITE = (255, 255, 255)
DIM = (130, 130, 140)
ACCENT_BLUE = (0, 122, 255)    # Apple blue
ACCENT_GREEN = (48, 209, 88)   # Apple green
ACCENT_GOLD = (255, 214, 10)   # Apple gold


class SegmentIllustratorAgent(BaseAgent):
    """Generate Apple keynote-style info slides for newscast segments."""

    name = "SegmentIllustrator"
    prompt_file = ""

    def run(
        self,
        *,
        topic_title: str,
        topic_description: str,
        script_excerpt: str,
        output_dir: str | Path,
        slug_prefix: str,
        num_images: int = 5,
        timeout_per_image: int = 120,
    ) -> list[str]:
        out_dir = Path(output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        cached = self._find_cached(out_dir, slug_prefix, num_images)
        if len(cached) >= num_images:
            self.log(f"{slug_prefix}: {len(cached)} cached slides")
            return cached

        slides = self._design_slides(
            topic_title, topic_description, script_excerpt, num_images
        )
        if not slides:
            self.log(f"{slug_prefix}: no slide designs from Gemini")
            return cached

        self.log(f"{slug_prefix}: rendering {len(slides)} keynote slides")
        results: list[str] = list(cached)
        for k, data in enumerate(slides):
            if len(results) >= num_images:
                break
            out_path = out_dir / f"{slug_prefix}.slide{k}.jpg"
            if out_path.exists() and out_path.stat().st_size > 5000:
                results.append(str(out_path))
                continue
            ok = self._render_slide(data, str(out_path))
            if ok:
                results.append(str(out_path))

        self.log(f"{slug_prefix}: {len(results)} slides ready")
        return results

    def _find_cached(self, out_dir: Path, prefix: str, n: int) -> list[str]:
        found = []
        for k in range(n + 2):
            for suffix in ("slide", "vis"):
                p = out_dir / f"{prefix}.{suffix}{k}.jpg"
                if p.exists() and p.stat().st_size > 5000:
                    found.append(str(p))
                    break
        return found[:n]

    def _design_slides(self, title, desc, excerpt, n) -> list[dict]:
        prompt = f"""You are designing {n} slides for an Apple-style keynote presentation segment.
These slides will appear behind a news anchor's narration about this topic.
Follow Steve Jobs' keynote design rules EXACTLY.

Topic: {title}
Description: {desc}
Content: {(excerpt or '')[:2000]}

SLIDE DESIGN RULES (STRICT — violating these makes the slide look amateur):
1. MAXIMUM 5 WORDS per slide. Not 6. Not 7. Five or fewer.
2. Each slide has ONE of these layouts:
   - "hero_number": A single large number + tiny label below (e.g., "1M" + "tokens")
   - "hero_word": One powerful word or phrase (e.g., "Revolutionary." or "Think Different.")
   - "statement": A short declarative (max 5 words, e.g., "AI that writes code.")
   - "versus": Two items being compared (e.g., "Before" / "After" or "GPT-4" / "GPT-5")
   - "reveal": A question on top, answer below (2 lines only)
3. NO bullet points. NO lists. NO paragraphs. ONE idea.
4. Every slide must give a SPECIFIC insight from the topic content.
   Do NOT use vague words like "Innovation" or "The Future" alone.
   Use CONCRETE facts: numbers, names, comparisons from the content.
5. Alternate between layouts — don't use the same type twice in a row.

Return ONLY a JSON array. Each object has:
- "layout": one of "hero_number", "hero_word", "statement", "versus", "reveal"
- "line1": primary text (THE BIG TEXT, max 5 words)
- "line2": secondary text (small label, max 8 words, or empty)
- "accent": "blue", "green", "gold", or "white" (for the primary text color)

Example output:
[
  {{"layout":"hero_number","line1":"1,000,000","line2":"tokens in one context","accent":"blue"}},
  {{"layout":"statement","line1":"Code that writes itself.","line2":"","accent":"white"}},
  {{"layout":"versus","line1":"Before: 8K tokens","line2":"After: 1M tokens","accent":"gold"}},
  {{"layout":"hero_word","line1":"Autonomous.","line2":"","accent":"green"}},
  {{"layout":"reveal","line1":"How fast?","line2":"10x faster than GPT-4.","accent":"blue"}}
]

Return ONLY the JSON array. No explanation."""

        raw = self.gemini.call(prompt)
        if not raw:
            return []
        try:
            cleaned = raw.strip()
            if cleaned.startswith("```"):
                cleaned = re.sub(r"^```[a-zA-Z]*\n?", "", cleaned)
                cleaned = re.sub(r"\n?```$", "", cleaned)
            parsed = json.loads(cleaned)
            if isinstance(parsed, list):
                return parsed[:n]
        except (json.JSONDecodeError, ValueError):
            self.log("Gemini returned invalid JSON")
        return []

    def _render_slide(self, data: dict, output_path: str) -> bool:
        try:
            from PIL import Image, ImageDraw, ImageFont
        except ImportError:
            return False

        layout = data.get("layout", "statement")
        line1 = str(data.get("line1", ""))[:60]
        line2 = str(data.get("line2", ""))[:80]
        accent = data.get("accent", "white")

        accent_color = {
            "blue": ACCENT_BLUE,
            "green": ACCENT_GREEN,
            "gold": ACCENT_GOLD,
            "white": WHITE,
        }.get(accent, WHITE)

        # Create gradient background.
        img = self._gradient_bg()
        draw = ImageDraw.Draw(img)

        font_path = self._pick_font()
        try:
            f_hero = ImageFont.truetype(font_path, 160) if font_path else ImageFont.load_default()
            f_big = ImageFont.truetype(font_path, 120) if font_path else ImageFont.load_default()
            f_med = ImageFont.truetype(font_path, 72) if font_path else ImageFont.load_default()
            f_label = ImageFont.truetype(font_path, 36) if font_path else ImageFont.load_default()
            f_small = ImageFont.truetype(font_path, 28) if font_path else ImageFont.load_default()
        except Exception:
            f_hero = f_big = f_med = f_label = f_small = ImageFont.load_default()

        if layout == "hero_number":
            self._draw_hero_number(draw, line1, line2, accent_color, f_hero, f_label)
        elif layout == "hero_word":
            self._draw_hero_word(draw, line1, accent_color, f_hero)
        elif layout == "versus":
            self._draw_versus(draw, line1, line2, accent_color, f_big, f_med)
        elif layout == "reveal":
            self._draw_reveal(draw, line1, line2, accent_color, f_med, f_big)
        else:  # statement
            self._draw_statement(draw, line1, line2, accent_color, f_big, f_label)

        # Subtle branding — bottom left, very small, very dim.
        draw.text((60, HEIGHT - 50), "MindTickleBytes", fill=(60, 60, 68), font=f_small)

        try:
            os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
            img.save(output_path, "JPEG", quality=95)
            return True
        except Exception:
            return False

    # ------------------------------------------------------------------
    # Layout renderers — Jobs keynote style
    # ------------------------------------------------------------------

    def _draw_hero_number(self, draw, number, label, color, f_hero, f_label):
        """One massive number centered. Tiny label below."""
        self._center_text(draw, number, f_hero, color, y_offset=-40)
        if label:
            self._center_text(draw, label, f_label, DIM, y_offset=100)

    def _draw_hero_word(self, draw, word, color, f_hero):
        """One word or short phrase filling the screen."""
        self._center_text(draw, word, f_hero, color, y_offset=0)

    def _draw_statement(self, draw, statement, sub, color, f_big, f_label):
        """Short declarative sentence centered."""
        self._center_text(draw, statement, f_big, color, y_offset=-30)
        if sub:
            self._center_text(draw, sub, f_label, DIM, y_offset=80)

    def _draw_versus(self, draw, left_text, right_text, color, f_big, f_med):
        """Two items contrasted with a divider line."""
        # Left item.
        left = left_text.replace("Before: ", "").replace("Before:", "").strip()
        right = right_text.replace("After: ", "").replace("After:", "").strip()

        # Dim left, bright right — "before → after" visual hierarchy.
        lx = WIDTH // 4
        rx = WIDTH * 3 // 4
        cy = HEIGHT // 2

        self._center_text_at(draw, left, f_med, DIM, lx, cy - 10)
        self._center_text_at(draw, right, f_big, color, rx, cy - 10)

        # Subtle divider line.
        mid = WIDTH // 2
        draw.line([(mid, cy - 80), (mid, cy + 80)], fill=(50, 50, 58), width=2)

    def _draw_reveal(self, draw, question, answer, color, f_med, f_big):
        """Question on top (dim), answer below (bright, large)."""
        self._center_text(draw, question, f_med, DIM, y_offset=-80)
        self._center_text(draw, answer, f_big, color, y_offset=60)

    # ------------------------------------------------------------------
    # Rendering helpers
    # ------------------------------------------------------------------

    def _gradient_bg(self) -> "Image.Image":
        """Apple-style vertical gradient: charcoal → near-black."""
        from PIL import Image
        import numpy as np

        arr = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
        for y in range(HEIGHT):
            ratio = y / HEIGHT
            r = int(BG_TOP[0] + (BG_BOTTOM[0] - BG_TOP[0]) * ratio)
            g = int(BG_TOP[1] + (BG_BOTTOM[1] - BG_TOP[1]) * ratio)
            b = int(BG_TOP[2] + (BG_BOTTOM[2] - BG_TOP[2]) * ratio)
            arr[y, :] = (r, g, b)
        return Image.fromarray(arr)

    def _center_text(self, draw, text, font, color, y_offset=0):
        """Center text both horizontally and vertically on the slide."""
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        x = (WIDTH - tw) // 2
        y = (HEIGHT - th) // 2 + y_offset
        draw.text((x, y), text, fill=color, font=font)

    def _center_text_at(self, draw, text, font, color, cx, cy):
        """Center text at a specific point."""
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((cx - tw // 2, cy - th // 2), text, fill=color, font=font)

    @staticmethod
    def _pick_font() -> str:
        for c in [
            "/System/Library/Fonts/AppleSDGothicNeo.ttc",
            "/Library/Fonts/AppleSDGothicNeo.ttc",
            "/System/Library/Fonts/Supplemental/NotoSansKR-Regular.otf",
            "/System/Library/Fonts/PingFang.ttc",
        ]:
            if os.path.exists(c):
                return c
        return ""
