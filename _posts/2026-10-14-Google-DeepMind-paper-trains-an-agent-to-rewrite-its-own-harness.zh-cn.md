---
layout: post
title: "AI自行修改其‘智能外壳’？自主进化AI代理时代来临"
description: "深度解析最新AI技术研究，AI代理在无需人工干预的情况下，自动改进并进化其运作方式（即“外壳/harness”）的技术进展。"
summary: "谷歌DeepMind的最新研究表明，AI代理无需繁琐的手动工程，即可自行修改并优化其运作环境（外壳），为自主软件开发铺平了道路。"
tags: [AI, GoogleDeepMind, 代理, AutoHarness, Evo2]
image: 2026-10-14-Google-DeepMind-paper-trains-an-agent-to-rewrite-its-own-harness.jpg
image_alt: "一幅展现AI代理自主编写代码并修改其运作体系的未来主义插画"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人类逐条制定规则的时代正在终结。AI识别并修复自身局限性的能力，将成为迈向真正自主代理的最重要钥匙。"
quiz:
  - question: "AI代理的‘外壳（harness）’是什么？"
    choices: ["AI的存储装置", "连接模型与任务的‘胶水’作用软件体系", "AI的训练数据集"]
    answer: 1
    explanation: "外壳是位于AI模型与待解决任务之间的管道或胶水，作为软件支撑架（scaffolding），帮助AI顺利运作。"
  - question: "谷歌DeepMind的AutoHarness研究是如何运作的？"
    choices: ["人类每天输入新代码。", "Gemini利用环境反馈通过反复精炼过程自主生成代码。", "保持原有规则不变。"]
    answer: 1
    explanation: "AutoHarness通过Gemini-2.5-Flash从环境中获取反馈，经由反复改进过程，自主构建最佳代码外壳。"
  - question: "Evo2框架的核心目标是什么？"
    choices: ["最大化人工干预。", "完全替换AI基础语言模型。", "在不改变任务执行者（task executor）的前提下改进代理的工作流与策略。"]
    answer: 2
    explanation: "Evo2是一个框架，它在不触动任务执行者本身的情况下，利用代理修改外壳的记录与评估数据作为训练材料，从而优化工作流与策略。"
lang: zh-cn
ref: 2026-10-14-Google-DeepMind-paper-trains-an-agent-to-rewrite-its-own-harness
---

想象一下，你雇佣了一位新助手。每次交代任务时，他都会说：“我觉得这样做效率更高”，并不断升级自己的工作方式（手册）。甚至在你没有指示的情况下，他还会自行重组自己的工具和记忆系统。这不是科幻电影中的情节，而是谷歌DeepMind（Google DeepMind）最新研究展示出的“自主进化AI代理”的真实面貌。

### 为什么这项技术至关重要？

