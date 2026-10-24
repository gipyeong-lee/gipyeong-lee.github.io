---
layout: post
title: "AI 竟能亲自制作《DOOM》？无需游戏引擎的 AI 游戏运行之秘"
description: "从无需游戏引擎、仅凭 AI 神经网络运行经典游戏《DOOM》的技术，到果蝇大脑与人类脑细胞“游玩”《DOOM》的趣闻，为您一一揭秘。"
summary: "谷歌的 GameNGen 模型以及利用果蝇和人类脑细胞进行的实验，展示了人工神经网络在实时模拟或控制复杂游戏方面的潜力。"
tags: [AI, 游戏, 神经网络, 技术趋势]
image: 2026-10-25-I-built-a-neural-network-using-DOOM-games.jpg
image_alt: "经典游戏《DOOM》的像素图形与相互连接的神经网络节点重叠在一起的艺术图像。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这些超越简单游戏的实验测试了 AI 的通用计算能力，预示了 AI 未来在理解和生成虚拟世界方面的进化方向。"
quiz:
  - question: "谷歌与特拉维夫大学开发的“GameNGen”的最大特点是什么？"
    choices: ["优化了原有的《DOOM》代码", "无需传统游戏引擎，仅凭神经网络即可模拟游戏", "需要用户亲自编写代码才能运行"]
    answer: 1
    explanation: "GameNGen 无需原有游戏引擎或代码，仅通过神经网络的动态生成即可实时实现《DOOM》。"
  - question: "利用果蝇大脑连接组（connectome）游玩《DOOM》的实验是如何运作的？"
    choices: ["让果蝇手持控制器", "将游戏画面转换为神经细胞刺激来控制游戏", "让果蝇亲自盯着显示器看"]
    answer: 1
    explanation: "将游戏帧信息转换为果蝇感觉神经细胞的刺激，并将由此产生的神经活动映射为游戏控制指令。"
  - question: "人类脑细胞游玩《DOOM》的方式使用了什么数据？"
    choices: ["玩家的心情", "玩家的健康数值和敌人的位置信息", "实时聊天信息"]
    answer: 1
    explanation: "脑细胞并非直接观看画面，而是通过神经网络将游戏内的数值化信息转换为数据进行传递。"
lang: zh-cn
ref: 2026-10-25-I-built-a-neural-network-using-DOOM-games
---

想象一下。你正在玩的这款游戏，实际上并非存储在电脑里的复杂程序，而是人工智能（AI）在每一瞬间即兴“想象”并绘制出来的画面，那会是怎样的一种体验？

最近，技术界接连开展了一些有趣且令人惊叹的实验，利用 1993 年发行的传奇 FPS 游戏《DOOM》来测试 AI 的能力。不仅出现了擅长游戏的 AI，甚至还尝试了无需游戏引擎即可实现游戏本身，甚至是利用真实生物的大脑来享受游戏。到底 AI 和《DOOM》之间发生了什么？

### 这为何重要？

