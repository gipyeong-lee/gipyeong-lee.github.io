# Learn Curriculum Platform Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Learn Admin to mindtickle-studio, generate the first robotic-hand curriculum through that Admin, and verify the generated course on gipyeong-lee.github.io.

**Architecture:** AI Blog Studio persists Learn drafts in SQLite, performs typed Gemini query planning and curriculum generation against classified live web sources, validates the result deterministically, then serializes and commits only the Learn contract into the Jekyll repository. The public site renders a separate ad-free Learn collection with browser-local progress and two optional 5,900 KRW Stripe Payment Link prompts.

**Tech Stack:** Python 3.14, FastAPI, SQLAlchemy 2, Pydantic 2, Gemini CLI, DDGS, Requests, BeautifulSoup, Jinja2, Jekyll 4, Liquid, Sass, vanilla JavaScript, pytest, unittest

---

## Repository and execution boundaries

- Studio implementation repository:
  `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio`
- Public site implementation repository:
  `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io`
- Preserve existing untracked files in both repositories. Stage exact paths only.
- Implement on `codex/learn-curriculum-platform` branches in isolated worktrees.
- Do not hand-write `_data/learn/precise-robot-hand.yml` or `_learn/precise-robot-hand/*.md`.
- Tests use fake search and Gemini clients. Only Task 10 performs a real Studio generation run.
- `stripe_payment_link` remains empty until the owner provides a real URL whose
  origin is `https://buy.stripe.com`. No test invents a working payment link.

## File map

### mindtickle-studio

- `scripts/app/learn_schema.py`: strict Pydantic curriculum contract.
- `scripts/app/learn_validation.py`: DAG, source, BOM, safety, Stripe, and path validation.
- `scripts/app/learn_research.py`: typed query planning, DDGS search, source classification, fetch, and URL validation.
- `scripts/app/learn_generator.py`: Gemini query-plan, blueprint, and per-module generation.
- `scripts/app/learn_service.py`: SQLite draft/run lifecycle and orchestration.
- `scripts/app/learn_publish.py`: safe Jekyll serialization, backups, exact staging, and publish result.
- `scripts/app/routes/learn.py`: Learn Admin HTML and JSON endpoints with one active generation job per course.
- `scripts/app/templates/learn_list.html`: draft/run list.
- `scripts/app/templates/learn_editor.html`: brief input, progress, validation, preview, and publish controls.
- `scripts/app/templates/base.html`: Learn navigation entry.
- `scripts/app/models_db.py`: `LearnCourse` and append-only `LearnGenerationRun` models.
- `scripts/app/main.py`: Learn router registration.
- `scripts/prompts/learn_query_planner_system.md`: source-family query contract.
- `scripts/prompts/learn_blueprint_system.md`: course/BOM/capstone contract.
- `scripts/prompts/learn_module_system.md`: detailed module contract.
- `scripts/app/tests/test_learn_schema.py`: schema and deterministic validation.
- `scripts/app/tests/test_learn_research.py`: research classification and source fetching.
- `scripts/app/tests/test_learn_generator.py`: staged Gemini generation with fakes.
- `scripts/app/tests/test_learn_service.py`: persistence and lifecycle.
- `scripts/app/tests/test_learn_publish.py`: serialization, rollback, and exact publish paths.
- `scripts/app/tests/test_learn_routes.py`: Admin routes and background jobs.

### gipyeong-lee.github.io

- `_config.yml`: Learn output collection.
- `_data/navigation.yml`: public Learn menu.
- `_data/learn_settings.yml`: sponsorship amount and public Payment Link.
- `_data/learn/courses.yml`: generated published-course index.
- `_layouts/learn-catalogue.html`: course catalogue.
- `_layouts/learn-course.html`: course, BOM, phase, capstone, and initial sponsorship UI.
- `_layouts/learn-module.html`: module content, assessment, sources, and completion UI.
- `_pages/learn.md`: `/learn/` entry.
- `_includes/head.html`: no-ad resource boundary.
- `_includes/javascripts.html`: Learn progress script inclusion.
- `_includes/main.scss`: Learn Sass import.
- `_sass/4-layouts/_learn.scss`: laboratory-notebook responsive design.
- `js/learn-progress.js`: versioned local progress, quiz, JSON import/export, and sponsorship prompts.
- `scripts/validate_learn.py`: generated contract and no-ads validator.
- `scripts/tests/test_learn_contract.py`: fixture-free validation tests.
- `scripts/tests/test_learn_progress.mjs`: pure progress-state tests.
- Generated only by Studio: `_data/learn/<course>.yml`, `_learn/<course>/index.md`, and `_learn/<course>/<module>.md`.

