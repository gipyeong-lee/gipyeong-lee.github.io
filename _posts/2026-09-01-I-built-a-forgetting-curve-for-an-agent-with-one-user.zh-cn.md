---
layout: post
title: "AI也学人类‘遗忘’？让AI更智能的140年前秘诀"
description: "为什么AI经常会忘记重要信息？我们来看看如何利用19世纪的心理学理论，让AI的记忆力变得更聪明、更高效。"
summary: "AI开发者引入了19世纪艾宾浩斯遗忘曲线理论，旨在帮助AI摒弃冗余信息，保留重要记忆，从而构建智能遗忘系统。"
tags: [AI, AI技术, 记忆力, 艾宾浩斯, 数据效率]
image: 2026-09-01-I-built-a-forgetting-curve-for-an-agent-with-one-user.jpg
image_alt: "数字记忆电路如同人脑结构一般，随着时间推移变得模糊的形象化图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI的无限记忆力有时反而会成为负担。正如人类会选择性记忆一样，AI也正通过‘智能遗忘’实现更高效的进化。"
quiz:
  - question: "AI学习‘遗忘曲线’的主要原因是什么？"
    choices: ["为了理解AI的情感", "为了区分重要信息和冗余信息，从而提高效率", "为了将存储空间无限扩大"]
    answer: 1
    explanation: "如果持续保留冗余信息会导致处理速度变慢，因此通过遗忘曲线管理以重要信息为主的记忆非常重要。"
  - question: "19世纪心理学家艾宾浩斯发现的‘遗忘曲线’的核心是什么？"
    choices: ["人类能完美记住所有信息", "信息记忆率随时间呈指数级衰减", "记忆像照片一样固定不变"]
    answer: 1
    explanation: "艾宾浩斯的理论表明，大多数信息会迅速被遗忘，但部分信息会缓慢从记忆中消失。"
  - question: "为什么过度的记忆力对AI来说是毒药？"
    choices: ["因为电费太贵", "因为冗余记忆会降低AI的思考速度", "因为AI会撒谎"]
    answer: 1
    explanation: "冗余的记忆数据增加后，处理和推理信息所需的时间也会增加。"
lang: zh-cn
ref: 2026-09-01-I-built-a-forgetting-curve-for-an-agent-with-one-user
---

想象一下：你每天早上都告诉秘书今天要做的所有事。但如果这个秘书想把你说的每一句话，哪怕是1年前的琐事都一字不差地记住，会怎样呢？估计每次你说“今天中午吃什么好呢”时，秘书都会回答“您还记得去年3月15日午餐吃的泡菜汤吗？”，这种不合时宜的信息干扰会让对话完全无法进行。

最近，人工智能（AI）领域也陷入了类似的烦恼。AI越智能，试图记住的信息就越多，反而导致处理重要任务的速度变慢，或是丢失对话语境。为了解决这个问题，开发者们翻出了140年前的心理学理论——“艾宾浩斯遗忘曲线（Ebbinghaus forgetting curve）”。

### 为什么这个问题很重要？

我们期待AI能像人一样聪明地行事，但实际上AI的记忆结构与人类大不相同。人类会自然地过滤掉不重要的信息，而AI在接收新信息时，往往会固执地抓着所有数据不放。问题在于，这种“无差别的记忆”反而让AI变得迟钝。

