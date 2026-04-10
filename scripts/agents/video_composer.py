"""Video Composer Agent — assembles the final mp4 from image + audio + script.

Runs the moviepy pipeline under the same torch-capable interpreter as the
image and TTS agents (shared via `_IMAGE_PYTHON`) so everything stays in
one Python environment where ffmpeg wheels + PIL + moviepy co-exist.

Layout per clip:
    [intro 3s]   black background, channel name + post title (fade in)
    [main  Ns]   1920x1080 canvas; hero image centered with blurred
                 letterbox background, subtle Ken Burns zoom, narration
                 audio, burn-in subtitles (sentence-level, even split)
    [outro 2s]   channel name + "구독과 좋아요" (fade out)

Subtitles are split by sentence and their timing is derived from
equal-interval distribution over the narration duration. Future work:
Whisper forced alignment for tight sync.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

from .base import BaseAgent
from .image_generator import _IMAGE_PYTHON


class VideoComposerAgent(BaseAgent):
    """Compose a 1920x1080 H.264 mp4 from a hero image, narration wav, and script."""

    name = "VideoComposer"
    prompt_file = ""

    SCRIPT_RELPATH = "local_video_compose.py"

    def run(
        self,
        *,
        image_path: str | Path,
        audio_path: str | Path,
        script_text: str,
        title: str,
        output_path: str | Path,
        channel_name: str = "Antigravity News",
        intro_seconds: float = 3.0,
        outro_seconds: float = 2.0,
        animation_path: str | Path | None = None,
        image_paths: Optional[List[str | Path]] = None,
        timeout_seconds: int = 10 * 60,
    ) -> Optional[float]:
        """Render an mp4 at `output_path`. Returns duration seconds or None.

        Two modes:
        - **Single-hero** (default): pass `image_path` only.
        - **Newscast** (multi-hero): pass `image_paths` with 2+ images.
          The runner divides the audio into N equal Ken-Burns segments.
          `image_path` is still required as a fallback / first hero.
        """
        image = Path(image_path)
        audio = Path(audio_path)
        output = Path(output_path)

        if not image.exists():
            self.log(f"Hero image missing: {image}")
            return None
        if not audio.exists():
            self.log(f"Narration audio missing: {audio}")
            return None

        output.parent.mkdir(parents=True, exist_ok=True)

        runner = self._resolve_runner()
        if not runner.exists():
            self.log(f"Runner not found: {runner}")
            return None

        cmd = [
            _IMAGE_PYTHON,
            str(runner),
            "--image", str(image),
            "--audio", str(audio),
            "--script", script_text,
            "--title", title,
            "--output", str(output),
            "--channel", channel_name,
            "--intro", str(intro_seconds),
            "--outro", str(outro_seconds),
        ]
        # Newscast multi-hero mode: pass the comma-separated image list
        # plus optional animation clips and topic titles.
        if image_paths and len(image_paths) > 1:
            valid = [str(Path(p)) for p in image_paths if Path(p).exists()]
            if len(valid) > 1:
                cmd.extend(["--images", ",".join(valid)])
                self.log(f"newscast mode: {len(valid)} hero images")
                # Forward animation clips if provided.
                if hasattr(self, '_animation_paths') and self._animation_paths:
                    anim_csv = ",".join(str(p) for p in self._animation_paths)
                    cmd.extend(["--animations", anim_csv])
                # Forward topic titles for title cards + lower thirds.
                if hasattr(self, '_topic_titles') and self._topic_titles:
                    cmd.extend(["--titles", "|".join(self._topic_titles)])
                # Forward per-segment image lists for fast visual cuts.
                # Format: "img1,img2,img3|img4,img5|..." (pipe = segment boundary).
                if hasattr(self, '_segment_images') and self._segment_images:
                    seg_str = "|".join(
                        ",".join(p for p in seg if p) for seg in self._segment_images
                    )
                    if seg_str:
                        cmd.extend(["--segment-images", seg_str])
        elif animation_path:
            anim = Path(animation_path)
            if anim.exists() and anim.stat().st_size > 10_000:
                cmd.extend(["--animation", str(anim)])
                self.log(f"using LTX animation foreground: {anim.name}")

        if _IMAGE_PYTHON != sys.executable:
            self.log(f"Using {_IMAGE_PYTHON} for video compose")
        self.log(f"Rendering video to {output.name}…")

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            self.log(f"Video render timed out after {timeout_seconds}s.")
            return None
        except Exception as e:
            self.log(f"Failed to spawn video runner: {e}")
            return None

        if result.stdout:
            for line in result.stdout.strip().splitlines()[-15:]:
                self.log(line)

        if result.returncode != 0:
            if result.stderr:
                self.log(f"Compose stderr: {result.stderr[:800]}")
            return None

        if not output.exists() or output.stat().st_size < 10_000:
            self.log("Output mp4 missing or too small.")
            return None

        duration = self._parse_duration(result.stdout)
        size_mb = output.stat().st_size / (1024 * 1024)
        self.log(f"Video ready: {output.name} ({size_mb:.1f} MB)")
        return duration

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
