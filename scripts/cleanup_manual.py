import os
import shutil
import unicodedata

BASE_DIR = os.getcwd()
POSTS_DIR = os.path.join(BASE_DIR, "_posts")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

# Match "2023-04-20" and "AI" to avoid unicode issues
TARGET_DATE = "2023-04-20"
TARGET_KEYWORD = "AI"
NEW_IMAGE_NAME = "2023-04-20-what-is-fine-tuning.jpg"

def cleanup():
    # 1. Rename Image
    for f in os.listdir(IMAGES_DIR):
        if TARGET_DATE in f and TARGET_KEYWORD in f and f.endswith(".jpg"):
            print(f"Found target image: {repr(f)}")
            old_path = os.path.join(IMAGES_DIR, f)
            new_path = os.path.join(IMAGES_DIR, NEW_IMAGE_NAME)
            
            try:
                os.rename(old_path, new_path)
                print(f"Renamed image: {f} -> {NEW_IMAGE_NAME}")
            except Exception as e:
                print(f"Error renaming {f}: {e}")
            break 

    # 2. Delete Old Posts
    for f in os.listdir(POSTS_DIR):
        if TARGET_DATE in f and TARGET_KEYWORD in f and f.endswith(".md"):
            print(f"Found old post: {repr(f)}")
            p_path = os.path.join(POSTS_DIR, f)
            try:
                os.remove(p_path)
                print(f"Deleted old post: {f}")
            except Exception as e:
                print(f"Error deleting post {f}: {e}")

if __name__ == "__main__":
    cleanup()
