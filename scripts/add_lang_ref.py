#!/usr/bin/env python3
"""Add lang and ref fields to all post front matter.

- .md -> lang: ko
- .en.md -> lang: en
- .ja.md -> lang: ja
- ref: <date-slug> (same for all language versions of a post)
"""

import os
import re
import glob

POSTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_posts')


def get_lang_and_ref(filepath):
    """Determine lang and ref from filename."""
    basename = os.path.basename(filepath)

    if basename.endswith('.en.md'):
        lang = 'en'
        # Remove .en.md to get slug
        slug_part = basename[:-6]  # remove '.en.md'
    elif basename.endswith('.ja.md'):
        lang = 'ja'
        slug_part = basename[:-6]  # remove '.ja.md'
    elif basename.endswith('.md'):
        lang = 'ko'
        slug_part = basename[:-3]  # remove '.md'
    else:
        return None, None

    # ref is the date-slug (e.g., "2023-04-11-JVM-G1GC-tuning-methods")
    ref = slug_part

    return lang, ref


def add_fields_to_file(filepath, lang, ref):
    """Add lang and ref to front matter. Returns True if modified."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        print(f"  WARNING: {os.path.basename(filepath)} doesn't start with ---")
        return False

    # Find the closing --- of front matter
    second_dash = content.index('---', 3)
    front_matter = content[3:second_dash]
    body = content[second_dash:]

    modified = False

    # Check if lang already exists
    if re.search(r'^lang:', front_matter, re.MULTILINE):
        # Update existing lang
        front_matter = re.sub(r'^lang:.*$', f'lang: {lang}', front_matter, flags=re.MULTILINE)
    else:
        # Add lang before closing ---
        front_matter = front_matter.rstrip('\n') + f'\nlang: {lang}\n'
        modified = True

    # Check if ref already exists
    if re.search(r'^ref:', front_matter, re.MULTILINE):
        # Keep existing ref (it may have been manually set)
        pass
    else:
        front_matter = front_matter.rstrip('\n') + f'\nref: {ref}\n'
        modified = True

    new_content = '---' + front_matter + body

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


def main():
    # Get all post files
    all_files = sorted(glob.glob(os.path.join(POSTS_DIR, '*.md')))

    total = 0
    modified = 0

    for filepath in all_files:
        lang, ref = get_lang_and_ref(filepath)
        if lang is None:
            continue

        total += 1
        basename = os.path.basename(filepath)

        if add_fields_to_file(filepath, lang, ref):
            modified += 1
            print(f"  Updated: {basename} (lang={lang}, ref={ref})")

    print(f"\nDone. Processed {total} files, modified {modified}.")

    # Verify: check that ref groups match
    refs = {}
    for filepath in sorted(glob.glob(os.path.join(POSTS_DIR, '*.md'))):
        lang, ref = get_lang_and_ref(filepath)
        if lang is None:
            continue
        if ref not in refs:
            refs[ref] = []
        refs[ref].append(lang)

    print(f"\nRef groups: {len(refs)} unique refs")
    multi_lang = sum(1 for langs in refs.values() if len(langs) > 1)
    print(f"Multi-language posts: {multi_lang}")

    # Show any groups with unexpected language counts
    for ref, langs in sorted(refs.items()):
        if len(langs) == 2:
            print(f"  2 langs ({', '.join(langs)}): {ref}")


if __name__ == '__main__':
    main()
