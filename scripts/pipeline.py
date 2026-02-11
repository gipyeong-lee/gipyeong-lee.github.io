"""Pipeline orchestrator — wires 5 agents together with fact-check loop."""

import datetime
import os
import re

from .models import Verdict
from .agents import (
    ResearcherAgent,
    WriterAgent,
    FactCheckerAgent,
    EditorAgent,
    TranslatorAgent,
    ImageGeneratorAgent,
)

POSTS_DIR = "_posts"
MAX_REVISION_ROUNDS = 2


class Pipeline:
    """Orchestrates the 5-agent fact-checked blog post pipeline."""

    def __init__(self):
        self.researcher = ResearcherAgent()
        self.writer = WriterAgent()
        self.fact_checker = FactCheckerAgent()
        self.editor = EditorAgent()
        self.translator = TranslatorAgent()
        self.image_generator = ImageGeneratorAgent()

    def run(self, topic: str) -> bool:
        """Run the full pipeline for a topic.

        Returns True if a post was successfully generated and saved.
        """
        today = datetime.date.today().strftime("%Y-%m-%d")
        slug = self._make_slug(topic)
        full_slug = f"{today}-{slug}"

        print(f"\n{'='*60}")
        print(f"  Pipeline Start: {topic}")
        print(f"  Slug: {full_slug}")
        print(f"{'='*60}\n")

        # --- Stage 1: Research ---
        print("[Stage 1/6] Research")
        brief = self.researcher.run(topic)
        if not brief:
            print("Pipeline ABORTED: Research failed.\n")
            return False

        print(f"  Research complete: {len(brief.verified_sources)} verified sources, "
              f"{len(brief.key_facts)} facts\n")

        # --- Stage 2: Write ---
        print("[Stage 2/6] Write Draft")
        draft = self.writer.run(brief, full_slug)
        if not draft:
            print("Pipeline ABORTED: Draft generation failed.\n")
            return False
        print(f"  Draft written: {len(draft)} chars\n")

        # --- Stage 3: Fact-Check (with revision loop) ---
        print("[Stage 3/6] Fact-Check")
        for round_num in range(1, MAX_REVISION_ROUNDS + 2):
            report = self.fact_checker.run(draft, brief)

            if report.verdict == Verdict.PASS:
                print(f"  Fact-check PASSED (round {round_num})\n")
                break

            if report.verdict == Verdict.FAIL:
                print(f"  Fact-check FAILED (round {round_num}): "
                      f"{'; '.join(report.issues)}")
                print("Pipeline ABORTED: Too many unverified claims.\n")
                return False

            # NEEDS_REVISION
            if round_num > MAX_REVISION_ROUNDS:
                print(f"  Max revision rounds ({MAX_REVISION_ROUNDS}) exceeded. "
                      "Treating as FAIL.")
                print("Pipeline ABORTED.\n")
                return False

            print(f"  Fact-check: NEEDS_REVISION (round {round_num})")
            print(f"  Sending back to Writer for revision...")
            draft = self.writer.revise(draft, brief, report.revision_instructions)
            if not draft:
                print("Pipeline ABORTED: Revision failed.\n")
                return False
            print(f"  Revised draft: {len(draft)} chars")

        # --- Stage 4: Edit ---
        print("[Stage 4/6] Edit")
        final_ko = self.editor.run(draft, report)
        if not final_ko:
            print("Pipeline ABORTED: Editor rejected the post.\n")
            return False
        print(f"  Editing complete: {len(final_ko)} chars\n")

        # --- Stage 5: Generate Image ---
        print("[Stage 5/6] Generate Image")
        image_filename = self.image_generator.run(
            topic=brief.topic,
            summary=brief.summary,
            slug=full_slug,
        )
        if image_filename:
            print(f"  Image generated: images/{image_filename}\n")
        else:
            print("  Warning: Image generation skipped/failed. Post will have no image.")
            # Remove image field from front matter so template shows no-image style
            final_ko = self._strip_image_field(final_ko)
            print()

        # --- Stage 6: Translate ---
        print("[Stage 6/6] Translate")
        final_en = self.translator.run(final_ko, "en")
        final_ja = self.translator.run(final_ko, "ja")
        final_zh_cn = self.translator.run(final_ko, "zh-cn")
        final_zh_tw = self.translator.run(final_ko, "zh-tw")

        # --- Save ---
        print("\nSaving posts...")
        self._save_post(final_ko, full_slug, "ko")
        if final_en:
            self._save_post(final_en, full_slug, "en")
        else:
            print("  Warning: English translation failed.")
        if final_ja:
            self._save_post(final_ja, full_slug, "ja")
        else:
            print("  Warning: Japanese translation failed.")
        if final_zh_cn:
            self._save_post(final_zh_cn, full_slug, "zh-cn")
        else:
            print("  Warning: Simplified Chinese translation failed.")
        if final_zh_tw:
            self._save_post(final_zh_tw, full_slug, "zh-tw")
        else:
            print("  Warning: Traditional Chinese translation failed.")

        print(f"\n{'='*60}")
        print(f"  Pipeline Complete: {topic}")
        print(f"{'='*60}\n")
        return True

    def _make_slug(self, topic: str) -> str:
        """Create a URL-safe slug from the topic."""
        slug = re.sub(r"[^\w\s-]", "", topic).strip()
        slug = re.sub(r"[\s]+", "-", slug)
        # Keep only ASCII for filename safety
        slug = slug.encode("ascii", "ignore").decode("ascii")
        if not slug:
            slug = "post"
        return slug

    def _save_post(self, content: str, slug: str, lang: str):
        """Save a post file with the correct naming convention."""
        if lang == "ko":
            filename = f"{slug}.md"
        else:
            filename = f"{slug}.{lang}.md"

        # Korean gets a pretty permalink; other languages use Jekyll's default
        # (file-based) URL to avoid permalink collisions between translations
        if lang == "ko":
            content = self._ensure_permalink(content, slug)
        else:
            content = self._strip_permalink(content)
            content = self._strip_tags(content)

        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Saved: {filepath}")

    def _strip_image_field(self, content: str) -> str:
        """Remove image field from front matter when no image was generated."""
        return re.sub(r"^image:.*\n", "", content, count=1, flags=re.MULTILINE)

    def _strip_tags(self, content: str) -> str:
        """Remove tags field from front matter to avoid jekyll-tagging conflicts."""
        return re.sub(r"^tags:.*\n", "", content, count=1, flags=re.MULTILINE)

    def _strip_permalink(self, content: str) -> str:
        """Remove permalink field from front matter to avoid collision with Korean version."""
        return re.sub(r"^permalink:.*\n", "", content, count=1, flags=re.MULTILINE)

    def _ensure_permalink(self, content: str, slug: str) -> str:
        """Ensure the post has a permalink in front matter."""
        if "permalink:" in content:
            return content

        # Parse date from slug: YYYY-MM-DD-rest
        match = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.+)", slug)
        if not match:
            return content

        y, m, d, rest = match.groups()
        permalink = f"/{y}/{m}/{d}/{rest}/"

        # Inject before closing ---
        second_dash = content.find("---", 3)
        if second_dash != -1:
            content = (
                content[:second_dash]
                + f"permalink: {permalink}\n"
                + content[second_dash:]
            )
        return content
