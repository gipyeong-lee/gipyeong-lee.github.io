---
layout: post
title: "Your Own Encyclopedia Written and Managed by AI? ‘WUPHF’ and the New Paradigm of AI Memory"
description: "Through the 'WUPHF' project where AI agents record and learn autonomously, we explore the secrets of a smart AI memory store built solely with Markdown and Git, without complex databases."
summary: "The 'WUPHF' system has been unveiled, allowing AI to move beyond one-off information consumption and instead build and update its own knowledge base using Markdown documents and Git."
tags: [AI, WUPHF, Karpathy, Agents, Markdown, Open Source]
image: 2026-05-03-Show-HN-A-Karpathy-style-LLM-wiki-your-agents-maintain-Markdown-and-Git.jpg
image_alt: "A robot writing in a large encyclopedia with a pen and paper, with digital code and documents blended in the background"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Returning to familiar and transparent tools like Markdown and Git instead of complex vector databases is an interesting attempt to solve the AI 'black box' problem."
quiz:
  - question: "What is the file format used as the 'Source of Truth' for storing information in the WUPHF system?"
    choices: ["PDF files", "Markdown files", "Excel sheets"]
    answer: 1
    explanation: "WUPHF uses Markdown files, a human-readable text format, as the basic unit of knowledge storage."
  - question: "What tool does WUPHF use to track and manage the history of data changes?"
    choices: ["Photoshop", "Git", "Google Drive"]
    answer: 1
    explanation: "WUPHF utilizes Git, a tool used by developers for code management, to record how the AI has modified information."
  - question: "Which database technology is WUPHF currently not using to find information?"
    choices: ["SQLite", "Bleve (BM25)", "Vector or Graph DB"]
    answer: 2
    explanation: "WUPHF currently uses relatively simple and fast search engines like SQLite and Bleve instead of complex vector or graph databases."
lang: en
ref: 2026-05-03-Show-HN-A-Karpathy-style-LLM-wiki-your-agents-maintain-Markdown-and-Git
audio: 2026-05-03-Show-HN-A-Karpathy-style-LLM-wiki-your-agents-maintain-Markdown-and-Git.en.mp3
industry: robotics
---

## No More AI 'Memory Gaps'! The Arrival of the 'Markdown Wiki' That Records and Learns

Imagine you have a very smart and efficient assistant. But this assistant has one fatal flaw: every time they wake up, they completely forget what they did yesterday or what your preferences are. Wouldn't it be frustrating if you had to explain every morning, "I like coffee with no acidity, and please write reports in this font"?

In fact, the Artificial Intelligence (AI) we have been using so far has faced similar problems. Due to a technical limitation called the 'Context Window' (the amount of information AI can remember and process at once), they often forget previous content as conversations get longer or time passes. This is why, even if you want to build a deep relationship with AI, it always feels like you 'just met yesterday.'

