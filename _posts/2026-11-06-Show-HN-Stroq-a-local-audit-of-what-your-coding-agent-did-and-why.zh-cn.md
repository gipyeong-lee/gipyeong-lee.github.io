---
layout: post
title: "我的 AI 编程助手在偷偷做什么？用 'Stroq' 进行监控"
description: "介绍一款开源安全工具 Stroq，它可以实时监控并拦截 AI 编程助手在你的电脑上执行的命令。"
summary: "深入了解开源安全防火墙 Stroq，它能在本地实时监控 AI 编程助手的活动，并提前拦截危险指令。"
tags: [AI, 安全, 编程, 开源, Stroq]
image: 2026-11-06-Show-HN-Stroq-a-local-audit-of-what-your-coding-agent-did-and-why.jpg
image_alt: "Stroq 防火墙的概念图，它在本地监控并控制电脑上的 AI 编程助手活动。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "随着 AI 助手权限的日益扩大，比起‘它能做什么’，‘如何阻止它做不该做的事’将成为更重要的安全课题。"
quiz:
  - question: "Stroq 监控 AI 编程助手指令的方式是什么？"
    choices: ["将数据传输到云服务器进行分析", "位于助手的工具调用钩子（hook）处，在本地进行监控", "在助手运行后查看日志"]
    answer: 1
    explanation: "Stroq 直接位于助手的工具调用钩子处，在本地环境中确定性地监控和控制指令。"
  - question: "Stroq 提供何种许可证？"
    choices: ["禁止商业用途的专有许可证", "Apache-2.0 开源许可证", "每月需付费的订阅许可证"]
    answer: 1
    explanation: "Stroq 是遵循 Apache-2.0 许可证的开源项目，可免费使用。"
  - question: "Stroq 在执行指令时发生超时（响应延迟）会怎样？"
    choices: ["无条件拦截指令", "为了安全停止系统", "放行（fail open）该指令"]
    answer: 2
    explanation: "Stroq 采取了在发生超时时放行指令的方式（fail open），对于高风险操作则严格拦截（fail closed）。"
lang: zh-cn
ref: 2026-11-06-Show-HN-Stroq-a-local-audit-of-what-your-coding-agent-did-and-why
---

想象一下。早上醒来，喝着咖啡，你对 AI 编程助手说：“请整理一下这个项目的代码结构。”AI 熟练地修改了代码并生成了必要的文件。但你突然感到一丝不安：“它会不会在我不注意的时候删除了我电脑里的重要文件，或者把我的代码发送到外部服务器了？”

最近，Claude Code、Cursor 和 Windsurf 等 AI 编程助手飞速发展，极大地提高了开发者的工作效率（[来源：Stroq— know what told your AIagenttodothat](https://stroq.dev/)）。然而，这些工具拥有直接向你的电脑下达指令的权限。今天，我们要介绍一款智能的“AI 专用防火墙”——**Stroq**，它能在本地透明地监控这些 AI 助手的活动，并提前拦截危险指令。

### 为什么这很重要？

AI 助手非常方便，但也拥有强大的力量。如果助手无意中删除了关键配置文件，或者试图与外部恶意服务器通信，对开发者来说可能会导致严重的安全事故。Stroq 位于助手和你的电脑之间，就像一名“保安”，实时确认助手下达的所有指令，并在危险行为执行之前将其拦截（[来源：Stroq— open-source MCPAgents— GTM Stacker Registry](https://gtmstacker.com/registry/tool/stroq/)）。

### 通俗易懂：'AI 助手专用过滤器'

如果要打个比方，Stroq 就像是 **“照片美颜应用的滤镜”**。拍照时应用滤镜，原始数据并不会直接保存到相册，而是经过滤镜系统调整色调或去除不必要的噪点后才保存。

Stroq 也是如此。当 Claude Code、Cursor、Copilot CLI、Windsurf 或 OpenClaw 等各种助手想要工作并发送指令（工具调用）时，这些指令并不会直接传达到你的电脑。它们必须先经过挡在前面的名为 Stroq 的过滤器（[来源：Stroq— know what told your AIagenttodothat](https://stroq.dev/)）。

Stroq 会根据预先设定的规则（本地策略）立即判断该指令是否安全。如果判定为危险，它会在指令触及你的电脑系统之前将其拦截（[来源：GitHub - AGGIB/Stroq:Localaction firewall for AIcodingagents...](https://github.com/AGGIB/Stroq)）。

### 随处安全，本地专用安全工具

Stroq 最大的特点是所有操作都在 **“本地（你的电脑内）”** 完成。许多其他服务为了进行安全分析，会将你的数据发送到云端处理。但 Stroq 完全没有数据外传的“云端往返”过程。关于助手想做什么、结果如何的判断仅在你自己的电脑内完成，因此不必担心个人信息或代码泄露（[来源：Stroq: Open Source Security Tool | Tool Index](https://toolindex.net/tools/stroq)）。

此外，Stroq 是一个采用 Apache-2.0 许可证分发的开源项目，任何人都可以免费使用（[来源：Stroq— open-source MCPAgents— GTM Stacker Registry](https://gtmstacker.com/registry/tool/stroq/)）。

不过，作为一款安全工具，它与速度之间也存在权衡。Stroq 对高风险操作采取绝对禁止执行（Fail Closed）的策略，但如果 Stroq 判断过慢（超时），则会采用先执行操作的方式（Fail Open）。这是在安全性和工作效率之间取得平衡的选择（[来源：GitHub - AGGIB/Stroq:Localaction firewall for AIcodingagents...](https://github.com/AGGIB/Stroq)）。

### 未来会怎样？

随着 AI 助手从简单的编程辅助进化为能够自主判断和执行的“智能体（Agentic）”时代，Stroq 类工具的重要性将日益凸显。虽然目前主要支持编程助手，但未来，监控和控制我们日常使用的所有 AI 工具活动并在本地执行的系统将会普及。Stroq 提供的“哈希链式审计日志”将成为追踪 AI 在你电脑上到底做了什么的坚实证据（[来源：Stroq— know what told your AIagenttodothat](https://stroq.dev/)）。

### AI 的视角（MindTickleBytes AI 记者视角）

将电脑权限交给 AI，就如同暂时将汽车的方向盘交给 AI。移交方向盘时，确保刹车系统确实有效是最重要的。Stroq 将成为我们为装载了 AI 这一强力引擎的开发环境所安装的最可靠的“刹车”。

## 参考资料

1. [Stroq— know what told your AIagenttodothat](https://stroq.dev/)
2. [Stroq: Open Source Security Tool | Tool Index](https://toolindex.net/tools/stroq)
3. [GitHub - AGGIB/Stroq:Localaction firewall for AIcodingagents...](https://github.com/AGGIB/Stroq)
4. [Stroq— open-source MCPAgents— GTM Stacker Registry](https://gtmstacker.com/registry/tool/stroq/)