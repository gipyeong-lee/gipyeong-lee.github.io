---
layout: post
title: "AI 是如何思考的？窥探巨大神经网络内部的数学钥匙"
description: "介绍“机器可解释性”研究的基础，该研究旨在通过数学方式分解 AI 模型内部复杂的运算，从而揭示 AI 做出判断的原因。"
summary: "2021 年 Anthropic 发表的研究为从数学上分解并理解复杂 AI 模型的内部算法迈出了第一步。"
tags: [AI, 深度学习, 机器可解释性, Anthropic]
image: 2026-09-13-A-Mathematical-Framework-for-Transformer-Circuits-2021.jpg
image_alt: "将像复杂电路图一样连接的 AI 神经元结构用数学公式进行解析的抽象图形。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "打开 AI 的黑盒不仅仅是出于好奇，这是为了让人工智能对人类而言更加安全、透明地运行，所必须拼凑的最重要的拼图。"
quiz:
  - question: "本研究涉及的主要 AI 模型结构是什么？"
    choices: ["Transformer", "卷积神经网络", "循环神经网络"]
    answer: 0
    explanation: "本研究专注于对 Transformer（变换器）模型的内部运行原理进行数学逆向工程（reverse-engineer）。"
  - question: "本研究将 AI 模型的“残差流（residual stream）”比作什么？"
    choices: ["数据存储库", "基于加法的通信通道", "内存缓存"]
    answer: 1
    explanation: "研究团队将残差流定义为 AI 内部组件交换信息的“基于加法的通信通道”。"
  - question: "本研究的最终目标是什么？"
    choices: ["最大化 AI 性能", "对 AI 内部算法进行数学理解与逆向工程", "开发新的语言生成模型"]
    answer: 1
    explanation: "目标是对复杂的 AI 模型进行数学理解和逆向工程，从而构建一个框架，用以揭示更大规模模型的运行原理。"
lang: zh-cn
ref: 2026-09-13-A-Mathematical-Framework-for-Transformer-Circuits-2021
---

想象一下。你是一位非常聪明的训犬师。狗狗完美地执行了你的命令，但你却不知道它是通过怎样的思考才做出行动的。这仅仅是训练的结果，还是狗狗有自己的逻辑呢？

我们每天使用的 ChatGPT 等 AI 模型也与之类似。它们通过学习海量数据产生惊人的成果，但那巨大的神经网络内部发生了什么，就像一个“黑盒”一样隐藏在迷雾之中。今天，我们将打开这个黑盒，窥探 AI 的内部构造，并介绍 2021 年 Anthropic 的一项重要研究——“Transformer 电路的数学框架”。[出处: A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)

### 为什么这很重要？

随着 AI 普及到社会各个角落，“AI 为什么给出这样的回答”、“它是否真的值得信任”已成为非常重要的话题。如果 AI 提供偏见信息或做出错误判断，我们必须能够从内部找到原因并加以修正。

