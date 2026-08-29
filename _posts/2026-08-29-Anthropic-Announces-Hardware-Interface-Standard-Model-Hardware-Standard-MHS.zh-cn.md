---
layout: post
title: "AI 操控机械臂？“模型硬件标准（MHS）”闪亮登场"
description: "安索比（Anthropic）发布的模型硬件标准（MHS）将 AI 代理与物理设备相连接，本文为您简要解读它将如何改变科学研究和制造现场。"
summary: "安索比开发的全新标准“MHS”使各类设备能够与 AI 进行通信，为 AI 在无需复杂编程的情况下安全控制实验室机器人或显微镜铺平了道路。"
tags: [AI, 安索比, MHS, 机器人技术, 技术趋势]
image: 2026-08-29-Anthropic-Announces-Hardware-Interface-Standard-Model-Hardware-Standard-MHS.jpg
image_alt: "AI 代理集成控制各类科学研究设备的构想图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "试图将复杂的设备统一为一种语言，这将成为 AI 从数字世界迈向物理世界的关键阶梯。"
quiz:
  - question: "模型硬件标准（MHS）的最大特点是什么？"
    choices: ["仅适用于安索比的 AI 模型 Claude", "无论设备类型如何，AI 都能以标准化方式进行控制", "无需 AI，由人类直接控制机器人的方式"]
    answer: 1
    explanation: "MHS 是一个模型无关（model-agnostic，即不依赖于特定 AI 模型）的标准，无论使用哪种 LLM，都能通过标准化的接口连接并控制各种物理设备。"
  - question: "MHS 是基于什么技术构建的？"
    choices: ["区块链技术", "数据源连接标准：模型上下文协议（MCP）", "物联网专用 5G 网络"]
    answer: 1
    explanation: "MHS 是在安索比于 2024 年推出的数据源连接标准——模型上下文协议（MCP）的基础上构建的。"
  - question: "通过 MHS 可以预期到什么效果？"
    choices: ["AI 代理完全取代所有人类劳动", "无需为每台设备编写专用代码，实现高效控制", "AI 能够自主发明新型硬件"]
    answer: 1
    explanation: "使用 MHS 后，专家们无需为每台设备编写专用代码，AI 代理即可通过标准化指令安全地操作机器人、显微镜等各种设备。"
lang: zh-cn
ref: 2026-08-29-Anthropic-Announces-Hardware-Interface-Standard-Model-Hardware-Standard-MHS
---

想象一下：实验室里的显微镜、搬运样品的机械臂、精密激光设备仿佛一个团队般自行运作，共同完成实验。以往，若想将这些设备连接到 AI，工程师必须为每台设备逐一编写专用代码。这就像是为讲不同语言的人们各配一名翻译官，极其低效。

然而，最近 AI 企业安索比（Anthropic）给这个复杂的难题带来了解决方案。这就是 **模型硬件标准（Model Hardware Standard，简称 MHS）**。

## 为什么它很重要？

