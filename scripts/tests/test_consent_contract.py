"""Consent / CMP contract for the ad stack.

Every assertion here pins a condition behind the fix for the 2026-09
AdSense Policy Center issue "Consent requirement: narrow coverage" (TC
string missing from some EEA/UK/CH ad requests). If one breaks, the
design conclusion in its docstring is void.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.validate_learn import AD_MARKERS, validate_repo

ROOT = Path(__file__).resolve().parents[2]
HEAD = (ROOT / "_includes/head.html").read_text(encoding="utf-8")
CONSENT = (ROOT / "_includes/consent.html").read_text(encoding="utf-8")
ANALYTICS = (ROOT / "_includes/google-analytics.html").read_text(encoding="utf-8")

EU27 = {
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU",
    "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE",
}
EEA_UK_CH = EU27 | {"IS", "LI", "NO"} | {"GB"} | {"CH"}


def _rendered(text: str) -> str:
    """Normalise whitespace-control tags ({%- ... -%}) and drop Liquid
    comment blocks: neither reaches the built HTML."""
    text = re.sub(r"\{%-\s*", "{% ", text)
    text = re.sub(r"\s*-%\}", " %}", text)
    return re.sub(r"\{% comment %\}.*?\{% endcomment %\}", "", text, flags=re.S)


def _guarded(text: str) -> tuple[str, str]:
    """Split Liquid into (inside `unless page.no_ads`, outside it)."""
    blocks = _rendered(text).split("{% unless page.no_ads %}")
    inside = "".join(block.split("{% endunless %}", 1)[0] for block in blocks[1:])
    outside = blocks[0] + "".join(
        block.split("{% endunless %}", 1)[1] for block in blocks[1:]
    )
    return inside, outside


class ConsentContractTest(unittest.TestCase):
    def test_consent_bootstrap_is_the_first_script_in_head(self):
        """Consent defaults only count if pushed before gtag.js, and
        adsbygoogle.js only waits for the CMP if the googlefcPresent signal
        is raised before it starts requesting ads."""
        include_at = HEAD.index("{% include consent.html %}")
        self.assertLess(include_at, HEAD.index("<script"))
        self.assertLess(include_at, HEAD.index("adsbygoogle.js"))
        # gtag.js is loaded from the body include, i.e. after <head>.
        self.assertNotIn("gtag/js", HEAD)
        self.assertIn("googletagmanager.com/gtag/js", ANALYTICS)

    def test_privacy_messaging_tag_precedes_adsense_loader(self):
        """Google's tag: fundingchoicesmessages script, then the
        googlefcPresent iframe signal adsbygoogle.js looks for."""
        self.assertIn(
            "https://fundingchoicesmessages.google.com/i/"
            "{{ site.data.settings.google.adsense_id | remove_first: 'ca-' }}?ers=1",
            CONSENT,
        )
        self.assertIn("iframe.name = 'googlefcPresent'", CONSENT)
        self.assertLess(
            CONSENT.index("fundingchoicesmessages.google.com/i/"),
            CONSENT.index("signalGooglefcPresent();"),
        )
        self.assertIn('rel="preconnect" href="https://fundingchoicesmessages.google.com"', HEAD)

    def test_cmp_tag_is_omitted_on_no_ads_pages_but_consent_defaults_stay(self):
        """Learn pages ship no ad stack at all (validate_learn contract);
        GA4 still runs there, so consent defaults must stay unconditional."""
        inside, outside = _guarded(CONSENT)
        self.assertIn("fundingchoicesmessages.google.com", inside)
        self.assertIn("googlefcPresent", inside)
        self.assertNotIn("fundingchoicesmessages", outside)
        self.assertNotIn("googlefcPresent", outside)
        self.assertIn("gtag('consent', 'default'", outside)
        head_inside, _ = _guarded(HEAD)
        self.assertIn("fundingchoicesmessages.google.com", head_inside)

    def test_consent_mode_v2_defaults_denied_in_eea_uk_ch_and_granted_elsewhere(self):
        """Google Consent Mode v2 needs all four signals; the regional
        default must cover exactly EEA + UK + CH (the regions Google's EU
        user consent policy applies to) and nothing else, so non-European
        traffic keeps today's behaviour."""
        defaults = re.findall(r"gtag\('consent', 'default', \{(.*?)\}\);", CONSENT, re.S)
        self.assertEqual(len(defaults), 2, defaults)
        regional, everywhere = defaults
        for signal in ("ad_storage", "ad_user_data", "ad_personalization", "analytics_storage"):
            self.assertIn(f"'{signal}': 'denied'", regional)
            self.assertIn(f"'{signal}': 'granted'", everywhere)
        self.assertNotIn("region", everywhere)
        region_list = regional.split("'region':", 1)[1]
        self.assertEqual(set(re.findall(r"'([A-Z]{2})'", region_list)), EEA_UK_CH)
        self.assertIn("'wait_for_update': 2000", regional)
        self.assertIn("gtag('set', 'ads_data_redaction', true);", CONSENT)
        # url_passthrough rewrites outbound link URLs; never wanted on a blog.
        self.assertNotIn("url_passthrough", CONSENT)

    def test_learn_validator_rejects_cmp_markers_in_built_html(self):
        """The CMP is part of the ad stack: a learn page that loads it has
        leaked ads-only resources."""
        self.assertIn("fundingchoicesmessages.google.com", AD_MARKERS)
        self.assertIn("googlefcPresent", AD_MARKERS)
        with TemporaryDirectory() as directory:
            repo = Path(directory) / "repo"
            data_dir = repo / "_data" / "learn"
            data_dir.mkdir(parents=True)
            (data_dir / "courses.yml").write_text("[]\n", encoding="utf-8")
            site = Path(directory) / "site" / "learn"
            site.mkdir(parents=True)
            (site / "index.html").write_text(
                '<script async src="https://fundingchoicesmessages.google.com/i/pub-1?ers=1"></script>',
                encoding="utf-8",
            )
            errors = validate_repo(repo, site_dir=site.parent)
            self.assertTrue(
                any("advertising marker fundingchoicesmessages.google.com" in error for error in errors),
                errors,
            )


