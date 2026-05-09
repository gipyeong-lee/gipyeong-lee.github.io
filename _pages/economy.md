---
title: "경제"
layout: default
permalink: /economy/
order: 0
description: "거시경제 관련 글 모음 — 금리, 물가, 환율, 통화정책, 글로벌 경제 동향"
---

{% assign macro_posts = site.posts | where: "lang", "ko" | where_exp: "p", "p.tags contains 'Macro'" %}

<div class="container">
  <div class="row">
    <div class="col col-12">
      <header class="economy-hero" style="padding: 2.5rem 0 1.25rem; border-bottom: 1px solid var(--border-color, #e5e7eb); margin-bottom: 1.5rem;">
        <h1 style="margin: 0 0 0.5rem; font-size: 2rem; letter-spacing: -0.02em;">거시경제</h1>
        <p style="margin: 0; color: #6b7280; font-size: 1rem;">금리 · 물가 · 환율 · 통화정책 · 글로벌 경제 동향</p>
      </header>
    </div>
  </div>
</div>

{% if macro_posts.size == 0 %}
<div class="container">
  <div class="row">
    <div class="col col-12">
      <div style="padding: 3rem 1.5rem; text-align: center; border: 1px dashed #d1d5db; border-radius: 8px; color: #6b7280;">
        <div style="font-size: 1.05rem; margin-bottom: 0.5rem;">아직 게시된 거시경제 글이 없습니다.</div>
        <div style="font-size: 0.9rem;">자동화 파이프라인이 첫 글을 준비 중입니다.</div>
      </div>
    </div>
  </div>
</div>
{% else %}
<div class="container">
  <div class="row">
    <div class="col col-12">
      <div class="news-grid">

        <div class="news-main-column">
          {% assign featured_post = macro_posts.first %}
          <article class="featured-article">
            {% if featured_post.image %}
            <a href="{{ site.baseurl }}{{ featured_post.url }}">
              <img src="/images/{{ featured_post.image }}" alt="{{ featured_post.title }}" class="featured-image">
            </a>
            {% endif %}
            <div class="category-label">Macro</div>
            <h2 class="post-title"><a href="{{ site.baseurl }}{{ featured_post.url }}">{{ featured_post.title }}</a></h2>
            <div class="post-excerpt">{{ featured_post.excerpt | strip_html | truncatewords: 30 }}</div>
            <div class="meta" style="margin-top: 10px; color: #888; font-size: 0.9em;">
              By <span style="color:black; font-weight:bold">{{ featured_post.reporter | default: "AI Reporter" }}</span> | {{ featured_post.date | date_to_string }}
            </div>
          </article>

          <div class="sub-articles-grid">
            {% for post in macro_posts offset:1 limit:6 %}
            <div class="sub-article-card">
              {% if post.image %}
              <a href="{{ site.baseurl }}{{ post.url }}">
                <img src="/images/{{ post.image }}" alt="{{ post.title }}" class="card-image">
              </a>
              {% endif %}
              <div class="card-content">
                <div class="category-label" style="font-size: 10px; color: #0056b3; margin-bottom: 5px;">Macro</div>
                <h3><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
                <div class="meta">{{ post.date | date: "%b %d" }}</div>
              </div>
            </div>
            {% endfor %}
          </div>
        </div>

        <aside class="news-sidebar">
          <div class="sidebar-section">
            <h4 class="section-title">More Macro</h4>
            <ul class="sidebar-list">
              {% for post in macro_posts offset:7 limit:8 %}
              <li>
                <a href="{{ site.baseurl }}{{ post.url }}">
                  <span style="display:block; font-size: 0.9em; line-height: 1.4;">{{ post.title }}</span>
                  <span style="font-size: 0.8em; color: #999;">{{ post.date | date: "%b %d" }}</span>
                </a>
              </li>
              {% endfor %}
            </ul>
          </div>
        </aside>

      </div>
    </div>
  </div>
</div>
{% endif %}
