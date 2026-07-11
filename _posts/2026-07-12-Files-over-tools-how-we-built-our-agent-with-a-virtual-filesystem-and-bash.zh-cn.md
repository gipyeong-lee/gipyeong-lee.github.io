---
layout: post
title: "当我给 AI 电脑而不是‘工具’时，发生了什么"
description: "介绍了一种新的 AI Agent 设计方式，让 AI 无需复杂的专用工具，即可通过文件系统和 bash 命令自主处理任务。"
summary: "不再为 AI Agent 反复构建专用工具，而是提供虚拟文件系统和 bash 命令，让其自主处理数据——“Files over tools”设计模式正受到关注。"
tags: [AI, Agent, 开发, 技术趋势]
image: 2026-07-12-Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash.jpg
image_alt: "形象化展示 AI 在虚拟文件系统环境中编写代码和浏览文件的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "与其构建复杂的工具，不如让 AI 在其熟悉的计算环境（文件和命令）中思考，这是一种更具扩展性和灵活性的方法。"
quiz:
  - question: "在近期的 AI Agent 设计中，取代工具（Tool）中心化方式的新趋势是什么？"
    choices: ["网页浏览器自动化方式", "虚拟文件系统和 bash 环境方式", "用户直接输入方式"]
    answer: 1
    explanation: "近来，人们认为与其为 AI 提供大量专用工具，不如让其使用文件系统和 bash 命令自主探索和操作数据，这种方式在效率上得到了认可。"
  - question: "使用虚拟文件系统的 Agent 有什么主要优势？"
    choices: ["可以将所有文件保存在实际硬盘上。", "无需每次开发新工具即可处理多种任务。", "需要始终保持互联网连接。"]
    answer: 1
    explanation: "拥有 bash 访问权限的 Agent 可以灵活地执行文件浏览、文本处理等多种任务，而无需开发专用工具。"
  - question: "虚拟文件系统中的数据实际上可以存储在哪里？"
    choices: ["必须仅存储在云服务器上。", "可以用 SQLite 等数据库替代实际磁盘文件进行备份。", "每次运行后都会消失。"]
    answer: 1
    explanation: "一些虚拟文件系统并不以实际文件的形式存在，而是利用 SQLite 等数据库作为备份存储，从而高效地运行。"
lang: zh-cn
ref: 2026-07-12-Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash
---

想象一下，你对厨师说：“给我做一道美味的泡菜汤。”如果这位厨师虽然会做泡菜汤，但每切一次洋葱都要现造一把“洋葱专用刀”，每用一次汤勺都要现造一台“制勺机”，你会怎样？你可能在菜还没上桌之前就已经累坏了，因为准备工具的时间比做菜本身还要长。

令人惊讶的是，这正是我们过去在构建 AI Agent（能够自主设定目标并执行复杂任务的智能体）时所使用的低效方式。我们为 AI 执行的每一项任务都专门定制并挂载了一个“专用工具（Tool）”。然而，最近开发人员中出现了一种新趋势：“别再重新造工具了，直接把计算机环境给 AI 吧”。这种设计方式被称为“文件优先（Files over tools）”。

## 为什么这种方式如此重要？

在此之前，AI Agent 每增加一个功能，开发者都必须设计复杂的软件工具并将其连接到 AI 上。这不仅耗时耗资，还是降低 AI 灵活性罪魁祸首。一旦遇到预设工具之外的情况，AI 往往就束手无策了。

但如果给 AI 提供虚拟文件系统（Virtual Filesystem）和 bash（Linux 系统中使用的命令行环境）访问权限，情况就会彻底改变。Agent 能够像人类开发者在电脑前工作一样，自主查找文件、读取内容、修改文件，并结合命令解决问题。这不仅大幅提升了 AI Agent 的生产力，还让 AI 无需开发者预设所有情况，就能自主、灵活地应对新环境。

## 简单的类比

简而言之，如果说过去的方式是给 AI 几百台“按下一个按钮就能执行特定动作的专用机器”，那么新的方式就是借给 AI 一台“安装了操作系统的电脑”。

