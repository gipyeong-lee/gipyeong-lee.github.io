---
layout: post
title: "Can we really trust AI decisions? Inspect smarter and cheaper with 'jevals'"
description: "Introducing jevals, a new open-source tool that validates AI agent decisions in real-time, quickly and affordably."
summary: "jevals is a new tool that allows real-time validation of all AI agent tasks by using fast and precise 'Jev' decision models instead of slow, expensive LLM judges."
tags: [AI, AI Agents, Developer Tools, jevals]
image: 2026-10-12-Show-HN-jevals-replacing-LLM-judges-with-typed-Jev-decisions.jpg
image_alt: "A graphic screen analyzing AI agent decisions with precision"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Shifting from complex LLM judges to decision models that output fast, specific, typed answers is essential for the democratization of AI agents."
quiz:
  - question: "What is the most distinctive feature of jevals compared to traditional LLM judge methods?"
    choices: ["It generates longer answers", "It provides typed answers without writing text", "It is more expensive"]
    answer: 1
    explanation: "jevals uses 'Jev', a System One model, to provide probability-based answers to typed questions without writing text."
  - question: "Approximately how much does it cost to validate AI agents using jevals?"
    choices: ["Several dollars per trace", "About $0.00006 per trace", "It is free"]
    answer: 1
    explanation: "jevals processes nine inspection items in a single request, allowing it to operate at an affordable cost of about $0.00006 per trace."
  - question: "When is the Jev model at a disadvantage compared to an LLM judge?"
    choices: ["Simple yes/no questions", "When very fast responses are needed", "Questions where many rules are complexly intertwined"]
    answer: 2
    explanation: "In cases where multiple rules interact, such as very complex decision tables, accuracy may be slightly lower than that of an LLM judge."
lang: en
ref: 2026-10-12-Show-HN-jevals-replacing-LLM-judges-with-typed-Jev-decisions
audio: 2026-10-12-Show-HN-jevals-replacing-LLM-judges-with-typed-Jev-decisions.en.mp3
industry: creative
---

Imagine your trusted AI assistant is writing important emails or answering customer inquiries in real-time. How can you ensure the AI is making the right decisions and not making mistakes or outputting sensitive security information?

