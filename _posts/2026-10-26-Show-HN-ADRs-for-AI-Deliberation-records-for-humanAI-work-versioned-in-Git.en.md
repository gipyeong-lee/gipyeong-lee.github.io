---
layout: post
title: "Conversations with AI: Do they vanish when you close the chat? Introducing 'ADRs4AI', a methodology for recording AI collaboration"
description: "We introduce ADRs4AI, a tool and methodology to record and version control critical decisions made during AI-assisted projects, ensuring they don't disappear."
summary: "Learn about 'ADRs4AI', a technique that allows anyone to resume discussions with AI by recording collaborative decisions alongside code in Git."
tags: [AI, Collaboration, Git, DeveloperTools, Productivity]
image: 2026-10-26-Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git.jpg
image_alt: "An image representing code and conversation records systematically accumulated in a Git repository"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Transforming AI's reasoning process into an asset rather than transient chat data is a critical step in changing the future of collaboration."
quiz:
  - question: "What is the core value ADRs4AI aims for?"
    choices: ["Increasing AI's memory infinitely", "Making the decision-making process between humans and AI sustainable and recoverable", "Enabling AI to make all decisions by itself"]
    answer: 1
    explanation: "ADRs4AI aims to secure 'epistemic continuity' so that thoughts and decisions shared with AI are not lost and can be resumed later."
  - question: "What recording principle does ADRs4AI use?"
    choices: ["Automatic storage on cloud servers", "Docs-as-code principle", "Utilizing an AI-specific database"]
    answer: 1
    explanation: "ADRs4AI follows the docs-as-code principle, where documentation is written like code and managed via Git."
  - question: "Does ADRs4AI support only specific AI models?"
    choices: ["No, it is a model-agnostic approach", "Yes, it can only be used with specific models", "It only supports Gemini models"]
    answer: 0
    explanation: "ADRs4AI adopts a model-agnostic methodology that is not dependent on any specific model."
lang: en
ref: 2026-10-26-Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git
audio: 2026-10-26-Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git.en.mp3
industry: creative
---

Imagine this: late last night, you designed the structure of a complex project with an AI. You rigorously discussed database schemas and which features (APIs) to build. The next morning, you say to the AI, "Let's continue from where we left off yesterday." But the AI remembers nothing about who you are or the decisions made. Your hard work from yesterday has simply vanished into past chat logs.

To solve this frustrating situation many people face, a concept called "ADRs4AI" has emerged.

## Why is it important?

AI has become exponentially smarter, but its "memory" still has limits. The moment you close the chat window, the context of the discussion often becomes fragmented. If the reasons behind important decisions aren't recorded, you end up repeating the same explanations or forgetting why those decisions were made when you collaborate later.

ADRs4AI solves this. By recording the AI collaboration process in a version control system like Git (a system that tracks software changes), we can manage "Decision Records" made with AI just as we manage software. This allows you, or future collaborators, to recall the flow of thought shared with the AI at any time. [Source: ADRs4AI - GitHub](https://github.com/ADRs4AI)

## In simple terms

"ADR" originally stands for "Architecture Decision Records," a method developers use to document the reasons for choosing specific technologies. ADRs4AI extends this for AI collaboration.

Metaphorically, it is **"your own work journal containing records of conversations with AI."** Just as writing a diary allows you to revisit past thoughts, ADRs4AI involves writing down complex technical choices decided with AI as Markdown documents and saving them in the project folder. [Source: Decision Records for AI-Driven Software Development](https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/)

It’s like leaving notes on a blueprint explaining why you placed a block of a certain color in a specific spot when building LEGOs. When you need to reassemble or modify the model later, simply reading those notes allows you to resume work without hesitation.

## Current State

ADRs4AI is not just a concept; it is implemented in actual tools.

*   **Tool Suite**: Comprised of VS Code extensions, iOS clients, project templates, and essays explaining the methodology. [Source: GitHub - ADRs4AI/human-ai-collaboration-template-A](https://github.com/ADRs4AI/human-ai-collaboration-template-A)
*   **Model Agnosticism**: It is not tied to a specific AI (e.g., Gemini, Claude). You can apply this methodology regardless of which AI you use. [Source: What is ADRs4AI?](https://adrs.systems/what-is/)
*   **Recording Principle**: It adheres to the "docs-as-code" approach, a way of handling documentation like code. Decisions made with AI are written as Markdown documents within the code repository, version-controlled via Git, and reviewed by colleagues through Pull Requests (PRs). [Source: Planning & Architecture Decision Records](https://lukewilk.github.io/AI-architecture/planning-and-adr.html)

This approach elevates AI from being a "one-off conversation partner" to a "continuous partner" who thinks along with us on our projects. [Source: ADRs4AI - GitHub](https://github.com/ADRs4AI)

## What happens next?

Collaboration with AI is becoming increasingly complex. We are entering an era where we look beyond simply asking AI to write code and instead deliberate on the entire project architecture with AI.

In this process, "epistemic-continuity" protocols like ADRs4AI—a state where the context of conversations with AI remains unbroken—will become essential. This is because it creates a virtuous cycle where the decisions we make remain as data, which is then recycled for the next stage of AI learning and reasoning. As seen in cases where AI has already been introduced into democratic deliberation processes, AI can greatly assist in systematically organizing human discussions and reaching consensus. [Source: AI can help humans find common ground in democratic deliberation](https://deepmind.google/research/publications/65220/)

Our work is no longer volatile. Every thought shared with AI will be systematically accumulated within the Git repository, and the next time we open the project, an even smarter AI will be able to resume the conversation immediately based on those records.

---

### MindTickleBytes AI Reporter's Perspective
Leaving the AI's reasoning process as transient data is a waste of intellectual resources. Managing the records of collaboration between AI and humans in Git is the clearest indicator that we have begun to treat AI as a "colleague" in our projects, rather than just a tool.

---

## References

1. [GitHub - ADRs4AI/human-ai-collaboration-template-A](https://github.com/ADRs4AI/human-ai-collaboration-template-A)
2. [Home | ADRS—AI-Driven Research for Systems](https://ucbskyadrs.github.io/)
3. [ADRs for AI - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=jlumbroso.adrs4ai)
4. [adrs4ai-pneumatic · PyPI](https://pypi.org/project/adrs4ai-pneumatic/)
5. [Towards Human-AI Deliberation: Design and Evaluation of...](https://arxiv.org/pdf/2403.16812)
6. [deliberation-AI Agents on GitHub | SkillsLLM](https://skillsllm.com/skill/deliberation)
7. [Free AI Humanizer | Humanize AI to Sound Like You, Not AI](https://www.grammarly.com/ai-humanizer)
8. [Human or Not: A Social Turing Game is Back, Play Now](https://humanornot.so/)
9. [AI can help humans find common ground in democratic deliberation](https://deepmind.google/research/publications/65220/)
10. [WURK - Microtask Marketplace for Humans & AI Agents](https://wurk.fun/)
12. [ADRs4AI - GitHub](https://github.com/ADRs4AI)
13. [What is ADRs4AI? · ADRs4AI - adrs.systems](https://adrs.systems/what-is/)
14. [Scaling AI Solution Architecture: How ADRs + Git + Claude...](https://www.linkedin.com/pulse/scaling-ai-solution-architecture-how-adrs-git-claude-rosselet-xhsre)
16. [Planning & Architecture Decision Records | Enterprise AI Delivery](https://lukewilk.github.io/AI-architecture/planning-and-adr.html)
17. [Decision Records for AI-Driven Software Development](https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/)