"""One-shot migration: scripts/history.csv → post_history table.

Also scans _posts/ to populate post_history entries for any Jekyll posts
that exist on disk but aren't in history.csv (so the dashboard's "total
posts" counter is accurate from day one).

Run with:  python -m scripts.app.history_import
"""
from __future__ import annotations

import csv
import json
import re
from datetime import datetime
from pathlib import Path

from sqlalchemy import select

from .config import POSTS_DIR, SCRIPTS_DIR
from .db import init_db, session_scope
from .models_db import PostHistory

HISTORY_CSV = SCRIPTS_DIR / "history.csv"

_FILENAME_RE = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.+?)(?:\.(?P<lang>[a-z-]+))?\.md$"
)
_KNOWN_LANGS = {"ko", "en", "ja", "zh-cn", "zh-tw"}


def _scan_posts() -> dict[str, dict]:
    """Group _posts/ files by (date, slug). Returns {slug_date: entry}."""
    by_ref: dict[str, dict] = {}
    posts = Path(POSTS_DIR)
    if not posts.exists():
        return by_ref
    for p in posts.iterdir():
        if not p.is_file() or p.suffix != ".md":
            continue
        m = _FILENAME_RE.match(p.name)
        if not m:
            continue
        date_str = m.group("date")
        slug = m.group("slug")
        lang = m.group("lang")
        if lang is None:
            lang = "ko"
        if lang not in _KNOWN_LANGS:
            # e.g. "markdown" extra suffixes -> treat as ko
            lang = "ko"
        ref = f"{date_str}-{slug}"
        entry = by_ref.setdefault(
            ref,
            {
                "slug": ref,
                "date": date_str,
                "languages": set(),
                "title": None,
            },
        )
        entry["languages"].add(lang)
        # best-effort title extraction (first file we hit)
        if entry["title"] is None:
            try:
                with p.open("r", encoding="utf-8") as f:
                    head = f.read(2048)
                mt = re.search(r'^title:\s*"?(.*?)"?\s*$', head, re.MULTILINE)
                if mt:
                    entry["title"] = mt.group(1).strip()
            except Exception:
                pass
    return by_ref


def _load_history_csv() -> list[tuple[str, str]]:
    """Return [(date, topic), ...] from history.csv."""
    out: list[tuple[str, str]] = []
    if not HISTORY_CSV.exists():
        return out
    try:
        with HISTORY_CSV.open("r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0 and row and row[0].lower() in ("date", "published_at"):
                    continue
                if len(row) >= 2:
                    out.append((row[0].strip(), row[1].strip()))
    except Exception as e:
        print(f"warn: history.csv parse failed: {e}")
    return out


def run() -> dict:
    init_db()
    scanned = _scan_posts()
    csv_rows = _load_history_csv()

    # Build topic-lookup: newest csv date -> topic
    topic_by_date: dict[str, str] = {}
    for date_str, topic in csv_rows:
        topic_by_date[date_str] = topic

    imported = 0
    skipped = 0
    with session_scope() as s:
        existing = {
            row[0] for row in s.execute(select(PostHistory.slug)).all()
        }

        for ref, entry in scanned.items():
            if ref in existing:
                skipped += 1
                continue
            date_str = entry["date"]
            try:
                pub_dt = datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                continue
            topic = topic_by_date.get(date_str) or entry["title"] or ref
            s.add(
                PostHistory(
                    slug=ref,
                    title=entry["title"],
                    topic=topic,
                    published_at=pub_dt,
                    run_id=None,
                    git_commit_sha=None,
                    languages=json.dumps(sorted(entry["languages"])),
                )
            )
            imported += 1

    return {
        "scanned_posts": len(scanned),
        "csv_rows": len(csv_rows),
        "imported": imported,
        "skipped_existing": skipped,
    }


if __name__ == "__main__":
    result = run()
    print("history_import complete:")
    for k, v in result.items():
        print(f"  {k}: {v}")
