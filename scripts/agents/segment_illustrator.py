"""Segment Illustrator — generates presentation-style slides per topic.

Instead of AI-generated "mood photos" (SDXL-Turbo), this agent creates
**presentation slides** (Pillow-rendered) that contain:
- Key phrases and numbers from the topic
- Bullet points, comparisons, diagrams (text-based)
- Title + subtitle layout matching broadcast news graphics

The agent asks Gemini to design the slide content (what text, what layout),
then renders each slide at 1920x1080 via Pillow. This produces images that
**actually explain the content** rather than showing decorative visuals.

Output: list of .jpg paths at `videos/<slug>.seg<N>.slide<K>.jpg`.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Optional

from .base import BaseAgent

# Slide dimensions matching the video canvas.
WIDTH = 1920
HEIGHT = 1080

# Color palette for slides (dark broadcast style).
BG_COLOR = (14, 18, 30)          # near-black blue
ACCENT_COLOR = (0, 160, 255)     # bright blue accent
TEXT_COLOR = (240, 245, 255)     # near-white
DIM_COLOR = (140, 155, 180)      # dim text
HIGHLIGHT_BG = (25, 40, 70)      # card background
BADGE_COLOR = (0, 200, 130)      # green for positive
WARN_COLOR = (255, 180, 40)      # amber for caution


class SegmentIllustratorAgent(BaseAgent):
    """Generate presentation-style info slides for each newscast segment."""

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
        num_images: int = 4,
        timeout_per_image: int = 120,
    ) -> list[str]:
        """Generate presentation slides for one topic segment.

        Returns list of .jpg paths (may be fewer than `num_images` on
        partial failure, or empty on total failure).
        """
        out_dir = Path(output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        # Check cache.
        cached = self._find_cached(out_dir, slug_prefix, num_images)
        if len(cached) >= num_images:
            self.log(f"{slug_prefix}: {len(cached)} cached slides, skipping")
            return cached

        # Ask Gemini for slide content designs.
        slides = self._design_slides(
            topic_title, topic_description, script_excerpt, num_images
        )
        if not slides:
            self.log(f"{slug_prefix}: Gemini returned no slide designs")
            return cached

        self.log(f"{slug_prefix}: rendering {len(slides)} info slides")

        results: list[str] = list(cached)
        for k, slide_data in enumerate(slides):
            if len(results) >= num_images:
                break
            out_path = out_dir / f"{slug_prefix}.slide{k}.jpg"
            if out_path.exists() and out_path.stat().st_size > 5000:
                results.append(str(out_path))
                continue
            ok = self._render_slide(slide_data, str(out_path), topic_title)
            if ok:
                results.append(str(out_path))

        self.log(f"{slug_prefix}: {len(results)} slides ready")
        return results

    def _find_cached(self, out_dir: Path, prefix: str, n: int) -> list[str]:
        found = []
        for k in range(n + 2):
            for suffix in ("slide", "vis"):  # backward compat with old names
                path = out_dir / f"{prefix}.{suffix}{k}.jpg"
                if path.exists() and path.stat().st_size > 5000:
                    found.append(str(path))
                    break
        return found[:n]

    def _design_slides(
        self,
        title: str,
        description: str,
        excerpt: str,
        n: int,
    ) -> list[dict]:
        """Ask Gemini for N slide content layouts."""
        prompt = f"""You are designing {n} presentation slides for a TV news segment about this topic.
These slides will be shown BEHIND the anchor's narration to help viewers UNDERSTAND the content.
Each slide should teach ONE key idea from the topic.

Topic: {title}
Description: {description}
Content excerpt: {(excerpt or '')[:2000]}

For each slide, return a JSON object with these fields:
- "layout": one of "title_stats", "bullet_list", "comparison", "key_quote", "big_number"
- "heading": main text (max 40 chars, English)
- "subheading": secondary text (max 60 chars, optional)
- "items": list of strings (for bullet_list: 3-5 bullets; for comparison: pairs; for key_quote: 1 quote)
- "highlight_number": a key number/stat to display big (for big_number and title_stats layouts)
- "highlight_label": label for the number (max 30 chars)
- "footer": small text at bottom (source attribution or context, max 50 chars)