长期以来，构建AI代理的过程是一连串极其痛苦且昂贵的“手工劳动”。因为AI代理要完成某项任务，必须由人类工程师逐一定义该任务的具体规则和限制。这种构建连接环节的过程在业内被称为“外壳（harness）”，实际上，这一过程一直是引入AI代理的最大障碍。 [来源: This AutoHarness paper(from Google DeepMind) is the most...](https://www.linkedin.com/posts/omarsar_this-autoharness-paper-from-google-deepmind-activity-7437877601853153280-uWyl)

但现在情况不同了。如果AI能够自行修改和优化其运作体系，那么无需人类介入，AI代理自主执行多样且复杂任务的世界将飞速到来。这将成为AI技术从实验室级别跨越到生产一线并实现“规模化（scalable）”部署的重要分水岭。

### 轻松理解：AI的“胶水”——外壳

让我们把技术术语说得再简单点。AI代理通常由作为“大脑”的巨大语言模型（LLM）和帮助这个大脑与外部世界沟通的“外壳”框架组成。 [来源: AutoHarness: improving LLM agents by automatically ...](https://arxiv.org/pdf/2603.03329)

可以这样比喻：我们将AI代理看作一位“天才画家”。画家要作画，必须要有画笔（工具）、画布（环境），并且作画指示（提示词）必须清晰。在这里，画家的工具箱和辅助作画的工作台整体就是“外壳”。过去，人类需要逐一准备画笔并调节工作台高度，而现在，画家（AI）会自言自语说：“这次作画需要这种画笔”，并主动调整工具箱的结构。

谷歌DeepMind的 **AutoHarness** 旨在通过Gemini-2.5-Flash模型利用从环境获得的反馈，辅助其自主设计更好的“工作台”。 [来源: AutoHarness: improving LLM agents by automatically ...](https://arxiv.org/pdf/2603.03329), [来源: AutoHarness | DAIR.AI Academy](https://academy.dair.ai/papers/autoharness) 

此外，名为 **Evo2** 的框架将代理在修复外壳过程中获得的数据转化为训练数据。也就是说，通过将修改和实验的经验积累为数据，从而自主强化其工作流（业务流程）。 [来源: Google DeepMind paper trains an agent to rewrite its own harness](https://runtimewire.com/article/google-deepmind-evo2-agent-harness-co-evolution)

### 进展到了什么程度？

目前，AI研究领域正在探讨多种自主改进结构的有趣方式。

首先，**AutoHarness** 允许代理通过编写代码自主创建外壳。相比人类手动构建复杂规则，经过少量反复精炼过程的自动化外壳往往表现出更高的效率。 [来源: [2603.03329] AutoHarness](https://arxiv.org/abs/2603.03329)

其次，**Self-Harness** 是一种新范式，即代理在没有外部强力支持或人类帮助的情况下，独立改进其运作环境。 [来源: [2606.09498] Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498)

第三，**RRSI（递归自我改进）** 技术由谷歌云AI研究团队等发布，它让AI能够自行重写提示词、工具、记忆系统、控制流，甚至下级代理（sub-agents）。 [来源: Paper AutoHarness from DeepMind Changes AI Agents 1](https://www.youtube.com/watch?v=4Xczb2z3N_w)

现场专家一致认为：“性能差距往往不在于模型本身，而在于使用什么样的外壳。”因为无论模型多么聪明，如果使用工具的方式不当，都无法发挥出应有的能力。 [来源: Auto-Harness Synthesis - Just Understanding Data](https://understandingdata.com/posts/auto-harness-synthesis/)

### 未来展望

未来，AI代理将不再是静态的存在。今天遇到的AI与1000天后的AI，其结构、记忆和工具可能完全不同。 [来源: The Harness That Learns You | XO Docs](https://docs.xo.builders/research/perspectives/the-harness-that-learns-you) 

我们现在已经超越了考虑“给AI分配什么任务”的阶段，进入了观察“AI自行选择何种工具和方式解决问题”的阶段。让我们共同期待，人类介入降至最低、真正意义上的自主代理将如何改变我们的日常生活。

## 参考资料

1. [Google DeepMind - Wikipedia](https://en.wikipedia.org/wiki/Google_DeepMind)
2. [This AutoHarness paper(from Google DeepMind) is the most...](https://www.linkedin.com/posts/omarsar_this-autoharness-paper-from-google-deepmind-activity-7437877601853153280-uWyl)
3. [Google DeepMind](https://deepmind.google/)
4. [AI has grown beyond human knowledge, says Google's DeepMind unit](https://www.zdnet.com/article/ai-has-grown-beyond-human-knowledge-says-googles-deepmind-unit/)
5. [The Harness That Learns You | XO Docs](https://docs.xo.builders/research/perspectives/the-harness-that-learns-you)
6. [Google DeepMind paper trains an agent to rewrite its own harness](https://runtimewire.com/article/google-deepmind-evo2-agent-harness-co-evolution)
7. [AutoHarness: improving LLM agents by automatically ...](https://arxiv.org/pdf/2603.03329)
8. [[2603.03329] AutoHarness: improving LLM agents by ...](https://arxiv.org/abs/2603.03329)
9. [AutoHarness: LLM Agents That Build Own Scaffolding | aiHola](https://aihola.com/article/autoharness-llm-agent-code-harness)
10. [Auto-Harness Synthesis - Just Understanding Data](https://understandingdata.com/posts/auto-harness-synthesis/)
11. [AutoHarness | DAIR.AI Academy](https://academy.dair.ai/papers/autoharness)
12. [[2606.09498] Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498)
13. [Paper AutoHarness from DeepMind Changes AI Agents 1](https://www.youtube.com/watch?v=4Xczb2z3N_w)