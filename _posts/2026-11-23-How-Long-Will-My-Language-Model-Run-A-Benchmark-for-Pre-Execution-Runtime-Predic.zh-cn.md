---
layout: post
title: "问AI“这活儿要花多长时间？”……结果99%都猜错了？"
description: "大型语言模型（LLM）能预测 AI 任务的执行时间吗？通过 PreRun 基准测试研究，轻松了解 AI 的时间感与现实局限性。"
summary: "根据研究团队开发的 PreRun 基准测试，最新的 AI 模型在仅凭任务描述预测执行时间时，往往会比实际时间短 90% 到 99%，预测严重失准。"
tags: [AI, 基准测试, 机器学习, GPU, PreRun]
image: 2026-11-23-How-Long-Will-My-Language-Model-Run-A-Benchmark-for-Pre-Execution-Runtime-Predic.jpg
image_alt: "插画，展现了尖端超级计算机机房与充满未来感的数字计时器并排闪耀的场景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "无论 AI 变得多么聪明，仅凭直觉很难猜中“物理计算资源的耗时”。这是一个有趣的案例，展示了为什么传统统计模型与 AI 的合作是必不可少的。"
quiz:
  - question: "研究团队为了预测大语言模型和视觉模型的执行时间而引入的新基准测试叫什么名字？"
    choices: ["PreRun", "LiveBench", "TerminalBench"]
    answer: 0
    explanation: "PreRun 是为了在执行前根据可用信息预测深度学习训练与推理运行时间而引入的基准测试。"
  - question: "当开放权重大语言模型（Open-weight LLMs）在没有示例（Few-shot）的情况下处理任务配置时，平均将延迟（Execution latency）低估（缩小预测）了多少？"
    choices: ["10~20%", "50~60%", "90~99%"]
    answer: 2
    explanation: "在没有示例的情况下提问时，开放权重 LLM 表现出严重的误差，将延迟低估了 90% 到 99%。"
  - question: "在对比评估中，用 32 个配置进行训练的哪种传统机器学习方法表现出远优于零样本（Zero-shot）Claude 平均绝对误差的性能？"
    choices: ["随机森林（Random Forest）", "线性回归（Linear Regression）", "支持向量机（SVM）"]
    answer: 0
    explanation: "随机森林（Random Forest）回归模型在使用 32 个配置进行训练时，记录到了远低于 Claude 零样本误差的误差。"
lang: zh-cn
ref: 2026-11-23-How-Long-Will-My-Language-Model-Run-A-Benchmark-for-Pre-Execution-Runtime-Predic
---

想象一下。你租下了一个极其昂贵且庞大的共享厨房（超级计算机 GPU 集群），准备开始做一道极其复杂的菜（大型 AI 模型训练与推理任务）。你问厨房管理员：“这道菜做完准确需要几分钟？”管理员大致扫了一眼菜谱（任务说明书），自信地回答：“嗯，1分钟就能搞定！” 

然而，实际开始做的时候却花了一个多小时（100多分钟），厨房租用费用如滚雪球般飙升。

最近，人工智能（AI）研究界公布了一项同样荒唐却又十分严肃的实验结果。当向大语言模型（LLM，Large Language Model——理解和生成人类语言的大型人工智能）提前询问 AI 模型训练和推理任务需要耗费多长时间时，它们对时间的预测竟然比实际短得离谱 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。这究竟是为什么呢？

---

## 为什么这很重要？

