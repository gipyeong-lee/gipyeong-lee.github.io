---
layout: post
title: "AI 编写的代码是“垃圾”吗？编程语言 Zig 与 Anthropic 的正面冲突"
description: "通过全面禁止 AI 编写的代码的编程语言 Zig，以及因此被迫放弃 4 倍性能提升的 Anthropic 旗下 Bun 项目，探讨 AI 时代下的软件开发争议。"
summary: "编程语言 Zig 全面禁止了所有由 AI 生成的代码贡献，导致 Anthropic 收购的 Bun 项目所开发的性能提升 4 倍的代码无法合并到官方项目中。"
tags: [AI, Zig, Bun, 编程, 开源]
image: 2026-07-13-Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke.jpg
image_alt: "电脑屏幕上方编程代码与 AI 机器人图标发生碰撞的图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "开源生态系统正围绕 AI 工具的使用走向两个极端。在技术价值与开发者文化发生碰撞的交汇点，我们该建立怎样的准则？"
quiz:
  - question: "编程语言 Zig 禁止 AI 相关贡献的原因是什么？"
    choices: ["AI 生成的代码太昂贵", "AI 代码质量低下，浪费了审核时间", "出于版权问题"]
    answer: 1
    explanation: "Zig 的创始人 Andrew Kelley 认为，AI 生成的代码质量低下，除了浪费核心开发团队的审核时间外，没有实际价值。"
  - question: "Anthropic 的 Bun 项目开发的性能改进为何未能合并到 Zig 官方项目中？"
    choices: ["性能改进不足", "由于 Zig 的 AI 贡献全面禁令政策", "由于技术兼容性问题"]
    answer: 1
    explanation: "Bun 虽然实现了 4 倍的性能提升，但由于 Zig 严格的 AI 贡献禁令，该代码无法并入（upstream）官方项目。"
  - question: "Zig 的 AI 贡献禁令范围涵盖哪些内容？"
    choices: ["仅限代码", "代码、评论、Issue、Bug 报告回复等所有贡献", "仅限现有贡献者"]
    answer: 1
    explanation: "Zig 不仅禁止代码，还禁止了评论、Issue、Pull Request、Bug 追踪器回复等任何涉及 AI 参与的贡献形式。"
lang: zh-cn
ref: 2026-07-13-Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke
---

想象一下。你花了好几个月通宵达旦地打造出一套极其高效的机械装置。这套装置的运行速度比现有部件快了整整 4 倍。然而，就在你准备将它送入官方生产线时，工厂运营者冷冷地说道：“你说你在制造这套装置的过程中用了 AI 工具？那绝对不行。立刻把它丢掉。”

目前，开源编程世界正在上演这样一幕。编程语言“Zig”与 Anthropic 收购的 JavaScript 运行时“Bun”之间发生的这场冲突，为我们在 AI 辅助软件开发的时代抛出了一个非常根本的思考：当 AI 能够帮助编写软件时，我们该如何看待这种进步？

## 这为何重要？

我们日常使用的应用程序之所以越来越智能，背后是无数开发者的心血。今天，开发人员利用 AI 工具来更快、更高效地构建软件。然而，“代码是谁、怎么写出来的”与“只要技术成果好就够了”这两种立场正在激烈碰撞。如果像 Zig 的案例这样，连 AI 辅助编写的成果也被排斥，那么未来开发者在使用 AI 工具时可能会变得畏手畏脚。反之，如果没有任何验证就让 AI 代码泛滥，软件的稳定性又由谁来负责？

## 简而言之 (The Explainer)

Zig 是一种被广泛使用的高性能编程语言。而 Bun 是一个基于 Zig 构建的 JavaScript 执行环境，最近被 AI 公司 Anthropic 收购了[Source 4, Source 6, Source 18]。

打个比方，Zig 就像一家极其讲究匠人精神的“高端木工坊”。这家木工坊的负责人 Andrew Kelley 在谈及 AI 编写的代码时直言不讳，称其为“一贯的垃圾 (invariably garbage)”[Source 1, Source 5]。他认为，AI 编写的代码不仅没有实际价值，还会浪费核心开发团队宝贵的评审时间。因此，他制定了严格的政策：不仅是代码，凡是涉及 AI 参与的评论、Issue，甚至是 Bug 报告的回复，均被全面禁止[Source 1, Source 2]。

