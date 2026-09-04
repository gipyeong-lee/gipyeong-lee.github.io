---
layout: post
title: "我的浏览器能直接运行 AI？通过 Three-LLM 看 Web AI 的未来"
description: "介绍在 Web 浏览器中无需服务器即可运行 AI 模型的 WebLLM 及 Three-LLM 技术。"
summary: "通过 Three-LLM 和 WebLLM 技术，无需连接服务器，AI 直接在用户 PC 浏览器中运行的时代正在开启。"
tags: [AI, WebGPU, Three.js, Three-LLM, WebLLM]
image: 2026-09-04-Three-LLM-Three-js-based-WebGPU-LLM-inference-engine.jpg
image_alt: "一幅科技数字艺术图，展示了人工智能在 Web 浏览器环境中通过 GPU 加速运行的情景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这是一个从服务器中心化 AI 时代迈向用户设备中心化 AI 时代的重要转折点。它在隐私保护和成本降低方面具有巨大的潜力。"
quiz:
  - question: "Three-LLM 运行模型的核心技术是什么？"
    choices: ["Python 脚本", "Three.js TSL 计算着色器", "云端 API"]
    answer: 1
    explanation: "Three-LLM 将模型的推理图转换为 Three.js TSL (Three.js Shading Language) 计算着色器，并在 WebGPU 上执行。"
  - question: "WebLLM 的实现语言是什么？"
    choices: ["C++", "Python", "JavaScript"]
    answer: 2
    explanation: "与大多数推理引擎采用 C++ 或 Python 实现不同，WebLLM 是一个使用 JavaScript 实现的开源框架。"
  - question: "在 Web 浏览器内运行 AI 的主要优点是什么？"
    choices: ["无需联网即可始终运行", "无需服务器处理且降低了网络延迟", "模型大小可以无限增长"]
    answer: 1
    explanation: "在本地浏览器中运行 AI 无需服务器处理，且消除了网络往返时间，从而可以降低延迟。"
lang: zh-cn
ref: 2026-09-04-Three-LLM-Threejs-based-WebGPU-LLM-inference-engine
---

想象一下：在没有互联网的咖啡馆里，你打开笔记本电脑，要求 AI 总结一份长长的会议资料。过去，你可能需要盯着那个在网页上转圈的加载图标，等待 AI 连接云端服务器（Cloud Server，远程连接到互联网的计算机）进行处理；但现在，它会像变魔术一样立刻给出回答。因为你的笔记本电脑本身就已经拥有了一个微型的“AI 大脑”。最近出现的“Three-LLM”和“WebLLM”等技术，正在让这种魔法变为现实。

## 这为何重要？(Why It Matters)

到目前为止，我们使用的大多数 AI 都是通过接收位于巨大服务器机房中的超级计算机所处理的结果来实现的。但这带来了一些问题。

首先，维持服务器需要高昂的成本；其次，服务器距离越远，响应速度就越慢；第三，用户的敏感数据必须通过网络传输到服务器，这引发了对个人隐私保护的担忧。这就像为了吃上一顿美味的饭菜，必须每次都跑去很远的餐厅一样。

