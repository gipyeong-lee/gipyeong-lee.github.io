---
layout: post
title: "不需要我的电脑也行？在 Hetzner 服务器上直接运行 AI 模型"
description: "没有高性能显卡也能运行自己的 AI 模型吗？了解如何利用 Hetzner 服务器直接部署和运行 AI 模型。"
summary: "介绍了如何利用 Hetzner 服务器的 GPU 和 CPU 环境高效运行个人 AI 模型，并解释了其核心原理。"
tags: [AI, Hetzner, 服务器, LLM, 基础设施]
image: 2026-07-24-Hetzner-is-working-on-LLM-Inference.jpg
image_alt: "数据中心内整齐排列的服务器机架"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "像 Hetzner 这样的基础设施供应商加强 AI 专用环境，将有力地帮助个人开发者掌握大语言模型的主动权。"
quiz:
  - question: "在 Hetzner 服务器上不使用 GPU 运行 AI 模型时，主要需要考虑什么？"
    choices: ["模型的参数数量与服务器的内存容量", "服务器的网速", "显示器的分辨率"]
    answer: 0
    explanation: "基于 CPU 的推理对模型规模很敏感，需要充足的内存（RAM）和较快的处理速度支撑。"
  - question: "拥有 96GB VRAM 的服务器主要适合什么工作？"
    choices: ["简单的网页浏览", "运行及微调 70B 以上的大规模模型", "压缩图像文件"]
    answer: 1
    explanation: "96GB VRAM 不仅足以运行大规模模型，还能处理多用户并发访问以及模型的微调（Fine-tuning）。"
  - question: "为了运行 AI 模型，通常需要在 Hetzner 服务器上安装什么服务？"
    choices: ["办公软件", "Ollama 或 vLLM 等服务框架", "杀毒软件"]
    answer: 1
    explanation: "Ollama 或 vLLM 是核心服务框架，用于加载 AI 模型并通过 API 提供外部调用。"
lang: zh-cn
ref: 2026-07-24-Hetzner-is-working-on-LLM-Inference
---

想象一下：早晨醒来，连接到你的个人服务器，输入命令：“总结一下今天的主要新闻”。这并非来自大公司的云服务，而是你在自己租用的服务器上，让私有的 AI 生成逻辑回复。过去，这似乎是拥有强大图形处理器（GPU）的专家们的专利，但现在情况已有所不同。今天，我们就来看看如何利用德国知名服务器厂商 Hetzner 来运行属于你自己的 AI 模型。

## 这为什么重要？

AI 早已超越了单纯的玩具，成为商业和日常生活中的必备工具。然而，有时我们并不愿意将数据完全托付给大企业的外部服务，因此直接在本地或私有服务器上运行模型的需求日益增长。这被称为推理（Inference，即 AI 模型根据所学内容实时生成回复的过程）。[出处 11](https://huggingface.co/blog/Kseniase/inference) 使用 Hetzner 等托管服务，你可以无需购买昂贵的硬件，就能以合理的成本拥有自己的“AI 引擎”。[出处 6](https://supa.works/hetzner-ai-hosting)

## 浅显易懂：如何为 AI 租赁“舞台”

运行 AI 模型就像准备一场演出。模型是演员，而服务器就是模型活动的舞台。

**1. GPU 服务器（专业舞台）：** 配备高性能图形处理器（GPU）的服务器就像最高级的剧院。对于需要同时处理海量数据的专业 AI 任务来说，这是必不可少的。[出处 5](https://effloow.com/articles/hetzner-cloud-ai-gpu-server-guide-2026) 例如，一台拥有 96GB VRAM（显存）的服务器，完全能够轻松运行参数量超过 700 亿的超大模型。[出处 5](https://effloow.com/articles/hetzner-cloud-ai-gpu-server-guide-2026)

**2. CPU 服务器（小型排练室）：** 那么，没有 GPU 就真的不能运行 AI 了吗？并非如此。只要有足够的内存（RAM）和快速的磁盘性能，仅依靠计算机的大脑——CPU 也能进行推理。[出处 1](https://codref.org/rated-d/run-llm-on-hetzner/) 虽然它仅限于参数量在 70 亿以下的小型模型，但作为创建轻量级对话 AI 的替代方案，这已经足够了。[出处 6](https://supa.works/hetzner-ai-hosting)

租赁服务器后，通常需要安装 Ollama 或 vLLM 等服务框架。[出处 6](https://supa.works/hetzner-ai-hosting) 它们就像演出总监，负责将模型部署到服务器上，并创建 API（数据交换通道），使用户可以通过提问来获取回复。[出处 3](https://community.hetzner.com/tutorials/ai-chatbot-with-ollama-and-libre-webui/)

## 现状

目前，Hetzner 提供多种选择，从基础的云实例到搭载顶级 RTX 6000 Ada（48GB VRAM）的专用 GPU 服务器应有尽有。[出处 5](https://effloow.com/articles/hetzner-cloud-ai-gpu-server-guide-2026), [出处 6](https://supa.works/hetzner-ai-hosting) 特别是在开发者群体中，已经出现了可以评估特定规格模型能否在特定服务器环境中运行的计算工具，极大地降低了门槛。[出处 5](https://effloow.com/articles/hetzner-cloud-ai-gpu-server-guide-2026) 不过需要记住，如果选择 CPU 服务器，能够运行的模型大小会有明确限制。[出处 6](https://supa.works/hetzner-ai-hosting)

## 未来前景

得益于技术进步，AI 推理成本每年正在以约 10 倍的速度下降。[出处 13](https://a16z.com/llmflation-llm-inference-cost/) 未来，能够在更少内存下运行更巨大模型的“优化技术”将变得普及。今天介绍的 CPU 推理方式也在朝着通过软件克服硬件瓶颈的方向发展，不久之后，我们将能够实现在更小的服务器上运行具备相当智能水平的个人 AI 助理。

---

### MindTickleBytes 的 AI 记者视角
随着计算资源伴随云基础设施的发展而大众化，AI 的主动权已不再是大企业的专利，而是成了个人的选择。通过 Hetzner 等服务尝试运行自己的 AI，不仅是技术上的好奇心尝试，更是为了数据保护和定制化应用而迈出的重要一步。

## 参考资料

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