import os
import re
import unicodedata

POSTS_DIR = "_posts"
LOG_FILE = "permalink_debug.log"

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)

def unify_permalinks():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    
    log(f"Starting unification in {os.getcwd()}")
    
    if not os.path.exists(POSTS_DIR):
        log(f"Error: {POSTS_DIR} does not exist.")
        return

    # Regex to handle YYYY-MM-DD-slug(.lang)?.md
    pattern = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+?)(\.(en|ja|ko))?\.md$")
    
    groups = {}
    files = os.listdir(POSTS_DIR)
    log(f"Found {len(files)} files in {POSTS_DIR}")

    for filename in files:
        # Normalize filename to NFC for regex matching
        filename_nfc = unicodedata.normalize('NFC', filename)
        
        match = pattern.match(filename_nfc)
        if match:
            date_part = match.group(1)
            raw_slug = match.group(2)
            
            key = f"{date_part}-{raw_slug}"
            if key not in groups:
                 groups[key] = []
            
            # Store original filename (NFD potentially) for file operations
            groups[key].append(filename)
        else:
            log(f"Skipping non-matching: {filename_nfc}")

    log(f"Grouped into {len(groups)} distinct posts.")

    for key, filenames in groups.items():
        parts = key.split('-', 3)
        if len(parts) < 4:
            continue
        year, month, day, slug = parts[0], parts[1], parts[2], parts[3]
        
        target_permalink = f"/{year}/{month}/{day}/{slug}/"
        
        for filename in filenames:
            path = os.path.join(POSTS_DIR, filename)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for existing permalink
                if re.search(r"^permalink:", content, re.MULTILINE):
                    new_content = re.sub(r"^permalink:.*$", f"permalink: {target_permalink}", content, flags=re.MULTILINE)
                    if new_content != content:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        log(f"Updated permalink in {filename}")
                else:
                    # Inject permalink
                    match = re.search(r"^---\s*$", content, re.MULTILINE)
                    if match:
                        second_match = re.search(r"^---\s*$", content[match.end():], re.MULTILINE)
                        if second_match:
                            insert_index = match.end() + second_match.start()
                            # Use newlines to be safe
                            new_content = content[:insert_index] + f"permalink: {target_permalink}\n" + content[insert_index:]
                            with open(path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            log(f"Injected permalink in {filename}")
                        else:
                             log(f"Could not find second --- in {filename}")
                    else:
                        log(f"Could not find first --- in {filename}")
                        
            except Exception as e:
                log(f"Error processing {path}: {e}")

if __name__ == "__main__":
    unify_permalinks()
