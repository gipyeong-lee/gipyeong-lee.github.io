---
layout: post
title: "Did You Say 90% Cost Reduction by Giving 'Errands' to Your AI Coding Assistant?"
description: "Learn how to drastically reduce token costs for AI coding agents through 'Portal,' a technology released by Spotify."
summary: "Spotify has reduced token usage by 90% by leveraging the open-source 'Portal' technology and AiKA mode to delegate repetitive, simple tasks to lower-cost models."
tags: [AI, Coding, Spotify, Cost Reduction, Efficiency]
image: 2026-09-05-Portal-by-Spotify-cut-my-Claude-Code-token-usage-by-90.jpg
image_alt: "An image conceptualizing a data flow that finds efficient paths between coding agents and codebases"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "It is inefficient to assign simple tasks that do not require complex reasoning to top-tier AI models. This technology is a smart approach to optimizing the 'cost-effectiveness' of AI utilization."
quiz:
  - question: "What is the name of the core technology Spotify introduced to reduce AI coding agent costs?"
    choices: ["Claude Code", "Portal", "AiKA"]
    answer: 1
    explanation: "Spotify released 'Portal,' a knowledge graph layer positioned between AI coding agents and the codebase."
  - question: "What is the primary role of the 'code-writer' in Portal's AiKA mode?"
    choices: ["Analyzing the entire codebase", "Generating code based on existing patterns", "Updating user documentation"]
    answer: 1
    explanation: "The code-writer mode is responsible for tasks like generating repetitive code by following existing patterns."
  - question: "What is the token usage reduction rate achieved by delegating simple repetitive tasks to cheaper models?"
    choices: ["50%", "70%", "90%"]
    answer: 2
    explanation: "By routing repetitive, I/O-heavy tasks to lower-cost models like Gemini 2.5 Flash, they achieved a 90% reduction in token usage."
lang: en
ref: 2026-09-05-Portal-by-Spotify-cut-my-Claude-Code-token-usage-by-90
audio: 2026-09-05-Portal-by-Spotify-cut-my-Claude-Code-token-usage-by-90.en.mp3
industry: creative
---

Imagine you hired a brilliant PhD as a personal assistant. But what if you only had this PhD clicking the "copy" button on a copier or sorting papers into folders every morning? Even while paying them a PhD-level salary.

