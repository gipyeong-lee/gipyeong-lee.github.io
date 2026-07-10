# Precompute the translation family for every post once per build.
#
# head.html (hreflang) and language-switcher.html previously ran
# `site.posts | where: "ref", page.ref` — a full O(posts) scan executed
# twice per page, which scales quadratically with the archive. This hook
# builds one ref => posts index and exposes it as `page.translations`
# (array of { "lang", "url" } hashes).
Jekyll::Hooks.register :site, :pre_render do |site|
  by_ref = Hash.new { |h, k| h[k] = [] }

  site.posts.docs.each do |post|
    ref = post.data["ref"]
    by_ref[ref] << post if ref
  end

  site.posts.docs.each do |post|
    ref = post.data["ref"]
    next unless ref

    post.data["translations"] = by_ref[ref].map do |p|
      { "lang" => p.data["lang"], "url" => p.url }
    end
  end
end
