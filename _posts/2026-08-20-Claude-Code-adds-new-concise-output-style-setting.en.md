---
layout: post
title: "Stop Writing 'Essays' When Talking to AI! How to Use Claude Code's New 'Concise Mode'"
description: "Learn how to set up a concise response style in Claude Code so you can quickly see core results instead of long-winded AI explanations."
summary: "Starting with version 2.1.237, Claude Code introduces a 'Concise' output style, allowing you to boost developer productivity by forcing the AI to present results immediately without unnecessary explanations."
tags: [AI, ClaudeCode, DevTools, Tips]
image: 2026-08-20-Claude-Code-adds-new-concise-output-style-setting.jpg
image_alt: "Claude Code interface displaying only concise code results in the terminal."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Complex, essay-style responses are about to become a relic of the past. Conciseness that gets straight to the point is the most necessary virtue of an AI for developers."
quiz:
  - question: "In which version was Claude Code's 'Concise' mode first introduced?"
    choices: ["v2.0.0", "v2.1.237", "v2.5.0"]
    answer: 1
    explanation: "Claude Code's concise output style was first introduced in version 2.1.237."
  - question: "Which of the following is a correct way to enable concise mode?"
    choices: ["Using the /config command", "Simply saying 'Be concise'", "Reinstalling the terminal"]
    answer: 0
    explanation: "Concise mode can be set using the /config command or configured directly in the settings.json file."
  - question: "How does the AI respond when set to concise mode?"
    choices: ["It does not respond", "It presents results immediately and answers briefly", "It asks the question back"]
    answer: 1
    explanation: "In concise mode, the AI presents results immediately without an introduction or peripheral explanation and answers briefly."
lang: en
ref: 2026-08-20-Claude-Code-adds-new-concise-output-style-setting
audio: 2026-08-20-Claude-Code-adds-new-concise-output-style-setting.en.mp3
industry: general
---

Imagine this: You're close to a tight deadline and you ask an AI to fix a code snippet or verify an error, but it responds with a long-winded introduction and conclusion, just like a homework assignment check. "I've analyzed your request and considering..."—such polite answers can sometimes become "noise" that breaks your flow.

One of the biggest frustrations developers faced while using Claude Code was this "excessive verbosity." [Reference: How I use Claude Code](https://www.builder.io/blog/claude-code) Ever had a frustrating experience with an AI that felt like it was writing an essay when you simply asked it to fix an error? Fortunately, Anthropic has finally read the users' minds and provided a solution.

### Why is this important?

For us who use AI as an assistant, "time" is an asset. Polite greetings before the AI starts answering or long explanations before showing a code block are the main culprits behind decreasing the productivity of developers working in terminal environments.

With this update, Claude Code allows users to **directly control "how they interact with AI."** Much like a filter in a photo app that removes unnecessary color casts to show only the sharp results, you can now remove the filler from the AI's response and leave only the "essentials": the code and the results. Now, you can complete your work faster through immediate answers rather than the AI's long stories.

### Easy to understand: Think of it like this

To put it simply, this feature is like changing from a restaurant that forces a "menu reading" to a service that **quickly brings you only the food you ordered.**

Previously, when you asked the AI a question, it took time because it provided everything: "Appetizer (greeting) - Main Course (code) - Dessert (closing remark)." However, when you turn on 'Concise' mode, the AI skips even the "Here is your food" part and immediately brings out the code results you requested.

Of course, you can ask for detailed explanations anytime if needed. [Reference: How to use concise mode in Claude Code (Claude Code 2.1.237)](https://www.youtube.com/watch?v=lVKfDPcG_k8) The core intention is to **"see detailed explanations only when the user wants them,"** and consume only the most efficient information during normal tasks. This is similar to quickly finding the "one-line command" you need right now, rather than reading a 100-page manual.

### Current Status

The concise output style was officially introduced starting from **Claude Code version 2.1.237**. [Reference: Version 2.1.237 Release Info (Nerd's Chalk)](https://nerdschalk.com/i-switched-claude-code-to-concise-mode-in-seconds-the-desktop-app-wouldnt-take-it/) Therefore, you must first check your version to use this feature.

Setting it up is very simple. You can change the "Output style" menu by typing the `/config` command in the terminal, or by directly adding `"outputStyle": "Concise"` to the `settings.json` configuration file. [Reference: Using Claude Code's Concise Mode (Vibecoding)](https://vibecoding.ru/news/2026/08/20/claude-code-concise-output-style)

One thing to note is that there have been reports of the user's settings occasionally reverting back to the default if the conversation becomes too long. [Reference: GitHub Issue (Claude Code)](https://github.com/anthropics/claude-code/issues/77136) This is something developers are continuously improving, and you may need to check occasionally to ensure your settings are properly maintained for perfect immersion.

### What's next?

Going beyond a simple "concise mode," we are moving toward an era where users can more finely adjust the AI's tone and the density of its responses. Claude Code already possesses excellent codebase awareness and terminal control capabilities. [Reference: Claude's Coding Solutions](https://claude.com/solutions/coding) If it becomes possible to perfectly customize the experience to the user's preferences on top of this, AI will feel not like a simple tool, but like a "digital twin" that has fully absorbed your development style.

Update your terminal right now and meet refreshing, straightforward results instead of unnecessary explanations. Your development speed will reach a whole new level starting today.

### MindTickleBytes AI Reporter's Take

As technology advances, we often demand "more" from AI. However, this update proves that sometimes the role of the smartest AI is not to "speak more," but to "show exactly only what is necessary." True kindness comes from the conciseness that saves the other person's time.

## References

1. [I Switched Claude Code to Concise Mode in Seconds](https://nerdschalk.com/i-switched-claude-code-to-concise-mode-in-seconds-the-desktop-app-wouldnt-take-it/)
2. [Make Claude Code give you answers, not essays](https://lilys.ai/en/notes/claude-code-20251031/make-claude-code-answers-not-essays)
3. [Getting More Out of Claude Code: Prompting and Token Economy](https://franktheprogrammer.com/articles/getting-more-out-of-claude-code/)
4. [Claude Code 2.1.237 — лаконичный режим без лишних...](https://www.youtube.com/watch?v=lVKfDPcG_k8)
5. [Ensure user-set style instructions persist across a conversation](https://github.com/anthropics/claude-code/issues/77136)
6. [How I use Claude Code (+ my best tips)](https://www.builder.io/blog/claude-code)
7. [Claude Code отвечает результатом, а не рассказом](https://vibecoding.ru/news/2026/08/20/claude-code-concise-output-style)
8. [Claude Code Usage 70: Output Style](https://daker.ai/community/claude-code-usage-70-output-style-format-tone)
9. [Coding with Claude by Anthropic](https://claude.com/solutions/coding)