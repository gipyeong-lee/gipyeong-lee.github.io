#!/usr/bin/env bash
# Uninstall the aiblog daemon from macOS launchd.

set -euo pipefail

LABEL="com.gipyeonglee.aiblog"
DEST="$HOME/Library/LaunchAgents/${LABEL}.plist"
UID_NUM="$(id -u)"
TARGET="gui/${UID_NUM}/${LABEL}"

if launchctl print "$TARGET" >/dev/null 2>&1; then
  echo "booting out $TARGET..."
  launchctl bootout "$TARGET" 2>/dev/null || true
else
  echo "(not currently loaded)"
fi

if [[ -f "$DEST" ]]; then
  rm -f "$DEST"
  echo "removed $DEST"
else
  echo "(plist already absent at $DEST)"
fi

echo "✓ uninstalled."
