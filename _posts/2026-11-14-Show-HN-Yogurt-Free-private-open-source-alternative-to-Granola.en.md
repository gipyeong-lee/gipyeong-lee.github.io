---
layout: post
title: "No More Surveillance Bots in Every Meeting: 'Yogurt', the Privacy-First Open-Source Meeting Notes App"
description: "Introducing Yogurt, a free open-source meeting notes app that runs securely on your computer without secret bots sneaking into Zoom, Google Meet, or Teams meetings."
summary: "As an alternative to traditional AI meeting note services where unfamiliar bots make participants feel watched, 'Yogurt'—an open-source desktop app that securely transcribes and summarizes audio locally on your computer—is gaining attention."
tags: [Yogurt, Granola, AIMeetingNotes, OpenSource, Privacy, OnDeviceAI]
image: 2026-11-14-Show-HN-Yogurt-Free-private-open-source-alternative-to-Granola.jpg
image_alt: "An illustration depicting the Yogurt app interface in front of a computer screen, symbolizing meeting notes being securely processed locally."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Armed with privacy and an open-source philosophy in a meeting notes market dominated by cloud services, Yogurt will be a welcome turning point for both developers and privacy-conscious users."
quiz:
  - question: "What is the biggest feature that sets Yogurt apart from many traditional meeting recording tools?"
    choices: ["It records locally in the background without AI bots directly joining the meeting", "You must have a paid subscription to export transcripts", "It will not run at all without an internet connection"]
    answer: 0
    explanation: "Yogurt protects your privacy by recording audio directly in the background of your computer rather than entering meetings as a bot on Zoom, Google Meet, or Teams."
  - question: "Where are the meeting recordings and summaries generated in the Yogurt app stored?"
    choices: ["The developer's cloud server", "Inside the user's computer", "An open-source public database"]
    answer: 1
    explanation: "Yogurt is designed so that all meeting recordings, transcripts, and summaries never leak outside your computer and remain solely on your local device."
  - question: "Under what license is Yogurt distributed as an open-source project?"
    choices: ["GPL v3", "MIT License", "Commercial Proprietary License"]
    answer: 1
    explanation: "Yogurt is a free and open-source desktop application based on the MIT license, developed by Eric."
lang: en
ref: 2026-11-14-Show-HN-Yogurt-Free-private-open-source-alternative-to-Granola
audio: 2026-11-14-Show-HN-Yogurt-Free-private-open-source-alternative-to-Granola.en.mp3
industry: creative
---

Imagine this: an important internal meeting or client meeting is about to start, and an unfamiliar "AI Bot" takes up prominent space in the corner of the meeting screen. Participants feel an inexplicable tension and cannot shake off the nagging anxiety: "Will this conversation be stored wholesale in some cloud server and later used for ad targeting or model training?"

While many AI meeting assistant tools we use daily provide convenience, they transmit our precious conversations to external clouds and sometimes force paid subscriptions. Services like Granola, which have recently gained popularity, are wonderful, but they have limitations such as restricting full export features to paid plans or managing data with encryption constraints [Source 13]. Metaphorically speaking, it's like keeping a diary while feeling the frustration of a stranger peeking over your shoulder to read and censor every entry.

To fundamentally resolve this frustration, a fresh open-source project has emerged: **Yogurt**. Introduced to the world via Hacker News Show HN, Yogurt is a free, open-source meeting notes app that operates securely entirely within your computer without sending bots into video conferences on Zoom, Google Meet, or Teams [Source 1, Source 8].

---

## Why Is This Important?

For modern office workers, freelancers, and remote workers, meetings take up a significant portion of the day. AI tools that record and summarize meeting contents have become essentials, but they have always carried the tag of "privacy infringement." Storing sensitive business ideas, private conversations, or internal confidential information on third-party cloud servers is like carrying a ticking time bomb of potential security incidents.

Yogurt solves this problem from its roots. Based on the philosophy that **"my meeting notes should exist only on my computer,"** it is designed so that meeting recordings, transcripts, and AI summaries are never leaked to external servers even once [Source 1]. Developer Eric focused on the fact that by leveraging smaller, more powerful on-device AI models, you can maximize hardware performance and create excellent meeting notes without relying on expensive paid cloud services [Source 1].

Furthermore, released as fully open-source (MIT License), its code can be transparently audited, and anyone can freely download and use it without subscription fee worries [Source 1, Source 8]. This acts as a massive attraction point for both cost-sensitive individual users and corporate environments requiring strict security. You no longer need to pay expensive monthly subscription fees and have your features restricted.

---

## Easy to Understand: How Does Yogurt Work?

Simply put, Yogurt is like **"a personal assistant working quietly inside your computer."** 

If traditional meeting recording bots are external observers who burst through the conference room door shouting "Hello, recording started," making participants tense, Yogurt is like a sophisticated recorder quietly sitting in the corner of the meeting room, leaving notes whispered solely in your notebook.

