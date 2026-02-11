import os
import sys
import subprocess
import re

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

def translate_file(filename, target_lang):
    """Translates a markdown file to the target language."""
    filepath = os.path.join(POSTS_DIR, filename)
    
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"Translating {filename} to {target_lang}...")
    
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
    
    translated_content = call_gemini_cli(prompt)
    
    if translated_content:
        # Clean up code blocks if present in output
        translated_content = re.sub(r'^```markdown\s*', '', translated_content)
        translated_content = re.sub(r'^```\s*', '', translated_content)
        translated_content = re.sub(r'\s*```$', '', translated_content)
        
        # Determine new filename
        base_name, ext = os.path.splitext(filename)
        lang_map = {
            "English": "en",
            "Japanese": "ja",
            "Simplified Chinese": "zh-cn",
            "Traditional Chinese": "zh-tw",
        }
        lang_code = lang_map.get(target_lang, "en")
        new_filename = f"{base_name}.{lang_code}{ext}"
        new_filepath = os.path.join(POSTS_DIR, new_filename)
        
        # --- Ensure Permalink Exists ---
        # If source had permalink, it should be in translated_content (due to prompt rule).
        # But if not, or if we want to enforce standard:
        if "permalink:" not in translated_content:
             # Extract date and slug from filename: YYYY-MM-DD-SLUG...
             match = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+?)(\.|$)", filename)
             if match:
                 y_m_d = match.group(1).replace('-', '/')
                 slug = match.group(2)
                 # Handle if slug has .en or similar (though filename is input)
                 # Actually base_name is usually YYYY-MM-DD-slug (without ext)
                 # But if filename input was "YYYY-MM-DD-slug.md"
                 
                 # Let's verify base_name logic. 
                 # If filename="2023-01-01-foo.md", base_name="2023-01-01-foo"
                 # If filename="2023-01-01-foo.en.md", base_name="2023-01-01-foo.en"? 
                 # wait, splitext only takes last extension.
                 # So if input is .md, base_name is date-slug.
                 
                 # Parse date and slug from base_name more carelessly
                 parts = base_name.split('-', 3)
                 if len(parts) >= 4:
                     y, m, d, raw_slug = parts[0], parts[1], parts[2], parts[3]
                     # Remove lang suffix if present in slug (unlikely if strictly named)
                     raw_slug = re.sub(r'\.(en|ja|ko|zh-cn|zh-tw)$', '', raw_slug)
                     permalink = f"/{y}/{m}/{d}/{raw_slug}/"
                     
                     # Inject
                     second_dash_idx = translated_content.find('---', 3)
                     if second_dash_idx != -1:
                         insertion = f"permalink: {permalink}\n"
                         translated_content = translated_content[:second_dash_idx] + insertion + translated_content[second_dash_idx:]

        with open(new_filepath, 'w', encoding='utf-8') as f:
            f.write(translated_content.strip())
            
        print(f"Saved translated file: {new_filepath}")
    else:
        print("Translation failed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/translate_post.py <filename>")
        sys.exit(1)
        
    target_file = sys.argv[1]
    
    # Translate to English
    translate_file(target_file, "English")

    # Translate to Japanese
    translate_file(target_file, "Japanese")

    # Translate to Simplified Chinese
    translate_file(target_file, "Simplified Chinese")

    # Translate to Traditional Chinese
    translate_file(target_file, "Traditional Chinese")
