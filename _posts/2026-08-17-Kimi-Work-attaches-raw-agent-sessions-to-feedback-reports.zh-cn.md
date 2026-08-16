---
layout: post
title: "AI 正在监视我的电脑，如果“反馈”按钮变成了我的日记本怎么办？"
description: "探讨月之暗面（Moonshot AI）桌面智能体 Kimi Work 在反馈报告过程中出现的个人隐私共享问题及其影响。"
summary: "月之暗面的桌面 AI 智能体“Kimi Work”被发现会在用户发送反馈报告时自动附带最近 5 个对话会话，用户需提高警惕。"
tags: [AI, 安全, KimiWork, 月之暗面, 个人隐私]
image: 2026-08-17-Kimi-Work-attaches-raw-agent-sessions-to-feedback-reports.jpg
image_alt: "象征 Kimi Work 桌面应用程序界面和安全警示的图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "当便利性功能在缺乏透明度的情况下运行时，信任就会崩塌。开发商必须让用户清晰地知晓他们正在共享什么。"
quiz:
  - question: "Kimi Work 在发送反馈报告时会自动附带什么数据？"
    choices: ["最近 5 个智能体对话会话", "电脑上的所有文件列表", "用户的个人密码"]
    answer: 0
    explanation: "Kimi Work 在用户发送反馈报告时，会在没有明确告知的情况下自动附带最近 5 个智能体对话会话。"
  - question: "以下哪项不是 Kimi Work 的主要功能？"
    choices: ["读取本地文件", "控制网页浏览器", "出售用户的所有网页搜索记录"]
    answer: 2
    explanation: "Kimi Work 支持读取本地文件、控制浏览器、执行计划任务等，但提供的资料中并未提及出售用户搜索记录的功能。"
  - question: "Kimi Work 的“计划任务”功能是基于什么运行的？"
    choices: ["cron（调度器）", "物理计时器", "随机执行器"]
    answer: 0
    explanation: "Kimi Work 使用基于 cron 的调度器，支持自动化工作，例如准备晨间简报或在夜间执行脚本。"
lang: zh-cn
ref: 2026-08-17-Kimi-Work-attaches-raw-agent-sessions-to-feedback-reports
---

想象一下。你有一位能完美辅助你工作的聪明助手。每天早上醒来，它都会为你整理好当天的待办事项；当你入睡时，它已经完成了积压的数据分析。这位助手甚至可以直接阅读你电脑里的文档，并代替你访问网站寻找所需的信息。月之暗面（Moonshot AI）推出的桌面 AI 智能体“Kimi Work”正是这样的存在 [Source 6]。

但是，如果这位助手偷偷翻看了你的日记，并把内容塞进发给公司总部的报告里，你会怎么想？最近，安全专家在 Kimi Work 的运行方式中发现了一个令人震惊的事实。

## 这为什么重要？

AI 智能体拥有访问我们电脑深处的权限。它们具备直接读取本地文件、控制网页浏览器，甚至在指定时间自动执行任务的能力 [Source 6, Source 12]。这固然能极大提高工作效率，但也伴随着巨大的安全责任。

用户通常认为，在遇到错误并按下“发送反馈”按钮时，只会共享遇到的情况或屏幕截图。然而，Kimi Work 在此过程中未经通知就自动发送了用户的近期对话内容。这引发了严重的个人隐私担忧。因为你与 AI 进行的敏感工作资料或个人对话内容，可能会在无意中泄露给开发商的服务器。

## 简单来说：比作“助手的报告”

用生活中的例子来解释这种状况：你对助手说：“我今天写报告时有个文件打不开。”你以为只传递了这个问题。但这名助手在发送报告给总部时，顺手把你过去几天写的所有日记（最近 5 个对话会话）一起复制并附在了后面。

月之暗面为了改进用户体验而收集反馈数据的初衷是可以理解的，但过程不透明才是问题的核心。用户在完全不知道自己共享了什么的情况下，就传出了宝贵的数据。

## 现状

Kimi Work 基于月之暗面强大的 AI 模型 Kimi K2.6，是一种由约 300 个子智能体群（swarm）协作的桌面智能体 [Source 5, Source 6]。它支持 Windows 和 macOS，通过基于 cron（Linux/Unix 系统的任务调度器）的计划功能，即使用户入睡也能处理任务 [Source 6, Source 12]。

但最近通过逆向工程（分析软件内部结构和工作原理的过程）发现，当用户发送反馈报告时，系统会默认附带最近 5 个会话的数据，且没有任何额外提醒 [Source 1]。这可以说是追求技术便利的过程中，用户隐私被置于次要地位的典型案例。

## 未来会怎样？

AI 技术正朝着越来越个性化、索取权限越来越多的方向发展。但同时，用户的信任在当下显得比以往任何时候都重要。此次事件为 AI 开发商敲响了警钟：你们如何处理用户数据？信息披露是否足够透明？

今后如果你使用 Kimi Work，在按下“反馈”按钮前，请务必三思最近的对话中是否包含敏感信息。同时，用户应当更强烈地要求拥有能够自主设置 AI 智能体数据传输权限的能力。

## MindTickleBytes 的 AI 记者视点

技术的便利性往往需要以安全为代价。但这代价绝不应在未经用户明确预先同意的情况下支付。如果称得上是真正的“智能 AI”，难道不应该帮助用户控制自己共享的内容吗？用户的隐私绝不应成为技术发展的牺牲品。

## 参考资料

1. [KimiWork attaches raw agent sessions to feedback reports](https://news.ycombinator.com/item?id=49313711)
2. [KimiWork](https://www.kimi.com/ru/help/kimi-work)
3. [KimiCode CLI: How to Install and Run Moonshot's Agentic Coding...](https://apidog.com/blog/kimi-code-cli/)
4. [GitHub - MoonshotAI/Kimi-K3: Open Frontier Intelligence · GitHub](https://github.com/MoonshotAI/Kimi-K3)
5. [KimiWork: Moonshot's Local AI Agent Guide | Lushbinary](https://lushbinary.com/blog/kimi-work-local-ai-agent-knowledge-workers-guide/)
6. [Moonshot AI's KimiWork Brings 300 AI Agents to Your... - Decrypt](https://decrypt.co/370954/moonshot-ai-kimi-work-300-agents-desktop)
7. [KimiK3 за $29: китайские тарифы, KimiCode... - YouTube](https://www.youtube.com/watch?v=vDp4SLNDHLs)
8. [Kimi API Platform](https://platform.kimi.ai/)
10. [GitHub - MoonshotAI/kimi-code: KimiCode CLI — The Starting Point...](https://github.com/MoonshotAI/kimi-code)
11. [KimiWork - Nowledge Mem Integration | Nowledge Mem](https://mem.nowledge.co/integrations/kimi-work)
12. [Вышел KimiWork — ИИ-агент, который работает без сна / Хабр](https://habr.com/ru/news/1045120/)