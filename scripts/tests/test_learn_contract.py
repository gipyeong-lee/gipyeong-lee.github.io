from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.validate_learn import (
    _bom_source_authority_error,
    _source_type_authoritative,
    validate_repo,
)


ROOT = Path(__file__).resolve().parents[2]


class LearnFoundationContractTest(unittest.TestCase):
    def test_jekyll_collection_and_navigation(self):
        config = (ROOT / "_config.yml").read_text(encoding="utf-8")
        self.assertIn("collections:\n  learn:\n    output: true", config)
        navigation = (ROOT / "_data/navigation.yml").read_text(encoding="utf-8")
        self.assertIn("- title: Learn\n  url: /learn/", navigation)

    def test_sponsorship_is_optional_fixed_5900_and_unconfigured(self):
        settings = (ROOT / "_data/learn_settings.yml").read_text(encoding="utf-8")
        self.assertIn("sponsorship:", settings)
        self.assertIn("enabled: true", settings)
        self.assertIn("amount_krw: 5900", settings)
        self.assertIn('stripe_payment_link: ""', settings)

    def test_catalogue_route_and_index_exist(self):
        page = (ROOT / "_pages/learn.md").read_text(encoding="utf-8")
        self.assertIn("layout: learn-catalogue", page)
        self.assertIn("permalink: /learn/", page)
        self.assertIn("no_ads: true", page)
        courses = (ROOT / "_data/learn/courses.yml").read_text(encoding="utf-8")
        self.assertTrue(courses.strip())

    def test_learn_layouts_are_ad_free_and_use_generated_contract(self):
        catalogue = (ROOT / "_layouts/learn-catalogue.html").read_text(encoding="utf-8")
        course = (ROOT / "_layouts/learn-course.html").read_text(encoding="utf-8")
        module = (ROOT / "_layouts/learn-module.html").read_text(encoding="utf-8")
        combined = catalogue + course + module
        self.assertIn("site.data.learn.courses", catalogue)
        self.assertIn("site.data.learn[page.course_slug]", course)
        self.assertIn("page.module_id", module)
        self.assertIn("item.specifications", course)
        self.assertIn("learn-module-nav", module)
        self.assertNotIn("adsense.html", combined)
        self.assertNotIn("ad-slot", combined)

    def test_unconfigured_sponsorship_never_renders_a_self_link(self):
        course = (ROOT / "_layouts/learn-course.html").read_text(encoding="utf-8")
        module = (ROOT / "_layouts/learn-module.html").read_text(encoding="utf-8")
        self.assertGreaterEqual(
            (course + module).count("contains 'https://buy.stripe.com'"), 3
        )

    def test_shared_head_omits_all_ad_resources_on_no_ads_pages(self):
        head = (ROOT / "_includes/head.html").read_text(encoding="utf-8")
        self.assertIn("{% unless page.no_ads %}", head)
        self.assertIn("pagead2.googlesyndication.com", head)
        blocks = head.split("{% unless page.no_ads %}")
        protected = "".join(block.split("{% endunless %}")[0] for block in blocks[1:])
        self.assertIn('rel="dns-prefetch" href="https://pagead2.googlesyndication.com"', protected)
        self.assertIn("adsbygoogle.js", protected)

    def test_learn_styles_and_script_are_conditionally_loaded(self):
        imports = (ROOT / "_includes/main.scss").read_text(encoding="utf-8")
        scripts = (ROOT / "_includes/javascripts.html").read_text(encoding="utf-8")
        self.assertIn("@import '4-layouts/learn';", imports)
        self.assertIn("{% if page.course_slug %}", scripts)
        self.assertIn("/js/learn-progress.js", scripts)
        self.assertTrue((ROOT / "_sass/4-layouts/_learn.scss").is_file())

    def test_generated_index_is_valid(self):
        self.assertEqual(validate_repo(ROOT), [])

    def test_generated_index_requires_manifest(self):
        with TemporaryDirectory() as directory:
            repo = Path(directory)
            data_dir = repo / "_data" / "learn"
            data_dir.mkdir(parents=True)
            (data_dir / "courses.yml").write_text("- slug: missing-course\n", encoding="utf-8")
            errors = validate_repo(repo)
            self.assertTrue(any("missing-course.yml" in error for error in errors), errors)

    def test_bom_source_authority_rejects_wikipedia_and_wrong_manufacturer(self):
        item = {"manufacturer": "ROBOTIS"}
        wikipedia = {"type": "standard", "url": "https://en.wikipedia.org/wiki/ISO"}
        retailer = {
            "type": "datasheet",
            "url": "https://retailer.example.com/robot-servo",
        }
        search = {
            "type": "datasheet",
            "url": "https://www.google.com/search?q=ROBOTIS+XM430",
        }
        root = {"type": "datasheet", "url": "https://robotis.com/"}
        forum_attachment = {
            "type": "datasheet",
            "url": "https://e2e.ti.com/cfs-file/community/third-party-datasheet.pdf",
        }
        official = {
            "type": "datasheet",
            "url": "https://emanual.robotis.com/docs/en/dxl/x/xm430-w350/",
        }
        self.assertIsNotNone(_bom_source_authority_error(item, wikipedia))
        self.assertIsNotNone(_bom_source_authority_error(item, retailer))
        self.assertIsNotNone(_bom_source_authority_error(item, search))
        self.assertIsNotNone(_bom_source_authority_error(item, root))
        self.assertIsNotNone(
            _bom_source_authority_error({"manufacturer": "TI"}, forum_attachment)
        )
        self.assertIsNone(_bom_source_authority_error(item, official))

    def test_learning_source_family_requires_matching_repository(self):
        self.assertTrue(_source_type_authoritative("https://arxiv.org/abs/1", "paper"))
        self.assertFalse(
            _source_type_authoritative("https://surveymonkey.com/survey", "paper")
        )
        self.assertTrue(
            _source_type_authoritative(
                "https://patents.google.com/patent/US11325264B1/en", "patent"
            )
        )
        self.assertFalse(
            _source_type_authoritative("https://aiweekly.co/robot-hand", "patent")
        )
        self.assertFalse(
            _source_type_authoritative(
                "https://www.uspto.gov/patents/search/patent-public-search", "patent"
            )
        )

    def test_built_learn_html_rejects_ad_markers(self):
        with TemporaryDirectory() as directory:
            repo = Path(directory) / "repo"
            data_dir = repo / "_data" / "learn"
            data_dir.mkdir(parents=True)
            (data_dir / "courses.yml").write_text("[]\n", encoding="utf-8")
            site = Path(directory) / "site" / "learn"
            site.mkdir(parents=True)
            (site / "index.html").write_text("<script>adsbygoogle</script>", encoding="utf-8")
            errors = validate_repo(repo, site_dir=site.parent)
            self.assertTrue(any("advertising marker adsbygoogle" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
