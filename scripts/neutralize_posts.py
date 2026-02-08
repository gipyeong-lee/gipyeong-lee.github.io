import os

POSTS_DIR = b"_posts"
MATCH_BYTES = b"2023-04-20-AI"

def neutralize_posts():
    print(f"Scanning {POSTS_DIR} to neutralize...")
    try:
        found = False
        for f in os.listdir(POSTS_DIR):
            if MATCH_BYTES in f:
                found = True
                path = os.path.join(POSTS_DIR, f)
                print(f"Neutralizing: {f}")
                try:
                    # Overwrite content with published: false
                    with open(path, 'wb') as file:
                        file.write(b"---\npublished: false\n---\n")
                    print(f"Neutralized.")
                except Exception as e:
                    print(f"Error neutralizing: {e}")
        if not found:
            print("No matching posts found.")
    except Exception as e:
        print(f"Error scanning posts: {e}")

if __name__ == "__main__":
    neutralize_posts()
