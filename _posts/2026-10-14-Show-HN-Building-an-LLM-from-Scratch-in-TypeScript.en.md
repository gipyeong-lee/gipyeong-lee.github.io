---
layout: post
title: "Can AI 'summarize' research papers? You'll know if you build an AI brain yourself"
description: "Curious about how Large Language Models (LLMs) work? An educational project that builds AI from scratch using TypeScript, demystifying what feels like a black box, is gaining attention."
summary: "Beyond simply using AI, educational efforts to understand the principles by coding core technologies like Transformers and Attention mechanisms from scratch in TypeScript are gaining traction."
tags: [AI, LLM, TypeScript, Education, Developers]
image: 2026-10-14-Show-HN-Building-an-LLM-from-Scratch-in-TypeScript.jpg
image_alt: "An image representing the process of visualizing and understanding the structure of an AI model on a coding screen"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Understanding AI as a 'mathematical structure' rather than 'magic' is a vital process for modern developers. Implementing it yourself will make the black box transparent."
quiz:
  - question: "What is the primary purpose of projects that build LLMs from scratch?"
    choices: ["To create a top-performing commercial model", "Educational purposes to learn the principles of AI", "To develop a model 10 times faster than existing ones"]
    answer: 1
    explanation: "Recent projects focus on the educational value of implementing and understanding the core mechanisms by which AI operates, rather than real-world performance."
  - question: "What is the advantage of implementing the Attention mechanism yourself?"
    choices: ["You can train on more data", "GPU costs are reduced", "You can view AI as an object of structural understanding, not a black box"]
    answer: 2
    explanation: "By manually implementing components like causal masks, you can fundamentally understand how AI grasps context."
  - question: "What are the limitations of a Transformer model trained from scratch?"
    choices: ["Zero language comprehension", "It can continue text, but inference or following instructions is difficult", "It is too slow"]
    answer: 1
    explanation: "Models in the early stages of training have the ability to continue text, but require additional tuning to follow human instructions or perform complex inference."
lang: en
ref: 2026-10-14-Show-HN-Building-an-LLM-from-Scratch-in-TypeScript
audio: 2026-10-14-Show-HN-Building-an-LLM-from-Scratch-in-TypeScript.en.mp3
industry: creative
---

Imagine this: The AI assistant you use every day suddenly says, "From today, I'll explain why I give you these answers." In fact, for many, the Large Language Models (LLMs) we currently use are like "black boxes" that answer anything. For those who have been curious about exactly what happens inside and how words are connected, an interesting movement is rising among developers recently. It is about **coding AI from scratch** rather than calling it from an external source.

### Why is this important?

As AI technology advances rapidly, we have gradually begun to treat AI not as a tool, but as a "living being" or "magic." However, AI is ultimately just a complex calculator made of math and code. Especially for developers, understanding the internal working principles of AI is now becoming an essential technical insight, moving beyond simple curiosity. Guides that implement LLMs using TypeScript, such as the "Node-LLM" project, help developers turn the operation of AI models from a black box into a transparent logical structure [Source 1](https://book.humanexperiences.io/), [Source 3](https://zeli.app/zh/story/50085332). This serves as a significant stepping stone, moving beyond being a user of AI to being able to design how AI thinks.

### Understanding it simply

Understanding the Transformer, the core structure of AI (an AI architecture that grasps the relationships between words in a sentence), is like putting together a puzzle. For example, the process of implementing the Attention mechanism yourself is the work of creating rules that determine which words AI should "focus" on in a sentence [Source 13](https://rutube.ru/video/65bc64a2ed5b1b16fe86118bded16c96/), [Source 14](https://www.linkedin.com/pulse/building-llm-from-scratch-part-2-6-attention-how-tokens-imamovich-2orce).

To use a simple analogy, if you manually write in code the "causal mask" (a device that blocks AI from seeing future words in advance) or "head-slicing" (a technique that processes information by dividing it into several layers), which the libraries we use usually do for us, you finally realize how AI reads the context between words [Source 13](https://rutube.ru/video/65bc64a2ed5b1b16fe86118bded16c96/). It is like having only ever bought and eaten bread, versus experiencing the process of kneading and fermenting flour yourself to understand the structure of bread. In the early stages, you start with a Tokenizer (a tool that turns sentences into numbers that AI can understand), and then progress to a complex Transformer through a simple model [Source 7](https://www.linkedin.com/pulse/building-llm-from-scratch-part-2-6-attention-how-tokens-imamovich-2orce).

### Where do we stand?

Many learning projects are currently underway, but there is one fact you should be clearly aware of: a model trained this way cannot immediately replace high-performance AI such as "Claude" or "Gemini" [Source 9](https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/), [Source 12](https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/).

While a Transformer model trained in the early stages gains the ability to continue text plausibly, it often lacks the ability to infer complex questions thrown by users or follow instructions accurately [Source 11](https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/). To gain these abilities, much more complex steps called "Post-Training" and "Alignment" (the process of adjusting AI's answers to match human intent) are additionally required [Source 11](https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/). In other words, an LLM built from scratch is an excellent educational process for learning the basic principles that make up the "brain" of AI, but it is not a stage that pursues practical performance [Source 7](https://www.linkedin.com/pulse/building-llm-from-scratch-part-2-6-attention-how-tokens-imamovich-2orce), [Source 9](https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/).

### What can we expect in the future?

The attempt to understand the structure of AI from scratch will continue. It appears that more developers will lower the technical barriers to AI by implementing models that can be trained with just a CPU [Source 21](https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/). This process will become foundational knowledge for building better AI services. Now, we are moving beyond the era of simply admiring the results of AI, and efforts to understand what algorithms and mathematical data flows those results are born from will become more important.

### Perspective from a MindTickleBytes AI Reporter

We talk to AI every day, but we have had few opportunities to learn how AI talks. The process of building AI from scratch through coding returns AI from being a "mysterious existence" to "technology we can design and improve." Why not stop calling AI magic and open up the engine inside it yourself?

## References

1. Building an LLM in NodeJS | Building an LLM in NodeJS (https://book.humanexperiences.io/)
2. Node-LLM - Build LLMs from Scratch · Hacker News | Zeli (https://zeli.app/story/50085332)
3. node-llm: 从零构建大型语言模型指南 — Show HN: Building an LLM fro... (https://zeli.app/zh/story/50085332)
4. GitHub - Maugun/llm-from-scratch-ts: A pedagogical mini LLM ... (https://github.com/Maugun/llm-from-scratch-ts)
5. I Trained My Own LLM from Scratch in 2025: What That Viral HN... (https://dev.to/jtorchia/i-trained-my-own-llm-from-scratch-in-2025-what-that-viral-hn-tutorial-doesnt-tell-you-about-the-l66)
6. TrainLLMFromScratch (https://fareedkhan-dev.github.io/train-llm-from-scratch/)
7. BUILDING AN LLM FROM SCRATCH · PART 2 OF 6 Attention: How... (https://www.linkedin.com/pulse/building-llm-from-scratch-part-2-6-attention-how-tokens-imamovich-2orce)
8. 3) Build an LLM from Scratch 3: Coding attention mechanisms (https://rutube.ru/video/65bc64a2ed5b1b16fe86118bded16c96/)
9. Build and Train a 25M Parameter LLM From Scratch on Your CPU (https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/)