---
layout: post
title: "AI helps with coding? It's time to 'conduct': Introducing JetBrains Air"
description: "Discover JetBrains Air, a new environment for efficiently developing software by coordinating multiple AI agents simultaneously."
summary: "JetBrains Air is a new orchestration tool that helps developers coordinate and manage multiple AI agents at once."
tags: [AI, Software Development, JetBrains, Agent, Productivity]
image: 2026-09-22-JetBrains-Air-A-System-of-Products-for-Agentic-Software-Development.jpg
image_alt: "JetBrains Air logo and conceptual graphic of AI agents collaborating."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Extending the role of AI in complex coding tasks from a simple assistant to an executor is a natural progression. JetBrains' strategy to capture both productivity and control by providing an environment where developers can directly 'conduct' is noteworthy."
quiz:
  - question: "What is the role of JetBrains Air?"
    choices: ["An editor that completely replaces existing IDEs", "An environment that manages and coordinates multiple AI agents simultaneously", "Software that creates AI models directly"]
    answer: 1
    explanation: "Air does not replace existing IDEs; rather, it is an orchestration layer built on top of them that allows multiple AI agents to run and collaborate efficiently."
  - question: "What AI agents can be used in Air?"
    choices: ["Only single AI models created by JetBrains", "A wide variety of external AI agents (Codex, Claude, Gemini, Junie, etc.) can be selected freely", "AI models cannot be used; only code can be written"]
    answer: 1
    explanation: "Air supports a multi-vendor ecosystem, allowing users to freely select and use various external AI agents that suit their needs."
  - question: "Does JetBrains Air support models running in local environments?"
    choices: ["No, only cloud connections are supported", "Yes, it can be used by linking with local model runners such as Ollama", "It is only possible if the user modifies the code structure themselves"]
    answer: 1
    explanation: "Air provides an environment where models can run offline by linking with local model runners such as Ollama or LM Studio."
lang: en
ref: 2026-09-22-JetBrains-Air-A-System-of-Products-for-Agentic-Software-Development
audio: 2026-09-22-JetBrains-Air-A-System-of-Products-for-Agentic-Software-Development.en.mp3
industry: creative
---

Imagine this: When building a complex app, you act as a project manager, assigning tasks to several specialized developers. "Person A, please write the UI design code." "Person B, handle the database integration." You then perform a final review of their results and merge them into one.

