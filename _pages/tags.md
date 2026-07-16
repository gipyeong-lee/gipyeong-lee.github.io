---
title: "tags"
layout: default
permalink: "/tags"
order: 1
---

{%- comment -%}
  Tag index: only tags that have a generated tag page (site.linkable_tags,
  set by _plugins/tag_pages.rb). The old version rendered a full article
  card for every post under every one of ~5,700 tags — a 34MB page.
{%- endcomment -%}
<div class="container">
  <div class="row">
    <div class="col col-12">
      <h1 class="archive-title">Tags</h1>
      <div class="categories" style="display:flex;flex-wrap:wrap;gap:8px;padding:24px 0;">
        {% for tag in site.tags %}
          {%- if site.linkable_tags contains tag[0] %}
          <a class="article__tag" href="{{ site.baseurl }}/tag/{{ tag[0] | downcase | replace: " ", "-" }}/">
            {{ tag[0] }} <small>({{ tag[1].size }})</small>
          </a>
          {%- endif %}
        {% endfor %}
      </div>
    </div>
  </div>
</div>
