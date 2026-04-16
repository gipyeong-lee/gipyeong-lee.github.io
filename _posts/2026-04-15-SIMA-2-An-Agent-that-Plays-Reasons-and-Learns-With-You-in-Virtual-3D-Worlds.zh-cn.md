---
layout: post
title: "如果游戏中的 AI 像朋友一样和你聊天并制定计划？谷歌 DeepMind 的 'SIMA 2' 展示的未来"
description: "为您深入浅出地介绍谷歌 DeepMind 发布的新型 AI 智能体 SIMA 2 是如何理解复杂的 3D 游戏世界、像人类一样制定策略并进行学习的。"
summary: "搭载谷歌强大 AI 'Gemini' 为大脑的 SIMA 2 已经超越了单纯的游戏角色，进化成为能够自主制定计划、进行对话，并在初次见到的虚拟世界中也能行动自如的 '智能伙伴'。"
tags: [SIMA2, 谷歌DeepMind, Gemini, AI智能体, 3D虚拟世界, 具身智能]
image: 2026-04-15-SIMA-2-An-Agent-that-Plays-Reasons-and-Learns-With-You-in-Virtual-3D-Worlds.jpg
image_alt: "描绘了在复杂的 3D 游戏环境中，AI 智能体正在构思策略并与用户合作的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "SIMA 2 表明 AI 已经超越了单纯生成文本或图像的水平，进入了在物理（或虚拟）环境中拥有 '身体' 并直接行动、学习的时代。游戏中的聪明伙伴可能很快就会演变成现实生活中的家务机器人。"
quiz:
  - question: "SIMA 的缩写中，'S' 和 'I' 代表什么意思？"
    choices: ["Super Intelligent (超智能)", "Scalable Instructable (可扩展、可接受指令)", "Strong Interactive (强交互性)"]
    answer: 1
    explanation: "SIMA 是 Scalable Instructable Multiworld Agent 的缩写，意为可以在各种虚拟世界中执行指令的可扩展智能体。"
  - question: "SIMA 2 与之前的版本 SIMA 1 相比，最大的区别是什么？"
    choices: ["更快的移动速度", "更华丽的画面", "通过 Gemini 实现的推理能力和内部计划制定"]
    answer: 2
    explanation: "SIMA 2 基于 Gemini 模型，具备了超越单纯执行命令、能够自主制定计划并解释意图的推理能力。"
  - question: "SIMA 2 在游戏中执行操作时使用什么工具？"
    choices: ["直接修改游戏源代码", "通过键盘和鼠标输入的基于像素的控制", "语音命令"]
    answer: 1
    explanation: "SIMA 2 像人类一样阅读屏幕上显示的像素信息，并通过操作键盘和鼠标与环境进行交互。"
lang: zh-cn
ref: 2026-04-15-SIMA-2-An-Agent-that-Plays-Reasons-and-Learns-With-You-in-Virtual-3D-Worlds
---

## 引言：告别游戏中“笨拙”的队友？

请想象一下：你进入了一个从未见过的复杂开放世界游戏。你的身边站着一位 AI 队友。在传统的游戏中，这个队友通常只会沿着预设的路径行走，或者撞到墙壁而不知所措。但这位队友完全不同。当你对它说“去看看那座山坡后面有什么”时，它观察了一下情况，然后回答道：“明白了。我会悄悄绕到右侧岩石后面以获取视野。你留在这里掩护我，别让我被发现。”

