---
layout: post
title: "AI Sees Everything on My Computer, What If the 'Feedback' Button Becomes My Diary?"
description: "Examining the personal data sharing issues and their implications during the feedback reporting process of Moonshot AI's desktop agent, Kimi Work."
summary: "It has been revealed that Moonshot AI's desktop AI agent, 'Kimi Work,' automatically transmits the last 5 conversation sessions when a user submits a feedback report, necessitating caution from users."
tags: [AI, Security, Kimi Work, Moonshot AI, Privacy]
image: 2026-08-17-Kimi-Work-attaches-raw-agent-sessions-to-feedback-reports.jpg
image_alt: "A graphic symbolizing the interface of the Kimi Work desktop application and security warnings."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Trust crumbles when convenience-oriented features operate without transparency. Developers must ensure users are clearly aware of what they are sharing."
quiz:
  - question: "What data does Kimi Work automatically attach when sending a feedback report?"
    choices: ["The last 5 agent sessions", "A list of all files on the computer", "The user's personal passwords"]
    answer: 0
    explanation: "When a user sends a feedback report, Kimi Work attaches the last 5 agent conversation sessions without separate notification."
  - question: "Which of the following is NOT a primary feature of Kimi Work?"
    choices: ["Reading local files", "Controlling web browsers", "Selling the user's entire web search history"]
    answer: 2
    explanation: "Kimi Work supports reading local files, controlling browsers, and executing scheduled tasks, but there is no information in the provided materials about it selling user search history."
  - question: "What is the 'scheduled task' feature of Kimi Work based on?"
    choices: ["cron (scheduler)", "Physical timer", "Random executor"]
    answer: 0
    explanation: "Kimi Work uses a cron-based scheduler to support automated tasks such as preparing morning briefings or running scripts overnight."
lang: en
ref: 2026-08-17-Kimi-Work-attaches-raw-agent-sessions-to-feedback-reports
audio: 2026-08-17-Kimi-Work-attaches-raw-agent-sessions-to-feedback-reports.en.mp3
industry: general
---

Imagine you have a smart assistant that perfectly supports your work. It tidies up your to-do list in the morning and handles your backlog of data analysis while you sleep. This assistant can even read documents on your computer directly and visit websites to fetch necessary information for you [Source 6]. Moonshot AI’s desktop AI agent, 'Kimi Work,' is exactly that kind of entity [Source 6].

But what if this assistant were secretly reading your diary and slipping its contents into a report sent to company headquarters? Recently, security experts discovered a somewhat shocking fact about how Kimi Work operates.

## Why Does This Matter?

AI agents have permission to access the deepest reaches of our computers. They have the ability to read local files, control web browsers, and even perform tasks autonomously at scheduled times [Source 6, Source 12]. While this maximizes work efficiency, it also comes with heavy security responsibilities.

When users experience an error and click the 'Send Feedback' button, they usually assume that only the situation they experienced or perhaps a screenshot is being shared. However, Kimi Work was transmitting the user's recent conversation contents as well without notice. This raises significant privacy concerns. Sensitive work materials or private conversations you’ve had with the AI could inadvertently flow into the developer's servers.

## Put Simply: An Analogy of the 'Assistant’s Report'

Let’s explain this situation with an everyday analogy. You tell your assistant, "I'm having trouble opening a file while working on today's report." You expect only the issue description to be relayed. However, when the assistant sends the report to headquarters, it also copies and attaches your entire diary from the last few days (the last 5 conversation sessions).

One can understand Moonshot AI’s intent to collect feedback data to improve user experience. But the core problem is that the process is not transparent. Users end up transmitting precious data without even knowing what they are sharing.

## Current Situation

Kimi Work is based on Moonshot AI’s powerful AI model, Kimi K2.6, and functions as a desktop agent where a swarm of about 300 sub-agents cooperate [Source 5, Source 6]. It supports both Windows and macOS and handles tasks while the user sleeps through a cron-based planning feature [Source 6, Source 12].

However, recent reverse engineering (a process of analyzing a software's internal structure and operating principles) revealed that when a user sends a feedback report, the application attaches data from the last 5 sessions without separate guidance [Source 1]. This is a prime example of user privacy being pushed to the back burner in the pursuit of technical convenience.

## What Happens Next?

AI technology is evolving to become more personalized and to demand more permissions. However, this is precisely why user trust is more important than ever. This issue serves as a major wake-up call regarding how AI developers handle user data and how transparently they disclose these practices.

If you use Kimi Work in the future, you should think twice before clicking the 'Feedback' button to check if any recent conversations contained sensitive information. Furthermore, users must more strongly demand the authority to personally set and control what data AI agents send and where.

## MindTickleBytes’ AI Reporter Perspective

Technical convenience often demands a price in the form of security. But that price should not be paid without the user's explicit prior consent. Wouldn't a truly 'smart AI' help the user control what they share themselves? User privacy should not be relegated to a sacrificial lamb for technological progress.

## References

1. [KimiWork attaches raw agent sessions to feedback reports](https://news.ycombinator.com/item?id=49313711)
2. [KimiWork](https://www.kimi.com/ru/help/kimi-work)
3. [KimiCode CLI: How to Install and Run Moonshot's Agentic Coding...](https://apidog.com/blog/kimi-code-cli/)
4. [GitHub - MoonshotAI/Kimi-K3: Open Frontier Intelligence · GitHub](https://github.com/MoonshotAI/Kimi-K3)
5. [KimiWork: Moonshot's Local AI Agent Guide | Lushbinary](https://lushbinary.com/blog/kimi-work-local-ai-agent-knowledge-workers-guide/)
6. [Moonshot AI's KimiWork Brings 300 AI Agents to Your... - Decrypt](https://decrypt.co/370954/moonshot-ai-kimi-work-300-agents-desktop)
7. [KimiK3 за $29: китайские тарифы, KimiCode... - YouTube](https://www.youtube.com/watch?v=vDp4SLNDHLs)
8. [Kimi API Platform](https://platform.kimi.ai/)
10. [GitHub - MoonshotAI/kimi-code: KimiCode CLI — The Starting Point...](https://github.com/MoonshotAI/kimi-code)
11. [KimiWork - Nowledge Mem Integration | Nowledge Mem](https://mem.nowledge.co/integrations/kimi-work)
12. [Вышел KimiWork — ИИ-агент, который работает без сна / Хабр](https://habr.com/ru/news/1045120/)