---

### Task 1: Create strict Learn curriculum schema and validators

**Files:**
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/learn_schema.py`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/learn_validation.py`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/tests/test_learn_schema.py`

- [ ] **Step 1: Write failing schema and validation tests**

```python
from scripts.app.learn_schema import LearnCoursePayload
from scripts.app.learn_validation import validate_course, validate_sponsorship_url


def minimal_payload() -> dict:
    return {
        "schema_version": 1,
        "curriculum_version": "1.0.0",
        "course": {
            "slug": "robot-hand",
            "title": "정교한 로봇손",
            "summary": "로봇손 설계와 제작",
            "outcome": "검증 가능한 5지 로봇손",
            "audience": "초급 제작자",
            "level": "beginner",
            "estimated_hours": 12,
            "budget_krw": {"min": 100000, "max": 300000},
            "required_tools": ["멀티미터"],
            "safety_summary": ["전원을 끄고 배선한다"],
            "last_reviewed": "2026-08-24",
        },
        "phases": [{"id": "phase-1", "title": "기초", "module_ids": ["m1"]}],
        "modules": [{
            "id": "m1", "slug": "safety", "phase_id": "phase-1",
            "title": "안전", "estimated_hours": 2, "prerequisites": [],
            "objectives": ["안전한 작업 절차를 설명한다"],
            "theory_markdown": "# 안전\n전원을 분리한다 [S1].",
            "worked_examples": ["전류 제한 계산"],
            "lab": {"title": "전원 점검", "steps": ["전원을 분리한다"],
                    "safety": ["보안경을 착용한다"], "deliverables": ["점검표"]},
            "assignment": {"title": "위험 분석", "deliverables": ["위험표"],
                           "rubric": ["위험과 완화책이 연결됨"]},
            "quiz": [{"question": "배선 전 첫 행동은?", "choices": ["전원 차단", "모터 구동"],
                      "answer_index": 0, "explanation": "무전원 상태가 기본이다."}],
            "completion_criteria": ["점검표 제출"], "source_ids": ["S1"],
        }],
        "sources": [{"id": "S1", "title": "Safety", "organization": "OSHA",
                     "url": "https://www.osha.gov/", "type": "standard",
                     "published_at": None, "accessed_at": "2026-08-24",
                     "primary": True, "supports": ["m1"]}],
        "bom": [{"id": "P1", "name": "Servo", "function": "actuation", "quantity": 1,
                 "model": "X", "manufacturer": "Y",
                 "specifications": [{"name": "voltage", "value": "7.4", "unit": "V"}],
                 "alternatives": ["Z"], "compatibility": ["7.4 V supply"],
                 "rationale": "sized torque", "datasheet_source_id": "S1"}],
        "capstone": {"title": "로봇손", "deliverables": ["CAD"],
                     "rubric": ["요구사항 검증"], "safety": ["전류 제한"]},
        "generation": {"run_id": "run-1", "generated_at": "2026-08-24T00:00:00Z",
                       "generator": "gemini"},
    }


def test_minimal_payload_parses_and_validates():
    course = LearnCoursePayload.model_validate(minimal_payload())
    assert validate_course(course) == []


def test_cycle_and_unknown_source_block_publish():
    payload = minimal_payload()
    payload["modules"][0]["prerequisites"] = ["m1"]
    payload["modules"][0]["source_ids"] = ["missing"]
    issues = validate_course(LearnCoursePayload.model_validate(payload))
    assert {issue.code for issue in issues} >= {"prerequisite_cycle", "unknown_source"}


def test_stripe_url_accepts_only_https_buy_stripe():
    assert validate_sponsorship_url("") == []
    assert validate_sponsorship_url("https://buy.stripe.com/test") == []
    assert validate_sponsorship_url("http://evil.example/pay")[0].code == "invalid_stripe_url"
```

- [ ] **Step 2: Run tests and confirm RED**

Run: `pytest -q scripts/app/tests/test_learn_schema.py`
Expected: collection fails with `ModuleNotFoundError: scripts.app.learn_schema`.

- [ ] **Step 3: Implement Pydantic models and deterministic validation**

```python
class LearnCoursePayload(BaseModel):
    model_config = ConfigDict(extra="forbid")
    schema_version: Literal[1]
    curriculum_version: str
    course: CourseMeta
    phases: list[Phase]
    modules: list[Module]
    sources: list[Source]
    bom: list[BomItem]
    capstone: Capstone
    generation: GenerationMeta


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    path: str
    message: str
    severity: str = "error"


