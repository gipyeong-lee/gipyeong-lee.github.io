"""Segment Illustrator — generates multiple AI images per topic for newscast.

Given a topic title, description, and script excerpt, asks Gemini for 4-5
visual scene descriptions that illustrate different aspects of the topic,
then generates each via SDXL-Turbo. The result is a list of image paths
that the composer cuts between every 20-30 seconds within a segment,
creating the "fast visual pacing" look of channels like 헤이제임스.

Design notes:
- Uses the same _IMAGE_PYTHON + local_image_gen.py pipeline as
  ImageGeneratorAgent — no new ML stack needed.
- Caches images at `videos/<slug>.seg<N>.vis<K>.jpg` so reruns skip.
- Falls back gracefully: if Gemini or SDXL fails, returns whatever
  images it managed to produce (even zero = composer uses hero only).
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Optional

from .base import BaseAgent
from .image_generator import _IMAGE_PYTHON


class SegmentIllustratorAgent(BaseAgent):
    """Generate supplementary AI images for each newscast segment."""

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
        """Generate supplementary images for one topic segment.

        Returns a list of absolute paths to successfully generated
        images (may be shorter than `num_images` on partial failure,
        or empty on total failure).
        """
        out_dir = Path(output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        # Check cache: if enough images already exist, skip generation.
        cached = self._find_cached(out_dir, slug_prefix, num_images)
        if len(cached) >= num_images:
            self.log(f"{slug_prefix}: {len(cached)} cached images, skipping")
            return cached

        # Ask Gemini for visual scene descriptions.
        scenes = self._design_scenes(
            topic_title, topic_description, script_excerpt, num_images
        )
        if not scenes:
            self.log(f"{slug_prefix}: Gemini returned no scene descriptions")
            return cached  # return whatever cache we have

        self.log(f"{slug_prefix}: generating {len(scenes)} illustrations")

        results: list[str] = list(cached)
        for k, scene_prompt in enumerate(scenes):
            if len(results) >= num_images:
                break
            out_path = out_dir / f"{slug_prefix}.vis{k}.jpg"
            if out_path.exists() and out_path.stat().st_size > 5000:
                results.append(str(out_path))
                continue
            ok = self._generate_image(scene_prompt, str(out_path), timeout_per_image)
            if ok:
                results.append(str(out_path))

        self.log(f"{slug_prefix}: {len(results)} images ready")
        return results

    def _find_cached(self, out_dir: Path, prefix: str, n: int) -> list[str]:
        """Find pre-existing illustration images from a prior run."""
        found = []
        for k in range(n + 2):  # check a few extra
            for path in [
                out_dir / f"{prefix}.vis{k}.jpg",
            ]:
                if path.exists() and path.stat().st_size > 5000:
                    found.append(str(path))
        return found[:n]

    def _design_scenes(
        self,
        title: str,
        description: str,
        script_excerpt: str,
        n: int,
    ) -> list[str]:
        """Ask Gemini for N visual scene prompts to illustrate the topic."""
        prompt = f"""You are a video art director for an AI news channel. Given the
topic below, design {n} DISTINCT visual scene descriptions for SDXL image generation.
Each scene should illustrate a DIFFERENT aspect, moment, or concept from the topic.

Topic: {title}
Description: {description}
Script excerpt: {(script_excerpt or '')[:1500]}

VISUAL RULES (STRICT):
- Each scene description starts with: "Cinematic photograph, high detail, editorial style"
- NO text, watermarks, logos, UI elements in the image
- NO human faces (use silhouettes, rear views, hands, or symbolic objects)
- Favor: abstract technological concepts, data visualization aesthetics,
  glowing circuits, cityscapes, server rooms, lab equipment, symbolic objects
- Each scene should feel DIFFERENT from the others (varied colors, compositions, subjects)
- Color palette: deep blues, teals, warm amber accents, dark backgrounds
- Widescreen 16:9 composition

Return ONLY {n} lines, one scene description per line. No numbering, no bullets, no explanation.
Just the raw prompt text for each scene."""

        result = self.gemini.call(prompt)
        if not result:
            return []
        lines = [
            line.strip() for line in result.strip().splitlines()
            if line.strip() and len(line.strip()) > 30
        ]
        return lines[:n]

    def _generate_image(
        self, prompt: str, output_path: str, timeout: int
    ) -> bool:
        """Generate one image via local_image_gen.py (SDXL-Turbo)."""
        script_dir = Path(__file__).resolve().parent.parent
        script_path = script_dir / "local_image_gen.py"
        if not script_path.exists():
            return False

        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        cmd = [
            _IMAGE_PYTHON,
            str(script_path),
            "--prompt", prompt,
            "--output", output_path,
        ]
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=timeout
            )
            if result.returncode == 0 and os.path.exists(output_path) and os.path.getsize(output_path) > 5000:
                return True
        except Exception:
            pass
        return False
