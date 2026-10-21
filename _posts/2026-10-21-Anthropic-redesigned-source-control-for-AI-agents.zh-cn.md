---
layout: post
title: "与 AI 协同工作的新方式？Anthropic 彻底颠覆了源代码控制系统"
description: "Anthropic 发布了全新源代码控制方法 'Scion' 及改进版 Claude Code 桌面应用程序，旨在实现与多个 AI 代理的同时协作。"
summary: "Anthropic 超越了传统 Git 的局限，推出了新一代源代码控制系统和界面，专为多个 AI 代理并行编码和测试而设计。"
tags: [AI, 开发, Anthropic, Claude, 编码代理]
image: 2026-10-21-Anthropic-redesigned-source-control-for-AI-agents.jpg
image_alt: "展示多个 AI 代理同时分析代码并并行执行任务的现代化开发环境界面图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "如果说过去的开发工具是为人类主导的顺序工作流程而设计的，那么现在这些工具已经准备好接纳 '代理'（Agent）作为新同事了。这一重要的转变表明，开发者的角色正从编写代码转向 AI 代理的指挥者（Orchestrator）。"
quiz:
  - question: "Anthropic 发布的新一代源代码控制系统名称是什么？"
    choices: ["Git Plus", "Scion", "Claude Control"]
    answer: 1
    explanation: "Anthropic 为了突破现有 Git 的局限，开发了一种名为 'Scion' 的新方法。"
  - question: "新的 Claude Code 桌面应用程序引入了哪些功能以减少开发者的上下文切换？"
    choices: ["会话侧边栏", "拖放布局", "云端自动删除"]
    answer: 1
    explanation: "Claude Code 通过会话侧边栏、拖放布局和内置终端等功能进行了改进，以便同时管理多个代理。"
  - question: "在代理驱动的编码（agentic coding）环境中，开发者的主要角色是什么？"
    choices: ["一行行编写代码", "管理多个代理会话的指挥者", "构建硬件服务器"]
    answer: 1
    explanation: "随着许多代理并行执行任务，开发者将扮演指挥者（Orchestrator）的角色来领导和管理它们。"
lang: zh-cn
ref: 2026-10-21-Anthropic-redesigned-source-control-for-AI-agents
---

想象一下，早晨醒来打开电脑，已经有三位 AI 开发者在协助你的软件项目了。一位在实现新功能，一位在修复漏洞，最后一位在实时测试新代码是否正常运行。

过去，开发者必须亲自按顺序完成所有这些步骤，或者为了合并不同部分的作业而忙得焦头烂额。但现在，开发方式正在发生彻底变革。Anthropic 推出了一套专为“代理时代”设计的全新源代码控制系统和工具。

## 为什么这很重要？

