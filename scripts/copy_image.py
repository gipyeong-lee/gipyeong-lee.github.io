#!/usr/bin/env python3
import os
import shutil

images_dir = "/Users/gipyeonglee/Documents/0.workspace/gipyeong-lee.github.io/images"

# Find the file with 2023-04-20 in the name
for filename in os.listdir(images_dir):
    if "2023-04-20" in filename and filename != "2023-04-20-ai-fine-tuning.jpg":
        source = os.path.join(images_dir, filename)
        dest = os.path.join(images_dir, "2023-04-20-ai-fine-tuning.jpg")
        print(f"Found: {filename}")
        print(f"Copying to: {dest}")
        shutil.copy2(source, dest)
        print("Copy successful!")
        break
else:
    print("No matching file found!")
    print("Files in directory:")
    for f in os.listdir(images_dir):
        print(f"  {f}")
