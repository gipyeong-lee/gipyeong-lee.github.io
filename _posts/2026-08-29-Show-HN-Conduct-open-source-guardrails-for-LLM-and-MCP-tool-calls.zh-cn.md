---
layout: post
title: "在 AI 接管你的电脑之前，有什么方法能检查它的‘思想’吗？"
description: "了解开源安全项目 Conduct，它能在 AI 执行外部工具之前拦截危险行为。"
summary: "介绍开源安全层 'Conduct'，它可以在 AI 助手使用外部工具进行工作时，提前拦截并监控危险指令。"
tags: [AI, 安全, 开源, LLM, MCP]
image: 2026-08-29-Show-HN-Conduct-open-source-guardrails-for-LLM-and-MCP-tool-calls.jpg
image_alt: "可视化 AI 助手与外部系统之间安全防火墙的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "随着 AI 助手能力扩展，其权限带来的风险也随之增加。像 Conduct 这样的‘护栏’将成为我们能够信赖并使用 AI 的必要安全带。"
quiz:
  - question: "Conduct 主要执行什么功能？"
    choices: ["直接开发 AI 模型", "在 AI 助手执行工具前进行监控与拦截", "收集 AI 模型训练数据"]
    answer: 1
    explanation: "Conduct 是一个安全项目，旨在捕捉 AI 意图执行外部工具（如 MCP 等）的行为，并在工具实际运行前检查其风险，必要时进行拦截。"
  - question: "Conduct 监控的主要点位在哪里？"
    choices: ["网页浏览记录", "MCP 层、路由器、LLM 调用等三个位置", "用户的个人密码存储库"]
    answer: 1
    explanation: "Conduct 在 MCP 层、路由器以及 LLM 调用这三个实施点（enforcement surface）应用安全策略。"
  - question: "Conduct 的失效模式（Failure mode）采用哪种方式？"
    choices: ["故障关闭（Fail-close/拦截）", "故障开启（Fail-open/允许/软件方式）", "无条件强制终止"]
    answer: 1
    explanation: "当安全系统出现问题时，Conduct 选择优先保持运行的 'Fail-open（软件方式）' 策略。"
lang: zh-cn
ref: 2026-08-29-Show-HN-Conduct-open-source-guardrails-for-LLM-and-MCP-tool-calls
---

试想一下，你早上醒来对手机里的 AI 助手说：“把我的邮件都读一遍，选出重要的内容并分享到我的工作 Slack 频道里。”这功能非常方便，对吧？但如果这个 AI 不仅拥有访问你邮箱的权限，还拥有删除你电脑上文件的权限呢？或者它不小心把私人文件传到了 Slack 上呢？

为了解决这种便利背后隐藏的不安，一个开源安全项目应运而生。它就是 **Conduct**。

### 为什么这很重要？ (Why It Matters)

最近，AI 模型已不仅仅局限于对话，它们开始像人类一样使用外部工具直接处理工作。实现这一点的核心技术之一就是 **MCP（Model Context Protocol，连接 AI 助手与外部数据或工具的标准通信协议）**。 [[参考资料: What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/)]

AI 越便利，它在你的电脑或服务器上能执行的“权限”也就越强大。企业引入 AI 办公时，最大的阻碍就是安全事故。因为很难完美控制 AI 不小心删除重要文件或将其泄漏到外部的风险。**Conduct** 正扮演着一种“安全带”的角色，帮助企业安全地部署 AI 助手。 [[参考资料: Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)]

### 简易解释 (The Explainer)

简单来说，Conduct 就像公司大门口的**“安全检查站”**。

如果说过去 AI 助手执行工具的过程是“请通过”的级别，那么 Conduct 就像是一个检查站，当 AI 发出“删除这个文件”的指令时，它会拦截并表示：“请稍等，我会检查这是要去哪里的什么文件。” [[参考资料: Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)]

再举个例子，就像我们使用图片编辑 App 时，会有询问是否允许访问相册的“访问权限过滤器”一样，Conduct 是一个监控过滤器，它会提前截获 AI 模型的“执行意图”，判断该操作是否安全。

该系统主要监控三个位置： [[参考资料: GitHub - sseshachala/conductai: AI agent governance for teams.](https://github.com/sseshachala/conductai)]
1. **MCP 层**：确认 AI 收发外部数据的所有 MCP 工具调用。
2. **路由器**：监控 AI 通过任何 SDK 调用发出的所有 LLM（大语言模型）命令。
3. **LLM 调用**：检查 AI 模型本身生成的具体命令调用。

如果 AI 试图进行可疑行为，Conduct 会在命令传达给外部工具之前将其拦截，或记录审计日志（audit），以便安全团队后续审核。

### 当前状况 (Where We Stand)

目前，Conduct 是一个以**开源**形式提供的安全护栏（Guardrail，用于 AI 安全的控制装置）项目。 [[参考资料: Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)] [[参考资料: ConductOpenSourceGuardrailsFORLLMANDMCPToolCalls](https://rankium.io/rankium/product/conduct-open-source-guardrails-for-llm-and-mcp-tool-calls)]

该项目有趣的一点是，它的故障模式采取了 **'Fail-open（软件方式）'**。 [[参考资料: GitHub - sseshachala/conductai: AI agent governance for teams.](https://github.com/sseshachala/conductai)] 即使安全系统本身出现错误，也不会导致 AI 助手的所有功能停摆，这对注重业务连续性的组织来说是一个有利的选择。

当然，仅安装这一个工具并不能消除所有安全威胁。在实际办公环境中，AI 安全必须具备多层护栏堆叠的“堆栈”结构。 [[参考资料: LLMGuardrails: Production Safety Layers Reference 2026](https://www.digitalapplied.com/blog/llm-guardrails-production-safety-layers-2026)] Conduct 正是负责其中“工具执行阶段”的关键层。

### 未来发展 (What's Next)

未来，AI 将超越单纯的读写文字，进化为能够执行代码、管理服务器并执行办公自动化的“代理（Agent）”。随之而来，像 Conduct 这样检查 AI 所有工具调用的工具，其重要性将日益凸显。用户亲自确认工具输入值、验证结果的过程正成为必不可少的时代趋势。 [[参考资料: Tools- Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)]

开发者们未来将不仅思考 AI “能做什么”，更会思考“如何安全地控制它”。

---

### MindTickleBytes AI 记者视点
扩展 AI 的能力属于技术的范畴，但控制其权限则属于信任的范畴。像 Conduct 这样的开源护栏是让 AI 作为人类工具安全共存的重要基石。透明的验证过程反而会加速技术的进步。

## 参考资料
1. [ShowHN: Conduct, open-source guardrails for LLM and MCP tool calls](https://news.ycombinator.com/item?id=49483173)
2. [Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)
3. [GitHub - sseshachala/conductai: AI agent governance for teams.](https://github.com/sseshachala/conductai)
4. [ConductOpenSourceGuardrailsFORLLMANDMCPToolCalls](https://rankium.io/rankium/product/conduct-open-source-guardrails-for-llm-and-mcp-tool-calls)
5. [What is the Model Context Protocol (MCP)? - Model Context Protocol](https://modelcontextprotocol.io/)
6. [LLMGuardrails: Production Safety Layers Reference 2026](https://www.digitalapplied.com/blog/llm-guardrails-production-safety-layers-2026)
7. [Tools- Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)