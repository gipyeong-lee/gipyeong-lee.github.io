# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Multilingual tech blog (Korean/English/Japanese) built with Jekyll 4.x, hosted on GitHub Pages. Uses a customized "Zolan" theme with a news agency-style layout. Content generation is automated via Python scripts using Gemini CLI.

**Live site:** https://gipyeong-lee.github.io

## Build & Serve Commands

```bash
# Install Ruby dependencies
bundle install

# Local development server (http://localhost:4000)
bundle exec jekyll serve

# If encoding errors occur (Ruby 3.4+/Homebrew Ruby)
export RUBYOPT="-Eutf-8"
/opt/homebrew/opt/ruby/bin/bundle exec jekyll serve

# Production build
bundle exec jekyll build
```

## Content Automation

Content generation and video pipeline are managed by a separate private service:
**[EternaxCode/mindtickle-studio](https://github.com/EternaxCode/mindtickle-studio)** (private repo)

The service reads `_posts/` and `images/` from this repo and pushes new content via git.

## Post Conventions

### File Naming
```
_posts/YYYY-MM-DD-slug.md        # Korean (default)
_posts/YYYY-MM-DD-slug.en.md     # English
_posts/YYYY-MM-DD-slug.ja.md     # Japanese
```

### Front Matter
```yaml
---
layout: post
title: "Post Title"
tags: [tag1, tag2]
style: border          # or fill (optional)
color: primary         # primary|info|success|warning|danger (optional)
description: "SEO description"
image: filename.jpg    # from /images/ directory (optional)
ref: YYYY-MM-DD-slug   # links translations together
---
```

The `ref` field must be identical across all language versions of the same post.

## Architecture

- **Theme:** Forked Zolan theme (`gem "zolan-jekyll-theme"` from `github.com/gipyeong-lee/zolan`)
- **Layouts:** `default.html` (base) > `post.html`, `page.html`, `home-news.html` (news grid), `tag_page.html`
- **SASS structure:** `_sass/` organized as `0-settings/` (variables, mixins) > `1-tools/` (grid, normalize) > `2-base/` > `3-modules/` (header, footer, search) > `4-layouts/` (page-specific)
- **Site config:** `_data/settings.yml` (author, social links, analytics, Disqus)
- **Search:** Client-side via `search.json` (Liquid-generated JSON index) + `js/common.js`
- **Automation:** Managed by [EternaxCode/mindtickle-studio](https://github.com/EternaxCode/mindtickle-studio) (private)

## Deployment

Push to `main` branch triggers GitHub Actions (`.github/workflows/jekyll.yml`) which builds and deploys to GitHub Pages automatically.

## Key Configuration

- **Pagination:** 5 posts/page (`/page/:num`)
- **Permalinks:** Pretty URLs (no `.html` extension)
- **Tag pages:** `/tag/tag-name/` via `jekyll/tagging` plugin
- **Comments:** Disqus (shortname: `gipyeong`)
- **Analytics:** Google Analytics 4 (`G-BZ475R8BPR`)
