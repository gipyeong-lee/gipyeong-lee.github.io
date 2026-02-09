#!/usr/bin/env python3
"""Local image generation using SDXL-Turbo via HuggingFace diffusers.

Usage:
    python3 scripts/local_image_gen.py --prompt "description..." --output "images/output.jpg"
"""

import argparse
import os
import sys


def get_device_and_dtype():
    """Detect best available device."""
    import torch

    if torch.backends.mps.is_available():
        return "mps", torch.float32  # float32 required for MPS
    elif torch.cuda.is_available():
        return "cuda", torch.float16
    else:
        return "cpu", torch.float32


def generate_image(prompt, output_path, width=1600, height=900):
    """Generate an image from a text prompt using SDXL-Turbo.

    Generates at native SDXL resolution (1024x576) then upscales to target size
    for better quality and memory efficiency.
    """
    import torch
    from diffusers import AutoPipelineForText2Image
    from PIL import Image

    model_id = "stabilityai/sdxl-turbo"
    device, dtype = get_device_and_dtype()
    print(f"  [ImageGen] Device: {device}, dtype: {dtype}")
    print(f"  [ImageGen] Loading {model_id}...")

    pipe = AutoPipelineForText2Image.from_pretrained(
        model_id,
        torch_dtype=dtype,
        use_safetensors=True,
    )
    pipe.enable_attention_slicing()
    pipe.to(device)

    # Add photorealistic style modifiers
    style_suffix = (
        ", raw photo, hyperrealistic, Fujifilm GFX 100S, hard focus, "
        "film grain, associated press, masterpiece, 8k uhd"
    )
    negative_prompt = (
        "blurry, low quality, distorted, deformed, ugly, bad anatomy, "
        "text, watermark, logo, split screen, illustration, 3d render, "
        "painting, drawing, anime"
    )

    full_prompt = prompt + style_suffix

    # Generate at native SDXL resolution (16:9)
    gen_width, gen_height = 1024, 576
    print(f"  [ImageGen] Generating {gen_width}x{gen_height} -> upscale to {width}x{height}...")

    image = pipe(
        prompt=full_prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=4,
        guidance_scale=0.0,
        height=gen_height,
        width=gen_width,
    ).images[0]

    # Upscale to target resolution
    if (width, height) != (gen_width, gen_height):
        image = image.resize((width, height), Image.LANCZOS)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    # Save as JPEG with quality optimization
    if output_path.lower().endswith(".jpg") or output_path.lower().endswith(".jpeg"):
        image.save(output_path, "JPEG", quality=85, optimize=True)
    else:
        image.save(output_path)

    print(f"  [ImageGen] Saved: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate news image using SDXL-Turbo")
    parser.add_argument("--prompt", type=str, required=True, help="Image description prompt")
    parser.add_argument("--output", type=str, required=True, help="Output file path")
    parser.add_argument("--width", type=int, default=1600, help="Image width")
    parser.add_argument("--height", type=int, default=900, help="Image height")

    args = parser.parse_args()
    generate_image(args.prompt, args.output, args.width, args.height)
