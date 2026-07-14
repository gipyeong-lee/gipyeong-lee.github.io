---
layout: post
title: "觉得 Claude AI 总是在用“load-bearing”这个词？这里有一个简单的解决方法"
description: "最近，许多用户对 Claude AI 频繁使用“load-bearing”（承重）这一表达感到困扰。本文将探讨这一现象背后的原因，并提供直接的技术性解决方案。"
summary: "整理了针对 Claude AI 过度使用“load-bearing”这一表达的技术性拦截方案及其背后的原因。"
tags: [AI, Claude, 技巧, 技术]
image: 2026-07-14-How-to-stop-Claude-from-saying-load-bearing.jpg
image_alt: "一名开发者正在处理代码，试图修改 AI 重复使用的词汇。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的语言习惯源于训练数据的模式。为用户提供能够直接控制环境的工具，是提升 AI 实用性的重要一步。"
quiz:
  - question: "Claude AI 通常在什么情况下使用“load-bearing”这个词？"
    choices: ["编写代码时", "在代码审查循环中", "日常对话时"]
    answer: 1
    explanation: "Claude 经常在代码审查循环（分析系统组件或约束条件的过程）中频繁使用该词。"
  - question: "阻断 Claude AI 重复使用词汇的技术手段是什么？"
    choices: ["重新输入提示词", "利用钩子 (hook) 脚本", "删除账户"]
    answer: 1
    explanation: "可以通过编写本地词汇替换脚本，并通过配置文件连接钩子 (hook) 来解决。"
  - question: "为什么用户会对“load-bearing”这个词的使用感到不满？"
    choices: ["词义理解有误", "因频繁重复而感到极其烦躁", "用户不理解这个词的意思"]
    answer: 1
    explanation: "一些用户表示，即便只运行一个小时的 Claude Code 会话，也会因反复看到该词而感到疲劳。"
lang: zh-cn
ref: 2026-07-14-How-to-stop-Claude-from-saying-load-bearing
---

想象一下：你正和一个非常聪明的 AI 助手一起进行项目。但是，它每说完一句话，甚至在句子中间，都要重复一遍：“这真的是一个‘承重 (load-bearing)’的核心要素。”起初一两次，你会觉得很专业；但到了第 10 次、20 次的时候呢？你将越来越难以专注于 AI 的核心表达。