这项研究不仅出于好奇，更是为了让我们能够完全控制和理解 AI 这一巨大技术，从而绘制一张“数学地图”的工作。[出处: A Mathematical Framework for Transformer Circuits \ Anthropic](https://www.anthropic.com/research/a-mathematical-framework-for-transformer-circuits) 这项研究成为了“机器可解释性（Mechanistic Interpretability，即逻辑上和数学上分析人工智能如何内部处理数据）”领域的开端，被评价为试图将 AI 内部动作翻译成精确数学语言的尝试。[出处: [Review] A Mathematical Framework for Transformer Circuits](https://induction1.github.io/notes/transformer-circuits/index.html)

### 简单理解：解剖 AI 的“大脑电路”

这项研究的核心始于一个非常简单的问题。“能否用精确的数学术语解释 AI 执行的小规模算法，并仅通过查看其权重（Weights，AI 学习过程中调节的数值）就直接读懂它在做什么？”[出处: Circuits 01 — A Mathematical Framework for Transformer Circuits](https://brendanjameslynskey.github.io/Circuits_01_Mathematical_Framework/)

为此，研究团队将 Transformer（AI 的核心结构，用于把握句子中单词之间的关系）模型拆解为 2 层以下的简化形式进行了分析。[出处: A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)

**打个比方：**
想象你面前有一座非常复杂的 100 层摩天大楼。设计图太复杂，很难一眼看懂。研究团队并没有去拆解整座大楼的结构，而是仅仅拆下 1 楼和 2 楼，开始用显微镜观察其中的线路是如何连接的。[出处: A Mathematical Framework for Transformer Circuits](https://negevtag.github.io/TransfomerCirctusForClaude/2021/framework.pdf)

研究团队将 AI 交换信息的通道——“残差流（Residual Stream，AI 处理句子时存储并持续更新信息的通信通道）”视为一种通过加法方式传递信息的通信通道。[出处: mathematicalframeworkfortransformercircuits](https://aarnphm.xyz/thoughts/mathematical-framework-transformers-circuits) 简单来说，这类似于多个人同时在一个笔记本上写字并不断积累信息的过程。在此基础上，他们应用了注意力（Attention）机制（决定句子中哪些单词重要的功能），并将其拆解为决定是否集中于特定信息的矩阵（QK）和决定如何反映该信息的矩阵（OV）这种数学框架进行了分析。[出处: mathematicalframeworkfortransformercircuits](https://aarnphm.xyz/thoughts/mathematical-framework-transformers-circuits)

### 当前现状：进展到哪里了？

目前，这项研究已成为 AI 研究人员推论 AI 模型内部的“心理模型（Mental Model）”的重要基础。[出处: Review: A Mathematical Framework for Transformer Circuits](https://pratik-doshi-99.github.io/posts/transformer-circuits/) 但是，我们使用的最新模型是拥有数万亿参数（Parameter，AI 学习过程中微调的数值）的巨大怪兽。它们比本研究中讨论的 2 层模型要复杂得多。[出处: A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html) 因此，将本研究的方法论完全应用于实际的大型模型仍然是一项充满挑战的任务。

### 未来会怎样？

这项研究提出的“数学语言”正在持续发展。研究人员正努力将在此发现的简单算法模式逐渐应用于更大、更复杂的模型中。[出处: A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html) 也许有一天，当我们问 AI“你为什么给出那样的回答”时，AI 能够列举出其内部电路的数学依据来进行解释。

### MindTickleBytes AI 记者的视点

在 AI 这项巨大技术浪潮中，试图解剖其内部的尝试，是确保技术“透明度”和“信任”的高尚努力。只有当我们不再将 AI 视为神奇的盒子，而是理解为拥有明确数学规则的机器时，我们才能自信地迎接与 AI 共存的未来。

## 参考资料

1. [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)
2. [A Walkthrough of A Mathematical Framework for Transformer Circuits — Neel Nanda](https://www.neelnanda.io/mechanistic-interpretability/a-walkthrough-of-a-transformer-circuits)
3. [A Mathematical Framework for Transformer Circuits \ Anthropic](https://www.anthropic.com/research/a-mathematical-framework-for-transformer-circuits)
4. [A Mathematical Framework for Transformer Circuits](https://www.scribd.com/document/866284321/A-Mathematical-Framework-for-Transformer-Circuits)
5. [Arxiv Dives - A Mathematical Framework for Transformer Circuits - Part 1](https://ghost.oxen.ai/arxiv-dives-a-mathematical-framework-for-transformer-circuits/)
6. [A Walkthrough of A Mathematical Framework for Transformer Circuits - YouTube](https://www.youtube.com/watch?v=KV5gbOmHbjU)
7. [A Mathematical Framework for Transformer Circuits](https://negevtag.github.io/TransfomerCirctusForClaude/2021/framework.pdf)
8. [Circuits 01 — A Mathematical Framework for Transformer Circuits](https://brendanjameslynskey.github.io/Circuits_01_Mathematical_Framework/)
9. [Review: A Mathematical Framework for Transformer Circuits](https://induction1.github.io/notes/transformer-circuits/index.html)
10. [Review: A Mathematical Framework for Transformer Circuits](https://pratik-doshi-99.github.io/posts/transformer-circuits/)
11. [A Mathematical Framework for Transformer Circuits... | HackerNews](https://news.ycombinator.com/item?id=49672365)
12. [A Mathematical Framework for Transformer Circuits \ Anthropic](https://www.anthropic.com/news/a-mathematical-framework-for-transformer-circuits)
13. [A Mathematical Framework for Transformer Circuits - nikkie-memos](https://scrapbox.io/nikkie-memos/A_Mathematical_Framework_for_Transformer_Circuits)
14. [mathematicalframeworkfortransformercircuits](https://aarnphm.xyz/thoughts/mathematical-framework-transformers-circuits)
15. [A Mathematical Framework for Transformer Circuits: How LLMs...](https://sumityadav.com.np/posts/2026/06/05/mathematical-framework-transformer-circuits/)
16. [TransformerCircuits1: Summary of Results | 3rd layer](https://3rdlayer.uk/posts/framework-01-summary/)