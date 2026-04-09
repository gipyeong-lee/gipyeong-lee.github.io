"""Base agent with Gemini CLI wrapper."""

import json
import os
import re
import subprocess
import time
from typing import Optional, Union

MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds


class GeminiCLI:
    """Wrapper for calling the Gemini CLI."""

    @staticmethod
    def call(prompt: str) -> str:
        """Call Gemini CLI with retries on transient API errors."""
        for attempt in range(1, MAX_RETRIES + 1):
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
                    if attempt < MAX_RETRIES:
                        delay = RETRY_DELAY * attempt
                        print(f"  [Gemini CLI] Attempt {attempt} failed, retrying in {delay}s...")
                        time.sleep(delay)
                        continue
                    print(f"  [Gemini CLI Error] {stderr}")
                    return ""

                return stdout.strip()
            except FileNotFoundError:
                print("  [Error] 'gemini' CLI not found. Is it installed and on PATH?")
                return ""
            except Exception as e:
                if attempt < MAX_RETRIES:
                    delay = RETRY_DELAY * attempt
                    print(f"  [Gemini CLI] Attempt {attempt} error: {e}, retrying in {delay}s...")
                    time.sleep(delay)
                    continue
                print(f"  [Error] Gemini CLI call failed: {e}")
                return ""
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


class CodexCLI:
    """Wrapper for calling the OpenAI Codex CLI in non-interactive mode.

    Parallel to GeminiCLI — any agent can opt in by using `self.codex`
    instead of `self.gemini`. Codex is generally stronger on code-heavy
    tasks (refactoring, structured output), while Gemini remains the
    default for creative / multilingual Korean text (the blog pipeline).

    The daemon runs both subscriptions, so either backend is free to use
    at runtime. Claude is intentionally NOT wrapped here: per user policy,
    Claude is dev-only and should not appear in the pipeline.
    """

    @staticmethod
    def call(prompt: str) -> str:
        """Call `codex exec` with the prompt on stdin. Returns stdout."""
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                process = subprocess.Popen(
                    ["codex", "exec", "-"],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
                stdout, stderr = process.communicate(input=prompt)

                if process.returncode != 0:
                    if attempt < MAX_RETRIES:
                        delay = RETRY_DELAY * attempt
                        print(f"  [Codex CLI] Attempt {attempt} failed, retrying in {delay}s...")
                        time.sleep(delay)
                        continue
                    print(f"  [Codex CLI Error] {stderr}")
                    return ""

                return stdout.strip()
            except FileNotFoundError:
                print("  [Error] 'codex' CLI not found. Is it installed and on PATH?")
                return ""
            except Exception as e:
                if attempt < MAX_RETRIES:
                    delay = RETRY_DELAY * attempt
                    print(f"  [Codex CLI] Attempt {attempt} error: {e}, retrying in {delay}s...")
                    time.sleep(delay)
                    continue
                print(f"  [Error] Codex CLI call failed: {e}")
                return ""
        return ""

    @staticmethod
    def call_json(prompt: str) -> Optional[Union[dict, list]]:
        raw = CodexCLI.call(prompt)
        if not raw:
            return None
        cleaned = re.sub(r"^```(?:json)?\s*", "", raw)
        cleaned = re.sub(r"\s*```$", "", cleaned)
        cleaned = cleaned.strip()
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            match = re.search(r"[\[{].*[\]}]", cleaned, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group())
                except json.JSONDecodeError:
                    pass
            print(f"  [Warning] Failed to parse JSON from Codex response.")
            return None


class BaseAgent:
    """Base class for all pipeline agents."""

    name: str = "BaseAgent"
    prompt_file: str = ""

    def __init__(self):
        # Both CLI backends are attached so each agent can pick per-call.
        # Default choice across the codebase is Gemini (see existing agents);
        # Codex is available for structured / code-heavy tasks.
        self.gemini = GeminiCLI()
        self.codex = CodexCLI()
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