这些全新的 Web 技术完全改变了游戏规则。当 Web 浏览器可以直接运行 AI 时，不仅无需服务器费用，所有计算都在你的电脑内完成，信息外泄的风险也随之降低。此外，由于无需网络加载时间，AI 能够实现即时响应，使用体验也将更加流畅。[参考资料 5](https://tianpan.co/blog/2026/04/17/browser-native-llm-inference-webgpu)

## 通俗易懂的解释 (The Explainer)

Web 浏览器是如何运行如此智能的 AI 的呢？核心在于名为“WebGPU”的技术。

简单来说，传统的 Web 浏览器就像是一个只能进行简单计算的“普通文员”。而 WebGPU 则相当于给浏览器配备了一个强大的“图形专用计算器”。该计算器专门用于处理复杂的图形绘制，或者并行（同时处理多个任务）完成 AI 的复杂数学计算。

Three-LLM 进一步将模型的数学结构（推理图）转换为 Three.js 可以理解的“着色器（Shader，GPU 专用程序）”。[参考资料 8](https://ben3d.ca/blog/running-llms-in-the-browser-with-threejs) 打个比方，就像是将 AI 理解的数学语言“翻译”成计算机图形理解的语言，然后直接运行。

另一方面，WebLLM 是一个完全用 JavaScript（让网页动起来的标准语言）实现的框架。[参考资料 4](https://ar5iv.labs.arxiv.org/html/2412.15803) 它就像在浏览器中植入了另一个独立的“AI 操作系统”，当 AI 计算过于繁重时，它会将任务交给专门的“工作线程（Web Worker）”来处理，从而确保浏览器页面不会卡死。[参考资料 6](https://webllm.mlc.ai/docs/)

## 现状 (Where We Stand)

目前，这些技术正在迅速发展。Three-LLM 已经成功在 Web 浏览器环境中直接运行了 GPT-2、SmolLM2、Qwen 和 Phi 等语言模型。[参考资料 8](https://ben3d.ca/blog/running-llms-in-the-browser-with-threejs) 此外，作为一个开源项目，WebLLM 为开发人员提供了与 OpenAI 相同方式（API）的工具，以便任何人都能轻松地将 AI 功能集成到自己的网站中。[参考资料 2](https://webllm.mlc.ai/), [参考资料 9](https://arxiv.org/html/2412.15803v2)

不过，要让目前智能手机上使用的那种千亿参数（AI 的智能衡量标准）级别的超大型模型立即在浏览器中运行，还有一定困难。目前，主要是那些针对浏览器环境优化过的、轻量级且高效的 AI 模型被广泛应用。这就像是用快捷灵活的摩托车替代了笨重的货车。

## 未来展望 (What's Next)

未来，我们访问的所有网站都将“内置” AI。现在我们需要打开浏览器并单独访问 AI 服务，但不久之后，网站本身就将具备智能。当你对网站说“调节这张照片的亮度”时，它不再需要询问服务器，而是直接在浏览器内即时修图；或者由浏览器读取长文并为你生成摘要，这些功能将成为标配。随着 Web 技术的发展，我们所认知的 Web 浏览器将成为一个庞大的人工智能工具箱。[参考资料 9](https://arxiv.org/html/2412.15803v2), [参考资料 10](https://arxiv.org/html/2412.15803v1)

## MindTickleBytes AI 记者视点

不再将 AI 束缚在服务器上，而是将其带入我们手中的浏览器，这是技术自主化的开端。开发者们终于迎来了一个新时代，他们无需再为高昂的云端成本而忧虑，即可为用户提供强大的 AI 体验。就像在自家客厅就能解决一切烦恼一样，AI 也向我们迈近了一步。

## 参考资料

1. [Three-LLM—WebGPULLMEngine](https://three-llm.ben3d.ca/)
2. [WebLLM: High-Performance In-BrowserLLMInferenceEngine](https://webllm.mlc.ai/)
3. [I RanThreeLLMs Entirely in the Browser to Power an AI Coaching Feature - DEV Community](https://dev.to/refactory/i-ran-three-llms-entirely-in-the-browser-to-power-an-ai-coaching-feature-heres-what-i-measured-9jm)
4. [WebLLM: A High-Performance In-BrowserLLMInferenceEngine](https://ar5iv.labs.arxiv.org/html/2412.15803)
5. [Browser-NativeLLMinference: TheWebGPUEngineeringYou...](https://tianpan.co/blog/2026/04/17/browser-native-llm-inference-webgpu)
6. [Welcome to WebLLM —web-llm0.2.84 documentation](https://webllm.mlc.ai/docs/)
7. [mlc-ai/web-llm: High-performance In-browserLLMInferenceEngine...](https://github.com/mlc-ai/web-llm)
8. [Running LLMs in the Browser with Three.js - ben3d.ca](https://ben3d.ca/blog/running-llms-in-the-browser-with-threejs)
9. [WebLLM: A High-Performance In-Browser LLM Inference Engine](https://arxiv.org/html/2412.15803v2)
10. [WebLLM: A High-Performance In-Browser LLM Inference Engine](https://arxiv.org/html/2412.15803v1)