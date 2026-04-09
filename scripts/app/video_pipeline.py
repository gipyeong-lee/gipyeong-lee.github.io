"""Video pipeline orchestrator — 5 stages from published post → YouTube.

Counterpart of `scripts/pipeline.py` (blog pipeline). This file is
synchronous-style (stages run in order on a worker thread); the async
`video_worker.py` wraps it with `asyncio.to_thread` and injects timeouts.

Stages:
    1. script     — ScriptWriterAgent  (Korean post → narration text)
    2. tts        — TTSVoiceAgent      (text → wav via MeloTTS + OpenVoice)
    3. compose    — VideoComposerAgent (wav + hero → mp4)
    4. thumbnail  — ThumbnailMakerAgent (hero → 1280x720 jpg)
    5. upload     — YouTubeUploaderAgent (mp4 → unlisted YouTube video)

All outputs land under `scripts/app/data/videos/<slug>.{wav,mp4,jpg}` so
the Admin UI can serve them directly and so nothing ever touches the
public Jekyll tree.

The orchestrator accepts a `stage_hook` callable so callers can stream
per-stage updates into the DB without this module knowing about ORM.
"""
from __future__ import annotations

import time
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

from ..agents import (
    ScriptWriterAgent,
    TTSVoiceAgent,
    ThumbnailMakerAgent,
    VideoComposerAgent,
    YouTubeUploaderAgent,
)
from .config import IMAGES_DIR, POSTS_DIR, VIDEOS_DIR
from .settings_store import get_settings


# ----------------------------------------------------------------------
# Result object
# ----------------------------------------------------------------------


@dataclass
class VideoPipelineResult:
    success: bool
    slug: str
    script: Optional[str] = None
    wav_path: Optional[str] = None
    mp4_path: Optional[str] = None
    thumbnail_path: Optional[str] = None
    duration_seconds: Optional[float] = None
    youtube_video_id: Optional[str] = None
    youtube_url: Optional[str] = None
    youtube_privacy: Optional[str] = None
    failed_stage: Optional[str] = None
    error: Optional[str] = None


# ----------------------------------------------------------------------
# Stage hook protocol
# ----------------------------------------------------------------------


# StageHook(stage, status, meta) — callers use this to log stage transitions.
# status ∈ {"start", "ok", "fail"}.
StageHook = Callable[[str, str, dict], None]


def _noop_hook(stage: str, status: str, meta: dict) -> None:
    pass


# ----------------------------------------------------------------------
# Orchestrator
# ----------------------------------------------------------------------