def validate_sponsorship_url(url: str) -> list[ValidationIssue]:
    if not url:
        return []
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname != "buy.stripe.com":
        return [ValidationIssue("invalid_stripe_url", "sponsorship.stripe_payment_link",
                                "Stripe link must use https://buy.stripe.com")]
    return []
```

Implement `validate_course()` with stable issue codes for duplicate IDs/slugs,
missing phase/module/source references, prerequisite cycles, phase-order
violations, missing module learning elements, unsupported BOM datasheet IDs,
missing specification units, missing capstone fields, unsafe path segments, and
minimum source-family warnings.

- [ ] **Step 4: Run schema tests and confirm GREEN**

Run: `pytest -q scripts/app/tests/test_learn_schema.py`
Expected: all tests pass.

- [ ] **Step 5: Commit Studio schema slice**

```bash
git add scripts/app/learn_schema.py scripts/app/learn_validation.py scripts/app/tests/test_learn_schema.py
git commit -m "feat(learn): add curriculum contract validation"
```

### Task 2: Persist Learn courses and generation provenance

**Files:**
- Modify: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/models_db.py`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/learn_service.py`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/tests/test_learn_service.py`

- [ ] **Step 1: Write failing persistence tests**

```python
def test_create_course_and_append_generation_run(learn_db):
    service = LearnService(session_scope=learn_db)
    course = service.create_course({"slug": "robot-hand", "title": "로봇손", "goal": "5지 로봇손"})
    run = service.start_generation(course.id)
    assert course.status == "draft"
    assert run.status == "researching"
    assert run.course_id == course.id


def test_failed_generation_preserves_last_valid_payload(learn_db):
    service = LearnService(session_scope=learn_db)
    course = service.create_course({"slug": "robot-hand", "title": "로봇손", "goal": "5지 로봇손"})
    service.save_generated(course.id, "run-ok", minimal_payload(), [])
    service.fail_generation(course.id, "run-bad", "Gemini unavailable")
    loaded = service.get_course(course.id)
    assert json.loads(loaded.payload_json)["course"]["slug"] == "robot-hand"
    assert loaded.status == "failed"
```

- [ ] **Step 2: Run persistence tests and confirm RED**

Run: `pytest -q scripts/app/tests/test_learn_service.py`
Expected: import fails because `LearnService` and ORM models do not exist.

- [ ] **Step 3: Add ORM models**

```python
class LearnCourse(Base):
    __tablename__ = "learn_courses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    slug: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    brief_json: Mapped[str] = mapped_column(Text, nullable=False)
    payload_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    validation_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String, nullable=False, default="draft")
    last_error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    published_commit_sha: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True, onupdate=func.current_timestamp())


class LearnGenerationRun(Base):
    __tablename__ = "learn_generation_runs"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey("learn_courses.id"), nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    stage: Mapped[str] = mapped_column(String, nullable=False)
    research_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    validation_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    started_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.current_timestamp())
    ended_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
```

- [ ] **Step 4: Implement lifecycle methods with injected `session_scope`**

Implement `create_course`, `list_courses`, `get_course`, `start_generation`,
`update_run_stage`, `save_generated`, `fail_generation`, and `mark_published`.
Serialize JSON with `ensure_ascii=False` and deterministic `sort_keys=True`.

- [ ] **Step 5: Run persistence tests and confirm GREEN**

Run: `pytest -q scripts/app/tests/test_learn_service.py`
Expected: all tests pass.

- [ ] **Step 6: Commit persistence slice**

```bash
git add scripts/app/models_db.py scripts/app/learn_service.py scripts/app/tests/test_learn_service.py
git commit -m "feat(learn): persist course generation runs"
```

### Task 3: Build focused research and Gemini generation pipeline

**Files:**
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/learn_research.py`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/learn_generator.py`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/prompts/learn_query_planner_system.md`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/prompts/learn_blueprint_system.md`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/prompts/learn_module_system.md`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/tests/test_learn_research.py`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/tests/test_learn_generator.py`

- [ ] **Step 1: Write failing research tests**

```python
def test_research_deduplicates_classifies_and_keeps_live_sources():
    search = FakeSearch({"robot hand paper": [
        {"title": "Paper", "href": "https://arxiv.org/abs/1", "body": "abstract"},
        {"title": "Paper duplicate", "href": "https://arxiv.org/abs/1", "body": "abstract"},
    ]})
    service = LearnResearchService(search=search, validate=lambda urls: [(urls[0], True, 200)], fetch=FakeFetch())
    sources = service.run([ResearchQuery(type="paper", query="robot hand paper")])
    assert len(sources) == 1
    assert sources[0].type == "paper"
    assert sources[0].primary is True
