#!/usr/bin/env python3
"""Import selected posts from the legacy HTML export into the Jekyll blog."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


LONG_POST_LIMIT = 1000
CONTENT_CLASS = "contents_style"
SKIP_TAGS = {"script", "style"}
ALLOWED_ATTRIBUTES = {
    "alt",
    "allowfullscreen",
    "class",
    "frameborder",
    "height",
    "href",
    "loading",
    "rel",
    "src",
    "target",
    "title",
    "width",
}


@dataclass
class SourcePost:
    source_path: Path
    source_id: str
    title: str
    date: str
    category: str
    tags: list[str]
    body: str
    body_text: str
    source_links: list[str] = field(default_factory=list)


@dataclass
class ConversionResult:
    post_path: Path | None
    body: str
    slug: str
    missing_images: list[str] = field(default_factory=list)
    copied_images: list[str] = field(default_factory=list)
    external_images: list[str] = field(default_factory=list)


class SourceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title: list[str] = []
        self.category: list[str] = []
        self.date: list[str] = []
        self.tags: list[str] = []
        self.body: list[str] = []
        self.body_text: list[str] = []
        self.source_links: list[str] = []
        self.capture: str | None = None
        self.content_depth = 0
        self.skip_depth = 0
        self.link_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        classes = set((attr_map.get("class") or "").split())

        if tag == "title":
            self.capture = "title"
        elif tag == "p" and "category" in classes:
            self.capture = "category"
        elif tag == "p" and "date" in classes:
            self.capture = "date"
        elif tag in {"div", "p"} and "tags" in classes:
            self.capture = "tags"
        elif tag == "a" and attr_map.get("href"):
            self.source_links.append(attr_map["href"] or "")

        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return

        if self.content_depth and tag == "div":
            self.content_depth += 1
        elif tag == "div" and CONTENT_CLASS in classes:
            self.content_depth = 1
            return

        if self.content_depth:
            self.body.append(serialize_start_tag(tag, attrs))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in SKIP_TAGS and tag not in {"area", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            if self.content_depth:
                self.body.append(f"</{tag}>")

    def handle_endtag(self, tag: str) -> None:
        if tag in SKIP_TAGS:
            if self.skip_depth:
                self.skip_depth -= 1
            return

        if self.capture and tag in {"title", "p", "div"}:
            self.capture = None

        if self.content_depth:
            if tag == "div":
                self.content_depth -= 1
                if self.content_depth == 0:
                    return
            self.body.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if self.capture == "title":
            self.title.append(data)
        elif self.capture == "category":
            self.category.append(data)
        elif self.capture == "date":
            self.date.append(data)
        elif self.capture == "tags":
            self.tags.append(data)
        if self.content_depth:
            self.body.append(html.escape(data, quote=False))
            self.body_text.append(f" {data} ")


class BodySanitizer(HTMLParser):
    def __init__(self, post: SourcePost, repo_root: Path, slug: str, copy_assets: bool) -> None:
        super().__init__(convert_charrefs=True)
        self.post = post
        self.repo_root = repo_root
        self.slug = slug
        self.output: list[str] = []
        self.missing_images: list[str] = []
        self.copied_images: list[str] = []
        self.external_images: list[str] = []
        self.copy_assets = copy_assets
        self.skip_depth = 0
        self.asset_dir = repo_root / "images" / "blog" / slug

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        attr_map = dict(attrs)
        if tag == "img":
            src = attr_map.get("src") or ""
            if is_external_url(src) or src.startswith("data:"):
                if is_external_url(src):
                    self.external_images.append(src)
                self.output.append(serialize_start_tag(tag, ensure_alt(attrs, src)))
                return
            if src.startswith("/"):
                existing_asset = (self.repo_root / src.lstrip("/")).resolve()
                if existing_asset.is_file():
                    rewritten = [(key, value) for key, value in attrs if key != "src"]
                    rewritten.append(("src", f"{{{{ site.baseurl }}}}{src}"))
                    self.output.append(serialize_start_tag(tag, ensure_alt(rewritten, src)))
                    return
            source_file = (self.post.source_path.parent / unquote(src)).resolve()
            if not source_file.is_file():
                self.missing_images.append(src)
                return
            asset_name = safe_filename(source_file.name)
            destination = self.asset_dir / asset_name
            if self.copy_assets:
                self.asset_dir.mkdir(parents=True, exist_ok=True)
                if not destination.exists():
                    shutil.copy2(source_file, destination)
            self.copied_images.append(str(destination.relative_to(self.repo_root)))
            public_src = f"{{{{ site.baseurl }}}}/images/blog/{self.slug}/{asset_name}"
            rewritten = [(key, value) for key, value in attrs if key != "src"]
            rewritten.append(("src", public_src))
            self.output.append(serialize_start_tag(tag, ensure_alt(rewritten, asset_name)))
            return
        self.output.append(serialize_start_tag(tag, attrs))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in SKIP_TAGS and tag not in {"area", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.output.append(f"</{tag}>")

    def handle_endtag(self, tag: str) -> None:
        if tag in SKIP_TAGS:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        if not self.skip_depth:
            self.output.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.output.append(html.escape(data, quote=False))


def serialize_start_tag(tag: str, attrs: list[tuple[str, str | None]]) -> str:
    kept: list[str] = []
    for key, value in attrs:
        key = key.lower()
        if key not in ALLOWED_ATTRIBUTES or key.startswith("data-"):
            continue
        if value is None:
            kept.append(key)
        else:
            kept.append(f'{key}="{html.escape(value, quote=True)}"')
    suffix = f" {' '.join(kept)}" if kept else ""
    return f"<{tag}{suffix}>"


def ensure_alt(attrs: list[tuple[str, str | None]], fallback: str) -> list[tuple[str, str | None]]:
    if any(key.lower() == "alt" and value for key, value in attrs):
        return attrs
    alt = Path(unquote(urlparse(fallback).path).split("/")[-1]).stem
    alt = re.sub(r"[_-]+", " ", alt).strip() or "이미지"
    return [(key, value) for key, value in attrs if key.lower() != "alt"] + [("alt", alt)]


def is_external_url(value: str) -> bool:
    parsed = urlparse(value)
    return bool(parsed.scheme or value.startswith("//"))


def visible_char_count(text: str) -> int:
    return len("".join(text.split()))


def parse_source(path: Path) -> SourcePost:
    parser = SourceParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    title = normalize_text("".join(parser.title)) or path.stem
    category = normalize_text("".join(parser.category))
    date = parse_date("".join(parser.date))
    tags = parse_tags("".join(parser.tags))
    return SourcePost(
        source_path=path,
        source_id=path.parent.name,
        title=title,
        date=date,
        category=category,
        tags=tags,
        body="".join(parser.body).strip(),
        body_text=normalize_text("".join(parser.body_text)),
        source_links=parser.source_links,
    )


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def parse_date(value: str) -> str:
    value = normalize_text(value)
    try:
        return datetime.strptime(value[:19], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return "2000-01-01 00:00:00"


def parse_tags(value: str) -> list[str]:
    return unique([tag.strip(" #") for tag in re.findall(r"#[^#\s]+", value)])


def should_import(post: SourcePost) -> bool:
    return category_for(post) == "books" or visible_char_count(post.body_text) > LONG_POST_LIMIT


def category_for(post: SourcePost) -> str:
    source = post.category.lower()
    title = post.title.lower()
    if post.category == "Etc/독서" or any(token in title for token in ("반야심경", "니체", "쇼펜하우어", "독서", "독후", "서평")):
        return "books"
    if source.startswith("dapp/") or any(token in title for token in ("stepn", "ethereum", "dapp", "bee coin")):
        return "web3"
    if "pbr" in title or "pine script" in title or "주가" in title or "투자" in title:
        return "finance"
    if source.startswith("projects/"):
        return "projects"
    if source in {"etc/제주살이", "etc/건축"}:
        return "life"
    if source.startswith("computer/") or source in {"etc/scrap", "computer"}:
        return "engineering"
    if source in {"etc/생각", "etc/경험담", "etc/시", "etc/자작시"}:
        return "essay"
    return "essay"


def tags_for(post: SourcePost, category: str) -> list[str]:
    tags = list(post.tags)
    if post.category and post.category not in tags:
        tags.append(post.category.split("/")[-1])
    if category not in tags:
        tags.append(category)
    return unique([tag for tag in tags if tag])[:6]


def description_for(post: SourcePost) -> str:
    text = normalize_text(post.body_text)
    if not text:
        return post.title[:157] + ("..." if len(post.title) > 157 else "")
    description = text[:157].rstrip()
    if len(text) > 157:
        description += "..."
    return description[:160]


def slug_for(post: SourcePost, category: str) -> str:
    title_slug = slugify(post.title) or "post"
    suffix = f"legacy-{post.source_id}-{category}"
    if title_slug != "post":
        suffix = f"{suffix}-{title_slug}"
    return f"{post.date[:10]}-{suffix}"[:180].rstrip("-")


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def safe_filename(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    suffix = Path(value).suffix.lower()
    stem = re.sub(r"[^\w.-]+", "-", Path(value).stem, flags=re.UNICODE).strip("-") or "image"
    return f"{stem}{suffix}"


def unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def front_matter(post: SourcePost, category: str, slug: str, noindex: bool, image: str | None, image_alt: str | None) -> str:
    lines = [
        "---",
        "layout: post",
        f"title: {yaml_quote(post.title)}",
        f"description: {yaml_quote(description_for(post))}",
        f"date: {post.date} +0900",
        "section: blog",
        f"category: {category}",
        "lang: ko",
        f"ref: {slug}",
        "tags:",
    ]
    for tag in tags_for(post, category):
        lines.append(f"  - {yaml_quote(tag)}")
    if noindex:
        lines.append("noindex: true")
    if image:
        lines.append(f"image: {yaml_quote(image)}")
        lines.append(f"image_alt: {yaml_quote(image_alt or post.title)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def convert_post(post: SourcePost, repo_root: Path, write: bool = False) -> ConversionResult:
    category = category_for(post)
    slug = slug_for(post, category)
    sanitizer = BodySanitizer(post, repo_root, slug, copy_assets=write)
    sanitizer.feed(post.body)
    body = clean_empty_wrappers("\n".join(line.strip() for line in sanitizer.output if line.strip()).strip())
    body = "\n".join(line.rstrip() for line in body.splitlines())
    image = sanitizer.copied_images[0].removeprefix("images/") if sanitizer.copied_images else None
    image_alt = post.title if image else None
    content = front_matter(post, category, slug, post.category == "Etc/Scrap", image, image_alt) + "\n" + body + "\n"
    post_path = repo_root / "_posts" / f"{slug}.md"
    if write:
        post_path.parent.mkdir(parents=True, exist_ok=True)
        post_path.write_text(content, encoding="utf-8")
    return ConversionResult(
        post_path=post_path if write else None,
        body=body,
        slug=slug,
        missing_images=unique(sanitizer.missing_images),
        copied_images=unique(sanitizer.copied_images),
        external_images=unique(sanitizer.external_images),
    )


def clean_empty_wrappers(body: str) -> str:
    previous = None
    while body != previous:
        previous = body
        body = re.sub(
            r"<(?:p|div|span|figure|figcaption)(?:\s[^>]*)?>\s*</(?:p|div|span|figure|figcaption)>",
            "",
            body,
            flags=re.IGNORECASE,
        )
        body = re.sub(
            r"<p(?:\s[^>]*)?>\s*(?:<br\s*/?>\s*)*</p>",
            "",
            body,
            flags=re.IGNORECASE,
        )
    return body.strip()


def discover_posts(source_root: Path) -> list[SourcePost]:
    return [parse_source(path) for path in sorted(source_root.rglob("*.html"))]


def cleanup_obsolete_generated_posts(repo_root: Path) -> list[str]:
    """Remove prior migration outputs that lack the CMS ref contract."""
    posts_dir = repo_root / "_posts"
    removed: list[str] = []
    if not posts_dir.is_dir():
        return removed
    for path in posts_dir.glob("*-legacy-*.md"):
        head = path.read_text(encoding="utf-8", errors="replace")[:4096]
        ref = re.search(r"^ref:\s*(\S+)\s*$", head, re.MULTILINE)
        if "section: blog" in head and (not ref or ref.group(1) != path.stem):
            path.unlink()
            removed.append(str(path))
    return removed


def run(source_root: Path, repo_root: Path, write: bool) -> dict:
    removed_obsolete = cleanup_obsolete_generated_posts(repo_root) if write else []
    posts = [post for post in discover_posts(source_root) if should_import(post)]
    results: list[ConversionResult] = []
    slugs: list[str] = []
    for post in posts:
        result = convert_post(post, repo_root, write=write)
        results.append(result)
        slugs.append(result.slug)

    report = {
        "source_root": source_root.name,
        "selected_count": len(posts),
        "source_count": len(list(source_root.rglob("*.html"))),
        "category_counts": {
            category: sum(category_for(post) == category for post in posts)
            for category in sorted({category_for(post) for post in posts})
        },
        "duplicate_slugs": sorted({slug for slug in slugs if slugs.count(slug) > 1}),
        "missing_images": [
            {"source": str(post.source_path.relative_to(source_root)), "path": path}
            for post, result in zip(posts, results)
            for path in result.missing_images
        ],
        "external_images": [
            {"source": str(post.source_path.relative_to(source_root)), "url": url}
            for post, result in zip(posts, results)
            for url in result.external_images
        ],
        "copied_images": [path for result in results for path in result.copied_images],
        "generated_posts": [str(result.post_path) for result in results if result.post_path],
        "removed_obsolete_posts": removed_obsolete,
        "missing_descriptions": [post.title for post in posts if not description_for(post)],
    }
    if write:
        report_path = repo_root / "scripts" / "legacy_blog_migration_report.json"
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_root", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    report = run(args.source_root, args.repo_root, write=not args.check_only)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["duplicate_slugs"] or report["missing_descriptions"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