RULES:
- Each slide must teach something DIFFERENT about the topic
- Use concrete numbers, names, dates from the content — NOT vague statements
- Slide 1 should be an overview (title_stats or big_number)
- Middle slides should be details (bullet_list, comparison)
- Last slide should be the takeaway (key_quote or big_number)
- ALL text in English
- Keep text SHORT — this is a TV slide, not a document

Return ONLY a JSON array of {n} objects. No explanation, no markdown fences."""

        raw = self.gemini.call(prompt)
        if not raw:
            return []
        try:
            # Strip markdown fences if present.
            cleaned = raw.strip()
            if cleaned.startswith("```"):
                cleaned = re.sub(r"^```[a-zA-Z]*\n?", "", cleaned)
                cleaned = re.sub(r"\n?```$", "", cleaned)
            parsed = json.loads(cleaned)
            if isinstance(parsed, list):
                return parsed[:n]
        except (json.JSONDecodeError, ValueError):
            self.log("Gemini returned invalid JSON for slides")
        return []

    def _render_slide(self, data: dict, output_path: str, topic_title: str) -> bool:
        """Render one slide to a 1920x1080 JPEG via Pillow."""
        try:
            from PIL import Image, ImageDraw, ImageFont
        except ImportError:
            self.log("Pillow not available")
            return False

        layout = data.get("layout", "bullet_list")
        heading = data.get("heading", topic_title)[:60]
        subheading = data.get("subheading", "")[:80]
        items = data.get("items", [])
        highlight_number = str(data.get("highlight_number", ""))[:20]
        highlight_label = data.get("highlight_label", "")[:40]
        footer = data.get("footer", "")[:60]

        img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
        draw = ImageDraw.Draw(img)

        # Load fonts.
        font_path = self._pick_font()
        try:
            font_heading = ImageFont.truetype(font_path, 64) if font_path else ImageFont.load_default()
            font_sub = ImageFont.truetype(font_path, 36) if font_path else ImageFont.load_default()
            font_body = ImageFont.truetype(font_path, 32) if font_path else ImageFont.load_default()
            font_big = ImageFont.truetype(font_path, 120) if font_path else ImageFont.load_default()
            font_small = ImageFont.truetype(font_path, 24) if font_path else ImageFont.load_default()
        except Exception:
            font_heading = font_sub = font_body = font_big = font_small = ImageFont.load_default()

        # Top accent bar.
        draw.rectangle([(0, 0), (WIDTH, 6)], fill=ACCENT_COLOR)

        # Topic label (top-left).
        draw.text((80, 30), f"MindTickleBytes", fill=DIM_COLOR, font=font_small)

        if layout == "big_number":
            self._draw_big_number(
                draw, heading, subheading, highlight_number, highlight_label,
                footer, font_heading, font_sub, font_big, font_small,
            )
        elif layout == "title_stats":
            self._draw_title_stats(
                draw, heading, subheading, highlight_number, highlight_label,
                items, footer, font_heading, font_sub, font_body, font_small,
            )
        elif layout == "comparison":
            self._draw_comparison(
                draw, heading, items, footer, font_heading, font_body, font_small,
            )
        elif layout == "key_quote":
            self._draw_key_quote(
                draw, heading, items, footer, font_heading, font_sub, font_small,
            )
        else:  # bullet_list (default)
            self._draw_bullet_list(
                draw, heading, subheading, items, footer,
                font_heading, font_sub, font_body, font_small,
            )

        # Footer bar.
        draw.rectangle([(0, HEIGHT - 50), (WIDTH, HEIGHT)], fill=(10, 12, 22))
        if footer:
            draw.text((80, HEIGHT - 42), footer, fill=DIM_COLOR, font=font_small)

        try:
            os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
            img.save(output_path, "JPEG", quality=92)
            return True
        except Exception as e:
            self.log(f"slide save failed: {e}")
            return False

    # ------------------------------------------------------------------
    # Layout renderers
    # ------------------------------------------------------------------

    def _draw_big_number(self, draw, heading, sub, number, label,
                         footer, f_h, f_s, f_big, f_sm):
        # Heading.
        draw.text((80, 100), heading, fill=TEXT_COLOR, font=f_h)
        if sub:
            draw.text((80, 180), sub, fill=DIM_COLOR, font=f_s)
        # Big number centered.
        if number:
            bbox = draw.textbbox((0, 0), number, font=f_big)
            tw = bbox[2] - bbox[0]
            draw.text(((WIDTH - tw) // 2, 350), number, fill=ACCENT_COLOR, font=f_big)
        if label:
            bbox = draw.textbbox((0, 0), label, font=f_s)
            tw = bbox[2] - bbox[0]
            draw.text(((WIDTH - tw) // 2, 520), label, fill=DIM_COLOR, font=f_s)

    def _draw_title_stats(self, draw, heading, sub, number, label,
                          items, footer, f_h, f_s, f_b, f_sm):
        draw.text((80, 100), heading, fill=TEXT_COLOR, font=f_h)
        if sub:
            draw.text((80, 180), sub, fill=DIM_COLOR, font=f_s)
        # Stats row.
        y = 280
        if number:
            draw.text((80, y), number, fill=ACCENT_COLOR, font=f_h)
            if label:
                draw.text((80, y + 70), label, fill=DIM_COLOR, font=f_s)
            y += 150
        # Bullet items below.
        for item in (items or [])[:4]:
            item = str(item)[:80]
            draw.text((100, y), f"  {item}", fill=TEXT_COLOR, font=f_b)
            y += 50

    def _draw_bullet_list(self, draw, heading, sub, items, footer,
                          f_h, f_s, f_b, f_sm):
        draw.text((80, 100), heading, fill=TEXT_COLOR, font=f_h)
        if sub:
            draw.text((80, 180), sub, fill=DIM_COLOR, font=f_s)
        y = 260
        for i, item in enumerate((items or [])[:6]):
            item = str(item)[:90]
            # Colored bullet dot.
            draw.ellipse([(90, y + 12), (106, y + 28)], fill=ACCENT_COLOR)
            draw.text((130, y), item, fill=TEXT_COLOR, font=f_b)
            y += 60

    def _draw_comparison(self, draw, heading, items, footer,
                         f_h, f_b, f_sm):
        draw.text((80, 80), heading, fill=TEXT_COLOR, font=f_h)
        # Two-column comparison.
        col_w = (WIDTH - 200) // 2
        y = 200
        for i, item in enumerate((items or [])[:6]):
            item = str(item)[:80]
            col = 0 if i % 2 == 0 else 1
            x = 100 + col * (col_w + 20)
            if i % 2 == 0:
                # Left = blue card bg.
                draw.rounded_rectangle(
                    [(x - 10, y - 5), (x + col_w, y + 50)],
                    radius=8, fill=HIGHLIGHT_BG,
                )
            else:
                draw.rounded_rectangle(
                    [(x - 10, y - 5), (x + col_w, y + 50)],
                    radius=8, fill=(40, 25, 18),
                )
            draw.text((x + 10, y + 5), item, fill=TEXT_COLOR, font=f_b)
            if i % 2 == 1:
                y += 80

    def _draw_key_quote(self, draw, heading, items, footer,
                        f_h, f_s, f_sm):
        draw.text((80, 100), heading, fill=TEXT_COLOR, font=f_h)
        # Big accent quote mark.
        try:
            font_quote = ImageFont.truetype(
                self._pick_font() or "", 200
            )
        except Exception:
            font_quote = f_h
        draw.text((80, 220), "\u201C", fill=(40, 60, 100), font=font_quote)
        # Quote text.
        quote = str(items[0])[:200] if items else ""
        y = 350
        # Wrap to ~45 chars per line.
        words = quote.split()
        line = ""
        for w in words:
            if len(line) + len(w) + 1 > 45:
                draw.text((160, y), line, fill=TEXT_COLOR, font=f_s)
                y += 50
                line = w
            else:
                line = f"{line} {w}".strip()
        if line:
            draw.text((160, y), line, fill=TEXT_COLOR, font=f_s)

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _pick_font() -> str:
        candidates = [
            "/System/Library/Fonts/AppleSDGothicNeo.ttc",
            "/Library/Fonts/AppleSDGothicNeo.ttc",
            "/System/Library/Fonts/Supplemental/NotoSansKR-Regular.otf",
            "/System/Library/Fonts/PingFang.ttc",
        ]
        for c in candidates:
            if os.path.exists(c):
                return c
        return ""
