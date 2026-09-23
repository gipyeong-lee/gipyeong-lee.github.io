---
layout: post
title: "Claude Code 新增对 AGENTS.md 的支持，为什么在我的项目中无效？"
description: "在最新的 Claude Code 中配置了 AGENTS.md 文件但 AI 却无视它？本文为您解析原因及解决方案。"
summary: "Claude Code 从 2.1.277 版本开始支持 AGENTS.md，但在特定环境或设置下该功能可能无法正常工作，使用时需多加注意。"
tags: [ClaudeCode, AI, 开发工具, AGENTS.md]
image: 2026-09-23-Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on.jpg
image_alt: "现代技术图形，融合了编码工具 Claude Code 标志与文档文件图标"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "引入新标准总是伴随着早期的混乱。目前，继续使用 CLAUDE.md 是最稳妥的选择。"
quiz:
  - question: "当 Claude Code 中同时存在 CLAUDE.md 和 AGENTS.md 时，哪个文件具有优先权？"
    choices: ["AGENTS.md", "CLAUDE.md", "未知"]
    answer: 1
    explanation: "当两个文件同时存在时，Claude Code 会优先读取传统的 CLAUDE.md，而忽略 AGENTS.md。"
  - question: "目前官方明确不支持 AGENTS.md 功能的环境是哪里？"
    choices: ["终端", "桌面端 App", "Amazon Bedrock"]
    answer: 2
    explanation: "在 Amazon Bedrock、Vertex 和 Foundry 等环境中，目前尚不支持 AGENTS.md 功能。"
  - question: "在无法使用 AGENTS.md 的环境下，推荐的解决方案是什么？"
    choices: ["修改文件名", "将内容导入（import）到 CLAUDE.md 中", "强制开启该功能"]
    answer: 1
    explanation: "在无法直接支持 AGENTS.md 的情况下，将该文件的内容直接包含在 CLAUDE.md 中是最安全的做法。"
lang: zh-cn
ref: 2026-09-23-Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on
---

想象一下：你每天早上都会编写一份单独的说明文件，用来告诉 AI 编码工具项目的规则。然而，AI 却完全无视你精心编写的文件。最近，许多开发者都遇到了这种令人困惑的情况。这是因为在最近的更新后引入的新方式并没有如预期般流畅运行。

## 为什么这很重要？

