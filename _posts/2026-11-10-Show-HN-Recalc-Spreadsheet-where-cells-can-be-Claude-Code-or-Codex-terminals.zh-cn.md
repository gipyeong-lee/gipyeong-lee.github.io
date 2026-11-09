---
layout: post
title: "如果 Excel 成为 AI 的终端？通过“Recalc”体验代理时代"
description: "介绍一款全新的开源电子表格“Recalc”，每个单元格均可运行 Claude Code 或 Codex，让你与 AI 代理协作。"
summary: "Recalc 是一款电子表格工具，它将表格中的每个单元格作为 AI 终端，协助多个代理共享数据并处理复杂的工作流。"
tags: [AI, 代理, 电子表格, Recalc, 生产力]
image: 2026-11-10-Show-HN-Recalc-Spreadsheet-where-cells-can-be-Claude-Code-or-Codex-terminals.jpg
image_alt: "屏幕显示多个 AI 代理会话在电子表格网格内同时运行"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "将复杂的编码代理工作流管理在熟悉的网格形式中是一种非常直观的方法。这是一个将 AI 与人类协作方式推向新高度的有趣尝试。"
quiz:
  - question: "在 Recalc 电子表格的每个单元格中可以执行什么操作？"
    choices: ["存储值", "进行公式计算", "执行终端命令及运行 AI 代理", "以上皆可"]
    answer: 3
    explanation: "Recalc 的设计初衷是让每个单元格不仅能处理简单数值或公式，还能直接运行终端命令、Claude Code 或 Codex 会话。"
  - question: "文中提到的 Recalc 操控 AI 代理的方式是什么？"
    choices: ["在不中断聊天的情况下编辑单元格来控制代理", "等待代理随机选择", "学习专门的编程语言"]
    answer: 0
    explanation: "Recalc 允许用户通过编辑电子表格单元格来直接操控代理的行为，而无需中断聊天流程。"
  - question: "Recalc 使用哪种技术来实现不同代理会话之间的通信？"
    choices: ["区块链", "MCP (Model Context Protocol) 服务器", "专用云端 API"]
    answer: 1
    explanation: "Recalc 利用 MCP 服务器帮助不同的单元格和会话之间共享数据并进行通信。"
lang: zh-cn
ref: 2026-11-10-Show-HN-Recalc-Spreadsheet-where-cells-can-be-Claude-Code-or-Codex-terminals
---

想象一下。你像往常一样打开 Excel 或 Google 表格。但这次，你没有在单元格中简单地输入数字，而是向 AI 发出指令：“分析这些数据并写一份报告草稿。”在旁边的单元格里，另一个 AI 代理（执行用户指示并自主工作的 AI）正在实时运行代码并搜寻必要信息。这就像是一群聪明的 AI 助手聚集在一本账簿里共同开会。

2026年11月8日，通过 GitHub 公布的开源电子表格工具 **“Recalc”** 正在将这样的未来变为现实 [Source 11]。

### 为什么这很重要？

到目前为止，处理 AI 代理时，我们通常被禁锢在聊天窗口这个狭小的空间里。当代理执行复杂任务时，如果需要与其他会话交换数据，通常需要手动保存文件或亲自配置复杂的编程接口（API），非常麻烦。

Recalc 将我们最熟悉的工具——“电子表格”变成了 AI 协作的枢纽。随着各个独立的代理会话能够在电子表格这个共同的网格中共享数据和交流，无论是 AI 评估还是复杂的业务处理过程（工作流），都变得更加直观可控 [Source 1, Source 11]。

### 简单理解

简单来说，如果现有的 AI 代理工作就像与“在密室里独自思考的研究员”对话，那么 Recalc 就提供了一个“多名研究员在一张巨幅图纸上共同绘图的环境”。

*   **数据流通的通道：** Excel 的单元格不再仅仅是存放数字的格子。每个单元格都是一个小型终端窗口，也是一个独立的空间，Claude Code（Anthropic 的 AI 编码代理）或 Codex 等 AI 代理常驻其中 [Source 10, Source 13]。
*   **数据共享：** 单元格之间是相互连接的。A 单元格中 AI 执行的结果，B 单元格中的另一个 AI 可以直接拿来使用。这是通过 **MCP（Model Context Protocol，AI 模型与外部数据或环境进行通信的规格）** 技术实现的，该规格起到了将整个应用程序有机粘合在一起的作用 [Source 1, Source 11]。

无需在聊天窗口中做冗长的说明，只需修改表格中的一个单元格，就能即时修正或指导 AI 代理的行为 [Source 10]。

### 当前状况

Recalc 目前作为一个开源项目进行开发，任何人都可以参与。主要特点如下：

*   **现场测试：** 开发人员为了在自己的创业公司中进行实际的 AI 性能评估（基准测试）而创建了该工具。例如，有一个演示案例是测试 AI 在预测美国食品药品监督管理局（FDA）提交文档的通过率方面有多准确 [Source 1]。
*   **运行环境：** 目前设计为在 macOS 环境下顺畅运行。虽然在 Linux 上也可以运行，但尚未经过充分测试，且暂不支持 Windows [Source 1]。
*   **安全：** 与 Claude Code 等工具联动时，它们通常在用户的本地计算机环境中执行。由于没有额外的后端服务器，直接与模型进行通信，因此在设计时充分考虑了安全性 [Source 3]。

### 未来前景

Recalc 展示了彻底改变 AI 与人类协作方式的可能性。未来，不仅是数据分析师，开发者和策划人员也可能通过电子表格来调度数十个 AI 代理。如果未来能够支持 Windows 并能在更多环境中轻松使用，它有望超越简单的重复性工作，成长为复杂的企业级业务管理工具 [Source 1]。

### MindTickleBytes 的 AI 记者视角

这是一个充分证明“工具越熟悉，AI 的能力扩展就越快”这一事实的案例。相比于学习新的复杂命令，用我们日常使用的表格编辑方式来操控 AI 显得更加直观，这正是 Recalc 最强大的武器。复杂的 AI 代理时代正比我们想象中更快地来到我们身边。

## 参考资料

1. [Show HN: Recalc – Spreadsheet where cells can be Claude Code or Codex terminals](https://github.com/sshah03/recalc)
2. [ClaudeCode by Anthropic | AI Coding Agent, Terminal, IDE](https://claude.com/product/claude-code)
3. [Recalc - Spreadsheet with Claude Code · Hacker News | Zeli](https://zeli.app/story/50413970)
4. [Recalc Spreadsheet Lets Cells Run Claude Code or Codex](https://emergent.sh/news/recalc-spreadsheet-lets-cells-run-claude-code)
5. [recalc/demos/done-means-green/repo/.codex at main - GitHub](https://github.com/sshah03/recalc/tree/main/demos/done-means-green/repo/.codex)
6. [recalc/CLAUDE.md at main · sshah03/recalc · GitHub](https://github.com/sshah03/recalc/blob/main/CLAUDE.md)