class PrivacyPolicyContractTest(unittest.TestCase):
    """The EU user consent policy audit expects the site to disclose how
    Google uses data (with a link to Google's business data responsibility
    site), to say that TCF Purpose 1 consent also covers analytics storage
    (required for the AdSense "consent mode for analytics" setting), and to
    let users withdraw consent from every page."""

    KO = ROOT / "_pages/privacy.md"
    EN = ROOT / "_pages/privacy.en.md"
    FOOTER = (ROOT / "_includes/footer.html").read_text(encoding="utf-8")

    def _front_matter(self, path: Path) -> str:
        return path.read_text(encoding="utf-8").split("---", 2)[1]

    def test_privacy_policy_exists_in_korean_and_english_and_cross_links(self):
        ko, en = self._front_matter(self.KO), self._front_matter(self.EN)
        self.assertIn("permalink: /privacy/\n", ko)
        self.assertIn("permalink: /privacy/en/\n", en)
        self.assertIn("lang: ko", ko)
        self.assertIn("lang: en", en)
        for fm in (ko, en):
            self.assertIn("ref: privacy", fm)
            self.assertIn("url: /privacy/\n", fm)
            self.assertIn("url: /privacy/en/\n", fm)
            self.assertNotIn("no_ads", fm)  # revocation control needs googlefc

    def test_privacy_policy_discloses_google_data_use_and_consent_scope(self):
        for path, purpose_one in ((self.KO, "TCF 목적 1"), (self.EN, "TCF Purpose 1")):
            body = path.read_text(encoding="utf-8")
            for required in (
                "Google Analytics",
                "AdSense",
                "https://policies.google.com/technologies/partner-sites",
                "https://business.safety.google/privacy/",
                "https://adssettings.google.com",
                "https://tools.google.com/dlpage/gaoptout",
                "data-consent-revoke",
                purpose_one,
            ):
                self.assertIn(required, body, f"{path.name} lacks {required!r}")

    def test_footer_links_policy_everywhere_and_revocation_only_with_ad_stack(self):
        inside, outside = _guarded(self.FOOTER)
        self.assertIn("/privacy/", outside)
        self.assertIn("data-consent-revoke", inside)
        self.assertIn("googlefc.showRevocationMessage()", inside)
        self.assertIn("CONSENT_DATA_READY", inside)
        # Fallback when the kernel does not export showRevocationMessage:
        # clear Google CMP's first-party consent cookies and reload.
        for cookie in ("FCCDCF", "FCNEC"):
            self.assertIn(cookie, inside)
        self.assertIn("location.reload()", inside)
        self.assertIn("data.gdprApplies", inside)
        self.assertNotIn("data-consent-revoke", outside)
        self.assertNotIn("showRevocationMessage", outside)


if __name__ == "__main__":
    unittest.main()
