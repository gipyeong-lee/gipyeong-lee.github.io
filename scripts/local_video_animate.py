#!/usr/bin/env python3
"""LTX-Video image-to-video runner (Apache 2.0, Apple Silicon MPS).

Called as a subprocess by `scripts/agents/video_animator.py`. Loads the
`Lightricks/LTX-Video` pipeline via diffusers, takes a hero image +
descriptive prompt, and renders a short animated mp4 clip that the
compositor can loop into the full narration timeline.

Design notes
------------
- Runs under the torch-capable interpreter discovered by
  `image_generator._find_python_with_torch()` (system Python 3.9 on
  this Mac) — same pattern as local_image_gen.py / local_tts_gen.py.
- Uses MPS float16 when available. LTX autoencoder and transformer
  both fit comfortably in 96 GB unified memory on M3 Max.
- Target resolution is LTX's native 16:9 canvas (1216×704). Moviepy
  upscales the result to 1920×1080 later.
- Duration defaults to 5 seconds @ 24 fps → 121 frames (LTX requires
  `num_frames - 1` to be divisible by 8).
- On any failure returns a non-zero exit code without a partial mp4 so
  the agent can cleanly fall back to the legacy Ken-Burns zoom.

Usage:
    python3 scripts/local_video_animate.py \
        --image images/<slug>.jpg \
        --prompt "cinematic newsroom footage, AI technology..." \
        --output data/videos/<slug>.anim.mp4 \
        [--duration 5.0] [--width 1216] [--height 704] [--fps 24]

Success prints `OK <duration_seconds>` as the last stdout line.
"""
from __future__ import annotations

import argparse
import os
import sys
import traceback

# LTX native 16:9 canvas. Must be divisible by 32 on both axes.
DEFAULT_WIDTH = 1216
DEFAULT_HEIGHT = 704
DEFAULT_FPS = 24
# LTX requires (num_frames - 1) % 8 == 0 — i.e. frame count 9, 17, 25, …
DEFAULT_DURATION_SECONDS = 5.0
# 20 steps is the diffusers reference; can be tuned down for speed.
DEFAULT_INFERENCE_STEPS = 20
# HF model ID — pinned to the base LTX-Video repo. Updating to a newer
# point release means editing this constant (intentional: we don't want
# the pipeline silently picking up a new model mid-run).
LTX_MODEL_ID = "Lightricks/LTX-Video"


def _get_device_and_dtype() -> tuple[str, "object"]:
    import torch

    if torch.backends.mps.is_available():
        # M-series GPUs run LTX transformer + VAE in fp16 comfortably at
        # 1216x704. bf16 would also work but fp16 is better tested on MPS.
        return "mps", torch.float16
    if torch.cuda.is_available():
        return "cuda", torch.float16
    return "cpu", torch.float32


