---
layout: post
title: "Is it okay if it's not my computer? Running AI models directly on Hetzner servers"
description: "Can you run your own AI models without a high-performance graphics card? We explore how to run AI models directly using Hetzner servers."
summary: "This article explains how to efficiently run your own AI models using the GPU and CPU environments of Hetzner servers, along with the core principles behind it."
tags: [AI, Hetzner, Server, LLM, Infrastructure]
image: 2026-07-24-Hetzner-is-working-on-LLM-Inference.jpg
image_alt: "Server racks in a data center neatly arranged"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Strengthening AI-specific environments by infrastructure providers like Hetzner will be a major boost for individual developers to secure sovereignty over large language models."
quiz:
  - question: "What is the primary consideration when running an AI model on a Hetzner server without a GPU?"
    choices: ["The number of model parameters and the server's RAM capacity", "The server's internet speed", "The monitor's resolution"]
    answer: 0
    explanation: "For CPU-based inference, the size of the model is critical, and it must be supported by sufficient memory (RAM) and fast processing speeds."
  - question: "What tasks are servers with 96GB of VRAM primarily suitable for?"
    choices: ["Simple web browsing", "Running and fine-tuning large models over 70B", "Compressing image files"]
    answer: 1
    explanation: "96GB of VRAM is sufficient not only for running large-scale models but also for handling concurrent connections from multiple users and model fine-tuning."
  - question: "What are the common services installed on Hetzner servers to run AI models?"
    choices: ["Office programs", "Serving frameworks like Ollama or vLLM", "Antivirus software"]
    answer: 1
    explanation: "Ollama or vLLM are core serving frameworks that allow you to load AI models and make them usable externally via APIs."
lang: en
ref: 2026-07-24-Hetzner-is-working-on-LLM-Inference
audio: 2026-07-24-Hetzner-is-working-on-LLM-Inference.en.mp3
industry: education
---

Imagine this: You wake up in the morning, connect to your personal server, and command it, "Summarize today's main news." Instead of using a big tech company's cloud service, your own AI, running on a server you rented yourself, logically generates an answer. In the past, this seemed like the exclusive domain of experts who owned very powerful graphics cards (GPUs), but now things are a bit different. Today, we look at how to run your own artificial intelligence models using Hetzner, a famous German server company.

## Why is this important?

AI has moved beyond being a mere toy to becoming an essential tool for business and daily life. However, there are times when you might be reluctant to entrust all your data to the external services of giant corporations. That's why there is an increasing attempt to run models independently. This is called Inference (the process where an AI model generates real-time answers based on what it has learned). [Source 11](https://huggingface.co/blog/Kseniase/inference) By using hosting services like Hetzner, you can own your own 'AI engine' at a cost-effective price without having to buy expensive hardware yourself. [Source 6](https://supa.works/hetzner-ai-hosting)

## Understanding it easily: How to rent a 'stage' for AI

Running an AI model is similar to preparing a performance. The model is the performer, and the server is the stage where the model performs.

