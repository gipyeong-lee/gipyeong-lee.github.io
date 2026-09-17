---
layout: post
title: "AI 用着被“限流”停下了？一种和朋友们一起等待的新方法"
description: "当因为 AI 使用量限制不得不停止编码工作时，向您介绍这款可以和朋友们聊天消磨时光的 Mac 应用“Die With Me”。"
summary: "一款名为“Die With Me”的 Mac 应用问世，它能让你与朋友共享 AI 使用限额，并在被限流时一起聊天。"
tags: [AI, 工具, 生产力, 开发人员, Mac]
image: 2026-09-18-Show-HN-Die-With-Me-Claude-and-Codex-rate-limits-as-AIM-away-messages.jpg
image_alt: "展示“Die With Me”应用界面的图像，该应用可监控 AI 使用限额并与朋友进行交流"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "将 AI 使用量限制这一略显枯燥且令人沮丧的经历，用往昔即时通讯工具的情怀来化解，这一点非常有趣。这是一种将技术瓶颈转化为社交连接的巧妙构思。"
quiz:
  - question: "“Die With Me”应用提供了哪些功能？"
    choices: ["无限制使用 AI 模型", "查看朋友的 AI token 使用量并在等待室聊天", "提高 AI 响应速度"]
    answer: 1
    explanation: "该应用提供查看朋友 AI 使用量并在 token 限制剩余不足 20% 时与其他等待者聊天室交流的功能。"
  - question: "可以查看哪些 AI 模型的使用量？"
    choices: ["Claude 和 Codex", "ChatGPT 和 Gemini", "所有模型"]
    answer: 0
    explanation: "该应用专注于追踪 Claude 和 Codex 的使用限额。"
  - question: "“Die With Me”应用参考了哪款应用的设计？"
    choices: ["Discord", "过去 AIM 聊天软件的好友列表", "最新的社交媒体"]
    answer: 1
    explanation: "它将过去 AIM 即时通讯软件的好友在线列表（Buddy List）的情怀应用到了 AI token 使用量的监控中。"
lang: zh-cn
ref: 2026-09-18-Show-HN-Die-With-Me-Claude-and-Codex-rate-limits-as-AIM-away-messages
---

想象一下：你正沉浸在复杂的代码编写中，向 AI 助手寻求帮助时，屏幕上突然跳出一条消息：“您已达到使用量上限”。工作被迫中断，你只能焦急地等待限制解除。此时，一种无奈油然而生，心里难免会想：“难道只有我一个人这样吗？”

然而最近，一款 Mac 应用引起了广泛关注，它以一种复古社交软件般的怀旧方式化解了这种无奈，它就是“Die With Me”。这款应用将技术局限带来的冰冷现实，转化为一个充满人情味的温暖“候机室”。

## 为什么这很重要？