如果说之前的 AI 仅停留在阅读文本和回答问题的水平，那么现在，它正迈向直接操控现实物理设备的阶段。在科学研究和高端制造领域，安索比决定为 AI 代理（具备自主规划和执行能力的 AI）提供一套标准化的驱动程序，以便它们能够安全、轻松地控制各种设备([参考资料 1](https://arstechnica.com/ai/2026/08/anthropics-new-hardware-standard-lets-ai-agents-control-the-physical-world/))。

这不仅是便利性的问题。当科学家研发新药或进行复杂化学反应实验时，这意味着他们可以减少操作设备的时间，专注于“研究成果”。简单来说，就像用一个万能遥控器控制家中复杂的家电一样，AI 现在能够通过标准化的接口操控实验室里复杂的设备([参考资料 2](https://www.cnbc.com/2026/08/27/anthropic-pushes-into-physical-world-with-new-standard-to-help-ai-agents-operate-machines.html))。

## 通俗解释

打个比方：过去，显微镜说的是“显微镜语”，机械臂说的是“机械臂语”，AI 若想与它们沟通，必须分别学习这些语言。如果设备有 100 台，就得雇 100 名翻译官。

但 MHS 为这些设备创造了一种“通用语言”。通过使用“读取（Read）”、“移动（Move）”等标准化指令，无论设备类型如何，AI 都能直接下达命令([参考资料 4](https://fortune.com/2026/08/27/anthropic-makes-first-move-into-physical-ai-with-universal-standard-for-scientists-manufacturing/))。得益于此，专家们无需再费心为每台设备编写专用代码。AI 代理能够高效地处理操控机械臂、精密对准激光或进行蛋白质分析等过程([参考资料 8](https://byteiota.com/anthropic-model-hardware-standard-physical-ai/))。

特别重要的一点是，MHS 是 **模型无关（model-agnostic，即不依赖于特定 AI 模型）** 的。也就是说，不仅安索比自家的 AI 模型“Claude”可以使用，OpenAI 的模型或其他开源 AI 模型也同样能使用这一标准来控制设备([参考资料 4](https://fortune.com/2026/08/27/anthropic-makes-first-move-into-physical-ai-with-universal-standard-for-scientists-manufacturing/), [参考资料 11](https://techstartups.com/2026/08/27/anthropic-launches-model-hardware-standard-to-let-ai-agents-control-physical-machines/))。这是安索比继之前推出的模型上下文协议（MCP，用于连接数据源的开放标准）之后，向物理世界延伸拓展的成果([参考资料 4](https://fortune.com/2026/08/27/anthropic-makes-first-move-into-physical-ai-with-universal-standard-for-scientists-manufacturing/))。

## 当前现状

目前，安索比已经发布了 MHS 的研究预览版（Research Preview），并正与少数科学实验室及高端制造企业合作测试该技术([参考资料 3](https://www.anthropic.com/news/model-hardware-standard-research-preview), [参考资料 6](https://www.aninews.in/news/business/anthropic-announces-new-model-hardware-standard-for-ai-agents-plans-open-source-release-with-safety-guidance20260828112959/))。

目前，该标准旨在支持研究领域常见的设备，如摄像机、机械臂、显微镜、离心机、移液器（定量吸取液体的工具）等([参考资料 13](https://modelhardwarestandard.com/))。虽然仍处于起步阶段，但相关进程正在构建一个环境，让海量设备能够连接 AI 并安全地处理复杂任务([参考资料 10](https://coursiv.io/blog/model-hardware-standard))。

## 未来展望

如果未来 MHS 得到广泛普及，“智能实验室”的设想将成为现实。不仅是操作设备，多个设备之间还可以相互通信并有机协作。安索比计划将该技术开源，预计会有更多开发者参与其中，共同打造更安全、更智能的制造与研究环境([参考资料 6](https://www.aninews.in/news/business/anthropic-announces-new-model-hardware-standard-for-ai-agents-plans-open-source-release-with-safety-guidance20260828112959/), [参考资料 18](https://aninews.in/news/business/anthropic-announces-new-model-hardware-standard-for-ai-agents-plans-open-source-release-with-safety-guidance20260828112959/))。AI 不再局限于数字屏幕，而是直接操控着我们手中的物理设备，正引领着一个助力人类破解科学难题的时代。

## MindTickleBytes AI 记者视点

数字世界与物理世界的界限正在迅速消融。像 MHS 这样的标准化工作，将成为 AI 从“聪明聊天机器人”进化为“现场实操专家”最关键的第一步。这一变革将显著提升科学技术的发展速度。

## 参考资料

1. [Anthropic's new hardware standard lets AI agents control the physical world - Ars Technica](https://arstechnica.com/ai/2026/08/anthropics-new-hardware-standard-lets-ai-agents-control-the-physical-world/)
2. [Anthropic pushes into physical world with new standard to help AI agents operate machines](https://www.cnbc.com/2026/08/27/anthropic-pushes-into-physical-world-with-new-standard-to-help-ai-agents-operate-machines.html)
3. [Previewing the Model Hardware Standard \ Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview)
4. [Anthropic makes first move into physical AI with universal standard that could bring scientific labs to life | Fortune](https://fortune.com/2026/08/27/anthropic-makes-first-move-into-physical-ai-with-universal-standard-for-scientists-manufacturing/)
6. [Anthropic announces new "Model Hardware Standard" for AI agents; plans open-source release with safety guidance](https://www.aninews.in/news/business/anthropic-announces-new-model-hardware-standard-for-ai-agents-plans-open-source-release-with-safety-guidance20260828112959/)
8. [AnthropicModelHardwareStandard: Physical AI Lands | byteiota](https://byteiota.com/anthropic-model-hardware-standard-physical-ai/)
9. [ModelHardwareStandard(MHS) Explained:AnthropicMHSvs MCP](https://openclawlaunch.com/guides/model-hardware-standard)
10. [ModelHardwareStandard: AI Agents MeetHardware| Coursiv Blog](https://coursiv.io/blog/model-hardware-standard)
11. [AnthropiclaunchesModelHardwareStandardto let... - Tech Startups](https://techstartups.com/2026/08/27/anthropic-launches-model-hardware-standard-to-let-ai-agents-control-physical-machines/)
12. [AnthropicUnveils Physical MCP: Claude Starts Taking Over the Real...](https://eu.36kr.com/en/p/3958406037667205)
13. [ModelHardwareStandard](https://modelhardwarestandard.com/)
14. [AnthropicLaunches MajorModelHardwareStandardMHS, AI Agent...](https://news.aibase.com/news/30693)
15. [Anthropic'sModelHardwareStandardLets AI Agents Control...](https://theoutpost.ai/news-story/anthropic-launches-model-hardware-standard-to-connect-ai-agents-with-physical-devices-30214/)
17. [AnthropicLaunchesModelHardwareStandardfor AI-Robot... | KuCoin](https://www.kucoin.com/news/flash/anthropic-launches-model-hardware-standard-for-ai-robot-integration)
18. [Anthropicannouncesnew "ModelHardwareStandard" for AI agents...](https://aninews.in/news/business/anthropic-announces-new-model-hardware-standard-for-ai-agents-plans-open-source-release-with-safety-guidance20260828112959/)