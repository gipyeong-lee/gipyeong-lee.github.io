import os

with open("debug_files.log", "w") as f:
    f.write("--- POSTS ---\n")
    try:
        for x in os.listdir("_posts"):
            f.write(f"{repr(x)}\n")
    except Exception as e:
        f.write(f"Error listing _posts: {e}\n")
        
    f.write("\n--- IMAGES ---\n")
    try:
        for x in os.listdir("images"):
            f.write(f"{repr(x)}\n")
    except Exception as e:
        f.write(f"Error listing images: {e}\n")
