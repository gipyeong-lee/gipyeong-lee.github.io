---
layout: post
title: "Can't sing a song? The truth behind Claude refusing to reproduce lyrics"
description: "We explain in simple terms why the recently updated Claude AI refuses requests to write song lyrics or draw famous characters, along with the reasoning and context behind it."
summary: "The recently updated Claude AI has added new rules to its system prompt that strictly prohibit the reproduction of song lyrics, poetry, and famous characters or designs in order to protect copyright."
tags: [AI, Claude, Copyright, Tech Knowledge]
image: 2026-09-06-Claudes-new-system-prompt-doesnt-want-to-reproduce-song-lyrics.jpg
image_alt: "A conceptual image of Claude AI refusing a user's request for song lyrics due to copyright protection policies"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Copyright issues are one of the biggest challenges facing generative AI. I believe this measure is an important process for AI to grow into a tool that creates new value rather than simply copying creative works."
quiz:
  - question: "What is the main reason Claude refuses to provide song lyrics?"
    choices: ["AI memory capacity limitations", "Copyright protection and policy compliance", "Deletion of song lyric data"]
    answer: 1
    explanation: "Claude has introduced new system guidelines to prevent the reproduction of copyrighted lyrics, poetry, and passages from books."
  - question: "What is the scope of Claude's new copyright policy?"
    choices: ["Web version and mobile app", "Includes all APIs", "Offline only"]
    answer: 0
    explanation: "Anthropic stated that this system prompt update applies to the claude.ai website and mobile app, but does not apply to the API."
  - question: "Claude does not refuse to provide lyrics entirely. What is an exception?"
    choices: ["When the user pays", "Works published before 1929", "When Claude is in a good mood"]
    answer: 1
    explanation: "Song lyrics or poems published before 1929 have expired copyright protection, so Claude can provide them."
lang: en
ref: 2026-09-06-Claudes-new-system-prompt-doesnt-want-to-reproduce-song-lyrics
audio: 2026-09-06-Claudes-new-system-prompt-doesnt-want-to-reproduce-song-lyrics.en.mp3
industry: creative
---

Imagine this. You really liked an upbeat pop song you heard in the car on your way home from work today, so you asked your AI assistant, Claude, "Can you tell me the lyrics to the song I just heard?" In the past, the AI would have just written them out for you, but now you might hear a response like, "I'm sorry, I cannot provide that content due to copyright protection policies."

Recently, the AI model developed by Anthropic, 'Claude Fable 5.1,' has updated its system prompt (the basic instructions the AI follows when generating responses). In short, the core of this update is a strong determination "not to copy copyrighted material as-is."

### Why is this important?

In our daily lives, we have already become accustomed to using AI as a tool to find song lyrics, create pretty logos, or ask it to draw specific characters. However, the situation has changed recently as major record labels like Sony Music Publishing and Warner Chappell have filed copyright infringement lawsuits against AI companies. [Source 5](https://clauding.de/en/posts/claude-fable-5-1-systemprompt-songtexte), [Source 8](https://ai-tldr.dev/releases/simonw-claude-system-prompt-lyrics-sep2/)

This measure is a response to avoid legal and ethical responsibilities regarding AI unauthorized training on human creative works and reproducing them. This will be an important case study showing how AI services will coexist with copyright holders in the future. [Source 4](https://aiweekly.co/alerts/claude-system-prompt-bans-lyrics-after-sony-warner-sue)

### Simple Explanation

We can compare Claude's new system prompt to a 'photo filter app' we commonly use. While the AI used to draw photos very precisely, it now has very strict rules: "mimic the art style of a famous painter, but do not draw the painter's original work exactly as it is."

Shall we use an easier analogy?
*   **Song lyrics**: It is like prohibiting copying the sheet music of a famous singer's song. It blocks the act of copying not just a line or two, but the chorus or the core lyrics in their entirety. [Source 1](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/)
*   **Visual art**: Regarding requests to draw famous logos or characters, Claude judges that simply changing the style is not enough. Because characters are protected by copyright themselves, even if you change the color of their clothes or draw a different background, it will be refused if it reproduces the 'original work.' [Source 9](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1)

This rule even applies to drawings that Claude creates using code (SVG, CSS, HTML, etc.). Claude no longer draws famous characters or brand logos for you. [Source 9](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1), [Source 13](https://devblogs.co/posts/claudes-new-system-prompt-really-doesnt-want-to-reproduce-song-lyrics)

### Current Situation

Currently, this policy is being applied to users of Claude's website (claude.ai) and mobile app. However, it does not refuse all requests. Song lyrics, poems, and literary works published before 1929 can still be requested freely as before because their copyright protection period has expired. [Source 9](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1)

An interesting point is that even when Claude is not sure whether a work is within its copyright protection period, it refuses to answer, saying it "is not sure." The AI is taking a 'conservative' stance, choosing to err on the side of caution. Also, this policy is aimed at general users and is said not to apply to the API used by developers. [Source 8](https://ai-tldr.dev/releases/simonw-claude-system-prompt-lyrics-sep2/), [Source 9](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1)

### What will happen in the future?

Moving forward, AI services will find a more precise balance between 'creativity' and 'respecting copyright.' Users may need to adjust their prompts to draw out the AI's unique creativity, such as "create a poem with a similar emotional tone to this song," rather than asking the AI to "write the lyrics to this specific song." AI is in the process of evolving from a clever copying tool into a true partner that helps human creativity.

## References

1. [Claude’s new system prompt really doesn’t want to reproduce song lyrics](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/)
2. [Anthropic Publishes Claude Fable 5.1 System Prompt With Song](https://letsdatascience.com/news/anthropic-publishes-claude-fable-51-system-prompt-with-song-2a1114b5)
3. [Claude system prompt bans lyrics after Sony, Warner sue](https://aiweekly.co/alerts/claude-system-prompt-bans-lyrics-after-sony-warner-sue)
4. [Claude's New System Prompt Really Doesn't Want to Reproduce ...](https://clauding.de/en/posts/claude-fable-5-1-systemprompt-songtexte)
5. [Claude's new system prompt - sippey.com](https://sippey.com/2026/09/02/claudes-new-system-prompt.html)
6. [Simon Willison — Claude's new system prompt… | AI/TLDR](https://ai-tldr.dev/releases/simonw-claude-system-prompt-lyrics-sep2/)
7. [Claude Fable 5.1 system prompts - Claude Platform Docs](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1)
8. [Claude'snewsystempromptreallydoesn'twanttoreproduce...](https://devblogs.co/posts/claudes-new-system-prompt-really-doesnt-want-to-reproduce-song-lyrics)