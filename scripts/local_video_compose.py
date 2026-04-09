#!/usr/bin/env python3
"""Local video composer — moviepy 2.x pipeline.

Called as a subprocess by scripts/agents/video_composer.py. Produces an
1920x1080 @ 30fps H.264 mp4 with:
  - 3s intro (channel name + post title, fade in)
  - Main segment sized to audio duration, hero image with Ken Burns,
    narration audio, burn-in subtitles split evenly across sentences
  - 2s outro (channel name + "구독과 좋아요", fade out)

Usage:
    python3 scripts/local_video_compose.py \
        --image images/slug.jpg --audio data/videos/slug.wav \
        --script "안녕하세요 ..." --title "..." \
        --output data/videos/slug.mp4 [--channel "Antigravity News"]

Prints "OK <duration>" on success.
"""
from __future__ import annotations

import argparse
import math
import os
import re
import sys
import traceback
from typing import List

# --- Rendering constants ---------------------------------------------------

WIDTH = 1920
HEIGHT = 1080
FPS = 30
KEN_BURNS_ZOOM_START = 1.05
KEN_BURNS_ZOOM_END = 1.18

# macOS built-in Korean font ships with the OS — reliable across machines.
KOREAN_FONT_CANDIDATES = [
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    "/Library/Fonts/AppleSDGothicNeo.ttc",
    "/System/Library/Fonts/Supplemental/NotoSansKR-Regular.otf",
    "/System/Library/Fonts/PingFang.ttc",
]


def pick_font() -> str:
    for cand in KOREAN_FONT_CANDIDATES:
        if os.path.exists(cand):
            return cand
    return ""


# --- Subtitle splitting ----------------------------------------------------

_SENTENCE_END_RE = re.compile(r"(?<=[.!?。！？])\s+|(?<=다\.)\s+|\n+")


def split_sentences(text: str) -> List[str]:
    text = re.sub(r"\s+", " ", text).strip()
    parts = _SENTENCE_END_RE.split(text)
    out: List[str] = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        # Further split long chunks on Korean commas so subtitles fit on screen.
        if len(p) > 40:
            chunks = re.split(r",\s*|,\s*", p)
            for c in chunks:
                c = c.strip()
                if c:
                    out.append(c)
        else:
            out.append(p)
    return out


def wrap_two_lines(text: str, per_line: int = 28) -> str:
    """Wrap a subtitle into at most two lines (<= per_line chars each)."""
    text = text.strip()
    if len(text) <= per_line:
        return text
    # Break near the middle on a space or comma.
    mid = len(text) // 2
    for step in range(0, 8):
        for idx in (mid - step, mid + step):
            if 0 < idx < len(text) and text[idx] in " ,":
                return text[:idx].strip() + "\n" + text[idx + 1:].strip()
    return text[:per_line].rstrip() + "\n" + text[per_line:].strip()


# --- MoviePy scene builders ------------------------------------------------


