#!/usr/bin/env bash
# Convert all JPGs in images/ to WebP (q80). Skips already-converted files.
# Run after the content pipeline adds new .jpg images so <picture> sources resolve.
# Requires: cwebp (brew install webp)
set -euo pipefail
cd "$(dirname "$0")/.."

command -v cwebp >/dev/null || { echo "cwebp not found. Run: brew install webp"; exit 1; }

n=0
for f in images/*.jpg; do
  [ -e "$f" ] || continue
  out="${f%.jpg}.webp"
  if [ ! -f "$out" ]; then
    cwebp -quiet -q 80 "$f" -o "$out"
    n=$((n+1))
  fi
done
echo "Converted $n new image(s). Total WebP: $(ls images/*.webp 2>/dev/null | wc -l | tr -d ' ')"
