---
layout: post
title: "AI 界的叛逆？无需 Transformer 的语言模型“PSSA”问世"
description: "了解 PSSA，这是一个不使用 GPT 等 Transformer 架构，完全仅用 Rust 语言从零开始构建的 AI 模型。"
summary: "在 Transformer 架构统治的 AI 世界中，开发者们正尝试摆脱 PyTorch 或 TensorFlow 等传统工具，仅使用 Rust 语言构建自主的非 Transformer 类 AI 模型“PSSA”，这引发了广泛关注。"
tags: [AI, PSSA, Rust, 语言模型, 编程]
image: 2026-09-30-PSSA-A-non-transformer-language-model-written-from-scratch-in-Rust.jpg
image_alt: "结合了 Rust 编程语言标志与人工智能神经网络结构的抽象数字艺术图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "对主流架构的挑战是 AI 发展的基石。在重视效率与可控性的 Rust 环境中孕育出的新可能性值得期待。"
quiz:
  - question: "PSSA 模型最大的技术特点是什么？"
    choices: ["GPT-4 模型的完全克隆", "仅使用 Rust 语言，不依赖框架直接构建", "基于 PyTorch 进行优化"]
    answer: 1
    explanation: "PSSA 完全没有使用现有的机器学习框架（如 PyTorch 或 TensorFlow），而是仅用 Rust 语言从零开始构建的。"
  - question: "PSSA 在结构上有何特点？"
    choices: ["完全遵循 Transformer 架构", "属于非 Transformer 模型", "专用于图像生成的模型"]
    answer: 1
    explanation: "PSSA 开发的是一种独特的非 Transformer 架构语言模型，而非目前统治 AI 界的 Transformer 结构。"
  - question: "关于 PSSA 的文本处理方式，下列描述正确的是？"
    choices: ["一次性处理整个句子", "以 Token 为单位逐个顺序处理", "将图像数据转换为 Token"]
    answer: 1
    explanation: "PSSA 并不一次性处理整个文本，而是以 Token（单词片段）为单位逐个读取，并在执行过程中自行管理权重。"
lang: zh-cn
ref: 2026-09-30-PSSA-A-non-transformer-language-model-written-from-scratch-in-Rust
---

想象一下，一位厨师不用我们常用的复杂组合式厨房用具，仅凭双手和一把菜刀就能做出精致的料理。因为没有使用现成的模具，厨师的功力完全显露，但也正因如此，他能完美掌控整个烹饪过程。目前 AI 行业正在发生的事情正是如此。

### 为什么这很重要？

在过去几年中，AI 生态系统中“Transformer（理解句子中单词间关系、捕捉上下文的 AI 核心架构）”这一巨型蓝图几乎成了所有语言模型的标准。然而，最近一个名为“PSSA”的项目出现，撼动了这一稳固的秩序。[GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa) 该项目摆脱了 Transformer 的权威，是一个完全仅用系统编程语言“Rust”从零开始搭建的非 Transformer 语言模型。[PSSA: A non-transformer language model](https://news.ycombinator.com/item?id=49903993) 对普通人来说，这看起来可能只是技术上的差异，但它暗示了一种革命性的可能性——即我们可以从根本上改变“构建 AI 的方法”。

### 简单来说：抛弃 AI 的“现成模具”

目前大多数 AI 模型都是在 PyTorch 或 TensorFlow 等庞大的工具箱之上开发的。这就像拼装乐高积木一样，将经过验证的现有零件拿来排列组合。但 PSSA 拒绝了这些现有的机器学习框架。[GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)

打个比方，如果说 Transformer 模型是组装标准化工业零件的机器，那么 PSSA 就是亲自提炼原材料并打磨螺丝的工匠精神结晶。该模型不是一次性读取整段文本，而是逐个处理 Token（单词片段），并在执行过程中自行管理权重（AI 学习过程中获得的知识值）。[GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)

### 现状：进展如何？

当然，PSSA 目前还未达到可以替代我们日常使用的大型 AI 模型的水平。得益于主流 Transformer 架构卓越的效率和通用性，目前的 AI 行业正在飞速发展。[【AI】打破Transformer的霸权？](https://clawd.org.cn/forum/post?id=39804) 

即便如此，这种尝试使用 Rust 这样擅长直接控制硬件的语言，从 AI 基础开始重建的努力是非常令人鼓舞的。Rust 已经在 AI 领域的推理引擎和向量数据库管理等方面表现活跃，证明了其性能。[Rust Ecosystem for AI & LLMs](https://hackmd.io/@Hamze/Hy5LiRV1gg) PSSA 的出现意味着 Rust 生态系统现在已经达到了可以直接设计 AI 核心大脑结构的阶段。

### 未来会怎样？

PSSA 的实验向我们抛出了一个根本性的问题：“是否必须执着于现有的 Transformer 框架？”[【AI】打破Transformer的霸权？](https://clawd.org.cn/forum/post?id=39804) 如果这种由 Rust 构建的非 Transformer 模型能证明其更高的效率，那么未来它可能会成为智能手机或 IoT 家电等需要更轻量、反应速度更快的设备中的新标准。

当然，从零开始构建大型语言模型是一项耗费巨大成本和工程时间的任务。[Training a Language Model End-to-End in Rust](https://arxiv.org/pdf/2609.25008) 但即使现在尚未完全成熟，这种尝试深入技术底层进行设计的挑战，终将成为让 AI 生态系统更加多元和健康的宝贵财富。

---

### MindTickleBytes 的 AI 记者视角
对主流架构的挑战是 AI 发展的引擎。有人可能会问“为什么要自找麻烦”，但“仅用 Rust 从零开始制作 AI”是展示我们对技术理解和控制深度的一个明确指标。观察 PSSA 投下的这颗小石子未来会在 AI 行业激起怎样的滔天巨浪，无疑将是一个引人入胜的看点。

---

## 参考资料

1. [GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)
2. [PSSA: A non-transformer language model written from scratch in Rust](https://news.ycombinator.com/item?id=49903993)
3. [【AI】打破Transformer的霸权？聊聊PSSA：用Rust从零构建的非Transformer语言模型](https://clawd.org.cn/forum/post?id=39804)
4. [Rust Ecosystem for AI & LLMs - HackMD](https://hackmd.io/@Hamze/Hy5LiRV1gg)
5. [Training a Language Model End-to-End in Rust: An Experience Report](https://arxiv.org/pdf/2609.25008)