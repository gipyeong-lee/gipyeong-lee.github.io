"""Image Generator Agent — designs prompt via Gemini CLI, generates via local SDXL-Turbo."""

import os
import subprocess
import sys
from typing import Optional

from .base import BaseAgent

IMAGES_DIR = "images"


class ImageGeneratorAgent(BaseAgent):
    """Generates blog post hero images.

    Step 1: Gemini CLI designs a photorealistic image prompt (text)
    Step 2: local_image_gen.py generates the image via SDXL-Turbo
    """

    name = "ImageGenerator"
    prompt_file = ""  # No separate prompt file; prompt is inline

    def run(self, topic: str, summary: str, slug: str) -> Optional[str]:
        """Generate a hero image for the blog post.

        Args:
            topic: Post topic
            summary: Research summary for context
            slug: Full slug (YYYY-MM-DD-name) for filename

        Returns:
            Image filename (e.g., "2026-02-08-Openclaw.jpg") or None.
        """
        self.log(f"Designing visual for: {topic}")

        # Step 1: Design image prompt via Gemini CLI
        image_prompt = self._design_prompt(topic, summary)
        if not image_prompt:
            self.log("Prompt design failed. Skipping image generation.")
            return None

        self.log(f"Prompt: {image_prompt[:80]}...")

        # Step 2: Generate image via local SDXL-Turbo
        filename = f"{slug}.jpg"
        filepath = os.path.join(IMAGES_DIR, filename)

        success = self._generate_local(image_prompt, filepath)
        if success:
            self.log(f"Image saved: {filepath}")
            return filename

        self.log("Image generation failed.")
        return None

    def _design_prompt(self, topic: str, summary: str) -> Optional[str]:
        """Use Gemini CLI to design a photorealistic image description."""
        summary_short = summary[:500] if len(summary) > 500 else summary

        prompt = f"""You are a professional photojournalist. Design a creative visual description for a news article header image.

Topic: {topic}
Context: {summary_short}

**VISUAL GUIDELINES (STRICT PHOTOREALISM):**
1. Start with: "Raw photo, Fujifilm GFX 100S, 100MP, hard focus, highly detailed"
2. Style: "National Geographic style", "Cinematic lighting", "Editorial photography"
3. Forbidden: "Illustration", "3D render", "Painting", "Drawing", "Anime", "Blurred"
4. NO text, watermarks, logos, or UI elements in the image
5. NO human faces (use silhouettes, rear views, or focus on objects/environments)
6. Focus on environmental storytelling — symbolic representation of the technology
7. Color palette: deep blues, cool grays, warm accent highlights
8. Widescreen landscape composition (16:9)

Return ONLY a single image description string (no JSON, no explanation, no quotes). Just the prompt text."""

        result = self.gemini.call(prompt)
        if not result:
            return None

        # Clean: remove quotes, code fences, etc.
        result = result.strip().strip('"').strip("'")
        if result.startswith("```"):
            result = result.split("\n", 1)[-1]
        if result.endswith("```"):
            result = result.rsplit("```", 1)[0]

        return result.strip() if result.strip() else None

    def _generate_local(self, prompt: str, output_path: str) -> bool:
        """Call local_image_gen.py to generate the image."""
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        script_path = os.path.join(script_dir, "local_image_gen.py")

        if not os.path.exists(script_path):
            self.log(f"Script not found: {script_path}")
            return False

        # Ensure images directory exists
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

        # Escape prompt for shell
        safe_prompt = prompt.replace('"', '\\"')

        cmd = [
            sys.executable,
            script_path,
            "--prompt", prompt,
            "--output", output_path,
        ]

        self.log("Generating image via SDXL-Turbo (this may take a moment)...")

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout
            )

            if result.stdout:
                for line in result.stdout.strip().split("\n"):
                    self.log(line)

            if result.returncode != 0:
                if result.stderr:
                    self.log(f"Error: {result.stderr[:500]}")
                return False

            # Verify the file was created and is not empty/HTML
            if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
                return True

            self.log("Output file missing or too small.")
            return False

        except subprocess.TimeoutExpired:
            self.log("Image generation timed out (5min).")
            return False
        except Exception as e:
            self.log(f"Failed to run local_image_gen.py: {e}")
            return False
