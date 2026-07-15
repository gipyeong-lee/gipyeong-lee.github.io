---
layout: post
title: "AI竟然未经我允许就修改了代码？Grepathy，这款能记录AI‘为何如此操作’的智能工具"
description: "深入了解Grepathy，这是一款能够透明追踪AI代理代码修改决策原因的工具。"
summary: "介绍Grepathy，它通过记录并保存AI的决策理由，防止作业历史记录随时间消失。"
tags: [AI, Claude, Grepathy, 开发工具, 透明度]
image: 2026-07-16-Show-HN-Grepathy-Claude-made-a-decision-nobody-approved.jpg
image_alt: "形象化展示Grepathy如何将AI决策记录并保存到代码仓库中的运行原理。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "随着AI自主性的增强，追踪其决策依据的透明度不再是可选项，而是必需品。Grepathy以实用的方式确保了开发者与AI共存所需的‘可解释性’。"
quiz:
  - question: "Grepathy研发的最主要原因是什么？"
    choices: ["为了提高AI的速度", "为了记录AI的决策理由并防止历史记录被删除", "为了自动修正AI的错误"]
    answer: 1
    explanation: "Grepathy旨在解决AI代理决策理由随时间被删除，导致历史记录丢失的问题，通过将这些记录保留在本地仓库中来解决该痛点。"
  - question: "Grepathy存储的是什么数据？"
    choices: ["与用户的完整对话内容", "仅选择性存储AI的决策（reasoning）信息", "电脑上所有文件的列表"]
    answer: 1
    explanation: "Grepathy不会存储完整的对话内容，而是筛选出AI的决策（decisions）信息，并以Markdown格式进行保存。"
  - question: "Grepathy通过什么方式运行？"
    choices: ["需要用户每次手动执行", "始终在后台运行", "通过Git钩子（hook）自动执行"]
    answer: 2
    explanation: "Grepathy无需用户每次手动操作，它是通过Git钩子（hooks）在工作流程中自动执行的。"
lang: zh-cn
ref: 2026-07-16-Show-HN-Grepathy-Claude-made-a-decision-nobody-approved
---

想象一下：在一个忙碌的早晨，你委托你的智能AI编程助手“把这个项目的代码整理得简洁一些”，然后便去开会了。晚上回来检查代码时，天哪！AI竟然修改了你认为绝对不能触碰的核心逻辑。“它到底为什么要这么做？”你想寻找原因，却发现AI工具早已把几天前的作业记录全部删除了。[Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537)

这种情况已不再是遥远的未来。近期在开发者群体中，“代理时代”已经开启，AI能够自主修改代码并做出决策，但由于其背后的“原因”随历史记录一起消失，开发者们常因此陷入困境。今天介绍的 **Grepathy** 就是为了“捕捉”这些“正在消失的决策原因”而诞生的。

### 为什么这很重要？

随着AI超越了仅仅提供回答的阶段，开始扮演“代理（Agent，指能自主完成特定目标的AI）”的角色，即亲自编写代码并修改文件，**“责任归属”和“可追溯性”**变得至关重要。[Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537)

许多AI工具，尤其是像Claude Code（一种允许AI在开发环境中直接修改和运行代码的工具）这类服务，默认会在一段时间（30天）后删除作业记录（transcript）。[Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537) 虽然这在个人信息保护或存储空间方面很有效，但对于后来必须回答“AI为什么要这样修改代码？”的开发者来说，可能是致命的。Grepathy通过记录AI自主决策的依据，帮助任何人日后都能确认其中的原因。

### 通俗理解：如何留下AI的“工作日志”

可以这样类比：你的项目团队中有一名非常聪明但记性很短的新员工（AI）。这名员工工作非常出色，但30天后他就会忘记自己当初为何做出那样的决定。Grepathy就像是专门负责记录这位新员工**“决策日志”的秘书**。

1. **智能筛选记录**：Grepathy不会存储用户与AI之间的所有私人对话内容，它只筛选出“AI为何做出该决定”的理由（reasoning）。[Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537)
2. **直接存入代码仓库**：记录下来的决策会转换为Markdown文档格式，并与你的代码一起永久保存在仓库（repository）中。[Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537)
3. **自动化**：用户无需繁琐地输入命令。通过Git钩子（hook，指特定事件发生时自动执行的脚本），每次提交或推送代码时，Grepathy都会自动运行。[GitHub - evansjp/grepathy](https://github.com/evansjp/grepathy)

简而言之，只需在项目文件夹中执行特定命令，就能一目了然地看到AI留下的“决策说明”。[GitHub - evansjp/grepathy](https://github.com/evansjp/grepathy)

### 现状：与AI协作的意义

AI编程工具日新月异。像Claude Code这类工具虽然默认采用“人机交互循环（human-on-the-loop，即人类监督AI的工作方式）”，但随着自动模式（Auto mode）的引入，AI已能实现无需人类直接干预即可处理更多事务。[Claude Code Defaults to Human Approval: Auto Mode Requires Explicit Opt-In](https://www.techtimes.com/articles/319874/20260707/claude-code-defaults-human-approval-auto-mode-requires-explicit-opt.htm)

然而，技术越先进，信任和管理AI判断的透明度问题就越突出。开发者之间已经开始分享AI制造虚假信息或扭曲事实的案例，[How to Stop Claude From Making $#it Up](https://medium.com/@brentwpeterson/how-to-stop-claude-from-making-it-up-921a6a9238c8) 企业层面也在警惕AI代理的决策可能带来的不可预见后果。[The Day an AI Agent Commits Your Company to a Decision Nobody ...](https://www.linkedin.com/posts/bhaviavelayudhan_the-day-an-ai-agent-commits-your-company-activity-7436671325772898305-TdKd)

### 未来会怎样？

像Grepathy这样的尝试在未来将变得愈发重要。随着AI不仅限于编写代码，而是成长为决定项目方向的决策主体，记录其决策依据将成为法律和伦理上必不可少的程序。

明天早上，当你的AI代理修改代码时，何不尝试通过Grepathy查看一下其决定的“原因”呢？这或许就是AI与人类实现透明沟通的第一步。

## 参考资料
1. [Show HN: Grepathy – Claude made a decision nobody approved | Hacker News](https://news.ycombinator.com/item?id=48920537)
2. [GitHub - evansjp/grepathy: Your agent writes down why, in the repo, so everyone else's agents can find it without asking you. · GitHub](https://github.com/evansjp/grepathy)
3. [Claude Code Defaults to Human Approval: Auto Mode Requires Explicit Opt-In](https://www.techtimes.com/articles/319874/20260707/claude-code-defaults-human-approval-auto-mode-requires-explicit-opt.htm)
4. [How to Stop Claude From Making $#it Up | by Brent W. Peterson | May, 2026 | Medium](https://medium.com/@brentwpeterson/how-to-stop-claude-from-making-it-up-921a6a9238c8)
5. [The Day an AI Agent Commits Your Company to a Decision Nobody ...](https://www.linkedin.com/posts/bhaviavelayudhan_the-day-an-ai-agent-commits-your-company-activity-7436671325772898305-TdKd)