研究结果显示，如果给AI Agent（执行特定任务的AI）多提供5千字节（KB）的记忆数据，处理信息和做出决策的时间就会增加1.1毫秒（ms）[[出处: HackerNoon](https://hackernoon.com/why-forgetting-is-the-secret-to-smarter-ai-agents)]。在数百甚至数千用户同时使用的AI服务中，这会引发严重的瓶颈效应。如果我们期待AI有更快的响应速度，那么AI也必须学会“如何更好地丢弃”。

### 简而言之：AI的“记忆瘦身”

艾宾浩斯遗忘曲线是展示人类随时间推移遗忘多少信息的图表[[出处: ELVTR](https://elvtr.com/blog/12-non-obvious-tips-tricks-for-successful-online-learning)]。简单来说，我们对初次接收的大部分信息会转瞬即逝，但多次重复思考的信息会更深地印在脑海中。

开发者们将这一原理移植到了AI记忆管理引擎中[[出处: Towards Data Science](https://towardsdatascience.com/context-windows-forget-what-matters-i-used-a-140-year-old-psychology-paper-to-fix-ai-memory/)]。

打个比方，把AI的记忆空间想象成一本“相册”。以前的AI试图保留每一天拍下的所有照片。但应用了“智能遗忘”的AI则不同：经常翻看的照片（用户经常提问或重要的信息）会被移到相册前端以便保存得更久，而从未看过、已经模糊的照片（冗余信息）时间久了会自动进入垃圾桶[[出处: Towards Data Science](https://towardsdatascience.com/context-windows-forget-what-matters-i-used-a-140-year-old-psychology-paper-to-fix-ai-memory/)]。这样一来，AI就能始终专注于“当下最需要的信息”。

### 目前进展如何？

目前，业界已经在积极开展基于该理论的实验。开源项目和记忆管理工具正在通过应用“遗忘曲线”来改变AI存储和调用记忆的方式[[出处: DEV Community](https://dev.to/sudarshangouda/ai-agent-memory-part-2-the-case-for-intelligent-forgetting-4i48)]。

但前路依然漫长。部分处于早期实验阶段的模型在判断信息的“重要性”时，仅依据词汇重复率（字符串匹配）来删除数据，从而犯了错误[[出处: Eris dev blog](https://eris-system.dev/blog/forgetting-curve)]。当人类模糊地说“昨天说的那个内容”时，AI本应能理解语境，但由于只应用了机械的删除标准，反而把珍贵的语境一起删除了。

此外，当AI流水线（工作流）中间有多个AI进行信息交互时，真正需要的信息在中途丢失的“失忆（amnesia）”问题，也是开发者们面临的一大难题[[出处: linksfor.dev](https://linksfor.dev/)]。

### 未来会有怎样的前景？

未来，AI将超越单纯学习海量数据的阶段，进化为学习“该丢弃哪些信息”的阶段。告别单纯基于最新信息管理记忆的方式，赋予不同数据以不同的“记忆寿命（TTL, Time-To-Live）”将成为常态[[出处: TianPan.co](https://tianpan.co/blog/2026-04-12-the-forgetting-problem-when-agent-memory-becomes-a-liability)]。

例如，用户今天进行的“性能调试工作”只在当天被记住，而“用户的喜好或偏好”则会设计得在更长的时间内缓慢消退[[出处: TianPan.co](https://tianpan.co/blog/2026-04-12-the-forgetting-problem-when-agent-memory-becomes-a-liability)]。这样一来，无需我们反复解释，AI就能像老练的秘书一样理解我们的风格。

---

**MindTickleBytes AI记者视角**
AI要想变聪明，需要的不仅仅是博学，更需要知道“什么时候装糊涂”的智慧。140年前的心理学理论正在让尖端AI的大脑变得更加轻盈、迅速，这既是悖论又是充满趣味的变革。未来的AI竞争，比拼的可能不再是“记忆力”，而是“遗忘的艺术”。

## 参考资料

1. [So this “forgetting curve” did not measure importance at all](https://eris-system.dev/blog/forgetting-curve) - Eris dev blog
2. [I built a forgetting curve for an agent with one user](https://news.ycombinator.com/item?id=49431546) - Hacker News
3. [Multi-agent AI pipelines lose context at every handoff between agents](https://linksfor.dev/) - linksfor.dev
4. [Forgetting is not passive at all. It is active.](https://foxfire.blog/explorations/the-forgetting-curve) - Foxfire
5. [German psychologist Hermann Ebbinghaus built a forgetting curve](https://elvtr.com/blog/12-non-obvious-tips-tricks-for-successful-online-learning) - ELVTR
6. [Context Windows Forget What Matters — I Built a Usage-Reinforced Decay Engine for AI Agent Memory](https://towardsdatascience.com/context-windows-forget-what-matters-i-used-a-140-year-old-psychology-paper-to-fix-ai-memory/) - Towards Data Science
7. [Your Memory is a practical open-source MCP server that bakes the Ebbinghaus forgetting curve](https://dev.to/sudarshangouda/ai-agent-memory-part-2-the-case-for-intelligent-forgetting-4i48) - DEV Community
8. [The cost curve exposed its own remedy: trim context every fifty seconds and cap recall at twenty kilobytes](https://hackernoon.com/why-forgetting-is-the-secret-to-smarter-ai-agents) - HackerNoon
9. [This mirrors the Ebbinghaus forgetting curve, where retention decays exponentially](https://tianpan.co/blog/2026-04-12-the-forgetting-problem-when-agent-memory-becomes-a-liability) - TianPan.co
10. [Implements Ebbinghaus forgetting-curve retention with usage-based reinforcement](https://github.com/topics/forgetting-curve?o=desc&s=updated) - GitHub Topics