```

- [ ] **Step 2: Run research test and confirm RED**

Run: `pytest -q scripts/app/tests/test_learn_research.py`
Expected: import fails because `learn_research` does not exist.

- [ ] **Step 3: Implement injected research service**

```python
@dataclass(frozen=True)
class ResearchQuery:
    type: str
    query: str


class LearnResearchService:
    def __init__(self, search=None, validate=validate_urls, fetch=None):
        self.search = search or DDGS()
        self.validate = validate
        self.fetch = fetch or fetch_source_text

    def run(self, queries: list[ResearchQuery], progress=None) -> list[dict]:
        candidates: dict[str, dict] = {}
        for position, item in enumerate(queries, start=1):
            rows = list(self.search.text(item.query, max_results=8))
            for row in rows:
                url = canonicalize_url(row.get("href"))
                if url and url not in candidates:
                    candidates[url] = {
                        "title": row.get("title", ""), "url": url,
                        "snippet": row.get("body", ""), "type": item.type,
                    }
            if progress:
                progress({"stage": "research", "query": position, "queries": len(queries)})
        live = {url: (ok, code) for url, ok, code in self.validate(list(candidates))}
        sources = []
        for url, row in candidates.items():
            ok, code = live.get(url, (False, 0))
            if not ok:
                continue
            sources.append({
                "id": f"S{len(sources) + 1}", **row,
                "http_status": code, "primary": is_primary_source(url, row["type"]),
                "content": self.fetch(url, fallback=row["snippet"]),
            })
        return sources
```

`fetch_source_text()` uses Requests with the existing browser User-Agent,
10-second timeout, a 2 MB response cap, BeautifulSoup for HTML, and a 12,000
character extracted-text cap. PDF and blocked sources retain title/snippet and
URL rather than being represented as fetched full text.

- [ ] **Step 4: Run research tests and confirm GREEN**

Run: `pytest -q scripts/app/tests/test_learn_research.py`
Expected: all tests pass without network.

- [ ] **Step 5: Write failing staged generator tests**

```python
def test_generator_plans_research_then_builds_each_module(fake_course_brief):
    gemini = FakeGemini([
        {"queries": [{"type": "paper", "query": "robot hand paper"}]},
        blueprint_without_module_bodies(),
        complete_module("m1"),
    ])
    generator = LearnGenerator(gemini=gemini, research=FakeResearch())
    payload = generator.generate(fake_course_brief, run_id="run-1")
    assert payload["generation"]["run_id"] == "run-1"
    assert payload["modules"][0]["theory_markdown"]
    assert len(gemini.calls) == 3


def test_generator_rejects_invalid_gemini_shape(fake_course_brief):
    generator = LearnGenerator(gemini=FakeGemini([{"wrong": []}]), research=FakeResearch())
    with pytest.raises(LearnGenerationError, match="query plan"):
        generator.generate(fake_course_brief, run_id="run-1")
```

- [ ] **Step 6: Run generator tests and confirm RED**

Run: `pytest -q scripts/app/tests/test_learn_generator.py`
Expected: import fails because `LearnGenerator` does not exist.

- [ ] **Step 7: Implement staged Gemini generator and complete prompts**

```python
class LearnGenerator:
    def __init__(self, gemini=None, research=None):
        self.gemini = gemini or GeminiCLI()
        self.research = research or LearnResearchService()

    def generate(self, brief: dict, run_id: str, progress=None) -> dict:
        query_plan = self._require_dict(self.gemini.call_json(self._query_prompt(brief)), "query plan")
        sources = self.research.run(parse_queries(query_plan), progress=progress)
        blueprint = self._require_dict(self.gemini.call_json(self._blueprint_prompt(brief, sources)), "blueprint")
        modules = []
        for descriptor in blueprint["modules"]:
            module = self._require_dict(
                self.gemini.call_json(self._module_prompt(brief, blueprint, descriptor, sources)),
                f"module {descriptor['id']}",
            )
            modules.append(module)
        payload = {**blueprint, "modules": modules,
                   "generation": {"run_id": run_id, "generated_at": utc_iso(), "generator": "gemini"}}
        return LearnCoursePayload.model_validate(payload).model_dump(mode="json")
