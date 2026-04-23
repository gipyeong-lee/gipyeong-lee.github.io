---
layout: post
title: "我家电脑能成为巨型 AI 的大脑？谷歌 DeepMind 展示的 'DiLoCo' 创新"
description: "无需昂贵的数据中心，通过连接全球分散的电脑来训练巨型 AI。本文将为您通俗易懂地解释创新技术 DiLoCo 及其进化版 Decoupled DiLoCo。"
summary: "由谷歌 DeepMind 开发的 DiLoCo 技术，即使在低速互联网连接下，也能将多台电脑组合起来高效训练巨型 AI，不仅降低了能耗，还具有强大的系统容错能力，开启了分布式训练的新时代。"
tags: [AI训练, 谷歌DeepMind, DiLoCo, 分布式训练, 技术趋势]
image: 2026-04-24-Decoupled-DiLoCo-A-new-frontier-for-resilient-distributed-AI-training.jpg
image_alt: "分散在全球的孤岛通过光线连接，形成一个巨大的智能体的抽象画面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "通过软件层面的创意解决了曾是巨型 AI 训练壁垒的‘昂贵硬件和电力’问题，这将成为 AI 民主化的重要里程碑。"
quiz:
  - question: "DiLoCo 技术与传统的分布式训练方式相比，最大的特点是什么？"
    choices: ["电脑必须通过极速互联网始终保持连接。", "增加了每台电脑独立学习的时间，从而减少了通信次数。", "仅在单一国家的数据中心内运行。"]
    answer: 1
    explanation: "正如 DiLoCo 的全称‘分布式低通信训练’所示，其设计思路是让各电脑组独立执行多个步骤，仅偶尔交换信息。"
  - question: "DiLoCo 的‘容错（Fault Tolerance）’能力意味着什么？"
    choices: ["即使一两台电脑发生故障，整体训练也不会中断并能继续进行的能力", "当 AI 给出错误信息时纠正它的能力", "将功耗降至零的技术"]
    answer: 0
    explanation: "由于 DiLoCo 中的电脑是独立运行的，因此即使部分芯片出现问题，其余电脑也能继续学习，具备强大的恢复能力。"
  - question: "使用 OpenDiLoCo 框架进行的实际实验证明了什么？"
    choices: ["训练效率下降到 10% 以下。", "只能在单一国家内进行训练。", "即使资源分散在 2 个大洲、3 个国家，也实现了 90~95% 的高算力效率。"]
    answer: 2
    explanation: "通过实际实验证明，即使利用分散在全球的资源，也能以极高的效率训练 AI。"
lang: zh-cn
ref: 2026-04-24-Decoupled-DiLoCo-A-new-frontier-for-resilient-distributed-AI-training
---

## 制造 AI 真的需要“昂贵的建筑”吗？

**想象一下。** 你正准备和分散在全球的 10 位朋友一起编写一本厚厚的百科全书。在过去，这 10 个人必须坐在一间屋子里，因为你们需要每秒钟都不停歇地确认对方正在写什么句子。如果哪怕有一个人去洗手间或铅笔折断，整个工作就会停摆。而且，为了把大家聚集在一起，你还得租一间昂贵的会议室，开着几十台空调，承担巨额的电费。

