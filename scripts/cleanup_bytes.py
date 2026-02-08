import os

POSTS_DIR = b"_posts"
IMAGES_DIR = b"images"
MATCH_BYTES = b"2023-04-20-AI"

def cleanup():
    print(f"Scanning {POSTS_DIR} in bytes mode...")
    try:
        found = False
        for f in os.listdir(POSTS_DIR):
            if MATCH_BYTES in f:
                found = True
                path = os.path.join(POSTS_DIR, f)
                print(f"Found bytes match: {f}")
                try:
                    os.remove(path)
                    print(f"Deleted.")
                except Exception as e:
                    print(f"Error deleting: {e}")
        if not found:
            print("No matching posts found in bytes.")
    except Exception as e:
        print(f"Error scanning posts: {e}")

    print(f"Scanning {IMAGES_DIR} in bytes mode...")
    try:
        found = False
        for f in os.listdir(IMAGES_DIR):
            if MATCH_BYTES in f:
                found = True
                path = os.path.join(IMAGES_DIR, f)
                print(f"Found bytes match: {f}")
                try:
                    os.remove(path)
                    print(f"Deleted.")
                except Exception as e:
                    print(f"Error deleting: {e}")
        if not found:
            print("No matching images found in bytes.")
    except Exception as e:
        print(f"Error scanning images: {e}")

if __name__ == "__main__":
    cleanup()
