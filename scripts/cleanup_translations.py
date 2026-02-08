#!/usr/bin/env python3
"""Clean up broken AI-generated translation files.

Fixes:
- AI preamble text before front matter ("Here is the translated...", etc.)
- ```markdown / ``` wrappers around content
- Any text before the first --- front matter delimiter
"""

import os
import re
import glob

POSTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_posts')


def cleanup_file(filepath):
    """Clean up a single translation file. Returns True if modified."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # If file already starts with ---, check for ```markdown wrapper inside
    # Otherwise, find the first --- and strip everything before it

    # Step 1: Find the first valid front matter block
    # The front matter starts with --- on its own line
    lines = content.split('\n')

    # Find the first line that is exactly '---'
    front_matter_start = None
    for i, line in enumerate(lines):
        if line.strip() == '---':
            front_matter_start = i
            break

    if front_matter_start is None:
        print(f"  WARNING: No front matter found in {os.path.basename(filepath)}")
        return False

    # If there's content before the front matter start, it's preamble - remove it
    if front_matter_start > 0:
        preamble = '\n'.join(lines[:front_matter_start])
        print(f"  Removing preamble ({front_matter_start} lines): {preamble[:80]}...")
        lines = lines[front_matter_start:]

    # Rejoin
    content = '\n'.join(lines)

    # Step 2: Remove ```markdown wrapper if present
    # Pattern: starts with ---, then front matter, then ---, then possibly ```markdown content ```
    # Or: ```markdown wraps the entire content including front matter

    # Remove leading ```markdown that might appear right after front matter opening
    # Actually the pattern is: preamble text, then ```markdown, then ---, then content, then ```
    # After step 1 we've removed preamble, so now we should start with ---

    # Check if there's a trailing ``` at the end of the file
    content_stripped = content.rstrip()
    if content_stripped.endswith('```'):
        # Check if there was a ```markdown before the front matter (which we already removed)
        # Or check if there's a ```markdown line somewhere
        content = content_stripped[:-3].rstrip() + '\n'
        print(f"  Removed trailing ``` wrapper")

    # Also handle case where ```markdown appears right after front matter
    # Find end of front matter
    fm_lines = content.split('\n')
    fm_end = None
    found_start = False
    for i, line in enumerate(fm_lines):
        if line.strip() == '---':
            if not found_start:
                found_start = True
            else:
                fm_end = i
                break

    if fm_end is not None:
        # Check if line after front matter is ```markdown
        if fm_end + 1 < len(fm_lines) and fm_lines[fm_end + 1].strip() in ('```markdown', '```'):
            fm_lines.pop(fm_end + 1)
            content = '\n'.join(fm_lines)
            print(f"  Removed ```markdown after front matter")

    # Step 3: Ensure file ends with single newline
    content = content.rstrip() + '\n'

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    # Process all .en.md and .ja.md files
    patterns = [
        os.path.join(POSTS_DIR, '*.en.md'),
        os.path.join(POSTS_DIR, '*.ja.md'),
    ]

    total_fixed = 0
    total_checked = 0

    for pattern in patterns:
        files = sorted(glob.glob(pattern))
        for filepath in files:
            total_checked += 1
            basename = os.path.basename(filepath)
            print(f"Checking {basename}...")
            if cleanup_file(filepath):
                total_fixed += 1
                print(f"  FIXED: {basename}")

    print(f"\nDone. Checked {total_checked} files, fixed {total_fixed}.")


if __name__ == '__main__':
    main()