Claude Code 是一款强大的“代理式编码工具”，它能阅读开发者的代码库、修改文件甚至直接执行命令（[Overview - Claude Code Docs](https://code.claude.com/docs/en/overview)）。一直以来，开发者们主要使用名为 `CLAUDE.md` 的文件来告知 AI 项目的编码规则或注意事项。

然而，最近有消息称将接受一种名为 `AGENTS.md` 的新格式作为标准，这让许多团队寄予厚望（[Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl](https://dev.blog/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)）。此次变革的核心目的是统一不同 AI 工具间的规则设置，但如果该功能无法正常运作，开发者精心编写的规则就无法传达给 AI，从而存在生成错误代码的风险。

## 轻松理解

将这种情况比作“学习新语言的学生”就很容易理解了：

*   **传统方式 (CLAUDE.md)**：这是 AI 以前学习并熟悉的旧教科书。
*   **新方式 (AGENTS.md)**：这是为了让 AI 学习得更系统而引入的新标准参考书。

然而，AI 要想阅读这本参考书，必须开启特定的“学习模式”。遗憾的是，在目前许多使用环境中，该模式默认是关闭的，或者 AI 根本没有阅读参考书的权限（[Claude Code's AGENTS.md Support: A Local Feature Locked Behind a Remote Switch](https://github.com/anthropics/claude-code/issues/95690)）。就好像 AI 不知道参考书的存在，或者没有意识到阅读它的必要性。特别是当使用数据收集（遥测，telemetry）功能关闭，或使用 Amazon Bedrock 等企业服务时，会出现完全无法读取该新规则文件的现象（[Claude Code reads AGENTS.md only when telemetry is on](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)）。

## 哪里出了问题？

从最新更新的 Claude Code 2.1.277 版本开始，增加了对 `AGENTS.md` 的支持（[Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog)）。但为了稳定使用，必须确认以下几个制约因素：

1.  **现有文件的优先级**：如果项目文件夹中同时存在 `CLAUDE.md` 和 `AGENTS.md`，AI 会按照惯例优先读取旧的 `CLAUDE.md`，而完全忽略新的 `AGENTS.md`（[Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl – rssfeedtelegrambot.bnaya.co.il](https://rssfeedtelegrambot.bnaya.co.il/index.php/2026/09/21/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)）。
2.  **环境限制**：Amazon Bedrock、Vertex 和 Foundry 等环境目前尚未官方支持此功能（[Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog)）。
3.  **内部连接方式**：该功能并未集成到 AI 的核心逻辑中，而是以内部连接的一种“插件”形式实现（[Claude Code Mods and agents.md: What's New and Why It Matters | MindStudio](https://www.mindstudio.ai/blog/claude-code-mods-agents-md)）。因此，如果特定条件未得到满足，很容易发生工具本身甚至无法识别文件的“静默失败（silent failure）”。

## 未来会怎样？

目前来看，仅靠 `AGENTS.md` 来托管规则存在较大的环境局限性。如果想在不支持的环境中共享规则，将相应内容直接包含（import）到现有的 `CLAUDE.md` 中是最安全且稳妥的做法（[Claude Code 2.1.277 reads AGENTS.md directly — resolution table, new silent-failure modes](https://github.com/fmslutions/harness-audit/issues/3)）。特别是对于那些计划在企业内部环境中采用 `AGENTS.md` 作为标准的团队，短期内需要多加注意（[Claude Code now also accepts instructions in OpenAI’s Agents.md format | InfoWorld](https://www.infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html)）。建议在后续更新扩大支持范围之前，继续沿用现有的方式。

## MindTickleBytes AI 记者视点
引入新标准是简化开发者复杂文件管理的一次精彩尝试。但此次案例表明，由于技术差距或环境设置差异，“聪明的 AI”有时反而会变成“睁眼瞎”。与其盲目跟进新技术，不如并行使用现有的成熟方案，这在当前阶段是保障工作连续性的最佳策略。

## 参考资料
1. [Claude Code reads AGENTS.md only when telemetry is on](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)
2. [Claude Code reads AGENTS.md only when telemetry is on - Hacker News](https://news.ycombinator.com/item?id=49814947)
3. [Set custom instructions for opencode.](https://opencode.ai/docs/rules/)
4. [Overview - Claude Code Docs](https://code.claude.com/docs/en/overview)
5. [How I use Claude Code (+ my best tips)](https://www.builder.io/blog/claude-code)
6. [Releases · anthropics/claude-code · GitHub](https://github.com/anthropics/claude-code/releases)
7. [AGENTS.md Just Turned One. The Evidence on... - Kernel Talks](https://kerneltalks.com/ai/agents-md-just-turned-one-the-evidence-on-whether-it-works-is-mixed/)
8. [claude-code/mods/agents-md/README.md at main · anthropics/claude-code](https://github.com/anthropics/claude-code/blob/main/mods/agents-md/README.md)
9. [1.2: Claude Code 2.1.277 reads AGENTS.md directly — resolution table, new silent-failure modes · Issue #3 · fmslutions/harness-audit](https://github.com/fmslutions/harness-audit/issues/3)
10. [[MODEL] Claude Code's AGENTS.md Support: A Local Feature Locked Behind a Remote Switch · Issue #95690 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/95690)
11. [Claude Code Mods and agents.md: What's New and Why It Matters | MindStudio](https://www.mindstudio.ai/blog/claude-code-mods-agents-md)
12. [claude-code/mods/agents-md at main · anthropics/claude-code](https://github.com/anthropics/claude-code/tree/main/mods/agents-md)
13. [Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl – rssfeedtelegrambot.bnaya.co.il](https://rssfeedtelegrambot.bnaya.co.il/index.php/2026/09/21/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)
14. [[incorrect-doctrine] "Claude Code reads CLAUDE.md, not AGENTS.md" is no longer true, and our setup command can silently switch a project's AGENTS.md off · Issue #1087 · fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills/issues/1087)
15. [Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog)
16. [Claude Code now also accepts instructions in OpenAI’s Agents.md format | InfoWorld](https://www.infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html)
17. [Claude Code Changelog (September 2026)](https://www.gradually.ai/en/changelogs/claude-code/)
18. [Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl - DevOps.com](https://devops.com/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)