---
layout: post
title: "Creating AI assistants: Could it be as easy as writing a notepad? Designing with 'Margarita' in Markdown"
description: "Can you create an AI agent without knowing how to code? Introducing Margarita, a new tool that extends the Markdown format to systematically write workflows for AI agents."
summary: "Margarita is a tool that helps anyone easily design AI agent workflows by adding programming features like variables and loops to Markdown syntax."
tags: [AI, Agent, Markdown, Programming, Margarita]
image: 2026-07-02-Show-HN-Margarita---Programming-language-for-Agents-using-Markdown-ish-syntax.jpg
image_alt: "A systematic structural representation of a complex AI agent workflow using Markdown syntax"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "The attempt to design AI agent logic without complex coding will be a key factor in the popularization of agents."
quiz:
  - question: "What does the .mgx file format, a key feature of Margarita, support?"
    choices: ["Static text generation", "Execution control of AI agents (state, memory, tool calls, etc.)", "Simple HTML conversion"]
    answer: 1
    explanation: "The .mgx format extends the existing .mg format to provide additional functionality required when an AI agent is running, such as state management and tool calls."
  - question: "Which AI models are required to use Margarita?"
    choices: ["All types of models", "Ollama and Claude", "Only specific language models"]
    answer: 1
    explanation: "Margarita currently requires Ollama and Claude for use."
  - question: "What is the goal of Margarita?"
    choices: ["Learning complex programming languages", "Making writing agents as easy as writing Markdown", "Search engine optimization"]
    answer: 1
    explanation: "Margarita aims to make writing agents as easy as writing in Markdown."
lang: en
ref: 2026-07-02-Show-HN-Margarita---Programming-language-for-Agents-using-Markdown-ish-syntax
audio: 2026-07-02-Show-HN-Margarita---Programming-language-for-Agents-using-Markdown-ish-syntax.en.mp3
industry: creative
---

Imagine you wake up in the morning and tell your AI assistant, "Summarize today's meeting materials for me." The AI then acts like a human, finding the necessary files itself, summarizing the content, and sending the results via email. We call these smart assistants 'AI Agents.' However, the process of creating such agents has been very complex until now. Developers have had to write complicated code and constantly wrestle with 'prompts' (instructions input into the AI) to ensure the AI follows directions well.

Recently, a new tool has appeared that allows you to design AI agents as simply as using 'Markdown' (a syntax for easily creating web documents) that we use when writing blog posts or taking notes. This is 'Margarita.'

### Why is this tool important?

Until now, the way we communicate with AI has been mainly conversation-oriented. However, conversation can sometimes lead the AI to misunderstand the user's intent or lose its way during long work processes. Developers have had to rely on prompt writing to make AI complete complex tasks step-by-step. [Reference 1](https://www.margarita.run/)

Margarita solves these difficulties. This is because it allows anyone to design an AI agent's behavior according to set rules in a familiar Markdown style, rather than using complex code. This means you can obtain the desired results systematically and consistently without having to rely on complex prompt engineering. [Reference 1](https://www.margarita.run/)

### Easy to understand: Giving wings to Markdown

To understand Margarita, let's use a metaphor. Imagine you are writing recipe cards when cooking. If the conventional method is like following a chef around saying, "Chop the onions now," or "Adjust the heat now," Margarita is like writing a systematic 'recipe card' in advance.

Simply put, Margarita mixes programming features into common Markdown syntax. [Reference 1](https://www.margarita.run/) The key features are as follows:
- **Variable**: A field to store the value of information.
- **Loop**: A rule to process multiple items one by one in order.
- **Conditional**: A decision of "If this, then do that."

By adding logical functions to Markdown in this way, you clearly specify how an AI agent should behave in certain situations. [Reference 4](https://github.com/Banyango/margarita) Margarita provides two file formats. [.mg files](https://pypi.org/project/margarita/) are used to create dynamic prompts, and [.mgx files](https://pypi.org/project/margarita/) act as 'agent scripts' that go further to control an agent's memory management or tool calls. [Reference 2](https://pypi.org/project/margarita/)

Since the resulting output is essentially rendered (displayed on screen) in the familiar Markdown format, it can be used anywhere that supports Markdown. [Reference 4](https://github.com/Banyango/margarita)

### Current status: How far has it come?

Margarita makes the process of configuring agents and building logic much simpler for developers. In particular, it enables the efficient handling of multiple templates—saving them separately and reusing or nesting them when needed—greatly increasing work efficiency. [Reference 3](https://www.banyango.com/margarita/)

However, keep in mind that currently, you need to configure the environment for Ollama and Claude models to utilize this tool. [Reference 3](https://www.banyango.com/margarita/) In other words, it is currently at a stage where it is better suited for users who already have some understanding of AI development environments to boost productivity, rather than for complete beginners.

### What is the future outlook?

Experts predict that in the near future, Markdown will transcend its role as a simple document format and become a core language for software development. [Reference 13](https://www.infoworld.com/article/4146579/markdown-is-now-a-first-class-coding-language-deal-with-it.html) Tools like Margarita will accelerate this trend. In the future, creating AI agents will increasingly resemble natural language and familiar document formats. The era is coming where you are no longer just a person writing 'prompts,' but a manager writing the 'behavior manual' for your assistant—the agent.

---

### MindTickleBytes AI Reporter's Perspective
As technology becomes more complex, the tools used to handle it must become more intuitive and easier. Margarita's attempt to define agents using Markdown will fundamentally make the collaboration between AI and humans more transparent.

---

## References
1. Margarita — Writing agents should be as easy as writing markdown. (https://www.margarita.run/)
2. margarita · PyPI (https://pypi.org/project/margarita/)
3. MARGARITA - MARGARITA (https://www.banyango.com/margarita/)
4. GitHub - Banyango/margarita: Margarita is a lightweight ... (https://github.com/Banyango/margarita/)
13. Markdown is now a first-class coding language: Deal with it | InfoWorld (https://www.infoworld.com/article/4146579/markdown-is-now-a-first-class-coding-language-deal-with-it.html)