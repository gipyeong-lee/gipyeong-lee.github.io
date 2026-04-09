"""Runtime settings read/write backed by the `settings` SQLite table.

Defaults come from `config.DEFAULTS`. The first time the app starts, we
seed any missing keys. Subsequent reads/writes go through this module so
the Admin UI can mutate live behavior.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, fields
from typing import Any

from sqlalchemy import select

from .config import DEFAULTS, DefaultSettings
from .db import session_scope
from .models_db import Setting


@dataclass
class RuntimeSettings:
    min_interval_seconds: int
    max_interval_seconds: int
    event_trigger_threshold: float
    source_poll_interval_seconds: int
    cooldown_after_fail_seconds: int
    max_fail_count_before_block: int
    pipeline_timeout_seconds: int
    auto_publish: bool
    git_push: bool
    # Fact-checker tuning
    fact_check_fail_ratio: float
    fact_check_revision_ratio: float
    fact_check_dead_link_tolerance: int
    fact_check_relaxation_per_round: float
    max_revision_rounds: int
    keyword_blocklist: list[str]
    sources_enabled: dict[str, bool]
    # Video pipeline (Phase E)
    video_generation_enabled: bool
    video_reference_voice_path: str
    video_target_duration_seconds: int
    video_auto_upload: bool
    youtube_default_privacy: str
    youtube_channel_name: str
    youtube_upload_daily_cap: int
    video_pipeline_timeout_seconds: int
    video_max_retries: int
    youtube_metadata_enabled: bool
    youtube_captions_enabled: bool
    youtube_playlist_id: str
    cli_backend: str
    video_animation_enabled: bool
    video_animation_model: str
    video_animation_duration_seconds: float
    video_animation_timeout_seconds: int
    video_animation_width: int
    video_animation_height: int
    video_animation_fps: int
    video_animation_steps: int
    # -- Daily broadcast scheduling --
    broadcast_hour_local: int
    broadcast_timezone: str
    video_language: str
    topics_per_episode: int
    topics_freshness_hours: int


def _defaults_as_dict() -> dict[str, Any]:
    return {
        "min_interval_seconds": DEFAULTS.min_interval_seconds,
        "max_interval_seconds": DEFAULTS.max_interval_seconds,
        "event_trigger_threshold": DEFAULTS.event_trigger_threshold,
        "source_poll_interval_seconds": DEFAULTS.source_poll_interval_seconds,
        "cooldown_after_fail_seconds": DEFAULTS.cooldown_after_fail_seconds,
        "max_fail_count_before_block": DEFAULTS.max_fail_count_before_block,
        "pipeline_timeout_seconds": DEFAULTS.pipeline_timeout_seconds,
        "auto_publish": DEFAULTS.auto_publish,
        "git_push": DEFAULTS.git_push,
        "fact_check_fail_ratio": DEFAULTS.fact_check_fail_ratio,
        "fact_check_revision_ratio": DEFAULTS.fact_check_revision_ratio,
        "fact_check_dead_link_tolerance": DEFAULTS.fact_check_dead_link_tolerance,
        "fact_check_relaxation_per_round": DEFAULTS.fact_check_relaxation_per_round,
        "max_revision_rounds": DEFAULTS.max_revision_rounds,
        "keyword_blocklist": list(DEFAULTS.keyword_blocklist),
        "sources_enabled": dict(DEFAULTS.sources_enabled),
        "video_generation_enabled": DEFAULTS.video_generation_enabled,
        "video_reference_voice_path": DEFAULTS.video_reference_voice_path,
        "video_target_duration_seconds": DEFAULTS.video_target_duration_seconds,
        "video_auto_upload": DEFAULTS.video_auto_upload,
        "youtube_default_privacy": DEFAULTS.youtube_default_privacy,
        "youtube_channel_name": DEFAULTS.youtube_channel_name,
        "youtube_upload_daily_cap": DEFAULTS.youtube_upload_daily_cap,
        "video_pipeline_timeout_seconds": DEFAULTS.video_pipeline_timeout_seconds,
        "video_max_retries": DEFAULTS.video_max_retries,
        "youtube_metadata_enabled": DEFAULTS.youtube_metadata_enabled,
        "youtube_captions_enabled": DEFAULTS.youtube_captions_enabled,
        "youtube_playlist_id": DEFAULTS.youtube_playlist_id,
        "cli_backend": DEFAULTS.cli_backend,
        "video_animation_enabled": DEFAULTS.video_animation_enabled,
        "video_animation_model": DEFAULTS.video_animation_model,
        "video_animation_duration_seconds": DEFAULTS.video_animation_duration_seconds,
        "video_animation_timeout_seconds": DEFAULTS.video_animation_timeout_seconds,
        "video_animation_width": DEFAULTS.video_animation_width,
        "video_animation_height": DEFAULTS.video_animation_height,
        "video_animation_fps": DEFAULTS.video_animation_fps,
        "video_animation_steps": DEFAULTS.video_animation_steps,
        "broadcast_hour_local": DEFAULTS.broadcast_hour_local,
        "broadcast_timezone": DEFAULTS.broadcast_timezone,
        "video_language": DEFAULTS.video_language,
        "topics_per_episode": DEFAULTS.topics_per_episode,
        "topics_freshness_hours": DEFAULTS.topics_freshness_hours,
    }


def seed_defaults_if_empty() -> None:
    """Insert default values for any missing keys."""
    with session_scope() as s:
        existing = {row.key for row in s.execute(select(Setting)).scalars().all()}
        for k, v in _defaults_as_dict().items():
            if k not in existing:
                s.add(Setting(key=k, value=json.dumps(v)))


def get_settings() -> RuntimeSettings:
    """Load current runtime settings (falls back to defaults per-key)."""
    defaults = _defaults_as_dict()
    with session_scope() as s:
        rows = s.execute(select(Setting)).scalars().all()
        values = dict(defaults)
        for row in rows:
            try:
                values[row.key] = json.loads(row.value)
            except json.JSONDecodeError:
                pass
    return RuntimeSettings(**{k: values[k] for k in defaults})


def set_setting(key: str, value: Any) -> None:
    encoded = json.dumps(value)
    with session_scope() as s:
        row = s.get(Setting, key)
        if row is None:
            s.add(Setting(key=key, value=encoded))
        else:
            row.value = encoded


def update_settings(patch: dict[str, Any]) -> RuntimeSettings:
    for k, v in patch.items():
        set_setting(k, v)
    return get_settings()
