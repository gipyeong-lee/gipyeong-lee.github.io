---
layout: post
title: "AI 真的聪明吗？事实上它们甚至可能连“基础算术”都不会"
description: "会像人一样说话的 AI，为什么在计算或逻辑问题面前会给出离谱的答案？本文探讨了大语言模型（LLM）意想不到的局限性及其成因。"
summary: "尽管大语言模型（LLM）具备卓越的语言能力，但由于缺乏实际计算能力、逻辑一致性以及对物理世界的理解，它们在处理重要任务时可能会犯下致命错误。"
tags: [AI, LLM, 技术分析, 人工智能]
image: 2026-08-26-Ask-HN-What-is-one-simple-thing-LLMs-are-insanely-bad-at.jpg
image_alt: "一幅描绘数字大脑形状的人工智能图形，在复杂的文档堆中显得非常困惑"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 可以成为出色的助理，但绝不能将其视为计算器或逻辑判断工具的替代品。只有明确意识到技术的局限性，我们才能更明智地利用这一工具。"
quiz:
  - question: "大语言模型（LLM）在数学计算上表现薄弱的根本原因是什么？"
    choices: ["计算机性能不足", "它们只是在预测似是而非的句子，而并没有进行实际计算", "训练数据不足"]
    answer: 2
    explanation: "LLM 并不是在执行数值运算，而是在预测上下文中下一个高概率出现的文本，因此无法进行准确的计算。"
  - question: "LLM 的“幻觉（Hallucination）”现象是指什么？"
    choices: ["AI 停止学习的现象", "生成听起来很可信但实际上错误的信息", "识别人类情感的功能"]
    answer: 2
    explanation: "幻觉是指 AI 虽然自信地回答问题，但实际上生成的内容并非事实的现象。"
  - question: "在使用 LLM 处理复杂工作时需要注意什么？"
    choices: ["盲目相信 AI 给出的结果", "将所有决策权交给 AI", "必须由人工验证结果"]
    answer: 3
    explanation: "由于 LLM 缺乏一致性且可能犯逻辑错误，最终的判断和验证必须由人类完成。"
lang: zh-cn
ref: 2026-08-26-Ask-HN-What-is-one-simple-thing-LLMs-are-insanely-bad-at
---

试想一下。你今天正忙于撰写一份重要报告，于是对坐在旁边的聪明 AI 助手说：“帮我把昨天会议中提到的数据汇总并告诉我结果。”AI 立即给出了流畅的回答。但如果计算结果微小地出错了呢？或者你在一分钟后再次询问同样的问题，它给出的数字却与刚才完全不同呢？

我们常说自己生活在“聪明 AI”的时代。然而，当你揭开表象时会发现，这些大语言模型（LLM，即通过学习海量文本来生成句子的 AI）并没有具备我们所认为的那种完美的“智能”。有时，它们甚至连最基础的逻辑都无法理解，从而陷入荒谬的境地。

### 为什么这个问题很重要？