Here is a step-by-step look at how Yogurt works:

1. **Bot-free background recording**: When starting a Zoom, Google Meet, or Teams meeting, Yogurt does not enter the meeting room with a bot account [Source 1, Source 2]. Instead, it quietly records by detecting your computer's audio system in the background. Other participants won't even know you're running a meeting notes app.
2. **Real-time transcription and summarization**: As the meeting progresses, conversations are transcribed into text and displayed on your screen in real time [Source 2]. Once the meeting ends, the on-device AI model immediately summarizes key points and neatly organizes action items decided in the meeting, to-dos per attendee, and personal notes [Source 2, Source 8].
3. **Local data retention**: All generated data is stored securely on the user's hard drive without being transmitted to the external cloud [Source 1]. 
4. **Local MCP server integration**: If you want to have meeting notes analyzed by frontier AI models with even greater capabilities (e.g., Anthropic's Claude, OpenAI, etc.), you can choose and connect them directly via the local MCP (Model Context Protocol) server provided by Yogurt [Source 1]. There is no need to rely on paid cloud services acting as middlemen [Source 1].

This is like taking photos and storing them in your smartphone's default gallery instead of unconditionally uploading them to the cloud, sharing them only where you want when needed. Control over technology returns entirely to the user rather than the service provider.

---

## Current Status: Where Is It Now and What Features Does It Have?

Yogurt has been developed as a cross-platform desktop app supporting Windows, Mac, and Linux [Source 1, Source 5]. From the early stages of development, effort was poured into UI interactions, animations, and hardware performance optimization to deliver a smooth and fast user experience [Source 1].

The recently released v0.3.6 version added automatic updates and version check settings, plus delicate convenience features such as automatically unmounting (ejecting) the disk image (DMG) after installation in macOS environments [Source 11]. It demonstrates a high level of polish, allowing you to sync with your calendar and immediately import meeting schedules without creating an account or going through separate complex linking processes [Source 1].

Among open-source communities and tech bloggers, it is spreading rapidly among privacy-conscious professionals and developers as word of mouth praises it as an excellent open-source Granola alternative [Source 1, Source 9]. In particular, providing powerful local-centric features for free in a SaaS market where paid subscription models are the norm serves as a major differentiator [Source 1, Source 9].

---

## What's Next?

Going forward, the AI meeting notes market is likely to be dichotomized into "cloud-centric centralized services" and "device-centric private on-device services." As the performance of small open-source AI models advances dramatically, high-quality summaries and Q&A (Chat with your meetings) have become fully possible on personal laptops or PCs without needing massive servers [Source 1].

When saving meeting notes in the future, users will first question, "Where is this meeting content transmitted?" Projects like Yogurt present a standard where developers can freely expand features and users can maintain complete control over their data.

Instead of the scene where bots were dismissed with a nagging uneasy feeling after a meeting, wrapping up meetings securely and quickly inside your computer may become the standard of the future.

---

## AI's Perspective: Why Pay Attention?

Armed with privacy and an open-source philosophy in a meeting notes market dominated by cloud services, Yogurt will be a welcome turning point for both developers and privacy-conscious users. It serves as an exemplary case showing how powerful a combination of on-device local AI and open source can be as an alternative for users fatigued by the centralized SaaS ecosystem.

---

## References

1. [Show HN: Yogurt – Free, private, open-source alternative to Granola](https://github.com/FrigadeHQ/yogurt) [Source 1]
2. [Yogurt: Free, private, open-source alternative to Granola](https://www.producthunt.com/products/yogurt) [Source 2]
3. [5 Best Open Source Granola Alternatives in 2026](https://openalternative.co/alternatives/granola) [Source 4]
4. [Best 10 Granola Alternatives & Competitors [2026] | Jamie](https://www.meetjamie.ai/blog/granola-alternatives) [Source 5]
5. [Free open-source alternatives to Granola | Maigentools](https://www.maigentools.com/alternatives/granola) [Source 6]
6. [Show HN: Yogurt – Free, private, open-source alternative...](https://daily.dev/posts/show-hn-yogurt-free-private-open-source-alternative-to-granola-w8zhburxd) [Source 8]
7. [Yogurt Growth Play: Free + Open Source Beats a Paid Leader ...](https://www.figuringoutwithai.com/growth/yogurt-free-open-source-granola-alternative-growth-play-2026) [Source 9]
8. [Yogurt AI: Granola의 무료 오픈소스 대안, 개인정보를 보호하는 AI 회의...](https://dev-hub.dev/news/8348) [Source 10]
9. [Yogurt AI: Free, Private, Open-Source Meeting Notes | AI/TLDR](https://ai-tldr.dev/tools/yogurt/) [Source 11]
10. [9 Best Granola AI Alternatives in 2026 (Compared & Reviewed)](https://www.getvoibe.com/resources/granola-alternatives/) [Source 13]