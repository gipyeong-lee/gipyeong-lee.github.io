"""Writer Agent — generates a blog post draft from verified research."""

import datetime
import re
from typing import Optional

from .base import BaseAgent
from ..models import ResearchBrief


class WriterAgent(BaseAgent):
    name = "Writer"
    prompt_file = "writer_system.md"

    def run(self, brief: ResearchBrief, slug: str) -> Optional[str]:
        """Write a blog post draft using only the ResearchBrief as source."""
        self.log(f"Writing draft for: {brief.topic}")
        draft = self._generate_draft(brief, slug)
        if not draft:
            self.log("Draft generation failed.")
            return None

        draft = self._clean_output(draft)
        return draft

    def revise(self, draft: str, brief: ResearchBrief, instructions: str) -> Optional[str]:
        """Revise a draft based on fact-checker instructions."""
        self.log("Revising draft based on fact-check feedback...")

        source_table = self._build_source_table(brief)
        prompt = f"""You are a professional tech journalist revising a blog post.

## REVISION INSTRUCTIONS
{instructions}

## SOURCE TABLE (only these URLs may be cited)
{source_table}

## CURRENT DRAFT
{draft}

## RULES
1. Fix the issues described in the revision instructions.
2. Do NOT add any new URLs not in the source table.
3. Do NOT add new factual claims not supported by the source table.
4. Remove or rephrase any unsupported claims.
5. Keep the `## 참고자료` section updated with all cited sources.
6. Output ONLY the revised markdown starting with front matter `---`.
"""
        revised = self.gemini.call(prompt)
        if not revised:
            return None
        return self._clean_output(revised)

    def _generate_draft(self, brief: ResearchBrief, slug: str) -> Optional[str]:
        """Generate the initial draft."""
        system_prompt = self.get_system_prompt()
        source_table = self._build_source_table(brief)
        facts_text = self._build_facts_text(brief)
        today = datetime.date.today().strftime("%Y-%m-%d")

        prompt = f"""{system_prompt}

## TOPIC
{brief.topic}

## RESEARCH SUMMARY
{brief.summary}

## SOURCE TABLE (ONLY these URLs may be cited)
{source_table}

## KEY FACTS (with source references)
{facts_text}

## POST METADATA
- slug: {slug}
- date: {today}
- image: {slug}.jpg
- lang: ko
- ref: {slug}

Write a complete blog post in Korean. Every factual claim MUST cite a source from the table above.
Include a `## 참고자료` section at the end.
Output ONLY the markdown content starting with `---`."""

        return self.gemini.call(prompt)

    def _build_source_table(self, brief: ResearchBrief) -> str:
        """Build a formatted source table for the prompt."""
        lines = []
        for s in brief.verified_sources:
            lines.append(f"[Source {s.index}] {s.title}")
            lines.append(f"  URL: {s.url}")
            lines.append(f"  Snippet: {s.snippet}")
            lines.append("")
        return "\n".join(lines)

    def _build_facts_text(self, brief: ResearchBrief) -> str:
        """Build a formatted facts list for the prompt."""
        lines = []
        for section_name, facts in [
            ("Key Facts", brief.key_facts),
            ("Statistics", brief.statistics),
            ("Expert Quotes", brief.expert_quotes),
        ]:
            if facts:
                lines.append(f"### {section_name}")
                for f in facts:
                    refs = ", ".join(f"Source {i}" for i in f.source_indices)
                    lines.append(f"- {f.statement} [{refs}]")
                lines.append("")
        return "\n".join(lines)

    def _clean_output(self, text: str) -> str:
        """Remove markdown code fences and clean up output."""
        text = re.sub(r"^```(?:markdown|yaml)?\s*", "", text)
        text = re.sub(r"^```\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
        return text.strip()
