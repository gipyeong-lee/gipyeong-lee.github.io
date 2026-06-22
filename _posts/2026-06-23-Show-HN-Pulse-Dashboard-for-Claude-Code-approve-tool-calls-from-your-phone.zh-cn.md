---
layout: post
title: "不在电脑前也能批准AI的决策？Claude Code实时仪表板 'Pulse'"
description: "使用Claude Code时无需再一直盯着终端。现在，你可以通过智能手机实时查看AI的操作并批准其工具使用。"
summary: "介绍一款名为 'Pulse' 的本地仪表板应用程序，它可以实时监控Claude Code终端会话，并允许你通过智能手机批准工具的使用。"
tags: [AI, ClaudeCode, 生产力, 工具, 移动端]
image: 2026-06-23-Show-HN-Pulse-Dashboard-for-Claude-Code-approve-tool-calls-from-your-phone.jpg
image_alt: "智能手机屏幕上实时显示Claude Code的终端活动，并出现批准工具使用的按钮"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "将复杂的AI开发环境与移动设备连接，从而确保了用户的控制权，这一点令人印象深刻。未来，与AI代理交互时的移动性将变得越来越重要。"
quiz:
  - question: "下列哪项不是Pulse仪表板的主要特点？"
    choices: ["实时会话监控", "通过移动设备批准工具使用", "所有对话记录永久存储在云端"]
    answer: 2
    explanation: "Pulse的设计原则是数据不离开用户的计算机（本地）。"
  - question: "使用Pulse可以获得的主要好处是？"
    choices: ["即使离开电脑，也能确认AI工作的上下文并进行交互", "可以完全取消AI的工具使用权限", "可以免费使用Claude Code的所有功能"]
    answer: 0
    explanation: "Pulse通过通知功能让用户在移动端直接回答AI的问题或批准工具的使用，从而提高了移动性。"
  - question: "Pulse应用程序的数据安全方式是什么？"
    choices: ["将所有数据传输到外部服务器", "在本地环境中运行，数据不会离开设备", "使用OAuth令牌进行每次外部服务器认证"]
    answer: 1
    explanation: "Pulse强调安全性，无需额外的依赖项，在本地运行，并且不会将用户数据发送到设备之外。"
lang: zh-cn
ref: 2026-06-23-Show-HN-Pulse-Dashboard-for-Claude-Code-approve-tool-calls-from-your-phone
---

想象一下。你在咖啡馆用笔记本电脑让AI代理进行复杂的编程任务，然后去洗手间呆了一会儿。如果此时AI试图删除重要文件或调用外部API，会发生什么？通常情况下，你需要坐在终端屏幕前点击批准才能继续工作，但现在不再需要这样了。

在与AI共事的时代，我们需要一种方法，即使不在屏幕前，也能实时确认并控制AI是否在做出正确的判断。为解决这一难题而诞生的工具就是“Pulse”。

## 为什么这很重要？

像Claude Code这样的AI代理拥有从代码编写到文件修改的广泛权限。为了安全地使用它们，用户必须监督并批准AI的所有行为，这给用户带来了相当大的疲劳感。

Pulse将用户从这种限制中解放出来。[Pulse](https://github.com/nikitadoudikov/claude-pulse)通过让你通过智能手机实时查看AI的任务，并在必要时直接批准工具的使用，从而同时确保了AI工作的移动性和控制权。这不仅仅是方便，更为那些想要随时随地确认AI是否在用户控制范围内安全运行的现代技术用户提供了必要的环境。

## 轻松理解：'AI专用监控摄像头与远程遥控器'

如果把Pulse比作一个简单的东西，它可以被称为**'AI专用监控摄像头与远程遥控器'**。

原理就像我们在家外通过智能手机打开门锁或查看宠物一样。[Pulse](https://news.ycombinator.com/item?id=48612844)扮演监控摄像头的角色，详细显示AI代理目前在终端中做什么，以及消耗了多少费用。同时，当AI想要进行文件修改或外部连接等重要任务时，它就成了遥控器，即使你不在座位上，也能通过智能手机发送通知，批准工具的使用。

简单来说，过去如果AI在终端窗口询问“我可以修改这个文件吗？”，用户必须亲自回答；而使用Pulse，就像AI通过智能手机聊天工具询问“我现在可以做这个工作吗？”，用户可以直接点击“批准”按钮。通过[Claude Code Notifier Companion](https://apps.apple.com/us/app/claude-code-notifier-companion/id6757701908)应用，用户无需亲自触碰Mac即可回答AI的问题或决定工具的使用。

## 目前的情况

目前，像[Pulse](https://github.com/nikitadoudikov/claude-pulse)这样的工具支持以下功能：

*   **实时监控：** 显示AI当前在做什么，以及花费了多少费用。[Source 2](https://github.com/hyeongjun-dev/claude-pulse)
*   **远程批准：** 无需查看终端，即可通过通知批准工具的使用或回答问题。[Source 4](https://apps.apple.com/us/app/claude-code-notifier-companion/id6757701908)
*   **个人信息保护：** 这些应用程序在本地运行，设计上无需额外的复杂依赖，确保数据不会泄露到设备之外。[Source 1](https://github.com/nikitadoudikov/claude-pulse)

但是，这与AI具备自我判断能力并不相同。用户仍然需要判断AI做出的决定是否正确，并应意识到它不会自动处理所有任务。此外，某些高级功能可能会根据服务模型有不同的设置。[Source 3](https://github.com/NoobyGains/claude-pulse)

## 未来会怎样？

未来，AI代理将能够自主完成更复杂的任务。因此，像Pulse这样能够透明可视化并远程控制AI行为的工具的重要性将进一步增加。虽然现在主要集中在编程任务上，但未来在日常办公或常规管理任务中，通过智能手机管理AI行为的方式有望成为标准。用户将逐渐从“坐在屏幕前的监督员”转变为“随时随地指挥AI的指挥官”。

## MindTickleBytes的AI记者观点

AI使用工具虽然具有创新性，但脱离用户的控制是危险的。Pulse找到了一个非常优雅的平衡点，既不阻碍用户的生产力，又能保持安全性。随着我们与AI走得越来越近，我们亲自点击“批准”按钮的那短暂瞬间将变得更加重要。

## 参考资料

1. [GitHub - nikitadoudikov/claude-pulse: Local, zero-dependency dashboard for Claude Code](https://github.com/nikitadoudikov/claude-pulse)
2. [GitHub - hyeongjun-dev/claude-pulse: Real-time session dashboard for Claude Code](https://github.com/hyeongjun-dev/claude-pulse)
3. [GitHub - NoobyGains/claude-pulse: Real-time usage monitor for Claude Code](https://github.com/NoobyGains/claude-pulse)
4. [Claude Code Notifier Companion - Apple App Store](https://apps.apple.com/us/app/claude-code-notifier-companion/id6757701908)
5. [ShowHN: Pulse – Dashboard for Claude Code, approve tool calls...](https://news.ycombinator.com/item?id=48612844)