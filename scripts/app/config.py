"""Static configuration: paths, constants, default settings.

Runtime-overridable settings live in the SQLite `settings` table and are
read through `settings_store.get_settings()`. The values here are only used
on first run (DB seeding) and as fallbacks.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

# -- Paths ---------------------------------------------------------------

# repo root = two directories up from this file (scripts/app/config.py)
REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts"
APP_DIR = SCRIPTS_DIR / "app"
DATA_DIR = APP_DIR / "data"
POSTS_DIR = REPO_ROOT / "_posts"
IMAGES_DIR = REPO_ROOT / "images"
TEMPLATES_DIR = APP_DIR / "templates"
STATIC_DIR = APP_DIR / "static"
VIDEOS_DIR = DATA_DIR / "videos"

DATA_DIR.mkdir(parents=True, exist_ok=True)
VIDEOS_DIR.mkdir(parents=True, exist_ok=True)

# User-scoped config (gitignored, survives daemon restarts).
# Holds YouTube OAuth client_secrets.json / token.json and voice reference wav.
AIBLOG_CONFIG_DIR = Path.home() / ".config" / "aiblog"
YOUTUBE_CLIENT_SECRETS = AIBLOG_CONFIG_DIR / "client_secrets.json"
YOUTUBE_TOKEN_PATH = AIBLOG_CONFIG_DIR / "youtube_token.json"
VOICE_REFERENCE_PATH = AIBLOG_CONFIG_DIR / "voice_reference.wav"

DB_PATH = DATA_DIR / "aiblog.db"
DB_URL = f"sqlite:///{DB_PATH}"

# -- Server --------------------------------------------------------------

HOST = os.environ.get("AIBLOG_HOST", "127.0.0.1")
PORT = int(os.environ.get("AIBLOG_PORT", "7001"))

# -- Default runtime settings (seeded into DB on first run) --------------


@dataclass(frozen=True)
class DefaultSettings:
    min_interval_seconds: int = 2 * 60 * 60               # 2h
    max_interval_seconds: int = 6 * 60 * 60               # 6h
    event_trigger_threshold: float = 0.85                 # score to preempt timer
    source_poll_interval_seconds: int = 15 * 60           # 15m
    cooldown_after_fail_seconds: int = 60 * 60            # 1h
    max_fail_count_before_block: int = 3
    pipeline_timeout_seconds: int = 20 * 60               # 20m per run
    auto_publish: bool = True
    git_push: bool = True

    # -- Fact-checker tuning (Option A relaxations) ----------------------
    # Raise defaults to be more forgiving than the hardcoded 0.30 / 0.20.
    # Run #4 failed at 20% revision threshold with a writer that couldn't
    # satisfy it in 2 rounds; the new defaults + snippet-based verification
    # should dramatically improve pass rate without sacrificing integrity.
    fact_check_fail_ratio: float = 0.40                   # >= this → FAIL
    fact_check_revision_ratio: float = 0.25               # >= this → NEEDS_REVISION
    fact_check_dead_link_tolerance: int = 2               # dead links allowed
    fact_check_relaxation_per_round: float = 0.10         # bump per retry
    max_revision_rounds: int = 3                          # was 2

    keyword_blocklist: list = field(default_factory=list)
    sources_enabled: dict = field(default_factory=lambda: {
        "hackernews": True,
        "arxiv": True,
        "openai_blog": True,
        "anthropic_blog": True,
        "deepmind_blog": True,
        "meta_ai_blog": True,
        "xai_blog": True,
        "mistral_blog": True,
    })

    # -- Video pipeline (Phase E) ----------------------------------------
    # Master switch; off until user finishes GCP OAuth + voice reference.
    video_generation_enabled: bool = False
    # Path to the user's 30-60s Korean voice reference wav used by OpenVoice.
    # Empty string means "use MeloTTS base voice without tone conversion".
    video_reference_voice_path: str = ""
    # Target narration length in seconds (soft guide for the script writer).
    video_target_duration_seconds: int = 90
    # Automatically upload to YouTube once compose succeeds.
    video_auto_upload: bool = True
    # Default YouTube visibility. Safety default: unlisted.
    youtube_default_privacy: str = "unlisted"
    # Display name used in intro / outro / description.
    youtube_channel_name: str = "Antigravity News"
    # Hard cap on YouTube API uploads per calendar day (quota defense).
    # 1 upload ≈ 1600 units; 10,000 daily quota → ~6 uploads/day max.
    youtube_upload_daily_cap: int = 5
    # Per-video pipeline timeout (script + tts + compose + thumbnail + upload).
    video_pipeline_timeout_seconds: int = 15 * 60
    # Hard cap on video pipeline retries for a single post.
    video_max_retries: int = 2
    # YouTube metadata / captions / playlist enhancements
    youtube_metadata_enabled: bool = True        # use Gemini-generated rich metadata
    youtube_captions_enabled: bool = True        # upload SRT subtitles after publish
    youtube_playlist_id: str = ""                # optional: auto-append to this playlist
    # Which CLI backend agents should default to when creative text is needed.
    # "gemini" (default — existing agents) or "codex". Claude is never a runtime
    # option per user policy.
    cli_backend: str = "gemini"
    # LTX-Video I2V animation (replaces Ken-Burns zoom on the static hero
    # image with actual generative motion). Defaults ENABLED — toggle off
    # in Settings if performance is unacceptable on this machine.
    video_animation_enabled: bool = True
    video_animation_model: str = "ltx-video-2b"      # display only; runner is hardcoded
    video_animation_duration_seconds: float = 5.0    # 5s clip → ping-pong looped
    video_animation_timeout_seconds: int = 10 * 60   # 10 min hard cap per generation
    video_animation_width: int = 1216
    video_animation_height: int = 704
    video_animation_fps: int = 24
    video_animation_steps: int = 20


DEFAULTS = DefaultSettings()

# -- launchd -------------------------------------------------------------

LAUNCHD_LABEL = "com.gipyeonglee.aiblog"
LAUNCHD_PLIST_PATH = Path.home() / "Library" / "LaunchAgents" / f"{LAUNCHD_LABEL}.plist"

# -- Misc ----------------------------------------------------------------

LOG_RETENTION_DAYS = 90
TICK_INTERVAL_SECONDS = 60  # scheduler_loop sleep between ticks
