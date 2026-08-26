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
        self.assertIn("learn-safety-boundary", module)
        self.assertIn("course.course.safety_summary", module)
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

    def test_power_branch_allocation_matches_supply_and_actuator_counts(self):
        manifest = copy.deepcopy(
            _load_yaml(ROOT / "_data" / "learn" / "precise-robot-hand.yml")
        )
        actuator = next(item for item in manifest["bom"] if item["category"] == "actuator")
        actuator["quantity"] = 10
        power = next(item for item in manifest["bom"] if item["category"] == "power")
        power["quantity"] = 2
        power["compatibility"] = [
            "각 출력은 독립 분기로 유지하고 양(+) 출력 병렬 연결은 절대 금지",
            "3개 분기는 액추에이터 4대/4대/3대로 배분",
        ]
        errors = _validate_manifest(ROOT, "precise-robot-hand", manifest)
        self.assertTrue(any("2 supplies" in error and "3 branches" in error for error in errors), errors)
        self.assertTrue(any("11 actuators" in error and "10" in error for error in errors), errors)

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
        grounded["evidence_excerpt"] = (
            "Unit: A; pitch is 3 mm; rated current is documented elsewhere."
        )
        self.assertFalse(_measurement_in_evidence(grounded))
        grounded["evidence_excerpt"] = (
            "Unit: A; contact positions: 3; rated current: 8.5"
        )
        self.assertFalse(_measurement_in_evidence(grounded))
        grounded["evidence_excerpt"] = "Rated current is listed in the manual."
        self.assertFalse(_measurement_in_evidence(grounded))

        for specification in (
            {
                "name": "호칭 나사 지름",
                "value": "3",
                "unit": "mm",
                "evidence_excerpt": "Unit:mm Nominal diameter of thread(d)(15) M3",
            },
            {
                "name": "나사 피치",
                "value": "0.5",
                "unit": "mm",
                "evidence_excerpt": "Unit:mm Nominal diameter of thread(d)(15) M3 Pitch of screw thread(P) 0.5",
            },
            {
                "name": "기본 머리 지름",
                "value": "5.5",
                "unit": "mm",
                "evidence_excerpt": "Unit:mm M3 dk Max.(Basic size) 5.5",
            },
        ):
            self.assertTrue(_measurement_in_evidence(specification), specification)

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

    def test_unsafe_quiz_distractor_is_not_build_instruction(self):
        bom = [{
            "category": "actuator",
            "name": "Smart Servo",
            "model": "XM430",
            "quantity": 11,
            "specifications": [],
        }]
        modules = [{
            "id": "M1",
            "quiz": [{
                "question": "안전한 전원 구성은 무엇인가?",
                "choices": [
                    "각 출력은 독립 분기로 유지한다.",
                    "배터리를 추가하여 모든 어댑터 출력을 병렬로 연결한다.",
                ],
                "answer_index": 0,
                "explanation": "각 전원 출력은 전기적으로 분리해야 한다.",
            }],
        }]
        errors = _module_bom_consistency_errors(modules, bom, "course")
        self.assertFalse(any("parallels" in error for error in errors), errors)

    def test_unsafe_quiz_correct_answer_is_build_instruction(self):
        modules = [{
            "id": "M1",
            "quiz": [{
                "question": "안전한 전원 구성은 무엇인가?",
                "choices": [
                    "모든 어댑터 출력을 병렬로 연결한다.",
                    "각 출력은 독립 분기로 유지한다.",
                ],
                "answer_index": 0,
                "explanation": "선택한 방법으로 배선한다.",
            }],
        }]
        errors = _module_bom_consistency_errors(modules, [], "course")
        self.assertTrue(any("parallels" in error for error in errors), errors)

    def test_estop_short_circuit_ev200_breaking_rating_and_prompt_tokens_fail(self):
        modules = [{
            "id": "M1",
            "content": (
                "비상정지 버튼을 누르고 전원 라인이 단락되는지 확인한다. "
                "EV200의 500 A 차단 정격을 적용한다. [bom_system_truth] [BOM]"
            ),
        }]
        errors = _module_bom_consistency_errors(modules, [], "course")
        self.assertTrue(any("short-circuit" in error for error in errors), errors)
        self.assertTrue(any("continuous-carry" in error for error in errors), errors)
        self.assertTrue(any("invalid citation token" in error for error in errors), errors)

    def test_inline_citation_must_reference_exact_existing_source(self):
        modules = [{"id": "M1", "content": "검증된 값 [S999] [S]."}]
        errors = _module_bom_consistency_errors(
            modules, [], "course", allowed_source_ids={"S1"}
        )
        self.assertTrue(any("invalid citation token [S999]" in error for error in errors), errors)

    def test_academic_module_safety_validation_does_not_require_actuator_bom(self):
        modules = [{
            "id": "M1",
            "content": "비상정지 버튼을 누르고 전원 라인이 단락되는지 확인한다.",
        }]
        errors = _module_bom_consistency_errors(modules, [], "course")
        self.assertTrue(any("short-circuit" in error for error in errors), errors)

    def test_ev200_voltage_fuse_timing_and_nc_contact_misstatements_fail(self):
        modules = [{
            "id": "M1",
            "content": (
                "EV200의 최대 DC 차단 전압은 900 VDC다. "
                "10 A ATOF 퓨즈가 과전류를 즉시 차단한다. "
                "EV200 접촉기 코일의 NC 접점을 점검한다."
            ),
        }]
        errors = _module_bom_consistency_errors(modules, [], "course")
        self.assertTrue(any("switching operating voltage" in error for error in errors), errors)
        self.assertTrue(any("time-current curve" in error for error in errors), errors)
        self.assertTrue(any("coil has no NC contact" in error for error in errors), errors)

    def test_correct_nc_contact_attribution_is_not_rejected(self):
        modules = [{
            "id": "M1",
            "content": "NC 접점은 E-stop 안전 제어 경로에 속하며 EV200 코일에는 NC 접점이 없다.",
        }]
        errors = _module_bom_consistency_errors(modules, [], "course")
        self.assertFalse(any("coil has no NC contact" in error for error in errors), errors)

    def test_actuator_count_before_model_is_system_count(self):
        bom = [{
            "category": "actuator",
            "name": "Smart Servo",
            "model": "XM430",
            "quantity": 11,
            "specifications": [],
        }]
        for claim in (
            "본 프로젝트는 5대의 XM430-W350-T 액추에이터를 사용한다.",
            "총 5개의 스마트 액추에이터로 로봇손을 구성한다.",
        ):
            errors = _module_bom_consistency_errors(
                [{"id": "M1", "content": claim}], bom, "course"
            )
            self.assertTrue(any("5 actuators" in error for error in errors), errors)

    def test_actuator_count_after_model_is_system_count(self):
        bom = [{
            "category": "actuator",
            "name": "Smart Servo",
            "model": "XM430-W350-T",
            "quantity": 11,
            "specifications": [],
        }]
        errors = _module_bom_consistency_errors(
            [{"id": "M1", "content": "XM430-W350-T 액추에이터 5대를 사용한다."}],
            bom,
            "course",
        )
        self.assertTrue(any("5 actuators" in error for error in errors), errors)

    def test_ev200_requires_safe_low_current_relay_chain(self):
        bom = [
            {
                "id": "B-SAFETY-ESTOP",
                "category": "safety",
                "name": "비상정지 버튼",
                "model": "A22E-M-12-EMO",
                "quantity": 1,
                "function": "EV200 코일 3개 직접 구동",
                "compatibility": ["A22E NC 접점이 EV200 코일을 직접 구동"],
                "specifications": [],
            },
            {
                "id": "B-SAFETY-CUTOFF",
                "category": "safety",
                "name": "DC 접촉기",
                "model": "EV200AAANA",
                "quantity": 3,
                "function": "분기 전원 차단",
                "compatibility": ["A22E NC 접점이 EV200 코일을 직접 구동"],
                "specifications": [
                    {"name": "코일 최대 돌입 전류", "value": "3.8", "unit": "A"},
                ],
            },
        ]
        errors = _module_bom_consistency_errors([], bom, "course")
        self.assertTrue(any("outside scope" in error for error in errors), errors)
        self.assertTrue(any("safety relay" in error for error in errors), errors)
        self.assertTrue(any("interposing relay" in error for error in errors), errors)
        self.assertTrue(any("must not directly drive" in error for error in errors), errors)

    def test_ev200_interposing_contact_must_cover_coil_inrush(self):
        bom = [
            {
                "id": "B-SAFETY-RELAY",
                "category": "safety",
                "name": "강제 유도 접점 릴레이",
                "model": "G7SA-3A1B DC12",
                "quantity": 1,
                "specifications": [
                    {"name": "코일 정격 전류", "value": "30", "unit": "mA"},
                    {"name": "DC13 유도 부하 접점 전류", "value": "1", "unit": "A"},
                ],
            },
            {
                "id": "B-SAFETY-COIL-RELAY",
                "category": "safety",
                "name": "코일 중계 릴레이",
                "model": "G2R-1-SND DC12(S)",
                "quantity": 3,
                "specifications": [
                    {"name": "코일 정격 전류", "value": "43.2", "unit": "mA"},
                    {"name": "유도 부하 접점 전류", "value": "2", "unit": "A"},
                ],
            },
            {
                "id": "B-SAFETY-CUTOFF",
                "category": "safety",
                "name": "DC 접촉기",
                "model": "EV200AAANA",
                "quantity": 3,
                "specifications": [
                    {"name": "코일 최대 돌입 전류", "value": "3.8", "unit": "A"},
                    {"name": "코일 돌입 시간 상한", "value": "130", "unit": "ms"},
                ],
            },
        ]
        errors = _module_bom_consistency_errors([], bom, "course")
        self.assertTrue(any("2 A" in error and "3.8 A" in error for error in errors), errors)

    def test_ev200_bom_cannot_call_900_vdc_a_breaking_voltage(self):
        bom = [{
            "id": "B-SAFETY-CUTOFF",
            "category": "safety",
            "name": "DC 접촉기",
            "model": "EV200AAANA",
            "quantity": 1,
            "specifications": [
                {"name": "최대 DC 차단 전압", "value": "900", "unit": "VDC"},
                {"name": "코일 최대 돌입 전류", "value": "3.8", "unit": "A"},
            ],
        }]
        errors = _module_bom_consistency_errors([], bom, "course")
        self.assertTrue(any("900 VDC" in error and "breaking" in error for error in errors), errors)

    def test_power_branch_allocation_capacity_and_real_fuses_fail_closed(self):
        manifest = copy.deepcopy(
            _load_yaml(ROOT / "_data" / "learn" / "precise-robot-hand.yml")
        )
        actuator = next(item for item in manifest["bom"] if item["category"] == "actuator")
        actuator["quantity"] = 11
        power = next(item for item in manifest["bom"] if item["category"] == "power")
        power["quantity"] = 3
        power["specifications"] = [
            {"name": "output voltage", "value": "12", "unit": "V", "evidence_excerpt": "12 V"},
            {"name": "rated output current", "value": "5", "unit": "A", "evidence_excerpt": "5 A"},
        ]
        power["compatibility"] = [
            "각 출력은 독립 분기로 유지하고 양(+) 출력 병렬 연결은 절대 금지"
        ]
        for item in manifest["bom"]:
            text = " ".join(str(item.get(field) or "") for field in ("name", "model", "function"))
            if "퓨즈" in text or "fuse" in text.lower():
                item["name"] = "퓨즈 홀더"
                item["model"] = "Fuse holder"
        errors = _validate_manifest(ROOT, "precise-robot-hand", manifest)
        self.assertTrue(any("allocation missing" in error for error in errors), errors)
        self.assertTrue(any("fuse BOM units" in error for error in errors), errors)

        power["compatibility"].append("3개 분기는 액추에이터 4대/4대/3대로 배분")
        errors = _validate_manifest(ROOT, "precise-robot-hand", manifest)
        self.assertTrue(any("branch load" in error for error in errors), errors)

    def test_branch_fuse_rating_must_sit_between_peak_and_supply(self):
        manifest = copy.deepcopy(
            _load_yaml(ROOT / "_data" / "learn" / "precise-robot-hand.yml")
        )
        fuse = next(item for item in manifest["bom"] if item.get("model") == "0287010.U")
        rating = next(
            specification
            for specification in fuse["specifications"]
            if "전류" in specification["name"]
        )
        rating.update(value="1", evidence_excerpt="1 A")
        errors = _validate_manifest(ROOT, "precise-robot-hand", manifest)
        self.assertTrue(any("fuse rating" in error and "branch peak" in error for error in errors), errors)

        rating.update(value="100", evidence_excerpt="100 A")
        errors = _validate_manifest(ROOT, "precise-robot-hand", manifest)
        self.assertTrue(any("fuse rating" in error and "per-supply" in error for error in errors), errors)

        rating.update(value="10", evidence_excerpt="10 A")
        errors = _validate_manifest(ROOT, "precise-robot-hand", manifest)
        self.assertFalse(any("fuse rating" in error for error in errors), errors)

    def test_module_rejects_safety_compliance_claim_and_estop_assembly(self):
        modules = [{
            "id": "M1",
            "content": (
                "이 회로는 IEC 60204-1 기계 안전 표준을 준수한다. "
                "비상정지 버튼과 릴레이를 배선해 정지 회로를 조립한다."
            ),
        }]
        errors = _module_bom_consistency_errors(modules, [], "course")
        self.assertTrue(any("safety compliance" in error for error in errors), errors)
        self.assertTrue(any("E-stop assembly" in error for error in errors), errors)

    def test_course_safety_summary_rejects_learner_estop_requirement(self):
        manifest = copy.deepcopy(
            _load_yaml(ROOT / "_data" / "learn" / "precise-robot-hand.yml")
        )
        manifest["course"]["safety_summary"].append(
            "회로당 퓨즈 보호 및 비상 차단기 적용"
        )

        errors = _validate_manifest(ROOT, "precise-robot-hand", manifest)

        self.assertTrue(any("safety summary requires learner E-stop" in error for error in errors), errors)

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