另一方面，Bun 团队积极利用 AI，取得了惊人的成果——将编译速度（将人类编写的代码转换为计算机语言的过程）提升了约 4 倍[Source 2, Source 3, Source 4]。但 Zig 设置的壁垒很高。Bun 团队原本希望将这一卓越成果并入官方项目，但由于使用了 AI 的事实必然会被拒绝，他们最终放弃了并入官方，决定将项目以独立版本（Fork，分叉）的形式进行维护[Source 2, Source 4]。

## 当前状况

目前，Zig 的立场十分坚决。只要怀疑使用了 AI，即便不去评估其技术价值也能将其拒之门外，这种原则坚持到底[Source 2]。实际上，许多开发者对这一政策反应热烈。有人对 Bun 项目的代码库和文档中充斥着“AI 垃圾 (AI slop)”感到反感，甚至出现了准备离开 Bun 的声音[Source 17]。

而 Anthropic 和 Bun 团队似乎为了追求技术优势，将继续使用 AI 工具。因为 Bun 目前正被用作 Anthropic 的“Claude Code”或“Claude Agent SDK”的基础设施[Source 16, Source 18]。可以说，追求技术成果的一方与坚持原则的一方，正各行其道，并存发展。

## 未来将如何发展？

这场争议不仅仅是一个项目的问题。“允许在多大程度上接受使用 AI 工具的贡献”已经成为所有开源项目必须回答的课题。Zig 提供了一个非常极端且明确的准则。未来，更多的项目将制定各自的“AI 贡献指南”，要么像 Zig 一样全面禁止，要么通过适当的验证流程予以接纳。开发人员现在必须生活在一个需要仔细检查自己所贡献的项目拥有何种政策的时代了。

## MindTickleBytes 的视角

“技术仅仅是工具”的观点与“技术改变了产生结果的本质”的观点正在激烈交锋。重要的或许不是使用工具本身，而是该工具对最终产品的质量和生态系统的可持续性产生了何种影响。Zig 的严苛是保护开源纯粹性的盾牌，还是在日新月异的开发趋势中自我封闭的道路，仍需拭目以待。

## 参考资料

1. [Zig bans LLM contributions, forcing Bun to fork | AI Weekly](https://aiweekly.co/alerts/zig-bans-llm-contributions-forcing-bun-to-fork)
2. [Zig Draws Hard Line On AI, Bun Chooses Fork Over Upstreaming - Open Source For You](https://www.opensourceforu.com/2026/05/zig-draws-hard-line-on-ai-bun-chooses-fork-over-upstreaming/)
3. [ZIG BANNED ANTHROPIC FROM ITS OWN LANGUAGE #Shorts - YouTube](https://www.youtube.com/shorts/sYMuqS2oyUw)
4. [Zig Reinforces LLM Contribution Ban As Anthropic-Owned Bun Forks 4x Gain](https://winbuzzer.com/2026/05/01/zig-llm-contribution-ban-bun-4x-speedup-downstream-xcxwbn/)
5. [Zig president says AI coding contributions are 'invariably garbage,' so he banned them](https://www.businessinsider.com/zig-programming-language-ai-rules-2026-5)
6. [The Zig project's rationale for their firm anti-AI contribution policy](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)
16. [Anthrophic's Bun team trials port from Zig to Rust](https://www.devclass.com/software/2026/05/11/anthrophics-bun-team-trials-port-from-zig-to-rust/5237835)
17. [This feels more like a reaction to Zig's anti-LLM policy than anything. Anthropi... | Hacker News](https://news.ycombinator.com/item?id=48017387)
18. [Bun’s Zig to Rust Rewrite: Anthropic’s AI Code Experiment | byteiota](https://byteiota.com/buns-zig-to-rust-rewrite-anthropics-ai-code-experiment/)