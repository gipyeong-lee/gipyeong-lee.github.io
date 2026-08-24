# Learn Curriculum Platform Design

Date: 2026-08-24
Status: Approved for implementation

## Goal

Build an ad-free Learn section where a learner can follow a university-level,
evidence-backed curriculum from prerequisites through a finished project. Add a
Learn authoring workflow to AI Blog Studio so a plain-language goal becomes a
reviewable curriculum grounded in university course material, papers, patents,
standards, and manufacturer documentation.

The first complete curriculum teaches the learner to design, build, control,
and validate a precise five-finger robotic hand. It must be created by entering
that goal through the completed AI Blog Studio Learn workflow. It must not be
hand-authored directly in the public repository.

## Repositories

- Public Jekyll site:
  `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io`
- Local FastAPI/Jinja authoring application:
  `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio`

## Product Principles

1. Every course remains free to read and complete.
2. Sponsorship is optional and never unlocks content, answers, progress, or a
   certificate.
3. Learn pages load no advertising slots, AdSense JavaScript, advertising DNS
   prefetches, or other ad tracking.
4. AI proposes curricula, but deterministic validation and a human publish
   action decide what reaches the public site.
5. Quantitative claims, component specifications, and safety requirements must
   point to identifiable sources.
6. A learner completes tangible work. Reading without exercises, assessment,
   and a final project is not a complete course.

## Chosen Architecture

Learn is a separate Jekyll content domain rather than a special Blog category.
Course manifests and module documents form a versioned curriculum graph.
AI Blog Studio writes this contract through a dedicated Learn service and uses
the existing explicit Git publisher only after validation and preview.

The public site remains static. Browser-local progress provides a useful first
student experience without accounts, a database, personal-data collection, or
new hosting costs. The data contract leaves room for an account sync service in
a later release.

### File boundaries

Public curriculum files use these exact boundaries:

- `_pages/learn.md`: catalogue entry point;
- `_data/learn/courses.yml`: published-course index;
- `_data/learn/<course-slug>.yml`: course manifest, source registry, BOM, and
  capstone contract;
- `_learn/<course-slug>/index.md`: course overview content;
- `_learn/<course-slug>/<module-slug>.md`: one instructional module;
- `_layouts/learn-catalogue.html`, `_layouts/learn-course.html`, and
  `_layouts/learn-module.html`: ad-free rendering;
- `assets/js/learn-progress.js`: progress, quiz, sponsorship-prompt, import,
  and export behavior;
- `_sass/4-layouts/_learn.scss`: Learn-only presentation.

Jekyll exposes `_learn` as an output collection. Every course and module sets
an explicit `/learn/.../` permalink, so file movement cannot silently change a
public URL.

Studio owns no public source of truth. Its SQLite database stores authoring
briefs, generated JSON payloads, lifecycle status, validation output, and the
last error. Publishing serializes a validated payload into the public file
contract above. Blog posts and Blog translation hashes remain untouched.

## Public Learn Information Architecture

### Catalogue

`/learn/` lists published courses. Each course card shows:

- title and outcome;
- level and prerequisites;
- estimated duration;
- required equipment and budget band;
- module count;
- local completion percentage;
- last curriculum review date.

### Course page

`/learn/<course-slug>/` shows:

- course outcome and tangible deliverables;
- safety notice;
- prerequisite graph;
- ordered phases and modules;
- assessment model;
- capstone requirements and rubric;
- sources and curriculum version;
- optional pre-course sponsorship prompt.

### Module page

`/learn/<course-slug>/<module-slug>/` shows:

- learning objectives;
- prerequisites;
- theory and worked examples;
- laboratory or build exercise;
- assignment;
- quiz;
- estimated study time;
- safety warnings;
- cited readings;
- explicit completion criteria;
- next-module navigation.

### Progress

Progress is stored in `localStorage` under a versioned course key. Stored data
contains only course slug, curriculum version, completed module IDs, assignment
checklist state, quiz scores, and update time. Learners can export and import
this state as JSON. Import rejects a different course, unsupported schema
version, unknown module IDs, invalid scores, and malformed JSON.

Completion requires every required module and capstone checklist item. Reaching
100% reveals the optional completion sponsorship prompt but does not depend on
payment.

## Ad-Free Boundary

Every Learn route sets `no_ads: true`. The shared head template uses that flag
to omit the AdSense loader and advertising DNS hints. Learn layouts never
include an ad slot. Generated-site assertions scan every `/learn/` HTML file
and fail if they find:

- `adsbygoogle`;
- the configured AdSense client ID;
- `pagead2.googlesyndication.com`;
- `ad-slot` markup.

Analytics may remain enabled for ordinary page traffic, but the Learn progress
payload is never sent to analytics.

## Optional Stripe Sponsorship

### Offer

One fixed-price, one-time Stripe Payment Link represents "커피 한 잔 후원" at
5,900 KRW. The same Payment Link appears at two deliberate moments:

1. before the learner begins the first module;
2. immediately after the learner completes the course.

Both prompts contain equally visible "학습 시작" or "나중에" actions. Closing
or skipping a prompt is stored locally so it does not interrupt every visit.
Skipping never changes course behavior.

