"""Tests for _ensure_wav_reference in scripts/local_tts_gen.py.

We avoid importing `scripts.local_tts_gen` at the module level because
that file also imports melo/openvoice/torch in `_synthesize_base`. We
load just the helper via importlib to keep the test environment pure.

The real ffmpeg-conversion test is skipped when ffmpeg is not on PATH.
"""
from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import time
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
_LTG_PATH = REPO_ROOT / "scripts" / "local_tts_gen.py"


def _load_ltg():
    spec = importlib.util.spec_from_file_location("_ltg_under_test", _LTG_PATH)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _ffmpeg_available() -> bool:
    return shutil.which("ffmpeg") is not None


@pytest.fixture
def ltg():
    return _load_ltg()


# ----------------------------------------------------------------------
# Edge cases that don't need ffmpeg
# ----------------------------------------------------------------------


def test_returns_none_for_missing_file(ltg, tmp_path):
    assert ltg._ensure_wav_reference(str(tmp_path / "nope.mp4")) is None
    assert ltg._ensure_wav_reference("") is None
    assert ltg._ensure_wav_reference(None) is None


def test_wav_source_is_returned_unchanged(ltg, tmp_path):
    # Existing .wav → zero-copy passthrough (no ffmpeg invocation).
    wav = tmp_path / "already_wav.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 100)  # fake wav header
    out = ltg._ensure_wav_reference(str(wav))
    assert out == str(wav)


def test_non_wav_ext_is_recognized(ltg):
    # Spot-check the extension set.
    for ext in (".mp4", ".m4a", ".mp3", ".aac", ".webm", ".mov", ".flac", ".ogg", ".opus"):
        assert ext in ltg._NON_WAV_EXTS, f"{ext} should be in _NON_WAV_EXTS"


# ----------------------------------------------------------------------
# Real ffmpeg conversion — skipped when ffmpeg isn't installed
# ----------------------------------------------------------------------


@pytest.mark.skipif(not _ffmpeg_available(), reason="ffmpeg not on PATH")
def test_mp4_is_converted_and_cached(ltg, tmp_path):
    # Generate a 1-second silent mp4 via ffmpeg lavfi (no external files).
    src = tmp_path / "fake.mp4"
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error",
            "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
            "-t", "1", "-c:a", "aac", str(src),
        ],
        check=True,
    )
    assert src.exists() and src.stat().st_size > 500

    out = ltg._ensure_wav_reference(str(src))
    assert out is not None
    assert out.endswith(".__autowav.wav")
    assert Path(out).exists()
    assert Path(out).stat().st_size > 2000

    # Second call: cache reuse, NO new ffmpeg invocation → mtime unchanged.
    mtime_before = os.path.getmtime(out)
    time.sleep(0.05)
    out2 = ltg._ensure_wav_reference(str(src))
    assert out2 == out
    assert os.path.getmtime(out2) == mtime_before

    # Touch the source newer than the cache → next call must rebuild.
    time.sleep(0.05)
    os.utime(str(src), None)
    out3 = ltg._ensure_wav_reference(str(src))
    assert os.path.getmtime(out3) > mtime_before


@pytest.mark.skipif(not _ffmpeg_available(), reason="ffmpeg not on PATH")
def test_m4a_also_works(ltg, tmp_path):
    src = tmp_path / "fake.m4a"
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error",
            "-f", "lavfi", "-i", "sine=frequency=440:duration=1",
            "-c:a", "aac", str(src),
        ],
        check=True,
    )
    out = ltg._ensure_wav_reference(str(src))
    assert out is not None and Path(out).exists()

    # Confirm the output wav is actually 24kHz mono PCM (what OpenVoice wants).
    probe = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "stream=codec_name,sample_rate,channels",
            "-of", "default=noprint_wrappers=1", out,
        ],
        capture_output=True, text=True, check=True,
    )
    assert "codec_name=pcm_s16le" in probe.stdout
    assert "sample_rate=24000" in probe.stdout
    assert "channels=1" in probe.stdout


def test_bad_ffmpeg_binary_returns_none(ltg, tmp_path, monkeypatch):
    # Simulate ffmpeg missing by shadowing PATH in the subprocess call.
    src = tmp_path / "fake.mp4"
    src.write_bytes(b"\x00" * 1000)
    real_run = subprocess.run

    def fake_run(*args, **kwargs):  # noqa: ANN001
        raise FileNotFoundError("mock: ffmpeg missing")

    monkeypatch.setattr("subprocess.run", fake_run)
    try:
        out = ltg._ensure_wav_reference(str(src))
    finally:
        monkeypatch.setattr("subprocess.run", real_run)
    assert out is None
