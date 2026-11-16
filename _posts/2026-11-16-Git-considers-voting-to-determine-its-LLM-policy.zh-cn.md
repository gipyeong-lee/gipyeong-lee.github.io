---
layout: post
title: "开发者的必备工具 Git，将通过“投票”决定 AI 使用政策？"
description: "探讨开源版本控制系统 Git 为确定大语言模型 (LLM) 使用政策而考虑投票背景，以及开源生态系统的民主决策过程。"
summary: "随着 Git 考虑通过投票程序决定 AI (LLM) 使用政策，开源社区正在探索应对技术变革的全新民主治理模式。"
tags: [Git, LLM, OpenSource, AI Policy, Governance]
image: 2026-11-16-Git-considers-voting-to-determine-its-LLM-policy.jpg
image_alt: "插图描绘了开发者们看着显示器，讨论投票和代码编写的情景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "技术变革越快，制定规则的方式也应越民主、越透明。Git 的这次尝试将成为开源社区驶向 AI 时代的重要里程碑。"
quiz:
  - question: "Git 目前正在考虑的 LLM 政策决定方式是什么？"
    choices: ["高层管理人员独自决定", "投票（Voting）程序", "自动化 AI 算法判定"]
    answer: 1
    explanation: "Git 正在考虑采用投票方式来决定与大语言模型 (LLM) 相关的政策。"
  - question: "在部分开源仓库（如 yt-dlp）中，开发者需要遵守的代表性政策规定是什么？"
    choices: ["NO AI / NO LLM POLICY", "所有代码由 AI 自动生成", "全面禁止商业用途"]
    answer: 0
    explanation: "部分开源项目要求贡献者在提交代码或问题时查看并遵守“NO AI / NO LLM POLICY”。"
  - question: "为什么在开源生态系统中建立政策和价值如此重要？"
    choices: ["为了提高软件构建速度", "为了在社会与技术变革中寻找正确的方向", "为了降低服务器成本"]
    answer: 1
    explanation: "随着社会和技术环境的变迁，我们需要系统性地探索和明确适当的政策与价值观。"
lang: zh-cn
ref: 2026-11-16-Git-considers-voting-to-determine-its-LLM-policy
---

试想一下。在全世界数千万开发者每天都在使用的核心工具中，我们需要制定关于如何在编写代码时使用人工智能（AI）的规则。如果这个重要的决定不是由少数管理者在密室中做出，而是通过整个社区的“投票”来决定，那会怎样？最近，全球开发者社群中出现了一个引人注目的有趣动向。作为版本控制系统标准的 Git，为了制定与大语言模型（LLM，Large Language Model，通过学习海量文本能够像人一样撰写文章和编写代码的 AI 技术）相关的政策，开始考虑采用投票方式 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)]。

---

## 为什么这很重要？

在软件开发的世界里，“Git”就像是一个管理建筑物蓝图的公认档案库。任何人都可以通过这个档案库修改代码、添加新功能，并与世界各地的人进行协作。对于学习计算机科学或编程的人来说，这是必须掌握的基础知识 [[Source 2](https://www.youtube.com/watch?v=Yi5Y2_r0t9Y)]。如果打个比方，它就像是“国民图书馆”，当世界各地的无数厨师共同修改一本巨大的食谱时，它能够以零误差记录并管理每次修改的历程。

然而，最近几年随着生成式 AI 的爆发式增长，全球开发一线陷入了巨大的混乱中。因为此前并没有明确的标准来界定：是否可以直接使用 AI 编写的代码、AI 生成的代码是否存在版权问题，或者在参与项目贡献时允许使用 AI 的界限在哪里。实际上，在某些开源项目中（例如以视频下载工具闻名的 yt-dlp 等），贡献者在提交代码或问题时，被要求勾选确认：“我已阅读 AI 使用政策（NO AI / NO LLM POLICY），并理解如果违反此规定，可能会被仓库封禁” [[Source 3](https://github.com/yt-dlp/yt-dlp/issues/17585)]。 

在这种情况下，像 Git 这样核心的基础设施项目为了制定 AI 政策而搬出了“投票”这一民主程序，这意味着它可能成为未来无数开源项目制定 AI 时代规则的标准先例 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)]。

---

## 轻松理解：制定规则的民主实验

我们可以打个比方。想象一下，在一个住宅小区里，居民们聚在一起制定宠物饲养指南。有些人完全欢迎宠物，而另一些人则希望进行严格限制。如果此时物业管理处长独断专行地制定规则，势必会引发居民的反感。相反，如果通过全体住户参与的投票来制定规则，那么无论结果如何，大家更容易接受。

Git 想要做的事情也与之类似。当技术发展速度过快且各方立场分歧时，社会成员需要思考如何就 AI 带来的政治、伦理影响以及偏见问题达成共识 [[Source 5](https://arxiv.org/pdf/2410.24190)]。开源生态系统原本就是通过自愿参与和讨论发展起来的，但在 AI 这股巨浪面前，它正式将透明地征求并决定社区意愿的制度性装置（投票程序）摆上了台面 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)]。

从更广阔的视角来看，这与民主社会面对新技术寻找适当政策与价值的过程如出一辙。正如社会成员需要根据各种指标分析潜在结果并探索更好方向一样，开发社群也正在技术变革中试验系统的决策结构 [[Source 15](https://iclr-blogposts.github.io/2025/blog/llm-democracy/)]。

---

## 当前状况：我们走到哪一步了？

目前，软件开发生态系统正经历着剧烈的变革期。在大型代码托管平台的政策变化以及寻求中心化服务替代方案的呼声日益高涨的背景下 [[Source 10](https://dbushell.com/2026/04/29/github-is-sinking/)]，作为开发工具基石的 Git 社区内部也存在着对接受 AI 与否的赞成与反对两派观点。 

一方面有人主张利用 AI 最大化生产力，而另一方面则以代码质量、许可证污染、安全风险等为由要求进行严格控制或限制。正是在这种情况下，通过明确的投票程序来制定官方政策、而不是用强权压制或模糊放任这种冲突的讨论，在此时此刻进入了实质化阶段 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)]。

---

## 未来会怎样？

Git 最终将采用什么样的投票方式以及敲定怎样的 LLM 政策，正吸引着全球开源社区的目光。如果通过投票决定的政策能够成功落地，许多其他开源项目极有可能会效仿并引入类似的治理模式。 

开发者们今后将能够在公开透明的规则中明确知晓，自己参与贡献的项目将以何种标准审核并接收 AI 编写的代码。可以说，Git 正在向我们展示这样一个教训：随着技术的发展，制定规则的方式也必须随之进化 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)]。

---

## 参考资料

1. [Git considers voting to determine its LLM policy](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/)
2. [We Need To Stop Lying About Git - YouTube](https://www.youtube.com/watch?v=Yi5Y2_r0t9Y)
3. [ok.ru not downloading any video · Issue #17585 · yt-dlp/yt-dlp · GitHub](https://github.com/yt-dlp/yt-dlp/issues/17585)
4. [Hidden Persuaders: LLMs’ Political Leaning and Their Influence on...](https://arxiv.org/pdf/2410.24190)
5. [Welcome to LWN.net [LWN.net]](https://lwn.net/)
6. [GitHub is sinking – David Bushell – Web Dev (UK)](https://dbushell.com/2026/04/29/github-is-sinking/)
7. [LLMs' Potential Influences on Our Democracy: Challenges and...](https://iclr-blogposts.github.io/2025/blog/llm-democracy/)