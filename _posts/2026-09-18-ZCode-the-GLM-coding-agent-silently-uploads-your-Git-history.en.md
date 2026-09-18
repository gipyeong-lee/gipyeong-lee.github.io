---
layout: post
title: "Wait, My Coding History Is Secretly Being Sent to the Cloud? The Controversy Surrounding ZCode's Covert Data Leaks"
description: "Allegations have emerged that the AI coding tool ZCode is sending users' Git history to its servers without their knowledge. We explore why this poses a danger to developers."
summary: "Forensic analysis has revealed that the AI coding tool ZCode has been secretly uploading users' entire project Git history—encrypted—to Alibaba Cloud (Aliyun OSS)."
tags: [AI, Coding, Security, ZCode, DevelopmentTools]
image: 2026-09-18-ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history.jpg
image_alt: "An illustration depicting coding data from a computer screen being siphoned off to an unknown cloud server."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "The data developers provide to coding tools is far more than just simple code. Opaque data collection practices are a dangerous act that fundamentally shakes trust in AI tools."
quiz:
  - question: "What user data is ZCode alleged to be secretly uploading?"
    choices: ["Chat history only", "Entire project Git history and settings", "Browser history only"]
    answer: 1
    explanation: "ZCode is accused of encrypting and transmitting an entire project workspace, including Git history, reflogs, and LFS caches."
  - question: "How does ZCode’s official privacy policy address data collection?"
    choices: ["It explicitly mentions uploading entire projects", "It only mentions data submitted during chat sessions", "It makes no mention at all"]
    answer: 1
    explanation: "The official policy only mentions the collection of text, files, and code submitted during chats; it does not mention uploading entire repositories."
  - question: "To which cloud service does ZCode upload the data?"
    choices: ["AWS S3", "Google Cloud Storage", "Aliyun OSS"]
    answer: 2
    explanation: "Analysis shows that ZCode is transmitting data to Alibaba Cloud (Aliyun OSS)."
lang: en
ref: 2026-09-18-ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history
audio: 2026-09-18-ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history.en.mp3
industry: security
---

Imagine this: All the revision history of a project you spent months working nights on, your past mistakes, and sensitive configuration information that might have accidentally slipped into the code are being transmitted to someone else’s server without your knowledge. How would that make you feel? Recently, this exact terrifying suspicion was raised among developers using the AI coding tool "ZCode."

ZCode is an official desktop AI coding agent built by Z.AI based on the GLM model [[Source 4](https://www.digitalapplied.com/blog/zcode-glm-5-2-agentic-development-environment-guide), [Source 5](https://glm5.app/blog/glm-5-3-zcode)]. The news that this tool, which had been gaining attention for its convenient features, has been secretly transmitting user data is sending shockwaves through the developer community.

### Why does this matter?

You might think, "It’s just sharing a bit of my code, what's the big deal?" But for developers, Git (a system that manages code change history) history is more than just files. It can contain not only the entire structure of the project but also accidentally included passwords, access tokens (authentication info), personal development habits, and even internal corporate secrets.

Transmitting such sensitive data to an external server without explicit user consent is a very serious security threat. In particular, this allegation suggests that even the "data transmission prevention" toggle provided in the UI might not be working properly, fundamentally shaking developers' trust [[Source 14](https://tokenstead.ai/guides/zcode-silent-git-history-upload)].

### Putting it simply

To use a simple analogy, imagine you installed a "Smart AI Diary App" to help you write a diary. The app helps you write. But while you're writing, the app secretly copies the "old diary" hidden behind the current one and the "scraps of notes" you already tore up and throws them into someone else’s warehouse.

Forensic reviews (the process of analyzing digital information to find evidence) show that ZCode version 3.12.3 generated an encrypted snapshot of a massive 748 MiB. Shockingly, 98.9% of this data was Git-related information [[Source 17](https://glbai.com/en/posts/zcode-silent-git-history-upload/)]. In other words, it wasn't just grabbing the parts needed for coding; it was taking the entire footprint of your project wholesale.

### What is the current situation?

The biggest problem is ZCode's attitude. Their official privacy policy only states that they collect "text, files, and code submitted during chats." There is no mention anywhere of collecting entire project repositories or Git history [[Source 16](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)].

According to what has been confirmed so far, ZCode is packaging and encrypting the user's workspace and uploading it to Alibaba Cloud (Aliyun OSS) [[Source 1](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)]. Some users even discovered these abnormal transmission attempts because they were repeatedly getting upload failure messages [[Source 16](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)].

### What happens next?

This incident has brought the issue of "transparency," hidden behind the immense convenience that AI development tools bring us, back to the surface. Developers now live in an era where they must carefully examine not only the performance of a tool but also how deeply and how it handles data on their computers (local environments).

We will have to wait and see if Z.AI offers a transparent explanation for this situation and improves its data collection methods, or if many developers will leave to find safer alternatives. When using AI coding tools, it is now a necessary habit to always check data privacy settings and network traffic at least once.

## References

1. [InsideZCode: Silently Uploading Your Entire Git History to the Cloud](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)
2. [ZCode Docs | GLM-5.3 Agentic Coding Guide](https://zcode.z.ai/en/docs/welcome)
3. [ZCode+GLM5.2 Tutorial - Stop Paying $200 for Claude Code](https://www.youtube.com/watch?v=7-evWQJ1Vlw)
4. [ZCode Explained: Z.ai's Agentic Dev Environment for GLM-5.2](https://www.digitalapplied.com/blog/zcode-glm-5-2-agentic-development-environment-guide)
5. [ZCode+GLM5.3: The Complete Guide to Z.AI's Coding Agent](https://glm5.app/blog/glm-5-3-zcode)
6. [Zcode Review 2026: Free AI Coding Agent With Goal Mode (vs Cursor)](https://www.bitdoze.com/zcode-ai-review/)
7. [GitHub - nothing1595/codex-zcode-bridge](https://github.com/nothing1595/codex-zcode-bridge)
8. [ZCode | Official Harness for GLM-5.3](https://zcode.z.ai/en)
9. [GLM5.2 бесплатно и БЕЗЛИМИТНО за 5 минут | Без карты в Zcode](https://www.youtube.com/watch?v=J3-lDiB-U8g)
10. [Claude Code vs Cursor vs ZCode: что выбрать в августе 2026](https://ip-calculator.ru/blog/artificial-intelligence/claude-code-vs-cursor-vs-zcode/)
11. [Революционный ZCode 3.0 — альтернатива Claude Code...](https://vc.ru/ai/3033535-zcode-3-0-alternativa-claude-code)
12. [What is GLM and how it can help you be more productive](https://sypalo.com/what-is-glm)
13. [OpenCode | The open source AI coding agent](https://opencode.ai/)
14. [ZCode uploads your git history; Z.ai holds the only key](https://tokenstead.ai/guides/zcode-silent-git-history-upload)
15. [ZCode, the GLM coding agent, silently uploads your Git history](https://news.ycombinator.com/item?id=49752422)
16. [ZCode AI Programming Tool Found to Upload Entire Git Repositories to Alibaba Cloud](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)
17. [Developers Asked Where ZCode Was Sending Their Git History](https://glbai.com/en/posts/zcode-silent-git-history-upload/)
18. [ZCode: what Z.ai's GLM-5.2 coding agent really is | eesel AI](https://www.eesel.ai/blog/zcode)
19. [Z.ai launches ZCode to turn GLM-5.2 into a coding-agent wedge](https://runtimewire.com/article/zai-zcode-glm-52-ai-coding-agent)