```

Prompts require Korean output, no unsupported source IDs, exact units, safety
language, 8-12 modules, one assignment and quiz per module, and capstone
traceability. They forbid claims that patents provide legal clearance.

- [ ] **Step 8: Run generator tests and confirm GREEN**

Run: `pytest -q scripts/app/tests/test_learn_generator.py`
Expected: all tests pass without Gemini or network.

- [ ] **Step 9: Commit research/generator slice**

```bash
git add scripts/app/learn_research.py scripts/app/learn_generator.py scripts/prompts/learn_* scripts/app/tests/test_learn_research.py scripts/app/tests/test_learn_generator.py
git commit -m "feat(learn): generate sourced curricula with Gemini"
```

### Task 4: Serialize and safely publish validated Learn output

**Files:**
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/learn_publish.py`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/tests/test_learn_publish.py`

- [ ] **Step 1: Write failing publisher tests**

```python
def test_serialize_course_writes_only_learn_contract(tmp_path, monkeypatch):
    monkeypatch.setattr(lp, "BLOG_REPO_PATH", tmp_path)
    result = lp.write_course(minimal_payload())
    assert set(result.paths) == {
        "_data/learn/courses.yml",
        "_data/learn/robot-hand.yml",
        "_learn/robot-hand/index.md",
        "_learn/robot-hand/safety.md",
    }
    assert "generated_by: mindtickle-studio" in (tmp_path / "_learn/robot-hand/index.md").read_text()


def test_publish_restores_files_when_git_publish_fails(tmp_path, monkeypatch):
    monkeypatch.setattr(lp, "BLOG_REPO_PATH", tmp_path)
    old = tmp_path / "_data/learn/robot-hand.yml"
    old.parent.mkdir(parents=True)
    old.write_bytes(b"old manifest\n")
    monkeypatch.setattr(
        lp, "publish_paths",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(RuntimeError("git failed")),
    )
    with pytest.raises(RuntimeError, match="git failed"):
        lp.publish_course(minimal_payload(), push=False)
    assert old.read_bytes() == b"old manifest\n"
    assert not (tmp_path / "_learn/robot-hand/safety.md").exists()
```

- [ ] **Step 2: Run publisher tests and confirm RED**

Run: `pytest -q scripts/app/tests/test_learn_publish.py`
Expected: import fails because `learn_publish` does not exist.

- [ ] **Step 3: Implement safe serializer and publisher**

`write_course()` validates with `LearnCoursePayload`, rejects any error-level
issue, writes UTF-8 YAML using
`yaml.safe_dump(document, allow_unicode=True, sort_keys=False)`, writes explicit
permalinks, updates the course index by slug,
and returns an exact relative path list. `publish_course()` snapshots existing
bytes, calls `publisher.publish_paths(paths, message=f"learn: {title}", push=push)`,
and restores or removes every touched path when publication raises.

Generated overview front matter:

```yaml
---
layout: learn-course
title: "정교한 로봇손"
course_slug: robot-hand
permalink: /learn/robot-hand/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: run-1
---
```

- [ ] **Step 4: Run publisher tests and confirm GREEN**

Run: `pytest -q scripts/app/tests/test_learn_publish.py`
Expected: all tests pass.

- [ ] **Step 5: Commit publisher slice**

```bash
git add scripts/app/learn_publish.py scripts/app/tests/test_learn_publish.py
git commit -m "feat(learn): publish validated curricula to Jekyll"
```

### Task 5: Add Learn Admin routes, navigation, and generation UI

**Files:**
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/routes/learn.py`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/templates/learn_list.html`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/templates/learn_editor.html`
- Modify: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/templates/base.html`
- Modify: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/main.py`
- Create: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/tests/test_learn_routes.py`

- [ ] **Step 1: Write failing route tests**

```python
def test_create_generate_validate_publish_flow(client, fake_generator, fake_publisher):
    created = client.post("/learn/api/courses", json={
        "slug": "robot-hand", "title": "정교한 로봇손",
        "goal": "정교한 5지 로봇손을 설계하고 제작한다",
        "learner_background": "일반인, 기초 수학부터",
        "budget_krw": 1000000, "available_tools": ["3D 프린터", "멀티미터"],
        "weekly_hours": 8, "safety_constraints": ["저전압 벤치 테스트"],
        "deliverables": ["CAD", "BOM", "펌웨어", "시험 보고서"],
    })
    assert created.status_code == 201
    job = client.post(f"/learn/api/courses/{created.json()['id']}/generate").json()
    assert client.get(f"/learn/api/jobs/{job['job_id']}").json()["status"] == "done"
    assert client.post(f"/learn/api/courses/{created.json()['id']}/publish").status_code == 200


def test_duplicate_active_generation_returns_409(client):
    created = client.post("/learn/api/courses", json={
        "slug": "robot-hand", "title": "로봇손", "goal": "5지 로봇손",
        "learner_background": "초급", "budget_krw": 100000,
        "available_tools": [], "weekly_hours": 4,
        "safety_constraints": ["전류 제한"], "deliverables": ["CAD"],
    }).json()
    learn_routes._active_generation_by_course[created["id"]] = "busy"
    learn_routes._jobs["busy"] = {"status": "running", "detail": None}
    response = client.post(f"/learn/api/courses/{created['id']}/generate")
    assert response.status_code == 409