This is exactly the current state of "AI coding agents" that have become a hot topic among developers. We entrusted coding to AI with superior intelligence, but it was spending more on simple "errands" like reading and writing files rather than solving problems that require advanced logical reasoning. Here, "cost" refers to the "token" fees (the units used to count AI's computational consumption) paid every time the AI processes and understands sentences. To overcome this inefficiency, Spotify engineers have proposed a new solution.

## Why Does This Matter?

As AI technology grows rapidly, many developers are significantly increasing their productivity through AI coding agents like Claude Code. However, there is one fatal obstacle: "cost." The top-tier models, known as "frontier models," which these agents use to solve complex logical problems, are as expensive as they are powerful.

The problem is that this smart AI charges the same high rates even when it simply reads through files repeatedly or writes test code in the exact same format it has already written dozens of times. Spotify's case serves as an important turning point that goes beyond the "adoption" phase of AI, demonstrating **which grade of AI should be assigned to which task to be the most economical and efficient.** This offers a realistic path to drastically lowering operational costs while maintaining developer productivity [[Reference 1](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)].

## Easy Understanding: A 'Smart Traffic Station'

Spotify has released a technology called 'Portal' [[Reference 6](https://www.youtube.com/watch?v=TfZsMjB9PMo)]. Simply put, Portal is like a **'smart traffic station'** positioned between the AI agent and the code (codebase). Previously, AI would waste tokens by blindly searching through various parts of the codebase [[Reference 9](https://getpushtoprod.substack.com/p/how-to-reduce-90-of-claude-code-token)]. 

Spotify hired two special employees here called 'AiKA mode' to share the workload [[Reference 11](https://github.com/spotify/portal-ai-plugins)]. 

1. **bulk-reader**: When multiple files need to be analyzed, it assigns the task to the 'Gemini 2.5 Flash' model, which has decent performance but is very cheap, instead of using expensive AI [[Reference 2](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)]. 
2. **code-writer**: It similarly delegates the task of writing repetitive code following existing patterns to cheaper models [[Reference 2](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)]. 

By installing a plugin called 'shunt,' high-performance AI models focus strictly on "creative problem solving" that truly requires intelligence, while the remaining simple, repetitive labor is handled by the cheaper AiKA models [[Reference 4](https://www.linkedin.com/posts/spotify-for-backstage_portal-by-spotify-cut-my-claude-code-token-activity-7501610054891274241-y4Db), [Reference 11](https://github.com/spotify/portal-ai-plugins)]. 

## Current Situation

Many developers are already feeling the burden of the massive monthly token costs incurred while using AI agents [[Reference 12](https://www.youtube.com/watch?v=UslVzxAkiZ0)]. Spotify's experiment did not just remain a theory but resulted in an astonishing outcome: **reducing the token usage of coding agents by 90%** [[Reference 3](https://zeli.app/story/49571465), [Reference 14](https://news.ycombinator.com/item?id=49571465)]. 

This technology is now open-sourced and available for anyone to use, and it is actively being used to optimize tasks with high file I/O within the Claude Code environment [[Reference 6](https://www.youtube.com/watch?v=TfZsMjB9PMo), [Reference 11](https://github.com/spotify/portal-ai-plugins)]. 

## What Comes Next?

In the future, true competitiveness will go beyond asking "which AI is smarter" to "how to deploy which AI." Systems that manage the inside of complex systems as knowledge graphs (visualized relationships between data) and automatically distribute models based on the nature of the task, like Spotify's Portal, are expected to emerge in greater numbers.

Developers must now move beyond worrying about "how to instruct the AI" and start considering "how to design a structure that saves expensive AI and wisely utilizes cheaper AI." To use smart AI more wisely, it is now time for efficient "division of labor."

## MindTickleBytes AI Reporter Opinion
The success of AI utilization no longer depends on the performance of the model itself, but on the "art of operation" that manages the efficiency of the entire system. Spotify's case is the most exemplary answer key, showing how to lower costs and maximize productivity by efficiently deploying the best-performing AI.

## References
1. [Portal by Spotify cut my Claude Code token usage by 90%](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)
2. [Portal by Spotify cut my Claude Code token usage by 90%](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)
3. [Spotify's Portal cut my Claude Code · Hacker News | Zeli](https://zeli.app/story/49571465)
4. [Portal by Spotify cut my Claude Code token usage by 90% ...](https://www.linkedin.com/posts/spotify-for-backstage_portal-by-spotify-cut-my-claude-code-token-activity-7501610054891274241-y4Db)
5. [Spotify’s Backstage Portal cut my Claude Code… | VibeLeaderboard](https://www.vibeleaderboard.ai/intel/7ff05f2d-e1d9-4b86-aa58-8d94a5fccd5f)
6. [Spotify cut Claude Code token usage by 90% with Portal](https://www.youtube.com/watch?v=TfZsMjB9PMo)
9. [How to Reduce 90% of Claude Code Token Usage - by John Kim](https://getpushtoprod.substack.com/p/how-to-reduce-90-of-claude-code-token)
11. [GitHub - spotify/portal-ai-plugins · GitHub](https://github.com/spotify/portal-ai-plugins)
12. [How To Save 90% of Claude Code Token Usage - YouTube](https://www.youtube.com/watch?v=UslVzxAkiZ0)
14. [PortalbySpotifycutmyClaudeCodetokenusage... | HackerNews](https://news.ycombinator.com/item?id=49571465)