---
layout: post
title: "把编码交给AI，成本竟差了17倍？“哈内斯”（Harness）的秘密"
description: "研究结果显示，即使使用相同的AI模型，根据编码代理系统（哈内斯）的不同，成本最高可相差17.5倍。"
summary: "对9个AI编码代理系统进行相同模型的测试结果表明，虽然性能相近，但运营成本最高存在17.5倍的差异。"
tags: [AI, 编码, 降本增效, 生产力, 技术趋势]
image: 2026-09-03-Show-HN-FrontierHarness-Eval-9-harness-same-model-cost-per-pass-varies-17x.jpg
image_alt: "可视化展示不同AI系统执行复杂编码任务的图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这表明，除了AI模型的智能水平外，运营模型的‘系统设计（哈内斯）’在成本效率方面也起着决定性作用。"
quiz:
  - question: "本次研究中，在对比9个AI编码系统时，没有固定的因素是？"
    choices: ["AI模型", "软件工程任务", "系统运营成本"]
    answer: 2
    explanation: "研究的核心在于衡量在固定模型、任务和运行时环境的情况下，成本将如何变化。"
  - question: "通过更换AI编码哈内斯（harness），无法改变的要素是？"
    choices: ["任务成功率", "缓存行为方式", "AI模型的基础智能"]
    answer: 2
    explanation: "哈内斯仅是控制模型的方式，并不能提升模型本身的智能。"
  - question: "在执行相同任务时，根据哈内斯设置，成本最高出现了多少倍的差异？"
    choices: ["约5倍", "约17.5倍", "约30倍"]
    answer: 1
    explanation: "研究结果显示，在12种设置下，成本最高出现了17.5倍的差异。"
lang: zh-cn
ref: 2026-09-03-Show-HN-FrontierHarness-Eval-9-harness-same-model-cost-per-pass-varies-17x
---

试想一下，你雇用了两位精明能干的秘书。两人均毕业于同一所大学，受过同样的教育，具备相同的业务处理能力。但如果其中一人完成工作只需1万元，而另一人做同样的事情却要花17.5万元，你会怎么做？

最近在人工智能（AI）编码领域出现了一个有趣的现象，情况与此非常相似。随着AI模型变得越来越聪明，委托其处理编码任务已变得司空见惯，但人们发现，根据处理这些任务的“方式”不同，成本竟会天差地别。

## 为什么这很重要？

对于企业或开发者而言，利用AI开发软件时，最重要的因素无疑是“成本”和“结果”。如果说过去人们只关注“哪个AI模型更聪明？”，那么现在，如何高效地驾驭这些模型则显得更为重要。如果有一种方法能在保持同样性能的同时，将成本降低17倍以上，那么企业的生产力将产生质的飞跃。

## 通俗易懂：什么是哈内斯（Harness）？

“哈内斯（harness）”这个术语可能让人感到陌生。简单来说，你可以把它理解为**将AI模型投入编码工作现场并进行管理的“系统外壳”**。

我们可以这样比喻：
- **AI模型**：一位具备极高专业能力的“天才开发者”。
- **哈内斯**：为这位开发者准备工具（计算机、参考书、搜索工具等）、下达指令并审核最终成果的“项目经理”。

这项研究（[FrontierHarness Eval](https://frontierharness.org/)）分析了即便雇用的是同一个天才开发者（相同的AI模型），根据管理他的项目经理（哈内斯）是谁，其工作处理方式及所耗费的成本会有多大差异。研究小组调用了9个不同的哈内斯，让它们各自完成30个相同的软件工程任务。[出处: Introducing FrontierHarness Eval — RUNTA](https://runta.com/blog/introducing-frontier-harness-eval/)

研究发现，即便保持模型和任务环境相同，根据哈内斯设置的不同，成功率、执行速度以及缓存（临时存储数据）的使用方式也都各不相同。[出处: GitHub - frontier-harness-eval/eval](https://github.com/frontier-harness-eval/eval)

## 现状：成本差距达17.5倍

该研究最令人震惊的结果是成本。[出处: GitHub - runta-dev/frontier-harness-eval](https://github.com/runta-dev/frontier-harness-eval) 研究小组对比了12种哈内斯设置，结果显示即使是同一个任务，成本竟然出现了高达**17.5倍**的差异。[出处: Samemodel. Similarpassrates. 17.5xcostdifferences across 12...](https://frontierharness.org/)

也就是说，即使下达的是同样的编码任务，根据所使用的系统不同，本来只需花1万元的工作，最终却可能耗费17.5万元。这表明，仅仅模型聪明并不能解决所有问题。如何设计哈内斯，决定了AI的判断力，它甚至可以通过减少无效提问来节省成本。[出处: GitHub - runta-dev/frontier-harness](https://github.com/runta-dev/frontier-harness)

## 未来会如何发展？

这一结果为生活在AI时代的我们提供了重要启示。未来，竞争将不仅限于寻找“高性能AI模型”，而是转向如何通过“高效设计”以最小化模型调用次数并获取最佳结果。

对用户而言，今后在使用AI时，除了考虑“这个模型有多聪明？”，还必须评估“这个AI处理工作的系统（哈内斯）有多高效？”。随着该领域研究的深入，我们将迎来一个能以更低成本、更快速度构建高质量软件的时代。

## MindTickleBytes的AI记者视角

AI的智能属于模型本身，但如何明智地利用这种智能来优化成本，则属于人类的职责。这就好比有的经理雇用了一位天才，却只让他做大量不必要的文书工作；而有的经理则能通过明确的指导将工作效率发挥到极致。随着技术的不断精进，最终决定企业和个人竞争力的，将是驾驭系统的“运营智慧”。

## 参考资料

1. [Samemodel. Similarpassrates. 17.5xcostdifferences across 12...](https://frontierharness.org/)
2. [GitHub - runta-dev/frontier-harness-eval: Public results and task...](https://github.com/runta-dev/frontier-harness-eval)
3. [Introducing FrontierHarness Eval — RUNTA](https://runta.com/blog/introducing-frontier-harness-eval/)
4. [GitHub - frontier-harness-eval/eval: Public results and task ...](https://github.com/frontier-harness-eval/eval)
5. [GitHub - runta-dev/frontier-harness: Public results and task ...](https://github.com/runta-dev/frontier-harness)
6. [Show HN: FrontierHarness Eval – 9 种评测方案，同一模型，单次成本...](https://memedata.com/post/143010)
7. [HackerNews– Telegram](https://t.me/hackernewslive/231515)