"""Thumbnail Maker Agent — YouTube-ready 1280x720 jpg from a hero image.

Pure Pillow — no torch, no ffmpeg. Runs in whatever interpreter the daemon
happens to be on (pyenv Python 3.11 fine; PIL is tiny).

Composition:
    - Resize hero image to 1280x720 (crop to fit 16:9).
    - Darken the bottom 55% with a vertical gradient.
    - Draw the Korean post title in large white bold with a black outline.
    - "AI 뉴스" top-left badge.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from .base import BaseAgent

THUMB_WIDTH = 1280
THUMB_HEIGHT = 720

_FONT_CANDIDATES = [
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    "/Library/Fonts/AppleSDGothicNeo.ttc",
    "/System/Library/Fonts/Supplemental/NotoSansKR-Regular.otf",
    "/System/Library/Fonts/PingFang.ttc",
]


def _pick_font_path() -> str:
    for cand in _FONT_CANDIDATES:
        if os.path.exists(cand):
            return cand
    return ""


class ThumbnailMakerAgent(BaseAgent):
    """Render a 1280x720 JPG thumbnail for a generated video."""

    name = "ThumbnailMaker"
    prompt_file = ""

    def run(
        self,
        *,
        image_path: str | Path,
        title: str,
        output_path: str | Path,
        badge_text: str = "AI 뉴스",
    ) -> Optional[str]:
        """Render the thumbnail. Returns the output path on success."""
        hero = Path(image_path)
        out = Path(output_path)
        if not hero.exists():
            self.log(f"Hero image missing: {hero}")
            return None
        out.parent.mkdir(parents=True, exist_ok=True)

        try:
            from PIL import Image, ImageDraw, ImageFont, ImageFilter
        except Exception as e:
            self.log(f"Pillow import failed: {e}")
            return None

        try:
            img = Image.open(hero).convert("RGB")
            img = self._fit_crop(img, THUMB_WIDTH, THUMB_HEIGHT)
            img = self._apply_gradient(img, ImageDraw, Image)
            img = self._draw_title(img, title, ImageDraw, ImageFont)
            img = self._draw_badge(img, badge_text, ImageDraw, ImageFont)
            img.save(str(out), format="JPEG", quality=92, optimize=True)
        except Exception as e:
            self.log(f"Thumbnail render failed: {e}")
            return None

        if not out.exists() or out.stat().st_size < 5000:
            self.log("Thumbnail file too small / missing.")
            return None

        self.log(f"Thumbnail saved: {out}")
        return str(out)

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _fit_crop(img, target_w: int, target_h: int):
        src_w, src_h = img.size
        src_ratio = src_w / src_h
        target_ratio = target_w / target_h
        if src_ratio > target_ratio:
            # Image is wider than target → crop left/right.
            new_w = int(src_h * target_ratio)
            left = (src_w - new_w) // 2
            img = img.crop((left, 0, left + new_w, src_h))
        else:
            # Image is taller than target → crop top/bottom.
            new_h = int(src_w / target_ratio)
            top = (src_h - new_h) // 2
            img = img.crop((0, top, src_w, top + new_h))
        return img.resize((target_w, target_h))

    @staticmethod
    def _apply_gradient(img, ImageDraw, Image):
        """Darken the bottom ~55% with a vertical gradient for text legibility."""
        overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        start_y = int(img.height * 0.45)
        span = img.height - start_y
        for i in range(span):
            # 0 → transparent at top of gradient, 220 → very dark at bottom.
            alpha = int(((i / span) ** 1.2) * 220)
            draw.rectangle(
                ((0, start_y + i), (img.width, start_y + i + 1)),
                fill=(0, 0, 0, alpha),
            )
        composite = Image.alpha_composite(img.convert("RGBA"), overlay)
        return composite.convert("RGB")

    @staticmethod
    def _draw_title(img, title: str, ImageDraw, ImageFont):
        draw = ImageDraw.Draw(img)
        font_path = _pick_font_path()
        size = 68
        font = (
            ImageFont.truetype(font_path, size=size)
            if font_path
            else ImageFont.load_default()
        )

        # Two-line wrap — pick break near middle on space / comma.
        lines = ThumbnailMakerAgent._wrap(title, max_chars=18)
        line_h = int(size * 1.15)
        total_h = len(lines) * line_h
        start_y = img.height - total_h - 60
        for i, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=font)
            tw = bbox[2] - bbox[0]
            x = (img.width - tw) // 2
            y = start_y + i * line_h
            # Black outline
            for dx in (-3, 0, 3):
                for dy in (-3, 0, 3):
                    if dx or dy:
                        draw.text((x + dx, y + dy), line, font=font, fill=(0, 0, 0))
            # White fill
            draw.text((x, y), line, font=font, fill=(255, 255, 255))
        return img

    @staticmethod
    def _draw_badge(img, text: str, ImageDraw, ImageFont):
        draw = ImageDraw.Draw(img)
        font_path = _pick_font_path()
        size = 42
        font = (
            ImageFont.truetype(font_path, size=size)
            if font_path
            else ImageFont.load_default()
        )
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        pad = 18
        x0, y0 = 40, 40
        x1 = x0 + tw + pad * 2
        y1 = y0 + th + pad * 2
        # Red accent badge
        draw.rectangle((x0, y0, x1, y1), fill=(220, 48, 48))
        draw.text((x0 + pad, y0 + pad - 4), text, font=font, fill=(255, 255, 255))
        return img

    @staticmethod
    def _wrap(text: str, max_chars: int = 18) -> list[str]:
        text = text.strip()
        if len(text) <= max_chars:
            return [text]
        # Try to break at a space / comma near the middle.
        mid = len(text) // 2
        for step in range(0, 10):
            for idx in (mid - step, mid + step):
                if 0 < idx < len(text) and text[idx] in " ,":
                    return [text[:idx].strip(), text[idx + 1:].strip()]
        return [text[:max_chars].rstrip(), text[max_chars:].lstrip()]
