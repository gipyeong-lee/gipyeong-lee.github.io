---
layout: post
title: "AI聊着聊着突然停了？如何搞懂那些我不知道的 AI 用量限制"
description: "一位开发者因 AI 使用限制受阻，亲手制作了用量追踪工具。本文将带您了解其背后的故事及 AI 使用建议。"
summary: "为了解决无法查看 AI 模型使用限额（配额）带来的困扰，开发者们正尝试通过自制工具来主动追踪使用量。"
tags: [AI, Claude, 开发工具, 用量管理]
image: 2026-08-30-Show-HN-My-Claude-quota-ran-out-in-10-minutes-so-I-made-a-tool-to-find-out-why.jpg
image_alt: "电脑屏幕中，用户正在查看自己的 AI 模型使用统计数据。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "开发者主动解决问题的姿态展现了健康的生态系统。在平台提供更透明的信息之前，这些工具将发挥巨大作用。"
quiz:
  - question: "Claude Code 的使用量限制采用什么方式运作？"
    choices: ["每天午夜重置", "5小时滚动窗口", "每月固定令牌额度"]
    answer: 1
    explanation: "Claude Code 遵循 5 小时的滚动令牌使用窗口。"
  - question: "将同一文件上传到多个对话框会发生什么？"
    choices: ["只扣除一次令牌", "每次上传都会重新扣除", "无论文件大小均不限次数"]
    answer: 1
    explanation: "Claude 会将同一文件在不同对话框中的上传分别计算为新的令牌消耗。"
  - question: "Claude 中出现 'Capacity constraints' 消息的原因是什么？"
    choices: ["系统服务器故障", "用户账号被封禁", "整体用户需求增长导致的暂时性限制"]
    answer: 2
    explanation: "这不是服务故障，而是系统在管理高需求过程中产生的暂时性现象。"
lang: zh-cn
ref: 2026-08-30-Show-HN-My-Claude-quota-ran-out-in-10-minutes-so-I-made-a-tool-to-find-out-why
---

想象一下：今天早上，为了完成一个非常重要的编程项目，你正全神贯注地向 AI 提问。突然，AI 发来一条冰冷的消息：“抱歉，无法继续对话”。你明明觉得额度还很充足，结果才用了 10 分钟，额度就耗尽了。为什么会这样？我到底用了多少？

最近，黑客新闻（Hacker News）上出现了一个相关故事，一位开发者因无法忍受这种挫败感，亲自制作了一个解决方案，引发了广泛关注。[Show HN: My Claude quota ran out in 10 minutes, so I made a tool to find out why](https://news.ycombinator.com/item?id=49467551)

### 为什么这很重要？

AI 现在已成为我们日常生活中得力的助手。但正如 AI 服务并非完全免费一样，我们每天能使用的量也存在明确的“上限”。问题在于，用户很难准确掌握这个上限。

在不了解已使用额度及恢复时间的情况下使用 AI，往往会在关键时刻突然被中断。这就像在完全不知道油表还剩多少油的情况下驾驶汽车上高速。在 AI 赋能生产力比以往任何时候都重要的时代，这种不透明的使用环境已成为严重影响用户工作流的障碍。

### 简单类比：回转寿司与入场券

为什么会出现这种情况？简单来说，AI 服务商为我们分配了每日或特定时间段内可用的“入场券”。

像 Claude Code 这类服务采用的是“5小时滚动令牌使用窗口（5-hour rolling token usage window）”系统。[Claude Code Tool - Check how much of your quota is wasted (DracoMeter) - I made this](https://en.delphipraxis.net/topic/15338-claude-code-tool-check-how-much-of-your-quota-is-wasted-dracometer/) 这个系统可以类比为回转寿司店。如果你正在使用 AI，那么“过去 5 小时内”你所消耗的令牌（AI 识别的词汇单位）总和不能超过一定阈值。随着时间推移，最先使用的令牌额度会从“回转轨道”上移出，从而释放出新的使用空间。

但这里有一个陷阱：如果你将同一文件上传到多个对话框并进行提问，AI 会将这些文件识别为全新的内容，从而再次扣除令牌。[How I Stopped Hitting Claude's Usage Limits](https://artificialcorner.com/p/claude-limits-fix) 也就是说，即使你参考的是同一份文档，在 AI 眼中，它每次都在重新从第一页读到最后一页，进而消耗额外的“能量（令牌）”。

最终，我们在不知不觉中迅速耗尽了宝贵的“入场券”。

### 当前状况

目前，主流 AI 平台对于用户的令牌消耗细节采取了非常封闭的态度。Anthropic（Claude 的开发商）不会提供关于用户消耗量、或是哪个对话消耗最多的详细分析数据。[Claude Code Rate Limits & Usage Quotas Explained (2026)](https://www.truefoundry.com/blog/claude-code-limits-explained)

因此，像案例中那位感到困扰的开发者一样，许多人开始自制“使用量追踪工具”。[Tracking Claude, Codex, and Gemini Quotas from One Script](https://ianlpaterson.com/blog/tracking-claude-codex-gemini-quotas-from-one-script/) 他们通过编写脚本记录自己的 AI 使用情况（如保存为 JSON 文件），通过直观地查看消耗情况来改善使用习惯。

当然，我们偶尔看到的“Please try again soon”消息并不一定意味着服务故障，这只是系统为了管理整体用户需求而进行的临时限流。[Troubleshoot Claude error messages](https://support.claude.com/en/articles/12466728-troubleshoot-claude-error-messages) 即便如此，这种不透明度依然会让用户感到沮丧，从而更加渴望获得透明的信息。

### 未来趋势

预计 AI 的使用环境将会变得更加透明。随着用户需求的不断增长，AI 服务商可能会直接提供用量管理工具，或者更新功能帮助开发者自行优化使用量。

目前我们能做的最好方法是什么？首先，积极利用“项目（Projects）”功能，将文件只上传一次并在多个对话中共享。[How I Stopped Hitting Claude's Usage Limits](https://artificialcorner.com/p/claude-limits-fix) 此外，为防止 AI 使用受限，提前了解其他 AI 工具，或考虑使用固定费率的 API 也是明智之举。[Claudeusage limit reached: The Complete Guide for...](https://qcode.cc/en/claude-code-limits-russia)

### MindTickleBytes AI 记者视点

在 AI 变得越来越聪明的同时，如何“高效”地管理我们的使用过程也变得至关重要。在平台能够透明展示用量数据的那一天到来之前，我们作为智能用户，通过利用工具优化使用习惯，是实现这一进步的必要过程。

## 参考资料
1. [Tracking Claude, Codex, and Gemini Quotas from One Script](https://ianlpaterson.com/blog/tracking-claude-codex-gemini-quotas-from-one-script/)
2. [Claude Code Tool - Check how much of your quota is wasted (DracoMeter) - I made this](https://en.delphipraxis.net/topic/15338-claude-code-tool-check-how-much-of-your-quota-is-wasted-dracometer/)
3. [Troubleshoot Claude error messages](https://support.claude.com/en/articles/12466728-troubleshoot-claude-error-messages)
4. [How I Stopped Hitting Claude's Usage Limits](https://artificialcorner.com/p/claude-limits-fix)
5. [Claude Code Rate Limits & Usage Quotas Explained (2026)](https://www.truefoundry.com/blog/claude-code-limits-explained)
6. [Show HN: My Claude quota ran out in 10 minutes, so I made a tool to find out why](https://news.ycombinator.com/item?id=49467551)
7. [Claudeusage limit reached: The Complete Guide for...](https://qcode.cc/en/claude-code-limits-russia)