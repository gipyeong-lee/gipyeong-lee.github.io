# Tech Journal (AI News Agency)

This is a professional tech journalism site powered by Jekyll and AI. It features a custom "News Agency" theme with a 3-column grid layout, news ticker, and AI analyst insights.

## Features
- **AI-Powered Content**: Automatic content generation, review, and refinement using Gemini CLI.
- **Multilingual Support**: Supports Korean (Default), English, and Japanese.
- **News Agency Layout**: Magazine-style grid, ticker, and journalist profiles.
- **Automated Workflow**: From keyword discovery to multilingual publication.

## Local Development

### Prerequisites
- **Ruby & Bundler**: Required for Jekyll.
  > **Note**: If using Ruby 3.4+ (or Homebrew's latest Ruby 4.0), ensure you install the updated dependencies in `Gemfile` (`csv`, `base64`, etc.) which are handled automatically by `bundle install`.
- **Python 3.x**: Required for automation scripts.
- **Gemini CLI**: Must be installed and authenticated.

### 1. Setup Environment
```bash
# Install Ruby Dependencies
bundle install

# Install Python Dependencies
pip install -r scripts/requirements.txt
```

### 2. Run Locally
To start the Jekyll development server:
```bash
bundle exec jekyll serve
```
Access the site at `http://localhost:4000`.

### Troubleshooting
If you encounter `Gem::GemNotFoundException` or encoding errors (e.g., `invalid byte sequence`), use this command:
```bash
export RUBYOPT="-Eutf-8"
/opt/homebrew/opt/ruby/bin/bundle exec jekyll serve
```

## Content Automation

### Auto-Post Script
To generate a new blog post automatically (including KR/EN/JA translations):
```bash
python3 scripts/auto_poster.py
```
This script will:
1. Fetch trending keywords from Google Trends (KR).
2. Check `scripts/history.csv` for duplicates.
3. Research the topic using DuckDuckGo.
4. Generate, review, and refine a draft using Gemini.
5. Translate the post into English and Japanese.
6. Save all files to `_posts/`.

## Deployment

### GitHub Pages
This site is configured to deploy automatically via **GitHub Actions**.

1. **Push to Main**: Simply push your changes (including new posts) to the `main` branch.
2. **Action Trigger**: The `.github/workflows/jekyll.yml` workflow will automatically build and deploy the site.

### Manual Build
If you need to build the static files manually:
```bash
bundle exec jekyll build
```
The output will be in the `_site/` directory.