软件开发的发展一直建立在“人类主导的顺序作业”这一假设之上。但随着 AI 代理（能自主执行特定目标的 AI 程序）参与编码，情况发生了变化。根据 Anthropic 的研究，随着代理驱动编码（agentic coding）的普及，传统软件开发流程的基本前提正在迅速进化[Source 1](https://www.anthropic.com/research/redesigning-source-control)。

这种变化不仅仅是提高编码速度的问题。当多个 AI 代理同时执行不同任务时，现有的源代码控制系统（管理开发者代码修改历史的系统）遇到了瓶颈。Anthropic 提出的新环境引导开发者扮演实时指挥多个代理工作的“指挥者（Orchestrator）”，并大幅减少了在此过程中频繁发生的上下文切换（Context-switching，即在不同任务间切换时导致的专注力下降）[Source 2](https://www.eigent.ai/blog/claude-code-desktop-redesign)[Source 5](https://completeaitraining.com/news/anthropic-redesigns-claude-code-desktop-app-to-better/)。

## 简单理解：从 Git 到 Scion

传统的源代码控制系统 Git，实际上是为单个人修改和保存文件而优化的。就像多个人轮流写同一本书。但是，如果多个 AI 代理同时修改不同的部分，会发生什么呢？

Anthropic 开发了一套名为“Scion”的新系统[Source 1](https://www.anthropic.com/research/redesigning-source-control)。

打个比方，如果说 Git 是为一名作家准备的“原稿纸”，那么 Scion 就是一个“现代协作平台”——几十位作家在各自的房间里同时写作，指挥者穿梭于各个房间，实时组合内容。该系统是根据代理的数量规模，对现有的源代码控制原则进行的全新设计[Source 1](https://www.anthropic.com/research/redesigning-source-control)。

## 当前状况：Claude Code 的进化

Anthropic 将这一理念融入其中，彻底重构了其编码代理工具“Claude Code”桌面应用[Source 2](https://www.eigent.ai/blog/claude-code-desktop-redesign)。

现在的 Claude Code 不再只是一个简单的命令行工具，它搭载了以下功能，改变了开发者的工作空间[Source 5](https://completeaitraining.com/news/anthropic-redesigns-claude-code-desktop-app-to-better/)：

*   **会话侧边栏（Session Sidebar）：** 可以一目了然地看到多个运行中 AI 代理的状态。
*   **拖放布局（Drag-and-Drop Layout）：** 可以自由放置作业窗口，管理代理的工作流。
*   **内置终端（Built-in Terminal）：** 无需在不同窗口间切换，即可在一个地方处理代码修改、测试执行和提交变更（Commit）[Source 5](https://completeaitraining.com/news/anthropic-redesigns-claude-code-desktop-app-to-better/)[Source 7](https://www.linkedin.com/posts/abhijeet-pachpute_anthropic-redesigned-claude-code-for-desktop-activity-7450256887431843840-lelR)。

通过这些更新，AI 代理可以并行处理任务，直接读取、修改、测试代码库，并安全地反映变更[Source 7](https://www.linkedin.com/posts/abhijeet-pachpute_anthropic-redesigned-claude-code-for-desktop-activity-7450256887431843840-lelR)。

## 未来会怎样？

Anthropic 的此次变革不仅仅是改变了工具的外观，它提出了开发者应如何运用 AI 的新标准。未来，更多的 AI 服务将采用“标准协议（MCP, Model Context Protocol，不同 AI 工具为交换信息而使用的通用语言）”来连接不同的代理[Source 14](https://www.zdnet.com/article/google-joins-openai-in-adopting-anthropics-protocol-for-connecting-ai-agents-why-it-matters/)。

我们所展望的未来，不仅在于 AI 变得更聪明，还在于**“AI 之间如何做到互不冲突地协作，以及人类指挥者如何高效地统御它们”**。正如源代码控制系统拥抱了 AI 时代一样，未来我们周边的所有开发环境都将演变为“代理优先”的时代。

## 参考资料

1. Redesigning source control at Anthropic (https://www.anthropic.com/research/redesigning-source-control)
2. Claude Code Desktop Redesign: Parallel Agents (2026) (https://www.eigent.ai/blog/claude-code-desktop-redesign)
3. Projects redesigned: from folder to conversation | Claude by Anthropic (https://claude.com/blog/projects-redesigned)
4. Anthropic Turns Claude Code Projects Into a Parallel AI... - KingyAI (https://kingy.ai/news/anthropic-claude-code-projects-ai-agents/)
5. Anthropic redesigns Claude Code desktop app to better handle... (https://completeaitraining.com/news/anthropic-redesigns-claude-code-desktop-app-to-better/)
6. Anthropic redesigns Claude Projects as multi-agent coordinator (https://www.brocker.org/anthropic-redesigns-claude-projects-multi-agent-coordinator-claude-code)
7. Anthropic redesigned Claude Code for desktop. tl;dr This is a serious... (https://www.linkedin.com/posts/abhijeet-pachpute_anthropic-redesigned-claude-code-for-desktop-activity-7450256887431843840-lelR)
14. Google joins OpenAI in adopting Anthropic's protocol for connecting AI agents - ZDNET (https://www.zdnet.com/article/google-joins-openai-in-adopting-anthropics-protocol-for-connecting-ai-agents-why-it-matters/)