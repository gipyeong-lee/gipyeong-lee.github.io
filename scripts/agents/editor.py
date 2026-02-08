"""Editor Agent — polishes fact-checked drafts for publication."""

import re
from typing import Optional

from .base import BaseAgent
from ..models import Verdict, FactCheckReport


class EditorAgent(BaseAgent):
    name = "Editor"
    prompt_file = "editor_system.md"

    def run(self, draft: str, fact_report: FactCheckReport) -> Optional[str]:
        """Edit and polish a fact-checked draft.

        Returns the final publication-ready markdown, or None if rejected.
        """
        # Gate: reject if fact-check failed
        if fact_report.verdict == Verdict.FAIL:
            self.log(
                f"REJECTED — Fact-check verdict is FAIL. "
                f"Issues: {'; '.join(fact_report.issues)}"
            )
            return None

        self.log("Polishing draft for publication...")
        system_prompt = self.get_system_prompt()

        prompt = f"""{system_prompt}

## DRAFT TO EDIT
{draft}

## FACT-CHECK SUMMARY
- Claims checked: {fact_report.claims_checked}
- Claims verified: {fact_report.claims_verified}
- Verdict: {fact_report.verdict.value}

Polish this draft for publication. Fix grammar, improve flow, ensure structure.
Do NOT add new facts or citations. Preserve all existing citations and the 참고자료 section.
Output ONLY the final markdown starting with `---`."""

        result = self.gemini.call(prompt)
        if not result:
            self.log("Editing failed.")
            return None

        result = self._clean_output(result)

        # Verify essential sections exist
        if "## 참고자료" not in result and "## References" not in result:
            self.log("Warning: 참고자료 section missing after edit. Restoring from draft.")
            ref_match = re.search(r"(## 참고자료.*)", draft, re.DOTALL)
            if ref_match:
                result = result.rstrip() + "\n\n" + ref_match.group(1)

        return result

    def _clean_output(self, text: str) -> str:
        text = re.sub(r"^```(?:markdown|yaml)?\s*", "", text)
        text = re.sub(r"^```\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
        return text.strip()
