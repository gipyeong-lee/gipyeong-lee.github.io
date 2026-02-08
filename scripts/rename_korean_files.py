#!/usr/bin/env python3
"""Rename Korean-filename posts to ASCII equivalents.

Handles:
- Renaming post files (.md, .en.md, .ja.md)
- Renaming corresponding image files
- Updating image references in front matter
- Removing duplicates where ASCII-named equivalents already exist
"""

import os
import re
import glob
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(BASE_DIR, '_posts')
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

# Mapping: Korean slug -> ASCII slug
# Some already have ASCII equivalents that exist (marked as duplicates to delete)
RENAMES = {
    'JVM-G1GC-튜닝-방법': {
        'new_slug': 'JVM-G1GC-tuning-methods',
        'has_existing': False,
    },
    'Web3-의-미래': {
        'new_slug': 'future-of-web3-kr',
        'has_existing': True,  # The-future-of-web3 already exists
        'existing_slug': 'The-future-of-web3',
    },
    '생성AI에-대한-이해': {
        'new_slug': 'understanding-generative-ai',
        'has_existing': False,
    },
    '나만의-ChatGPT-만들기': {
        'new_slug': 'building-your-own-chatgpt',
        'has_existing': False,
    },
    'Blockchain의-미래': {
        'new_slug': 'future-of-blockchain-kr',
        'has_existing': False,
    },
    'AI-모델에서-fine-tuning-이란?': {
        'new_slug': 'what-is-ai-fine-tuning',
        'has_existing': True,  # what-is-fine-tuning already exists
        'existing_slug': 'what-is-fine-tuning',
    },
}


def update_image_ref_in_file(filepath, old_image, new_image):
    """Update image reference in a post's front matter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_image in content:
        content = content.replace(old_image, new_image)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    for korean_slug, info in RENAMES.items():
        print(f"\n{'='*60}")
        print(f"Processing: {korean_slug}")

        # Find all post files with this Korean slug
        extensions = ['.md', '.en.md', '.ja.md']
        korean_files = []
        for ext in extensions:
            pattern = os.path.join(POSTS_DIR, f'*-{korean_slug}{ext}')
            korean_files.extend(glob.glob(pattern))

        if not korean_files:
            print(f"  No files found for {korean_slug}")
            continue

        # Get date prefix from the first file found
        basename = os.path.basename(korean_files[0])
        date_prefix = basename[:11]  # e.g., "2023-04-11-"

        if info['has_existing']:
            # ASCII equivalent already exists - just delete Korean-named files
            existing_slug = info['existing_slug']
            print(f"  ASCII equivalent already exists: {existing_slug}")
            print(f"  Deleting Korean-named duplicates...")

            for kf in korean_files:
                print(f"    Deleting: {os.path.basename(kf)}")
                os.remove(kf)

            # Delete Korean-named image too
            korean_img = os.path.join(IMAGES_DIR, f'{date_prefix}{korean_slug}.jpg')
            if os.path.exists(korean_img):
                print(f"    Deleting image: {os.path.basename(korean_img)}")
                os.remove(korean_img)
        else:
            # Rename Korean files to ASCII
            new_slug = info['new_slug']
            old_image_name = f'{date_prefix}{korean_slug}.jpg'
            new_image_name = f'{date_prefix}{new_slug}.jpg'

            for kf in sorted(korean_files):
                old_basename = os.path.basename(kf)
                # Determine extension
                if old_basename.endswith('.en.md'):
                    ext = '.en.md'
                elif old_basename.endswith('.ja.md'):
                    ext = '.ja.md'
                else:
                    ext = '.md'

                new_basename = f'{date_prefix}{new_slug}{ext}'
                new_path = os.path.join(POSTS_DIR, new_basename)

                print(f"  Rename: {old_basename} -> {new_basename}")
                os.rename(kf, new_path)

                # Update image reference in the file
                if update_image_ref_in_file(new_path, old_image_name.replace(date_prefix, ''), new_image_name.replace(date_prefix, '')):
                    print(f"    Updated image ref in {new_basename}")
                # Also try full path match
                update_image_ref_in_file(new_path, korean_slug, new_slug)

            # Rename image
            korean_img = os.path.join(IMAGES_DIR, old_image_name)
            if os.path.exists(korean_img):
                new_img = os.path.join(IMAGES_DIR, new_image_name)
                print(f"  Rename image: {old_image_name} -> {new_image_name}")
                os.rename(korean_img, new_img)
            else:
                print(f"  No image found: {old_image_name}")

    print(f"\n{'='*60}")
    print("Done!")

    # Verify no Korean-named files remain
    remaining = []
    for f in os.listdir(POSTS_DIR):
        # Check if filename contains Korean characters (Hangul range)
        if re.search(r'[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f\ua960-\ua97f\ud7b0-\ud7ff]', f):
            remaining.append(f)

    if remaining:
        print(f"\nWARNING: {len(remaining)} files still have Korean names:")
        for f in remaining:
            print(f"  {f}")
    else:
        print("\nAll Korean filenames successfully converted to ASCII!")


if __name__ == '__main__':
    main()
