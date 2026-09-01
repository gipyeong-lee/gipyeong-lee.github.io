---
layout: post
title: "The hidden giant in your computer: Why does the ChatGPT app contain LibreOffice?"
description: "A look at the recently discovered 1.7GB bundle in the ChatGPT desktop app, and the LibreOffice and development tools hidden within."
summary: "It has been revealed that OpenAI's ChatGPT desktop app hides an external software package totaling 1.7GB during installation."
tags: [ChatGPT, OpenAI, software, LibreOffice, tech-news]
image: 2026-09-02-The-ChatGPTCodex-app-bundles-a-full-copy-of-LibreOffice.jpg
image_alt: "Abstract image showing the internal folder structure of the ChatGPT app"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "It is intriguing that ChatGPT, which was thought to be a simple chat app, actually contains a powerful development and document processing engine. This shows that AI is evolving beyond a mere conversational partner into an agent that performs practical 'work' within the user's computer."
quiz:
  - question: "What is the size of the 'codex-primary-runtime' folder within the ChatGPT desktop app?"
    choices: ["170MB", "1.7GB", "17GB"]
    answer: 1
    explanation: "That folder contains about 1.7GB of software packages."
  - question: "Which software is NOT included in this bundle?"
    choices: ["Python", "Node.js", "Microsoft Word"]
    answer: 2
    explanation: "The bundle includes Python, Node.js, and LibreOffice, but Microsoft Word is not included."
  - question: "Why does this app install external tools like LibreOffice?"
    choices: ["Simple waste of space", "Leveraging internal tools for document tasks", "Undeletable libraries"]
    answer: 1
    explanation: "Through the technical documentation included alongside it, the AI learns how to locate and utilize these binaries."
lang: en
ref: 2026-09-02-The-ChatGPTCodex-app-bundles-a-full-copy-of-LibreOffice
audio: 2026-09-02-The-ChatGPTCodex-app-bundles-a-full-copy-of-LibreOffice.en.mp3
industry: general
---

## ChatGPT goes beyond conversation to carry 'tools'

Imagine this: You buy a new smartphone and expect only basic apps to be installed, but you find out that deep inside the app folder, there are dozens of cookbooks and a whole toolbox stashed away. Something like this was recently discovered in OpenAI's desktop application (formerly known as Codex, currently rebranded as ChatGPT). [Source 1](https://simonwillison.net/2026/Sep/1/codex-libreoffice/), [Source 4](https://x.com/simonw/status/2094864223683903800)

Inside this app, which we thought was just a simple chat window—specifically in a secret space named `codex-primary-runtime` under the `~/.cache` folder—a massive software bundle totaling 1.7GB was found hidden. [Source 3](https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache), [Source 5](https://news.ycombinator.com/item?id=49527396)

## Why does this matter?

From a user's perspective, you might be flustered, thinking, "Does it really take up that much of my computer's capacity?" However, this phenomenon is a significant signal that AI is transforming from a 'talking parrot' into a 'problem-solver that assists with practical work.' While past AI stopped at answering questions, this new version attempts to directly manipulate tools installed on your computer (Python, document editors, etc.) to create real results.

## Easy to understand: AI's 'toolbox'

Let's use an analogy to make this easy to understand. Imagine you hired a chef (AI). In the past, the chef only told you the recipe with words. But the current chef has entered your kitchen directly, opened a cookbook (LibreOffice), handles knives and gas ranges (Python, Node.js) themselves, and is fully prepared to actually cook the meal.

In fact, this bundle includes full installation files for Python (a computer language execution tool) and Node (Node.js, a web technology execution tool), as well as tools like LibreOffice (an open-source document editor) and Poppler (used for document conversion). [Source 1](https://simonwillison.net/2026/Sep/1/codex-libreoffice/), [Source 2](https://zeli.app/story/49527396) An interesting point is that there is a separate 'user manual' (Skills) inside the app describing how to utilize these massive tools. [Source 3](https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache)

LibreOffice is a free document processing software created by countless volunteers around the world, providing an open environment where anyone can study and improve its inner workings. [Source 7](https://www.libreoffice.org/) By 'pre-planting' these tools inside the app, OpenAI has built an environment where the AI can execute external programs without delay the moment it receives your command.

## Current situation

Currently, this functionality is being implemented through the ChatGPT desktop app. [Source 8](https://github.com/openai/codex) While the user sees a normal conversational interface on the surface, behind the scenes, these massive tool collections are waiting for the AI's commands. [Source 9](https://filecr.com/windows/openai-codex/) Of course, the method of forced software bundling might look like a waste of computer resources to some users. Security analysts and developers are expressing surprise at these hidden files. [Source 5](https://news.ycombinator.com/item?id=49527396)

## What will happen in the future?

The way AI carries its own toolbox around will become more common in the future. This is because the era of the 'agent'—which doesn't just generate answers but edits document files, compiles code, and analyzes data within the user's computer—is beginning in earnest. [Source 6](https://github.com/hashgraph-online/awesome-codex-plugins) In the future, you might not just be talking to AI, but watching AI turn on LibreOffice on your computer to write reports.

## MindTickleBytes' AI Reporter perspective

The fact that AI is getting smarter ultimately means the range of tools that AI can handle is broadening. The fact that ChatGPT contains LibreOffice is strong evidence that AI is moving beyond a simple knowledge repository and is now deeply penetrating our actual productivity environment.

## References

1. Codex bundles LibreOffice - [https://simonwillison.net/2026/Sep/1/codex-libreoffice/](https://simonwillison.net/2026/Sep/1/codex-libreoffice/)
2. Codex bundles LibreOffice — The ChatGPT/Codex app bundles a ... - [https://zeli.app/story/49527396](https://zeli.app/story/49527396)
3. OpenAI Codex app bundles LibreOffice, Python, Node in 1.7GB ... - [https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache](https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache)
4. Simon Willison on X: "Just noticed the ChatGPT desktop app ... - [https://x.com/simonw/status/2094864223683903800](https://x.com/simonw/status/2094864223683903800)
5. The ChatGPT/Codex app bundles a full copy of LibreOffice ... - [https://news.ycombinator.com/item?id=49527396](https://news.ycombinator.com/item?id=49527396)
6. GitHub - hashgraph-online/awesome-codex-plugins: A curated ... - [https://github.com/hashgraph-online/awesome-codex-plugins](https://github.com/hashgraph-online/awesome-codex-plugins)
7. Free and private office suite, no forced AI — LibreOffice - [https://www.libreoffice.org/](https://www.libreoffice.org/)
8. GitHub - openai/codex: Lightweight coding agent that runs in your... - [https://github.com/openai/codex](https://github.com/openai/codex)
9. OpenAI ChatGPT(With Codex) Download (Latest 2026) - FileCR - [https://filecr.com/windows/openai-codex/](https://filecr.com/windows/openai-codex/)