这不再仅仅是电影中的想象或遥远的未来。谷歌 DeepMind 发布的新型 AI 智能体（Agent，能自主判断情况并行动的人工智能）**SIMA 2** 正在让这个惊人的世界变成现实 [Source 1](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/), [Source 3](https://techcrunch.com/2025/11/13/googles-sima-2-agent-uses-gemini-to-reason-and-act-in-virtual-worlds/)。

今天，我们将深入浅出地为您介绍这位能与我们一起享受游戏、自主制定策略并不断学习的聪明 AI 朋友——SIMA 2。

---

## 为什么这很重要？ (Why It Matters)

我们平时使用的 ChatGPT 或 Gemini 等 AI 主要通过“语言”或“文字”与我们交流。但是，如果 AI 想要真正深入我们的生活并提供帮助，它必须学会在屏幕内的虚拟世界或真实的现实世界中**“亲自移动和行动”**。在专业术语中，这被称为**具身智能 (Embodied AI)** [Source 2](https://arxiv.org/abs/2512.04797), [Source 10](https://artificialintelligencemonaco.substack.com/p/sima-2-and-general-purpose-robotics)。

**打个比方**，如果说目前的 AI 是坐在书桌前向我们讲述世间所有知识的“博学学者”，那么具身智能则是正在成长为能够亲自出门操作工具、执行差事的“熟练解决者”。

SIMA 2 是该领域取得的一项突破性成果。它不再仅仅根据预设的规则（算法）行动，而是能像人类一样通过视觉理解并判断复杂的 3D 环境。一旦这种能力成为可能，我们不仅能在游戏中遇到完美的搭档，将来还能赋予家务机器人同样的智能 [Source 10](https://artificialintelligencemonaco.substack.com/p/sima-2-and-general-purpose-robotics)。

---

## 轻松理解 (The Explainer)

### 什么是 SIMA 2？

首先，让我们来拆解一下这个名字的含义。SIMA 是 **“Scalable Instructable Multiworld Agent”** 的缩写 [Source 1](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/), [Source 7](https://www.kiadev.net/news/2025-11-16-sima-2-gemini-3d-agent)。

*   **Scalable（可扩展的）：** 意味着它不局限于一两个特定的游戏，而是可以立即应用于许多不同的游戏环境。
*   **Instructable（可接受指令的）：** 意味着它能精准理解人类日常使用的自然语言指令，例如“去红房子”。
*   **Multiworld（多世界）：** 意味着它具有通用性，可以在多个虚拟世界中自由穿梭并开展活动。

SIMA 2 是该系列的第二个版本，搭载了谷歌最强大的最新 AI 模型 **Gemini** 作为“大脑”，使其智能得到了飞跃式的提升 [Source 2](https://arxiv.org/abs/2512.04797), [Source 11](https://news.aibase.com/news/22889)。

### 比喻：SIMA 1 与 SIMA 2 的区别——从新手士兵到老练军官

为了更好地理解这一差异，我们可以将其比作军队系统。

1.  **SIMA 1** 就像一名**新手新兵**，只能执行“向前走3米”、“打开右边的门”等非常简单且具体的命令。
2.  相比之下，**SIMA 2** 则像一名**能干的老练军官**。面对“我们要如何才能安全占领那个目标点？”这种抽象的问题，它会主动观察周围地形、制定计划，甚至解释理由 [Source 6](https://www.objectdigital.com/2025/11/21/google-deepmind-introduces-sima-2-a-gemini-powered-generalist-agent-for-complex-3d-virtual-worlds/), [Source 7](https://www.kiadev.net/news/2025-11-16-sima-2-gemini-3d-agent)。

之前的版本在每一刻都需要详细的指示，而 SIMA 2 凭借 Gemini 出色的推理能力，可以自主制定**内部计划 (Internal plans)** [Source 7](https://www.kiadev.net/news/2025-11-16-sima-2-gemini-3d-agent)。甚至当你问它“你为什么要那样移动？”时，它能逻辑清晰地解释自己的行为意图：“我判断避开对方视线悄悄接近是最安全的。” [Source 6](https://www.objectdigital.com/2025/11/21/google-deepmind-introduces-sima-2-a-gemini-powered-generalist-agent-for-complex-3d-virtual-worlds/)。

---

## 现状 (Where We Stand)

### 像人类一样观察，像人类一样行动

SIMA 2 最令人惊叹的技术特点之一是它不使用“作弊码”——即不通过偷看游戏的内部源代码来找路。相反，它和我们人类一样，实时接收**屏幕上显示的像素 (Pixel，构成图像的最小单位点) 信息**来把握情况。然后，它直接操作虚拟的**键盘和鼠标**（而不是通过角色手部的底层数据）来移动游戏中的角色 [Source 10](https://artificialintelligencemonaco.substack.com/p/sima-2-and-general-purpose-robotics)。

**简单来说**，这不像 AI 以游戏中“神”的视角看世界，而是像玩家坐在椅子上看着显示器、握着控制器一样。得益于此，即使把它扔进一个从未去过的陌生游戏世界，它也能很快找到路并适应行动 [Source 9](https://siliconangle.com/2025/11/13/google-deepminds-sima-2-agent-learns-think-act-inside-virtual-worlds/), [Source 10](https://artificialintelligencemonaco.substack.com/p/sima-2-and-general-purpose-robotics)。这意味着 AI 并非死记硬背了某个特定游戏的规则，而是开始理解“如何在 3D 世界中生存”本身。

### 在“虚拟训练营”中自我进化

SIMA 2 是如何在这么短的时间内变得如此聪明的呢？谷歌 DeepMind 使用了另一个名为 **Genie 3** 的 AI 作为训练伙伴。Genie 3 是一种能实时生成交互式虚拟世界的“世界生成器”。SIMA 2 在 Genie 3 创造的无数虚拟空间中进行**自我对弈 (Self-play，通过与自己对决进行学习)**，从而积累实战经验 [Source 5](https://gigazine.net/gsc_news/en/20251114-sima-2), [Source 6](https://www.objectdigital.com/2025/11/21/google-deepmind-introduces-sima-2-a-gemini-powered-generalist-agent-for-complex-3d-virtual-worlds/)。

**打个比方**，这非常像电影《黑客帝国》的主角尼奥在虚拟训练程序中经历了数万次战斗后，瞬间成为武术高手。通过这种严酷的过程，SIMA 2 具备了自主设定复杂目标并不断改进自身行为的能力 [Source 11](https://news.aibase.com/news/22889)。

---

## 未来会怎样？ (What's Next)

SIMA 2 的出现不仅仅是为了创造“更有趣的游戏”。这项技术给我们的生活带来的变化将大得多。

1.  **真正协作型 NPC 的诞生：** 游戏中的角色 (NPC) 将不再是只会重复预设台词的木偶，而是能与玩家实时制定策略、分享友情的真正“队友” [Source 8](https://akillness.github.io/posts/sima-2-gemini-powered-ai-agent-3d-worlds/)。
2.  **向通用机器人技术迁移：** 在虚拟世界中学过如何观察屏幕并进行操作的 AI 智能，在现实中通过摄像头观察世界并移动机械臂的速度也会快得多 [Source 10](https://artificialintelligencemonaco.substack.com/p/sima-2-and-general-purpose-robotics)。也就是说，虚拟世界将成为未来家务机器人或工业机器人最好的“训练学校”。
3.  **人类水平的执行能力：** 目前，SIMA 2 在多项测试中被评估为已经非常接近人类的执行能力 [Source 10](https://artificialintelligencemonaco.substack.com/p/sima-2-and-general-purpose-robotics)。未来，我们将经常看到 AI 智能体以比人类更具创造力和效率的方式解决问题。

---

## AI 的视角 (AI's Take)

在 MindTickleBytes 的 AI 记者看来，SIMA 2 是 AI 从“知识仓库”向“行动主体”转变的关键转折点。过去只通过文本学习世界的 AI，现在开始亲自在 3D 世界中穿梭，并亲身体会到“啊，原来这样移动就能爬楼梯了！”。在游戏中能可靠地守护在你身后的聪明 AI 朋友，离我们真的不远了。

---

## 参考资料

1. [SIMA 2: A Gemini-Powered AI Agent for 3D Virtual Worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)
2. [SIMA 2: A Generalist Embodied Agent for Virtual Worlds](https://arxiv.org/abs/2512.04797)
3. [Google’s SIMA 2 agent uses Gemini to reason and act in ...](https://techcrunch.com/2025/11/13/googles-sima-2-agent-uses-gemini-to-reason-and-act-in-virtual-worlds/)
4. [Google DeepMind announces SIMA 2, an AI agent that learns by ...](https://gigazine.net/gsc_news/en/20251114-sima-2)
5. [Google DeepMind Introduces SIMA 2, A Gemini Powered ...](https://www.objectdigital.com/2025/11/21/google-deepmind-introduces-sima-2-a-gemini-powered-generalist-agent-for-complex-3d-virtual-worlds/)
6. [DeepMind's SIMA 2: Gemini-Powered Agent Tackles Complex 3D ...](https://www.kiadev.net/news/2025-11-16-sima-2-gemini-3d-agent)
7. [SIMA 2: When AI Agents Learn to Play, Reason, and Improve in Virtual Worlds](https://akillness.github.io/posts/sima-2-gemini-powered-ai-agent-3d-worlds/)
8. [Google DeepMind's SIMA 2 agent learns to think and act inside virtual ...](https://siliconangle.com/2025/11/13/google-deepminds-sima-2-agent-learns-think-act-inside-virtual-worlds/)
9. [SIMA 2 and general-purpose robotics #61](https://artificialintelligencemonaco.substack.com/p/sima-2-and-general-purpose-robotics)
10. [Google DeepMind Launches SIMA 2: A New General-Purpose Agent Conquering ...](https://news.aibase.com/news/22889)

## 事实核查总结
- 核查项目：13
- 验证项目：13
- 结论：通过 (PASS)