这些实验不仅仅是为了打造“爱玩游戏的 AI”。其核心在于确认**“人工神经网络（Neural Network，模仿人类大脑结构处理信息的 AI 模型）”**能够多么精确地学习并模仿物理世界的复杂规则或虚拟世界。([参考资料 10](https://karpathy.ai/zero-to-hero.html))

如果我们能证明 AI 即使在没有游戏引擎的情况下也能实时生成游戏，这就意味着未来的元宇宙或虚拟现实服务可以比以往更加轻量、更加智能化地运行。此外，将生物大脑的神经连接图（connectome）与游戏控制相结合的研究，为 AI 如何模仿和辅助人类或动物的智能提供了重要线索。

### 浅显易懂：AI 是如何“想象”游戏的？

首先，作为 AI 核心的神经网络就像一个**“巨大的过滤装置”**。([参考资料 3](https://playground.tensorflow.org/)) 当我们输入数字后，数据会经过神经网络内部的层（layer），在此过程中被过滤和放大，最终得出结果。([参考资料 6](https://www.youtube.com/watch?v=aircAruvnKk)) 如果把这个过程比作过滤，它就像是通过非常复杂的筛子，只筛选出信息的核心部分。

1. **无引擎模拟 (GameNGen)：** 谷歌与特拉维夫大学的研究团队开发的“GameNGen”模型完全不使用现有的游戏代码或虚幻引擎等传统游戏引擎。([参考资料 17](https://www.311institute.com/googles-ai-generated-doom-frame-by-frame-without-a-game-engine/), [参考资料 18](https://pixeldojo.ai/industry-news/gamengen-googles-ai-model-simulates-doom-in-real-time)) 相反，该神经网络通过学习《DOOM》的游戏数据，自行预测并生成每一帧（画面单位）应该呈现的内容。这就像一位资深画家记住了《DOOM》的所有场景，并根据用户的操作即兴作画一样。研究团队已成功实时运行了这款复杂的视频游戏。([参考资料 2](https://futurism.com/doom-running-on-neural-network), [参考资料 15](https://arxiv.org/pdf/2408.14837))

2. **果蝇大脑游玩《DOOM》：** 软件工程师 Alex Wormuth 将果蝇大脑的神经连接图“连接组（connectome）”数字化实现。([参考资料 1](https://www.techspot.com/news/113780-google-mapped-fly-nervous-system-developers-using-play.html)) 游戏画面发生变化时，会对该神经网络施加电信号般的刺激，并将由此产生的神经活动转化为游戏角色的动作（左右移动、射击等）。([参考资料 19](https://gigazine.net/gsc_news/en/20260909-google-fly-brain-mapping-doom)) 也就是说，果蝇的大脑数据在操控实际的游戏。

### 现状：进展如何？

目前研究范围非常广泛。
- **AI 的幻觉与梦境：** 在某些研究中，AI 基于游戏数据，自行可视化出《DOOM》的“噩梦”。玩家需要在 AI 想象出来的无尽火球中躲避并继续游戏。([参考资料 4](https://www.rockpapershotgun.com/dodge-fireballs-forever-in-a-neural-nets-doom-nightmare))
- **脑细胞直接游玩：** 甚至还有培养的人类脑细胞游玩《DOOM》的案例。脑细胞并非直接观看显示器，而是通过神经网络接收玩家健康状态或敌人位置等数值，学习并采取适当行动。([参考资料 7](https://www.theguardian.com/games/2026/mar/16/petri-dish-brain-cells-playing-doom-cortical-labs))
- **基于语言模型的实现：** 最近出现的“Torchwright Doom”将《DOOM》这款游戏本身编译进语言模型（LLM）中运行。这证明了语言模型不仅是写作工具，还能作为通用计算平台发挥作用。([参考资料 13](https://emergent.sh/news/doom-compiled-into-rtorchwright-doom))

然而，这些技术仍处于初期阶段。在效率方面还存在许多课题，尚无法完美替代需要实时性和复杂操作的游戏。虽然目前用此技术运行最新游戏还很困难，但它暗示了人工智能认知和表达世界的方式正在发生根本性的变革。

### 未来将会怎样？

未来，AI 将向着利用更少的数据、自主生成并控制更复杂环境的方向进化。游戏或许会从“被制作出来的程序”转变为“AI 实时想象出的体验”。终有一天，当你对 AI 说“给我做一个恐怖氛围的火星基地游戏”时，它可能会即兴为你创造出一个像《DOOM》那样的游戏。我们所想象的一切都将通过数据和神经网络呈现，如同现实一般——这一天已不再遥远。

### MindTickleBytes AI 记者视角
《DOOM》在过去 30 多年里一直是 AI 研究者的游乐场。但现在它超越了简单的游乐场，成为了证明 AI 对虚拟世界理解程度的舞台。从脑细胞到果蝇大脑，这些将它们与《DOOM》连接起来的奇特尝试，最终都在向我们抛出一个关于如何定义“智能”并将其人工实现的问题。人工智能正在超越仅仅处理数据的机器，进化为能够发挥想象力并创造世界的“智能主体”，这难道不引人入胜吗？

## 参考资料

1. [Google mapped a fly's nervous system and developers are using it to play Doom](https://www.techspot.com/news/113780-google-mapped-fly-nervous-system-developers-using-play.html)
2. [Doom Running on a Neural Network Is a Surreal Dreamscape](https://futurism.com/doom-running-on-neural-network)
3. [A Neural Network Playground](https://playground.tensorflow.org/)
4. [Neural Net dreaming of Doom | Rock Paper Shotgun](https://www.rockpapershotgun.com/dodge-fireballs-forever-in-a-neural-nets-doom-nightmare)
6. [But what is a neural network? | Deep learning chapter 1](https://www.youtube.com/watch?v=aircAruvnKk)
7. [A petri dish of human brain cells is currently playing Doom](https://www.theguardian.com/games/2026/mar/16/petri-dish-brain-cells-playing-doom-cortical-labs)
9. [But what is a Neural Network? | 3Blue1Brown](https://www.3blue1brown.com/lessons/neural-networks/)
10. [Neural Networks: Zero To Hero](https://karpathy.ai/zero-to-hero.html)
13. [Doom Compiled into an LLM: Torchwright Doom Launches](https://emergent.sh/news/doom-compiled-into-llm-torchwright-doom)
15. [arXiv:2408.14837v2 [cs.LG] 24 Apr 2025](https://arxiv.org/pdf/2408.14837)
17. [Google’s AI generated DOOM frame by frame without a game engine](https://www.311institute.com/googles-ai-generated-doom-frame-by-frame-without-a-game-engine/)
18. [GameNGen: Google's AI Model Simulates Doom in Real-Time](https://pixeldojo.ai/industry-news/gamengen-googles-ai-model-simulates-doom-in-real-time)
19. [As soon as Google released the mapping of a fly's brain and ...](https://gigazine.net/gsc_news/en/20260909-google-fly-brain-mapping-doom)