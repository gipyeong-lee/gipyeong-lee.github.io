"""Base agent with Gemini CLI wrapper."""

import json
import os
import re
import subprocess
from typing import Optional, Union


class GeminiCLI:
    """Wrapper for calling the Gemini CLI."""

    @staticmethod
    def call(prompt: str) -> str:
        """Call Gemini CLI with the given prompt and return the response."""
        try:
            process = subprocess.Popen(
                ["gemini"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            stdout, stderr = process.communicate(input=prompt)

            if process.returncode != 0:
                print(f"  [Gemini CLI Error] {stderr}")
                return ""

            return stdout.strip()
        except FileNotFoundError:
            print("  [Error] 'gemini' CLI not found. Is it installed and on PATH?")
            return ""
        except Exception as e:
            print(f"  [Error] Gemini CLI call failed: {e}")
            return ""

    @staticmethod
    def call_json(prompt: str) -> Optional[Union[dict, list]]:
        """Call Gemini CLI and parse the response as JSON.

        Attempts to extract JSON from the response even if wrapped in
        markdown code blocks.
        """
        raw = GeminiCLI.call(prompt)
        if not raw:
            return None

        # Strip markdown code fences
        cleaned = re.sub(r"^```(?:json)?\s*", "", raw)
        cleaned = re.sub(r"\s*```$", "", cleaned)
        cleaned = cleaned.strip()

        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            # Try to find JSON within the response
            match = re.search(r"[\[{].*[\]}]", cleaned, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group())
                except json.JSONDecodeError:
                    pass
            print(f"  [Warning] Failed to parse JSON from Gemini response.")
            return None


class BaseAgent:
    """Base class for all pipeline agents."""

    name: str = "BaseAgent"
    prompt_file: str = ""

    def __init__(self):
        self.gemini = GeminiCLI()
        self._system_prompt = None

    def get_system_prompt(self) -> str:
        """Load the system prompt from the prompts directory."""
        if self._system_prompt is None:
            prompts_dir = os.path.join(os.path.dirname(__file__), "..", "prompts")
            path = os.path.join(prompts_dir, self.prompt_file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self._system_prompt = f.read()
            except FileNotFoundError:
                print(f"  [Warning] Prompt file not found: {path}")
                self._system_prompt = ""
        return self._system_prompt

    def log(self, message: str):
        print(f"  [{self.name}] {message}")
