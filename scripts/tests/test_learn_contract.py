from __future__ import annotations

import unittest
from pathlib import Path


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

    def test_catalogue_route_and_empty_index_exist(self):
        page = (ROOT / "_pages/learn.md").read_text(encoding="utf-8")
        self.assertIn("layout: learn-catalogue", page)
        self.assertIn("permalink: /learn/", page)
        self.assertIn("no_ads: true", page)
        courses = (ROOT / "_data/learn/courses.yml").read_text(encoding="utf-8")
        self.assertEqual(courses.strip(), "[]")

    def test_learn_layouts_are_ad_free_and_use_generated_contract(self):
        catalogue = (ROOT / "_layouts/learn-catalogue.html").read_text(encoding="utf-8")
        course = (ROOT / "_layouts/learn-course.html").read_text(encoding="utf-8")
        module = (ROOT / "_layouts/learn-module.html").read_text(encoding="utf-8")
        combined = catalogue + course + module
        self.assertIn("site.data.learn.courses", catalogue)
        self.assertIn("site.data.learn[page.course_slug]", course)
        self.assertIn("page.module_id", module)
        self.assertNotIn("adsense.html", combined)
        self.assertNotIn("ad-slot", combined)

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


if __name__ == "__main__":
    unittest.main()
