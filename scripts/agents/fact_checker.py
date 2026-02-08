"""Fact Checker Agent — verifies claims against research and re-validates URLs."""

import re
from typing import List

from .base import BaseAgent
from ..models import ResearchBrief, Claim, FactCheckReport, Verdict
from ..url_validator import validate_urls


class FactCheckerAgent(BaseAgent):
    name = "FactChecker"
    prompt_file = "fact_checker_system.md"

    def run(self, draft: str, brief: ResearchBrief) -> FactCheckReport:
        """Fact-check a draft against the research brief."""
        self.log("Starting fact-check...")

        # 1. Extract claims from the draft
        claims = self._extract_claims(draft)
        self.log(f"Extracted {len(claims)} claims from draft.")

        # 2. Check that cited URLs are in verified sources
        source_urls = brief.get_source_urls()
        self._check_url_membership(claims, source_urls)

        # 3. Verify claims against research facts
        self._verify_claims(claims, brief)

        # 4. Re-validate all URLs in the draft
        dead_links = self._revalidate_draft_urls(draft)

        # 5. Build report
        return self._build_report(claims, dead_links)

    def _extract_claims(self, draft: str) -> List[Claim]:
        """Use Gemini to extract factual claims from the draft."""
        system_prompt = self.get_system_prompt()
        prompt = f"""{system_prompt}

## TASK
Extract all factual claims from this blog post draft. (TASK 1)

## DRAFT
{draft}

Return valid JSON with the claims array."""

        data = self.gemini.call_json(prompt)
        if not data or not isinstance(data, dict):
            self.log("Failed to extract claims.")
            return []

        claims = []
        for item in data.get("claims", []):
            if isinstance(item, dict):
                claims.append(
                    Claim(
                        text=item.get("text", ""),
                        cited_url=item.get("cited_url"),
                    )
                )
        return claims

    def _check_url_membership(self, claims: List[Claim], source_urls: set):
        """Check that cited URLs in claims are from verified sources."""
        for claim in claims:
            if claim.cited_url:
                if claim.cited_url not in source_urls:
                    claim.issue = f"URL not in verified sources: {claim.cited_url}"

    def _verify_claims(self, claims: List[Claim], brief: ResearchBrief):
        """Use Gemini to verify each claim against research facts."""
        # Build facts reference
        all_facts = brief.key_facts + brief.statistics + brief.expert_quotes
        facts_text = "\n".join(
            f"- {f.statement}" for f in all_facts
        )

        claims_text = "\n".join(
            f"{i+1}. {c.text}" for i, c in enumerate(claims)
        )

        prompt = f"""You are a fact-checker. Verify each claim against the research facts below.

## RESEARCH FACTS
{facts_text}

## CLAIMS TO VERIFY
{claims_text}

For each claim, determine if it is supported by the research facts.
A claim is "supported" if its core factual content is consistent with at least one research fact.
Opinions and subjective analysis (clearly marked as AI opinion) should be marked as supported.

Return valid JSON:
{{
  "verifications": [
    {{"claim_index": 1, "supported": true, "reason": "Matches fact about..."}},
    {{"claim_index": 2, "supported": false, "reason": "No matching fact found"}}
  ]
}}"""

        data = self.gemini.call_json(prompt)
        if not data or not isinstance(data, dict):
            self.log("Failed to verify claims.")
            return

        for v in data.get("verifications", []):
            if not isinstance(v, dict):
                continue
            idx = v.get("claim_index", 0) - 1
            if 0 <= idx < len(claims):
                claims[idx].matches_source = v.get("supported", False)
                if not v.get("supported", False) and not claims[idx].issue:
                    claims[idx].issue = v.get("reason", "Unsupported claim")

    def _revalidate_draft_urls(self, draft: str) -> List[str]:
        """Find all URLs in the draft and re-validate them."""
        urls = re.findall(r"https?://[^\s\)\]\"'>]+", draft)
        unique_urls = list(set(urls))

        if not unique_urls:
            return []

        self.log(f"Re-validating {len(unique_urls)} URLs in draft...")
        results = validate_urls(unique_urls, max_workers=5)
        dead = [url for url, is_live, _ in results if not is_live]

        if dead:
            self.log(f"Found {len(dead)} dead links in draft.")
        return dead

    def _build_report(self, claims: List[Claim], dead_links: List[str]) -> FactCheckReport:
        """Build the final fact-check report."""
        verified = sum(1 for c in claims if c.matches_source is True and not c.issue)
        unverified = sum(1 for c in claims if c.matches_source is False or c.issue)
        issues = [c.issue for c in claims if c.issue]

        # Determine verdict
        if not claims:
            verdict = Verdict.FAIL
            issues.append("No claims could be extracted from the draft.")
        elif dead_links:
            verdict = Verdict.NEEDS_REVISION
            issues.extend(f"Dead link: {url}" for url in dead_links)
        elif unverified > len(claims) * 0.3:
            verdict = Verdict.FAIL
            issues.append(
                f"Too many unverified claims: {unverified}/{len(claims)} "
                f"({unverified/len(claims)*100:.0f}%)"
            )
        elif unverified > 0:
            verdict = Verdict.NEEDS_REVISION
        else:
            verdict = Verdict.PASS

        # Build revision instructions
        revision_instructions = None
        if verdict == Verdict.NEEDS_REVISION:
            instructions = ["Fix the following issues in the draft:\n"]
            for issue in issues:
                instructions.append(f"- {issue}")
            instructions.append(
                "\nRemove or rephrase unsupported claims. "
                "Replace dead links with working alternatives from the verified sources."
            )
            revision_instructions = "\n".join(instructions)

        report = FactCheckReport(
            verdict=verdict,
            claims_checked=len(claims),
            claims_verified=verified,
            claims_unverified=unverified,
            dead_links=dead_links,
            issues=issues,
            revision_instructions=revision_instructions,
        )

        self.log(
            f"Verdict: {verdict.value} | "
            f"Checked: {len(claims)}, Verified: {verified}, Unverified: {unverified}"
        )
        return report