最近，许多 Claude AI 用户，尤其是开发者，对“load-bearing”一词的过度使用进行了热烈讨论。一条关于此抱怨的社交媒体帖子甚至获得了超过 3.6 万次的浏览量 [[Fernando 🌺🌌 on X](https://x.com/zetalyrae/status/2063109680017334311)]。今天，我们将探讨为什么 Claude 会对这个词产生执念，以及如何阻止它。

## 为什么这很重要？

AI 是我们提高工作效率的强大助手，但 AI 使用的特定语调或重复性词汇会严重降低用户体验。特别是在需要精密工作的代码审查中，多余的修饰语会阻碍我们对系统上下文的理解 [[Why Your Claude-Assisted Code Becomes a Mess](https://dev.to/panav_mhatre_732271d2d44b/why-your-claude-assisted-code-becomes-a-mess-its-not-your-prompts-imj)]。用户试图解决这个问题，不仅仅是因为讨厌某个词，而是为了保持与 AI 协作环境的简洁和高效。

打个比方，这就好比歌手唱歌时总是不断强调同一个词。你想感受歌曲的情感，却因为总是听到同一个词而导致整体节奏被打乱。用户希望与 AI 进行更自然、更流畅的对话。

## 简单易懂：什么是“承重 (load-bearing)”？

我们需要理解“load-bearing”的本意。在建筑学中，这个词指的是支撑建筑物重量的墙壁或柱子。如果移除这些部分，建筑物就会倒塌，所以它们是核心要素 [[Marek Šuppa](https://mareksuppa.com/til/load-bearing/)]。

Claude 在代码审查循环（反复检查代码结构和逻辑的过程）中经常使用这个词。从 AI 的角度来看，当它想强调“这段代码是系统的核心，绝对不能删除”时，它会将这个词用作一种“过滤器” [[Marek Šuppa](https://mareksuppa.com/til/load-bearing/)]。然而，Claude 过度忠实于它所学的模式，甚至将这个词应用在重要性较低的部分，从而让用户感到困惑 [[AI: When the Metaphors are Load-Bearing](https://medium.com/@Bismar/ai-when-the-metaphors-are-load-bearing-830d37971e25)]。

## 现状：停不下来的 AI

这个问题比想象中严重。即使你直接在内存（AI 的对话记录）中指示“不要使用这个词”，Claude 往往也会无视指令继续使用，用户甚至在 GitHub 上提起了相关的问题 [[Claude Code can not stop using the word "load-bearing"](https://github.com/anthropics/claude-code/issues/53454)]。一些用户感到非常沮丧，认为 AI 似乎是在没有用户指导的情况下自己学会了这个习惯 [[Claude Code can not stop using the word "load-bearing"](https://www.linkedin.com/posts/scott-cunningham-7788912_model-claude-code-can-not-stop-using-the-activity-7480745075279376384-myox)]。这看起来不仅仅是一个暂时现象，而是深植于 AI 学习模型中的一种习惯。

## 解决方法：技术性拦截

如果 AI 无法自行修正，我们就必须使用外部强制过滤的方法。幸运的是，有技术解决方案。

可以使用 Claude 在启动时自动运行的“钩子 (hook)”功能。这是一种在 AI 输出回答之前，在本地环境中截获并修改内容的方法。简单总结如下：

1. 在本地电脑的 `~/.claude/hooks/` 文件夹中创建一个自动替换词汇的 shell 脚本（例如 `wordswap.sh`）。在这个脚本中，编写查找“load-bearing”并将其替换为其他词汇的命令。
2. 将该文件设置为可执行（`chmod +x`）。
3. 在配置文件 `~/.claude/settings.json` 中连接该脚本。

这样，在 Claude 输出回答之前，脚本会在中间过程中干预，从而拦截“load-bearing”一词或将其替换为其他词汇 [[How to stop Claude from saying load-bearing](https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing)]。

## 未来会怎样？

未来，AI 模型预计会通过反映用户的反馈来逐步改善这种重复性的语调。不过，AI 偏好特定词汇是语言模型学习数据结构中不可避免的一面。在短期内，用户可能需要通过上述工具性的解决方案，根据自己的偏好优化 AI 环境 [[How to Fix Claude Code’s Most Annoying Behavior](https://www.geeky-gadgets.com/fix-claude-code-annoying-behavior/)]。如果你的 Claude 对话也被特定词汇所困，为什么不试试今天的解决方法呢？

技术存在的意义就是让我们更好地驾驭 AI。解决小烦恼的过程，本身就能让与 AI 的协作变得更加有趣。

## MindTickleBytes 的 AI 记者视点

AI 使用的语言最终是大数据海洋中提取的统计产物。对“load-bearing”一词的执着，是一个有趣的案例，展示了 AI 理解语境的方式与人类不满之间的鸿沟。超越技术性的拦截，我们期待 AI 模型本身能更灵活地学习用户喜好的时代早日到来。机器学会更像人类一样与我们交流的那一天，已经不远了。

## 参考资料

1. [How to stop Claude from saying load-bearing | jola.dev](https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing)
2. [[MODEL] Claude Code can not stop using the word "load-bearing" · Issue #53454 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/53454)
3. [Dial-Back Discipline - Claude Blattman · AI for Professionals Who Don't Code](https://claudeblattman.com/build-your-own/dial-back-discipline/)
4. [Why Your Claude-Assisted Code Becomes a Mess (It's Not Your Prompts) - DEV Community](https://dev.to/panav_mhatre_732271d2d44b/why-your-claude-assisted-code-becomes-a-mess-its-not-your-prompts-imj)
5. [The Complete Guide to CLAUDE.md: Memory, Rules, Loading, and Cross-Tool Compression | by Bijit Ghosh | Medium](https://medium.com/@bijit211987/the-complete-guide-to-claude-md-memory-rules-loading-and-cross-tool-compression-97cc12ed037b)
6. [Fernando 🌺🌌 on X: "I asked Claude to stop saying "load-bearing" 😭](https://x.com/zetalyrae/status/2063109680017334311)
7. ["Load-bearing" is becoming LLM speak · Marek Šuppa](https://mareksuppa.com/til/load-bearing/)
8. [[MODEL] Claude Code can not stop using the word "load-bearing ...](https://www.linkedin.com/posts/scott-cunningham-7788912_model-claude-code-can-not-stop-using-the-activity-7480745075279376384-myox)
9. [AI: When the Metaphors are Load-Bearing - Medium](https://medium.com/@Bismar/ai-when-the-metaphors-are-load-bearing-830d37971e25)
10. [How to Fix Claude Code’s Most Annoying Behavior - Geeky Gadgets](https://www.geeky-gadgets.com/fix-claude-code-annoying-behavior/)
11. [how to stop claude from being a YES-MAN Ole built a skill ...](https://x.com/shannholmberg/status/2038941912447791499)