---
layout: post
title: "让办公室更智能！Claude 和 Codex 代理竟然能直接安装在我的服务器上？"
description: "了解如何直接在自己的服务器上部署“公司操作系统”（Company OS），并分部门利用 Claude Code 和 Codex 等 AI 代理。"
summary: "一种基于 Claude Code 和 Codex 代理的“自托管公司操作系统”（Company OS）已经出现，它允许各部门直接在公司服务器上运行 AI 任务，无需担心数据泄露。"
tags: [AI, 自托管, 公司操作系统, Claude Code, Codex]
image: 2026-09-10-Show-HN-Self-hosted-company-OS-Claude-Code-and-Codex-agents-in-departments.jpg
image_alt: "未来主义图形，展示了在服务器上运行的各部门 AI 代理"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在数据安全至关重要的企业环境中，将 AI 代理置于自有服务器内进行管理，将是解决云端 AI 部署主要阻碍的重要转折点。"
quiz:
  - question: "关于此次介绍的公司操作系统（Company OS），以下哪项描述是正确的？"
    choices: ["仅在云服务器上运行", "任何人都可以免费安装并自行托管", "没有付费订阅无法使用"]
    answer: 1
    explanation: "该系统作为开源项目提供，企业可以自行在服务器上安装和运营。"
  - question: "为了维护 AI 代理的安全，使用了哪些技术手段？"
    choices: ["强化密码", "应用沙盒内核和网络隔离技术", "保持始终在线的互联网连接"]
    answer: 1
    explanation: "每个代理都通过沙盒（bubblewrap）环境和网络隔离（pasta）技术，在确保安全的服务器内部运行。"
  - question: "将项目规则或命令传达给 AI 代理的方式是什么？"
    choices: ["仅在专用应用中输入", "在项目文件夹中创建 CLAUDE.md 或 AGENTS.md 等规则文件", "每次都在聊天窗口中输入"]
    answer: 1
    explanation: "Claude Code 通过 CLAUDE.md 文件，Codex 通过 AGENTS.md 文件，预先学习并执行项目规则和命令。"
lang: zh-cn
ref: 2026-09-10-Show-HN-Self-hosted-company-OS-Claude-Code-and-Codex-agents-in-departments
---

想象一下。早晨走进办公室，你对 AI 助手说：“请整理上个月的销售数据，并撰写各部门的报告草案。”然而，这个 AI 并没有将你的资料发送到外部云服务器，而是在公司地下机房的安全服务器中，仅利用本公司的资料进行学习并输出结果。不仅消除了信息泄露的担忧，还完美保留了公司原有的工作流程。

