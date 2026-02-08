import os

DIR = "_posts"

def fix():
    print(f"Scanning {DIR}...")
    files = os.listdir(DIR)
    count = 0
    for f in files:
        if not f.endswith(".md"):
            continue
            
        path = os.path.join(DIR, f)
        try:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if "permalink:" in content:
                continue
                
            # Parse filename: YYYY-MM-DD-SLUG.md
            parts = f.split('-', 3)
            if len(parts) < 4:
                print(f"Skipping malformed filename: {f}")
                continue
                
            y, m, d = parts[0], parts[1], parts[2]
            rest = parts[3]
            
            slug = rest
            if slug.endswith(".en.md"): slug = slug[:-6]
            elif slug.endswith(".ja.md"): slug = slug[:-6]
            elif slug.endswith(".ko.md"): slug = slug[:-6]
            elif slug.endswith(".md"): slug = slug[:-3]
            
            link = f"/{y}/{m}/{d}/{slug}/"
            
            # Inject
            if content.startswith("---"):
                idx = content.find("---", 3)
                if idx > 0:
                    new_content = content[:idx] + f"permalink: {link}\n" + content[idx:]
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f"Fixed {f}")
                    count += 1
        except Exception as e:
            print(f"Error reading {f}: {e}")

    print(f"Finished. Fixed {count} files.")

if __name__ == "__main__":
    fix()
