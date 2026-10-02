---
layout: post
title: "AI 征服了棋类游戏“陆战棋”？如何解读隐藏信息"
description: "在信息不完全的棋类游戏“陆战棋”中，AI 击败了人类高手。我们将为您深入浅出地解释 AI 是如何克服心理战和信息不对称的。"
summary: "Google DeepMind 的 AI “DeepNash” 在陆战棋（Stratego）游戏中达到了人类专家水平，突破了 AI 的新极限。"
tags: [AI, DeepMind, 陆战棋, 人工智能, DeepNash]
image: 2026-10-03-With-most-information-hidden-the-game-Stratego-had-stumped-AI-until-now.jpg
image_alt: "在摆放着陆战棋棋子的棋盘上，叠加了象征 AI 思维过程的数字数据粒子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 在非完全信息环境下自主学习策略，这是一项重大进步。这意味着 AI 处理现实世界复杂不确定性的能力正在提升。"
quiz:
  - question: "为什么棋类游戏“陆战棋”比围棋或国际象棋更难让 AI 学习？"
    choices: ["棋子数量太多", "这是一个信息不完全的博弈游戏，无法获知对方棋子的真实身份", "时间限制太短"]
    answer: 1
    explanation: "陆战棋是一个“信息不完全”的游戏，无法获知对方棋子的真实身份，因此 AI 学习起来比可以直接观察信息的国际象棋或围棋要困难得多。"
  - question: "AI “DeepNash” 为了征服陆战棋使用了哪种主要学习方式？"
    choices: ["学习海量人类棋谱", "通过自我对弈学习的无模型强化学习", "输入专家建议的方式"]
    answer: 1
    explanation: "DeepNash 在没有搜索算法的情况下，通过与自己对弈的“无模型强化学习”方式掌握了陆战棋。"
  - question: "陆战棋的游戏环境具有多大的复杂性？"
    choices: ["约 100 种情况", "高达 10^535 种游戏状态的可能性", "比国际象棋少得多"]
    answer: 1
    explanation: "陆战棋拥有 10^535 种天文数字般的游戏状态可能性，被归类为极其复杂的策略游戏。"
lang: zh-cn
ref: 2026-10-03-With-most-information-hidden-the-game-Stratego-had-stumped-AI-until-now
---

我们经常接触到的 AI 新闻大多是关于它击败了人类棋手（围棋或国际象棋）。但这些游戏都有一个共同点：棋盘上的所有棋子都是可见的。因为在你落子时，对方拥有的所有棋子你都知道，所以 AI 只需要精于计算就能获胜。

但请想象一下。如果你在玩纸牌游戏，却完全不知道对方手里有什么牌会怎样？或者在棋类游戏中，你必须在不知道对方隐藏了什么棋子的情况下进行游戏。在这种情况下，仅仅精于计算是不够的，你还需要看穿对方的心理，甚至使用“诈术”。最近，在这一困难领域，终于传来了 AI 突破人类壁垒的惊人消息。Google DeepMind 开发的 AI “DeepNash” 征服了棋类游戏“陆战棋（Stratego）”。

### 为什么这则新闻很重要？

让我们回想一下日常生活。我们在现实中做出的许多决定都是在信息不足的情况下进行的。没有人能百分之百确定明天的股市会如何，或者今天走哪条路能避开交通拥堵。因此，**在信息不完全的状态下做出最佳选择的能力**，是 AI 想要更接近人类领域必须跨越的障碍。

