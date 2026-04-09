"""Video Animator Agent — drives LTX-Video I2V via local_video_animate.py.

Sibling of `image_generator.py` and `tts_voice.py`: the heavy ML stack
(torch + diffusers) lives in the interpreter discovered by
`image_generator._find_python_with_torch()` (system Python 3.9 on this
Mac). We spawn a subprocess and capture stdout / stderr.

Output is a short LTX-generated mp4 clip (default 5s @ 24fps, 1216×704)
that the video composer can ping-pong loop into the full narration
timeline. If anything fails (model download, MPS op gap, OOM, missing
weights) the agent returns None and the composer falls back to the
legacy Ken-Burns zoom on the static hero image — zero regression.

Configuration knobs are exposed via Settings (`video_animation_*`).
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Optional

from .base import BaseAgent
from .image_generator import _IMAGE_PYTHON


class VideoAnimatorAgent(BaseAgent):
    """Generate a short animated clip from a hero image using LTX-Video."""

    name = "VideoAnimator"
    prompt_file = ""

    SCRIPT_RELPATH = "local_video_animate.py"

    def run(
        self,
        *,
        image_path: str | Path,
        prompt: str,
        output_path: str | Path,
        duration_seconds: float = 5.0,
        width: int = 1216,
        height: int = 704,
        fps: int = 24,
        inference_steps: int = 20,
        timeout_seconds: int = 600,
    ) -> Optional[float]:
        """Render an LTX I2V clip. Returns actual clip duration or None on failure."""
        image = Path(image_path)
        out = Path(output_path)
        if not image.exists():
            self.log(f"hero image missing: {image}")
            return None

        out.parent.mkdir(parents=True, exist_ok=True)
        runner = self._resolve_runner()
        if not runner.exists():
            self.log(f"runner not found: {runner}")
            return None

        cmd = [
            _IMAGE_PYTHON,
            str(runner),
            "--image", str(image),
            "--prompt", prompt or "",
            "--output", str(out),
            "--duration", str(duration_seconds),
            "--width", str(width),
            "--height", str(height),
            "--fps", str(fps),
            "--steps", str(inference_steps),
        ]

        if _IMAGE_PYTHON != sys.executable:
            self.log(f"Using {_IMAGE_PYTHON} for LTX-Video (has torch)")
        self.log(
            f"Animating hero ({duration_seconds}s @ {width}×{height}/{fps}fps)…"
        )

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            self.log(f"animation timed out after {timeout_seconds}s")
            return None
        except Exception as e:
            self.log(f"failed to spawn runner: {e}")
            return None

        if result.stdout:
            for line in result.stdout.strip().splitlines()[-15:]:
                self.log(line)

        if result.returncode != 0:
            if result.stderr:
                self.log(f"runner stderr: {result.stderr[:500]}")
            return None

        if not out.exists() or out.stat().st_size < 10_000:
            self.log("output mp4 missing or too small")
            return None

        duration = self._parse_duration(result.stdout)
        size_mb = out.stat().st_size / (1024 * 1024)
        self.log(f"animation ready: {out.name} ({size_mb:.1f} MB)")
        return duration

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------

    def _resolve_runner(self) -> Path:
        return Path(__file__).resolve().parent.parent / self.SCRIPT_RELPATH

    @staticmethod
    def _parse_duration(stdout: str) -> Optional[float]:
        for line in reversed((stdout or "").strip().splitlines()):
            line = line.strip()
            if line.startswith("OK "):
                try:
                    return float(line.split()[1])
                except (IndexError, ValueError):
                    return None
        return None

    @staticmethod
    def build_prompt_from_post(topic: str, summary: str = "") -> str:
        """Compose a concise LTX-friendly description from the post topic.

        Kept short on purpose — LTX rewards descriptive nouns over long
        sentences. The runner appends its own cinematic-style suffix.
        """
        topic = (topic or "").strip()
        summary = (summary or "").strip()
        if summary and len(summary) > 200:
            summary = summary[:200].rsplit(" ", 1)[0] + "…"
        if summary:
            return f"News footage about {topic}. {summary}"
        return f"News footage about {topic}"
