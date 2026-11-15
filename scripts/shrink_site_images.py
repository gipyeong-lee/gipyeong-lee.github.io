#!/usr/bin/env python3
"""Shrink the built site's hero images before the Pages artifact is made.

Usage: python3 scripts/shrink_site_images.py _site

Why: the Pages artifact reached 997 MB on 2026-11-15, 93% of the 1 GiB that
actions/deploy-pages accepts, and each post added ~0.38 MB, so the limit was
two weeks away. Three quarters of it was images/: every post ships a
1600x900 hero as a q85 jpg (~197 KB) plus a q82 webp sibling (~110 KB). The
content pipeline renders those heroes at 1024x576 (SDXL-Turbo) and only
upscales them to 1600x900, so the extra pixels carry little detail.

What it does, in place, to <site>/images (top level only, so the Blog
section's images/blog/<slug>/ files and other subfolders are untouched):

* a jpg wider than 1200 px is resized to 1200 px wide (aspect kept) and saved
  as a q82 progressive jpg. 1200 px is the floor because og:image,
  twitter:image and the Article schema point at this file, and Google
  Discover only shows large previews for images at least 1200 px wide.
* the webp sibling of every jpg is deleted; the templates no longer
  reference webp (scripts/tests/test_image_budget_contract.py).

Measured 2026-11-15 on 96 heroes sampled across every month (ssimulacra2 at
1600x900, against the committed jpg; 70 = high, 80 = very high): 1200 px q82
progressive jpg 112.5 KB, score 74.7, versus 108 KB / 75.4 for the q82 webp
that <picture> served until then. On the whole corpus the heroes went from
772 MB (jpg + webp) to 291 MB; webp at 1200 px q86 next to the jpg would have
kept 520 MB.

git keeps the pipeline's originals: the repository is already ~5 GB and the
video pipeline reads the heroes from images/. Re-encoding every build costs
~25 ms of CPU per image; caching the output would mean saving ~290 MB of
cache on every post, which costs about as much as it saves.

A jpg that cannot be processed is left as it is, with a warning annotation.
More than 1% of them failing exits non-zero instead of silently deploying
full-size images.
"""
from __future__ import annotations

import io
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

MAX_WIDTH = 1200
QUALITY = 82
MAX_FAILURE_RATIO = 0.01


def shrink_jpeg(path: Path) -> tuple[int, int, str]:
    """Shrink one jpg in place; return (bytes before, bytes after, status)."""
    from PIL import Image, ImageOps

    before = path.stat().st_size
    with Image.open(path) as source:
        icc_profile = source.info.get("icc_profile")
        # EXIF orientation is not copied to the output, so bake it in first.
        image = ImageOps.exif_transpose(source)
        width, height = image.size
        if width <= MAX_WIDTH:
            return before, before, "small"
        if image.mode not in ("RGB", "L"):
            image = image.convert("RGB")
        resized = image.resize((MAX_WIDTH, round(height * MAX_WIDTH / width)), Image.LANCZOS)
    buffer = io.BytesIO()
    options = {"quality": QUALITY, "optimize": True, "progressive": True}
    if icc_profile:
        options["icc_profile"] = icc_profile
    resized.save(buffer, "JPEG", **options)
    data = buffer.getvalue()
    if len(data) >= before:
        return before, before, "kept-larger"
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(data)
    os.replace(temporary, path)
    return before, len(data), "shrunk"


def _shrink_or_report(path: Path) -> tuple[int, int, str]:
    try:
        return shrink_jpeg(path)
    except Exception as error:  # a bad file must not stop the other 2,500
        size = path.stat().st_size
        return size, size, f"error: {type(error).__name__}: {error}"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.splitlines()[2], file=sys.stderr)
        return 2
    images = Path(argv[1]) / "images"
    if not images.is_dir():
        print(f"{images} not found", file=sys.stderr)
        return 2
    import PIL  # fail the step loudly when Pillow is missing  # noqa: F401

    jpegs = sorted(p for p in images.iterdir() if p.is_file() and p.suffix.lower() == ".jpg")
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as pool:
        results = list(pool.map(_shrink_or_report, jpegs, chunksize=32))

    counts: dict[str, int] = {}
    failures = []
    for path, (_, _, status) in zip(jpegs, results):
        if status.startswith("error"):
            failures.append(path)
            print(f"::warning file={path}::kept unshrunk ({status})")
            status = "error"
        counts[status] = counts.get(status, 0) + 1
    jpg_before = sum(before for before, _, _ in results)
    jpg_after = sum(after for _, after, _ in results)

    webp_removed = 0
    webp_bytes = 0
    for path in jpegs:
        sibling = path.with_suffix(".webp")
        if sibling.is_file():
            webp_bytes += sibling.stat().st_size
            sibling.unlink()
            webp_removed += 1

    summary = (
        f"Hero images: {len(jpegs)} jpg {jpg_before / 1e6:.1f} MB -> {jpg_after / 1e6:.1f} MB "
        f"({', '.join(f'{k} {v}' for k, v in sorted(counts.items()))}); "
        f"removed {webp_removed} webp ({webp_bytes / 1e6:.1f} MB)"
    )
    print(summary)
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as handle:
            handle.write(summary + "\n")
    if failures and len(failures) > MAX_FAILURE_RATIO * len(jpegs):
        print(f"{len(failures)} of {len(jpegs)} jpg failed to shrink", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
