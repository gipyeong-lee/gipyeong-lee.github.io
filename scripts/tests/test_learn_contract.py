from __future__ import annotations

import copy
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.validate_learn import (
    _load_yaml,
    _measurement_in_evidence,
    _module_bom_consistency_errors,
    _bom_source_authority_error,
    _specification_unit_issue,
    _source_type_authoritative,
    _unsafe_generated_values,
    _validate_manifest,
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
        self.assertIn('amount_display: "5,900원"', settings)
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
        self.assertIn("specification.unit == 'dimensionless'", course)
        self.assertIn("course.course.required_tools", course)
        self.assertIn("item.alternatives", course)
        self.assertIn("item.compatibility", course)
        self.assertIn("course.capstone.safety", course)
        self.assertIn("page.lab.deliverables", module)
        self.assertIn("data-complete-capstone", course)
        self.assertIn("learn-module-nav", module)
        self.assertNotIn("adsense.html", combined)
        self.assertNotIn("ad-slot", combined)
        self.assertIn("{{ source.url | escape }}", module)
        self.assertIn("{{ source.title | escape }}", module)
        self.assertIn("{{ source.organization | escape }}", module)

    def test_unconfigured_sponsorship_never_renders_a_self_link(self):
        course = (ROOT / "_layouts/learn-course.html").read_text(encoding="utf-8")
        module = (ROOT / "_layouts/learn-module.html").read_text(encoding="utf-8")
        self.assertGreaterEqual((course + module).count("slice: 0, 23"), 2)
        self.assertNotIn("contains 'https://buy.stripe.com'", course + module)

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

    def test_academic_course_allows_empty_bom(self):
        manifest = copy.deepcopy(
            _load_yaml(ROOT / "_data" / "learn" / "precise-robot-hand.yml")
        )
        manifest["course"]["course_type"] = "academic"
        manifest["bom"] = []
        errors = _validate_manifest(ROOT, "precise-robot-hand", manifest)
        self.assertFalse(any("BOM" in error or "actuator peak" in error for error in errors), errors)

    def test_bom_specification_requires_correct_unit_and_grounded_excerpt(self):
        coefficient = {
            "name": "friction coefficient",
            "value": "0.20",
            "unit": "N",
            "evidence_excerpt": "Friction coefficient 0.20 N",
        }
        grounded = {
            "name": "rated current",
            "value": "2.3",
            "unit": "A",
            "evidence_excerpt": "Rated current is 2.3 A at 12 V.",
        }
        self.assertIsNotNone(_specification_unit_issue(coefficient))
        self.assertTrue(_measurement_in_evidence(grounded))
        grounded["evidence_excerpt"] = "Unit: A; rated current: 2.3"
        self.assertTrue(_measurement_in_evidence(grounded))
        grounded.update({"value": "34", "unit": "pins", "evidence_excerpt": "34 programmable GPIOs"})
        self.assertTrue(_measurement_in_evidence(grounded))
        grounded.update(
            {
                "value": "3",
                "unit": "A",
                "evidence_excerpt": "Pitch is 3 mm; available in size A",
            }
        )
        self.assertFalse(_measurement_in_evidence(grounded))
        grounded["evidence_excerpt"] = "Rated current is listed in the manual."
        self.assertFalse(_measurement_in_evidence(grounded))

    def test_module_electrical_claims_must_match_bom(self):
        specifications = [
            {"name": "rated current", "value": "2.3", "unit": "A"},
            {"name": "rated voltage", "value": "12", "unit": "V"},
        ]
        bom = [
            {
                "category": "actuator",
                "name": "Smart Servo",
                "model": "XM430",
                "quantity": 11,
                "specifications": specifications,
            },
            {
                "category": "wiring",
                "name": "Micro-Fit connector",
                "model": "MF-8A",
                "quantity": 1,
                "specifications": [
                    {"name": "rated current", "value": "8.5", "unit": "A"}
                ],
            },
        ]
        modules = [{
            "id": "M1",
            "content": "로봇손 모터 5개, 총 전류 7.5 A. XM430은 12 V~24 V이며 MF-8A를 메인 전원에 쓴다.",
        }]
        errors = _module_bom_consistency_errors(modules, bom, "course")
        self.assertEqual(len(errors), 4, errors)

    def test_module_electrical_variants_and_parallel_supplies_are_rejected(self):
        bom = [
            {
                "category": "actuator",
                "name": "Smart Servo",
                "model": "XM430",
                "quantity": 11,
                "specifications": [
                    {"name": "stall current", "value": "2.3", "unit": "A"},
                    {"name": "rated voltage", "value": "12", "unit": "V"},
                ],
            }
        ]
        modules = [
            {
                "id": "M1",
                "content": (
                    "로봇손 액추에이터 5대의 총 전류는 7.5 amperes다. "
                    "XM430 액추에이터 구동 전원으로 24 V를 인가한다. "
                    "3개 전원 어댑터 출력을 병렬로 연결한다."
                ),
            }
        ]
        errors = _module_bom_consistency_errors(modules, bom, "course")
        self.assertTrue(any("5 actuators" in error for error in errors), errors)
        self.assertTrue(any("7.5 A" in error for error in errors), errors)
        self.assertTrue(any("24" in error or "voltage" in error for error in errors), errors)
        self.assertTrue(any("parallels" in error for error in errors), errors)

    def test_parallel_supply_hazard_warning_is_not_assembly_instruction(self):
        modules = [{
            "id": "M1",
            "content": (
                "독립 전원 어댑터 출력을 병렬로 연결하면 순환 전류와 화재 위험이 생긴다. "
                "각 출력을 병렬로 구성한다는 뜻이 아니라 전기적으로 분리한다."
            ),
        }]
        errors = _module_bom_consistency_errors(modules, [], "course")
        self.assertFalse(any("parallels" in error for error in errors), errors)

    def test_single_actuator_lab_does_not_claim_total_system_count(self):
        bom = [{
            "category": "actuator",
            "name": "Smart Servo",
            "model": "XM430",
            "quantity": 11,
            "specifications": [],
        }]
        modules = [{"id": "M1", "content": "액추에이터 1개를 무부하 상태로 시험한다."}]
        errors = _module_bom_consistency_errors(modules, bom, "course")
        self.assertFalse(any("actuators but BOM" in error for error in errors), errors)

    def test_opencr_fsr_divider_rejects_actuator_rail_voltage(self):
        bom = [{
            "category": "actuator",
            "name": "Smart Servo",
            "model": "XM430",
            "quantity": 11,
            "specifications": [],
        }]
        unsafe = [{
            "id": "M1",
            "content": "12 V 입력 전원 하에서 FSR과 10 kΩ 저항으로 분압기를 구성한다.",
        }]
        errors = _module_bom_consistency_errors(unsafe, bom, "course")
        self.assertTrue(any("FSR divider above 3.3 V" in error for error in errors), errors)

        safe = [{
            "id": "M1",
            "content": "3.3 V 센서 전원으로 FSR과 10 kΩ 저항 분압기를 구성한다.",
        }]
        errors = _module_bom_consistency_errors(safe, bom, "course")
        self.assertFalse(any("FSR divider above 3.3 V" in error for error in errors), errors)

    def test_generated_source_fields_reject_unsafe_markup(self):
        errors = _unsafe_generated_values(
            {"sources": [{"title": "<img src=x onerror=alert(1)>"}]}
        )
        self.assertTrue(any("manifest.sources.0.title" in error for error in errors), errors)

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