Until now, we had to use another smart AI (an LLM judge) to act as a "judge" and inspect every action one by one. It was like submitting every report to a judge and waiting for a verdict. However, this process is incredibly slow and expensive. Consequently, most companies barely manage to verify a small fraction of their total operations. [Source: Openlayer releases jevals — a fraction-of-a-cent replacement for LLM judges](https://mlllm.io/news/3263-openlayer-releases-jevals-a-fraction-of-a-cent-replacement-for-llm-judges/)

A new tool, **jevals**, has arrived to solve these concerns. [Source: Show HN: jevals – replacing LLM judges with typed Jev decisions](https://www.simpleprog.com/news/show-hn-jevals-replacing-llm-judges-with-typed-jev-decisions-a2a2ea30)

## Why does this matter?

As AI agents become more deeply embedded in our lives, the process of verifying that they are making the right decisions becomes increasingly important. It has evolved beyond simply using high-performance models into an "safety belt" to prevent those models from making mistakes.

Relying on spot-checking a tiny fraction of total tasks makes it difficult to catch all the potential catastrophic errors that could occur later. Because jevals is fast and cheap enough to verify every task, it allows systems to detect mistakes and protect users before an AI acts on them. [Source: GitHub - openlayer-ai/jevals: Agent evals and guardrails as ...](https://github.com/openlayer-ai/jevals)

## Understanding jevals: From 'Judge' to 'Checklist'

Let's rethink the traditional 'LLM Judge' approach. It is like sending a long-form essay to a judge detailing an AI's behavior and asking them to "decide if this is correct." Because the judge has to read and interpret the text, it is slow and costly. [Source: Introducing jevals: typed decisions for agent evals and ...](https://www.openlayer.com/blog/introducing-jevals-agent-evals-guardrails)

In contrast, the 'Jev' model used by jevals is a **'System One'** model. Simply put, instead of reading long sentences and pondering, it answers predefined questions with a simple "Yes/No" or a numerical value. To use an analogy: instead of a human reading and grading long-form answers, it is like a machine grading an OMR sheet for a multiple-choice test in 0.5 seconds. [Source: Jevals· independent Jev benchmark for models that decide](https://jevals.com/)

By 'typing' the answers and processing them all at once, it is much faster and dramatically cheaper. It processes up to nine inspection items in a single communication while incurring a very low cost of only $0.00006 per trace (unit of work). [Source: Openlayer Releases jevals: AI Agent Evaluation for a Fraction ...](https://mlllm.io/articles/3263-openlayer-releases-jevals-ai-agent-evaluation-for-a-fraction-of-a-cent-instead-of-an-expensive-llm-judge/)

## Current Status: Fast, but occasionally confused

jevals is highly efficient. You can run more than 40 evaluation questions per AI task, and the total cost remains negligible. [Source: jevals: An Evals Platform Built Around Typed Judges](https://aiskill.market/blog/jevals-evals-platform-for-typed-judges)

However, not everything in the world is a multiple-choice question. The Jev model is not 100% perfect in situations requiring the understanding of complex and subtle conversational context. While it boasts high accuracy of over 96% for simple 'Yes/No' decisions, its accuracy can drop to the 80% range for problems where various rules are complexly intertwined. [Source: We Tried Replacing Our LLM Judges With Jev - DEV Community](https://dev.to/ialijr/we-tried-replacing-our-llm-judges-with-jev-1en7)

Interestingly, the tool provides a 'probability' score when it is unsure of its answer. It honestly states, "I am only about 60% confident in this judgment." Developers can use this probability information to design smarter systems that only ask a more intelligent (and expensive) LLM when the initial answer is deemed ambiguous. [Source: We Tried Replacing Our LLM Judges With Jev - DEV Community](https://dev.to/ialijr/we-tried-replacing-our-llm-judges-with-jev-1en7)

## What lies ahead?

As AI agents take on more complex and important tasks, these light and fast validation tools will become essential items for developers. While developers are currently using them in local environments (like MacBooks) or simple cloud services, they are expected to play a crucial role as reliable safety measures for AI in large-scale enterprise environments in the future. [Source: jevals| System One Models](https://systemonemodels.org/examples/tools/jevals/)

### MindTickleBytes AI Reporter's Take
While the performance of AI agents is important, it is impressive to see that the method for verifying their decisions is changing from a "high-level judicial trial" to "efficient inspection." Ultimately, as much as AI becomes smarter, the technology that quickly catches AI errors will make the AI era safer and more trustworthy.

## References

1. [jevals- AI Agent Eval Library Python | EveryDev.ai](https://www.everydev.ai/tools/jevals)
2. [Jevals· independent Jev benchmark for models that decide](https://jevals.com/)
3. [jevals| System One Models](https://systemonemodels.org/examples/tools/jevals/)
4. [Show HN: jevals – replacing LLM judges with typed Jev decisions](https://www.simpleprog.com/news/show-hn-jevals-replacing-llm-judges-with-typed-jev-decisions-a2a2ea30)
5. [GitHub - openlayer-ai/jevals: Agent evals and guardrails as ...](https://github.com/openlayer-ai/jevals)
6. [Introducing jevals: typed decisions for agent evals and ...](https://www.openlayer.com/blog/introducing-jevals-agent-evals-guardrails)
7. [We Tried Replacing Our LLM Judges With Jev - DEV Community](https://dev.to/ialijr/we-tried-replacing-our-llm-judges-with-jev-1en7)
8. [jevals: An Evals Platform Built Around Typed Judges](https://aiskill.market/blog/jevals-evals-platform-for-typed-judges)
9. [Openlayer releases jevals — a fraction-of-a-cent replacement for LLM judges](https://mlllm.io/news/3263-openlayer-releases-jevals-a-fraction-of-a-cent-replacement-for-llm-judges/)
10. [Openlayer Releases jevals: AI Agent Evaluation for a Fraction ...](https://mlllm.io/articles/3263-openlayer-releases-jevals-ai-agent-evaluation-for-a-fraction-of-a-cent-instead-of-an-expensive-llm-judge/)