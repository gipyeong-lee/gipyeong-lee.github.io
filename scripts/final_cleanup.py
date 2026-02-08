import os

POSTS_DIR = "_posts"
IMAGES_DIR = "images"
TARGET_DATE = "2023-04-20"
KEEP_KEYWORD = "what-is-fine-tuning"

def cleanup():
    # Posts
    print(f"Scanning {POSTS_DIR}...")
    try:
        for f in os.listdir(POSTS_DIR):
            if TARGET_DATE in f and KEEP_KEYWORD not in f:
                path = os.path.join(POSTS_DIR, f)
                try:
                    os.remove(path)
                    print(f"Deleted post: {f}")
                except Exception as e:
                    print(f"Error deleting post {f}: {e}")
    except Exception as e:
        print(f"Error scanning posts: {e}")

    # Images
    print(f"Scanning {IMAGES_DIR}...")
    try:
        for f in os.listdir(IMAGES_DIR):
            if TARGET_DATE in f and KEEP_KEYWORD not in f:
                path = os.path.join(IMAGES_DIR, f)
                try:
                    os.remove(path)
                    print(f"Deleted image: {f}")
                except Exception as e:
                    print(f"Error deleting image {f}: {e}")
    except Exception as e:
        print(f"Error scanning images: {e}")

if __name__ == "__main__":
    cleanup()
