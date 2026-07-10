# Precompute "related posts" once per build.
#
# related-posts.html previously scanned up to 600 same-language posts with
# nested tag loops in Liquid for every post page. Doing the same scoring in
# Ruby with an inverted tag index is orders of magnitude cheaper.
#
# Behavior preserved from the Liquid version: same language, shared-tag
# overlap scoring, excludes the current post and its translation family,
# candidates limited to the most recent posts per language (fresh-content
# bias), top 4 exposed as `page.related` [{url,title,image,image_alt,date}].
Jekyll::Hooks.register :site, :pre_render do |site|
  scan_cap = 600

  posts_by_lang = Hash.new { |h, k| h[k] = [] }
  site.posts.docs.each do |post|
    lang = post.data["lang"] || site.config["default_lang"] || "ko"
    posts_by_lang[lang] << post
  end

  posts_by_lang.each_value do |posts|
    # site.posts.docs is oldest-first; recent first for the scan cap
    candidates = posts.sort_by { |p| p.date }.reverse.first(scan_cap)

    tag_index = Hash.new { |h, k| h[k] = [] }
    candidates.each do |p|
      (p.data["tags"] || []).each { |t| tag_index[t] << p }
    end

    posts.each do |post|
      tags = post.data["tags"] || []
      next if tags.empty?

      scores = Hash.new(0)
      tags.each do |t|
        tag_index[t].each { |c| scores[c] += 1 }
      end
      scores.delete(post)
      if (ref = post.data["ref"])
        scores.reject! { |c, _| c.data["ref"] == ref }
      end

      top = scores.sort_by { |c, s| [-s, c.date.to_i * -1] }.first(4)
      post.data["related"] = top.map do |c, _|
        {
          "url" => c.url,
          "title" => c.data["title"],
          "image" => c.data["image"],
          "image_alt" => c.data["image_alt"] || c.data["title"],
          "date" => c.date.strftime("%b %d, %Y"),
        }
      end
    end
  end
end
