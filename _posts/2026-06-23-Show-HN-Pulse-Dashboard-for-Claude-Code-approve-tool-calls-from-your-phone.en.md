---
layout: post
title: "Approving AI decisions even away from my computer? 'Pulse', a real-time dashboard for Claude Code"
description: "You no longer need to keep an eye on your terminal while using Claude Code. Now, check AI actions in real-time and approve tool usage from your smartphone."
summary: "Introducing 'Pulse', a local dashboard application that allows you to monitor Claude Code terminal sessions in real-time and approve tool usage via your smartphone."
tags: [AI, ClaudeCode, Productivity, Tool, Mobile]
image: 2026-06-23-Show-HN-Pulse-Dashboard-for-Claude-Code-approve-tool-calls-from-your-phone.jpg
image_alt: "A view of the Claude Code terminal activity displayed in real-time on a smartphone screen, with buttons appearing to approve tool usage"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Connecting complex AI development environments to mobile devices to secure user control is impressive. Mobility will become increasingly important for interactions with AI agents."
quiz:
  - question: "Which of the following is not a key feature of the Pulse dashboard?"
    choices: ["Real-time session monitoring", "Tool usage approval via mobile device", "All conversation history is permanently stored in the cloud"]
    answer: 2
    explanation: "Pulse is designed on the principle that data does not leave the user's computer (locally)."
  - question: "What is the primary benefit of using Pulse?"
    choices: ["You can check the context of AI tasks and interact even while away from your computer", "You can completely remove AI's tool usage permissions", "You can use all features of Claude Code for free"]
    answer: 0
    explanation: "Pulse increases mobility by allowing you to answer AI questions or approve tool usage directly from mobile via notifications."
  - question: "What is the data security method for the Pulse application?"
    choices: ["All data is sent to external servers", "It runs in a local environment so data does not leave the device", "Uses OAuth tokens to authenticate with an external server every time"]
    answer: 1
    explanation: "Pulse runs locally without separate dependencies and emphasizes security by ensuring user data does not leave the device."
lang: en
ref: 2026-06-23-Show-HN-Pulse-Dashboard-for-Claude-Code-approve-tool-calls-from-your-phone
audio: 2026-06-23-Show-HN-Pulse-Dashboard-for-Claude-Code-approve-tool-calls-from-your-phone.en.mp3
industry: creative
---

Imagine this: You're at a coffee shop, and you've tasked an AI agent with a complex coding job on your laptop before stepping away for a moment. What would happen if the AI attempted to delete an important file or call an external API at that exact moment? Usually, you would have to sit in front of the terminal screen to hit "approve" for the task to proceed, but now, you don't have to.

In the era of working with AI, we need a way to check in real-time whether the AI is making the right decisions and maintain control, even when we aren't tethered to our screens. This tool, 'Pulse', was born out of that necessity.

## Why is this important?

AI agents like Claude Code have extensive permissions, ranging from writing code to modifying files. To utilize them safely, users must monitor and approve every action the AI takes, which can be quite exhausting.

Pulse liberates users from these constraints. [Pulse](https://github.com/nikitadoudikov/claude-pulse) allows you to check AI tasks in real-time on your smartphone and approve tool usage directly when necessary, securing both mobility and control over AI tasks. This provides an essential environment for modern technology users who want to verify that their AI is operating safely under their control from anywhere, going beyond mere convenience.

## Easy to understand: 'AI-dedicated CCTV and remote control'

You can easily think of Pulse as an **'AI-dedicated CCTV and remote control'**.

It follows the same principle as unlocking a door lock or checking on a pet with your smartphone while you're away from home. [Pulse](https://news.ycombinator.com/item?id=48612844) acts as CCTV, showing you in detail what the AI agent is currently doing in the terminal and how much it is costing. And it becomes a remote control that lets you approve tool usage via smartphone notifications when the AI attempts important tasks like file modifications or external connections, even when you aren't at your desk.

Simply put, whereas previously the AI would ask in the terminal window, "Can I modify this file?", and you would have to answer directly, using Pulse is akin to the AI messaging you on your smartphone, "Can I perform this task now?", and you tapping the 'Approve' button immediately. Through the [Claude Code Notifier Companion](https://apps.apple.com/us/app/claude-code-notifier-companion/id6757701908) app, users can answer AI questions or decide on tool usage without ever touching their Mac directly.

## Current status

Currently, tools like [Pulse](https://github.com/nikitadoudikov/claude-pulse) support the following features:

*   **Real-time monitoring:** Shows what the AI is currently doing and how much it is costing. [Source 2](https://github.com/hyeongjun-dev/claude-pulse)
*   **Remote approval:** Allows you to approve tool usage or answer questions via notifications without looking at the terminal. [Source 4](https://apps.apple.com/us/app/claude-code-notifier-companion/id6757701908)
*   **Privacy protection:** These applications are designed to run locally, without complex separate dependencies, ensuring that data does not leak outside the device. [Source 1](https://github.com/nikitadoudikov/claude-pulse)

However, this is not the same as the AI having the ability to judge for itself. Users must still determine if the decisions the AI is making are correct; it is important to recognize that not all tasks are handled automatically. Also, certain advanced features may have different settings depending on the service model. [Source 3](https://github.com/NoobyGains/claude-pulse)

## What's next?

In the future, AI agents will perform more complex tasks autonomously. Accordingly, the importance of tools that transparently visualize AI behavior and control it remotely, like Pulse, will continue to grow. While the current focus is on coding tasks, this method of managing AI behavior via smartphone is likely to become standard for general office tasks and daily management duties as well. Users will increasingly transform from 'supervisors sitting in front of a screen' into 'commanders directing AI from anywhere, at any time.'

## MindTickleBytes' AI Reporter perspective

While it is innovative for AI to use tools, it is dangerous for them to operate outside of user control. Pulse has found a very sophisticated balance that maintains security without hindering user productivity. As we get closer to AI, those brief moments where we personally press the 'approve' button will become even more critical.

## References

1. [GitHub - nikitadoudikov/claude-pulse: Local, zero-dependency dashboard for Claude Code](https://github.com/nikitadoudikov/claude-pulse)
2. [GitHub - hyeongjun-dev/claude-pulse: Real-time session dashboard for Claude Code](https://github.com/hyeongjun-dev/claude-pulse)
3. [GitHub - NoobyGains/claude-pulse: Real-time usage monitor for Claude Code](https://github.com/NoobyGains/claude-pulse)
4. [Claude Code Notifier Companion - Apple App Store](https://apps.apple.com/us/app/claude-code-notifier-companion/id6757701908)
5. [ShowHN: Pulse – Dashboard for Claude Code, approve tool calls...](https://news.ycombinator.com/item?id=48612844)