#!/usr/bin/env bash
# Install aiblog daemon into macOS launchd.
#
# Usage: ./launchd/install.sh [path/to/python]
#
# Defaults to `which python3`. The script renders the plist template,
# places it in ~/Library/LaunchAgents/, and bootstraps it into the
# user's GUI launchd domain so it auto-starts on login.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TEMPLATE="$SCRIPT_DIR/com.gipyeonglee.aiblog.plist.template"
LABEL="com.gipyeonglee.aiblog"
DEST="$HOME/Library/LaunchAgents/${LABEL}.plist"

if [[ ! -f "$TEMPLATE" ]]; then
  echo "error: template missing at $TEMPLATE" >&2
  exit 1
fi

PYTHON_BIN="${1:-}"
if [[ -z "$PYTHON_BIN" ]]; then
  if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v python3)"
  else
    echo "error: python3 not found. Pass an explicit path as the first argument." >&2
    exit 1
  fi
fi

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "error: $PYTHON_BIN is not executable" >&2
  exit 1
fi

echo "repo root:   $REPO_ROOT"
echo "python:      $PYTHON_BIN"
echo "plist dest:  $DEST"

# Ensure data dir exists so launchd can write the log files
mkdir -p "$REPO_ROOT/scripts/app/data"

# Render template
mkdir -p "$(dirname "$DEST")"
sed -e "s|{{PYTHON}}|${PYTHON_BIN}|g" \
    -e "s|{{REPO_ROOT}}|${REPO_ROOT}|g" \
    "$TEMPLATE" > "$DEST"

echo "plist rendered."

# Verify syntactically
if command -v plutil >/dev/null 2>&1; then
  plutil -lint "$DEST"
fi

# Bootstrap into user's GUI domain
UID_NUM="$(id -u)"
TARGET="gui/${UID_NUM}/${LABEL}"

# Bootout first (idempotent — ignore errors if not loaded)
launchctl bootout "$TARGET" 2>/dev/null || true
launchctl bootstrap "gui/${UID_NUM}" "$DEST"

echo "launchd bootstrapped. Status:"
launchctl list "$LABEL" 2>/dev/null || echo "  (not yet visible — may take a few seconds)"

echo ""
echo "✓ installed. Open http://127.0.0.1:7001 in your browser."
echo "  Logs: $REPO_ROOT/scripts/app/data/daemon.{out,err}.log"
echo "  Uninstall: ./launchd/uninstall.sh"
