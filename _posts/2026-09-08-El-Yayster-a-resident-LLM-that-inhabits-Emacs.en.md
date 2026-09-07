---
layout: post
title: "Introducing El Yayster: The AI that has become the 'body,' not just the 'mouth,' of my computer"
description: "What would it look like if an AI weren't just a chatbot assistant, but could move directly within your editor to manage code and control the environment? We explore El Yayster, a new form of AI residing in Emacs."
summary: "While existing AI tools for Emacs functioned merely as a 'mouth' simply answering user questions, El Yayster grants the AI control over the editor, acting as a 'body' that can observe and act within the user's Emacs environment."
tags: [AI, Emacs, ElYayster, Programming]
image: 2026-09-08-El-Yayster-a-resident-LLM-that-inhabits-Emacs.jpg
image_alt: "A conceptual image depicting an AI actively working within the Emacs editor environment."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "This represents a shift from AI that uses tools to AI that becomes the environment itself. It is an exciting step forward from a passive relationship waiting for user intent toward an agentic relationship where we work together."
quiz:
  - question: "What is the biggest difference between El Yayster and most existing Emacs AI packages?"
    choices: ["The types of AI models supported", "Whether the AI directly controls the Emacs environment", "The installation method"]
    answer: 1
    explanation: "El Yayster goes beyond a simple conversational interface by acting as a 'body' that allows the AI to observe the Emacs environment and actively use tools to control it."
  - question: "How does El Yayster control the Emacs environment?"
    choices: ["Direct cloud connection", "Gated Emacs Lisp code", "Macros manually entered by the user"]
    answer: 1
    explanation: "El Yayster uses 'gated Emacs Lisp' to interact with the Emacs environment."
  - question: "What is the recommended execution environment (happy path) for El Yayster?"
    choices: ["Commercial cloud services requiring an API key", "Ollama running locally", "A web browser-based editor"]
    answer: 1
    explanation: "While El Yayster supports various OpenAI-compatible endpoints, running it locally via Ollama is the recommended approach."
lang: en
ref: 2026-09-08-El-Yayster-a-resident-LLM-that-inhabits-Emacs
audio: 2026-09-08-El-Yayster-a-resident-LLM-that-inhabits-Emacs.en.mp3
industry: creative
---

Imagine waking up, turning on your computer, and finding that your usual editor has become more than just a space for writing documents—it has become a colleague that thinks and acts alongside you.

Many of the AI tools we have used until now were like a "mouth." When we spoke to them (inputted text), the AI would simply spit out appropriate answers in a document window. Recently, however, a project has emerged that brings a very interesting change to the Emacs (a highly extensible text editor) environment. It is an experimental tool called **'El Yayster.'**

### Why is this important?

Most AI integrations so far have been in the form of "Q&A" assistants, where the user asks a question and the AI simply shows the results. El Yayster, however, completely flips this relationship.

The reason this technology is important is that the "location of the AI" has changed. The AI is no longer a passive assistant waiting for instructions, but an "agent" that grasps the situation inside the editor and controls the environment itself. This change is like a chef having a skilled apprentice who not only provides recipes but also trims ingredients and manages the heat on the stove. It means the AI can handle repetitive tasks by operating the editor itself. [Source: ElYayster – a resident LLM that inhabits Emacs | Modern Orange](https://modernorange.io/item/49602258)

### Easy to understand: From 'mouth' to 'body'

We can use an analogy to easily understand this shift.

Previous AI tools were like a consultant on the other end of a phone line. If we described our symptoms, they would tell us the solution. **El Yayster is like lending an AI a 'body' called Emacs.** [Source: GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)

This model doesn't just write text into a buffer; it perceives the Emacs software environment like a living organism. [Source: yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md)

1. **Observe**: First, the AI looks at your live environment.
2. **Decide**: It judges what action is necessary.
3. **Act**: It operates the editor using a tool called 'gated Emacs Lisp' (the programming language used to manipulate the Emacs editor).
4. **Repeat**: It verifies the results and proceeds to the next task. [Source: GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)

It is as if the AI is directly clicking buttons and executing commands in Emacs, just as we move around the editor with a mouse and keyboard.

### Current status: How can it be used?

El Yayster is currently evaluated as a very unique attempt that resides and operates within the space of Emacs. [Source: Branches · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/branches/all)

Users can connect it to any model compatible with OpenAI, and it designates 'Ollama' running in a local environment as the recommended setup, or the 'happy path.' [Source: yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md) This also means that AI can freely control your editor within your own computer safely, without using cloud APIs.

Of course, one must keep in mind that this is still an experimental tool in its early stages. It will be a powerful automation tool for users who are proficient with Emacs, but because complex control is given to the AI, it is up to the user to decide how much of their editor environment they want to entrust to the AI.

### What lies ahead?

In the future, it is highly likely that we will see AI going beyond just reviewing the code we write; it will become a daily occurrence for AI to change editor settings, find bugs, and optimize project structures according to rules we set. El Yayster is a bold experiment toward that future.

It will be a very interesting experience to watch how much more delicately AI will move the 'body' of our editors, and how much more comfortable our work environments will become in the process.

---

## MindTickleBytes AI Reporter's Perspective
The emergence of El Yayster is a prime example of how technical tools can coexist with humans. Moving past the era where humans had to input every single command, the era of 'Resident AI,' where AI becomes part of the system and breathes with us, is rapidly approaching.

## References
1. [ElYayster – a resident LLM that inhabits Emacs | Modern Orange](https://modernorange.io/item/49602258)
2. [yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md)
3. [GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)
4. [Branches · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/branches/all)