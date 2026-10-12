---
layout: post
title: "AI 代理编写代码的时代，为何拥有20年历史的“Git”基础设施已触及瓶颈？"
description: "AI 代理频繁的代码提交导致现有 Git 基础设施触及瓶颈。我们将为您深入浅出地解释 GitHub 等主要服务如何为了解决这一问题而重构其存储库结构。"
summary: "为了承载 AI 代理爆发式的活动量，GitHub 等服务正在针对代理规模对以人为中心的传统 Git 基础设施进行彻底重构。"
tags: [AI, Git, GitHub, 开发工具, 基础设施]
image: 2026-10-12-Building-Git-infrastructure-for-agent-scale-development.jpg
image_alt: "象征数据中心服务器与复杂连接的数字网络的图像。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "随着 AI 代理成为开发的主体，人类曾经创造的“工具”本身也正面临根本性的变革。这不仅是简单的性能提升，更是整个软件开发方式进入自动化时代的信号。"
quiz:
  - question: "传统 Git 基础设施不适合 AI 代理开发的主要原因是什么？"
    choices: ["因为安全漏洞", "因为它被设计为假设以人为中心的流程（分支、PR 等）", "因为它不兼容云服务"]
    answer: 1
    explanation: "传统的 Git 是为了以人为中心的流程而设计的，即开发人员修改代码、创建分支并提交 PR。"
  - question: "GitHub 的新 Git 存储库结构在初步测试中表现出了多大的性能提升？"
    choices: ["5倍", "15倍", "35倍"]
    answer: 2
    explanation: "GitHub 的新架构在初步内部测试中表现出了比现有架构快 35 倍的写入性能改进。"
  - question: "代码编辑器“Cursor”自主开发的“Origin”是通过什么方式优化性能的？"
    choices: ["区块链技术", "基于 WAL（预写式日志）的 S3 存储", "数据压缩技术"]
    answer: 1
    explanation: "Cursor 通过在 S3 上构建 WAL（预写式日志）系统，解决了现有 Git 托管的问题。"
lang: zh-cn
ref: 2026-10-12-Building-Git-infrastructure-for-agent-scale-development
---

想象一下：你早上起床，对 AI 说：“请帮我实现今天需要的所有网站功能。” AI 代理立刻开始工作。然而，这个代理的工作方式与人类完全不同。它几乎在每一次微小的动作中都会提交（Commit）代码并留下记录。就像我们吃饭呼吸一样自然，AI 也在不断提交代码。

然而，我们使用了 20 多年的代码管理工具“Git”却无法跟上这种 AI 的速度。这就像数千列高速列车同时行驶在人类曾经使用的狭窄自行车道上。为了解决这个问题，作为软件开发核心的 Git 基础设施正在被彻底重写。

## 为什么这很重要？

软件开发正在从“人类”主导的时代向“AI 代理”主导的时代跨越。但我们使用的 Git 是针对 20 年前人类编写和管理代码的方式进行优化的。人类一天提交几十次，与 AI 代理在几分钟内执行数千次操作并提交，这是完全不同的量级。

如果无法解决这个问题，AI 代理的工作速度就会触及物理基础设施的极限并停滞不前。如果开发基础设施不改变，未来的智能开发代理也无法发挥出应有的性能。因此，这种技术变革是决定未来软件构建速度和稳定性关键的钥匙。

## 浅显易懂：现在的 Git 为什么慢？

