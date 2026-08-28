# Learn Multilingual Generation and Stripe Sponsorship Design

Date: 2026-08-29
Status: Approved direction; written-spec review pending
Extends: `2026-08-24-learn-curriculum-platform-design.md`

## Goal

Extend Learn so AI Blog Studio generates one evidence-backed Korean curriculum
and validated English, Japanese, Simplified Chinese, and Traditional Chinese
versions. Publish all selected languages as ad-free static Learn pages with
shared local progress. Create and connect a real, optional, one-time Stripe
sponsorship offer for 5,900 KRW.

The existing precise robotic-hand curriculum is the first multilingual run.
Its translations must be created through Learn Admin. They must not be written
directly in the public repository.

## Confirmed Product Decisions

1. Supported languages are `ko`, `en`, `ja`, `zh-cn`, and `zh-tw`.
2. Korean is the canonical source language.
3. Research, sources, BOM selection, safety engineering, assessment answers,
   identifiers, URLs, and quantitative values are established once in Korean.
4. Gemini translates only learner-visible text. Deterministic code reconstructs
   localized payloads and verifies immutable technical fields.
5. Every selected language must validate before the course can publish.
6. Translation jobs are serial, resumable, and skip current translations.
7. Learn remains free, ad-free, and usable without sponsorship.
8. Stripe sponsorship is a fixed 5,900 KRW one-time Payment Link, shown before
   learning begins and after course completion.

## Architecture

### Canonical curriculum plus localized payloads

`LearnCourse.payload_json` remains the canonical Korean payload. Each target
language has one persisted translation record containing:

- course ID and language;
- canonical source hash;
- translated payload JSON;
- deterministic validation output;
- lifecycle status and last error;
- translator and translation run metadata;
- created and updated timestamps.

A new `LearnCourseTranslation` table has a unique `(course_id, language)`
constraint. Separate rows make single-language retry and status display simple
without weakening the canonical curriculum lifecycle.

The existing schema stays backward-compatible. A localized payload may contain
an optional `localization` block:

```yaml
localization:
  source_language: ko
  language: en
  source_hash: <sha256>
  translator: gemini-cli
  translated_at: <iso-8601>
  translation_run_id: <uuid>
```

The canonical Korean payload omits the block or identifies itself as Korean.
Its curriculum version and generation provenance remain unchanged.

### Why full localized payloads are published

Jekyll Liquid cannot safely deep-merge an arbitrary nested translation overlay.
Studio therefore persists and publishes complete localized manifests. Gemini
does not create those complete manifests directly. Studio copies immutable
fields from Korean and applies translated text only at allowlisted paths.

This gives simple static rendering while preventing the model from changing
technical identity, values, answers, or evidence.

## Translation Contract

### Translatable fields

The translator may change learner-visible natural language, including:

- course title, summary, outcome, audience, tools, and safety text;
- phase and module titles;
- objectives, theory, examples, lab instructions, assignments, rubrics,
  explanations, and completion criteria;
- capstone title, deliverables, rubric, and safety text;
- user-facing BOM names, functions, specification labels, compatibility notes,
  alternatives, evidence excerpts, and rationale;
- source support descriptions when present.

Official source titles and organization names remain in their published form
unless a separate localized title is added without replacing the original.

### Immutable fields

Localized output must exactly match Korean for:

- schema and curriculum versions;
- course, phase, module, BOM, and source identifiers;
- course and module slugs;
- phase membership and prerequisite graph;
- estimated hours and budget values;
- source URL, type, publication/access dates, and primary-source flag;
- BOM category, quantity, model, manufacturer, numeric value, unit, and
  datasheet source ID;
- quiz question count, choice count, and `answer_index`;
- source links assigned to modules;
- generation run provenance.

Any immutable-field difference blocks that locale.

### Translator protocol

Studio sends Gemini a compact translation document keyed by stable JSON paths,
not the full unconstrained course schema. The response is strict JSON mapping
each requested path to translated text. Program code then:

1. rejects missing, extra, duplicate, or non-string paths;
2. overlays translated text on a deep copy of Korean;
3. adds localization metadata;
4. validates the ordinary Learn schema;
5. compares every immutable path with Korean;
6. scans for untranslated Korean leakage and suspicious number or unit changes;
7. saves only the validated localized payload.

Gemini calls use the existing CLI-only backend and configured serial delay.
Automated tests use fake translators and never spend model quota.

### Staleness and retry

The canonical source hash covers normalized Korean curriculum JSON and excludes
volatile translation metadata. Changing canonical content marks every prior
translation stale. Admin can retry one locale or all missing/stale locales.
Hash-matched validated translations are skipped.

A failed locale preserves its last valid payload but marks it stale or failed.
It can be inspected, but it cannot satisfy the publish gate.

## Learn Admin Experience

### Course creation

