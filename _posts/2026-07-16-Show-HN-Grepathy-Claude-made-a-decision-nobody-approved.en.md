---
layout: post
title: "AI changed code without my permission? Meet Grepathy, the smart tool that records 'why'"
description: "Discover Grepathy, a tool that allows you to transparently track the reasoning behind decisions made by your AI agents when they modify code."
summary: "Introducing Grepathy, a tool that records and saves the rationale behind AI decisions to prevent the loss of critical work history."
tags: [AI, Claude, Grepathy, DevTools, Transparency]
image: 2026-07-16-Show-HN-Grepathy-Claude-made-a-decision-nobody-approved.jpg
image_alt: "An illustration of how Grepathy works to document and save AI-made decisions into a code repository."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "As AI autonomy increases, transparency in tracking the basis of its decisions is no longer optional—it is essential. Grepathy provides a practical way to achieve the 'explainability' developers need to coexist with AI."
quiz:
  - question: "What is the primary reason Grepathy was developed?"
    choices: ["To increase AI speed", "To record the rationale behind AI decisions and prevent history loss", "To automatically fix AI errors"]
    answer: 1
    explanation: "Grepathy was created to solve the problem of disappearing history by storing the reasons for decisions made by AI agents in a local repository."
  - question: "What kind of data does Grepathy store?"
    choices: ["All conversation content with the user", "Selectively stores only the decisions (reasoning) made by the AI", "A list of all files on the computer"]
    answer: 1
    explanation: "Grepathy selectively stores only the reasoning information behind AI decisions in Markdown format, rather than the entire conversation."
  - question: "How is Grepathy executed?"
    choices: ["Users must execute it manually every time", "It always runs in the background", "It is executed automatically via Git hooks"]
    answer: 2
    explanation: "Grepathy runs automatically during the workflow via Git hooks, so users do not need to execute it manually."
lang: en
ref: 2026-07-16-Show-HN-Grepathy-Claude-made-a-decision-nobody-approved
audio: 2026-07-16-Show-HN-Grepathy-Claude-made-a-decision-nobody-approved.en.mp3
industry: legal
---

Imagine this: On a busy morning, you ask your smart AI coding agent, "Please clean up the code for this project," and then head into a meeting. When you return in the evening to check the code, you're shocked! The AI has even modified core logic you thought should never be touched. You try to look for the reason, "Why on earth did it make this decision?" but the AI tool has already deleted all the work history from a few days ago. [Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537)

This situation is no longer a thing of the distant future. The "era of agents"—where AI modifies code and makes decisions on its own—has arrived among developers, but instances of developers being troubled by the disappearing "reasons" behind these outcomes are becoming more frequent. **Grepathy**, which we are introducing today, was created precisely to capture these "disappearing reasons."

### Why is this important?

As AI moves beyond simply providing answers to acting as an "agent" (AI that autonomously performs specific goals) that writes code and modifies files, **"accountability" and "traceability"** have become extremely important. [Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537)

Many AI tools—specifically services like Claude Code (a tool where AI directly modifies and executes code in the development environment)—default to deleting work history (transcripts) after a certain period (30 days). [Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537) While this might be efficient in terms of privacy or storage space, it can be fatal for a developer who later needs to answer the question, "Why did the AI change this code this way?" Grepathy helps anyone verify those reasons later by recording the rationale behind decisions made by the AI itself.

### Easy to Understand: How to Keep an 'Activity Log' for AI

Think of it this way: There is a new team member (AI) on your project who is very smart but has a poor memory. This person is great at their job, but after 30 days, they forget why they made certain decisions. Grepathy is like a **secretary taking down this new employee's 'decision log.'**

1. **Intelligent Selective Recording**: Grepathy does not store all private conversations between the user and the AI. It purifies only the reasoning behind the decisions the AI made. [Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537)
2. **Direct Storage in the Code Repository**: Recorded decisions are converted into Markdown documents and permanently stored in the repository alongside your code. [Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537)
3. **Automation**: The user doesn't need to bother typing commands. Through Git hooks (scripts that run automatically when specific events occur), Grepathy operates on its own every time you commit or push code. [GitHub - evansjp/grepathy](https://github.com/evansjp/grepathy)

Simply put, you can see the "answers to why" left by the AI at a glance just by running a specific command within your project folder. [GitHub - evansjp/grepathy](https://github.com/evansjp/grepathy)

### Current Situation: Working with AI

AI coding tools are evolving day by day. Tools like Claude Code adopt a "human-on-the-loop" approach where humans make the final confirmation by default, but with the introduction of Auto mode, they have come to handle more tasks on their own without direct human intervention. [Claude Code Defaults to Human Approval: Auto Mode Requires Explicit Opt-In](https://www.techtimes.com/articles/319874/20260707/claude-code-defaults-human-approval-auto-mode-requires-explicit-opt.htm)

However, as technology advances, the issue of transparency in trusting and managing AI judgments is growing. Examples of AI creating false information or distorting facts are being shared among developers, [How to Stop Claude From Making $#it Up](https://medium.com/@brentwpeterson/how-to-stop-claude-from-making-it-up-921a6a9238c8) and companies are also wary of the fact that AI agent decisions can lead to unexpected results. [The Day an AI Agent Commits Your Company to a Decision Nobody ...](https://www.linkedin.com/posts/bhaviavelayudhan_the-day-an-ai-agent-commits-your-company-activity-7436671325772898305-TdKd)

### What Will Happen Next?

Attempts like Grepathy will become even more important in the future. As AI grows beyond the level of simply writing code and becomes an entity that makes decisions regarding the direction of a project, leaving a record of the rationale will become a legally and ethically necessary procedure.

Why not check the "reasons" for your AI agent's decisions using Grepathy the next time it modifies your code tomorrow morning? It might be the first step toward transparent communication between AI and humans.

## References
1. [Show HN: Grepathy – Claude made a decision nobody approved | Hacker News](https://news.ycombinator.com/item?id=48920537)
2. [GitHub - evansjp/grepathy: Your agent writes down why, in the repo, so everyone else's agents can find it without asking you. · GitHub](https://github.com/evansjp/grepathy)
3. [Claude Code Defaults to Human Approval: Auto Mode Requires Explicit Opt-In](https://www.techtimes.com/articles/319874/20260707/claude-code-defaults-human-approval-auto-mode-requires-explicit-opt.htm)
4. [How to Stop Claude From Making $#it Up | by Brent W. Peterson | May, 2026 | Medium](https://medium.com/@brentwpeterson/how-to-stop-claude-from-making-it-up-921a6a9238c8)
5. [The Day an AI Agent Commits Your Company to a Decision Nobody ...](https://www.linkedin.com/posts/bhaviavelayudhan_the-day-an-ai-agent-commits-your-company-activity-7436671325772898305-TdKd)