2026 年的今天，Claude Code 和 Codex 已成为许多开发人员不可或缺的核心 AI 编码代理 [[出处: Claude Code vs Codex: developers debate after - explainx.ai](https://explainx.ai/blog/claude-code-vs-codex-rate-limit-boost-2026)]。然而，这些强大的工具也面临着共同的困境——“使用量限制”。

对于开发者来说，AI 限流不仅仅是小小的不便，它更是彻底打断工作流的“杀手”。尤其是在多个工具间切换工作时，往往会丢失工作上下文（背景知识、AI 已理解的任务语境），导致不得不花费大量时间重新解释 [[出处: Show HN: `npx continues` – resume same session Claude, Gemini ...](https://news.ycombinator.com/item?id=47075089)]。“Die With Me”正是抓住了这一点，它将限流从单纯的技术故障转化为一种与朋友共享的社交体验。

## 轻松理解：AI 等待室里的“好友列表”

如果要把“Die With Me”比作什么，那它就像是**“把昔日即时通讯软件的好友状态显示器做成了 AI 使用量版本”**。

我们以前使用的 AIM 等聊天软件，都有一个“好友列表”，用来查看谁在线并打个招呼。这款应用能够实时显示朋友们的 Claude 或 Codex 剩余 token（AI 一次处理的数据单位）使用量 [[出处: Show HN: Die With Me – Claude and Codex rate limits as AIM away messages](https://blogviral010.blogspot.com/2026/09/show-hn-die-with-me-claude-and-codex.html)]。

例如，当朋友 A 在写代码且限额即将耗尽时，我可以实时获知这一状态。更有趣的是，当用户的 token 额度降至 20% 以下时，该应用不仅是一个个人的等待室，还会将你连接到“候机室聊天室”，让你与同样被限流、正在等待的其他朋友们交流 [[出处: Show HN: Die With Me – Claude and Codex rate limits as AIM away messages](https://blogviral010.blogspot.com/2026/09/show-hn-die-with-me-claude-and-codex.html)]。

这就像我们抢偶像演唱会门票失败时，在粉丝社区里互相慰藉一样。这是一种用人文连接填补技术缺失的方式。

## 现状：限流依然是开发者的烦恼

目前在开发生态圈中，围绕 Claude Code 和 Codex 的使用限额竞争十分激烈。Anthropic 正在持续调整 Claude Code 的使用限制 [[出处: Claude Code Limits Cut 17% Sept 14 (2026 Math) - explainx.ai](https://www.explainx.ai/blog/anthropic-claude-code-limits-17-percent-cut-september-2026-august-2026)]，许多开发者每天都在为了寻找适合自己工作风格的工具而苦苦挣扎 [[出处: Claude Code vs. Codex for Heavy Users: Limits, Costs, and ...](https://codeongrass.com/blog/claude-code-vs-codex-heavy-users-limits-costs-switching/)]。

但关键在于，无论工具如何进步，限制的壁垒始终存在。“Die With Me”并没有选择无视或规避这种局限，而是重新定义了这段等待时间——将其变为“共享时光”。通过这款应用，开发者们可以轻松问候一声：“我也被限流了，你那边怎么样？”，从而获得分享技巧、缓解压力的机会。

## 未来将会怎样？

未来，AI 编码工具的限流政策仍会根据情况灵活变动。也许有的日子充裕，有的日子紧巴巴。但“Die With Me”这类应用的出现，暗示了 AI 时代的一种新文化。

随着 AI 变得更加智能和便捷，我们将会更加关注的不是技术本身，而是那些与我们一同使用这些技术的人。下次当你在工作时看到 AI 使用量限制提醒，别再郁闷了。不妨把它看作是一个进入候机室、与朋友们闲聊放松片刻的机会吧。

## MindTickleBytes AI 记者视点

当技术尚不完美时，人们才有机会聚集在一起。“Die With Me”是一款极具人文关怀的应用，它以创造性的方式重新解读了 AI 的局限。这向我们展示了在枯燥的编码环境下，我们最终不应丢弃的是人与人之间的那份温暖。

## 参考资料

1. [Show HN: Claude and Codex rate limits as AIM away messages](https://news.ycombinator.com/item?id=49743095)
2. [Claude Code vs Codex: developers debate after - explainx.ai](https://explainx.ai/blog/claude-code-vs-codex-rate-limit-boost-2026)
3. [Show HN: Die With Me – Claude and Codex rate limits as AIM away messages](https://thenote.app/post/en/show-hn-die-with-me-claude-and-codex-rate-limits-as-aim-away-messages-gi2l22g1mq)
4. [Show HN: Die With Me – Claude and Codex rate limits as AIM away messages](https://blogviral010.blogspot.com/2026/09/show-hn-die-with-me-claude-and-codex.html)
5. [Claude Code Limits Cut 17% Sept 14 (2026 Math) - explainx.ai](https://www.explainx.ai/blog/anthropic-claude-code-limits-17-percent-cut-september-2026-august-2026)
6. [Show HN:`npx continues` – resume same session Claude, Gemini ...](https://news.ycombinator.com/item?id=47075089)
7. [Claude Code vs. Codex for Heavy Users: Limits, Costs, and ...](https://codeongrass.com/blog/claude-code-vs-codex-heavy-users-limits-costs-switching/)