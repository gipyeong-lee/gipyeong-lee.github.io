---
layout: post
title: "AI 会玩吃豆人？测试 AI 实时判断能力的另类基准测试 'Jevman'"
description: "介绍一款名为 'Jevman' 的吃豆人游戏基准测试，该测试旨在评估 AI 模型做出快速、准确决策的能力。"
summary: "探讨开源基准测试项目 'Jevman'，该项目通过观察不同 AI 模型在吃豆人游戏中实时躲避幽灵的过程，衡量其判断的准确性与速度。"
tags: [AI, 基准测试, 吃豆人, Jevman, 决策模型]
image: 2026-10-09-Show-HN-Jevman-AI-decision-models-play-Pac-Man.jpg
image_alt: "在经典吃豆人游戏画面的上方，显示着 AI 模型实时做出决策并享受游戏的场景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "相比复杂的公式，在游戏这种亲切的环境下测试 AI 的判断速度，对于展示模型的实战能力而言，更加直观且有效。"
quiz:
  - question: "Jevman 基准测试的主要目的是什么？"
    choices: ["测试 AI 的图形处理能力", "测试 AI 模型实时做出快速、准确判断的能力", "比拼 AI 玩游戏的时间长短"]
    answer: 1
    explanation: "Jevman 旨在测量 AI 模型在吃豆人游戏环境中快速处理信息并做出正确决策的实时判断能力。"
  - question: "Jevman 中进行的测试方式是怎样的？"
    choices: ["每个模型玩 10 局，共 50 局", "6 个模型参与，每个模型各玩 100 局", "人类与 AI 进行 1 对 1 对决"]
    answer: 1
    explanation: "Jevman 基准测试共有 6 个主流 AI 模型参与，每个模型实时进行 100 局吃豆人游戏以比拼性能。"
  - question: "关于 Jevman 项目的特点，以下哪项描述是正确的？"
    choices: ["只能通过付费服务访问", "不公开测试结果", "它是开源的，任何人都可以提交自己的模型"]
    answer: 2
    explanation: "Jevman 是一个开源项目，用户可以亲自将自己的模型提交到基准测试中以查看其性能。"
lang: zh-cn
ref: 2026-10-09-Show-HN-Jevman-AI-decision-models-play-Pac-Man
---

试想一下，你正坐在街机前操控着吃豆人（Pac-Man）。屏幕里的幽灵正飞速向你追来。此时，你需要在 0.1 秒内决定“是向左走还是向右走？”。对于人类来说，这令人汗流浃背的关键时刻，人工智能（AI）又是如何做出判断的呢？

最近，为了实时测试 AI 的判断力，出现了一个非常有趣的“吃豆人基准测试”，它就是 **Jevman**。

## 为什么这很重要？

我们平时使用的聪明 AI 虽然擅长阅读长文并进行总结，但在需要极短时间内做出即时判断的情况下，表现又如何呢？

Jevman 正是为了考验 AI 的这种“决策（Decision-making）”能力而诞生的。当我们日常让 AI 替我们做决定时，比如“现在马上要带雨伞吗？”或者“该接受这笔投资吗？”，AI 必须在极短时间内分析复杂的情况。吃豆人游戏通过观察幽灵的移动来寻找路径，为模拟这种复杂的决策过程提供了最佳环境。

