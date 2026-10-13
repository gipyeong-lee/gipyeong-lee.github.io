---
layout: post
title: "Did AI Change Hundreds of Thousands of Lines of Code on Its Own? Microsoft's $120,000 'Rust' Major Surgery"
description: "Microsoft has completely rewritten the foundation code for GitHub Copilot into Rust using AI agents. We explore the significance of this massive experiment, which cost $120,000."
summary: "Microsoft successfully utilized AI agents to rewrite the underlying software for GitHub Copilot from 430,000 lines of TypeScript to over 800,000 lines of Rust code."
tags: [AI, GitHub, Copilot, Rust, Software Development]
image: 2026-10-14-Microsoft-agentically-ports-Copilot-runtime-to-Rust-for-120K.jpg
image_alt: "An image conceptualizing a modern development environment blending Microsoft and GitHub logos."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "This case demonstrates that AI has evolved beyond a simple tool into an entity capable of completing complex engineering projects on its own."
quiz:
  - question: "What was the key role played by the AI agents in this Microsoft project?"
    choices: ["Generating design mockups", "Converting existing code into Rust", "Physically installing server infrastructure"]
    answer: 1
    explanation: "The AI agents were responsible for rewriting the TypeScript code that serves as the foundation for GitHub Copilot into the Rust language."
  - question: "Why was this project considered impossible in the past?"
    choices: ["Because there were too many types of languages", "Because AI agents did not exist", "Because it was a massive and complex rewrite"]
    answer: 2
    explanation: "A complete rewrite of such a massive system was considered a highly difficult and inefficient task, even for human developers, and was deemed an impossible project before the introduction of AI agents."
  - question: "What is the approximate total AI computing cost for this project?"
    choices: ["Approximately $120,000", "Approximately $50,000", "No cost incurred"]
    answer: 0
    explanation: "Microsoft spent approximately $120,000 in computing and token costs to execute this large-scale code migration."
lang: en
ref: 2026-10-14-Microsoft-agentically-ports-Copilot-runtime-to-Rust-for-120K
audio: 2026-10-14-Microsoft-agentically-ports-Copilot-runtime-to-Rust-for-120K.en.mp3
industry: creative
---

Imagine you are a librarian in a massive library, and you have to completely restructure the entire library's classification system from scratch. Reorganizing hundreds of thousands of books according to new rules is a gargantuan task that would be impossible to handle alone. But what if thousands of AI assistant librarians were deployed simultaneously to finish the job in just a few weeks?

Microsoft and GitHub recently accomplished something very similar. They completely replaced the core engine of "GitHub Copilot," the AI tool used by countless developers, with a different programming language.

### Why does this matter?

The term "runtime" (the environment required while a program is running) might sound unfamiliar. Simply put, it is the "foundation engine" that quietly supports the GitHub Copilot apps and command-line tools we use every day so they run smoothly. The fact that this engine has been changed means that Copilot will stay with us faster and more reliably.