class VideoPipeline:
    """Run all 5 video stages for a single published post."""

    def __init__(
        self,
        *,
        script_writer: Optional[ScriptWriterAgent] = None,
        tts: Optional[TTSVoiceAgent] = None,
        composer: Optional[VideoComposerAgent] = None,
        thumbnail: Optional[ThumbnailMakerAgent] = None,
        uploader: Optional[YouTubeUploaderAgent] = None,
    ):
        self.script_writer = script_writer or ScriptWriterAgent()
        self.tts = tts or TTSVoiceAgent()
        self.composer = composer or VideoComposerAgent()
        self.thumbnail = thumbnail or ThumbnailMakerAgent()
        self.uploader = uploader or YouTubeUploaderAgent()

    def run(
        self,
        *,
        slug: str,
        title: str,
        description: str = "",
        tags: Optional[list[str]] = None,
        post_path: Optional[Path] = None,
        image_path: Optional[Path] = None,
        permalink: str = "",
        stage_hook: StageHook = _noop_hook,
        upload: Optional[bool] = None,
    ) -> VideoPipelineResult:
        """Execute all stages for `slug`. Returns a VideoPipelineResult."""
        settings = get_settings()
        channel = settings.youtube_channel_name or "Antigravity News"
        target_duration = settings.video_target_duration_seconds or 90
        ref_voice = (settings.video_reference_voice_path or "").strip()
        if upload is None:
            upload = settings.video_auto_upload
        privacy = settings.youtube_default_privacy or "unlisted"

        result = VideoPipelineResult(success=False, slug=slug)

        # Resolve input files.
        if post_path is None:
            post_path = Path(POSTS_DIR) / f"{slug}.md"
        if image_path is None:
            image_path = _find_image(slug)

        if post_path is None or not Path(post_path).exists():
            result.failed_stage = "script"
            result.error = f"post file not found for slug {slug}"
            stage_hook("script", "fail", {"error": result.error})
            return result

        if image_path is None or not Path(image_path).exists():
            result.failed_stage = "compose"
            result.error = f"hero image not found for slug {slug}"
            stage_hook("compose", "fail", {"error": result.error})
            return result

        Path(VIDEOS_DIR).mkdir(parents=True, exist_ok=True)
        wav_path = Path(VIDEOS_DIR) / f"{slug}.wav"
        mp4_path = Path(VIDEOS_DIR) / f"{slug}.mp4"
        thumb_path = Path(VIDEOS_DIR) / f"{slug}.jpg"

        # --- Stage 1: Script ---------------------------------------------
        stage_hook("script", "start", {})
        t0 = time.time()
        script = self.script_writer.run(
            post_path=post_path,
            channel_name=channel,
            target_duration_seconds=target_duration,
        )
        if not script:
            result.failed_stage = "script"
            result.error = "script writer returned empty"
            stage_hook("script", "fail", {"error": result.error})
            return result
        result.script = script
        stage_hook(
            "script",
            "ok",
            {"chars": len(script), "elapsed": round(time.time() - t0, 2)},
        )

        # --- Stage 2: TTS ------------------------------------------------
        stage_hook("tts", "start", {"has_reference": bool(ref_voice)})
        t0 = time.time()
        try:
            duration = self.tts.run(
                script_text=script,
                output_path=wav_path,
                reference_voice=ref_voice or None,
            )
        except Exception as e:
            traceback.print_exc()
            result.failed_stage = "tts"
            result.error = f"tts crashed: {e}"
            stage_hook("tts", "fail", {"error": result.error})
            return result
        if duration is None or not wav_path.exists():
            result.failed_stage = "tts"
            result.error = "tts produced no wav output"
            stage_hook("tts", "fail", {"error": result.error})
            return result
        result.wav_path = str(wav_path)
        stage_hook(
            "tts",
            "ok",
            {"duration": duration, "elapsed": round(time.time() - t0, 2)},
        )

        # --- Stage 3: Compose --------------------------------------------
        stage_hook("compose", "start", {})
        t0 = time.time()
        try:
            total = self.composer.run(
                image_path=image_path,
                audio_path=wav_path,
                script_text=script,
                title=title,
                output_path=mp4_path,
                channel_name=channel,
            )
        except Exception as e:
            traceback.print_exc()
            result.failed_stage = "compose"
            result.error = f"compose crashed: {e}"
            stage_hook("compose", "fail", {"error": result.error})
            return result
        if total is None or not mp4_path.exists():
            result.failed_stage = "compose"
            result.error = "compose produced no mp4 output"
            stage_hook("compose", "fail", {"error": result.error})
            return result
        result.mp4_path = str(mp4_path)
        result.duration_seconds = total
        stage_hook(
            "compose",
            "ok",
            {"duration": total, "elapsed": round(time.time() - t0, 2)},
        )

        # --- Stage 4: Thumbnail ------------------------------------------
        stage_hook("thumbnail", "start", {})
        t0 = time.time()
        try:
            thumb_result = self.thumbnail.run(
                image_path=image_path,
                title=title,
                output_path=thumb_path,
            )
        except Exception as e:
            traceback.print_exc()
            thumb_result = None
        if thumb_result and thumb_path.exists():
            result.thumbnail_path = str(thumb_path)
            stage_hook(
                "thumbnail",
                "ok",
                {"elapsed": round(time.time() - t0, 2)},
            )
        else:
            # Non-fatal: thumbnail failure should not kill the whole video.
            stage_hook("thumbnail", "fail", {"error": "thumbnail skipped"})

        # --- Stage 5: Upload ---------------------------------------------
        if not upload:
            stage_hook("upload", "ok", {"skipped": True})
            result.success = True
            return result

        stage_hook("upload", "start", {"privacy": privacy})
        t0 = time.time()
        upload_desc = _build_description(description, permalink, tags, channel)
        try:
            upload_result = self.uploader.run(
                mp4_path=mp4_path,
                title=title,
                description=upload_desc,
                tags=(tags or []) + ["AI", "AI뉴스", channel.replace(" ", "")],
                privacy=privacy,
                thumbnail_path=thumb_path if result.thumbnail_path else None,
            )
        except Exception as e:
            traceback.print_exc()
            result.failed_stage = "upload"
            result.error = f"upload crashed: {e}"
            stage_hook("upload", "fail", {"error": result.error})
            return result

        if upload_result is None:
            result.failed_stage = "upload"
            result.error = "upload returned None"
            stage_hook("upload", "fail", {"error": result.error})
            return result

        result.youtube_video_id = upload_result.video_id
        result.youtube_url = upload_result.url
        result.youtube_privacy = upload_result.privacy
        stage_hook(
            "upload",
            "ok",
            {
                "video_id": upload_result.video_id,
                "url": upload_result.url,
                "elapsed": round(time.time() - t0, 2),
            },
        )

        result.success = True
        return result


# ----------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------


def _find_image(slug: str) -> Optional[Path]:
    """Locate the Jekyll hero image for this slug."""
    images = Path(IMAGES_DIR)
    if not images.exists():
        return None
    for ext in ("jpg", "jpeg", "png", "webp"):
        cand = images / f"{slug}.{ext}"
        if cand.exists():
            return cand
    return None


def _build_description(
    description: str, permalink: str, tags: Optional[list[str]], channel: str
) -> str:
    base = (description or "").strip()
    tag_line = " ".join(f"#{t.replace(' ', '')}" for t in (tags or [])[:8])
    link_line = ""
    if permalink:
        origin = "https://gipyeong-lee.github.io"
        if not permalink.startswith("http"):
            link_line = f"원문: {origin}{permalink}"
        else:
            link_line = f"원문: {permalink}"
    parts: list[str] = [base]
    if link_line:
        parts.append("")
        parts.append(link_line)
    parts.append("")
    parts.append(f"#{channel.replace(' ', '')} #AI #AI뉴스 {tag_line}".strip())
    return "\n".join(parts).strip()
