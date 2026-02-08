"""Translator Agent — translates posts to English and Japanese."""

import re
from typing import Optional

from .base import BaseAgent


class TranslatorAgent(BaseAgent):
    name = "Translator"
    prompt_file = "translator_system.md"

    LANG_MAP = {
        "en": "English",
        "ja": "Japanese",
    }

    REF_SECTION_MAP = {
        "en": "## References",
        "ja": "## 参考資料",
    }

    def run(self, content: str, target_lang: str) -> Optional[str]:
        """Translate content to the target language.

        Args:
            content: The Korean markdown post content.
            target_lang: Language code ("en" or "ja").

        Returns:
            Translated markdown content with corrected front matter.
        """
        lang_name = self.LANG_MAP.get(target_lang)
        if not lang_name:
            self.log(f"Unsupported target language: {target_lang}")
            return None

        self.log(f"Translating to {lang_name}...")
        system_prompt = self.get_system_prompt()

        prompt = f"""{system_prompt}

## TARGET LANGUAGE
{lang_name}

## CONTENT TO TRANSLATE
{content}

Translate the above content to {lang_name}.
Output ONLY the translated markdown starting with `---`."""

        translated = self.gemini.call(prompt)
        if not translated:
            self.log(f"Translation to {lang_name} failed.")
            return None

        translated = self._clean_output(translated)

        # Force-replace lang field (don't trust Gemini)
        translated = self._force_lang_field(translated, target_lang)

        # Ensure reference section header is translated
        translated = self._fix_reference_header(translated, target_lang)

        return translated

    def _clean_output(self, text: str) -> str:
        text = re.sub(r"^```(?:markdown|yaml)?\s*", "", text)
        text = re.sub(r"^```\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
        return text.strip()

    def _force_lang_field(self, content: str, target_lang: str) -> str:
        """Programmatically force the lang field in front matter."""
        # Match lang field in front matter
        pattern = r"(^---\n.*?)lang:\s*\w+(.*?^---)"
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if match:
            content = re.sub(
                r"(lang:\s*)\w+",
                f"\\g<1>{target_lang}",
                content,
                count=1,
            )
        else:
            # If no lang field, inject it before the closing ---
            second_dash = content.find("---", 3)
            if second_dash != -1:
                content = (
                    content[:second_dash]
                    + f"lang: {target_lang}\n"
                    + content[second_dash:]
                )
        return content

    def _fix_reference_header(self, content: str, target_lang: str) -> str:
        """Ensure the references section header is in the target language."""
        target_header = self.REF_SECTION_MAP.get(target_lang, "## References")
        # Replace any variant of the references header
        content = re.sub(
            r"## (?:참고자료|References|参考資料|참고 자료)",
            target_header,
            content,
        )
        return content
