"""Tests for the deploy watcher classifier + auto-fix handler.

No network, no gh shell-outs — we feed real-looking log snippets to
classify_deploy_error and create corrupted fixture files for
DeployFixerAgent.fix_yaml_front_matter.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from scripts.agents.deploy_fixer import (
    DeployFixerAgent,
    _count_unescaped_double_quotes,
    _repair_unterminated_strings,
    _split_front_matter,
)
from scripts.app.diagnostics import (
    DEPLOY_CATEGORIES,
    classify_deploy_error,
)


# ----------------------------------------------------------------------
# classify_deploy_error
# ----------------------------------------------------------------------


REAL_YAML_LOG = """
Configuration file: /home/runner/work/gipyeong-lee.github.io/gipyeong-lee.github.io/_config.yml
      Generating...
     Error: YAML Exception reading /home/runner/work/gipyeong-lee.github.io/gipyeong-lee.github.io/_posts/2026-04-09-ProductFeb-17-2026Introducing-Claude-Sonnet-46.ja.md: (<unknown>): did not find expected key while parsing a block mapping at line 2 column 1
  Liquid Exception: undefined method `length' for nil:NilClass in search.json
  Process completed with exit code 1.
"""


def test_classifier_prefers_yaml_over_cascading_liquid_error():
    d = classify_deploy_error(REAL_YAML_LOG)
    assert d.category == "yaml_parse_error"
    assert d.auto_apply is True
    assert d.fix_fn == "fix_yaml_front_matter"
    assert d.fix_params["path"].endswith("2026-04-09-ProductFeb-17-2026Introducing-Claude-Sonnet-46.ja.md")
    assert "did not find expected key" in d.fix_params["detail"]


def test_classifier_liquid_nil_method_no_auto_fix():
    log = (
        "Liquid Exception: undefined method `length' for nil:NilClass in "
        "search.json\nProcess completed with exit code 1."
    )
    d = classify_deploy_error(log)
    assert d.category == "liquid_nil_method"
    assert d.auto_apply is False  # templates shouldn't auto-edit
    assert "search.json" in d.evidence["file"]
    assert d.evidence["method"] == "length"


def test_classifier_bundle_install_failure():
    log = "Bundler::InstallError: Could not find gem 'foo' in any sources"
    d = classify_deploy_error(log)
    assert d.category == "bundle_install_failed"
    assert d.auto_apply is False


def test_classifier_actions_infrastructure():
    log = "The runner has received a shutdown signal."
    d = classify_deploy_error(log)
    assert d.category == "actions_infrastructure"


def test_classifier_unknown_falls_back():
    d = classify_deploy_error("nothing recognizable here")
    assert d.category == "unknown_deploy_failure"
    assert d.auto_apply is False


def test_classifier_empty_log():
    d = classify_deploy_error("")
    assert d.category == "unknown_deploy_failure"


def test_every_deploy_category_is_declared():
    # Every classifier branch returns a category in DEPLOY_CATEGORIES.
    for log, expected in [
        (REAL_YAML_LOG, "yaml_parse_error"),
        ("Liquid Exception: undefined method `X' for nil:NilClass in foo.liquid", "liquid_nil_method"),
        ("Bundler::InstallError: something", "bundle_install_failed"),
        ("EAI_AGAIN getaddrinfo github.com", "actions_infrastructure"),
        ("some random Jekyll Error happened\nexit code 1", "jekyll_build_failed"),
        ("garbage", "unknown_deploy_failure"),
    ]:
        d = classify_deploy_error(log)
        assert d.category == expected, f"{expected} != {d.category} for log: {log[:60]}"
        assert d.category in DEPLOY_CATEGORIES


# ----------------------------------------------------------------------
# Front matter repair helpers
# ----------------------------------------------------------------------


def test_split_front_matter_basic():
    content = '---\nkey: value\n---\nbody\n'
    front, body, _ = _split_front_matter(content)
    assert front is not None
    assert front.startswith("---")
    assert front.rstrip().endswith("---")
    assert body == "body\n"


def test_split_front_matter_no_delimiters():
    front, body, _ = _split_front_matter("no front matter here")
    assert front is None
    assert body == "no front matter here"


