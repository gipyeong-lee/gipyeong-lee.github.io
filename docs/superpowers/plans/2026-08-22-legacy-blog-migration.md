# Legacy Blog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Import 64 selected Korean legacy posts into the Jekyll Blog section with stable categories, SEO metadata, and safe local-image handling.

**Architecture:** A Python migration utility parses source HTML, selects explicit reading posts or posts exceeding 1,000 visible non-whitespace characters, converts only `.contents_style`, and writes deterministic Jekyll posts that satisfy Blog Studio's filename/ref contract. Template changes add category labels, `noindex`, and `BlogPosting` schema; missing source images are omitted and reported.

**Tech Stack:** Python 3 standard library, HTMLParser, Jekyll, Liquid, YAML, kramdown.

---

### Task 1: Add migration utility tests

**Files:**
- Create: `scripts/tests/test_legacy_blog_migration.py`
- Test: `scripts/import_legacy_blog.py` public parsing and selection helpers

- [x] **Step 1: Write failing tests**

```python
import tempfile
import unittest
from pathlib import Path

from scripts.import_legacy_blog import (
    category_for,
    convert_post,
    parse_source,
    should_import,
    visible_char_count,
)

class LegacyBlogMigrationTest(unittest.TestCase):
    def write_html(self, directory, category, body):
        source = Path(directory) / "1" / "1-entry.html"
        source.parent.mkdir()
        source.write_text(
            f'<title>테스트 글</title><p class="category">{category}</p>'
            f'<p class="date">2024-01-01 00:00:00</p>'
            f'<div class="contents_style">{body}</div>',
            encoding="utf-8",
        )
        return source

    def test_selects_books_even_when_short(self):
        with tempfile.TemporaryDirectory() as directory:
            post = parse_source(self.write_html(directory, "Etc/독서", "짧은 글"))
            self.assertTrue(should_import(post))
            self.assertEqual(category_for(post), "books")

    def test_selects_non_book_only_above_1000_non_whitespace_chars(self):
        with tempfile.TemporaryDirectory() as directory:
            post = parse_source(self.write_html(directory, "Computer/Server", "가나다 " * 334))
            self.assertEqual(visible_char_count(post.body_text), 1002)
            self.assertTrue(should_import(post))

    def test_omits_missing_local_image_and_reports_it(self):
        with tempfile.TemporaryDirectory() as directory:
            post = parse_source(self.write_html(directory, "Etc/독서", '<img src="./img/missing.png">본문'))
            result = convert_post(post, Path(directory) / "out")
            self.assertIn("missing.png", result.missing_images)
            self.assertNotIn("missing.png", result.body)
```

- [x] **Step 2: Run tests and confirm expected missing-module failure**

Run: `python3 -m unittest discover -s scripts/tests -p 'test_legacy_blog_migration.py' -v`
Expected: FAIL because `scripts/import_legacy_blog.py` does not exist.

### Task 2: Implement deterministic HTML conversion

**Files:**
- Create: `scripts/import_legacy_blog.py`

- [x] **Step 1: Implement parser and selection helpers**

```python
def visible_char_count(html):
    return len("".join(html.split()))

def should_import(post):
    return post.category == "Etc/독서" or visible_char_count(post.body_text) > 1000
```

Parser must extract title, date, source category, tags, `.contents_style`, local image references, and explicit source links. Ignore `script`, `style`, and outer document markup.

- [x] **Step 2: Implement category mapping and metadata generation**

Use `books`, `essay`, `engineering`, `projects`, `life`, `finance`, and `web3`. Generate a stable slug from date, source numeric ID, and normalized title. Generate a description from the first meaningful body text and truncate to 160 characters without cutting inside a word when possible.

- [x] **Step 3: Implement safe image conversion**

Copy only existing local image files into `images/blog/<slug>/`; rewrite body paths to `{{ site.baseurl }}/images/blog/<slug>/<filename>`. Preserve existing alt text. Remove missing local `<img>` elements and append missing paths to a JSON report. Preserve external URLs only for source content where no local replacement exists.

- [x] **Step 4: Implement post and audit output**

Write front matter with `layout`, `title`, `description`, `date`, `section: blog`, `category`, `lang: ko`, `ref` equal to the filename stem, `tags`, and optional `noindex`, `image`, and `image_alt`. Write `scripts/legacy_blog_migration_report.json` containing selected count, category counts, removed obsolete outputs, missing images, and source paths.

- [x] **Step 5: Run tests and confirm green**

Run: `python3 -m unittest discover -s scripts/tests -p 'test_legacy_blog_migration.py' -v`
Expected: all converter tests PASS.

### Task 3: Add Blog taxonomy and SEO template support

**Files:**
- Modify: `_data/blog_categories.yml`
- Modify: `_includes/head.html`
- Modify: `_includes/article-schema.html`
- Modify: `_includes/breadcrumb-schema.html`

- [x] **Step 1: Add categories**

Add labels and unique order values for `books`, `engineering`, `projects`, `life`, `finance`, and `web3`; retain existing `essay` and `portfolio` entries.

- [x] **Step 2: Add noindex and BlogPosting behavior**

Render `<meta name="robots" content="noindex,follow">` when `page.noindex` is true. Set article JSON-LD `@type` to `BlogPosting` for `page.section == 'blog'`, otherwise keep `NewsArticle`.

- [x] **Step 3: Run Liquid/config checks**

Run: `git diff --check`
Expected: no whitespace errors.

### Task 4: Generate selected posts and assets

**Files:**
- Create: 64 generated files under `_posts/`
- Create: local assets under `images/blog/` only when source files exist
- Create: `scripts/legacy_blog_migration_report.json`

- [x] **Step 1: Run migration against the supplied export**

Run: `python3 scripts/import_legacy_blog.py /Users/gipyeonglee/Downloads/gipyeonglee-1-1 --repo-root .`
Expected: 64 selected posts; 45 missing local image references reported; no broken local image tags emitted.

- [x] **Step 2: Audit generated front matter**

Run: `python3 scripts/validate_posts.py`
Expected: no new front-matter or filename errors.

- [x] **Step 3: Audit selection and links**

Run: `python3 scripts/import_legacy_blog.py /Users/gipyeonglee/Downloads/gipyeonglee-1-1 --repo-root . --check-only`
Expected: selected count remains 64; zero duplicate generated slugs; zero missing descriptions; zero local image references pointing outside `images/blog/`.

- [x] **Step 4: Verify Blog Studio compatibility**

Run: `BLOG_REPO_PATH=/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io python3 -c 'from scripts.app.blog_service import scan_blog; print(len([p for p in scan_blog("/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_posts") if "legacy-" in p["ref"]]))'`
Expected: `64`; every migrated file stem equals `ref` and passes Blog Studio slug validation.

### Task 5: Build and inspect output

**Files:**
- Inspect: `_site/blog/`, `_site/`

- [x] **Step 1: Build the site**

Run: `RUBYOPT=-Eutf-8 bundle exec jekyll build`
Expected: exit code 0 and generated pages for all 64 imported posts.

- [x] **Step 2: Verify Blog category counts and SEO markers**

Run: `rg -l 'section: blog' _posts | wc -l` and `rg -l 'BlogPosting' _site/blog _site 2>/dev/null | wc -l`
Expected: 69 Korean Blog post files including 64 imported posts and 5 existing language variants, and generated BlogPosting markup in all imported pages.

- [x] **Step 3: Verify no broken local images**

Run: `rg -n 'images/blog|<img' _site/blog | head -100`
Expected: every `/images/blog/` path exists; no generated `./img/` paths remain.
