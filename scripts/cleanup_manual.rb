LOG_FILE = "ruby_cleanup.log"

def log(msg)
  puts msg
  File.open(LOG_FILE, "a") { |f| f.puts(msg) }
end

begin
  File.delete(LOG_FILE) if File.exist?(LOG_FILE)
  log("Starting Ruby cleanup...")
  
  # Clean posts
  posts_dir = "_posts"
  if Dir.exist?(posts_dir)
    Dir.foreach(posts_dir) do |f|
        if f.include?("2023-04-20") && f.include?("AI") && f.end_with?(".md")
            path = File.join(posts_dir, f)
            log("Deleting post: #{f}")
            File.delete(path)
        end
    end
  else
    log("_posts dir not found")
  end

  # Rename image
  images_dir = "images"
  target_new_name = "2023-04-20-what-is-fine-tuning.jpg"
  
  if Dir.exist?(images_dir)
     Dir.foreach(images_dir) do |f|
        if f.include?("2023-04-20") && f.include?("AI") && f.end_with?(".jpg")
            old_path = File.join(images_dir, f)
            new_path = File.join(images_dir, target_new_name)
            
            if old_path != new_path
                log("Renaming image: #{f} -> #{target_new_name}")
                File.rename(old_path, new_path)
            end
        end
     end
  else
    log("images dir not found")
  end

  log("Cleanup finished.")
rescue => e
  log("Error: #{e.message}")
end