例如，假设 Agent 需要管理客户信息。过去，必须专门开发“客户信息查询工具”和“客户信息修改工具”。但现在，只需给 Agent 一个存有客户数据的虚拟文件夹，并让其使用 bash 命令（例如：用 `grep` 查找数据，用 `echo` 修改内容）。[参考资料 2](https://www.linkedin.com/posts/knocklabs_how-do-you-build-an-ai-agent-that-safely-activity-7481434587642957843-qCEi) 这样，AI 就像使用电脑的用户一样，通过浏览文件自主掌握上下文并完成工作。[参考资料 14](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)

此外，这个文件系统无需占用物理硬盘即可运行。一些虚拟文件系统利用 SQLite（一种轻量且快速的数据库程序）来安全地存储和管理数据。[参考资料 19](https://github.com/maxi-moss/agent-filesystem) 在我们看来就像是在电脑上浏览文件夹，但实际上是在数据库中更高效地处理信息。

## 目前的技术进展如何？

许多企业和项目已经引入了这种方式。一家名为“Knock”的公司在其 AI Agent 架构中结合了 bash 环境、虚拟文件系统和管理用 API，用于处理客户消息传递资源。[参考资料 1](https://knock.app/blog/how-we-built-the-knock-agent-virtual-filesystem-and-bash) [参考资料 3](https://fooqux.com/article/6457)

此外，像“AgentFS”这样的项目专门为 AI Agent 提供了文件系统。它不仅能让 AI 安全地使用命令行工具（CLI Tool），还能帮助审计所有的操作记录。[参考资料 15](https://github.com/tursodatabase/agentfs) [参考资料 16](https://www.agentfs.ai/) 目前技术的关键不仅在于减少工具的使用，还在于通过记录 AI 的行为来确保安全性。

## 未来会是什么样子？

AI Agent 的发展方向正变得越来越“像人类”。开发者每次都要设计新工具的时代即将过去，取而代之的是 AI 利用计算机环境像熟练助手一样工作的时代。

未来，Agent 需要处理的数据将以文件形式有条理地整理好，而 Agent 则通过 Linux 命令游刃有余地进行操作。你需要做的可能不是去制造工具，而是构建一个能够让 AI 高效工作的“数字环境”。现在，是时候“借出”环境而非工具了。

## MindTickleBytes 的 AI 记者视角
从工具时代转向环境时代，意味着 AI 技术已超越简单的计算器，演变为真正的“数字员工”。这种旨在最小化开发人工介入、最大化 AI 自主性的设计，将决定未来 Agent 的生态系统。

## 参考资料

1. [Files over tools: how we built the Knock Agent using a virtual filesystem and bash](https://knock.app/blog/how-we-built-the-knock-agent-virtual-filesystem-and-bash)
2. [How do you build an AI agent that can safely manage customer messaging resources?](https://www.linkedin.com/posts/knocklabs_how-do-you-build-an-ai-agent-that-safely-activity-7481434587642957843-qCEi)
3. [Files over tools: how we built the Knock Agent using a virtual filesystem and bash](https://fooqux.com/article/6457)
4. [Files over tools: how we built our agent with a virtual filesystem and bash](https://news.ycombinator.com/item?id=48845364)
5. [How to build agents with filesystems and bash - Vercel](https://vercel.com/blog/how-to-build-agents-with-filesystems-and-bash)
6. [Knock builds AI agent with virtual filesystem and bash](https://savedelete.com/news/knock-agent-virtual-filesystem/)
7. [Building a Filesystem + Bash Based Agentic Memory System (Part 1)](https://justinbarias.io/blog/agentic-memory-filesystem-part-1/)
14. [We removed 80% of our agent’s tools - Vercel](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)
15. [GitHub - tursodatabase/agentfs: The filesystem for agents.](https://github.com/tursodatabase/agentfs)
16. [AgentFS - Filesystem Isolation for AI Agents](https://www.agentfs.ai/)
18. [Building AI agents with just bash and a filesystem in TypeScript](https://turso.tech/blog/agentfs-just-bash)
19. [GitHub - maxi-moss/agent-filesystem: A virtual filesystem for agents.](https://github.com/maxi-moss/agent-filesystem)