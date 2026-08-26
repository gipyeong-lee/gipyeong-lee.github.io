---
layout: post
title: "我的电脑变身智能 AI 助手？Perplexity 与英伟达挑战“本地 AI”"
description: "Perplexity 与英伟达合作推出“便携式计算机” AI 代理，无需联网即可在个人电脑上安全、低成本地使用 AI"
summary: "Perplexity 与英伟达合作推出 AI 代理平台“便携式计算机（Portable Computer）”，可在个人电脑上直接运行，无需连接互联网。"
tags: [AI, 本地AI, Perplexity, 英伟达, 人工智能]
image: 2026-08-27-Perplexity-partners-with-Nvidia-to-launch-a-local-AI-agent.jpg
image_alt: "在搭载英伟达 GPU 的个人电脑上运行的 Perplexity AI 代理界面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这是降低对云端依赖并将数据主权归还给个人的重要转折点。从安全和成本效益的角度来看，本地 AI 的吸引力将与日俱增。"
quiz:
  - question: "Perplexity 和英伟达此次联合发布的平台名称是什么？"
    choices: ["云端计算机", "便携式计算机", "AI 本地中心"]
    answer: 1
    explanation: "正确答案是“便携式计算机（Portable Computer）”。这是一个无需互联网连接，即可在个人设备上直接运行的 AI 代理平台。"
  - question: "使用该平台可以获得什么成本优势？"
    choices: ["每月订阅免费", "零 Token 成本", "免电费"]
    answer: 1
    explanation: "使用云端 AI 服务时产生的“Token 费用”，在该平台上将不再产生。"
  - question: "该 AI 代理主要在什么硬件环境下运行？"
    choices: ["网页浏览器", "所有智能手机", "搭载英伟达 GPU 的 PC 和服务器"]
    answer: 2
    explanation: "初期主要可在搭载英伟达 DGX Spark 以及英伟达 RTX 显卡的 Linux 系统 PC 等设备上运行。"
lang: zh-cn
ref: 2026-08-27-Perplexity-partners-with-Nvidia-to-launch-a-local-AI-agent
---

试想一下：早上醒来，你对电脑说：“帮我整理好今天需要开会用的资料。” 直到目前，我们使用的大多数生成式 AI 都必须经过庞大的云端（连接互联网的远程服务器）。但现在，那个聪明的 AI 助手不再存在于互联网彼端的服务器中，而是就在你桌面上的电脑里安全地处理任务，这样的未来已经触手可及。

最近，以人工智能搜索服务闻名的 Perplexity 携手图形处理器（GPU）巨头英伟达（NVIDIA），发布了全新的 AI 代理平台“便携式计算机（Portable Computer）”([Perplexity-英伟达便携式计算机发布](https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs))。这项服务是一次创新尝试，旨在将 AI 的运行方式从以云端为中心转变为以个人设备为中心。

## 为什么重要？