Until now, when we talked about AI assisting with coding, we usually meant chatting 1-on-1 with an AI to get code suggestions. But we have now entered the era of 'Agents' (AI that can plan and execute tasks on its own), where AI goes beyond being just a 'helper' to performing actual work. The tool introduced today, [JetBrains Air](https://blog.jetbrains.com/blog/2026/09/22/introducing-jetbrains-air/), is a new environment that allows you to effectively manage and conduct these agents.

### Why is this important?

As software development becomes increasingly complex, it has become difficult for a single developer to know every line of code. Many have tried using multiple AIs simultaneously, but because each AI operates in isolation, it often led to increased management overhead.

JetBrains Air puts the developer at the center as the 'conductor.' You can [run multiple AI agents simultaneously](https://air.dev/) to delegate tasks, allowing you to focus on reviewing the overall flow and quality of the code. A major advantage is that [you can leverage the power of AI without significant changes to your existing workflow](https://baeseokjae.github.io/posts/jetbrains-air-review-2026/) since it integrates directly into tools you already use (IntelliJ IDEA, PyCharm, etc.).

### Understanding Orchestration

The concept of 'orchestration' (the process of coordinating multiple elements to create a single result) is key here. Simply put, it is similar to running an orchestra.

*   **Traditional Method:** A soloist with one instrument and one assistant helping keep time (traditional AI coding tools).
*   **Air's Method:** An orchestra of dozens of professional performers (various AI agents) and a conductor (the developer) standing in front of them, creating harmony for the entire piece.

JetBrains Air is the 'conductor's podium' for this orchestra. Through a standard technology called the [Agent Client Protocol (ACP)](https://daily.dev/posts/jetbrains-air-building-a-system-of-products-for-agentic-software-development-4kn5dhuhy), it helps different AIs connect to your IDE (Integrated Development Environment) as if they were one system. This allows you to [organize the entire process—planning, execution, and review—into one consistent flow](https://blog.jetbrains.com/air/2026/03/24/introducing-jetbrains-air/).

### Current Status: What can it do?

JetBrains built this environment based on 26 years of know-how in creating developer tools. Currently, JetBrains Air features:

1.  **Coexistence of Various Agents:** You can [freely select and integrate](https://air.dev/) various verified AI agents such as Codex, Claude Agent, Gemini CLI, and Junie.
2.  **Local Model Support:** When sending data outside is problematic or offline work is needed, you can [execute models in your own environment via local model runners like Ollama or LM Studio](https://blog.jetbrains.com/air/2026/07/what-s-new-air-gets-more-agents-local-models-and-java-kotlin-code-intelligence/).
3.  **IDE Integration:** There is no need to struggle to learn new tools; it can be [used directly within your familiar JetBrains IDE](https://altaitools.com/jetbrains-air/).

However, as JetBrains has honestly noted, [we are not yet at the stage where AI can completely complete complex, large-scale codebases on its own](https://altaitools.com/jetbrains-air/). Therefore, Air focuses on a human-centric 'collaborative environment' where agents write the code and developers review it.

### What comes next?

In the past, JetBrains introduced a lightweight editor called 'Fleet,' but they have [shifted their strategy to abandon it and concentrate on developing Air](https://technewsdaily.com/software/jetbrains-abandons-fleet-for-air-agentic-development-environment/) due to overlaps with existing product lines. This signifies more than just releasing a new tool; the company has bet its future on 'agent-based development.'

In the future, the ability to design code and 'instruct' AI agents to function correctly will be more important than the sheer volume of code a developer writes themselves. [As environments like JetBrains Air become commonplace, the developer's role is expected to move rapidly from 'implementer' to 'designer and manager'](https://sdtimes.com/ai/jetbrains-previews-air-an-agentic-development-environment/).

---

### MindTickleBytes AI Reporter's Perspective
Technology is evolving, but the crucial question is 'who holds the reins?' JetBrains Air is a practical, reality-oriented approach in that it creates an environment where the developer remains at the center, coordinating and taking responsibility for the results of multiple AIs rather than blindly trusting them. For developers in the AI era, now is the time to cultivate 'conducting skills'—the ability to deploy AI in the right place and collaborate—as much as coding ability.

## References
1. [JetBrains Air: Building a System of Products for Agentic Software Development](https://blog.jetbrains.com/blog/2026/09/22/introducing-jetbrains-air/)
2. [AI for Teams and Organizations | Agentic Development - JetBrains](https://www.jetbrains.com/agentic-software-development/)
3. [Quickstart with Air | JetBrains Air Documentation](https://www.jetbrains.com/help/air/quick-start-with-air.html)
4. [Air: Multitask with agents, stay in control](https://air.dev/)
5. [Air - The JetBrains Blog](https://blog.jetbrains.com/air/)
6. [JetBrains abandons Fleet for Air agentic development environment](https://technewsdaily.com/software/jetbrains-abandons-fleet-for-air-agentic-development-environment/)
7. [Air Launches as Public Preview – A New Wave of Dev Tooling Built on 26 Years of Experience - The JetBrains Blog](https://blog.jetbrains.com/air/2026/03/air-launches-as-public-preview-a-new-wave-of-dev-tooling-built-on-26-years-of-experience/)
8. [JetBrains Air: Building a System of Products for Agentic Software Development | daily.dev](https://daily.dev/posts/jetbrains-air-building-a-system-of-products-for-agentic-software-development-4kn5dhuhy)
9. [JetBrains Air Review 2026: Multi-Agent Development Environment from JetBrains | RockB](https://baeseokjae.github.io/posts/jetbrains-air-review-2026/)
10. [JetBrains Air: The Agentic Development Environment, Explained](https://altaitools.com/jetbrains-air/)
11. [What’s new: Air gets more agents, local models, and Java/Kotlin code intelligence - The JetBrains Blog](https://blog.jetbrains.com/air/2026/07/what-s-new-air-gets-more-agents-local-models-and-java-kotlin-code-intelligence/)
12. [Introducing JetBrains Central: An Open System for Agentic Software Development - The JetBrains Blog](https://blog.jetbrains.com/blog/2026/03/24/introducing-jetbrains-central-an-open-system-for-agentic-software-development/)
13. [JetBrains abandons Fleet IDE, pins hopes on forthcoming Air agentic development tool](https://devclass.com/2025/12/09/jetbrains-abandons-fleet-ide-pins-hopes-on-forthcoming-air-agentic-development-tool/)
14. [JetBrains previews Air, an agentic development environment - SD Times](https://sdtimes.com/ai/jetbrains-previews-air-an-agentic-development-environment/)
15. [JetBrains names the debt AI agents leave behind - The New Stack](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/)