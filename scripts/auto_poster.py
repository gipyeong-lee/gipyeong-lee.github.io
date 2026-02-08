#!/usr/bin/env python3
"""Fact-checked multilingual blog post generator.

Usage:
    # Auto mode: select topic from Google Trends
    python3 scripts/auto_poster.py

    # Manual mode: specify topic
    python3 scripts/auto_poster.py --topic "Kubernetes 보안"

    # Alternative: run as module
    python3 -m scripts.auto_poster --topic "Kubernetes 보안"
"""

import argparse
import csv
import datetime
import os
import sys

# Ensure project root is on sys.path for both direct and module execution
_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

import feedparser

# --- Configuration ---
GOOGLE_TRENDS_RSS_KR = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=KR"
HISTORY_FILE = "scripts/history.csv"


def get_hot_keywords():
    """Fetches trending keywords from Google Trends RSS."""
    print("Parsing Google Trends RSS...")
    feed = feedparser.parse(GOOGLE_TRENDS_RSS_KR)
    keywords = []
    for entry in feed.entries[:5]:
        keywords.append(entry.title)
    return keywords


def load_history():
    """Loads used keywords from history.csv."""
    used_keywords = set()
    if not os.path.exists(HISTORY_FILE):
        return used_keywords

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "keyword" in row:
                    used_keywords.add(row["keyword"])
    except Exception as e:
        print(f"Error loading history: {e}")
    return used_keywords


def append_history(keyword):
    """Appends a new keyword to history.csv."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    is_new_file = not os.path.exists(HISTORY_FILE)

    try:
        with open(HISTORY_FILE, "a", encoding="utf-8", newline="") as f:
            fieldnames = ["date", "keyword"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            if is_new_file:
                writer.writeheader()

            writer.writerow({"date": today, "keyword": keyword})
        print(f"Added '{keyword}' to history.")
    except Exception as e:
        print(f"Error appending history: {e}")


def select_topic_from_trends():
    """Select a fresh topic from Google Trends."""
    keywords = get_hot_keywords()
    if not keywords:
        print("No keywords found from Google Trends.")
        return None

    print(f"Top keywords: {keywords}")
    used_keywords = load_history()

    for kw in keywords:
        if kw in used_keywords:
            print(f"  Skipping (already used): {kw}")
            continue
        return kw

    print("All top keywords have already been covered.")
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Generate a fact-checked multilingual blog post."
    )
    parser.add_argument(
        "--topic",
        type=str,
        default=None,
        help="Topic to write about. If omitted, selects from Google Trends.",
    )
    args = parser.parse_args()

    # Select topic
    if args.topic:
        topic = args.topic
        print(f"Manual topic: {topic}")
    else:
        topic = select_topic_from_trends()
        if not topic:
            return

    print(f"\nSelected topic: {topic}\n")

    # Run pipeline
    from scripts.pipeline import Pipeline

    pipeline = Pipeline()
    success = pipeline.run(topic)

    if success:
        append_history(topic)
        print("\nDone! Check the _posts directory for KO, EN, JA versions.")
    else:
        print("\nPipeline failed. No posts were saved.")
        sys.exit(1)


if __name__ == "__main__":
    main()
