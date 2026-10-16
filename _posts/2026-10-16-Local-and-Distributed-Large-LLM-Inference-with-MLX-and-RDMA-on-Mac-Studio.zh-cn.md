---
layout: post
title: "桌面上的超级计算机：用多台 Mac Studio 构建超大 AI"
description: "无需昂贵的云服务器，为您介绍如何通过连接多台 Mac Studio，利用基于 RDMA 的分布式 AI 构建方法来运行超大规模 AI 模型。"
summary: "通过利用苹果 M5 Mac Studio 和最新 macOS 26.2 的 RDMA 技术，将多台 Mac 连接起来，无需依赖云端，即可在本地运行万亿参数级的 AI 模型。"
tags: [Apple, MacStudio, AI, MLX, RDMA]
image: 2026-10-16-Local-and-Distributed-Large-LLM-Inference-with-MLX-and-RDMA-on-Mac-Studio.jpg
image_alt: "多台 Mac Studio 通过雷雳 5 (Thunderbolt 5) 电缆连接，组成了一个巨大的 AI 计算集群。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "摆脱云端依赖，在本地环境运行超大规模模型，是个人隐私保护与性能提升方面的一大进步。"
quiz:
  - question: "在构建分布式 AI 集群时，进行 RDMA 通信需要注意什么？"
    choices: ["必须连接所有 Mac 的以太网接口", "必须避开以太网接口旁边的雷雳 5 端口", "必须同时开启所有 Mac 的电源"]
    answer: 1
    explanation: "Mac Studio 以太网接口旁边的雷雳 5 端口不支持 RDMA 链路，因此在构建集群时必须避开使用。"
  - question: "连接多台 Mac 构建分布式 AI 时，可以预期到多大的性能提升？"
    choices: ["约 1.5 倍", "约 3 倍", "约 10 倍"]
    answer: 1
    explanation: "使用由 4 个节点组成的 Mac 集群，可以将推理和微调 (fine-tuning) 的速度提升约 3 倍。"
  - question: "在 Apple Silicon Mac 上利用 RDMA 通信的必要条件是什么？"
    choices: ["macOS 26.2 或更高版本，并在系统设置中启用 RDMA", "安装独立的图形显卡", "基于最新英特尔处理器的 Mac"]
    answer: 0
    explanation: "所有设备必须安装 macOS 26.2 或更高版本，并需在系统设置中手动启用 RDMA 功能。"
lang: zh-cn
ref: 2026-10-16-Local-and-Distributed-Large-LLM-Inference-with-MLX-and-RDMA-on-Mac-Studio
---

想象一下。您是否曾为了运行复杂的人工智能 (AI) 模型，而每月支付数十万韩元的云服务费用，或者担心个人数据会被泄露到外部服务器？现在，时代已经开启，只需将桌上的几台电脑连接起来，您就可以直接运营性能媲美企业级大型服务器的 AI。

苹果于 2026 年 8 月推出的基于 M5 Max 和 M5 Ultra 的新款 Mac Studio，不仅是一款高性能桌面电脑，现在更成为了“分布式 AI 集群”（将多台计算机绑定在一起，像一台大型计算设备一样运行的系统）的核心枢纽[Source 1, Source 15]。

## 为什么这很重要？

此前，对于拥有超过 1 万亿个参数（Parameter，决定 AI 模型智能程度的内部可调数值）的超大规模 AI 模型来说，普通个人电脑根本无法运行。当然，昂贵的“数据中心级”设备是必不可少的[Source 2]。

但此次技术更新的核心在于，您可以“在本地设备 (On-device)”上解决所有问题。特别是对于企业或个人而言，无需将敏感数据发送到外部服务器，就能在本地环境安全地训练和利用最先进的 AI 模型，这是一项巨大的变革[Source 2]。无需再依赖云服务公司，您可以在完全掌控自身数据的同时，享受到强大的 AI 性能[Source 13]。

## 简而言之：RDMA 就像高速公路的“专用通道”

要连接多台计算机来运行同一个 AI 模型，海量数据必须在计算机之间瞬间传输。此时的核心技术就是 **RDMA (Remote Direct Memory Access，远程直接内存访问)**。

