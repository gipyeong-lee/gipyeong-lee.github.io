# Replaces the jekyll/tagging gem.
#
# Only tags with at least `tag_min_posts` posts (default 5) get a
# /tag/<slug>/ page — LLM-generated tags are mostly unique, and the ~5,700
# pages the gem generated for them bloated site.pages (and every template
# that scans it) plus the deploy artifact.
#
# Also annotates each post with `linkable_tags` (the subset of its tags
# that have a page) and exposes the full sorted list as
# `site.linkable_tags`, so templates decide link-vs-text in O(1) instead
# of scanning site.tags.
#
# URL scheme matches both the old gem and article-content.html exactly:
# downcase, spaces to dashes (CJK preserved).
require "set"

module Blog
  class TagPage < Jekyll::Page
    def initialize(site, dir, layout, tag, posts)
      @site = site
      @base = site.source
      slug = tag.downcase.gsub(" ", "-")
      @dir = File.join(dir, slug)
      @name = "index.html"
      process(@name)
      @content = ""
      @data = {
        "layout" => layout,
        "tag" => tag,
        "posts" => posts,
        "title" => "Tag: #{tag}",
      }
    end
  end

  class TagPageGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      min = site.config["tag_min_posts"] || 5
      dir = site.config["tag_page_dir"] || "tag"
      layout = site.config["tag_page_layout"] || "tag_page"

      valid = site.tags.select { |_tag, posts| posts.size >= min }
      linkable = valid.keys.sort
      site.config["linkable_tags"] = linkable
      lset = linkable.to_set

      site.posts.docs.each do |post|
        tags = post.data["tags"] || []
        post.data["linkable_tags"] = tags.select { |t| lset.include?(t) }
      end

      valid.each do |tag, posts|
        sorted = posts.sort_by { |p| -p.date.to_f }
        site.pages << TagPage.new(site, dir, layout, tag, sorted)
      end
    end
  end
end
