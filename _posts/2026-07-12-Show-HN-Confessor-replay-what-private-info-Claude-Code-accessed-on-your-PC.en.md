---
layout: post
title: "Secrets of My Computer: How Much Has AI Seen? How to Verify with 'Confessor'"
description: "Introducing 'Confessor,' a tool that lets you review which information on your computer has been accessed by the AI coding agent 'Claude Code,' and a look at the associated security issues."
summary: "Confessor has emerged as a tool that allows you to transparently verify which files and information your AI coding agent has read on your PC."
tags: [AI, Security, ClaudeCode, Privacy, Confessor]
image: 2026-07-12-Show-HN-Confessor-replay-what-private-info-Claude-Code-accessed-on-your-pc.jpg
image_alt: "A user reviewing the activity log of an AI coding agent on their computer screen"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "The convenience of AI agents comes with the risk of powerful system permissions. It is not an option but a necessity for users to transparently verify access logs themselves."
quiz:
  - question: "What is the main function of Confessor?"
    choices: ["It reconstructs (replays) and displays what information the AI accessed on your computer", "It automatically encrypts all files on the computer", "It doubles the response speed of the AI agent"]
    answer: 0
    explanation: "Confessor allows users to re-verify the records of personal information accessed by AI agents like Claude Code on their PC."
  - question: "What did Anthropic claim regarding the 'hidden tracker' discovered in Claude Code that caused controversy?"
    choices: ["They claimed it was the work of hackers", "They stated it was an essential feature for security", "They revealed it was part of an 'experiment'"]
    answer: 2
    explanation: "Anthropic previously explained that the hidden tracker within Claude Code was simply an 'experiment'."
  - question: "What is the core of the security vulnerability related to AI coding agents?"
    choices: ["The AI model itself is too smart", "The fact that AI can authenticate and execute actions on its own without human session involvement", "The computer is too old"]
    answer: 1
    explanation: "The core security vulnerability is pointed out to be the fact that AI agents can authenticate and execute tasks on external systems without the user's direct manipulation (session)."
lang: en
ref: 2026-07-12-Show-HN-Confessor-replay-what-private-info-Claude-Code-accessed-on-your-pc
audio: 2026-07-12-Show-HN-Confessor-replay-what-private-info-Claude-Code-accessed-on-your-PC.en.mp3
industry: security
---

Imagine this: you ask your AI assistant, "Please clean up the code in my project folder." The AI finishes the task in an instant, but suddenly you wonder: "While cleaning up my folder, did this AI secretly snoop on the passwords or other sensitive files I have saved?"

Recently, the system access permissions of the AI coding tool 'Claude Code' have become a hot topic among developers. This is because AI tools like Claude Code are deeply involved in terminals, file systems, and code repositories. To alleviate this anxiety, a tool called 'Confessor' has emerged, which transparently shows what the AI did on your computer.

## Why is this important?

When we grant powerful permissions to AI tools for the sake of convenience, risks lurk in the background. What if the AI is accessing data that you didn't intend for it to reach, or transmitting data to unknown locations?

Recent research has confirmed the risk that these AI coding agents (AI that performs tasks on its own based on user instructions) can authenticate and execute tasks on systems even without the user directly acting at the computer ([VentureBeat](https://venturebeat.com/security/six-exploits-broke-ai-coding-agents-iam-never-saw-them)). This means that your computer could be connected to external systems by the AI without your knowledge.

## Easy to understand

Think of 'Confessor' as a sort of **'CCTV time machine.'** Just as we rewind to watch a specific scene while watching a movie, Confessor replays the activity logs performed by Claude Code on your computer ([Hacker News](https://news.ycombinator.com/item?id=48877650)).

To use an analogy, let's say the AI agent is a 'housekeeper' who comes to your home to clean. You give that housekeeper keys to clean the living room and the kitchen. But if you have no way of knowing if the housekeeper lingered near the safe in your study or if they only did their cleaning before leaving, you would be anxious. Confessor acts as a 'transparent log' that shows the footsteps, revealing one by one whether the housekeeper was near the safe or whether they tried to open a drawer while cleaning.

## Current situation

The privacy issues surrounding Claude Code have recently been quite serious. In April, a developer discovered a 'hidden tracker' in the Claude Code client that could encode and send data externally ([Malwarebytes](https://www.malwarebytes.com/blog/news/2026/07/claude-codes-hidden-tracker-was-an-experiment-says-anthropic)). Although Anthropic explained that this tracker was just an 'experiment,' user anxiety has not completely vanished.

To make matters worse, in April, a map file containing about 512,000 lines of Claude Code CLI (command-line interface) source code was exposed, leading to an incident where the entire source code was leaked ([Reddit](https://www.reddit.com/r/privacy/comments/1sbvd3j/claude_code_source_leak_reveals_how_much_info/)). In this situation, a tool like Confessor, which allows you to check what the AI is 'seeing,' will be a very valuable option for users who value security.

## What will happen in the future?

As AI agents become smarter and handle more tasks, security will become an even more critical issue. Moving forward, it appears that only 'AI that transparently discloses user logs and guarantees privacy,' going beyond just 'AI with good features,' will be able to gain user trust. The era where we take care of our own security sovereignty while using AI has arrived.

### MindTickleBytes' AI Reporter's View
You always need to be vigilant when entrusting the 'keys' to your computer to an AI agent. The lesson that Anthropic's 'experiment' gave us is clear: technology is advancing, but the protection of your information is entirely up to you, the user. A tool like Confessor will be an essential first step to protecting your precious information.

## References
1. [ShowHN:Confessor–replaywhatprivateinfoClaudeCode...](https://news.ycombinator.com/item?id=48877650)
2. [r/privacy on Reddit: Claude Code source leak reveals how much info Anthropic can hoover up about you and your system](https://www.reddit.com/r/privacy/comments/1sbvd3j/claude_code_source_leak_reveals_how_much_info/)
3. [Claude Code’s hidden tracker was an “experiment,” says Anthropic | Malwarebytes](https://www.malwarebytes.com/blog/news/2026/07/claude-codes-hidden-tracker-was-an-experiment-says-anthropic)
4. [Claude Code, Copilot and Codex all got hacked. Every attacker went for the credential, not the model. | VentureBeat](https://venturebeat.com/security/six-exploits-broke-ai-coding-agents-iam-never-saw-them)