```

- [ ] **Step 2: Run route tests and confirm RED**

Run: `pytest -q scripts/app/tests/test_learn_routes.py`
Expected: import or route registration fails because Learn routes do not exist.

- [ ] **Step 3: Implement routes and background job lock**

Expose:

```text
GET    /learn
GET    /learn/new
GET    /learn/{course_id}
POST   /learn/api/courses
POST   /learn/api/courses/{course_id}/generate
GET    /learn/api/jobs/{job_id}
POST   /learn/api/courses/{course_id}/validate
POST   /learn/api/courses/{course_id}/publish
```

Generation runs in `BackgroundTasks`, updates job progress after query planning,
research, blueprint, and each module, and rejects a second active job for the
same course with HTTP 409. Publish rejects non-validated or error-containing
payloads.

- [ ] **Step 4: Build Admin templates**

`learn_editor.html` posts the complete brief as JSON, polls the job endpoint,
renders source-family counts and validation issues, shows generated modules and
BOM in preview, and enables Publish only for `validated` status. UI copy states
that the course itself is AI-generated and human review does not edit seed
course content.

- [ ] **Step 5: Register router and navigation**

```python
from .routes import learn as r_learn  # noqa: E402
app.include_router(r_learn.router)
```

Add this link beside Blog in `base.html`:

```html
<a href="/learn" class="hover:underline {% if page == 'learn' %}font-semibold text-emerald-300{% endif %}">Learn</a>
```

- [ ] **Step 6: Run route tests and confirm GREEN**

Run: `pytest -q scripts/app/tests/test_learn_routes.py`
Expected: all tests pass.

- [ ] **Step 7: Run focused Studio suite**

Run: `pytest -q scripts/app/tests/test_learn_*.py`
Expected: all Learn tests pass.

- [ ] **Step 8: Commit Admin slice**

```bash
git add scripts/app/routes/learn.py scripts/app/templates/learn_list.html scripts/app/templates/learn_editor.html scripts/app/templates/base.html scripts/app/main.py scripts/app/tests/test_learn_routes.py
git commit -m "feat(learn): add curriculum Admin workflow"
```

### Task 6: Add public ad-free Learn collection and layouts

**Files:**
- Modify: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_config.yml`
- Modify: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_data/navigation.yml`
- Create: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_data/learn_settings.yml`
- Create: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_data/learn/courses.yml`
- Create: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_pages/learn.md`
- Create: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_layouts/learn-catalogue.html`
- Create: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_layouts/learn-course.html`
- Create: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_layouts/learn-module.html`
- Modify: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_includes/head.html`
- Modify: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_includes/javascripts.html`
- Modify: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_includes/main.scss`
- Create: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_sass/4-layouts/_learn.scss`

- [ ] **Step 1: Write failing static contract test**

Create `scripts/tests/test_learn_contract.py` asserting Learn collection config,
navigation, `no_ads` conditionals, sponsorship amount `5900`, and empty initial
course index. Run it before adding production files.

- [ ] **Step 2: Run contract test and confirm RED**

Run: `python3 -m unittest scripts.tests.test_learn_contract -v`
Expected: failures for missing Learn config/layout files.

- [ ] **Step 3: Configure collection, route, navigation, and sponsorship**

```yaml
collections:
  learn:
    output: true

sponsorship:
  enabled: true
  amount_krw: 5900
  label: "커피 한 잔 후원"
  stripe_payment_link: ""
```

- [ ] **Step 4: Implement no-ad head boundary**

Wrap both the ad DNS prefetch and AdSense loader in `{% unless page.no_ads %}`.
Do not weaken the existing Blog ad behavior.

- [ ] **Step 5: Implement three Learn layouts and responsive Sass**

Catalogue reads `site.data.learn.courses`. Course layout reads
`site.data.learn[page.course_slug]`, renders phases, module links, BOM, capstone,
sources, and an optional initial sponsorship card. Module layout renders
objectives, Markdown body, lab, assignment, quiz, citations, completion button,
and previous/next links. Every layout uses semantic landmarks and visible focus.

- [ ] **Step 6: Run contract test and confirm GREEN**

Run: `python3 -m unittest scripts.tests.test_learn_contract -v`
Expected: all tests pass with no generated course yet.

- [ ] **Step 7: Commit public foundation**

```bash
git add _config.yml _data/navigation.yml _data/learn_settings.yml _data/learn/courses.yml _pages/learn.md _layouts/learn-catalogue.html _layouts/learn-course.html _layouts/learn-module.html _includes/head.html _includes/javascripts.html _includes/main.scss _sass/4-layouts/_learn.scss scripts/tests/test_learn_contract.py
git commit -m "feat(learn): add ad-free learning experience"
```

### Task 7: Add progress, quiz, export/import, and optional sponsorship behavior

**Files:**
- Create: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/js/learn-progress.js`
- Create: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/scripts/tests/test_learn_progress.mjs`
- Modify: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_layouts/learn-course.html`
- Modify: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/_layouts/learn-module.html`

- [ ] **Step 1: Write failing pure-state tests**

```javascript
import test from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { initialState, completeModule, importState, sponsorshipUrl } = require('../../js/learn-progress.js');