简而言之，Jevman 是一个“AI 大脑考场”，用于客观评价 AI 是否能够超越简单的语言知识，**在紧急情况下实时、快速且准确地选择正确的行动**。 [[来源: jevman: AI decision models play Pac-Man | VibeLeaderboard](https://www.vibeleaderboard.ai/app/17f8acd3-69b1-4c04-b083-30957220898d)]

## 易于理解的解释

“Jevman”所进行的测试就像是 **“AI 驾驶证路考”**。

1. **状态感知 (State)**: AI 模型作为信息接收方，得知吃豆人当前的位置以及幽灵的位置。 [[来源: GitHub - denis-shvets/jevman-benchmark: Pac-Man driven by the ...](https://github.com/denis-shvets/jevman-benchmark)]
2. **判断 (System One decision)**: 被称为“系统一（System One）”的快速本能决策模型对这些信息进行分析。比喻来说，就像手触碰到热锅时反射性地躲开一样的直觉判断。 [[来源: Jev: System One Decision Model Explained | AIJev](https://aijev.org/)]
3. **行动 (Action)**: AI 根据判断结果，在上下左右四个方向中选择一个来移动吃豆人。 [[来源: GitHub - codaaiteam/jev-pacman: You drive Pac-Man; Jev...](https://github.com/codaaiteam/jev-pacman)]

这个过程以毫秒（ms）为单位反复进行。如果将其比作新手司机看着车道和红绿灯转动方向盘的过程，那么 AI 正在游戏中操控吃豆人的同时，也在积累驾驶技术。目前参加这场考试的 6 个 AI 模型（jev 1.13、kev、clef、clef flash、GPT-6 Luna、Laya 等）各自进行了 100 局吃豆人游戏，以证明各自的判断力。 [[来源: jevman: AI decision models play Pac-Man | TheaterFire](https://theaterfi.re/post/3741604), [来源: Jevman: AI Decision Models Play Pac-Man | VibeLeaderboard](https://www.vibeleaderboard.ai/app/17f8acd3-69b1-4c04-b083-30957220898d)]

## 当前情况

Jevman 不仅仅止步于 AI 玩游戏这一事实。所有游戏记录都是公开的，任何人都可以观看，并且存在一个可以一目了然地确认谁获得了更高分数的 **官方排行榜**。 [[来源: jevman: a Pac-Man benchmark for decision models | OpperAI](https://opper.ai/jevman-benchmark/), [来源: jevman — Six AI decision models play Pac-Man, ranked live](https://launchdaily.info/products/jevman)]

更令人感兴趣的是该项目是 **开源** 的。也就是说，只要是 AI 开发者，任何人都可以将自己的模型注册到 Jevman 基准测试中来测量性能。甚至普通用户也可以在亲自尝试玩吃豆人的同时，实时对比自己与 AI 模型的得分。这实际上确认了“人类的判断力是否真的比 AI 更出色？”这一疑问。 [[来源: jevman · Can you beat the AI at Pac-Man?](https://jevman.apps.chadda.se/), [来源: jevman — Six AI decision models play Pac-Man, ranked live](https://launchdaily.info/products/jevman)]

## 未来将会如何？

像 Jevman 这样基于游戏的基准测试未来将会越来越多。因为 AI 不仅仅停留在炫耀知识的阶段，正在进化为能够控制现实生活中软件、并按照业务规则自动做出决定的“行动型 AI”。

现在，我们在选择 AI 时，将不再仅仅苦恼于“谁说话更好听”，而是“谁在紧急情况下能不出错地做出正确判断”。Jevman 是为了准备那个未来，提供给 AI 们的一处名为“吃豆人游戏”的愉快训练场。

**MindTickleBytes 的 AI 记者视角**: 
AI 阅读浩如烟海的论文并进行创作固然令人惊叹，但观察它们在吃豆人这类紧张刺激的游戏中如何减少失误的过程，感觉就像在观看 AI 的“实战肌肉”，显得更加真实。期待未来出现更多“游戏型基准测试”，能够更加精确地验证 AI 的判断力。

## 参考资料

1. [jevman: a Pac-Man benchmark for decision models | OpperAI](https://opper.ai/jevman-benchmark/)
2. [jevman · Can you beat the AI at Pac-Man?](https://jevman.apps.chadda.se/)
3. [GitHub - joch/jevman: Pac-Man driven by the jev decision model](https://github.com/joch/jevman)
4. [jevman: AI decision models play Pac-Man | TheaterFire](https://theaterfi.re/post/3741604)
5. [Show HN: Jevman – AI decision models play Pac-Man](https://semasocial.com/blog/show-hn-jevman-ai-decision-models-play-pac-man-61213)
6. [jevman — Six AI decision models play Pac-Man, ranked live](https://launchdaily.info/products/jevman)
7. [GitHub - denis-shvets/jevman-benchmark: Pac-Man driven by the ...](https://github.com/denis-shvets/jevman-benchmark)
8. [Jevman: AI Decision Models Play Pac-Man | VibeLeaderboard](https://www.vibeleaderboard.ai/app/17f8acd3-69b1-4c04-b083-30957220898d)
9. [Jev: System One Decision Model Explained | AIJev](https://aijev.org/)
10. [GitHub - codaaiteam/jev-pacman: You drive Pac-Man; Jev...](https://github.com/codaaiteam/jev-pacman)