### Configuration

Public configuration lives in `_data/learn_settings.yml`:

```yaml
sponsorship:
  enabled: true
  amount_krw: 5900
  label: "커피 한 잔 후원"
  stripe_payment_link: ""
```

The Stripe-hosted Payment Link is public and safe to expose. No secret key,
Price ID, customer data, or webhook secret is written to either repository.
Studio validates that a configured URL uses HTTPS and the
`buy.stripe.com` host. When the URL is empty, the site explains that the
sponsorship channel is being prepared and renders no fake payment action.

The owner creates a one-time, fixed 5,900 KRW Payment Link in the Stripe
Dashboard. Its post-payment behavior redirects to the related course page.
Link parameters may distinguish `learn_start` from `learn_complete` for Stripe
analytics, but contain no learner identifier or other personal data.

The site appends only `utm_source=learn`, `utm_medium=sponsorship`, and either
`utm_campaign=learn_start` or `utm_campaign=learn_complete`. The Stripe link is
opened in the current tab. After payment, Stripe redirects back to the course
URL configured in the Dashboard; cancellation uses browser back navigation.

No webhook is required because payment has no fulfillment effect. Receipts,
refunds, and payment records remain in Stripe. Site copy must not claim that a
payment is a tax-deductible charitable donation.

## Content Contract

### Course manifest

Each course manifest contains:

- `schema_version` and `curriculum_version`;
- slug, title, summary, outcome, status, and review date;
- audience, level, duration, budget, tools, and safety summary;
- ordered phases and module IDs;
- capstone deliverables and rubric;
- source registry;
- authorship and review metadata.

### Source registry

Each source records:

- stable source ID;
- title, author or organization, and URL;
- source type: university, paper, patent, standard, datasheet, textbook, or
  technical documentation;
- publication date when known and access date;
- primary-source status;
- modules and claims supported.

### Module

Each module records:

- module ID, slug, phase, title, and estimated time;
- prerequisite module IDs;
- measurable objectives;
- instructional Markdown;
- worked examples;
- laboratory steps and safety notes;
- assignment deliverables and rubric;
- quiz questions, answers, and explanations;
- completion criteria;
- source IDs.

### Bill of materials

Every part records exact name, function, quantity, key specifications with
units, recommended model or part number, compatible alternatives, selection
rationale, and datasheet source ID. Compatibility notes cover voltage,
continuous and peak current, torque, speed, interface, dimensions, tolerance,
and operating limits when relevant.

## AI Blog Studio Learn Workflow

### Inputs

The Learn editor collects:

- desired finished capability;
- learner background;
- budget and available tools;
- time commitment;
- hardware and safety constraints;
- expected final deliverables.

### Pipeline

1. Convert the goal into measurable outcomes and prerequisite domains.
2. Build separate search queries for university syllabi, primary papers,
   patents, standards, manufacturer datasheets, and implementation references.
3. Search, deduplicate, classify, and live-check candidate URLs.
4. Extract source-bounded facts with Gemini.
5. Generate a structured course manifest and modules with Gemini.
6. Run deterministic contract, citation, graph, assessment, BOM, and safety
   validation.
7. Save a draft and render an admin preview with blocking errors and warnings.
8. Let the owner edit any structured field or Markdown body.
9. Revalidate and publish only after an explicit publish action.
10. Commit only the Learn files named in the publish result.

Gemini remains the default AI runtime. Verification tests use fake research and
AI clients; test commands never make real Gemini calls.

The first release authors and publishes Learn content in Korean. Learn content
translation is a later, separately reviewed pipeline because translating
technical safety instructions and specifications requires its own validation.

### Research strategy

The existing general news researcher is not sufficient for curricula. Learn
uses a focused research service with query families and source quotas. A draft
cannot pass with search snippets alone. Numeric specifications must be backed
by a manufacturer document, standard, patent, or primary technical paper.

Minimum coverage for a hardware curriculum:

- two university or textbook foundations;
- three primary research papers;
- two patents for historical or mechanism context;
- one applicable standard or authoritative safety reference;
- manufacturer documentation for every recommended electrical or mechanical
  part with a model number.

Patents are learning references, not freedom-to-operate opinions. The course
states that commercial use requires separate legal review.

### Draft lifecycle and failure behavior

Draft states are `draft`, `researching`, `generated`, `needs_review`,
`validated`, `published`, and `failed`. Research or AI failure preserves the
last valid draft and source set. Concurrent generation for the same course is
rejected. Publish failure restores changed files from backups and reports the
exact failed paths. A failed publish never leaves a course marked published.

## Deterministic Validation

Publication is blocked when:

- required fields are absent;
- slugs or IDs are invalid or duplicated;
- prerequisite references are missing or cyclic;
- phase order contradicts prerequisites;
- required modules have no objective, exercise, assignment, assessment,
  completion criterion, or source;
- a source ID does not exist;
- a quantitative claim or recommended part specification lacks a supporting
  source;
- a BOM item lacks units, quantity, compatibility information, or datasheet;
- capstone rubric criteria do not trace to course outcomes;
- safety-critical work lacks a warning and a verification step;
- generated paths escape the Learn content directories;
- sponsorship configuration uses a non-HTTPS or non-Stripe payment URL.

