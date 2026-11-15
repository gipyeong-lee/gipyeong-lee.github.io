"""Pages image budget contract.

On 2026-11-15 the Pages artifact was 997 MB of the 1 GiB that
actions/deploy-pages accepts and grew ~0.38 MB a post; three quarters of it
were hero images, a 1600x900 jpg plus a webp sibling per post. The build now
replaces them with one 1200 px progressive jpg per hero
(scripts/shrink_site_images.py), which took the artifact to about half the
limit and the growth to ~0.19 MB a post. If an assertion here breaks, that
budget is void.

The functional tests need Pillow (the workflow installs it); run them with
`python3 -m unittest scripts.tests.test_image_budget_contract` from an
environment that has it.
"""
from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts import shrink_site_images as shrink

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = (ROOT / ".github/workflows/jekyll.yml").read_text(encoding="utf-8")
TEMPLATES = sorted((ROOT / "_layouts").glob("*.html")) + sorted((ROOT / "_includes").glob("*.html"))
HAS_PILLOW = importlib.util.find_spec("PIL") is not None


def _build_steps() -> list[str]:
    job = re.search(r"^  build:\n(.*?)(?=^  \S|\Z)", WORKFLOW, re.M | re.S)
    if job is None:
        raise AssertionError("build job not found in jekyll.yml")
    return re.findall(r"^      - name: .*?(?=^      - |\Z)", job.group(1), re.M | re.S)


def _jpeg(path: Path, size: tuple[int, int], exif: bytes | None = None) -> None:
    from PIL import Image

    width, height = size
    # A gradient with a little structure: compressible like a photo, and a
    # re-encode at a lower quality is reliably smaller.
    image = Image.linear_gradient("L").resize(size).convert("RGB")
    image.paste((200, 40, 40), (width // 4, height // 4, width // 2, height // 2))
    options = {"quality": 95}
    if exif:
        options["exif"] = exif
    image.save(path, "JPEG", **options)


class ImageBudgetContractTest(unittest.TestCase):
    def test_templates_reference_no_webp(self):
        """The deployed site has no hero webp. A <source type="image/webp">
        whose file is missing renders a broken hero in Chrome, with no
        fallback to the <img> jpg (every post 2026-06-07..07-20)."""
        for template in TEMPLATES:
            with self.subTest(template=template.name):
                self.assertNotIn(".webp", template.read_text(encoding="utf-8"))

    def test_workflow_shrinks_images_between_build_and_upload(self):
        """The shrink must see the built _site and finish before the
        artifact is packed."""
        steps = _build_steps()

        def index(pattern: str) -> int:
            hits = [i for i, step in enumerate(steps) if re.search(pattern, step)]
            self.assertEqual(len(hits), 1, f"expected one build step matching {pattern!r}")
            return hits[0]

        build = index(r"jekyll build")
        shrink_step = index(r"python3 scripts/shrink_site_images\.py _site\b")
        upload = index(r"uses: actions/upload-pages-artifact@")
        self.assertLess(build, shrink_step)
        self.assertLess(shrink_step, upload)
        self.assertRegex(steps[shrink_step], r"pip install pillow==\d")

    def test_hero_stays_at_least_1200_px_wide(self):
        """og:image, twitter:image and the Article schema point at this jpg,
        and Google Discover only shows large previews for images at least
        1200 px wide; 1200 px is also the width the quality was measured at
        (ssimulacra2 74.7 vs 75.4 for the webp it replaced)."""
        self.assertGreaterEqual(shrink.MAX_WIDTH, 1200)

    @unittest.skipUnless(HAS_PILLOW, "Pillow not installed")
    def test_shrinks_top_level_heroes_and_drops_their_webp(self):
        from PIL import Image

        with TemporaryDirectory() as tmp:
            images = Path(tmp) / "images"
            (images / "blog" / "post").mkdir(parents=True)
            _jpeg(images / "hero.jpg", (1600, 900))
            (images / "hero.webp").write_bytes(b"webp")
            _jpeg(images / "small.jpg", (800, 450))
            small_before = (images / "small.jpg").read_bytes()
            (images / "lonely.webp").write_bytes(b"webp")  # no jpg sibling
            _jpeg(images / "blog" / "post" / "inline.jpg", (1600, 900))
            nested_before = (images / "blog" / "post" / "inline.jpg").read_bytes()
            (images / "blog" / "post" / "inline.webp").write_bytes(b"webp")

            self.assertEqual(shrink.main(["shrink", tmp]), 0)

            with Image.open(images / "hero.jpg") as hero:
                self.assertEqual(hero.size, (1200, 675))
                self.assertTrue(hero.info.get("progressive") or hero.info.get("progression"))
            self.assertFalse((images / "hero.webp").exists())
            self.assertEqual((images / "small.jpg").read_bytes(), small_before)
            self.assertTrue((images / "lonely.webp").exists())
            self.assertEqual((images / "blog" / "post" / "inline.jpg").read_bytes(), nested_before)
            self.assertTrue((images / "blog" / "post" / "inline.webp").exists())

    @unittest.skipUnless(HAS_PILLOW, "Pillow not installed")
    def test_exif_orientation_is_baked_in(self):
        """The output carries no EXIF, so a rotated photo must be turned
        upright before resizing or it would deploy sideways."""
        from PIL import Image

        exif = Image.Exif()
        exif[0x0112] = 6  # rotate 90 degrees clockwise when displayed
        with TemporaryDirectory() as tmp:
            images = Path(tmp) / "images"
            images.mkdir()
            _jpeg(images / "photo.jpg", (3000, 1600), exif.tobytes())

            self.assertEqual(shrink.main(["shrink", tmp]), 0)

            with Image.open(images / "photo.jpg") as photo:
                self.assertEqual(photo.size, (1200, 2250))
                self.assertNotEqual(photo.getexif().get(0x0112), 6)

    @unittest.skipUnless(HAS_PILLOW, "Pillow not installed")
    def test_unreadable_heroes_fail_the_step_instead_of_deploying_full_size(self):
        with TemporaryDirectory() as tmp:
            images = Path(tmp) / "images"
            images.mkdir()
            (images / "broken.jpg").write_bytes(b"not a jpeg")

            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/shrink_site_images.py"), tmp],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("::warning file=", result.stdout)
            self.assertEqual((images / "broken.jpg").read_bytes(), b"not a jpeg")


if __name__ == "__main__":
    unittest.main()
