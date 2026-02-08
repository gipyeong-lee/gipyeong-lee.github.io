import os
import sys
import subprocess
import re
import time

POSTS_DIR = "_posts"

def call_gemini_cli(prompt):
    """Calls the Gemini CLI with the given prompt via piping."""
    try:
        process = subprocess.Popen(
            ['gemini'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=prompt)
        
        if process.returncode != 0:
            print(f"Gemini CLI Error: {stderr}")
            return None
            
        return stdout.strip()
    except Exception as e:
        print(f"Failed to execute Gemini CLI: {e}")
        return None

def translate_content(content, target_lang):
    """Translates content using Gemini CLI."""
    prompt = f"""
    You are a professional technical translator.
    
    [TASK]
    Translate the following Markdown blog post to {target_lang}.
    
    [RULES]
    1. Preserve the Front Matter exactly as is, BUT interpret and translate the 'title' and 'description' fields if they exist.
    2. Do NOT translate the 'layout', 'date', 'image', 'tags', 'style', 'color' fields in Front Matter.
    3. Translate the main content naturally and professionally.
    4. Maintain all Markdown formatting, code blocks, and links.
    5. Output ONLY the translated content starting with the Front Matter.
    
    [CONTENT]
    {content}
    """
    return call_gemini_cli(prompt)

def process_file(filename):
    """Checks and translates a single file if translations are missing."""
    file_path = os.path.join(POSTS_DIR, filename)
    base_name, ext = os.path.splitext(filename)
    
    # Skip if it's already a translated file
    if base_name.endswith('.en') or base_name.endswith('.ja'):
        return

    en_filename = f"{base_name}.en{ext}"
    ja_filename = f"{base_name}.ja{ext}"
    en_path = os.path.join(POSTS_DIR, en_filename)
    ja_path = os.path.join(POSTS_DIR, ja_filename)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Translate to English
    if not os.path.exists(en_path):
        print(f"Translating {filename} to English...")
        translated = translate_content(content, "English")
        if translated:
            translated = re.sub(r'^```markdown\s*', '', translated)
            translated = re.sub(r'^```\s*', '', translated)
            translated = re.sub(r'\s*```$', '', translated)
            with open(en_path, 'w', encoding='utf-8') as f:
                f.write(translated.strip())
            print(f"Created: {en_filename}")
        else:
            print(f"Failed to translate {filename} to English")
        time.sleep(2) # Prevent rate limiting
    else:
        print(f"Skipping English (exists): {en_filename}")

    # Translate to Japanese
    if not os.path.exists(ja_path):
        print(f"Translating {filename} to Japanese...")
        translated = translate_content(content, "Japanese")
        if translated:
            translated = re.sub(r'^```markdown\s*', '', translated)
            translated = re.sub(r'^```\s*', '', translated)
            translated = re.sub(r'\s*```$', '', translated)
            with open(ja_path, 'w', encoding='utf-8') as f:
                f.write(translated.strip())
            print(f"Created: {ja_filename}")
        else:
            print(f"Failed to translate {filename} to Japanese")
        time.sleep(2) # Prevent rate limiting
    else:
        print(f"Skipping Japanese (exists): {ja_filename}")

def main():
    print("Starting batch translation...")
    files = sorted([f for f in os.listdir(POSTS_DIR) if f.endswith('.md')])
    
    for filename in files:
        process_file(filename)
        
    print("Batch translation complete.")

if __name__ == "__main__":
    main()
