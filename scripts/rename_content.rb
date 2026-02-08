require 'yaml'
require 'fileutils'

POSTS_DIR = "_posts"
IMAGES_DIR = "images"
LOG_FILE = "rename.log"

def log(msg)
  puts msg
  File.open(LOG_FILE, "a") { |f| f.puts(msg) }
end

def slugify(text)
  text.downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')
end

def process_renaming
  File.delete(LOG_FILE) if File.exist?(LOG_FILE)
  log("Starting content standardization...")

  # Group files by YYYY-MM-DD-Basename
  groups = {}
  
  Dir.foreach(POSTS_DIR) do |f|
    next if f == '.' || f == '..' || !f.end_with?('.md')
    
    # Analyze filename structure
    # Expected: YYYY-MM-DD-Title.lang.md or YYYY-MM-DD-Title.md
    if f =~ /^(\d{4}-\d{2}-\d{2})-(.*?)(\.en|\.ja|\.ko)?\.md$/
      date = $1
      base_slug = $2
      
      key = "#{date}-#{base_slug}"
      groups[key] ||= { :files => [], :date => date }
      groups[key][:files] << f
    end
  end

  log("Found #{groups.keys.length} post groups.")

  groups.each do |key, data|
    files = data[:files]
    date = data[:date]
    
    # 1. Determine Target English Slug
    english_title = nil
    
    # Try to find English file first
    en_file = files.find { |f| f.end_with?('.en.md') }
    if en_file
      content = File.read(File.join(POSTS_DIR, en_file))
      if content =~ /\A(---\s*\n.*?\n?)^(---\s*$\n?)/m
        front_matter = YAML.load($1)
        english_title = front_matter['title']
      end
    end
    
    # Fallback to default file if no English file (or try to use its title if it looks English?)
    # If we can't find an English title, we might have to skip or use the existing slug if it's ASCII
    if english_title.nil?
      # Try default file
      default_file = files.find { |f| !f.include?('.en.md') && !f.include?('.ja.md') }
      if default_file
        content = File.read(File.join(POSTS_DIR, default_file))
        if content =~ /\A(---\s*\n.*?\n?)^(---\s*$\n?)/m
          front_matter = YAML.load($1)
          # check if title is ASCII?
          if front_matter['title'] && front_matter['title'].ascii_only?
             english_title = front_matter['title']
          end
        end
      end
    end

    if english_title.nil?
      log("SKIPPING [#{key}]: Could not determine English title.")
      next
    end

    new_slug = slugify(english_title)
    new_base = "#{date}-#{new_slug}"
    
    log("Processing [#{key}] -> [#{new_base}]")
    
    # 2. Rename Markdown Files & Update Image References
    target_image_filename = nil
    
    # First, find the image used in these posts (assume consistent)
    # We need to find the OLD image name to rename it.
    old_image_path = nil
    old_image_name = nil
    
    files.each do |fname|
      path = File.join(POSTS_DIR, fname)
      content = File.read(path)
      if content =~ /^image:\s*(.*)$/
        img_val = $1.strip
        # Remove quotes if present
        img_val = img_val.gsub(/^["']|["']$/, '')
        
        if !img_val.empty? && !img_val.start_with?('http')
          # Check if this image exists in images/
          if File.exist?(File.join(IMAGES_DIR, img_val))
            old_image_name = img_val
            old_image_path = File.join(IMAGES_DIR, img_val)
            break
          end
        end
      end
    end

    # Rename Image if found
    if old_image_path
      ext = File.extname(old_image_name)
      new_image_name = "#{new_base}#{ext}"
      new_image_path = File.join(IMAGES_DIR, new_image_name)
      
      if old_image_path != new_image_path
        FileUtils.mv(old_image_path, new_image_path)
        log("  Renamed Image: #{old_image_name} -> #{new_image_name}")
      end
      target_image_filename = new_image_name
    end

    # Rename Markdown files and Update Content
    files.each do |fname|
      old_path = File.join(POSTS_DIR, fname)
      
      # Determine new filename
      lang_ext = ""
      if fname.end_with?('.en.md')
        lang_ext = ".en"
      elsif fname.end_with?('.ja.md')
        lang_ext = ".ja"
      elsif fname.end_with?('.ko.md')
        lang_ext = ".ko"
      end
      
      new_filename = "#{new_base}#{lang_ext}.md"
      new_path = File.join(POSTS_DIR, new_filename)
      
      # Read Content
      content = File.read(old_path)
      
      # Update Image Front Matter if we renamed an image
      if target_image_filename
        # Regex replace image: value
        content = content.gsub(/^image:.*$/, "image: #{target_image_filename}")
      end
      
      # Write new file (rename)
      if old_path != new_path
        File.write(new_path, content)
        File.delete(old_path)
        log("  Renamed Post: #{fname} -> #{new_filename}")
      else
        # Just update content (image path)
        File.write(old_path, content)
        log("  Updated Post: #{fname} (Image updated)")
      end
    end

  end
  
  log("Done.")
end

process_renaming