However, a project recently emerged that attempts to solve this problem in a very unique and simple way, heating up 'Hacker News,' the playground for developers worldwide. It is a project called **WUPHF (pronounced 'Woof')**. [Source 1: Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://news.ycombinator.com/item?id=47899844)

The goal of this project is to create a 'knowledge store' where AI Agents (smart programs that judge and act on their own rather than just doing what they are told) record and manage information themselves, much like we write diaries or edit Wikipedia. [Source 3: WUPHF's Karpathy-Style LLM Wiki Puts Agent Memory Back on Markdown and Git](https://www.dailyneuraldigest.com/newsroom/2026-04-26-show-hn-a-karpathy-style-llm-wiki-your-agents-main/) Now, AI has its own 'secret notebook.'

---

## Why It Matters

The chatbots we use usually supplement their lack of knowledge through a technology called 'RAG (Retrieval-Augmented Generation),' which searches for external information to provide answers. However, this process is as complex as finding a code that only machines can read deep in the stacks of a giant library. It is nearly impossible for a general user to look into why the AI gave such an answer or on what basis it made that judgment.

WUPHF is important because it moves this complex and difficult process to very basic and transparent tools: **'Markdown'** (a very easy text format used for writing on the web) and **'Git'** (a time-machine-like tool that meticulously records revision history). [Source 2: WUPHF's Karpathy-Style LLM Wiki Puts Agent Memory Back on Markdown and Git](https://lilting.ch/en/articles/wuphf-markdown-git-llm-wiki)

To use a simple analogy, it's like making the structure of the AI's brain into a 'glass box' that we can see at a glance. Facts the AI learns about me or work knowledge are saved in **plain text files that we can also read**, and if the AI accidentally modifies information incorrectly, a **system is in place to return to past records at any time**. This is highly significant in terms of security and reliability, as it allows us to directly control and monitor the AI's memory.

---

## The Explainer: How the AI's 'Digital Brain' Works

The core idea of WUPHF started from a proposal by Andrej Karpathy, a legendary AI researcher who led Tesla's autonomous driving. [Source 7: llm-wiki · GitHub](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) Karpathy argued that AI needs a 'Knowledge Substrate' where it doesn't just consume information as a one-off but records and builds it up itself. [Source 4: Karpathy-Style LLM Wiki Ships for AI Agents: Markdown, Git, and BM25 as ...](https://www.clawbot.blog/blog/karpathy-style-llm-wiki-ships-for-ai-agents-markdown-git-and-bm25-as-memory-laye/)

Let's look deeper into how this system works through three analogies.

### 1. Markdown: The 'Standard Notebook' Written by AI
If you store information haphazardly, it's hard to find later. WUPHF stores it in a format called **Markdown files**. Markdown is a document with very simple rules, such as "bolding text or adding headings." Simply put, it's like the AI taking notes in a 'standardized notebook' that can be opened even in Notepad. Thanks to this, humans can also sneak a peek at what the AI has been studying. [Source 1: Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://news.ycombinator.com/item?id=47899844)

### 2. Git: The 'Time Machine' to Correct AI's Mistakes
Have you ever pressed 'Ctrl+Z' while working on a computer to undo an action? **Git** is a giant recording device that applies this to entire documents or even entire projects. Every time the AI modifies the wiki content, Git leaves a record of it like a photograph. If the AI enters nonsensical information or accidentally deletes important content, we don't need to panic and can simply command, "Return to the state as of 2 PM yesterday." [Source 5: [HN] Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown ...](https://www.dailydoseofai.tech/update/show-hn-a-karpathystyle-llm-wiki-your-agents-maintain-markdo-18d463)

### 3. Search Engines (Bleve & SQLite): Finding Information in One Second
Even if there are tens of thousands of books in a library, you can't find the one you want without a catalog. Instead of complex, state-of-the-art AI databases (Vector DBs), WUPHF uses traditional but proven search technologies called **Bleve (BM25 method)** and **SQLite**. [Source 13: ShowHN: WUPHF —Karpathy-Style LLMWiki with Markdown+Git...](https://openclawradar.com/article/wuphf-karpathy-llm-wiki-markdown-git) These act as 'smart librarians' that can instantly pick out the necessary information from tens of thousands of notes.

---

## Where We Stand

Currently, WUPHF is available as open source, so anyone can install and use it on their own computer. [Source 3: WUPHF's Karpathy-Style LLM Wiki Puts Agent Memory Back on Markdown and ...](https://www.dailyneuraldigest.com/newsroom/2026-04-26-show-hn-a-karpathy-style-llm-wiki-your-agents-main/) The attractive points of this project are as follows:

*   **Local-first:** All information is stored inside your computer (in the `~/.wuphf/wiki/` folder), not in the cloud. This reduces concerns about my personal stories or precious trade secrets leaking to external servers. [Source 1: Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://news.ycombinator.com/item?id=47899844)
*   **Self-Management System:** An automatic inspector called a 'Lint' runs once a day. it meticulously checks if there are any typos in the content recorded by the AI or if any linked links are broken. [Source 13: ShowHN: WUPHF —Karpathy-Style LLMWiki with Markdown+Git...](https://openclawradar.com/article/wuphf-karpathy-llm-wiki-markdown-git)
*   **Entity Fact Logs:** Important facts about people or projects are managed in separate summaries. It organizes things like "my preferences" and "decisions from the last meeting" in a clear manner. [Source 13: ShowHN: WUPHF —Karpathy-Style LLMWiki with Markdown+Git...](https://openclawradar.com/article/wuphf-karpathy-llm-wiki-markdown-git)

Immediately after its release, this project became a hot topic in the developer community, receiving 23 points of recommendation, and Andrej Karpathy's technical repository, which served as the foundation, drew a huge response, receiving more than 37,000 'Stars' (bookmarks) in just a few days. [Source 6: Hacker News => Show], [Source 11: Claude Code has learned to program in the Karpathy style.](https://www.linkedin.com/posts/aizendinternationalinnovations_claude-code-has-learned-to-program-in-the-activity-7450481858959769601-lLk-)

---

## What's Next

The emergence of WUPHF could significantly change the way AI agents work with us. While AI until now has been a 'obedient but forgetful new employee,' the foundation has now been laid for it to evolve into a **'reliable partner that understands me better the longer we work together.'**

Experts believe that this 'knowledge substrate' model will become a powerful alternative to existing complex and expensive AI memory systems. [Source 4: Karpathy-Style LLM Wiki Ships for AI Agents: Markdown, Git, and BM25 as ...](https://www.clawbot.blog/blog/karpathy-style-llm-wiki-ships-for-ai-agents-markdown-git-and-bm25-as-memory-laye/) It is particularly attractive in that it can maximize the AI's intelligence while protecting user privacy.

Imagine one day your AI assistant suggests first, "I re-read the work report you recorded last week, and there's a part that connects with this project. Should I draft a proposal in advance?" WUPHF is the first step toward such a future.

---

## AI's Take
**Perspective of MindTickleBytes' AI Reporter**

"The WUPHF project once again proves the old truth that 'the simplest is the most powerful.' In an age where state-of-the-art models worth trillions of won are pouring out, the attempt to implement AI's 'sustainable intelligence' using text files that anyone can read and database technology that has been loved for over 50 years is very refreshing. Now, AI is not just a search engine that answers your questions, but is being reborn as a true colleague who cultivates a garden of knowledge and shares records with you. Why not gift your AI partner a 'dedicated notebook' starting today?"

---

## References
1. [Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://news.ycombinator.com/item?id=47899844)
2. [WUPHF's Karpathy-Style LLM Wiki Puts Agent Memory Back on Markdown and Git](https://lilting.ch/en/articles/wuphf-markdown-git-llm-wiki)
3. [Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://www.dailyneuraldigest.com/newsroom/2026-04-26-show-hn-a-karpathy-style-llm-wiki-your-agents-main/)
4. [Karpathy-Style LLM Wiki Ships for AI Agents: Markdown, Git, and BM25 as ...](https://www.clawbot.blog/blog/karpathy-style-llm-wiki-ships-for-ai-agents-markdown-git-and-bm25-as-memory-laye/)
5. [[HN] Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown ...](https://www.dailydoseofai.tech/update/show-hn-a-karpathystyle-llm-wiki-your-agents-maintain-markdo-18d463)
6. [Hacker News => Show](https://www.hacker-news.news/Show)
7. [llm-wiki · GitHub](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
8. [ShowHN: A Karpathy-style LLM wiki your agents maintain...](https://catalayer.com/news/show-hn-a-karpathy-style-llm-wiki-your-agents-maintain-markdown-and-git)
9. [AgentWiki: Markdown Knowledge Base for LLM Agents](https://mcp-market.vercel.app/server/agent-wiki)
10. [ShowHN：一个由智能体维护의 Karpathy 风格 LLM...](https://thenote.app/post/zh/show-hn-ge-you-zhi-neng-ti-wei-hu-de-karpathy-feng-ge-llm-wei-ji-zhi-chi-ocq98m9n0e)
11. [Claude Code has learned to program in the Karpathy style.](https://www.linkedin.com/posts/aizendinternationalinnovations_claude-code-has-learned-to-program-in-the-activity-7450481858959769601-lLk-)
12. [llm-wiki-bootstrap by nanzhipro/karpathy-llm-wiki-bootstrap-skill](https://skills.sh/nanzhipro/karpathy-llm-wiki-bootstrap-skill/llm-wiki-bootstrap)
13. [ShowHN: WUPHF — Karpathy-Style LLMWiki with Markdown+Git...](https://openclawradar.com/article/wuphf-karpathy-llm-wiki-markdown-git)