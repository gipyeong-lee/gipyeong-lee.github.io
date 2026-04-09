"""Deploy Fixer Agent — self-healing handlers for GitHub Pages deploy failures.

Sibling of diagnostics.py's in-process auto-fix functions, but scoped to
*repository* fixes (as opposed to Topic / database mutations). Each
handler:

1. Takes a DeployDiagnosis-like object (path + detail from the log).
2. Reads the affected file from the working tree (NOT the CI workspace —
   paths in the log are translated to the local repo root).
3. Attempts a targeted repair and verifies it with `yaml.safe_load` or
   an equivalent sanity check.
4. Returns a tuple `(ok: bool, detail: str)`.

The deploy_watcher calls `dispatch(fn_name, params)` and, on success,
stages + commits + pushes the fix itself. Keeping the handler side-effect-
free (no git operations) makes unit testing trivial.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

import yaml

from .base import BaseAgent
from ..app.config import REPO_ROOT


# CI workspace paths have this prefix on GitHub-hosted runners. We strip
# it so we can read the file at the equivalent local path.
_CI_PATH_PREFIX_RE = re.compile(
    r"^/home/runner/work/[^/]+/[^/]+/"
)


@dataclass
class FixResult:
    ok: bool
    detail: str
    # Relative path (from repo root) of any file the handler modified.
    modified_file: Optional[str] = None


class DeployFixerAgent(BaseAgent):
    """Apply safe, rule-based repairs to files that broke the deploy."""

    name = "DeployFixer"
    prompt_file = ""

    # ------------------------------------------------------------------
    # Dispatcher
    # ------------------------------------------------------------------

    def dispatch(self, fix_fn: str, params: dict) -> FixResult:
        """Run the named handler with the given params. Never raises."""
        handler = _DISPATCH.get(fix_fn)
        if handler is None:
            return FixResult(ok=False, detail=f"unknown fix_fn: {fix_fn}")
        try:
            return handler(self, params)
        except Exception as e:
            self.log(f"handler {fix_fn} crashed: {e}")
            return FixResult(ok=False, detail=f"handler crashed: {e}")

    # ------------------------------------------------------------------
    # Handlers
    # ------------------------------------------------------------------

    def fix_yaml_front_matter(self, params: dict) -> FixResult:
        """Repair a Jekyll post's YAML front matter.

        The most common failure (observed in production as of 2026-04-09)
        is an unterminated double-quoted string — typically the `title`
        field on a translated post, where Gemini's translation cut off
        the closing quote. Detection strategy:

        1. Resolve the CI path to the local repo path.
        2. Read the file, extract the front matter block.
        3. For each `key: "...` line inside the front matter, count
           unescaped double quotes. If the count is odd, that line has
           an unterminated string — append `"` right before the trailing
           newline of that line.
        4. Re-validate with `yaml.safe_load`. If it parses, write back.

        This is intentionally narrow. It will not touch:
        - Keys with single-quoted strings (Gemini rarely produces them)
        - Multi-line strings (not used in our front matter schema)
        - Unquoted values
        - Any field outside the `---` delimited front matter block
        """
        raw_path = params.get("path") or ""
        local_path = _resolve_repo_path(raw_path)
        if local_path is None:
            return FixResult(ok=False, detail=f"cannot resolve CI path: {raw_path}")
        if not local_path.exists():
            return FixResult(
                ok=False, detail=f"file not found in local repo: {local_path}"
            )

        try:
            content = local_path.read_text(encoding="utf-8")
        except Exception as e:
            return FixResult(ok=False, detail=f"read failed: {e}")

        front, body, sep_idx = _split_front_matter(content)
        if front is None:
            return FixResult(
                ok=False, detail="file has no `---` delimited front matter"
            )

        # yaml.safe_load chokes on the wrapping `---` because it treats
        # them as multi-document markers. Strip them before validation.
        def _interior(fm: str) -> str:
            lines = fm.splitlines(keepends=True)
            return "".join(l for l in lines if l.strip() != "---")

        # Fast path: is it already valid?
        try:
            yaml.safe_load(_interior(front))
            return FixResult(
                ok=False,
                detail="front matter already parses — log may be stale",
            )
        except yaml.YAMLError:
            pass  # proceed to repair

        repaired_front = _repair_unterminated_strings(front)
        if repaired_front == front:
            return FixResult(
                ok=False,
                detail="no unterminated-string lines found; needs manual fix",
            )

        try:
            yaml.safe_load(_interior(repaired_front))
        except yaml.YAMLError as e:
            return FixResult(
                ok=False,
                detail=f"repair did not yield valid YAML: {e}",
            )

        new_content = repaired_front + content[len(front):]
        try:
            local_path.write_text(new_content, encoding="utf-8")
        except Exception as e:
            return FixResult(ok=False, detail=f"write failed: {e}")

        rel = local_path.relative_to(REPO_ROOT)
        self.log(f"repaired YAML front matter: {rel}")
        return FixResult(
            ok=True,
            detail=f"appended missing closing quote in {rel.name}",
            modified_file=str(rel),
        )


# ----------------------------------------------------------------------
# Internal helpers
# ----------------------------------------------------------------------


def _resolve_repo_path(ci_path: str) -> Optional[Path]:
    """Translate /home/runner/work/<repo>/<repo>/foo.md → <REPO_ROOT>/foo.md."""
    if not ci_path:
        return None
    # Strip CI prefix if present.
    stripped = _CI_PATH_PREFIX_RE.sub("", ci_path)
    # If the path came in already relative, just use it as-is.
    candidate = (Path(REPO_ROOT) / stripped).resolve()
    # Safety: ensure the path is still inside the repo root (no ../.. escapes).
    try:
        candidate.relative_to(Path(REPO_ROOT).resolve())
    except ValueError:
        return None
    return candidate


def _split_front_matter(content: str) -> tuple[Optional[str], str, int]:
    """Return (front_matter_including_delimiters, body_after, sep_idx).

    front_matter is `---\\n...\\n---\\n` (the full block including the two
    `---` lines). Returns `(None, content, -1)` if the document does not
    start with `---`.
    """
    if not content.startswith("---"):
        return None, content, -1
    # Find the *second* `---` line (end of front matter).
    second = content.find("\n---", 3)
    if second == -1:
        return None, content, -1
    end = content.find("\n", second + 4)
    if end == -1:
        # No trailing newline after the closing `---` — malformed.
        end = len(content)
    front = content[: end + 1]
    body = content[end + 1 :]
    return front, body, end


# Matches lines inside the front matter that have a `key: "...` pattern.
# The closing `"` may be present on the SAME line (balanced) or missing.
_KV_DOUBLE_QUOTE_RE = re.compile(
    r'^(?P<key>[A-Za-z_][\w-]*)\s*:\s*"(?P<rest>.*)$'
)


def _repair_unterminated_strings(front: str) -> str:
    """Scan front-matter lines; append `"` to any line whose double-quoted
    value lacks a closing quote. Idempotent on already-balanced lines.
    """
    lines = front.splitlines(keepends=True)
    out_lines: list[str] = []
    changed = False
    for line in lines:
        stripped = line.rstrip("\r\n")
        if stripped in ("---", ""):
            out_lines.append(line)
            continue
        m = _KV_DOUBLE_QUOTE_RE.match(stripped)
        if not m:
            out_lines.append(line)
            continue
        rest = m.group("rest")
        # Count unescaped double quotes in `rest`. An unescaped quote is
        # one NOT preceded by a backslash. YAML doesn't use backslash
        # escaping the same way Python does, but Gemini-produced posts
        # don't embed literal quotes inside strings, so a simple count is
        # accurate in practice.
        quote_count = _count_unescaped_double_quotes(rest)
        # Opening `"` is consumed by the regex; rest must have exactly 1
        # closing `"` to be balanced. 0 means unterminated.
        if quote_count == 0:
            # Repair: append `"` before the line terminator.
            newline = ""
            if line.endswith("\r\n"):
                newline = "\r\n"
            elif line.endswith("\n"):
                newline = "\n"
            repaired = stripped + '"' + newline
            out_lines.append(repaired)
            changed = True
        else:
            out_lines.append(line)
    return "".join(out_lines) if changed else front


def _count_unescaped_double_quotes(s: str) -> int:
    count = 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s):
            i += 2
            continue
        if ch == '"':
            count += 1
        i += 1
    return count


# Dispatcher map: fix_fn name → (agent_self, params) → FixResult.
_Handler = Callable[["DeployFixerAgent", dict], FixResult]

_DISPATCH: dict[str, _Handler] = {
    "fix_yaml_front_matter": DeployFixerAgent.fix_yaml_front_matter,
}
