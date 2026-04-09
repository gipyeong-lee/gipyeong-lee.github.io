"""VideoAnimatorAgent tests — pure-Python, no torch / diffusers needed.

Covers:
- prompt builder (topic-only and topic + summary, summary truncation)
- runner path resolution
- _parse_duration on the OK marker
- run() failure paths (missing image, missing runner, subprocess non-zero,
  small output) without invoking the real LTX model
"""
from __future__ import annotations

import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest

from scripts.agents.video_animator import VideoAnimatorAgent


# ----------------------------------------------------------------------
# build_prompt_from_post
# ----------------------------------------------------------------------


def test_build_prompt_topic_only():
    p = VideoAnimatorAgent.build_prompt_from_post(topic="Claude 4.6 출시")
    assert p == "News footage about Claude 4.6 출시"


def test_build_prompt_with_summary():
    p = VideoAnimatorAgent.build_prompt_from_post(
        topic="GPT-5",
        summary="OpenAI announced new reasoning capabilities.",
    )
    assert p.startswith("News footage about GPT-5.")
    assert "OpenAI announced" in p


def test_build_prompt_truncates_long_summary():
    long = "x" * 500
    p = VideoAnimatorAgent.build_prompt_from_post(topic="t", summary=long)
    # Topic prefix (~24) + truncated summary <= ~250 chars
    assert len(p) < 260
    assert p.endswith("…") or p.endswith("x")


def test_build_prompt_handles_blank_inputs():
    assert VideoAnimatorAgent.build_prompt_from_post(topic="") == "News footage about "
    assert VideoAnimatorAgent.build_prompt_from_post(topic="x", summary="   ") == "News footage about x"


# ----------------------------------------------------------------------
# _parse_duration
# ----------------------------------------------------------------------


def test_parse_duration_picks_last_ok_line():
    out = "loading model\nstep 5\nOK 1.667\n"
    assert VideoAnimatorAgent._parse_duration(out) == pytest.approx(1.667)


def test_parse_duration_returns_none_when_missing():
    assert VideoAnimatorAgent._parse_duration("inference failed") is None
    assert VideoAnimatorAgent._parse_duration("") is None
    assert VideoAnimatorAgent._parse_duration(None) is None


def test_parse_duration_handles_garbage_after_ok():
    assert VideoAnimatorAgent._parse_duration("OK notanumber") is None


# ----------------------------------------------------------------------
# _resolve_runner
# ----------------------------------------------------------------------


def test_resolve_runner_points_to_local_video_animate():
    agent = VideoAnimatorAgent()
    runner = agent._resolve_runner()
    assert runner.name == "local_video_animate.py"
    assert runner.exists(), f"runner missing on disk: {runner}"


# ----------------------------------------------------------------------
# run() failure paths (no real LTX call)
# ----------------------------------------------------------------------


def test_run_returns_none_when_image_missing(tmp_path):
    agent = VideoAnimatorAgent()
    result = agent.run(
        image_path=tmp_path / "nope.jpg",
        prompt="x",
        output_path=tmp_path / "out.mp4",
    )
    assert result is None


def test_run_returns_none_when_runner_missing(tmp_path, monkeypatch):
    agent = VideoAnimatorAgent()
    img = tmp_path / "hero.jpg"
    img.write_bytes(b"\xff\xd8fake")

    # Point runner resolution somewhere that doesn't exist.
    monkeypatch.setattr(
        agent, "_resolve_runner", lambda: tmp_path / "missing.py"
    )

    result = agent.run(
        image_path=img,
        prompt="x",
        output_path=tmp_path / "out.mp4",
    )
    assert result is None


def test_run_returns_none_when_subprocess_fails(tmp_path, monkeypatch):
    agent = VideoAnimatorAgent()
    img = tmp_path / "hero.jpg"
    img.write_bytes(b"\xff\xd8fake")
    fake_runner = tmp_path / "runner.py"
    fake_runner.write_text("# fake")
    monkeypatch.setattr(agent, "_resolve_runner", lambda: fake_runner)

    def fake_run(cmd, **kwargs):
        return SimpleNamespace(returncode=7, stdout="boom", stderr="oops")

    monkeypatch.setattr(subprocess, "run", fake_run)
    result = agent.run(
        image_path=img,
        prompt="x",
        output_path=tmp_path / "out.mp4",
    )
    assert result is None


def test_run_returns_none_on_tiny_output(tmp_path, monkeypatch):
    agent = VideoAnimatorAgent()
    img = tmp_path / "hero.jpg"
    img.write_bytes(b"\xff\xd8fake")
    fake_runner = tmp_path / "runner.py"
    fake_runner.write_text("# fake")
    monkeypatch.setattr(agent, "_resolve_runner", lambda: fake_runner)

    out = tmp_path / "out.mp4"

    def fake_run(cmd, **kwargs):
        out.write_bytes(b"x" * 100)  # below 10 KB threshold
        return SimpleNamespace(returncode=0, stdout="OK 1.0", stderr="")

    monkeypatch.setattr(subprocess, "run", fake_run)
    result = agent.run(image_path=img, prompt="x", output_path=out)
    assert result is None


def test_run_returns_duration_on_success(tmp_path, monkeypatch):
    agent = VideoAnimatorAgent()
    img = tmp_path / "hero.jpg"
    img.write_bytes(b"\xff\xd8fake")
    fake_runner = tmp_path / "runner.py"
    fake_runner.write_text("# fake")
    monkeypatch.setattr(agent, "_resolve_runner", lambda: fake_runner)

    out = tmp_path / "out.mp4"

    def fake_run(cmd, **kwargs):
        out.write_bytes(b"x" * 20_000)  # >10 KB
        return SimpleNamespace(returncode=0, stdout="loading\nOK 4.917", stderr="")

    monkeypatch.setattr(subprocess, "run", fake_run)
    result = agent.run(image_path=img, prompt="x", output_path=out)
    assert result == pytest.approx(4.917)


def test_run_returns_none_on_timeout(tmp_path, monkeypatch):
    agent = VideoAnimatorAgent()
    img = tmp_path / "hero.jpg"
    img.write_bytes(b"\xff\xd8fake")
    fake_runner = tmp_path / "runner.py"
    fake_runner.write_text("# fake")
    monkeypatch.setattr(agent, "_resolve_runner", lambda: fake_runner)

    def fake_run(cmd, **kwargs):
        raise subprocess.TimeoutExpired(cmd=cmd, timeout=1)

    monkeypatch.setattr(subprocess, "run", fake_run)
    result = agent.run(
        image_path=img,
        prompt="x",
        output_path=tmp_path / "out.mp4",
        timeout_seconds=1,
    )
    assert result is None
