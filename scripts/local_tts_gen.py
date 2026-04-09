#!/usr/bin/env python3
"""Local TTS generator — MeloTTS (ko) + optional OpenVoice v2 tone conversion.

Called as a subprocess by scripts/agents/tts_voice.py. Runs under the
interpreter that has torch + melo + openvoice installed (system Python 3.9
on this Mac — see scripts/agents/image_generator._find_python_with_torch).

Usage:
    python3 scripts/local_tts_gen.py \
        --text "안녕하세요, ..." \
        --output path/to/out.wav \
        [--reference path/to/voice_reference.wav] \
        [--speed 1.0]

On success, prints "OK <duration_seconds>" as the last stdout line.
"""
from __future__ import annotations

import argparse
import os
import sys
import tempfile
import traceback
import wave
from pathlib import Path


def _get_device() -> str:
    import torch

    if torch.backends.mps.is_available():
        # OpenVoice has some ops that fall back to CPU on MPS — that's fine,
        # we let torch handle the fallback. MeloTTS is MPS-friendly.
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


def _wav_duration_seconds(path: str) -> float:
    try:
        with wave.open(path, "rb") as w:
            frames = w.getnframes()
            rate = w.getframerate()
            return frames / float(rate) if rate else 0.0
    except Exception:
        try:
            import soundfile as sf

            data, rate = sf.read(path)
            return float(len(data)) / float(rate) if rate else 0.0
        except Exception:
            return 0.0


def _synthesize_base(text: str, output_path: str, speed: float) -> str:
    """Run MeloTTS Korean synthesis into `output_path` (wav). Returns speaker key."""
    from melo.api import TTS  # type: ignore

    device = _get_device()
    print(f"  [TTS] MeloTTS device={device}")
    # MeloTTS downloads the ckpt on first call; HF cache keeps it.
    model = TTS(language="KR", device=device)
    # spk2id is melo's custom HParams object. It does NOT iterate cleanly
    # (its __getitem__ calls getattr and fails on int indices from iter()).
    # Use .keys() or look up "KR" directly.
    spk2id = model.hps.data.spk2id
    try:
        keys = list(spk2id.keys())
    except Exception:
        keys = ["KR"]
    speaker_key = "KR" if "KR" in keys else (keys[0] if keys else "KR")
    speaker_id = spk2id[speaker_key]
    print(f"  [TTS] speaker={speaker_key} id={speaker_id} speed={speed}")
    model.tts_to_file(text, speaker_id, output_path, speed=speed)
    return speaker_key


def _convert_voice(
    base_wav: str,
    reference_wav: str,
    output_wav: str,
    base_speaker_key: str,
) -> bool:
    """Apply OpenVoice v2 ToneColorConverter. Returns True on success."""
    try:
        import torch  # noqa: F401
        from openvoice import se_extractor  # type: ignore
        from openvoice.api import ToneColorConverter  # type: ignore
    except Exception as e:
        print(f"  [TTS] OpenVoice import failed: {e}. Skipping tone conversion.")
        return False

    try:
        from huggingface_hub import snapshot_download  # type: ignore
    except Exception as e:
        print(f"  [TTS] huggingface_hub missing: {e}. Skipping tone conversion.")
        return False

    try:
        ckpt_dir = snapshot_download(repo_id="myshell-ai/OpenVoiceV2")
    except Exception as e:
        print(f"  [TTS] OpenVoiceV2 checkpoint download failed: {e}")
        return False

    converter_dir = os.path.join(ckpt_dir, "converter")
    base_speakers_dir = os.path.join(ckpt_dir, "base_speakers", "ses")

    # Pick the Korean base speaker embedding. OpenVoiceV2 ships files like
    # "kr.pth", "en-us.pth", etc.
    lang_tag = "kr"
    source_se_path = os.path.join(base_speakers_dir, f"{lang_tag}.pth")
    if not os.path.exists(source_se_path):
        print(f"  [TTS] Base speaker embedding not found: {source_se_path}")
        return False

    device = _get_device()
    tcc = ToneColorConverter(
        os.path.join(converter_dir, "config.json"),
        device=device,
    )
    tcc.load_ckpt(os.path.join(converter_dir, "checkpoint.pth"))

    import torch

    source_se = torch.load(source_se_path, map_location=device)

    # Extract target speaker embedding from the reference audio.
    with tempfile.TemporaryDirectory() as tmp:
        target_se, _ = se_extractor.get_se(
            reference_wav, tcc, target_dir=tmp, vad=True
        )

    tcc.convert(
        audio_src_path=base_wav,
        src_se=source_se,
        tgt_se=target_se,
        output_path=output_wav,
        message="@AI뉴스",
    )
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True)
    ap.add_argument("--output", required=True, help="Path to final wav")
    ap.add_argument("--reference", default="", help="Optional reference voice wav")
    ap.add_argument("--speed", type=float, default=1.0)
    args = ap.parse_args()

    output_path = os.path.abspath(args.output)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    # Stage 1: base synthesis (MeloTTS Korean).
    base_path = output_path
    needs_convert = bool(args.reference) and os.path.exists(args.reference)
    if needs_convert:
        base_path = output_path + ".base.wav"

    try:
        speaker_key = _synthesize_base(args.text, base_path, args.speed)
    except Exception as e:
        print(f"  [TTS] MeloTTS synthesis failed: {e}")
        traceback.print_exc()
        return 2

    # Stage 2: tone conversion, only if a reference is provided.
    if needs_convert:
        ok = _convert_voice(base_path, args.reference, output_path, speaker_key)
        if not ok:
            # Fall back: copy base to output so the pipeline can continue
            # with MeloTTS base voice instead of failing the entire video.
            print("  [TTS] Tone conversion unavailable, using base voice.")
            try:
                import shutil

                shutil.copyfile(base_path, output_path)
            except Exception as e:
                print(f"  [TTS] Fallback copy failed: {e}")
                return 3
        try:
            os.remove(base_path)
        except OSError:
            pass

    dur = _wav_duration_seconds(output_path)
    if dur <= 0:
        print("  [TTS] Output wav is empty or unreadable.")
        return 4

    print(f"OK {dur:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
