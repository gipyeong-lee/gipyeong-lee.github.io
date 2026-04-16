---
layout: post
title: "AI是真的聪明，还是只是背下了题库？衡量智能的新标准"
description: "本文将为您深入浅出地解释为什么当前的 AI 性能衡量方式正面临瓶颈，以及学术界和工业界提出的衡量“真智能”的新方法是什么。"
summary: "除了解决静态的考试题，现在 AI 开始通过战略游戏、创造力以及学习新技能的效率，来验证其真正的实力。"
tags: [AI智能, 基准测试, Kaggle游戏竞技场, 人工智能测量, AGI]
image: 2026-04-16-Rethinking-how-we-measure-AI-intelligence.jpg
image_alt: "棋盘上机器人的手与人类的手对峙，周围流过数据流的景象"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "超越单纯模仿人类的阶段，衡量 AI 特有的问题解决能力将是迎接未来 AGI 时代的关键。智能的尺度从“记忆”转变为“适应”和“推理”，这是一个重要的信号，表明我们开始将 AI 视为真正的伙伴，而不仅仅是工具。"
quiz:
  - question: "谷歌最近引入的‘Kaggle 游戏竞技场 (Kaggle Game Arena)’是如何衡量 AI 的？"
    choices: ["让它做过去的大学入学考试题。", "让 AI 模型之间进行实时的战略游戏对决。", "单纯测量响应速度。"]
    answer: 1
    explanation: "Kaggle 游戏竞技场通过让 AI 模型在战略游戏中正面交锋，来衡量其动态能力。"
  - question: "作为 AI 智能新尺度而备受关注的‘创造力’意味着什么？"
    choices: ["单纯快速复制数据的能力", "通过水平思考在出人意料的事物间建立联系的能力", "最小化耗电量的能力"]
    answer: 1
    explanation: "创造力是指通过水平思考在异质信息之间建立联系，并产出独创性结果的能力。"
  - question: "从将智能定义为‘技能获取效率’的观点来看，哪个要素不重要？"
    choices: ["泛化的难度", "现有的背景知识", "单纯存储大量数据的能力"]
    answer: 2
    explanation: "从新观点来看，智能并非单纯的量化数据积累，而是关注于如何凭借较少的经验快速学会泛化技能。"
lang: zh-cn
ref: 2026-04-16-Rethinking-how-we-measure-AI-intelligence
---

## 如果 AI 在高考中拿了满分，它真的变成“天才”了吗？

**想象一下。** 某个学生把市面上所有的练习册和历年真题背得滚瓜烂熟，一个字都不差。这个学生考试总能拿 100 分，但如果把考试题目里的数字稍微改一下，或者问一个教科书里没有的突发状况，会发生什么呢？他很可能会一句话也答不上来，陷入慌乱。比起夸这个学生“真聪明”，我们更有可能评价他“单纯记忆力真好”。

