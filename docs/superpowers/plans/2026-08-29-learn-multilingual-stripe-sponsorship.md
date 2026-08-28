# Learn Multilingual and Stripe Sponsorship Implementation Plan

> **Execution:** Implement task-by-task in current session. Apply test-driven
> development for every behavior change. Do not delegate or hand-author course
> translations.

**Goal:** Generate and publish five-language Learn curricula through AI Blog
Studio, then create and connect one isolated live Stripe 5,900 KRW sponsorship
Payment Link without modifying existing Stripe products.

**Architecture:** Korean remains canonical. Studio extracts an allowlisted map
of learner-visible strings, translates that map serially through Gemini CLI,
reconstructs full localized payloads from canonical immutable data, and blocks
publishing until every selected locale validates. Jekyll receives complete
locale manifests and explicit locale routes. A standalone, metadata-scoped
Stripe provisioner reuses only exact Learn sponsorship objects or creates new
ones; it never updates, archives, or deletes existing Stripe objects.

**Tech Stack:** Python 3.14, FastAPI, SQLAlchemy 2, Pydantic 2, Gemini CLI,
Jinja2, Jekyll 4, Liquid, vanilla JavaScript, Stripe CLI/API, pytest, Node test
runner.

---

## Repository boundaries

- Studio worktree:
  `/Users/gipyeonglee/Documents/0.workspace/mindtickle-studio/.worktrees/learn-curriculum-platform`
- Public worktree:
  `/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/.worktrees/learn-curriculum-platform`
- Branch in both worktrees: `codex/learn-curriculum-platform`
- Generated robotic-hand locale files must come from Studio publish only.
- Stage exact files. Preserve unrelated user changes.
- Tests never make Gemini or Stripe calls.
- Stripe live work happens only after all deterministic and test-mode checks.
- Stripe scope: create/reuse metadata-exact Learn objects only. Never update,
  archive, deactivate, or delete any existing Product, Price, Payment Link, or
  payment setting.

## Locale contract

| Learn locale | Stripe locale | Public prefix |
| --- | --- | --- |
| `ko` | `ko` | `/learn/` |
| `en` | `en` | `/learn/en/` |
| `ja` | `ja` | `/learn/ja/` |
| `zh-cn` | `zh` | `/learn/zh-cn/` |
| `zh-tw` | `zh-TW` | `/learn/zh-tw/` |

---

### Task 1: Add localization schema and persistence

**Studio files:**

- Modify: `scripts/app/learn_schema.py`
- Modify: `scripts/app/models_db.py`
- Modify: `scripts/app/learn_service.py`
- Modify: `scripts/app/tests/test_learn_schema.py`
- Modify: `scripts/app/tests/test_learn_service.py`

- [ ] Write failing tests for supported language constants, optional
  localization metadata, default selected languages, unique translation rows,
  persisted status/source hash/payload/errors, and stale detection.
- [ ] Run focused tests and confirm expected failures.
- [ ] Add `LocalizationMeta` to the backward-compatible payload schema.
- [ ] Add `LearnCourseTranslation` table with unique course/language constraint.
- [ ] Store selected languages in the course brief, defaulting to all five for
  legacy briefs that do not contain the field.
- [ ] Add service methods to upsert, list, fail, validate, and mark translation
  rows stale without overwriting their last valid payload.
- [ ] Run focused tests until green.
- [ ] Commit Studio exact paths.

### Task 2: Build strict translation extraction and overlay engine

**Studio files:**

- Create: `scripts/app/learn_translation.py`
- Create: `scripts/prompts/learn_translation_system.md`
- Create: `scripts/app/tests/test_learn_translation.py`
- Modify: `scripts/app/learn_validation.py`
- Modify: `scripts/app/tests/test_learn_schema.py`

- [ ] Write failing tests for deterministic source hash, translatable path
  extraction, strict path completeness, extra paths, non-string output,
  immutable ID/URL/number/unit/answer preservation, Korean leakage, and stale
  translation detection.
- [ ] Run focused tests and confirm expected failures.
- [ ] Implement allowlisted JSON-path extraction and strict overlay onto a deep
  canonical copy.
- [ ] Add localized payload validation comparing immutable projections.
- [ ] Implement Gemini CLI translator wrapper returning JSON-only path maps.
- [ ] Preserve official source titles and organization names.
- [ ] Run focused tests until green.
- [ ] Commit Studio exact paths.

### Task 3: Add Admin multilingual generation workflow

**Studio files:**

- Modify: `scripts/app/routes/learn.py`
- Modify: `scripts/app/templates/learn_editor.html`
- Modify: `scripts/app/templates/learn_list.html`
- Modify: `scripts/app/tests/test_learn_routes.py`

- [ ] Write failing route tests for language defaults, automatic post-canonical
  translation, one active mutating job, serial order, retry-one-locale,
  retry-missing/stale, job progress, and publish gate.
- [ ] Run focused tests and confirm expected failures.
- [ ] Add background translation orchestration using existing configured delay.
- [ ] Add endpoints for all-locale generation and single-locale retry.
- [ ] Extend course detail response with locale rows and source-hash status.
- [ ] Add language checkboxes and localization status/actions to Admin UI.
- [ ] Keep canonical generation fail-closed and preserve successful locales on
  one-locale failure.
- [ ] Run focused tests until green.
- [ ] Commit Studio exact paths.

### Task 4: Publish atomic multilingual Jekyll artifacts

**Studio files:**

- Modify: `scripts/app/learn_publish.py`
- Modify: `scripts/app/routes/learn.py`
- Modify: `scripts/app/tests/test_learn_publish.py`
- Modify: `scripts/app/tests/test_learn_routes.py`