随着 AI 技术的迅猛发展，世界各地的研究人员和企业正在构建和运行无数的深度学习（Deep Learning，模仿人类神经网络让计算机自主学习的技术）模型。在这个过程中，最令人头疼的问题之一就是准确预测**“运行这个 AI 任务需要消耗多少计算机资源，又要花多长时间”** [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。

在现实中，研究人员将任务提交到被称为 GPU（Graphics Processing Unit，快速处理高性能运算的显卡设备）集群的共享计算资源时，必须设置“时间限制（Time limit）”。因为一旦超时，任务就会被强制终止。此外，为了高效分配预算和选择硬件，准确预测运行时间（Runtime）也是必不可少的 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。

于是，人们没有选择每次都进行复杂的数学计算或运行模拟，而是想了一条诱人的捷径——**“把任务说明书交给 AI，问问它要花几分钟！”**这个想法 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。如果 LLM 能够通过阅读文档顺利猜出运行时间，研究人员的工作量将会大幅减轻。然而，我们有必要验证 AI 是否真有这种能力，为此研究团队专门搭建了一个测试平台。

---

## 简单易懂：什么是 PreRun 基准测试？

为了解决这个问题，研究团队引入了一项名为 **PreRun** 的全新基准测试（Benchmark，用于公平比较性能的评估测试）[[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。 

简而言之，**PreRun 就是 AI 模型们的“时间感试卷”**。这份试卷中包含了从实际 GPU 集群中收集的大量记录。具体而言，它包含 801 条语言模型与视觉模型训练（Training）记录，以及 1,884 条推理（Inference，训练好的模型实际生成答案的过程）记录 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。其中任务配置值与明确定义的时间目标值成对出现。此外，它还包含在标准化条件下测量的 64 个文本生成配置（每个配置单独运行 3 次），旨在进行彻底的验证 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。

打个比方，这就好比为了让厨师猜出“用这些材料做两人份意面需要花多少时间”，我们把过去几千次做饭的厨房监控视频和菜谱笔记全部收集了起来，然后看 AI 看着这些笔记能把时间猜得多么精准来进行打分。

通过这项测试，研究团队将三个代表性 AI 模型——**Qwen3.5-9B、GPT-OSS-120B、Claude Opus 5.5**——的实力与传统的统计回归分析模型（Regression baselines，基于数据预测数值关系的传统数学模型）进行了对比 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。

---

## 现状：AI 的时间感达到了什么水平？

实验结果相当令人震惊。尽管 AI 能够极其流利地理解人类语言并进行复杂的编程，但在预测物理计算机任务的执行时间方面，它却暴露出巨大的漏洞。

1. **严重低估（90%~99% 的误差）**：在完全不提供示例（Zero-shot）的情况下让 AI 查看任务配置并询问时间时，开放权重 LLM（Open-weight LLMs，源码公开的开放式人工智能模型）表现出将延迟（Latency，下达指令到出结果所需的延迟时间）**低估了 90% 到 99%** 的情况 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。也就是说，实际上需要 100 分钟的任务，AI 却荒谬地预测“1分钟就行”。
2. **与传统方法的对比**：以 Claude 为例，在没有示例的情况下直接预测（零样本）时，其平均绝对误差（Mean absolute error）比仅用 32 个配置值训练的**随机森林（Random Forest，组合多个决策树以提高预测准确度的传统机器学习算法）**模型高出 **4.5 倍** [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。这意味着仅凭直觉或文本理解能力，AI 并不能很好地衡量硬件所需的物理耗时。
3. **标准答案（示例）的效果**：不过，如果在事前向 AI 提供仅仅 5 个具体的学习示例（Labeled examples），Claude 的文本生成预测误差就会大幅减小。不过，这些示例的效果根据所测量的计时目标会有所不同 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。

这些结果清楚地表明，虽然 AI 读懂文本并理解“这是什么任务”的能力堪称一绝，但它并不能直观地感受到在真实硬件内部电子移动、内存与运算装置碰撞所消耗的物理时间的厚度。

---

## 未来会怎样？

那么，这项研究给我们带来了什么启示？未来 AI 与系统运营的世界将走向何方？

首先，研究团队计划将此次构建的数据和评估管道（Pipeline，数据流经并处理的一系列加工体系）以开源（Open-source，任何人都可以自由使用和修改的公开软件）形式向学术界和工业界公开 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。通过这种方式，世界各地的研究人员能够开展各种后续研究，以提升 AI 的“时间预测能力”。

未来的发展方向大致可以预测如下：
- **混合方法的普及**：结合了 AI 卓越的文档理解能力与传统机器学习（随机森林等）数值计算能力的混合系统将备受瞩目。任务说明书由 AI 阅读，而实际的时间计算则由数学回归模型来弥补。
- **云资源管理的精细化**：运营 GPU 集群的企业将能够在提交任务前更准确地设置时间限制，从而防止计算资源的浪费，减少不必要的开支 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]。

虽然看起来这是一个 AI 能像变魔术一样包办一切的时代，但唯独理解“硬件的物理时间”这一点，依然属于冷酷而准确的数据和统计领域。未来 AI 是否会进化成能够准确预测自身工作时间的聪明助手，让我们拭目以待。

---

## 参考资料

1. [How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)