最近，开发者 Dimitris 在 Hacker News 社区发布了一个名为**“公司操作系统”（Company OS，旨在协助企业处理业务的 AI 集成系统）**的项目，引起了广泛关注。[参考资料 1](https://modernorange.io/item/49630606) 该环境允许在公司服务器上直接部署我们熟悉的“Claude Code（辅助开发的 AI 代理）”等强大工具，并供各部门自由使用。[参考资料 1](https://modernorange.io/item/49630606), [参考资料 10](https://news.ycombinator.com/item?id=49630606)

## 为什么这很重要？

此前，许多企业尽管想引入 AI，却因“数据安全”而犹豫不决，因为它们不希望公司的核心机密被传输到外部云服务商。然而，此次推出的公司操作系统选择了**“自托管（Self-hosting，不租用外部服务，而是直接在自有服务器上安装和运营程序）”**模式。[参考资料 1](https://modernorange.io/item/49630606), [参考资料 4](https://rankium.io/rankium/press/press-self-hosted-company-os-claude-code-and-codex-agents-in-depa-hackernews)

简单来说，就是打造一个公司数据绝不外流的“专属安全 AI 岛”。各部门可以拥有自己的 AI 代理，负责管理工作日程、使用所需工具，并积累属于部门自己的业务记忆。[参考资料 10](https://news.ycombinator.com/item?id=49630606)

## 浅显易懂：我的“公司专属 AI 工厂”

如果将该系统做一个类比，它就像是**“公司专属 AI 工厂”**。

1. **代理（AI 助手）**：是在工厂工作的聪明熟练工。Claude Code 或 Codex（辅助编程的 AI 模型）承担此角色。[参考资料 5](https://claude.com/), [参考资料 10](https://news.ycombinator.com/item?id=49630606)
2. **沙盒（Sandbox，隔离的安全区域）**：是工厂内部的安全围栏。通过名为“bubblewrap”的技术，确保 AI 熟练工在努力工作时，信息不会泄露到工厂外，同时严防外部黑客入侵。[参考资料 10](https://news.ycombinator.com/item?id=49630606)
3. **规则文件（CLAUDE.md / AGENTS.md）**：是工厂的作业手册。Claude Code 只要在项目文件夹中放入 `CLAUDE.md` 文件，AI 熟练工每天早上上班就会阅读该手册并工作。Codex 则通过 `AGENTS.md` 手册执行同样的任务。[参考资料 6](https://theivansergeev.com/guide-gpt-5-6-vs-code/)

即通过向 AI 投喂“公司遵循这些规则工作”的手册，AI 就能在公司服务器内部安全地遵守规则并处理业务。

## 能做到什么程度？

目前该系统为各部门提供了独立的作业空间。每个代理都拥有各自的业务记忆和日程安排，并能独立运行。[参考资料 10](https://news.ycombinator.com/item?id=49630606) 特别是针对安全要求严苛的企业环境，系统采用了网络隔离技术“pasta”，彻底屏蔽了与外部不必要的连接。[参考资料 10](https://news.ycombinator.com/item?id=49630606)

目前，Claude Code 作为帮助开发者理解和编辑代码的工具已广为人知，并可通过开源方式直接安装使用。[参考资料 5](https://claude.com/), [参考资料 12](https://claude.com/product/claude-code) 需要注意的是，若要将其作为公司操作系统充分利用，需要具备一定的服务器构建基础技术知识。

## 未来展望

预计未来，企业将更多地放弃复杂的云端订阅模式，转而根据自有服务器规格选择合适的模型进行直接部署。由于此次发布的项目是任何人都可以免费使用的开源项目，随着更多开发者参与贡献，它很有可能发展成为更简便、更强大的管理工具。[参考资料 1](https://modernorange.io/item/49630606) 我们离直接雇佣并管理公司专属“AI 助手团队”的时代已经不远了。

## MindTickleBytes 的 AI 记者视角

技术的发展正从“云端公用空间”回归到“企业内部私有空间”。最终，相比 AI 的智能程度，如何既能安全地守护公司宝贵数据、又能高效地与 AI 协作，将成为未来竞争力的核心。

## 参考资料

1. [Show HN: Self-hosted company OS, Claude Code and Codex agents in departments](https://modernorange.io/item/49630606)
2. [VueHN 2.0 | Show HN: Self-hosted company OS, Claude Code and...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49630606)
3. [Show HN: Self-hosted company OS, Claude Code and Codex agents in departments](https://vk.ru/wall-238001904_5064)
4. [Self-hosted company OS, Claude Code and Codex agents in departments](https://rankium.io/rankium/press/press-self-hosted-company-os-claude-code-and-codex-agents-in-depa-hackernews)
5. [Claude](https://claude.com/)
6. [Codex в VSCode: как подключить GPT-5.6 и настроить ИИ-агента](https://theivansergeev.com/guide-gpt-5-6-vs-code/)
7. [Show HN: Self-hosted company OS, Claude Code... | HackerNews](https://news.ycombinator.com/item?id=49630606)
8. [Natural 20 — AI News in Real-Time | The Bloomberg Terminal for AI](https://natural20.com/c/1bbk9g)
9. [Claude Code by Anthropic | AI Coding Agent, Terminal, IDE](https://claude.com/product/claude-code)