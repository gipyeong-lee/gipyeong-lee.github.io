---
layout: post
title: "AI 代替编程？开发者们选择了 'Codex'"
description: "在 OpenAI 的 Codex 和 Anthropic 的 Claude Code 这两款 AI 编程工具中，哪一款更受开发者青睐？通过 Homebrew 安装统计数据，一探 AI 编程代理的趋势。"
summary: "近期对过去 30 天 macOS 系统下 AI 编程工具安装数据的分析显示，OpenAI 的 Codex 已超越 Anthropic 的 Claude Code，成为更多开发者的首选。"
tags: [AI, 编程, 开发工具, Codex, ClaudeCode]
image: 2026-07-26-Codex-now-leads-Claude-Code-in-first-time-Homebrew-installs-for-last-30-days.jpg
image_alt: "展示代码在终端屏幕上自动生成的数字插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "开发者采用 AI 代理工具的速度非常快。工具间的竞争最终将转化为用户体验和性能提升等更好的结果。"
quiz:
  - question: "在近期的 Homebrew 安装统计中，哪款 AI 编程工具的安装率更高？"
    choices: ["Claude Code", "Codex", "两者相同"]
    answer: 1
    explanation: "根据近期统计，Codex 日均安装量达到 836 次，领先于 Claude Code（473 次）。"
  - question: "像 Claude Code 这样的“代理型编程工具”的主要特点是什么？"
    choices: ["仅在网页浏览器中运行", "在终端内将创意转化为代码", "仅执行设计任务"]
    answer: 1
    explanation: "这些工具直接在开发者的终端环境中运行，帮助将创意实现为实际代码。"
  - question: "Claude Code 的日均 GitHub 代码提交贡献量大约是多少？"
    choices: ["约 5 万个", "约 15 万个", "超过 32 万个"]
    answer: 2
    explanation: "Claude Code 每天生成超过 32.6 万次提交，约占所有公开提交的 10%。"
lang: zh-cn
ref: 2026-07-26-Codex-now-leads-Claude-Code-in-first-time-Homebrew-installs-for-last-30-days
---

想象一下，你是一名程序员，当需要实现复杂功能时，只需脑中浮现构思，AI 就会自动打开终端窗口并为你写好代码。就像有一位经验丰富的同行在旁边实时辅助你编码。这种梦想中的场景如今已成为现实。这得益于“代理型编程工具（Agentic Coding Tool，即在开发者终端环境中自主执行任务并编写代码的 AI）”。

近期，OpenAI 的 **Codex** 和 Anthropic 的 **Claude Code** 这两大 AI 工具在开发者群体中展开了激烈竞争。然而，最近出现了一些值得关注的变化。通过观察开发者在 macOS 上安装软件时最常用的“Homebrew（Mac 软件包管理器）”统计数据可以发现，选择 Codex 的开发者正在迅速增加。

### 为什么这很重要？

这不仅是安装数量的简单对比，更意味着开发者正在决定引入哪位 AI 合作伙伴进入自己的编码环境。终端驱动的 AI 编程代理不仅限于建议代码片段，还能理解整个项目并自主执行任务。[Source 2](https://docs.anthropic.com/en/docs/claude-code/overview), [Source 13](https://formulae.brew.sh/cask/codex) 

当这些工具成为日常，开发者将从重复性的编码工作中解放出来，专注于更具创造性的问题解决。换言之，这将为我们日常使用的 App 和网页服务变得更快、更智能奠定基础。

### 浅显易懂：AI 助手风格的差异

简单来说，**Claude Code** 和 **Codex** 就像是雇佣了不同风格的“助手”。比喻如下：

*   **Claude Code** 就像一位非常严谨的“模范生”助手。它在 SWE-bench 等开发能力评估中表现出色，且产出量惊人，占据了 GitHub 上所有公开提交的约 10%（每天超过 32.6 万次！）。[Source 9](https://www.morphllm.com/comparisons/codex-vs-claude-code)
*   **Codex** 是一位快速、灵活的“实战派”助手。根据近期统计，它通过 Homebrew 的日均安装量为 836 次，比 Claude Code 的 473 次高出约 1.77 倍。许多开发者似乎因为其更快的作业速度或特定的功能优势而转向了 Codex。[Source 8](https://x.com/tickerplus/status/2051344320028938670)

这两款工具都在终端内运行，等待开发者的指令。[Source 3](https://github.com/anthropics/claude-code), [Source 13](https://formulae.brew.sh/cask/codex) 就像在照片应用中应用滤镜来改变照片风格一样，开发者正在根据个人喜好选择工具，以优化自己的编程风格。

### 现状：开发者的选择是什么？

目前开发者群体对这两款工具的评价各异。从性能指标来看，两款 AI 各有千秋。[Source 11](https://aithinkerlab.com/openai-codex-vs-claude-code/) 哪款更好取决于开发者当前进行的项目类型以及偏好的工作方式。

*   **Claude Code** 的安装较为灵活。在 macOS 或 Linux 上可以使用 Homebrew 安装，在 Windows 环境下也可以通过原生安装程序、WinGet 或 npm 等方式轻松启动。[Source 3](https://github.com/anthropics/claude-code), [Source 4](https://claudeskills.ru/blog/claude-code-windows), [Source 16](https://code.claude.com/docs/en/quickstart) 
*   **Codex** 同样可以通过 Homebrew 在 Mac 环境下非常简便地进行安装和使用。[Source 5](https://www.verdent.ai/guides/codex-app-download-install-macos)

### 未来展望

AI 编程工具市场才刚刚进入开花期。两款模型都在持续优化性能，并根据开发者的反馈不断添加新功能。[Source 1](https://code.claude.com/docs/en/setup) 专家预测，未来 AI 将不仅仅是生成代码，还将发展出组成更复杂的代理团队进行协作的方式。[Source 9](https://www.morphllm.com/comparisons/codex-vs-claude-code)

时代正在从开发者逐行“撰写”代码，转变为“指令和管理”AI 执行工作的时代。在这个潮流中，哪款工具能成为标准，又或者是二者相互借鉴彼此的优点而变得更加强大，将是一个非常值得观察的看点。

---

### MindTickleBytes AI 记者视角
比起争论工具的优劣，更重要的是开发者们已经开始将 AI 视为自身的一部分来使用。在 AI 每天编写超过 30 万次代码提交的时代，我们或许需要重新定义什么是“开发”。

## 参考资料

1. Advanced setup - ClaudeCodeDocs (https://code.claude.com/docs/en/setup)
2. ClaudeCodeoverview - Anthropic (https://docs.anthropic.com/en/docs/claude-code/overview)
3. GitHub - anthropics/claude-code (https://github.com/anthropics/claude-code)
4. Установка ClaudeCode на Windows — пошаговый гайд 2026 (https://claudeskills.ru/blog/claude-code-windows)
5. How to Download & Install Codex App on macOS (https://www.verdent.ai/guides/codex-app-download-install-macos)
8. TickerTrends 🔬 on X (https://x.com/tickerplus/status/2051344320028938670)
9. Codex vs Claude Code (July 2026) (https://www.morphllm.com/comparisons/codex-vs-claude-code)
11. Claude Code vs OpenAI Codex: 30-Day Dev Test Results (2026) (https://aithinkerlab.com/openai-codex-vs-claude-code/)
13. Homebrew Formulae: codex (https://formulae.brew.sh/cask/codex)
16. Quickstart - ClaudeCodeDocs (https://code.claude.com/docs/en/quickstart)