def build_intro(
    duration: float, channel_name: str, title: str, font: str
):
    from moviepy import ColorClip, TextClip, CompositeVideoClip

    bg = ColorClip(size=(WIDTH, HEIGHT), color=(8, 12, 24), duration=duration)

    channel_kwargs = dict(
        text=channel_name,
        font=font or None,
        font_size=84,
        color="white",
        size=(int(WIDTH * 0.9), None),
        method="caption",
    )
    channel = TextClip(**channel_kwargs).with_duration(duration).with_position(
        ("center", HEIGHT // 2 - 120)
    )

    title_kwargs = dict(
        text=title,
        font=font or None,
        font_size=52,
        color=(200, 220, 255),
        size=(int(WIDTH * 0.82), None),
        method="caption",
        text_align="center",
    )
    title_clip = TextClip(**title_kwargs).with_duration(duration).with_position(
        ("center", HEIGHT // 2 + 20)
    )

    return CompositeVideoClip([bg, channel, title_clip], size=(WIDTH, HEIGHT)).with_duration(duration)


def build_outro(duration: float, channel_name: str, font: str):
    from moviepy import ColorClip, TextClip, CompositeVideoClip

    bg = ColorClip(size=(WIDTH, HEIGHT), color=(8, 12, 24), duration=duration)

    channel = TextClip(
        text=channel_name,
        font=font or None,
        font_size=96,
        color="white",
        size=(int(WIDTH * 0.9), None),
        method="caption",
    ).with_duration(duration).with_position(("center", HEIGHT // 2 - 120))

    cta = TextClip(
        text="구독과 좋아요 부탁드립니다",
        font=font or None,
        font_size=56,
        color=(220, 230, 255),
        size=(int(WIDTH * 0.82), None),
        method="caption",
    ).with_duration(duration).with_position(("center", HEIGHT // 2 + 20))

    return CompositeVideoClip([bg, channel, cta], size=(WIDTH, HEIGHT))


def build_multi_hero(image_paths: List[str], audio_duration: float):
    """Build a multi-segment hero track for the 50-min newscast format.

    Slices `audio_duration` into ``len(image_paths)`` equal windows and
    runs a Ken Burns zoom on each hero image during its window. The
    blurred letterbox background is rebuilt per segment so each segment
    feels visually distinct without expensive transitions.

    No LTX animation here — generating per-segment animations would add
    20+ minutes to every render and the visual benefit on a 50-min
    newscast is marginal compared to the existing zoom.
    """
    from moviepy import (
        ImageClip,
        CompositeVideoClip,
        concatenate_videoclips,
    )
    from moviepy.video.fx import FadeIn, FadeOut, Resize
    from PIL import Image, ImageFilter
    import numpy as np

    n = max(1, len(image_paths))
    per = audio_duration / n
    print(f"multi-hero: {n} images @ {per:.1f}s each")

    segments = []
    for idx, img_path in enumerate(image_paths):
        try:
            bg_img = Image.open(img_path).convert("RGB")
        except Exception as e:
            print(f"failed to open hero {img_path}: {e}; skipping")
            continue
        bg_img = bg_img.resize((WIDTH, HEIGHT))
        bg_img = bg_img.filter(ImageFilter.GaussianBlur(radius=40))
        bg_arr = np.array(bg_img)
        bg_clip = ImageClip(bg_arr).with_duration(per)

        fg = ImageClip(img_path).with_duration(per)
        target_w = int(WIDTH * 0.9)
        ratio = target_w / fg.w
        target_h = int(fg.h * ratio)
        fg = fg.with_effects([Resize(new_size=(target_w, target_h))])

        # Per-segment Ken Burns: alternate zoom-in / zoom-out so adjacent
        # segments don't all push the same direction.
        zoom_in = (idx % 2 == 0)
        z_start = KEN_BURNS_ZOOM_START if zoom_in else KEN_BURNS_ZOOM_END
        z_end = KEN_BURNS_ZOOM_END if zoom_in else KEN_BURNS_ZOOM_START

        def make_zoom(z0, z1, dur):
            def _z(t):
                if dur <= 0:
                    return 1.0
                progress = min(max(t / dur, 0.0), 1.0)
                return z0 + (z1 - z0) * progress
            return _z

        fg = fg.with_effects(
            [Resize(new_size=make_zoom(z_start, z_end, per))]
        ).with_position("center")

        seg = CompositeVideoClip(
            [bg_clip, fg], size=(WIDTH, HEIGHT)
        ).with_duration(per)
        # Cross-fade between segments — 0.4s fade keeps transitions
        # smooth without burning subtitle space.
        seg = seg.with_effects([FadeIn(0.4), FadeOut(0.4)])
        segments.append(seg)

    if not segments:
        # Pathological: no images openable. Caller should have prevented
        # this; return a single black clip so the pipeline doesn't crash.
        from moviepy import ColorClip
        return ColorClip(size=(WIDTH, HEIGHT), color=(0, 0, 0), duration=audio_duration)

    return concatenate_videoclips(segments, method="compose").with_duration(audio_duration)


def build_hero(
    image_path: str, audio_duration: float, animation_path: str | None = None
):
    """Build the main segment: blurred letterbox + centered hero.

    Two modes:

    - **Animation mode** (`animation_path` provided): The animation clip
      is the foreground. We *ping-pong loop* it (forward → reverse →
      forward …) until the audio duration is filled. The static blurred
      background is still rendered from the original hero image.

    - **Static mode** (no animation): legacy Ken Burns zoom on the
      static hero image. Identical to the original behavior — used as
      automatic fallback when LTX-Video is disabled or generation fails.
    """
    from moviepy import ImageClip, ColorClip, CompositeVideoClip, concatenate_videoclips
    from moviepy.video.fx import Resize
    from PIL import Image, ImageFilter
    import numpy as np

    # Blurred background — same in both modes (animation clip is too low-res
    # to also use as the background letterbox).
    bg_img = Image.open(image_path).convert("RGB")
    bg_img = bg_img.resize((WIDTH, HEIGHT))
    bg_img = bg_img.filter(ImageFilter.GaussianBlur(radius=40))
    bg_arr = np.array(bg_img)
    bg_clip = ImageClip(bg_arr).with_duration(audio_duration)

    if animation_path and os.path.exists(animation_path):
        fg = _build_animation_foreground(animation_path, audio_duration)
        if fg is not None:
            print(f"foreground: animation clip ({animation_path})")
            return CompositeVideoClip(
                [bg_clip, fg], size=(WIDTH, HEIGHT)
            ).with_duration(audio_duration)
        # If the animation clip can't be opened, fall through to Ken Burns.
        print("animation clip unusable; falling back to Ken Burns")

    # --- Static fallback: Ken Burns zoom on the hero image -------------
    fg = ImageClip(image_path).with_duration(audio_duration)
    target_w = int(WIDTH * 0.9)
    ratio = target_w / fg.w
    target_h = int(fg.h * ratio)
    fg = fg.with_effects([Resize(new_size=(target_w, target_h))])

    def zoom_factor(t: float) -> float:
        if audio_duration <= 0:
            return 1.0
        progress = min(max(t / audio_duration, 0.0), 1.0)
        return KEN_BURNS_ZOOM_START + (KEN_BURNS_ZOOM_END - KEN_BURNS_ZOOM_START) * progress

    fg = fg.with_effects([Resize(new_size=zoom_factor)]).with_position("center")
    return CompositeVideoClip(
        [bg_clip, fg], size=(WIDTH, HEIGHT)
    ).with_duration(audio_duration)


def _build_animation_foreground(animation_path: str, audio_duration: float):
    """Load the LTX clip, ping-pong loop it to fill `audio_duration`, fit canvas."""
    try:
        from moviepy import VideoFileClip, concatenate_videoclips
        from moviepy.video.fx import Resize
    except Exception as e:
        print(f"moviepy import failed for animation: {e}")
        return None

    try:
        clip = VideoFileClip(animation_path).without_audio()
    except Exception as e:
        print(f"failed to open animation clip: {e}")
        return None

    if clip.duration <= 0 or audio_duration <= 0:
        return None

    # Resize to fit 90% width while preserving aspect ratio.
    target_w = int(WIDTH * 0.9)
    ratio = target_w / clip.w
    target_h = int(clip.h * ratio)
    clip = clip.with_effects([Resize(new_size=(target_w, target_h))])

    # Ping-pong loop: [forward, reverse] tile, then trim to audio_duration.
    try:
        from moviepy.video.fx import TimeMirror

        reverse = clip.with_effects([TimeMirror()])
    except Exception:
        # Older moviepy: skip the reverse leg, just loop forward.
        reverse = None

    base_unit = (
        concatenate_videoclips([clip, reverse], method="compose")
        if reverse is not None
        else clip
    )
    unit_dur = base_unit.duration
    if unit_dur <= 0:
        return None

    import math
    repeats = max(1, int(math.ceil(audio_duration / unit_dur)))
    looped = concatenate_videoclips([base_unit] * repeats, method="compose")
    looped = looped.subclipped(0, audio_duration)
    return looped.with_position("center")


def build_subtitles(sentences, audio_duration: float, font: str):
    """Create a list of TextClips with sentence-level timing."""
    from moviepy import TextClip

    if not sentences:
        return []

    per = audio_duration / len(sentences)
    clips = []
    for i, sentence in enumerate(sentences):
        wrapped = wrap_two_lines(sentence)
        start = i * per
        dur = per

        txt = TextClip(
            text=wrapped,
            font=font or None,
            font_size=48,
            color="white",
            stroke_color="black",
            stroke_width=4,
            size=(int(WIDTH * 0.85), None),
            method="caption",
            text_align="center",
        ).with_start(start).with_duration(dur).with_position(
            ("center", HEIGHT - 220)
        )
        clips.append(txt)
    return clips


# --- Main ------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", required=True, help="Primary hero image (single-topic mode)")
    ap.add_argument(
        "--images",
        default="",
        help=(
            "Comma-separated list of hero image paths for newscast (multi-"
            "topic) mode. When provided, the composer slices the audio "
            "into N equal Ken-Burns segments, one per image."
        ),
    )
    ap.add_argument("--audio", required=True)
    ap.add_argument("--script", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--channel", default="Antigravity News")
    ap.add_argument("--intro", type=float, default=3.0)
    ap.add_argument("--outro", type=float, default=2.0)
    ap.add_argument(
        "--animation",
        default="",
        help="Optional path to a pre-rendered LTX-Video clip to use as the foreground.",
    )
    args = ap.parse_args()

    try:
        from moviepy import AudioFileClip, CompositeVideoClip, concatenate_videoclips
        from moviepy.video.fx import FadeIn, FadeOut
    except Exception as e:
        print(f"moviepy import failed: {e}", file=sys.stderr)
        return 2

    font = pick_font()
    print(f"font: {font or '(default)'}")

    audio = AudioFileClip(args.audio)
    audio_duration = float(audio.duration)
    print(f"audio duration: {audio_duration:.2f}s")

    try:
        intro = build_intro(args.intro, args.channel, args.title, font)
        intro = intro.with_effects([FadeIn(0.5), FadeOut(0.4)])

        # Newscast (multi-hero) mode bypasses single-hero logic entirely.
        multi_paths = [
            p.strip() for p in (args.images or "").split(",") if p.strip()
        ]
        if len(multi_paths) > 1:
            print(f"newscast mode: {len(multi_paths)} hero images")
            hero = build_multi_hero(multi_paths, audio_duration)
        else:
            animation_path = args.animation.strip() or None
            hero = build_hero(args.image, audio_duration, animation_path=animation_path)
        subtitles = build_subtitles(split_sentences(args.script), audio_duration, font)
        main_comp = CompositeVideoClip([hero, *subtitles], size=(WIDTH, HEIGHT))
        main_comp = main_comp.with_audio(audio)

        outro = build_outro(args.outro, args.channel, font)
        outro = outro.with_effects([FadeIn(0.4), FadeOut(0.6)])

        final = concatenate_videoclips([intro, main_comp, outro], method="compose")
    except Exception as e:
        print(f"compose error: {e}", file=sys.stderr)
        traceback.print_exc()
        return 3

    try:
        final.write_videofile(
            args.output,
            codec="libx264",
            audio_codec="aac",
            fps=FPS,
            preset="medium",
            threads=4,
            bitrate="4000k",
            temp_audiofile=args.output + ".temp.m4a",
            remove_temp=True,
            logger=None,
        )
    except Exception as e:
        print(f"write_videofile failed: {e}", file=sys.stderr)
        traceback.print_exc()
        return 4
    finally:
        try:
            final.close()
            audio.close()
        except Exception:
            pass

    total_duration = args.intro + audio_duration + args.outro
    print(f"OK {total_duration:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
