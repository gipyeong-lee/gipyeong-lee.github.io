---
layout: post
title: "Is My Coding History Public? Alert Regarding Claude Code's 'Session URL'"
description: "We examine concerns and mitigation strategies regarding the session URLs that Claude Code automatically appends to commit messages, which could potentially expose private information and confidential data."
summary: "The session URLs that Claude Code automatically inserts pose a risk of leaking conversation history, leading many users to demand that the feature be changed to opt-in."
tags: [AI, Coding, ClaudeCode, Security, Privacy]
image: 2026-08-30-Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default.jpg
image_alt: "A computer screen showing code commit history with a danger warning indicator next to it"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "While transparency in the development process is beneficial, having private conversations with an AI permanently documented alongside code is a serious security issue. Information protection must take precedence over feature convenience."
quiz:
  - question: "Why is the 'Session URL' that Claude Code adds to commit messages problematic?"
    choices: ["Because it slows down the code", "Because it can expose the entire conversation history", "Because it consumes too much storage space"]
    answer: 1
    explanation: "Because clicking that URL reveals the entire conversation with the AI, posing a risk that sensitive information could be leaked externally."
  - question: "Could you turn off the session URL using existing 'attribution.commit' settings?"
    choices: ["Yes, it was perfectly controllable", "No, session URLs were not subject to those controls", "It was partially possible"]
    answer: 1
    explanation: "Initially, many users pointed out that even 'attribution.commit' or 'attribution.pr' settings could not control the insertion of session URLs."
  - question: "What is the correct improvement the developer community is demanding of Anthropic?"
    choices: ["Complete removal of the session URL feature", "Changing the default to 'opt-in'", "Providing longer URLs"]
    answer: 1
    explanation: "They are consistently demanding that the default be changed to an 'opt-in' method so that users can selectively activate it only when needed."
lang: en
ref: 2026-08-30-Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default
audio: 2026-08-30-Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default.en.mp3
industry: creative
---

Imagine this: this morning, you worked closely with an AI coding assistant to write code for a highly confidential project. You even explicitly requested, "This part is company internal intellectual property, so it must never leak." However, what would happen if, a few days later, someone entered your repository and accidentally clicked the link attached next to your code? Through that link, the entire conversation you had with the AI would be displayed on their screen.

Recently, concerns have been growing among developers using the AI coding tool "Claude Code." It is being pointed out that a feature introduced for development convenience is becoming a gateway for unexpected security incidents.

### Why does this matter?

Most developers record their code in repository systems like Git. In doing so, Claude Code automatically appends a URL containing the phrase "Claude-Session" to the commit messages and the bodies of pull requests (PRs) after code is written [Source 1, Source 5].

On the surface, it looks like an attribution marker, saying, "I wrote this code with Claude Code." However, clicking this link reveals the **entire conversation history** from the time that code was created [Source 5]. This can include not just code, but also planning details for private projects, security discussions, or even internal company secrets. If this repository is publicly accessible, all of your thoughts and the development process are essentially exposed to the entire world [Source 5].

### Simplifying the issue: 'Scratchpad' and 'Post-it'

Let's use an analogy to make this problem easier to understand. If the code we write is the "final deliverable," then the conversation with the AI is "all the scribbles and deliberation marks" we wrote on a scratchpad to arrive at that result.

Claude Code is currently in a situation where, when submitting the deliverable, it takes everything written on the scratchpad, writes it on a Post-it note, and sticks it onto the deliverable [Source 6, Source 7]. The problem is that this Post-it note explicitly shows exactly who you were with and what kind of secrets you shared [Source 5].

The "attribution.commit" or "attribution.pr" settings used by developers in the past were simply for declaring, "This code was written by AI." However, these settings could not control the powerful data exposure feature known as the "Session URL" that was recently added [Source 3].

### Why are users anxious?

Many developers are currently voicing strong dissatisfaction regarding this issue [Source 1, Source 9]. In particular, when using Claude Code in a cloud environment, even if a developer changes Git settings on their local machine, there is no way to prevent the commit messages generated on the server, making the situation even more difficult [Source 2].

A flood of improvement requests is pouring into Anthropic (the developer of Claude) regarding this [Source 1, Source 11]. The core requirement is that **"it should not be included by default, and should be changed so that it can be added selectively only when the user wants it (opt-in)"** [Source 1, Source 8].

### What will happen in the future?

Technology enhances our productivity, but in the process, we must not lose "data sovereignty." It is highly likely that this feature will be improved from a mandatory default to a form that users can directly control, in response to requests from many users [Source 8, Source 11].

If you are currently using Claude Code, make sure to check the extent to which your history is exposed when creating commits or pull requests. A single carelessly shared link could turn all of your valuable ideas and secrets into public information [Source 5].

### MindTickleBytes' AI Reporter Perspective

"Convenience only has value within the fence of security. For an AI tool to become a developer's partner, it must prioritize the user's 'confidentiality' as the most basic indicator of trust. True productivity innovation can only be achieved when the tool's fundamental design guarantees the user's right to protect information first."

## References

1. [FEATURE] Session URL appended to commit messages and PR descriptions by default — should be opt-in · Issue #66504 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/66504)
2. attribution setting does not control session URL in commit messages · Issue #41873 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/41873)
3. Is the 'Claude-Session' URL That Claude Code Embeds in Commits Still in Your Repository? (https://zenn.dev/khasegawa/articles/985d970d6cc4a2?locale=en)
4. Stop Claude Code Session URLs From Landing in Your Public Git History (https://outofcontext.dev/blog/claude-code-session-url-attribution/)
5. [BUG] `attribution.sessionUrl` should default to `false` (opt-in) · Issue #76899 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/76899)
6. [Bug] Model leaks private session URL into git commits and PR bodies via Claude-Session trailer · Issue #72557 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/72557)
7. Claude Code Co-Author Commits: What It Is, How to Disable | explainx.ai Blog | explainx.ai (https://www.explainx.ai/blog/claude-code-commit-co-author-attribution-disable-guide-2026)
8. claude-code -(How to fix) Fix [FEATURE]SessionURLappended... (https://www.stepcodex.com/en/issue/feature-session-url-appended-to-commit)
9. ClaudeSessionURLappendedtocommitmessagesandPR... (https://news.ycombinator.com/item?id=49498201)
10. ClaudeSessionKey - Chrome Web Store (https://chromewebstore.google.com/detail/claude-session-key/ppofmhjkjfinjpidlidepeonimpjmadj)
11. How to fixClaudeCode hooks not firing or failing · 7752 Issues & Trend (https://claudeissues.com/topic/hooks-and-automation)
12. ClaudePrevious Response Still Running: Fix It Fast (https://www.digitbin.com/fix-claude-previous-response-still-running/)
13. ClaudeSwitched Models Mid-Conversation? | UsingClaude (https://usingclaude.com/en/guides/troubleshooting/claude-flagged-model-switching)
14. Claude (https://claude.com/)
15. FixClaudeCode "Please run /login" API Error 401 - SmartScope (https://smartscope.blog/en/generative-ai/claude/claude-code-401-auth-error-fix/)