打个比方，如果说现有的数据传输方式是载货车辆通过复杂收费站的过程，那么 RDMA 就相当于撤掉了所有道路和收费站，直接将各计算机的内存连接成一条长长的走廊[Source 17]。结合雷雳 5 (Thunderbolt 5) 技术，RDMA 能够以 80Gb/s 的惊人速度传输数据，并将响应延迟 (Latency) 缩短到 5 到 9 微秒 (μs) 的极短水平[Source 17]。正因如此，多台 Mac 才能像一台巨型计算机一样有机地协同工作。

苹果的开源通信库“JACCL”能高效地协调这种通信。就像 4 个人合作同时拼好 4 块复杂拼图一样，它承担着将 AI 计算智能分配给多台 Mac 的任务[Source 18, Source 19]。

## 现状：需要什么准备？

要亲手实现这一出色的系统，您需要一些准备工作。

1. **最新硬件**：需要搭载 M5 Ultra 且支持雷雳 5 的设备，如 Mac Studio 等[Source 5]。特别是 Mac Studio 提供高达 512GB 的统一内存，非常适合运行大型模型[Source 1]。
2. **软件环境**：所有设备必须安装 macOS 26.2 或更高版本，并需在系统设置中手动启用 RDMA 功能[Source 3, Source 5]。
3. **连接注意事项**：这需要比单纯插拔电缆更细心。在 Mac Studio 背面的端口中，以太网接口旁边的雷雳 5 端口不支持 RDMA 集群网络，因此连接时必须避开[Source 7]。

配置完成后，通过苹果的 MLX 框架和分布式训练工具，可以将多台 Mac 绑定在一起。连接 4 台 Mac 节点，可以将推理和微调（fine-tuning，指对现有模型进行追加训练以适应特定目的的过程）的速度提升约 3 倍[Source 3, Source 19]。

## 未来会怎样？

RDMA over 雷雳 5 似乎将成为分布式 AI 推理领域的一个转折点[Source 4, Source 5]。原本只有昂贵的企业级设备才能触及的领域，现在已经下放到普通消费级桌面环境[Source 6]。未来，期待个人开发者或小规模团队能够摆脱昂贵的云端基础设施，仅靠桌上的几台 Mac 直接训练属于自己的超大规模模型，这类案例将大幅增加。

## MindTickleBytes 的 AI 记者视角

曾被大型科技公司垄断的“计算之力”开始分发到个人的桌面上。这不仅是性能提升的问题，在 AI 技术民主化和数据主权方面也是一个非常令人振奋的趋势。因为它意味着我们每个人都正在成为 AI 技术真正的主人。

## 参考资料

1. [M5 Ultra Mac Studio: 512GB Local AI (Aug 2026) | explainx.ai](https://www.explainx.ai/blog/apple-mac-studio-m5-max-ultra-local-ai-august-2026)
2. [Towards Training Private LLMs: Exploring Fine-Tuning Language...](https://arxiv.org/html/2609.18066)
3. [MLX Distributed Training Arrives: 3x Faster Fine-Tuning and...](https://blog.imseankim.com/apple-mlx-distributed-training-rdma-thunderbolt-5-multi-mac-wwdc-2026/)
4. [Running Large Language Models Locally: Complete Hardware Guide...](https://berdachuk.com/ai/running-giant-ai-models-on-your-own-computer)
5. [daniliants.com/insights/github-exo-explore-exo-run-frontier-ai-locally.md](https://daniliants.com/insights/github-exo-explore-exo-run-frontier-ai-locally.md)
6. [Explore distributed inference and training with MLX - WWDC26...](https://developer.apple.com/videos/play/wwdc2026/233/)
7. [Mac Studio Cluster for Trillion-Parameter AI in 2026: RDMA Over...](https://runaihome.com/blog/mac-studio-cluster-rdma-thunderbolt5-trillion-parameter-2026/)
13. [AnythingLLM — On-device AI for productivity | Local & Private](https://anythingllm.com/)
15. [Apple introduces new Mac Studio with M5 Max and M5 Ultra - Apple](https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/)
17. [Apple RDMA: How Mac Clusters Are Changing Local AI](https://stabilise.io/blog/apples-rdma-revolution-how-mac-clusters-are-changing-local-ai-hosting)
18. [WWDC 2026: Explore distributed inference and training with MLX...](https://wwdc.ai/2026/233)
19. [Running Agentic AI on the Mac with MLX](https://blakecrosley.com/blog/agentic-ai-mac-mlx)