def test_count_unescaped_double_quotes():
    assert _count_unescaped_double_quotes('') == 0
    assert _count_unescaped_double_quotes('no quotes') == 0
    assert _count_unescaped_double_quotes('"open') == 1
    assert _count_unescaped_double_quotes('"closed"') == 2
    assert _count_unescaped_double_quotes('\\"escaped') == 0


def test_repair_unterminated_title():
    front = (
        '---\n'
        'layout: post\n'
        'title: "[技術分析] アンソロピック、「Claude Sonnet 4.6」を電撃公開\n'
        'description: "正常な説明文"\n'
        'lang: ja\n'
        '---\n'
    )
    repaired = _repair_unterminated_strings(front)
    assert repaired != front
    assert 'title: "[技術分析] アンソロピック、「Claude Sonnet 4.6」を電撃公開"\n' in repaired
    # Description stays untouched (it was balanced).
    assert 'description: "正常な説明文"\n' in repaired


def test_repair_is_noop_when_balanced():
    front = (
        '---\n'
        'layout: post\n'
        'title: "All good"\n'
        'description: "Also good"\n'
        '---\n'
    )
    assert _repair_unterminated_strings(front) == front


# ----------------------------------------------------------------------
# DeployFixerAgent.fix_yaml_front_matter (file IO round-trip)
# ----------------------------------------------------------------------


def test_fix_yaml_front_matter_roundtrip(tmp_path, monkeypatch):
    # Put the fixture inside a fake REPO_ROOT so the resolver accepts it.
    fake_repo = tmp_path / "repo"
    (fake_repo / "_posts").mkdir(parents=True)
    fixture = fake_repo / "_posts" / "2026-04-09-broken.ja.md"
    fixture.write_text(
        '---\n'
        'layout: post\n'
        'title: "壊れたタイトル\n'
        'description: "intact"\n'
        'lang: ja\n'
        '---\n'
        '\n'
        'body\n',
        encoding="utf-8",
    )

    # deploy_fixer uses REPO_ROOT from config; patch it for the duration of
    # the test so the CI-path resolver lands inside our fake repo.
    import scripts.agents.deploy_fixer as df
    monkeypatch.setattr(df, "REPO_ROOT", str(fake_repo))

    agent = DeployFixerAgent()
    ci_path = (
        "/home/runner/work/gipyeong-lee.github.io/gipyeong-lee.github.io/"
        "_posts/2026-04-09-broken.ja.md"
    )
    result = agent.dispatch(
        "fix_yaml_front_matter",
        {"path": ci_path, "detail": "did not find expected key"},
    )
    assert result.ok is True, result.detail
    assert result.modified_file is not None
    assert "broken.ja.md" in result.modified_file

    repaired = fixture.read_text(encoding="utf-8")
    assert 'title: "壊れたタイトル"\n' in repaired
    assert 'description: "intact"\n' in repaired

    import yaml
    # The front matter now parses — strip the `---` delimiters that
    # yaml.safe_load would otherwise treat as a multi-document marker.
    front, _, _ = _split_front_matter(repaired)
    interior = "".join(l for l in front.splitlines(keepends=True) if l.strip() != "---")
    assert yaml.safe_load(interior)["title"] == "壊れたタイトル"


def test_fix_yaml_front_matter_refuses_unknown_handler():
    agent = DeployFixerAgent()
    result = agent.dispatch("nonexistent_handler", {})
    assert result.ok is False
    assert "unknown fix_fn" in result.detail


def test_fix_yaml_front_matter_bails_on_missing_file(tmp_path, monkeypatch):
    import scripts.agents.deploy_fixer as df
    monkeypatch.setattr(df, "REPO_ROOT", str(tmp_path))
    agent = DeployFixerAgent()
    result = agent.dispatch(
        "fix_yaml_front_matter",
        {"path": "/home/runner/work/repo/repo/_posts/nope.md"},
    )
    assert result.ok is False
    assert "not found" in result.detail


def test_fix_yaml_front_matter_refuses_path_escape(tmp_path, monkeypatch):
    import scripts.agents.deploy_fixer as df
    fake_repo = tmp_path / "repo"
    fake_repo.mkdir()
    monkeypatch.setattr(df, "REPO_ROOT", str(fake_repo))
    agent = DeployFixerAgent()
    # A `..` escape should be rejected by the resolver's repo-root guard.
    result = agent.dispatch(
        "fix_yaml_front_matter",
        {"path": "../../../etc/passwd"},
    )
    assert result.ok is False
