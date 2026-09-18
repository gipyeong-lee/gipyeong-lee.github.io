---
layout: post
title: "AI 编程助手，现在可以无‘语言障碍’协作：开始支持 AGENTS.md"
description: "Anthropic 的 Claude Code 终于开始支持 AGENTS.md 标准了。我们将探讨在多个 AI 工具之间切换编程时，这会带来哪些便利。"
summary: "随着 Claude Code 开始支持开源标准 AGENTS.md，开发人员可以更自由地交叉使用各种 AI 工具，并提高项目管理的效率。"
tags: [AI, 编程, 开发者, ClaudeCode, 生产力]
image: 2026-09-19-Anthropic-finally-adds-AGENTSmd-support-to-Claude-Code.jpg
image_alt: "一幅形象化的图像，展示了各种 AI 编程工具通过一个共同的规则文件 AGENTS.md 连接在一起。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "工具间的兼容性是技术生态系统成熟度的指标。选择开放标准而非封闭政策，是改善 AI 开发者体验的重要一步。"
quiz:
  - question: "AGENTS.md 文件起什么作用？"
    choices: ["帮助 AI 理解项目技术栈、编码规范等的通用指南", "存储 AI 模型权重的数据文件", "提高代码执行速度的编译优化文件"]
    answer: 0
    explanation: "AGENTS.md 是一种通用规格的 Markdown 文件，包含项目的技术栈或编码风格等规则，旨在帮助 AI 编程代理更好地理解代码库。"
  - question: "此次更新后，如何在 Claude Code 中使用 AGENTS.md？"
    choices: ["必须删除原有的 CLAUDE.md 才能使用", "在没有 CLAUDE.md 的情况下，可以通过自动读取 AGENTS.md 的回退（Fallback）方式使用", "不再支持 Markdown 文件"]
    answer: 1
    explanation: "当 Claude Code 没有找到原有使用的 CLAUDE.md 时，会自动读取 AGENTS.md 文件并将其用作项目指南。"
  - question: "AGENTS.md 标准化为开发者带来的主要好处是什么？"
    choices: ["AI 的计算能力翻倍", "通过一个规则文件即可实现多个 AI 工具的高效协作", "不再需要编写代码"]
    answer: 1
    explanation: "使用标准化的 AGENTS.md 后，多个 AI 编程代理之间的指令可以兼容，无需在更换工具时重新设置，从而提高了维护效率。"
lang: zh-cn
ref: 2026-09-19-Anthropic-finally-adds-AGENTSmd-support-to-Claude-Code
---

想象一下。如果你在客厅用法语交谈，然后走进厨房必须改用英语继续对话，但每次都要从头重新解释对话内容或规则，那该有多累？

最近，许多开发者在与 AI 编程助手协作时，都经历过类似的“挫败感”。因为有些 AI 工具喜欢这套规则，而另一些则遵循那套规则。但终于，Anthropic 的 AI 编程工具“Claude Code”发布了一项解决该问题的重要更新。现在，Claude Code 也可以使用开发者中广泛采用的标准规格“AGENTS.md”了。

### 为什么这一变化很重要？ (Why It Matters)

对于开发者来说，时间就是竞争力。每次都要向 AI 编程助手重新解释项目的性质、技术栈（所使用的编程工具组合）以及团队的编码习惯，是一种巨大的浪费。此前，Claude Code 一直坚持使用名为“CLAUDE.md”的自有规格，但这与其他 AI 工具不兼容，导致开发者在交替使用多个工具时非常不便 [[来源标题](https://eu.36kr.com/en/p/3955873528626311)]。

随着这一变化，只要写好一个规则文件，不仅是 Claude Code，其他许多 AI 工具也能将其作为通用指南。简而言之，所有 AI 工具现在共享了一个“标准语法”。

### 简单来说，什么是“AGENTS.md”？ (The Explainer)

“AGENTS.md”到底是什么，为何如此引人注目？打个比方，这个文件就是**“AI 的项目使用说明书”**。

就像我们组装新乐高套件时查看盒子里的说明书一样，AI 编程助手读取这个 `AGENTS.md` 文件后，就能立即掌握：“啊，这个项目是用 Python 构建的”，“编写代码时倾向于这种风格” [[来源标题](https://github.com/anthropics/claude-code/issues/6235), [来源标题](https://epokha.ai/blog/kak-nikogda-ne-upiratsia-v-limity-claude-i-codex)]。

如果说过去每个工具都需要不同的说明书，那么现在，只需一份被超过 6 万个开源项目采用的标准说明书，即可与所有 AI 工具进行沟通 [[来源标题](https://eu.36kr.com/en/p/3955873528626311)]。这样一来，开发者无需每次根据工具调整设置，只需专注于项目本身。

### 当前情况 (Where We Stand)

Anthropic 的这一决定是积极接纳社区声音的结果。包括 Shopify 首席执行官 Tobi Lutke 在内的许多开发者指出了多工具间的兼容性问题，并强烈强调了标准化的必要性 [[来源标题](https://x.com/i/trending/2092264944116850961)]。

目前，Claude Code 在保留原有 `CLAUDE.md` 方式的同时，采用了如果在项目根目录下存在 `AGENTS.md` 就会自动读取它的“回退（Fallback）”方式 [[来源标题](https://codex.danielvaughan.com/2026/06/13/anthropic-overtakes-openai-business-adoption-codex-cli-vendor-diversification-platform-hedging/)]。也就是说，无需立即更改所有设置，只要准备好标准文件，工具就会灵活应对。Anthropic 的 Thariq 也承诺，将接纳开发者的这些反馈，使 Claude Code 变得更加开放和易用 [[来源标题](https://x.com/i/trending/2092264944116850961)]。

### 未来会怎样？ (What's Next)

未来的 AI 编程环境将迅速从“以工具为中心”转向“以项目为中心”。随着 AI 模型无论工具种类如何都能更准确地把握项目本质，开发者将能够把更多的精力投入到策划和设计中，而不是学习如何使用工具。

此外，这次更新也表明 AI 行业正在跨越封闭的生态竞争，进入确保以用户为中心的兼容性这一成熟阶段。Anthropic 也承认，与其试图用自有规格将开发者“锁定”，不如遵循大家都约定的标准，这样才能使整个生态系统的生产力最大化。

### MindTickleBytes AI 记者视点

技术的进步速度很快，但最好的技术是那种能让用户“忘记工具存在”的技术。这次变化减少了开发者为每个 AI 工具的设置而烦恼的时间，转而让他们专注于更有创造性的问题解决，这是一个非常值得欢迎的消息。最终，我们正在朝着与 AI 进行更好对话、更顺畅协作的方向前进。

## 参考资料
1. [Claude Code Sparks Developer Backlash Over AGENTS.md Ban: Anthropic's Controversial Industry Standard Rejection & Official Response That Enraged the Dev Community](https://eu.36kr.com/en/p/3955873528626311)
2. [Feature Request: Support AGENTS.md. · Issue #6235 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/6235)
3. [Shopify CEO Pushes Anthropic to Support AGENTS.md in Claude Code / X](https://x.com/i/trending/2092264944116850961)
4. [Как не упираться в лимиты Claude и Codex: 14... — ЭПОХА ИИ](https://epokha.ai/blog/kak-nikogda-ne-upiratsia-v-limity-claude-i-codex)
5. [Anthropic Overtakes OpenAI in Business Adoption: What the Ramp AI...](https://codex.danielvaughan.com/2026/06/13/anthropic-overtakes-openai-business-adoption-codex-cli-vendor-diversification-platform-hedging/)