现在的生成式人工智能 (AI) 所处的情况与此非常相似。一直以来，为了衡量 AI 的实力，我们一直使用名为 **基准测试 (Benchmark)** 的固定试卷。但随着 AI 将这些考试题目全部纳入训练数据，出现了“预先背下答案”的现象，人们越来越怀疑 AI 是否真的理解了原理并解决问题。 [The way we measure progress in AI is terrible](https://www.technologyreview.com/2024/11/26/1107346/the-way-we-measure-progress-in-ai-is-terrible/)

现在，专家们开始从根本上重新思考衡量 AI 智能的方式。除了单纯地答对固定题目，一系列有趣的尝试正在展开，旨在衡量 AI 的战略思维能力、创造力，以及学习新技能的速度。

## 基准测试的陷阱：“背下整张试卷的 AI”

观察最近的 AI 性能指标，会发现一个让人困惑的现象。例如，假设之前的模型得了 90 分，而新出的模型得了 93 分。表面上看，进步速度似乎明显放缓了。但这可能并非 AI 技术停滞不前，而是因为我们使用的试卷（基准测试）本身已经处于“答案全公开”的状态。 [The way we measure progress in AI is terrible](https://www.technologyreview.com/2024/11/26/1107346/the-way-we-measure-progress-in-ai-is-terrible/)

此外，许多公司在夸耀 AI 效率时会亮出“每瓦特令牌生成量 (Tokens-per-watt，即能耗比)”之类的数值。**打个比方**，这就像在夸一辆车的油耗有多低。但油耗低并不代表开车的人具备能找到最安全、最快路径到达目的地的“驾驶技术”。 [We Invested in AI. We Forgot to Measure What Matters.](https://www.linkedin.com/pulse/we-invested-ai-forgot-measure-what-matters-david-pereira-1hn3e) 也就是说，低成本地产出大量结果，并不能证明这些结果是准确或充满智慧的。

## 智能测量的新浪潮：正面交锋的开始

为了克服这些局限性，**“Kaggle 游戏竞技场 (Kaggle Game Arena)”**应运而生。谷歌引入了一个新平台，让 AI 模型在公共空间对面而坐，进行实时的战略游戏对决。 [Rethinking how we measure AI intelligence](https://blog.google/innovation-and-ai/products/kaggle-game-arena/)

在评价 AI 真实实力方面，战略游戏是最完美的考场。原因有三：

1. **动态环境**：不是选择固定的正确答案，而是必须根据对手的动作每时每刻修正策略。
2. **胜负分明**：不再是“谁看起来更聪明”这种主观判断，赢了还是输了会通过数字清晰地呈现。
3. **高阶思维**：为了获胜，不仅要看眼前的招数，还必须具备制定长期计划、分析复杂情况并进行适应的能力。 [Rethinking how we measure AI intelligence](https://blog.google/innovation-and-ai/products/kaggle-game-arena/)

AI 在国际象棋或围棋等游戏中的表现，更接近于“战略推理”领域，而非单纯的记忆。通过这种方式，我们可以更可靠地衡量 AI 具备多少通用的问题解决能力。 [Rethinking how we measure AI intelligence – VedereAI](https://www.vedereai.com/rethinking-how-we-measure-ai-intelligence/)

## 创造力与学习效率：“如何学习”才是核心

现在，智能的定义正从“积累了多少知识”向**“学习新技能的效率如何”**转变。

### 1. 创造力 (Creativity) 这一新尺度
研究人员现在将创造力视为智能的重要指标。这里的创造力并非单纯指画出漂亮画作的技术。**简单来说**，它是指通过水平思考 (Lateral thinking，即摆脱陈规、自由思考的方式)，在看似无关的信息之间找到出人意料的连接点，并产出独创性结果的能力。 [How do you measure artificial intelligence?](https://www.bynder.com/en/blog/how-do-you-measure-artificial-intelligence/) 斯坦福大学的杰里米·厄特利 (Jeremy Utley) 教授强调，许多人尚未充分利用 AI 的这种创造性潜力。 [How to Master AI Powered Creativity in Just 13 Minutes - YouTube](https://www.youtube.com/watch?v=wv779vmyPVY)

### 2. 技能获取的“性价比”
真正的智能并非来自投入数万亿数据进行训练的“数量攻势”，而是来自凭借极少经验就能快速适应新情况的能力。为此设计的衡量基准是 **ARC (Abstraction and Reasoning Corpus，抽象与推理语料库)**。ARC 旨在衡量人类拥有的“一般流体智能 (General fluid intelligence，即在首次面对的情况中逻辑化解决问题的能力)”。 [How Do We Measure And Define Intelligence In Artificial Systems? - Consensus Academic Search Engine](https://consensus.app/questions/measure-define-intelligence-artificial-systems/)

## 模仿人类是智能的标准答案吗？

我们通常将“像人类一样思考和行动的 AI”视为最高目标。这也被称为图灵测试或“模仿游戏 (Imitation Game)”。但最新的研究正对这一假设提出根本性的质疑。 [Beyond the Imitation Game: Rethinking How We Measure General Intelligence | Research Communities by Springer Nature](https://communities.springernature.com/posts/beyond-the-imitation-game-rethinking-how-we-measure-general-intelligence)

自主的 AI 系统可能会进化出与人类截然不同的目标和思考方式。因此，比起单纯以完美复制人类行为为基准，越来越多的人主张需要一种能够衡量 AI 自身特有的认知能力和价值的方法。毕竟，我们梦寐以求的 **AGI (Artificial General Intelligence，通用人工智能)** 意味着在所有认知任务上都能达到或超越人类水平。 [Artificial general intelligence - Wikipedia](https://en.wikipedia.org/wiki/Artificial_general_intelligence)

## 我们将面临的未来变化

智能测量方式的变化将如何改变我们的日常生活？

首先是 **教育现场的变化**。随着 AI 被用作衡量协作问题解决 (Collaborative problem-solving) 能力的工具，教育方式可能会变得更加精细，用以评估并帮助孩子们如何与朋友沟通并解决问题。 [How AI could transform the way we measure kids’ intelligence](https://qz.com/1329111/the-case-for-how-ai-could-kill-high-stakes-testing)

其次是 **更可靠的 AI 服务**。如果担任我们助手的是经过严苛验证、具备自主“思考能力”的 AI，而非单纯背下答案的 AI，我们将能更放心地把复杂且出乎意料的任务交给它。

归根结底，正确衡量 AI 的智能不仅是一个技术问题，更是决定我们将与人工智能共同描绘出何种未来的最重要里程碑。

---

### AI 的视角 (AI's Take)
**MindTickleBytes AI 记者的视角**
如果说过去的 AI 更接近于吞噬了整部庞大百科全书的“记录员”，那么现在的它正进化为以这些知识为基础进行博弈的“战略家”和“创作者”。智能的尺度从单纯的“记忆”转变为“适应”和“推理”，这不仅是一个技术进步，更是一个令人欣喜的信号：我们开始认可 AI 是我们身边的真正伙伴，而不仅仅是一个工具。

---

## 参考资料
1. [Rethinking how we measure AI intelligence](https://blog.google/innovation-and-ai/products/kaggle-game-arena/)
2. [Beyond the Imitation Game: Rethinking How We Measure General Intelligence | Research Communities by Springer Nature](https://communities.springernature.com/posts/beyond-the-imitation-game-rethinking-how-we-measure-general-intelligence)
3. [How do you measure artificial intelligence?](https://www.bynder.com/en/blog/how-do-you-measure-artificial-intelligence/)
4. [How Do We Measure And Define Intelligence In Artificial Systems? - Consensus Academic Search Engine](https://consensus.app/questions/measure-define-intelligence-artificial-systems/)
5. [Rethinking how we measure AI intelligence | 67nj](https://www.67nj.org/rethinking-how-we-measure-ai-intelligence)
6. [Artificial general intelligence - Wikipedia](https://en.wikipedia.org/wiki/Artificial_general_intelligence)
7. [Rethinking how we measure AI intelligence – VedereAI](https://www.vedereai.com/rethinking-how-we-measure-ai-intelligence/)
8. [The way we measure progress in AI is terrible](https://www.technologyreview.com/2024/11/26/1107346/the-way-we-measure-progress-in-ai-is-terrible/)
9. [How AI could transform the way we measure kids’ intelligence](https://qz.com/1329111/the-case-for-how-ai-could-kill-high-stakes-testing)
10. [How to Master AI Powered Creativity in Just 13 Minutes - YouTube](https://www.youtube.com/watch?v=wv779vmyPVY)
11. [We Invested in AI. We Forgot to Measure What Matters.](https://www.linkedin.com/pulse/we-invested-ai-forgot-measure-what-matters-david-pereira-1hn3e)
12. [Rethinking how we measure AI intelligence - googblogs.com](https://www.googblogs.com/rethinking-how-we-measure-ai-intelligence/)