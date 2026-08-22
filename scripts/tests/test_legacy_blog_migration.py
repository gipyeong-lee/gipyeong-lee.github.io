import tempfile
import unittest
from pathlib import Path
import re

from scripts.import_legacy_blog import (
    category_for,
    convert_post,
    cleanup_obsolete_generated_posts,
    front_matter,
    parse_source,
    slug_for,
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

    def test_classifies_religious_text_commentary_as_books(self):
        with tempfile.TemporaryDirectory() as directory:
            source = self.write_html(directory, "Etc/기타", "본문 " * 20)
            source.write_text(
                source.read_text(encoding="utf-8").replace("테스트 글", "[해설] 반야심경"),
                encoding="utf-8",
            )
            post = parse_source(source)
            self.assertEqual(category_for(post), "books")

    def test_selects_non_book_only_above_1000_non_whitespace_chars(self):
        with tempfile.TemporaryDirectory() as directory:
            post = parse_source(self.write_html(directory, "Computer/Server", "가나다 " * 334))
            self.assertEqual(visible_char_count(post.body_text), 1002)
            self.assertTrue(should_import(post))

    def test_omits_missing_local_image_and_reports_it(self):
        with tempfile.TemporaryDirectory() as directory:
            post = parse_source(
                self.write_html(
                    directory,
                    "Etc/독서",
                    '<img src="./img/missing.png">본문',
                )
            )
            result = convert_post(post, Path(directory) / "out")
            self.assertIn("./img/missing.png", result.missing_images)
            self.assertNotIn("missing.png", result.body)

    def test_reuses_existing_repo_asset_image(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            (repo / "assets" / "images").mkdir(parents=True)
            (repo / "assets" / "images" / "diagram.svg").write_text("<svg />", encoding="utf-8")
            source = repo / "source" / "1" / "1-entry.html"
            source.parent.mkdir(parents=True)
            source.write_text(
                '<title>테스트 글</title><p class="category">Computer</p>'
                '<p class="date">2024-01-01 00:00:00</p>'
                '<div class="contents_style"><img src="/assets/images/diagram.svg"></div>',
                encoding="utf-8",
            )
            result = convert_post(parse_source(source), repo)
            self.assertIn("{{ site.baseurl }}/assets/images/diagram.svg", result.body)
            self.assertEqual(result.missing_images, [])

    def test_check_only_does_not_copy_local_images(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            source = repo / "source" / "1" / "1-entry.html"
            (source.parent / "img").mkdir(parents=True)
            (source.parent / "img" / "photo.png").write_bytes(b"image")
            source.write_text(
                '<title>테스트 글</title><p class="category">Etc/독서</p>'
                '<p class="date">2024-01-01 00:00:00</p>'
                '<div class="contents_style"><img src="./img/photo.png"></div>',
                encoding="utf-8",
            )
            post = parse_source(source)
            result = convert_post(post, repo, write=False)
            self.assertEqual(result.missing_images, [])
            self.assertFalse((repo / "images" / "blog").exists())

    def test_generates_blog_studio_compatible_slug_and_ref(self):
        with tempfile.TemporaryDirectory() as directory:
            post = parse_source(self.write_html(directory, "Etc/독서", "본문"))
            category = category_for(post)
            slug = slug_for(post, category)
            self.assertRegex(slug, r"^\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$")
            self.assertIn(f"ref: {slug}", front_matter(post, category, slug, False, None, None).splitlines())

    def test_cleanup_removes_only_old_generated_posts_without_ref(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            posts = repo / "_posts"
            posts.mkdir()
            old = posts / "2015-08-01-legacy-57-books-한글.md"
            old.write_text("---\nsection: blog\n---\n본문\n", encoding="utf-8")
            keep = posts / "2015-08-01-legacy-57-books.md"
            keep.write_text("---\nsection: blog\nref: 2015-08-01-legacy-57-books\n---\n본문\n", encoding="utf-8")
            cleanup_obsolete_generated_posts(repo)
            self.assertFalse(old.exists())
            self.assertTrue(keep.exists())