我们迄今为止使用的 Git 是完全为了“人类”而设计的。[参考资料 7](https://www.linkedin.com/posts/atharvapandey_origin-is-hosted-on-github-quite-funny-activity-7497924180622004224-p_BB) 包括人类编写代码、拆分分支、请求同事评审（PR）的一系列流程。

但 AI 代理不同。它们几乎在每一次操作时都要创建检查点或提交代码。[参考资料 1](https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/) 也就是说，它们试图在密集的作业循环中不断写入数据。现有的 Git 基础设施在处理这种“高频写入”时会遇到严重的瓶颈。

打个比方，就像原本只需单人通过的旋转门，突然涌入了数千名人群。由于狭窄的门一次只能通过一个人，无法处理数千名 AI 的数据，系统自然会不堪重负。

因此，企业正在寻找新的方法。例如，基于 AI 的代码编辑器“Cursor”开发了名为“Origin”的自托管系统。[参考资料 6](https://www.explainx.ai/blog/cursor-origin-git-hosting-block-buzz-projects-august-2026) 该系统在 S3（云存储）之上采用了“WAL（Write-Ahead Logging，预写式日志）”方式。

再做一个比喻，在餐厅点餐时，不是每次收到订单都跑去请求厨师做菜，而是先把订单（日志）快速记录在表格上，最后统一进行烹饪。得益于此，记录变得更加快速和稳定。

## 当前状况：准备迎接“35 倍”的奇迹

GitHub 目前正在从零开始重新设计适合这种代理时代的 Git 存储库结构。[参考资料 3](https://www.theregister.com/devops/2026/10/09/so-long-spokes-github-rewrites-storage-to-restore-reliability-just-in-time-for-agentic-hordes/5302148) 因为人类使用的现有基础设施根本无法承载日益增长的 AI 代理活动量。

令人惊讶的消息是，已经取得了明显的成果。根据 GitHub 的初步内部测试，新设计的架构显示出比以往方式快 **35 倍的写入性能**。[参考资料 3](https://www.theregister.com/devops/2026/10/09/so-long-spokes-github-rewrites-storage-to-restore-reliability-just-in-time-for-agentic-hordes/5302148) 35 倍这个数字不仅仅是稍微改善，而是突破基础设施根本限制的强烈意愿。业界分析称，GitHub 正试图通过这种基础设施重构，抢占代理中心化的开发环境。[参考资料 2](https://www.c-sharpcorner.com/article/github-is-building-git-infrastructure-for-agent-scale-development)

## 未来会怎样？

我们将迎来一个名为“代理规模软件开发（Agent-scale Software Development）”的新现实。[参考资料 9](https://qiita.com/yoshioterada/items/e796d7255e0a4efdb9f9) 未来，更多的开发工具和平台将改造其基础设施，以允许 AI 代理自由地读取和写入代码。

不仅是提高 Git 的性能，还将营造一个更多多代理系统能够轻松协作的环境。[参考资料 8](https://www.youtube.com/watch?v=lW5xEm7iSXk) 作为用户的你们，未来可能会更频繁地目睹 AI 在极短时间内实现极其复杂和庞大软件的壮观景象。开发基础设施的静默创新，正在成为让眼前的 AI 服务变得更加智能和快速的基石。

## MindTickleBytes AI 记者的视角

对于非开发人员来说，“Git”可能是一个陌生的词汇。但在 AI 改变我们日常生活的这个时代，改变 AI 的工作方式——Git，是一场极其重要的变革。在深不可测的数据中心里，为了让 AI 代理比人类快数十倍地堆叠代码，基础设施的重构已经开始。这表明技术的进步不仅停留在外观功能上，更是在从基础建设开始进行根本性的变化。

## 参考资料

1. [Building Git infrastructure for agent-scale development](https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/)
2. [GitHub Is Building Git Infrastructure for Agent-Scale Development](https://www.c-sharpcorner.com/article/github-is-building-git-infrastructure-for-agent-scale-development)
3. [So long, Spokes: GitHub rewrites storage to restore reliability, just in time for agentic hordes](https://www.theregister.com/devops/2026/10/09/so-long-spokes-github-rewrites-storage-to-restore-reliability-just-in-time-for-agentic-hordes/5302148)
4. [Startup Entire Launches Distributed Git Network for the...](https://daily.dev/posts/startup-entire-launches-distributed-git-network-for-the-agent-era-bgrcebmrv)
5. [Cursor Origin: How Its New Git Hosting Actually Works | explainx.ai](https://www.explainx.ai/blog/cursor-origin-git-hosting-block-buzz-projects-august-2026)
6. [GitHub’s Scale: Mind Boggling, Alternatives Limited | LinkedIn](https://www.linkedin.com/posts/atharvapandey_origin-is-hosted-on-github-quite-funny-activity-7497924180622004224-p_BB)
7. [n8n Just Made MultiAgent AI Way Easier: New AI Agent... - YouTube](https://www.youtube.com/watch?v=lW5xEm7iSXk)
8. [GitHubが「AIエージェント時代」を見据えて、Git... - Qiita](https://qiita.com/yoshioterada/items/e796d7255e0a4efdb9f9)
9. [AI Workflow Automation Platform - n8n](https://n8n.io/)