最大的变化在于成本和安全。此前，使用云端 AI 时，每当 AI 生成回答，用户都必须根据所谓的“Token（AI 使用的单词单位信息量）”支付使用费。但“便携式计算机”借用用户电脑的硬件性能直接运行 AI，因此无需再支付这些 Token 费用([Perplexity 便携式计算机发布](https://www.androidauthority.com/perplexity-portable-computer-local-ai-agent-3703083/))。

此外，在安全性方面也具有突破性。传统方式要求用户的操作内容必须传输到外部服务器，但现在 AI 模型、用户数据以及 AI 执行的任务本身都保留在设备内部，因此在个人隐私保护方面更令人放心([Perplexity 与英伟达的本地桌面 AI 代理](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lhM3JydkVSRWVaUGZFWUJReU1pZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en))。

## 易懂解析

如果用一个比喻来形容“便携式计算机”的原理，那就是**“付费图书馆”与“个人书房”的区别**。

如果说此前的云端 AI 是每次付费去外部图书馆借书阅读的方式，那么“便携式计算机”就像是把图书馆直接搬进了你的房间。虽然初期需要投入购买设备的成本，但一旦配置完成，无论何时使用 AI，都不会产生额外费用。

在技术上，该平台不仅包含作为 AI 大脑的“模型”，还将判断 AI 该做什么的“调度器（Orchestrator）”和“代理工具包（AI 代理的运行环境）”都设计为在个人设备内部运行([Perplexity 本地 AI 行为](https://www.theregister.com/ai-and-ml/2026/08/26/now-perplexity-is-trying-to-get-into-the-local-ai-action/5292449))。这意味着即使断开互联网，AI 也能自主判断并解决复杂任务([Perplexity 便携式计算机发布](https://x.com/wallstengine/status/2092262633068277776))。

## 当前状况

目前该平台率先在英伟达的硬件环境下实现优化。具体而言，可在搭载英伟达 DGX Spark 系统，或配备英伟达 RTX 显卡的 Linux PC 上使用([英伟达 DGX Spark 与本地 AI](https://www.gadgetvoize.com/2026/08/26/nvidia-pushes-local-ai-with-open-models-agents-and-perplexity-partnership/))。

发布初期支持“Qwen 3.8 27B”模型或经过额外训练的“Qwen PPLX 27B”模型，不久后还将支持英伟达的“Nemotron 3.5 Lightning (30B)”模型([Perplexity 与英伟达的本地 AI 代理](https://www.howtogeek.com/perplexity-release-portable-computer-a-local-ai-agent/))。从一般的信息搜索到复杂的流程处理都能在本地直接完成，这是其一大特点([Perplexity 便携式计算机发布](https://aistart.ai/ainews/perplexity-local-ai-agent-nvidia))。

## 未来展望

未来，预计更多的普通个人 PC 环境也将能够体验到这种“本地 AI”。随着 AI 技术突破云端的巨大围栏，深入用户的设备之中，即便在互联网连接不稳定的环境下，也能享受到高性能 AI 红利的时代即将开启([Perplexity 便携式计算机发布](https://basic-tutorials.com/news/perplexity-portable-computer-ai-agent-now-runs-locally-on-nvidia-dgx-spark/))。或许不久之后，当我们选择个人电脑时，除了 CPU 或 RAM 之外，“能以多快的速度运行何种 AI 代理”也将成为重要的购买标准。

---

## MindTickleBytes 的 AI 记者视点
此次尝试降低对云端的依赖并将数据主权归还给个人，是人工智能发展的重要转折点。期待这项技术在超越便捷性的同时，能更深入地融入个人日常生活并建立起安全保障。

## 参考资料
1. [Perplexity partners with Nvidia to launch Portable Computer, a fully local AI agent with zero token costs | VentureBeat](https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs)
2. [Perplexity and NVIDIA team up to release a local AI agent | How-To Geek](https://www.howtogeek.com/perplexity-release-portable-computer-a-local-ai-agent/)
3. [Perplexity launches a local AI agent with zero token costs - Android Authority](https://www.androidauthority.com/perplexity-portable-computer-local-ai-agent-3703083/)
4. [Perplexity and Nvidia partner for local-first AI platform | CNBC](https://www.cnbc.com/video/2026/08/25/perplexity-and-nvidia-partner-for-local-first-ai-platform.html)
5. [Wall St Engine on X: "PERPLEXITY LAUNCHES FULLY LOCAL AI AGENTS..."](https://x.com/wallstengine/status/2092262633068277776)
6. [NVIDIA Pushes Local AI With Open Models, Agents and Perplexity Partnership – Gadget Voize](https://www.gadgetvoize.com/2026/08/26/nvidia-pushes-local-ai-with-open-models-agents-and-perplexity-partnership/)
7. [Perplexity and Nvidia partner for local desktop AI agent - Overview | Google News](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lhM3JydkVSRWVaUGZFWUJReU1pZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en)
8. [Perplexity Launches Local AI Agent Portable Computer | The Outpost](https://theoutpost.ai/news-story/perplexity-portable-computer-brings-local-ai-agent-to-your-desktop-with-no-cloud-dependency-30115/)
9. [Perplexity partners With Nvidia to launch... | VMVirtualMachine.com](https://vmvirtualmachine.com/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs/)
10. [Portable Computer is Perplexity's new local AI agent - why... | ZDNET](https://www.zdnet.com/article/portable-computer-perplexity-local-ai-agent/)
11. [World Leader in Artificial Intelligence Computing | NVIDIA](https://www.nvidia.com/)
12. [Perplexity and Nvidia Launch a Zero-Token-Cost Local AI Agent | AI Market Watch](https://www.ai-market-watch.com/news/perplexity-and-nvdia-launch-portable-computer-a-fully-local-ai-agent-with-zero--kyx83w)
13. [Perplexity Launches Fully Local AI Agent with Nvidia | AI News](https://aistart.ai/ainews/perplexity-local-ai-agent-nvidia)
14. [Now Perplexity is trying to get into the local AI action | The Register](https://www.theregister.com/ai-and-ml/2026/08/26/now-perplexity-is-trying-to-get-into-the-local-ai-action/5292449)
15. [Perplexity Portable Computer: AI agent now runs locally on NVIDIA DGX Spark | Basic Tutorials](https://basic-tutorials.com/news/perplexity-portable-computer-ai-agent-now-runs-locally-on-nvidia-dgx-spark/)
16. [Perplexity AI launches Portable Computer on-device AI agent | SiliconAngle](https://siliconangle.com/2026/08/25/perplexity-ai-launches-portable-computer-on-device-ai-agent/)