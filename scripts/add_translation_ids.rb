require 'yaml'
require 'securerandom'

POSTS_DIR = "_posts"
LOG_FILE = "logic.log"

def log(msg)
  File.open(LOG_FILE, "a") { |f| f.puts(msg) }
end

def add_translation_ids
  if File.exist?(LOG_FILE)
    File.delete(LOG_FILE)
  end
  # Create log file explicitly
  File.open(LOG_FILE, "w") {}
  
  log("Starting Ruby script...")

  # Group files
  groups = {}
  
  if !Dir.exist?(POSTS_DIR)
     log("Directory #{POSTS_DIR} not found!")
     return
  end

  Dir.foreach(POSTS_DIR) do |f|
    next if f == '.' || f == '..' || !f.end_with?('.md')
    
    base = f
    if f.end_with?(".en.md")
      base = f[0...-6]
    elsif f.end_with?(".ja.md")
      base = f[0...-6]
    elsif f.end_with?(".ko.md")
      base = f[0...-6]
    else
      base = f[0...-3]
    end
    
    groups[base] ||= []
    groups[base] << f
  end
  
  log("Found groups: #{groups.keys.length}")

  groups.each do |base, filenames|
    next if filenames.empty?
    
    existing_ref = nil
    
    # Pass 1: find existing ref
    filenames.each do |fname|
      path = File.join(POSTS_DIR, fname)
      begin
        content = File.read(path)
        if content =~ /\A(---\s*\n.*?\n?)^(---\s*$\n?)/m
          front_matter = YAML.load($1)
          if front_matter['ref']
            existing_ref = front_matter['ref']
            log("[#{base}] Found existing ref: #{existing_ref}")
            break
          end
        end
      rescue => e
        log("Error reading #{fname}: #{e}")
      end
    end
    
    existing_ref ||= base # Use basename as ref
    
    # Pass 2: update
    filenames.each do |fname|
      path = File.join(POSTS_DIR, fname)
      begin
        content = File.read(path)
        if content =~ /\A(---\s*\n.*?\n?)^(---\s*$\n?)/m
          header = $1
          body = $'
          front_matter = YAML.load(header)
          
          if !front_matter['ref'] || front_matter['ref'] != existing_ref
            front_matter['ref'] = existing_ref
            
            new_header = YAML.dump(front_matter)
            
            final_content = "#{new_header}---\n#{body}"
            File.write(path, final_content)
            log("Updated #{fname} with ref: #{existing_ref}")
          end
        end
      rescue => e
        log("Error updating #{fname}: #{e}")
      end
    end
  end
  log("Done.")
end

add_translation_ids