**1. GPU Server (Professional Stage):** A server equipped with a high-performance graphics card (GPU) is like a top-tier theater. It is essential for professional AI tasks that require processing vast amounts of data simultaneously. [Source 5](https://effloow.com/articles/hetzner-cloud-ai-gpu-server-guide-2026) For example, a server with 96GB of VRAM (memory for graphics cards) can easily run large models with over 70 billion parameters (units used to store AI knowledge). [Source 5](https://effloow.com/articles/hetzner-cloud-ai-gpu-server-guide-2026)

**2. CPU Server (Small Rehearsal Room):** So, can't you run AI without a GPU? No. If you have enough memory (RAM) and fast disk performance, inference is possible using just the CPU, the computer's brain. [Source 1](https://codref.org/rated-d/run-llm-on-hetzner/) Of course, it is limited to smaller models with fewer than 7 billion parameters, but it is a sufficient alternative for creating lightweight conversational AI. [Source 6](https://supa.works/hetzner-ai-hosting)

After renting a server, you typically install serving frameworks like 'Ollama' or 'vLLM'. [Source 6](https://supa.works/hetzner-ai-hosting) These act like a performance director, loading the model onto the server and creating an API (a channel to exchange data) that retrieves answers when a user asks a question. [Source 3](https://community.hetzner.com/tutorials/ai-chatbot-with-ollama-and-libre-webui/)

## Current Situation

Currently, Hetzner offers a variety of options, from basic cloud instances to dedicated GPU servers equipped with top-of-the-line RTX 6000 Ada (48GB VRAM) cards. [Source 5](https://effloow.com/articles/hetzner-cloud-ai-gpu-server-guide-2026), [Source 6](https://supa.works/hetzner-ai-hosting) Accessibility has greatly improved, especially as developer communities share calculator tools that allow you to gauge whether a model with specific specifications will run in your server environment. [Source 5](https://effloow.com/articles/hetzner-cloud-ai-gpu-server-guide-2026) However, you should keep in mind that if you choose a CPU server, there is a clear limit to the size of the models you can run. [Source 6](https://supa.works/hetzner-ai-hosting)

## What will happen in the future?

AI inference costs are decreasing by about 10 times every year due to technological advancements. [Source 13](https://a16z.com/llmflation-llm-inference-cost/) In the future, 'optimization technologies' that allow larger models to be run with less memory will become widespread. The CPU inference method introduced today is also evolving in a direction that overcomes hardware limitations with software, so the day will soon come when you can operate an AI with decent intelligence as a personal assistant, even on smaller servers.

---

### MindTickleBytes AI Reporter's Opinion
As computing resources become popularized alongside the advancement of cloud infrastructure, AI sovereignty is no longer the exclusive domain of giant corporations but has become an option for individuals. Attempts to run your own AI through services like Hetzner are more than just technical curiosity; they will be an important step forward for data protection and customized utilization.

## References

1. [Run your LLM on Hetzner dedicated servers | codref.org](https://codref.org/rated-d/run-llm-on-hetzner/)
2. [Deploy a Private AI Chat Interface with Libre WebUI and Ollama on a GPU Server | Hetzner Community](https://community.hetzner.com/tutorials/ai-chatbot-with-ollama-and-libre-webui/)
3. [AI inference server setup for Hetzner GEX44 GPU server | GitHub](https://github.com/digital-memory-lab/ai-server-setup)
4. [Hetzner Cloud for AI: GPU Server Setup and Cost Guide 2026 | Effloow](https://effloow.com/articles/hetzner-cloud-ai-gpu-server-guide-2026)
5. [Hetzner AI Hosting – GPU Cloud Instances & Availability | SUPA](https://supa.works/hetzner-ai-hosting)
6. [Running the AI chatbot DeepSeek with Ollama | Hetzner Community](https://community.hetzner.com/tutorials/ai-chatbot-with-ollama-and-deepseek/)
7. [HeteGen: Heterogeneous Parallel Inference for Large LLMs | MLSys 2024](https://proceedings.mlsys.org/paper_files/paper/2024/file/5431dca75a8d2abc1fb51e89e8324f10-Paper-Conference.pdf)
8. [AI-Chatbot DeepSeek mit Ollama ausführen | Hetzner Community](https://community.hetzner.com/tutorials/ai-chatbot-with-ollama-and-deepseek/de/)
9. [Запуск LLM на CPU без GPU | AiManual](https://ai-manual.ru/article/cpu-only-inferens-llm-polnoe-rukovodstvo-po-optimizatsii-skorosti-i-pamyati-bez-videokartyi/)
10. [Topic 23: What is LLM Inference, its challenges and solutions | Hugging Face Blog](https://huggingface.co/blog/Kseniase/inference)
11. [TensorRT-LLM: NVIDIA Inference Optimization | GitHub](https://github.com/NVIDIA/TensorRT-LLM)
12. [Welcome to LLMflation - LLM inference cost is going down fast | a16z](https://a16z.com/llmflation-llm-inference-cost/)
13. [Groq is fast, low cost inference | Groq.com](https://groq.com/)
14. [Mastering LLM Techniques: Inference Optimization | NVIDIA Technical Blog](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/)
15. [LLM Inference Hardware Needs Memory, Not More Compute | OraCore.dev](https://oracore.dev/en/news/llm-inference-hardware-memory-interconnect-en)