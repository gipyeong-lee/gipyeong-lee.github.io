"""Settings routes."""
from __future__ import annotations

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse

from ..settings_store import get_settings, update_settings

router = APIRouter(prefix="/settings")


@router.get("", response_class=HTMLResponse)
async def settings_page(request: Request) -> HTMLResponse:
    from ..main import templates

    s = get_settings()
    return templates.TemplateResponse(
        request,
        "settings.html",
        {
            "page": "settings",
            "settings": s,
        },
    )


@router.post("")
async def save_settings(
    min_interval_seconds: int = Form(...),
    max_interval_seconds: int = Form(...),
    event_trigger_threshold: float = Form(...),
    source_poll_interval_seconds: int = Form(...),
    cooldown_after_fail_seconds: int = Form(...),
    max_fail_count_before_block: int = Form(...),
    pipeline_timeout_seconds: int = Form(...),
    auto_publish: bool = Form(False),
    git_push: bool = Form(False),
    fact_check_fail_ratio: float = Form(...),
    fact_check_revision_ratio: float = Form(...),
    fact_check_dead_link_tolerance: int = Form(...),
    fact_check_relaxation_per_round: float = Form(...),
    max_revision_rounds: int = Form(...),
    keyword_blocklist: str = Form(""),
    sources_enabled_csv: str = Form(""),
    video_generation_enabled: bool = Form(False),
    video_reference_voice_path: str = Form(""),
    video_target_duration_seconds: int = Form(90),
    video_pipeline_timeout_seconds: int = Form(900),
    video_max_retries: int = Form(2),
    video_auto_upload: bool = Form(False),
    youtube_default_privacy: str = Form("unlisted"),
    youtube_upload_daily_cap: int = Form(5),
    youtube_channel_name: str = Form("Antigravity News"),
    youtube_metadata_enabled: bool = Form(False),
    youtube_captions_enabled: bool = Form(False),
    youtube_playlist_id: str = Form(""),
    cli_backend: str = Form("gemini"),
    video_animation_enabled: bool = Form(False),
    video_animation_duration_seconds: float = Form(5.0),
    video_animation_timeout_seconds: int = Form(600),
    video_animation_width: int = Form(1216),
    video_animation_height: int = Form(704),
    video_animation_fps: int = Form(24),
    video_animation_steps: int = Form(20),
) -> JSONResponse:
    # Parse blocklist: one keyword per line, or comma-separated
    bl = [kw.strip() for chunk in keyword_blocklist.split("\n") for kw in chunk.split(",") if kw.strip()]
    # Parse sources: "name=true,name=false,..."
    sources_enabled: dict[str, bool] = {}
    for pair in sources_enabled_csv.split(","):
        pair = pair.strip()
        if "=" in pair:
            k, v = pair.split("=", 1)
            sources_enabled[k.strip()] = v.strip().lower() in ("1", "true", "yes", "on")

    patch: dict = {
        "min_interval_seconds": min_interval_seconds,
        "max_interval_seconds": max_interval_seconds,
        "event_trigger_threshold": event_trigger_threshold,
        "source_poll_interval_seconds": source_poll_interval_seconds,
        "cooldown_after_fail_seconds": cooldown_after_fail_seconds,
        "max_fail_count_before_block": max_fail_count_before_block,
        "pipeline_timeout_seconds": pipeline_timeout_seconds,
        "auto_publish": bool(auto_publish),
        "git_push": bool(git_push),
        "fact_check_fail_ratio": fact_check_fail_ratio,
        "fact_check_revision_ratio": fact_check_revision_ratio,
        "fact_check_dead_link_tolerance": fact_check_dead_link_tolerance,
        "fact_check_relaxation_per_round": fact_check_relaxation_per_round,
        "max_revision_rounds": max_revision_rounds,
        "keyword_blocklist": bl,
        "video_generation_enabled": bool(video_generation_enabled),
        "video_reference_voice_path": video_reference_voice_path.strip(),
        "video_target_duration_seconds": video_target_duration_seconds,
        "video_pipeline_timeout_seconds": video_pipeline_timeout_seconds,
        "video_max_retries": video_max_retries,
        "video_auto_upload": bool(video_auto_upload),
        "youtube_default_privacy": youtube_default_privacy,
        "youtube_upload_daily_cap": youtube_upload_daily_cap,
        "youtube_channel_name": youtube_channel_name,
        "youtube_metadata_enabled": bool(youtube_metadata_enabled),
        "youtube_captions_enabled": bool(youtube_captions_enabled),
        "youtube_playlist_id": youtube_playlist_id.strip(),
        "cli_backend": cli_backend.strip() or "gemini",
        "video_animation_enabled": bool(video_animation_enabled),
        "video_animation_duration_seconds": float(video_animation_duration_seconds),
        "video_animation_timeout_seconds": int(video_animation_timeout_seconds),
        "video_animation_width": int(video_animation_width),
        "video_animation_height": int(video_animation_height),
        "video_animation_fps": int(video_animation_fps),
        "video_animation_steps": int(video_animation_steps),
    }
    if sources_enabled:
        patch["sources_enabled"] = sources_enabled

    updated = update_settings(patch)
    return JSONResponse({"status": "saved", "settings": updated.__dict__})
