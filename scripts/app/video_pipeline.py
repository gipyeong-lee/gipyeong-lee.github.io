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
    VideoAnimatorAgent,
    VideoComposerAgent,
    YouTubeMetadataAgent,
    YouTubeUploaderAgent,
)
from ..agents.youtube_metadata import build_srt_captions
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
    srt_path: Optional[str] = None
    duration_seconds: Optional[float] = None
    metadata_title: Optional[str] = None
    metadata_description: Optional[str] = None
    metadata_tags: list = None  # type: ignore[assignment]
    youtube_video_id: Optional[str] = None
    youtube_url: Optional[str] = None
    youtube_privacy: Optional[str] = None
    caption_uploaded: bool = False
    playlist_added: bool = False
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
        animator: Optional[VideoAnimatorAgent] = None,
        composer: Optional[VideoComposerAgent] = None,
        thumbnail: Optional[ThumbnailMakerAgent] = None,
        metadata: Optional[YouTubeMetadataAgent] = None,
        uploader: Optional[YouTubeUploaderAgent] = None,
    ):
        self.script_writer = script_writer or ScriptWriterAgent()
        self.tts = tts or TTSVoiceAgent()
        self.animator = animator or VideoAnimatorAgent()
        self.composer = composer or VideoComposerAgent()
        self.thumbnail = thumbnail or ThumbnailMakerAgent()
        self.metadata = metadata or YouTubeMetadataAgent()
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

        # --- Stage 2.5: Animate (LTX-Video I2V) --------------------------
        # Generates a short animated clip from the hero image. The composer
        # then ping-pong loops it under the narration. On any failure
        # (disabled, model missing, OOM, MPS op gap) we silently fall
        # through to the legacy Ken-Burns zoom on the static hero.
        anim_path: Optional[Path] = None
        if settings.video_animation_enabled:
            anim_path = Path(VIDEOS_DIR) / f"{slug}.anim.mp4"
            # Reuse a pre-existing animation clip across reruns to save
            # ~1-3 minutes of generation time when only later stages need
            # to be retried.
            reuse = anim_path.exists() and anim_path.stat().st_size > 10_000
            stage_hook(
                "animate",
                "start",
                {"reused": reuse, "model": settings.video_animation_model},
            )
            t0 = time.time()
            anim_ok = False
            if reuse:
                anim_ok = True
            else:
                try:
                    anim_prompt = self.animator.build_prompt_from_post(
                        topic=title,
                        summary=meta.get("description", "") if (meta := _read_post_meta_for_anim(post_path)) else "",
                    )
                    anim_dur = self.animator.run(
                        image_path=image_path,
                        prompt=anim_prompt,
                        output_path=anim_path,
                        duration_seconds=settings.video_animation_duration_seconds,
                        timeout_seconds=settings.video_animation_timeout_seconds,
                    )
                    anim_ok = anim_dur is not None and anim_path.exists()
                except Exception as e:
                    traceback.print_exc()
                    self.animator.log(f"animator crashed: {e}")
                    anim_ok = False
            if anim_ok:
                stage_hook(
                    "animate",
                    "ok",
                    {"path": anim_path.name, "elapsed": round(time.time() - t0, 2)},
                )
            else:
                # Non-fatal: fall through to static Ken-Burns mode.
                stage_hook(
                    "animate",
                    "fail",
                    {
                        "fallback": "ken_burns",
                        "elapsed": round(time.time() - t0, 2),
                    },
                )
                anim_path = None

        # --- Stage 3: Compose --------------------------------------------
        stage_hook("compose", "start", {"animation": bool(anim_path)})
        t0 = time.time()
        try:
            total = self.composer.run(
                image_path=image_path,
                audio_path=wav_path,
                script_text=script,
                title=title,
                output_path=mp4_path,
                channel_name=channel,
                animation_path=anim_path,
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

        # --- Stage 4.5: Metadata (title/description/chapters/tags) -------
        # Runs even when upload is off, because the metadata is useful for
        # the Admin UI preview and gets stored on the Video row.
        tts_duration = float(duration or 0.0)
        stage_hook("metadata", "start", {})
        t0 = time.time()
        meta_obj = None
        if settings.youtube_metadata_enabled:
            try:
                meta_obj = self.metadata.run(
                    post_path=post_path,
                    narration_script=script,
                    narration_duration_seconds=tts_duration,
                    channel_name=channel,
                    permalink=permalink,
                    fallback_title=title,
                    fallback_description=description,
                    fallback_tags=tags or [],
                )
            except Exception as e:
                self.metadata.log(f"metadata agent crashed: {e}")
                meta_obj = None
        if meta_obj is None:
            # Legacy fallback: plain description + hashtag tail.
            from ..agents.youtube_metadata import YouTubeMetadata

            meta_obj = YouTubeMetadata.from_fallback(
                title=title,
                description=description,
                tags=tags or [],
                permalink=permalink,
                channel_name=channel,
            )
        result.metadata_title = meta_obj.title
        result.metadata_description = meta_obj.description
        result.metadata_tags = list(meta_obj.tags)
        stage_hook(
            "metadata",
            "ok",
            {
                "title_chars": len(meta_obj.title),
                "desc_chars": len(meta_obj.description),
                "tags": len(meta_obj.tags),
                "chapters": len(meta_obj.chapters),
                "elapsed": round(time.time() - t0, 2),
            },
        )

        # --- Stage 4.6: SRT captions ------------------------------------
        srt_path: Optional[Path] = None
        if settings.youtube_captions_enabled and tts_duration > 0:
            try:
                srt_text = build_srt_captions(
                    script,
                    narration_duration_seconds=tts_duration,
                )
                if srt_text:
                    srt_path = Path(VIDEOS_DIR) / f"{slug}.srt"
                    srt_path.write_text(srt_text, encoding="utf-8")
                    result.srt_path = str(srt_path)
                    stage_hook("captions", "ok", {"bytes": len(srt_text)})
            except Exception as e:
                stage_hook("captions", "fail", {"error": str(e)})
                srt_path = None

        # --- Stage 5: Upload ---------------------------------------------
        if not upload:
            stage_hook("upload", "ok", {"skipped": True})
            result.success = True
            return result

        stage_hook("upload", "start", {"privacy": privacy})
        t0 = time.time()
        try:
            upload_result = self.uploader.run(
                mp4_path=mp4_path,
                title=meta_obj.title or title,
                description=meta_obj.description,
                tags=meta_obj.tags,
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

        # --- Post-upload extras: captions + playlist --------------------
        if srt_path and srt_path.exists():
            try:
                ok = self.uploader.upload_captions(
                    upload_result.video_id, srt_path, language="ko"
                )
                result.caption_uploaded = bool(ok)
                stage_hook("captions_upload", "ok" if ok else "fail", {})
            except Exception as e:
                stage_hook("captions_upload", "fail", {"error": str(e)})

        if settings.youtube_playlist_id:
            try:
                ok = self.uploader.add_to_playlist(
                    upload_result.video_id, settings.youtube_playlist_id
                )
                result.playlist_added = bool(ok)
                stage_hook("playlist", "ok" if ok else "fail", {})
            except Exception as e:
                stage_hook("playlist", "fail", {"error": str(e)})

        result.success = True
        return result


# ----------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------


def _read_post_meta_for_anim(post_path: Optional[Path]) -> Optional[dict]:
    """Tiny helper: extract front-matter fields from a post for the animator prompt.

    Reuses the same parser pattern as other modules; we intentionally
    don't import the heavier video_worker version to keep the pipeline
    module dependency-free.
    """
    if post_path is None:
        return None
    try:
        from pathlib import Path as _P
        p = _P(post_path)
        if not p.exists():
            return None
        raw = p.read_text(encoding="utf-8")
    except Exception:
        return None
    import re as _re

    match = _re.match(r"^---\s*\n(.*?)\n---\s*\n", raw, _re.DOTALL)
    if not match:
        return None
    fm = match.group(1)
    out: dict = {}
    for line in fm.splitlines():
        kv = _re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if not kv:
            continue
        key, val = kv.group(1), kv.group(2).strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        out[key] = val
    return out


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


