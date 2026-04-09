"""TTS Voice Agent — drives MeloTTS (ko) + OpenVoice v2 via local_tts_gen.py.

The heavy ML stack lives in the interpreter discovered by
`image_generator._find_python_with_torch()` (system Python 3.9 on this
Mac). We reuse that same helper so both image + audio generation go
through the same known-good interpreter.

If a voice reference wav is configured and exists, the pipeline applies
OpenVoice v2 tone conversion on top of MeloTTS's base Korean voice.
Otherwise it falls back to the base MeloTTS voice so the video pipeline
keeps working even before the user has recorded a reference sample.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Optional

from .base import BaseAgent
from .image_generator import _IMAGE_PYTHON


class TTSVoiceAgent(BaseAgent):
    """Generate a wav narration track from a Korean script."""

    name = "TTSVoice"
    prompt_file = ""  # No Gemini prompt — pure ML inference

    # The standalone runner is in scripts/local_tts_gen.py, same dir as
    # local_image_gen.py. We compute the path at call time rather than
    # caching it so the tests can swap the scripts directory.
    SCRIPT_RELPATH = "local_tts_gen.py"

    def run(
        self,
        script_text: str,
        output_path: str | Path,
        *,
        reference_voice: str | Path | None = None,
        speed: float = 1.0,
        language: str = "ko",
        timeout_seconds: int = 10 * 60,
    ) -> Optional[float]:
        """Synthesize `script_text` to `output_path` wav. Returns duration or None.

        `language` selects MeloTTS speaker + OpenVoice base embedding:
        ``ko`` → Korean speaker / kr.pth, ``en`` → English speaker / en.pth.
        """
        if not script_text or not script_text.strip():
            self.log("Empty script; nothing to synthesize.")
            return None

        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        script_path = self._resolve_runner()
        if not script_path.exists():
            self.log(f"Runner not found: {script_path}")
            return None

        lang = (language or "ko").lower()
        cmd = [
            _IMAGE_PYTHON,
            str(script_path),
            "--text", script_text,
            "--output", str(out),
            "--speed", str(speed),
            "--language", lang,
        ]
        if reference_voice:
            ref = Path(reference_voice)
            if ref.exists() and ref.stat().st_size > 2000:  # > 2KB → plausible audio
                cmd.extend(["--reference", str(ref)])
            else:
                self.log(
                    f"Reference voice missing or too small ({ref}); "
                    "falling back to MeloTTS base voice."
                )

        if _IMAGE_PYTHON != sys.executable:
            self.log(f"Using {_IMAGE_PYTHON} for TTS (has torch)")
        self.log(
            f"Synthesizing {len(script_text)} chars of {lang.upper()} narration…"
        )

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            self.log(f"TTS timed out after {timeout_seconds}s.")
            return None
        except Exception as e:
            self.log(f"Failed to spawn TTS runner: {e}")
            return None

        # Surface runner stdout to the agent log.
        if result.stdout:
            for line in result.stdout.strip().splitlines():
                self.log(line)

        if result.returncode != 0:
            if result.stderr:
                self.log(f"TTS runner stderr: {result.stderr[:800]}")
            self.log(f"TTS runner exited with code {result.returncode}")
            return None

        if not out.exists() or out.stat().st_size < 2000:
            self.log("TTS output missing or too small.")
            return None

        # Final line of stdout is "OK <seconds>"
        duration = self._parse_duration(result.stdout)
        if duration is None:
            # File exists; fall back to probing later.
            self.log("Could not parse duration from runner output.")
        else:
            self.log(f"Narration generated: {duration:.2f}s @ {out}")
        return duration

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------

    def _resolve_runner(self) -> Path:
        # scripts/agents/tts_voice.py → scripts/local_tts_gen.py
        agents_dir = Path(__file__).resolve().parent
        scripts_dir = agents_dir.parent
        return scripts_dir / self.SCRIPT_RELPATH

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