世界已经变成了一个 AI 可以编写学校教育大纲、撰写企业报告，甚至代写代码的时代。[Mind Matters](https://mindmatters.ai/2025/05/llms-are-bad-at-good-things-good-at-bad-things/) 警告称，教育领域正在迅速向教师和学生都与 AI 聊天机器人沟通的环境转型。

问题在于 AI 太擅长“假装懂行”。据 [Hackernoon](https://hackernoon.com/a-simple-hardware-question-exposes-the-limits-of-todays-llms) 报道，当一名用户询问有关硬件性能的问题时，AI 用非常专业且极具说服力的逻辑给出了回答，但提供的技术信息却是完全错误的。这种工作处理方式最终会导致决策质量下降，甚至可能引发导致企业运营不稳定的“复杂性危机”。盲目信任 [Hacker News](https://news.ycombinator.com/item?id=48819891) 上 AI 的回答，就如同盲目相信未经验证的专家一样危险。

### 简单来说，AI 的本质是什么？

为什么看起来如此聪明的 AI 会在基础计算或逻辑上败下阵来？

打个比方，**AI 就像一位非常擅长拍照的“模仿派演员”。** 这位演员背下了无数剧本，以至于在面对任何情况时，都能讲出非常像样的台词。但这位演员实际上并不会解数学题，也不明白数字的位置或大小代表着什么。[DEV Community](https://dev.to/james_anderson_h/why-llms-are-bad-at-math-explained-simply-3omj)

如果更深入地了解 LLM 的工作原理，会发现它们理解的不是我们看到的 1、2、3，而是将数字拆解成无数单词碎片（token）进行学习。[Nate Silver](https://www.natesilver.net/p/chatgpt-is-shockingly-bad-at-poker) 在这个过程中，数字之间的位置或逻辑层级被混淆了。最终，AI 并不是在进行实际的“计算”，而只是在概率性地排列那些在上下文中看起来最合理的单词。[DEV Community](https://dev.to/james_anderson_h/why-llms-are-bad-at-math-explained-simply-3omj) 我们对 AI 寄予厚望的“智能”与 AI 实际执行的“基于概率的单词预测”之间，确实存在巨大的差距。

### 我们的现状：到底能信到什么程度？

目前的 AI 模型具有以下致命局限：

1. **幻觉现象（Hallucination）：** 将不实信息生成得如同真理一般，且表现得非常自信。[Educative](https://www.educative.io/blog/limitations-of-llms)
2. **缺乏一致性：** 间隔仅仅几秒再次询问同一个问题，它可能会给出完全相反的答案。[Mind Matters](https://mindmatters.ai/2026/01/large-language-models-llms-are-inherently-frail-and-unreliable/)
3. **缺乏对物理世界的理解：** 它只是简单地遵循文本模式，由于无法理解我们所处现实世界的物理法则或逻辑结构，常会犯下荒唐的错误。[Hackernoon](https://hackernoon.com/a-simple-hardware-question-exposes-the-limits-of-todays-llms)
4. **基础逻辑失效：** 在处理需要反复交互或附加复杂限制条件的问题时表现脆弱。[Strange Loop Canon](https://www.strangeloopcanon.com/p/what-can-llms-never-do)

[Builder Society](https://www.buildersociety.com/threads/current-ai-llms-are-so-terrible-basic-task-failure-beyond-writing-is-everywhere.9062/) 论坛上批评声不断：AI 虽然擅长写作等基础工作，但在消除重复、组合数据等需要逻辑思维的日常工作中表现得非常糟糕。这暗示我们应当将 AI 视为“工具”，但绝不能将其放在“决策者”的位置。

### 未来会如何改变？

专家们建议我们要摆脱 LLM 是万能解决者的幻想。[Hacker News](https://news.ycombinator.com/item?id=45321983) 未来的 AI 似乎将进化为一种不再试图独自解决所有问题，而是在必要时直接调用外部工具（如计算器、代码解释器等）来解决问题的模式。[Hacker News](https://news.ycombinator.com/item?id=41699457)

想象一下，当需要进行复杂计算时，AI 会自动开启计算器，推导出准确的数值，并基于该结果撰写句子。这种“协作式进化”将是技术未来的方向。

最终，我们不应认为“AI 是完美的预言家（回答者）”，而应将其视为“一位非常有能力但偶尔会撒谎且逻辑不足的助手”。即便技术再进步，人类仔细核对 AI 生成的结果并做出最终判断的习惯，在短时间内都不会消失。[Hacker News](https://news.ycombinator.com/item?id=48819891)

## 参考资料

1. [What can LLMs never do? - by Rohit Krishnan](https://www.strangeloopcanon.com/p/what-can-llms-never-do)
2. [AI Leaderboard 2026: Compare & Rank 300+ Top AI Models by...](https://llm-stats.com/)
3. [Why LLMs Are Bad at Math, Explained Simply - DEV Community](https://dev.to/james_anderson_h/why-llms-are-bad-at-math-explained-simply-3omj)
4. [Three Things LLMs Aren’t Great At (Yet) With Examples!](https://www.linkedin.com/pulse/three-things-llms-arent-great-yet-examples-reid-sherman-qdclc)
5. [ChatGPT is shockingly bad at poker - by Nate Silver](https://www.natesilver.net/p/chatgpt-is-shockingly-bad-at-poker)
6. [LLMs Are Bad at Good Things, Good at Bad Things | Mind Matters](https://mindmatters.ai/2025/05/llms-are-bad-at-good-things-good-at-bad-things/)
7. [LLMs are still surprisingly bad at some simple tasks | Hacker News](https://news.ycombinator.com/item?id=45321983)
8. [What are LLMs Bad At? And Why? - InfernoRed Technology Blog](https://blog.infernored.com/what-are-llms-bad-at-and-why/)
9. [A Simple Hardware Question Exposes the Limits of Today’s LLMs](https://hackernoon.com/a-simple-hardware-question-exposes-the-limits-of-todays-llms)
10. [LLMs - What aren't they good for? - manhattanmetric.com](https://www.manhattanmetric.com/blog/2026/02/what-are-llms-bad-at)
11. [What are the limitations of large language models (LLMs)?](https://www.educative.io/blog/limitations-of-llms)
12. [Limitations of LLMs: Bias, Hallucinations, and More](https://learnprompting.org/docs/basics/pitfalls)
13. [Ask HN: Are LLMs slowly making companies dysfunctional ...](https://news.ycombinator.com/item?id=48819891)
14. [Large Language Models (LLMs) Are Inherently Frail and Unreliable | Mind Matters](https://mindmatters.ai/2026/01/large-language-models-llms-are-inherently-frail-and-unreliable/)
15. [This is one of the least interesting questions to ask LLMs. I wish it wasn't so ... | Hacker News](https://news.ycombinator.com/item?id=41699457)
16. [Ask HN: Anyone struggling to get value out of coding LLMs? | Hacker News](https://news.ycombinator.com/item?id=44095189)
17. [Two things LLM coding agents are still bad at | Hacker News](https://news.ycombinator.com/item?id=45523537)
18. [2025: The Year in LLMs | Hacker News](https://news.ycombinator.com/item?id=46449643)
19. [Current AI LLMs are so terrible. Basic task failure beyond writing, is everywhere. | Builder Society](https://www.buildersociety.com/threads/current-ai-llms-are-so-terrible-basic-task-failure-beyond-writing-is-everywhere.9062/)
20. [What can LLMs never do? | Hacker News](https://news.ycombinator.com/item?id=40179232)