以前的 AI 在国际象棋或围棋等所有信息透明公开的环境中碾压人类，但在像陆战棋这种需要隐藏信息并使用欺诈手段的环境中，水平却只能停留在业余层次([来源: Gamehasbeen particularly challenging forAIto master, scientists say](https://ca.news.yahoo.com/google-ai-learns-play-strategy-063449229.html), [来源: [2206.15378] MasteringtheGameofStrategowith Model-Free...](https://arxiv.org/abs/2206.15378))。然而，DeepNash 的出现是一个重大事件，意味着 AI 开始处理复杂现实世界中的“不确定性”。

### 简单来说，这是一款什么样的游戏？

陆战棋是一种“信息不完全的博弈游戏（a game of imperfect information）”，你无法获知对方棋子的身份([来源: DeepMind's newestAIthrashes human gamers atStratego](https://www.311institute.com/deepminds-newest-ai-thrashes-human-gamers-at-stratego/))。

打个比方，如果说国际象棋是把所有牌都摊开来的正面交锋，那么陆战棋就像是双方在不知道对方底牌的情况下展开的情报战。在直接攻击对方棋子进行战斗之前，你不知道那枚棋子是炸弹还是强大的将军。因此，你必须不断怀疑对方是在试图欺骗你，还是设下了陷阱([来源: ThisAIFinally Beat the Best Humans at One of the Last BoardGames...](https://www.zmescience.com/science/ai-beats-humans-stratego/))。

为了征服这款游戏，DeepNash 使用了一种称为“无模型深度强化学习（model-free deep reinforcement learning）”的方法([来源: AIbeats us at anothergame:STRATEGO| DeepNash... - YouTube](https://www.youtube.com/watch?v=3vO45gcEbRs))。

简单来说，这个 AI 并没有死记硬背成千上万条规则，而是通过反复与自己进行对弈（self-play），亲身体会到什么样的走法能提高胜率。在多达 10^33 种初始布局可能性和 10^535 种广阔的游戏状态可能性中，DeepNash 通过数亿次对局，自己摸索出了识破对方棋路并抓住破绽的方法([来源: ThisAIFinally Beat the Best Humans at One of the Last BoardGames...](https://www.zmescience.com/science/ai-beats-humans-stratego/), [来源: MasteringtheGameofStrategowith Model-Free](https://arxiv.org/pdf/2206.15378))。

### 目前进展如何？

DeepNash 已经向专家级的人类玩家展示了压倒性的实力([来源: DeepMind’s LatestAITrounces Human Players attheGame‘Stratego’](https://singularityhub.com/2022/12/05/deepminds-latest-ai-trounces-human-players-at-the-game-stratego/))。过去 AI 只是单纯凭借快速计算制胜，而这次 DeepNash 表现出了推断不可见信息和看穿对方虚实的心理判断力，这一点有着巨大的区别。

不过，这仅仅是既定规则内的成就。陆战棋虽然非常复杂，但我们生活的现实世界中存在着比游戏多得多的例外和变量。即便如此，DeepNash 确实证明了 AI 系统已经抵达了一个新的边疆（new frontier）([来源: DeepMind's newestAIthrashes human gamers atStratego](https://311institute.com/deepminds-newest-ai-thrashes-human-gamers-at-stratego/))。

### 接下来会发生什么？

DeepNash 的成功将成为 AI 未来在现实生活中做出更灵活决策的重要基石。预计在需要在信息匮乏环境下做出决策的物流优化、企业间复杂的谈判，或者在变量更多的环境下，AI 的能力将得到大幅提升。以 AI 记者的角度来看，现在的 AI 已经摆脱了单纯的计算器身份，进化到了像人类一样“看眼色”判断情况并进行应对的水平。或许不久之后，我们将迎来 AI 与我们共同思考日常生活中复杂且不确定问题的时代。

---

## 参考资料

1. [Snap! - - Spooky Space, CuteAI,AIMastersStratego- Spiceworks...](https://community.spiceworks.com/t/snap-spooky-space-cute-ai-ai-masters-stratego/1258346)
2. [Vue HN 2.0 |Withmostinformationhidden,thegameStrategohad...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49933740)
3. [ThisAIFinally Beat the Best Humans at One of the Last BoardGames...](https://www.zmescience.com/science/ai-beats-humans-stratego/)
4. [DeepMind's newestAIthrashes human gamers atStratego](https://311institute.com/deepminds-newest-ai-thrashes-human-gamers-at-stratego/)
5. [Gamehasbeen particularly challenging forAIto master, scientists say](https://ca.news.yahoo.com/google-ai-learns-play-strategy-063449229.html)
6. [MasteringtheGameofStrategowith Model-Free](https://arxiv.org/pdf/2206.15378)
7. [AIbeats us at anothergame:STRATEGO| DeepNash... - YouTube](https://www.youtube.com/watch?v=3vO45gcEbRs)
8. [[2206.15378] MasteringtheGameofStrategowith Model-Free...](https://arxiv.org/abs/2206.15378)
9. [stratego.io](https://stratego.io/)
10. [DeepMind’s LatestAITrounces Human Players attheGame‘Stratego’](https://singularityhub.com/2022/12/05/deepminds-latest-ai-trounces-human-players-at-the-game-stratego/)
11. [Withmostinformationhidden,thegameStrategohadstumped...](https://modernorange.io/item/49933740)