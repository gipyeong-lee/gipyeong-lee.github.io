"""YouTube Uploader Agent — resumable video.insert via Google API.

OAuth 2.0 Desktop flow. On first call, opens a browser tab; subsequent
runs reuse the refresh token persisted at
`~/.config/aiblog/youtube_token.json`.

Configuration (all paths configured in scripts/app/config.py):
    YOUTUBE_CLIENT_SECRETS → desktop OAuth client json from GCP console
    YOUTUBE_TOKEN_PATH     → auto-managed, holds refresh token
    AIBLOG_CONFIG_DIR      → parent dir for both

See `docs/youtube_setup.md` for the 6-step GCP console walkthrough.
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .base import BaseAgent

# Module-level so tests can patch without pulling google-auth-oauthlib into
# test environments that don't need it.
_YOUTUBE_SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
_CATEGORY_SCIENCE_TECH = "28"


@dataclass
class UploadResult:
    video_id: str
    url: str
    privacy: str


class YouTubeUploaderAgent(BaseAgent):
    """Upload a local mp4 to YouTube with OAuth2 desktop flow."""

    name = "YouTubeUploader"
    prompt_file = ""

    def __init__(
        self,
        client_secrets_path: str | Path | None = None,
        token_path: str | Path | None = None,
    ):
        super().__init__()
        from ..app.config import YOUTUBE_CLIENT_SECRETS, YOUTUBE_TOKEN_PATH

        self.client_secrets_path = Path(
            client_secrets_path or YOUTUBE_CLIENT_SECRETS
        )
        self.token_path = Path(token_path or YOUTUBE_TOKEN_PATH)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def run(
        self,
        *,
        mp4_path: str | Path,
        title: str,
        description: str,
        tags: list[str] | None = None,
        privacy: str = "unlisted",
        thumbnail_path: str | Path | None = None,
        made_for_kids: bool = False,
    ) -> Optional[UploadResult]:
        mp4 = Path(mp4_path)
        if not mp4.exists():
            self.log(f"mp4 not found: {mp4}")
            return None
        if not self.client_secrets_path.exists():
            self.log(
                f"OAuth client_secrets.json not at {self.client_secrets_path}. "
                "See docs/youtube_setup.md to complete GCP setup."
            )
            return None

        try:
            youtube = self._build_service()
        except Exception as e:
            self.log(f"OAuth / service build failed: {e}")
            return None

        body = {
            "snippet": {
                "title": title[:100],
                "description": description[:4500],
                "tags": (tags or [])[:30],
                "categoryId": _CATEGORY_SCIENCE_TECH,
                "defaultLanguage": "ko",
                "defaultAudioLanguage": "ko",
            },
            "status": {
                "privacyStatus": privacy if privacy in ("public", "unlisted", "private") else "unlisted",
                "selfDeclaredMadeForKids": bool(made_for_kids),
            },
        }

        try:
            video_id = self._resumable_insert(youtube, mp4, body)
        except Exception as e:
            self.log(f"Upload failed: {e}")
            return None
        if not video_id:
            return None

        if thumbnail_path:
            try:
                self._set_thumbnail(youtube, video_id, Path(thumbnail_path))
            except Exception as e:
                self.log(f"Thumbnail upload failed (non-fatal): {e}")

        url = f"https://youtu.be/{video_id}"
        self.log(f"Uploaded: {url} (privacy={privacy})")
        return UploadResult(video_id=video_id, url=url, privacy=privacy)

    def upload_captions(
        self,
        video_id: str,
        srt_path: str | Path,
        *,
        language: str = "ko",
        name: str = "한국어 (자동)",
    ) -> bool:
        """Upload an SRT file as a YouTube caption track for `video_id`."""
        path = Path(srt_path)
        if not path.exists() or path.stat().st_size < 30:
            self.log(f"captions file missing/tiny: {path}")
            return False
        try:
            from googleapiclient.http import MediaFileUpload

            youtube = self._build_service()
            body = {
                "snippet": {
                    "videoId": video_id,
                    "language": language,
                    "name": name,
                    "isDraft": False,
                }
            }
            media = MediaFileUpload(
                str(path),
                mimetype="application/octet-stream",
                resumable=False,
            )
            youtube.captions().insert(
                part="snippet",
                body=body,
                media_body=media,
            ).execute()
            self.log(f"captions uploaded for {video_id}")
            return True
        except Exception as e:
            self.log(f"captions upload failed (non-fatal): {e}")
            return False

    def add_to_playlist(self, video_id: str, playlist_id: str) -> bool:
        """Append `video_id` to `playlist_id`."""
        if not playlist_id:
            return False
        try:
            youtube = self._build_service()
            youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video_id,
                        },
                    }
                },
            ).execute()
            self.log(f"video {video_id} added to playlist {playlist_id}")
            return True
        except Exception as e:
            self.log(f"playlist append failed (non-fatal): {e}")
            return False

    def update_privacy(self, video_id: str, privacy: str) -> bool:
        """Promote an already-uploaded video (unlisted → public, etc.)."""
        if privacy not in ("public", "unlisted", "private"):
            self.log(f"Invalid privacy: {privacy}")
            return False
        try:
            youtube = self._build_service()
            youtube.videos().update(
                part="status",
                body={
                    "id": video_id,
                    "status": {"privacyStatus": privacy},
                },
            ).execute()
            self.log(f"Video {video_id} privacy → {privacy}")
            return True
        except Exception as e:
            self.log(f"privacy update failed: {e}")
            return False

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    def _build_service(self):
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build

        creds: Credentials | None = None
        if self.token_path.exists():
            try:
                creds = Credentials.from_authorized_user_file(
                    str(self.token_path), _YOUTUBE_SCOPES
                )
            except Exception as e:
                self.log(f"token load failed, re-authing: {e}")
                creds = None

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        if not creds or not creds.valid:
            self.log("Starting OAuth desktop flow (browser will open)…")
            flow = InstalledAppFlow.from_client_secrets_file(
                str(self.client_secrets_path), _YOUTUBE_SCOPES
            )
            creds = flow.run_local_server(port=0)

        self.token_path.parent.mkdir(parents=True, exist_ok=True)
        self.token_path.write_text(creds.to_json(), encoding="utf-8")

        return build("youtube", "v3", credentials=creds, cache_discovery=False)

    def _resumable_insert(self, youtube, mp4_path: Path, body: dict) -> Optional[str]:
        from googleapiclient.http import MediaFileUpload

        media = MediaFileUpload(
            str(mp4_path),
            chunksize=8 * 1024 * 1024,  # 8MB chunks for resumable progress
            resumable=True,
            mimetype="video/mp4",
        )
        request = youtube.videos().insert(
            part=",".join(body.keys()),
            body=body,
            media_body=media,
        )

        response = None
        retries = 0
        max_retries = 5
        while response is None:
            try:
                status, response = request.next_chunk()
                if status:
                    pct = int(status.progress() * 100)
                    self.log(f"upload progress: {pct}%")
            except Exception as e:
                retries += 1
                if retries > max_retries:
                    self.log(f"resumable upload giving up after {retries} retries: {e}")
                    return None
                delay = 2 ** retries
                self.log(f"transient upload error ({e}); retry {retries} in {delay}s")
                time.sleep(delay)

        return response.get("id") if isinstance(response, dict) else None

    def _set_thumbnail(self, youtube, video_id: str, thumb_path: Path) -> None:
        from googleapiclient.http import MediaFileUpload

        if not thumb_path.exists() or thumb_path.stat().st_size < 2000:
            return
        youtube.thumbnails().set(
            videoId=video_id,
            media_body=MediaFileUpload(
                str(thumb_path),
                mimetype="image/jpeg",
                resumable=False,
            ),
        ).execute()
        self.log(f"Thumbnail set for {video_id}")