test('completion is independent from sponsorship', () => {
  const state = completeModule(initialState('robot-hand', '1.0.0'), 'm1');
  assert.deepEqual(state.completedModules, ['m1']);
  assert.equal(state.sponsorshipPaid, undefined);
});

test('import rejects unknown modules', () => {
  assert.throws(() => importState('{"courseSlug":"robot-hand","completedModules":["bad"]}', {
    courseSlug: 'robot-hand', curriculumVersion: '1.0.0', moduleIds: ['m1'],
  }), /unknown module/);
});

test('sponsorship URL contains location campaign and no learner identifier', () => {
  assert.equal(sponsorshipUrl('https://buy.stripe.com/test', 'complete'),
    'https://buy.stripe.com/test?utm_source=learn&utm_medium=sponsorship&utm_campaign=learn_complete');
});
```

- [ ] **Step 2: Run JS tests and confirm RED**

Run: `node --test scripts/tests/test_learn_progress.mjs`
Expected: module import fails because `learn-progress.js` does not exist.

- [ ] **Step 3: Implement pure exports plus browser enhancement**

Use a UMD-compatible module: export pure functions through `module.exports` in
Node and attach initialization on `DOMContentLoaded` in browsers. Store only
schema version, course slug/version, completion, assignment checks, quiz scores,
and dismissed sponsorship moments. Never store payment state or personal data.

- [ ] **Step 4: Wire initial and completion sponsorship prompts**

The initial prompt renders before first-module navigation until dismissed. The
completion prompt renders when all required module IDs are complete. Both show
an equally visible skip action. If the configured link is empty, show
"후원 창구 준비 중" without an anchor.

- [ ] **Step 5: Run JS tests and confirm GREEN**

Run: `node --test scripts/tests/test_learn_progress.mjs`
Expected: all tests pass.

- [ ] **Step 6: Commit browser behavior**

```bash
git add js/learn-progress.js scripts/tests/test_learn_progress.mjs _layouts/learn-course.html _layouts/learn-module.html
git commit -m "feat(learn): track progress and optional sponsorship"
```

### Task 8: Add generated-site validation and fake end-to-end publication

**Files:**
- Create: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/scripts/validate_learn.py`
- Modify: `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/scripts/tests/test_learn_contract.py`
- Modify: `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/scripts/app/tests/test_learn_publish.py`

- [ ] **Step 1: Write failing generated validation tests**

Tests create a temporary generated course through `learn_publish.write_course`,
then call `validate_learn.py` to assert manifest/module/source/BOM completeness,
generation provenance, and ad-marker absence in built HTML.

- [ ] **Step 2: Run tests and confirm RED**

Run: `pytest -q scripts/app/tests/test_learn_publish.py` in Studio and
`python3 -m unittest scripts.tests.test_learn_contract -v` in public repo.
Expected: new assertions fail because generated validation is absent.

- [ ] **Step 3: Implement validator CLI**

```python
def validate_repo(repo: Path, site_dir: Path | None = None) -> list[str]:
    errors = validate_course_files(repo)
    if site_dir:
        for html in (site_dir / "learn").rglob("*.html"):
            text = html.read_text(encoding="utf-8")
            for marker in ("adsbygoogle", "pagead2.googlesyndication.com", "ad-slot"):
                if marker in text:
                    errors.append(f"{html}: advertising marker {marker}")
    return errors
```

- [ ] **Step 4: Run focused end-to-end tests and confirm GREEN**

Run both commands from Step 2.
Expected: all tests pass.

- [ ] **Step 5: Commit validation in both repositories**

```bash
git add scripts/validate_learn.py scripts/tests/test_learn_contract.py
git commit -m "test(learn): validate generated curriculum output"
```

```bash
git add scripts/app/tests/test_learn_publish.py
git commit -m "test(learn): cover generated publication contract"
```

### Task 9: Run full regression suites before real generation

- [ ] **Step 1: Run full Studio tests**

Run: `pytest -q scripts/app/tests`
Expected: all tests pass; no Gemini/network calls.