- [ ] Write failing tests for five locale indexes/manifests/pages, Korean URL
  stability, localized URL prefixes, translation metadata, explicit
  `translations` arrays, stale generated locale cleanup, exact staging, and
  rollback.
- [ ] Run focused tests and confirm expected failures.
- [ ] Change publisher input to canonical payload plus validated selected
  translations.
- [ ] Serialize complete locale manifests and localized overview/module files.
- [ ] Generate locale catalogue pages and translation navigation metadata.
- [ ] Block publish if any selected locale is missing, stale, or invalid.
- [ ] Back up every Korean and locale path before write/delete.
- [ ] Run focused tests until green.
- [ ] Commit Studio exact paths.

### Task 5: Localize public Learn rendering

**Public files:**

- Create: `_data/learn_i18n.yml`
- Modify: `_layouts/learn-catalogue.html`
- Modify: `_layouts/learn-course.html`
- Modify: `_layouts/learn-module.html`
- Modify: `_includes/language-switcher.html`
- Modify: `_includes/head.html`
- Modify: `js/learn-progress.js`
- Modify: `scripts/tests/test_learn_contract.py`
- Modify: `scripts/tests/test_learn_progress.mjs`
- Modify: `scripts/validate_learn.py`

- [ ] Write failing public tests for locale dictionary completeness, manifest
  selection, localized route families, `html[lang]`, hreflang/x-default,
  language switcher, progress identity sharing, and absence of mixed-language
  fallback.
- [ ] Run Python and Node focused tests and confirm expected failures.
- [ ] Add five-language UI dictionary and resolve all Learn interface copy from
  `page.lang`.
- [ ] Select manifest/index using page locale keys.
- [ ] Render locale-aware internal links and language navigation.
- [ ] Keep localStorage key language-neutral.
- [ ] Extend source and built-site validators to all locale routes.
- [ ] Run focused tests until green.
- [ ] Commit public exact paths.

### Task 6: Harden and provision Stripe sponsorship

**Studio files:**

- Create: `scripts/provision_learn_sponsorship.py`
- Create: `scripts/app/tests/test_learn_sponsorship.py`
- Modify: `scripts/app/learn_validation.py`
- Modify: `scripts/app/tests/test_learn_schema.py`

**Public files:**

- Modify: `_data/learn_settings.yml`
- Modify: `_layouts/learn-course.html`
- Modify: `_layouts/learn-module.html`
- Modify: `js/learn-progress.js`
- Modify: `scripts/tests/test_learn_contract.py`
- Modify: `scripts/tests/test_learn_progress.mjs`

- [ ] Write failing tests for exact Stripe host validation, credential/port and
  lookalike rejection, locale mapping, UTM mapping, metadata-exact object
  matching, partial-object resume, response verification, and fail-closed YAML
  update.
- [ ] Run focused tests and confirm expected failures.
- [ ] Accept only `https://donate.stripe.com` and
  `https://buy.stripe.com` public links.
- [ ] Implement standalone provisioner with injected runner for tests.
- [ ] List and filter Stripe objects read-only before creation. Reuse only exact
  metadata/currency/amount matches.
- [ ] Create new objects with idempotency keys when no exact match exists.
- [ ] Never call update, archive, deactivate, or delete APIs.
- [ ] Verify test-mode Product, Price, and Link contract without payment.
- [ ] After all code tests pass, repeat exact flow in live mode and write only
  returned public URL into `_data/learn_settings.yml`.
- [ ] Add locale and UTM parameters client-side without personal data.
- [ ] Commit Studio provisioner/tests and public configuration/UI/tests as exact
  paths after live verification.

### Task 7: Run full automated verification

- [ ] Run all Studio Learn tests.
- [ ] Run full Studio regression suite.
- [ ] Run all public Python tests.
- [ ] Run public Node tests.
- [ ] Run `python3 scripts/validate_learn.py --repo .`.
- [ ] Run Jekyll build.
- [ ] Run `python3 scripts/validate_learn.py --repo . --site _site`.
- [ ] Record test totals and investigate every new failure before proceeding.

### Task 8: Generate robotic-hand translations through Admin

- [ ] Start Studio with `BLOG_REPO_PATH` pointing to public Learn worktree.
- [ ] Open existing `precise-robot-hand` course in Learn Admin.
- [ ] Trigger Admin multilingual generation; do not write locale course content
  manually.
- [ ] Monitor serial Gemini calls and preserve visible progress.
- [ ] If validation fails, fix generator/translator/validator and rerun only the
  affected locale.
- [ ] Confirm all four translation rows are validated and source-hash current.
- [ ] Publish via Admin and record translation run IDs and commit SHA.

### Task 9: Browser and Stripe acceptance

- [ ] Build and serve final public site locally.
- [ ] Test all five catalogues and course pages, one representative module per
  locale, language switching, shared progress, completion, import/export,
  mobile layout, keyboard use, and console errors.
- [ ] Verify every built Learn HTML route has no ad resource or marker.
- [ ] Open the live Stripe Link from each locale and verify 5,900 KRW base
  offer, donation presentation, and localized checkout without paying.
- [ ] Verify existing Stripe objects were not changed by comparing pre/post
  object IDs and modified timestamps for non-Learn objects when available.
- [ ] Restore local learner progress to zero for user testing.
- [ ] Report local URLs, commits, test evidence, Stripe object IDs in truncated
  non-secret form, and any production/deployment boundary.

## Completion rule

Do not claim completion until:

- all selected locales are Admin-generated and valid;
- public files came from Studio publish;
- live Stripe link is present and verified without a charge;
- all automated and built-site checks pass;
- browser acceptance passes in five languages;
- no existing Stripe product was updated, archived, deactivated, or deleted.