Warnings cover stale access dates, secondary-only reading sets, unusually long
modules, and non-blocking optional equipment gaps.

## First Curriculum: Precise Five-Finger Robotic Hand

### Generation provenance requirement

The robotic-hand curriculum is the first production run of the Learn authoring
system, not fixture content written before or outside that system. Delivery
order is mandatory:

1. implement and test the Studio Learn research, generation, validation,
   preview, and publishing workflow;
2. enter the robotic-hand learning goal and constraints through the same Learn
   input used for any future course;
3. run real source research and Gemini generation from Studio;
4. inspect the generated validation report and preview;
5. publish the validated generated payload through Studio;
6. retain generation metadata and source provenance so the run is auditable.

If the first output is incomplete or invalid, implementation corrects the
research queries, prompt, schema, or deterministic validator and runs the
course generation again. It does not repair curriculum prose, BOM entries,
assignments, citations, or module files by hand. Human action is limited to
the same brief input, review, approval, and publish controls available for all
future courses.

The initial course produces a benchtop five-finger robotic hand capable of
independent digit movement, controlled grasping, bounded force, calibration,
and repeatability testing. It does not claim human equivalence, autonomous body
construction, medical suitability, or safe interaction without further
engineering.

Research determines final part numbers and exact module content. Required
curriculum phases are:

1. hand anatomy, biomechanics, safety, and engineering requirements;
2. degrees of freedom, kinematics, joints, and tendon mechanisms;
3. CAD, tolerances, materials, and fabrication;
4. actuator, transmission, torque, speed, and thermal sizing;
5. position, force, and tactile sensing;
6. power, motor drivers, protection, and wiring;
7. embedded firmware and low-level control;
8. calibration, kinematics, force control, and grasp planning;
9. staged integration, fault handling, and validation;
10. capstone build and engineering report.

The capstone requires CAD and drawings, complete BOM, firmware and control
code, wiring documentation, calibration records, grasp demonstrations, force
limit evidence, repeatability and endurance results, failure analysis, and a
reproducible final report.

Hardware work includes explicit pinch, sharp-tool, hot-surface, electrical,
battery, unexpected-motion, and stored-energy warnings. Learners test at
limited current and speed before full-power operation.

## UI Direction

Learn uses a calm laboratory-notebook visual language distinct from the news
feed: wide reading column, phase rail, restrained technical typography,
specification tables, source badges, progress ring, and persistent module
navigation. Sponsorship prompts look like small support cards rather than ads.
They contain no countdown, modal trap, guilt copy, or repeated animation.

Admin adds a top-level Learn menu with course list, new-course brief, generation
progress, validation report, structured editor, Markdown module editor, preview,
and publish controls.

## Testing

### Studio

- service tests for serialization, parsing, validation, DAG ordering, source
  coverage, BOM compatibility, and sponsorship URL validation;
- route tests for list, create, generate, edit, validate, preview, and publish;
- fake-client tests for research and Gemini success, partial failure, retry,
  duplicate generation, and invalid output;
- publisher tests for explicit staging, rollback, and dirty-file recovery;
- full `pytest -q scripts/app/tests` regression run.

### Public site

- curriculum contract tests for manifests, modules, source references, and the
  robotic-hand course completeness;
- progress reducer tests for completion, quiz scores, versioning, export, and
  import rejection;
- Jekyll build;
- generated route and metadata assertions;
- generated Learn HTML advertising-absence assertions;
- responsive browser review at phone, tablet, and desktop widths;
- keyboard and screen-reader checks for navigation, quizzes, sponsorship
  prompts, and progress controls.

No test or build contacts Stripe or Gemini.

## Scope Boundaries

This release includes one complete course, Studio generation and review,
static public learning, local progress, optional Stripe sponsorship prompts,
and reproducible validation. The complete course must be generated and
published by Studio after the generator exists; pre-seeding hand-written course
files is outside scope.

This release does not include accounts, cloud progress sync, instructor
grading, accredited certificates, discussion forums, tax receipts, recurring
sponsorship, payment-triggered fulfillment, autonomous purchasing, or control
of a physical robot from the website. It also does not include Learn
translations; the Korean curriculum is the canonical first release.

## Acceptance Criteria

1. Learn appears in public navigation and Studio navigation.
2. The precise robotic-hand course can be followed from prerequisites through
   capstone with cited sources, exact component specifications, assignments,
   quizzes, and completion criteria.
3. Studio can create, research, generate, validate, edit, preview, and publish a
   curriculum without changing Blog posts.
4. Invalid source, graph, BOM, safety, or path data cannot publish.
5. Course progress survives reload and can be exported and restored.
6. Optional 5,900 KRW Stripe sponsorship appears before starting and after
   completion, while both prompts can be skipped immediately.
7. No Learn HTML loads or renders advertising resources.
8. Automated tests and Jekyll build pass without real Stripe or Gemini calls.
9. The robotic-hand course has a recorded Studio generation run and source
   provenance, and no course content is hand-authored directly in the public
   repository.