The new-course brief adds a language section. Korean is fixed and enabled.
English, Japanese, Simplified Chinese, and Traditional Chinese are selected by
default. These language choices are stored with the course.

The primary action becomes `실제 조사 · AI 5개 언어 생성`:

1. run research and canonical Korean generation;
2. run canonical validation;
3. translate selected target languages serially;
4. validate each translation;
5. show a final readiness summary.

If canonical generation fails, no translations run. If one translation fails,
the job completes as `needs_translation` and reports that locale without
discarding successful locales.

### Existing course detail

The detail page adds a localization panel with one row per language:

- language and source hash state;
- missing, translating, validated, stale, or failed status;
- issue count and last error;
- `이 언어 재생성` action;
- localized preview link.

`다국어 생성/갱신` processes only missing or stale languages. Publish stays
disabled until Korean and every selected locale pass current validation.

### Concurrency and provenance

Only one canonical or translation job may mutate a course at a time. Duplicate
requests return HTTP 409. Translation run IDs, model backend, source hash,
timestamps, validation results, and errors remain auditable.

## Public File and URL Contract

### Data files

- Korean index: `_data/learn/courses.yml`
- Locale indexes: `_data/learn/courses.<lang>.yml`
- Korean manifest: `_data/learn/<slug>.yml`
- Locale manifests: `_data/learn/<slug>.<lang>.yml`

### Pages

Korean keeps existing URLs:

- `/learn/`
- `/learn/<course>/`
- `/learn/<course>/<module>/`

Localized routes are:

- `/learn/<lang>/`
- `/learn/<lang>/<course>/`
- `/learn/<lang>/<course>/<module>/`

Examples:

- `/learn/en/precise-robot-hand/`
- `/learn/ja/precise-robot-hand/assembly/`
- `/learn/zh-cn/precise-robot-hand/`
- `/learn/zh-tw/precise-robot-hand/`

Publisher writes Korean and all selected locale files in one explicit Git
transaction. Stale Studio-generated locale files are removed only when they
belong to the same course and are included in the rollback backup set.

### Localization metadata and navigation

Every page sets `lang`, localized title, canonical family ID, and explicit
translation links. The shared head emits `hreflang` for available languages
and Korean `x-default`. Course, module, catalogue, progress, quiz, safety,
sponsorship, and navigation interface copy comes from one checked-in
`_data/learn_i18n.yml` dictionary.

No page silently falls back to Korean learner-visible content. Missing locale
artifacts are a publish error, not a mixed-language page.

### Shared progress

Progress identity remains course slug plus curriculum version, not language.
Changing language preserves completed modules, assignments, quiz scores,
capstone state, and sponsorship dismissal. Exported progress is language
neutral and imports from any supported locale.

## Stripe Sponsorship

### Live object contract

Create or reuse exactly one live Stripe Product, Price, and Payment Link using
metadata that identifies this integration:

```text
service=learn
support_tier=coffee
currency=krw
unit_amount=5900
integration_version=1
```

Product display name is `Learn 운영 후원 · 커피 한 잔`. Price is one-time,
`krw`, and `unit_amount=5900`. Quantity is fixed at one. Payment Link uses
`submit_type=donate` and hosted confirmation with a short thank-you message.

The link does not collect shipping address, phone number, custom personal
fields, or save payment details for future off-session use. Stripe dynamically
offers account-enabled payment methods. Payment does not unlock or fulfill
anything, so no webhook is needed for this release.

Site copy says `후원` or `운영 후원`, not tax-deductible charitable donation.

### Safe provisioning

Provisioning runs outside application requests. It performs read-only metadata
search first and reuses an exact active match. Creation uses stable Stripe
idempotency keys for product, price, and link requests. It verifies returned
object mode, currency, amount, quantity, active state, submit type, metadata,
and URL host before writing the public URL.

The live secret remains only in Stripe CLI configuration. Repositories store
only the public Payment Link. Logs and test output never print API keys.

Test mode proves the provisioning contract first. Live mode runs only after
the code and public static tests pass. Verification opens the live hosted page
but does not submit a real charge.

### Supported hosts and locale

Current Stripe Payment Links can use `donate.stripe.com` when
`submit_type=donate`. Public and Studio URL validation accepts only HTTPS URLs
whose host is exactly `donate.stripe.com` or `buy.stripe.com`. Subdomains,
lookalike hosts, credentials, and nonstandard ports are rejected.

The public sponsorship URL adds only:

- `locale`: `ko`, `en`, `ja`, `zh`, or `zh-TW`;
- `utm_source=learn`;
- `utm_medium=sponsorship`;
- `utm_campaign=learn_start` or `learn_complete`.

`zh-cn` maps to Stripe locale `zh`; `zh-tw` maps to `zh-TW`. No learner ID,
email, course progress, quiz result, or other personal data enters the URL.

### Public presentation

