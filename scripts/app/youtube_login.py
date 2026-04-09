"""One-shot YouTube OAuth login helper.

Run this once after placing `client_secrets.json` at
``~/.config/aiblog/client_secrets.json``::

    /usr/bin/python3 -m scripts.app.youtube_login

It opens a browser, asks the user to grant `youtube.upload` (and a few
related scopes the daemon also needs), then writes the refresh token to
``~/.config/aiblog/youtube_token.json``. Subsequent uploads from the
daemon are fully unattended — the daemon picks up that token, refreshes
it on demand, and only re-prompts if the user revokes consent.

Why this exists as a separate command:
- Google's OAuth 2.0 InstalledAppFlow requires *interactive* browser
  consent on the first run. There is no fully-automated alternative
  for desktop apps; that is by design.
- Running it from a one-shot CLI command lets the user complete the
  flow on their own schedule (and re-run after a token revocation),
  without having to wait for the daemon scheduler to fire.

Usage::

    /usr/bin/python3 -m scripts.app.youtube_login            # default scopes
    /usr/bin/python3 -m scripts.app.youtube_login --force    # re-prompt even if token exists
    /usr/bin/python3 -m scripts.app.youtube_login --revoke   # remove the saved token
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Scopes the daemon uses today: upload videos, read channel info, manage
# captions/playlists. We request them all at first login so refresh-token
# upgrades never silently fail when a new code path comes online.
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl",
]


def _config_dir() -> Path:
    return Path.home() / ".config" / "aiblog"


def _client_secrets_path() -> Path:
    return _config_dir() / "client_secrets.json"


def _token_path() -> Path:
    return _config_dir() / "youtube_token.json"


def _ensure_config_dir() -> None:
    d = _config_dir()
    d.mkdir(parents=True, exist_ok=True)


def revoke() -> int:
    token = _token_path()
    if not token.exists():
        print(f"No token to revoke at {token}")
        return 0
    token.unlink()
    print(f"Removed {token}")
    return 0


def login(force: bool = False) -> int:
    _ensure_config_dir()
    secrets = _client_secrets_path()
    token = _token_path()

    if not secrets.exists():
        print(f"client_secrets.json missing at {secrets}", file=sys.stderr)
        print(
            "  → Download an OAuth 2.0 Desktop client JSON from GCP and "
            "place it there. See docs/youtube_setup.md.",
            file=sys.stderr,
        )
        return 2

    if token.exists() and not force:
        print(f"Token already exists at {token}")
        print("Use --force to re-prompt, or --revoke to delete and start over.")
        return 0

    try:
        from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore
        from googleapiclient.discovery import build  # type: ignore
    except Exception as e:
        print(
            f"Missing google-auth-oauthlib / google-api-python-client: {e}",
            file=sys.stderr,
        )
        return 3

    flow = InstalledAppFlow.from_client_secrets_file(str(secrets), SCOPES)
    print("Starting local OAuth callback server…", flush=True)
    print(
        "If a browser does not open automatically, copy the URL printed "
        "below into your browser manually.",
        flush=True,
    )
    print("─" * 70, flush=True)
    creds = flow.run_local_server(
        port=0,
        prompt="consent",
        authorization_prompt_message=(
            "\n>>> OPEN THIS URL TO AUTHORIZE MindTickleBytes UPLOADS:\n\n  {url}\n"
        ),
        success_message=(
            "MindTickleBytes auth complete. You may close this tab and "
            "return to the terminal."
        ),
        open_browser=True,
    )

    token.parent.mkdir(parents=True, exist_ok=True)
    token.write_text(creds.to_json(), encoding="utf-8")
    try:
        os.chmod(token, 0o600)
    except OSError:
        pass
    print(f"Saved refresh token to {token}")

    # Verify by listing the user's channel — confirms the right Google
    # account is selected and that the channel actually exists.
    try:
        youtube = build("youtube", "v3", credentials=creds, cache_discovery=False)
        resp = (
            youtube.channels()
            .list(part="snippet,contentDetails", mine=True)
            .execute()
        )
        items = resp.get("items") or []
        if items:
            snip = items[0].get("snippet", {})
            title = snip.get("title", "(unknown)")
            cid = items[0].get("id", "(unknown)")
            print(f"Connected channel: {title}  (id={cid})")
        else:
            print("Warning: no channel found on this Google account.")
    except Exception as e:
        print(f"Channel verification call failed (non-fatal): {e}")

    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="YouTube OAuth login helper")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--force", action="store_true", help="Re-prompt even if a token already exists")
    g.add_argument("--revoke", action="store_true", help="Delete the saved token")
    args = ap.parse_args()

    if args.revoke:
        return revoke()
    return login(force=args.force)


if __name__ == "__main__":
    sys.exit(main())
