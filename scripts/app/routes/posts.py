"""Posts listing + delete + regenerate routes."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import delete, select

from ..config import IMAGES_DIR, POSTS_DIR, REPO_ROOT
from ..db import session_scope
from ..models_db import PostHistory

router = APIRouter(prefix="/posts")

_FILENAME_RE = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.+?)(?:\.(?P<lang>[a-z-]+))?\.md$"
)
_KNOWN_LANGS = {"ko", "en", "ja", "zh-cn", "zh-tw"}


def _scan_posts() -> list[dict]:
    by_ref: dict[str, dict] = {}
    posts = Path(POSTS_DIR)
    if not posts.exists():
        return []
    for p in posts.iterdir():
        if not p.is_file() or p.suffix != ".md":
            continue
        m = _FILENAME_RE.match(p.name)
        if not m:
            continue
        date_str = m.group("date")
        slug = m.group("slug")
        lang = m.group("lang") or "ko"
        if lang not in _KNOWN_LANGS:
            lang = "ko"
        ref = f"{date_str}-{slug}"
        entry = by_ref.setdefault(
            ref,
            {
                "ref": ref,
                "date": date_str,
                "slug": slug,
                "languages": set(),
                "title": None,
                "image": None,
            },
        )
        entry["languages"].add(lang)
        if lang == "ko" and entry["title"] is None:
            try:
                with p.open("r", encoding="utf-8") as f:
                    head = f.read(2048)
                tm = re.search(r'^title:\s*"?(.*?)"?\s*$', head, re.MULTILINE)
                if tm:
                    entry["title"] = tm.group(1).strip()
                im = re.search(r'^image:\s*(\S+)\s*$', head, re.MULTILINE)
                if im:
                    entry["image"] = im.group(1).strip()
            except Exception:
                pass
    return sorted(
        (
            {**v, "languages": sorted(v["languages"])}
            for v in by_ref.values()
        ),
        key=lambda x: x["date"],
        reverse=True,
    )


@router.get("", response_class=HTMLResponse)
async def list_posts(request: Request) -> HTMLResponse:
    from ..main import templates

    posts = _scan_posts()
    return templates.TemplateResponse(
        request,
        "posts.html",
        {"page": "posts", "posts": posts},
    )


def _gather_files(ref: str) -> tuple[list[Path], Path | None]:
    posts = Path(POSTS_DIR)
    files: list[Path] = []
    for p in posts.iterdir():
        if p.name.startswith(ref) and p.suffix == ".md":
            files.append(p)
    img: Path | None = None
    for ext in ("jpg", "jpeg", "png", "webp"):
        candidate = Path(IMAGES_DIR) / f"{ref}.{ext}"
        if candidate.exists():
            img = candidate
            break
    return files, img


@router.delete("/{ref}")
async def delete_post(ref: str) -> JSONResponse:
    files, img = _gather_files(ref)
    if not files:
        raise HTTPException(status_code=404, detail="post not found")

    for f in files:
        try:
            f.unlink()
        except FileNotFoundError:
            pass
    if img is not None:
        try:
            img.unlink()
        except FileNotFoundError:
            pass

    # Record removal as a git commit
    paths = [str(f.relative_to(REPO_ROOT)) for f in files]
    if img is not None:
        paths.append(str(img.relative_to(REPO_ROOT)))
    try:
        subprocess.run(["git", "add", *paths], cwd=REPO_ROOT, check=True)
        subprocess.run(
            ["git", "commit", "-m", f"revert: remove {ref} via admin"],
            cwd=REPO_ROOT,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        return JSONResponse(
            {"status": "files_removed_commit_failed", "error": str(e)},
            status_code=500,
        )

    with session_scope() as s:
        s.execute(delete(PostHistory).where(PostHistory.slug == ref))

    return JSONResponse({"status": "deleted", "ref": ref})