Start and completion prompts remain inline, nonmodal, and immediately
skippable. Both use the same Payment Link. Opening sponsorship marks that prompt
dismissed locally but does not mark payment success. Completion and progress
never depend on Stripe.

If configuration is missing or invalid, the site renders a disabled preparation
message and no fake/self link. Learn pages remain advertising-free.

## Failure Handling

- Canonical research or generation failure: preserve last valid curriculum and
  translations; mark current run failed.
- Translation parse or validation failure: preserve valid locales and expose
  locale-specific retry; block publish.
- Canonical change: mark old translations stale by source hash.
- Concurrent generation or translation: return HTTP 409.
- Publish validation failure: write no public files.
- Git commit or push failure: restore all changed Korean and locale files, or
  keep an auditable pending commit under the existing publisher contract.
- Stripe exact object already exists: reuse it.
- Stripe partial provisioning: find the metadata-tagged partial objects and
  continue without creating duplicates.
- Stripe response mismatch: stop before changing `_data/learn_settings.yml`.

## Testing

### Studio automated tests

- language selection validation and defaults;
- translation path extraction and strict overlay;
- immutable-field comparison for IDs, URLs, numbers, units, BOM, and answers;
- missing, extra, stale, malformed, and Korean-leak translation failures;
- serial delay, single-locale retry, resume, skip-current, and concurrency;
- translation persistence and unique course/language rows;
- Admin route and publish-gate behavior;
- publisher path set, stale cleanup, rollback, and locale metadata;
- Stripe host validation for `donate.stripe.com` and `buy.stripe.com`;
- full Studio regression suite with fake AI clients.

### Public automated tests

- five catalogue, course, and module route families;
- correct manifest selection and localized UI copy;
- `html[lang]`, canonical, `hreflang`, and `x-default` metadata;
- no mixed-language fallback;
- shared progress across language changes;
- Stripe locale and UTM query mapping;
- invalid or absent Stripe URL fail-closed rendering;
- every generated Learn HTML page contains no ad resource or marker;
- source and built-site validators;
- Jekyll build and JavaScript tests.

### Real acceptance run

1. Start Learn Admin against the Learn public worktree.
2. Open the existing precise-robot-hand course in Admin.
3. Run the Admin multilingual generation action with real Gemini CLI.
4. Wait serially for all four target languages.
5. Confirm all five locales pass validation and retain source provenance.
6. Publish through Admin, not by manually editing course output.
7. Build and serve the public Jekyll site.
8. Test catalogue, course, one module, language switching, progress sharing,
   responsive layout, keyboard use, and no-ad assertions in all languages.
9. Provision test Stripe objects and verify their contract without charging.
10. Provision/reuse the live 5,900 KRW objects, save only the public URL, rebuild,
    and open each localized checkout page without submitting payment.

## Scope Boundaries

Included:

- five-language Learn generation and publishing;
- Admin localization status, retry, preview, and publish gate;
- localized catalogue, courses, modules, SEO metadata, and UI copy;
- shared anonymous local progress;
- real one-time Stripe sponsorship link;
- current robotic-hand course generated into all languages through Admin.

Excluded:

- accounts or cloud progress sync;
- certificates, accreditation, instructor grading, or discussion forums;
- recurring sponsorship or variable donation amount;
- payment-triggered content, receipts in the Learn app, tax receipts, webhooks,
  customer portals, or local payment history;
- independent research or independent BOM decisions per language;
- automatic production deployment outside the current feature-branch test flow.

## Acceptance Criteria

1. Learn Admin defaults new courses to all five languages and can resume or
   retry multilingual generation without repeating current work.
2. All localized technical payloads preserve canonical IDs, source URLs, BOM
   values and units, graph structure, and quiz answers.
3. Publish is impossible while a selected locale is missing, stale, failed, or
   invalid.
4. Public Korean URLs remain stable and all four localized route families build.
5. Language switching preserves progress and produces correct locale metadata.
6. Every Learn route remains free, skippable, and advertising-free.
7. One live Stripe-hosted sponsorship link charges a base price of 5,900 KRW,
   uses donation presentation, and requests no unnecessary personal fields.
8. Start and completion sponsorship prompts use locale-aware Stripe URLs and
   never gate learning or completion.
9. The robotic-hand translations are generated from Admin with Gemini and have
   recorded source hashes and translation provenance.
10. Studio tests, public tests, Jekyll build, built-site validation, and browser
    acceptance checks pass without submitting a real payment.

## External References

- Stripe Payment Link creation and `submit_type=donate`:
  <https://docs.stripe.com/api/payment-link/create>
- Stripe Payment Link locale URL parameters:
  <https://docs.stripe.com/payment-links/customize>
- Stripe idempotent POST requests:
  <https://docs.stripe.com/api/idempotent_requests>
- Stripe currency minor-unit and KRW charge rules:
  <https://docs.stripe.com/currencies>