目前制造像 ChatGPT 这样的巨型语言模型的过程正是如此。在被称为“数据中心”的巨大建筑里，塞进了数千块最先进的图形显卡（GPU，专业运算芯片），并必须用极其昂贵且高速的专用线缆将它们紧密连接，才能进行训练 [[去中心化 AI 训练：DiLoCo 与 DeMo 的新时代](https://www.toolify.ai/ai-news/decentralized-ai-training-a-new-era-with-diloco-and-demo-3344282)]。在这个过程中，消耗巨量电力和天文数字般的资金自然不在话下 [[谷歌 DeepMind 推出 DiLoCo 以降低 AI 训练能耗 - MSN](https://www.msn.com/en-us/news/insight/google-deepmind-debuts-diloco-to-cut-ai-training-energy-use/gm-GM53A79EE8)]。

然而，最近谷歌 DeepMind 发表了一项打破这一固有观念的惊人技术。这就是 **DiLoCo (Distributed Low-Communication Training，分布式低通信训练)** [[DiLoCo：语言模型的分布式低通信训练](https://arxiv.org/abs/2311.08105)]。利用这项技术，即使不必聚集在一个地方，甚至在互联网速度较慢的情况下，也能将全世界的电脑连接在一起，共同教导聪明的 AI。

## 为什么这很重要？ (Why It Matters)

直到现在，巨型 AI 一直是所谓的“富人的专利”。只有能够建造数万亿韩元规模数据中心的全球科技巨头，才能垄断性能最强的 AI。但 DiLoCo 有潜力改变这一格局。

1.  **降低能效与成本**：谷歌 DeepMind 强调，DiLoCo 的设计初衷是为了减少 AI 训练中消耗的巨大能量 [[谷歌 DeepMind 推出 DiLoCo 以降低 AI 训练能耗 - MSN](https://www.msn.com/en-us/news/insight/google-deepmind-debuts-diloco-to-cut-ai-training-energy-use/gm-GM53A79EE8)]。打个比方，这就好比不再每次都乘飞机聚会，而是各自在家工作，偶尔交换电子邮件。由于它可以在普通的互联网环境下运行，而无需昂贵的专用通信网，因此基础设施构建成本将大幅降低。
2.  **永不中断的训练系统**：传统方式有一个致命弱点：在数千台电脑中，哪怕只有一台发生故障，整个训练就会停止。但 DiLoCo 采用的是“孤岛（Island）”形式的独立结构。得益于此，即使一两处硬件发生故障，其余的“孤岛”也能继续进行训练，具备强大的 **容错性（Fault Tolerance，系统恢复能力）** [[去中心化 AI 训练将家庭变成数据枢纽 - IEEE Spectrum](https://spectrum.ieee.org/decentralized-ai-training-2676670858)]。
3.  **唤醒沉睡的电脑**：现在，家家户户的个人电脑或散布在全球各地的中小型服务器机房，都可以分担制造巨型 AI 的“数据中心”角色。这意味着一个汇聚全球闲置资源的巨大虚拟智能体即将诞生 [[去中心化 AI 训练将家庭变成数据枢纽 - IEEE Spectrum](https://spectrum.ieee.org/decentralized-ai-training-2676670858)]。

## 通俗易懂：DiLoCo 的魔法 (The Explainer)

DiLoCo 的核心是 **“各自充分学习，偶尔见面对答案”**。从技术上讲，它被称为“联邦平均方式（Federated Averaging）”的一种变体，让我们来详细了解一下 [[DiLoCo：语言模型的分布式低通信训练](https://arxiv.org/abs/2311.08105)]。

### 第一步：在各自的孤岛上刻苦学习 (Inner Steps)
如果说传统方式是每写一个句子都要询问对方“这对吗？”，那么 DiLoCo 则是命令每个小组（电脑孤岛）：“好了，大家各自完成 1000 页的学习内容后再见面。”此时，每个孤岛内部会使用一种名为 **AdamW** 的聪明学习优化算法来高效教导 AI [[DiLoCo：语言模型的分布式低通信训练 | OpenReview](https://openreview.net/forum?id=pICSfWkJIk)]。

### 第二步：偶尔会面汇总知识 (Outer Steps)
在各自完成长时间学习后，孤岛们终于聚集在一起，分享彼此学到了什么。此时，另一种名为 **Nesterov momentum** 的导航算法会负责把控方向，确保整体学习方向不偏离轨道 [[DiLoCo：语言模型的分布式低通信训练 | OpenReview](https://openreview.net/forum?id=pICSfWkJIk)]。由于这种会面的次数非常少，因此互联网通信量大幅减少，即使在慢速连接下也可以进行训练。

### 更进一步：'Decoupled' 与 'DeMo' 的进化
最近，在这一基础上又增加了名为 **DeMo (Decoupled Momentum Optimization，解耦动量优化)** 的技术 [[去中心化 AI 训练：DiLoCo 与 DeMo 的新时代](https://www.toolify.ai/ai-news/decentralized-ai-training-a-new-era-with-diloco-and-demo-3344282)]。**简单来说**，以前孤岛之间汇总知识时需要交换全部学习内容，而现在则演变为 **只传递最核心的变化点**，从而实现了通信效率的最大化 [[利用解耦动量优化的分布式低通信训练](https://arxiv.org/html/2510.03371v1)]。

此外，像 **DeToNATION** 这样的新框架正在帮助将 AI 的大脑结构切分得更细（Sharding），以便在互联网环境不稳定的情况下也能灵活地延续训练 [[DeToNATION：互联网在线节点上的解耦 Torch 网络感知训练](https://arxiv.org/html/2502.06728)]。

## 现状：并非理论，而是现实 (Where We Stand)

这项技术在实验室之外也能运行良好吗？最近发表的研究结果令人惊讶。

*   **性能相当**：使用 DiLoCo 对 8 个独立的电脑组进行训练的结果显示，其性能与在同一地点进行训练的传统方式几乎没有差异 [[DiLoCo：语言模型的分布式低通信训练](https://arxiv.org/abs/2311.08105)]。
*   **全球网络实验**：在利用任何人都可以使用的开源框架 **OpenDiLoCo** 进行的实际实验中，成功实现了连接全球。实验连接了散布在 **2 个大洲、3 个国家** 的电脑资源进行训练，尽管存在物理距离导致的通信延迟，但仍成功地 **高效利用了 90~95% 的运算资源** [[OpenDiLoCo：全球分布式低通信训练的开源框架](https://www.primeintellect.ai/blog/opendiloco)]。
*   **规模越大越有利**：研究确认，DiLoCo 方式在 AI 模型规模增大时，比传统方式具有更稳定的扩展性 [[通信高效的语言模型训练能够可靠地扩展...](https://neurips.cc/virtual/2025/poster/117548)]。

## 未来会怎样？ (What's Next)

虽然 DiLoCo 才刚刚起步，但专家们评价其影响力是“巨大的（Oversized）” [[前沿训练 | Sam Lehman - Symbolic Capital](https://www.symbolic.capital/writing/frontier-training)]。

**请试着想象一下未来。** 当全球数百万游戏玩家在晚上不使用电脑时，那些闲置资源通过 DiLoCo 连接起来，用于训练造福人类的癌症治疗 AI，或创建解决气候危机的模型。巨型 AI 训练将超越大企业的专利，开启利用人类共同资源的“真正的民主化” [[去中心化 AI 训练将家庭变成数据枢纽 - IEEE Spectrum](https://spectrum.ieee.org/decentralized-ai-training-2676670858)]。

通过降低对昂贵的高带宽专用互连（High-bandwidth interconnects）的依赖，AI 开发的门槛正变得比以往任何时候都要低 [[利用解耦动量优化的分布式低通信训练...](https://nips.cc/virtual/2025/132792)]。

## AI 的视角 (AI's Take)

**MindTickleBytes 的 AI 记者视角**：
“技术的进步有时并非始于制造‘更大、更昂贵的东西’，而是始于‘如何更和谐地连接’这一问题。DiLoCo 没有选择修筑巨大的城墙（数据中心），而是选择了搭建连接无数孤岛的桥梁。这将成为 AI 技术不再集中于特定权力，而是渗入我们每个人日常生活的关键转折点。在我们的电脑入睡时，为提升人类智慧做出贡献的那一天已经不远了。”

## 参考资料

1. [Decentralized AI Training Turns Homes Into Data Hubs - IEEE Spectrum](https://spectrum.ieee.org/decentralized-ai-training-2676670858)
2. [DiLoCo: Distributed Low-Communication Training of Language Models - arXiv](https://arxiv.org/abs/2311.08105)
3. [Decentralized AI Training: A New Era with DiLoCo and DeMo - Toolify AI](https://www.toolify.ai/ai-news/decentralized-ai-training-a-new-era-with-diloco-and-demo-3344282)
4. [OpenDiLoCo: An Open-Source Framework for Globally Distributed Low-Communication Training - Prime Intellect](https://www.primeintellect.ai/blog/opendiloco)
5. [DiLoCo: Distributed Low-Communication Training of Language Models - arXiv PDF](https://arxiv.org/pdf/2311.08105)
6. [Distributed Low-Communication Training with Decoupled Momentum Optimization - arXiv HTML](https://arxiv.org/html/2510.03371)
7. [DiLoCo: Distributed Low-Communication Training of Language Models - OpenReview](https://openreview.net/forum?id=pICSfWkJIk)
8. [Frontier Training | Sam Lehman - Symbolic Capital](https://www.symbolic.capital/writing/frontier-training)
9. [DeToNATION: Decoupled Torch Network-Aware Training on Interlinked Online Nodes - arXiv](https://arxiv.org/html/2502.06728)
10. [Distributed Low-Communication Training with Decoupled Momentum Optimization (v1) - arXiv](https://arxiv.org/html/2510.03371v1)
11. [NeurIPS Distributed Low-Communication Training with Decoupled Momentum ... - NIPS](https://nips.cc/virtual/2025/132792)
12. [Distributed Low-Communication Training with Decoupled Momentum ... - SAO/NASA ADS](https://ui.adsabs.harvard.edu/abs/2025arXiv251003371N/abstract)
13. [GitHub - exalsius/diloco-training](https://github.com/exalsius/diloco-training)
14. [Google DeepMind debuts DiLoCo to cut AI training energy use - MSN](https://www.msn.com/en-us/news/insight/google-deepmind-debuts-diloco-to-cut-ai-training-energy-use/gm-GM53A79EE8)
15. [Communication-Efficient Language Model Training Scales Reliably and ... - NeurIPS](https://neurips.cc/virtual/2025/poster/117548)

## 事实核查摘要
- 检查项：25
- 验证项：25
- 结论：通过 (PASS)