def _round_to_multiple(value: int, base: int) -> int:
    return max(base, (value // base) * base)


def _valid_frame_count(total: int) -> int:
    """LTX wants `num_frames - 1` divisible by 8. Round down to nearest."""
    if total < 9:
        return 9
    return ((total - 1) // 8) * 8 + 1


def _default_prompt(user_prompt: str) -> str:
    """Augment user prompt with LTX-friendly style cues.

    LTX-Video responds best to descriptive, cinematic-camera language.
    We append a subtle-motion clause so news content doesn't get
    hallucinated faces or chaotic scene changes.
    """
    base = (user_prompt or "").strip()
    cinematic_tail = (
        " cinematic news footage, subtle camera pan, soft focus, "
        "natural motion, professional lighting, high detail, "
        "documentary photography, no text, no watermark"
    )
    if not base:
        return cinematic_tail.strip()
    return (base + cinematic_tail).strip()


def generate(
    image_path: str,
    prompt: str,
    output_path: str,
    *,
    duration_seconds: float = DEFAULT_DURATION_SECONDS,
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    fps: int = DEFAULT_FPS,
    inference_steps: int = DEFAULT_INFERENCE_STEPS,
) -> int:
    if not os.path.exists(image_path):
        print(f"  [Animate] image not found: {image_path}", file=sys.stderr)
        return 2

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    try:
        import torch
        from diffusers import LTXImageToVideoPipeline
        from diffusers.utils import export_to_video, load_image
    except Exception as e:
        print(f"  [Animate] failed to import diffusers/torch: {e}", file=sys.stderr)
        traceback.print_exc()
        return 3

    device, dtype = _get_device_and_dtype()
    print(f"  [Animate] device={device} dtype={dtype}")

    # Resolution + frame-count sanity.
    width = _round_to_multiple(int(width), 32)
    height = _round_to_multiple(int(height), 32)
    num_frames = _valid_frame_count(int(fps * duration_seconds))
    actual_seconds = (num_frames - 1) / float(fps)
    print(
        f"  [Animate] {width}×{height} @ {fps}fps · {num_frames} frames "
        f"(~{actual_seconds:.2f}s) · steps={inference_steps}"
    )

    print(f"  [Animate] loading {LTX_MODEL_ID} (first run downloads weights)…")
    try:
        pipe = LTXImageToVideoPipeline.from_pretrained(
            LTX_MODEL_ID,
            torch_dtype=dtype,
        )
    except Exception as e:
        print(f"  [Animate] pipeline load failed: {e}", file=sys.stderr)
        traceback.print_exc()
        return 4

    try:
        pipe.to(device)
    except Exception as e:
        print(f"  [Animate] .to({device}) failed: {e}", file=sys.stderr)
        traceback.print_exc()
        return 5

    # Memory-efficient modes — safe no-ops if the backend doesn't support them.
    for fn in ("enable_attention_slicing", "enable_vae_slicing"):
        try:
            getattr(pipe, fn)()
        except Exception:
            pass

    try:
        image = load_image(image_path).convert("RGB")
    except Exception as e:
        print(f"  [Animate] failed to load image: {e}", file=sys.stderr)
        return 6

    full_prompt = _default_prompt(prompt)
    negative = (
        "worst quality, low quality, blurry, distorted, deformed, "
        "text, watermark, logo, artifacts, chaotic motion, flicker"
    )

    print(f"  [Animate] prompt: {full_prompt[:120]}")
    try:
        result = pipe(
            image=image,
            prompt=full_prompt,
            negative_prompt=negative,
            width=width,
            height=height,
            num_frames=num_frames,
            num_inference_steps=inference_steps,
            guidance_scale=3.0,
            generator=torch.Generator().manual_seed(42),
        )
    except Exception as e:
        print(f"  [Animate] inference failed: {e}", file=sys.stderr)
        traceback.print_exc()
        return 7

    try:
        frames = result.frames[0]
    except Exception:
        print("  [Animate] result has no frames", file=sys.stderr)
        return 8

    try:
        export_to_video(frames, output_path, fps=fps)
    except Exception as e:
        print(f"  [Animate] export_to_video failed: {e}", file=sys.stderr)
        traceback.print_exc()
        return 9

    if not os.path.exists(output_path) or os.path.getsize(output_path) < 10_000:
        print("  [Animate] output missing or too small", file=sys.stderr)
        try:
            if os.path.exists(output_path):
                os.remove(output_path)
        except OSError:
            pass
        return 10

    print(f"OK {actual_seconds:.3f}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--duration", type=float, default=DEFAULT_DURATION_SECONDS)
    ap.add_argument("--width", type=int, default=DEFAULT_WIDTH)
    ap.add_argument("--height", type=int, default=DEFAULT_HEIGHT)
    ap.add_argument("--fps", type=int, default=DEFAULT_FPS)
    ap.add_argument("--steps", type=int, default=DEFAULT_INFERENCE_STEPS)
    args = ap.parse_args()

    return generate(
        args.image,
        args.prompt,
        args.output,
        duration_seconds=args.duration,
        width=args.width,
        height=args.height,
        fps=args.fps,
        inference_steps=args.steps,
    )


if __name__ == "__main__":
    sys.exit(main())
