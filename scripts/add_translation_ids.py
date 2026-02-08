import os
import re
import uuid
import frontmatter

POSTS_DIR = "_posts"
LOG_FILE = "logic.log"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")

def add_translation_ids():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    log("Starting script...")
    
    # Group files by base name (without lang extension)
    groups = {} 
    # Key: base_filename (e.g. "2023-04-20-topic"), Value: list of filenames
    
    files = os.listdir(POSTS_DIR)
    print(f"Found {len(files)} files in {POSTS_DIR}")
    
    for f in files:
        # print(f"Processing: {f}") # Verbose
        if not f.endswith(".md"):
            continue
        if not f.endswith(".md"):
            continue
            
        # Determine base name
        # Pattern: YYYY-MM-DD-title(.lang).md
        # We want YYYY-MM-DD-title
        
        base = f
        if f.endswith(".en.md"):
            base = f[:-6] # strip .en.md
        elif f.endswith(".ja.md"):
            base = f[:-6] # strip .ja.md
        elif f.endswith(".ko.md"):
            base = f[:-6]
        else:
            base = f[:-3] # strip .md
            
        if base not in groups:
            groups[base] = []
        groups[base].append(f)

    # Process each group
    for base, filenames in groups.items():
        if len(filenames) < 1:
            continue
            
        # Check if any file in the group already has a ref
        existing_ref = None
        
        # First pass: look for existing ref
        for fname in filenames:
            path = os.path.join(POSTS_DIR, fname)
            try:
                post = frontmatter.load(path)
                if 'ref' in post.metadata:
                    existing_ref = post.metadata['ref']
                    log(f"[{base}] Found existing ref: {existing_ref}")
                    break
            except Exception as e:
                log(f"Error reading {fname}: {e}")

        # If no ref, generate one
        if not existing_ref:
            existing_ref = base 
            
        # Second pass: apply ref to all
        for fname in filenames:
            path = os.path.join(POSTS_DIR, fname)
            try:
                post = frontmatter.load(path)
                if 'ref' not in post.metadata or post.metadata['ref'] != existing_ref:
                    post.metadata['ref'] = existing_ref
                    
                    with open(path, 'wb') as f_out:
                        frontmatter.dump(post, f_out)
                        
                    log(f"Updated {fname} with ref: {existing_ref}")
            except Exception as e:
                 log(f"Error updating {fname}: {e}")

if __name__ == "__main__":
    add_translation_ids()