Most remarkably, this project was not executed by humans working by hand, but was led by **"autonomous AI coding agents"** that can think and judge for themselves [[Reference 7](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ), [Reference 9](https://www.usefulainews.com/microsoft-agentically-ports-copilot-runtime-to/)].

### Easy to understand: The major surgery of changing 'languages'

Computer programming languages are similar to Korean or English. They just have different ways of giving instructions to computers. In this case, Microsoft swapped out their engine from the existing "TypeScript" (a language mainly used for web development) to a language called "Rust."

To use an analogy, if TypeScript is a "general notebook" that allows for free-form writing, Rust is like a "math textbook with very strict rules." Because Rust places extreme importance on code safety, once written, the probability of errors occurring is significantly lower compared to other languages. However, having a person manually convert hundreds of thousands of lines of code into such a strict language is as painful and time-consuming as rewriting a thousands-page dissertation into new rules without making a single mistake, word for word.

Microsoft's engineers hired a smart assistant called an **AI agent** to perform this task. Like a veteran developer, the AI agent read the existing code, grasped the context, and converted it into safe Rust code. As a result, 430,000 lines of TypeScript code were reborn as over 800,000 lines of Rust code [[Reference 7](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ), [Reference 12](https://www.tabnews.com.br/NewsletterOficial/microsoft-reescreve-runtime-do-copilot-em-rust)].

### Current situation: An impossible mission accomplished by AI

In the past, this project would have been classified as an "impossible plan" and would never have been started in the first place. By introducing AI agents, however, this massive migration was successfully completed in about 3 weeks of developer time, across 135 updates over 14.5 weeks [[Reference 6](https://sygentai.com/blog/2026-09-21-google-shipped-an-open-agentic-orchestrator-and-what-it-actually-takes-off-your-), [Reference 7](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ)].

In the process, $120,000 in tokens (AI processing costs) were consumed [[Reference 9](https://www.usefulainews.com/microsoft-agentically-ports-copilot-runtime-to/), [Reference 16](https://www.linkedin.com/posts/basharatwani_migrating-the-github-copilot-runtime-to-rust-activity-7508513737730084865-vrkT)]. This might feel expensive, but considering the cost of having dozens of human developers tied up for months on such major surgery, it shows how efficiently the AI performed the work. Of course, dozens of errors occurred during the process that required fixes, but the migration was ultimately completed successfully while fully maintaining the quality of the code [[Reference 12](https://www.tabnews.com.br/NewsletterOficial/microsoft-reescreve-runtime-do-copilot-em-rust), [Reference 16](https://www.linkedin.com/posts/basharatwani_migrating-the-github-copilot-runtime-to-rust-activity-7508513737730084865-vrkT)].

### What's next?

This case is a powerful signal of the future of software development. We are moving rapidly beyond the era where "developers write code directly" into an era where "developers provide goals to AI agents and review the results."

Microsoft's success hints that companies will inevitably need to utilize AI agents when replacing outdated systems with modern environments in the future. If the voice assistant on your smartphone or your work messenger is one day replaced with a faster and safer foundation engine, there might just be a massive AI "gardening" job behind the scenes like this one.

---
**MindTickleBytes' AI Reporter Perspective**
The fact that AI can modify and improve code on its own is not just a matter of cost. It means an era has opened where ideas that humans previously gave up on due to technical limitations can now take flight with the wings of AI agents and become reality.

## References
1. [Microsoft agentically ports Copilot runtime to Rust for $120K](https://www.devclass.com/devops/2026/09/19/microsoft-agentically-ports-copilot-runtime-to-rust-for-120k/5297592)
2. [Vue HN 2.0 | Microsoft agentically ports Copilot runtime to Rust for...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49763701)
3. [Unsealed Documents Highlight Microsoft And OpenAI Concerns Over...](https://www.finanznachrichten.de/nachrichten-2026-09/69622107-unsealed-documents-highlight-microsoft-and-openai-concerns-over-use-of-news-content-020.htm)
4. [Microsoft and Citrix mix 'n' match fake desktops](https://www-theregister-co-uk.nproxy.org/2009/07/13/citrix_microsoft_virtual_pcs/)
5. [Rust in Visual Studio Code](https://code.visualstudio.com/docs/languages/rust)
6. [Google shipped an open agentic orchestrator, and what it actually...](https://sygentai.com/blog/2026-09-21-google-shipped-an-open-agentic-orchestrator-and-what-it-actually-takes-off-your-)
7. [AI Accelerates Code Production, Not Responsibility | LinkedIn](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ)
9. [Microsoft Agentically Ports Copilot Runtime to Rust](https://www.usefulainews.com/microsoft-agentically-ports-copilot-runtime-to/)
10. [Vue HN 2.0 | Microsoft agentically ports Copilot runtime to Rust for...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49773998)
11. [Microsoft porte le runtime Copilot vers Rust de façon... — Fellow](https://www.fellow.news/article/www.theregister.com-devops-2026-09-18-microsoft-agentically-ports-copilot-runtime-to-rust-for-120k-5297549)
12. [Microsoft reescreve runtime do Copilot em Rust · Newsletter Oficial](https://www.tabnews.com.br/NewsletterOficial/microsoft-reescreve-runtime-do-copilot-em-rust)
14. [Microsoft agentically ports Copilot runtime to Rust for $120K](https://modernorange.io/item/49773998)
15. [Google News - Microsoft - Latest](https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFJ6ZGpRU0FtVnNLQUFQAQ?hl=en-US&gl=US&ceid=US:en)
16. [GitHub Engineers Use AI Agents to Port Codebase to Rust | LinkedIn](https://www.linkedin.com/posts/basharatwani_migrating-the-github-copilot-runtime-to-rust-activity-7508513737730084865-vrkT)
17. [Microsoft agentically ports Copilot runtime to Rust for...](https://vk.ru/wall-238001904_5872)
18. [RuStore — mobile app and game catalog for Android](https://www.rustore.ru/)