- [ ] **Step 2: Run public unit tests and Jekyll build without a generated course**

Run: `python3 -m unittest discover -s scripts/tests -v`
Expected: all tests pass.

Run: `node --test scripts/tests/test_learn_progress.mjs`
Expected: all tests pass.

Run: `RUBYOPT=-Eutf-8 bundle exec jekyll build`
Expected: exit 0 and `_site/learn/index.html` exists.

### Task 10: Generate robotic-hand curriculum through Learn Admin

**Files:**
- Generated by Studio only in public worktree:
  `_data/learn/courses.yml`
- Generated by Studio only in public worktree:
  `_data/learn/precise-robot-hand.yml`
- Generated by Studio only in public worktree:
  `_learn/precise-robot-hand/index.md`
- Generated by Studio only in public worktree:
  `_learn/precise-robot-hand/*.md`

- [ ] **Step 1: Start Studio against the public feature worktree**

Run with `BLOG_REPO_PATH` pointing to the public Learn worktree and
`git_push=False`. Confirm `GET /learn` returns 200 before generation.

- [ ] **Step 2: Submit the real brief through the Admin API used by the UI**

```json
{
  "slug": "precise-robot-hand",
  "title": "정교한 5지 로봇손 만들기",
  "goal": "부품 선택부터 설계, 제작, 제어, 검증까지 따라 하면 정교한 5지 로봇손을 완성할 수 있는 대학·대학원 수준의 교과과정을 만든다.",
  "learner_background": "일반인. 수학, 기계, 전자, 제어를 필요한 순서대로 기초부터 배운다.",
  "budget_krw": 1500000,
  "available_tools": ["FDM 3D 프린터", "멀티미터", "납땜 인두", "일반 수공구"],
  "weekly_hours": 10,
  "safety_constraints": ["저전압 벤치 전원", "전류 제한", "끼임 방지", "보안경", "비상 전원 차단"],
  "deliverables": ["요구사항", "CAD", "도면", "정확한 BOM과 사양", "배선도", "펌웨어", "제어 코드", "교정 기록", "파지 시험", "내구 시험", "최종 보고서"]
}
```

- [ ] **Step 3: Run real research and Gemini generation**

Trigger `/learn/api/courses/{id}/generate`, poll the job, and preserve its
course ID, generation run ID, source counts, validation result, and errors.
Do not edit generated curriculum files or payload content.

- [ ] **Step 4: If validation fails, improve generator and rerun TDD**

Add a failing regression test for the observed generator deficiency, update
research query planning/prompt/schema/validator, rerun all Learn tests, then
rerun generation. Never patch generated prose, BOM, citations, assignments, or
module files manually.

- [ ] **Step 5: Publish from Learn Admin**

Call the Admin publish endpoint only after status is `validated`. Confirm the
public worktree commit contains the exact generated path list and generation
run ID.

### Task 11: Verify generated site in build and browser

- [ ] **Step 1: Re-run public contract validation and build**

Run: `python3 scripts/validate_learn.py --repo .`
Expected: zero errors.

Run: `RUBYOPT=-Eutf-8 bundle exec jekyll build`
Expected: exit 0.

Run: `python3 scripts/validate_learn.py --repo . --site _site`
Expected: zero errors and no advertising markers in Learn HTML.

- [ ] **Step 2: Serve generated site locally**

Run: `python3 -m http.server 3100 -d _site`
Expected: `http://127.0.0.1:3100/learn/` returns 200.

- [ ] **Step 3: Browser QA public Learn**

Verify catalogue, robotic-hand course, every module, BOM/spec tables, source
links, progress persistence, quiz feedback, export/import, initial sponsorship,
completion sponsorship, keyboard focus, dark mode, and phone/tablet/desktop
layouts. Inspect network/DOM and confirm no AdSense request or marker.

- [ ] **Step 4: Browser QA Learn Admin**

Verify list, creation form, generation progress, recorded source provenance,
validation report, preview, and published state at `http://127.0.0.1:7001/learn`.

- [ ] **Step 5: Final full regression runs**

Studio: `pytest -q scripts/app/tests`

Public: `python3 -m unittest discover -s scripts/tests -v`

Public JS: `node --test scripts/tests/test_learn_progress.mjs`

Public build: `RUBYOPT=-Eutf-8 bundle exec jekyll build`

Expected: every command exits 0. Record exact counts and any pre-existing
Jekyll warnings separately.

---

## Execution decision

Use inline execution with `executing-plans`. The user requested direct
completion in this task and did not request subagent delegation. Stop only for
a genuine external blocker: missing Gemini authentication/network after three
bounded attempts, or missing real Stripe Payment Link when activating payment.
