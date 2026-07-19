---
layout: post
title: "AI仅用11天重写100万行代码？“Bun”的惊人蜕变"
description: "探索AI辅助大规模代码迁移的历史，了解JavaScript运行时Bun重构为Rust语言的过程。"
summary: "AI模型Claude仅用11天时间，就将JavaScript运行时“Bun”的100多万行代码重写为Rust语言。"
tags: [AI, Bun, Rust, Claude, 编程]
image: 2026-07-19-Claude-Code-uses-Bun-written-in-Rust-now.jpg
image_alt: "象征AI优化和重写代码的数字图形。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人类开发者需要3人一年才能完成的工作，AI仅用11天就完成了，这一事实表明软件开发的范式已经彻底改变。现在，核心竞争力不再是“写代码有多快”，而是“如何更好地利用AI”。"
quiz:
  - question: "Bun最初是用什么语言编写的？"
    choices: ["Rust", "Zig", "Python"]
    answer: 1
    explanation: "Bun最初是用Zig语言编写的，但最近利用Claude AI完成了向Rust的语言迁移。"
  - question: "这次代码重写项目花费了多少时间？"
    choices: ["11天", "11个月", "1年"]
    answer: 0
    explanation: "Bun创始人Jarred Sumner利用Claude Code，仅用11天就重写了超过100万行代码。"
  - question: "这次语言迁移到Rust带来的性能提升效果是什么？"
    choices: ["文件下载速度提升50%", "Linux环境下启动速度提升10%", "内存占用降低90%"]
    answer: 1
    explanation: "在Linux环境下，Claude Code的启动速度比以前快了10%。"
lang: zh-cn
ref: 2026-07-19-Claude-Code-uses-Bun-written-in-Rust-now
---

想象一下。假设你需要将一个拥有超过100万页书的巨大图书馆翻译成另一种语言。如果由人工完成，这可能需要数年时间，但如果能在短短11天内完成呢？最近，软件开发领域确实发生了这样令人惊叹的事情。

AI模型“Claude”将JavaScript（在Web浏览器中运行的编程语言）运行时“Bun”的核心基础，彻底重构为全新的语言——“Rust”（一种注重内存安全和性能的系统编程语言），重写的代码量超过100万行 [Source 9, Source 13]。今天，我们将深入探讨这次大规模代码转换的重要性，以及它对我们日常生活的意义。

### 为什么这很重要？

“Bun”是一个帮助开发者更快速、更高效地运行JavaScript或TypeScript代码的工具 [Source 3, Source 4]。那么，为什么要将这个重要的工具从原有语言换成Rust呢？

最大的原因是“安全”和“速度”。Rust语言能够更安全地管理计算机内存，从而减少程序意外崩溃的情况 [Source 3, Source 10]。此外，它在性能优化方面也具有优势。事实上，在这次重写之后，“Claude Code”（一种AI辅助编程工具）在Linux环境下的启动速度比以前提升了10% [Source 1, Source 7]。虽然普通用户可能很难察觉到这种细微的变化，但这在技术层面上是一个非常重要的进步。

### 通俗理解：就像更换食谱

我们可以打个比方：想象你经营着一家为数千人提供餐点的大型餐厅。起初，你们使用“Zig”这种工具精心制定了食谱。但为了更安全、更高效地配送餐点，你决定将所有食谱更换为全球厨师最信赖的“Rust”这一新工具。

在过去，这样庞大的食谱重写工作必须由人工一一完成。但这一次，一个名叫Claude的“超人AI助手”代劳了。Bun的创始人Jared Sumner设定了大约50个AI工作流，指挥Claude Code在11天内不间断地将100多万行代码迁移到了Rust [Source 12, Source 13]。如果靠人工，这可能需要3个人花费1年时间才能完成，而现在通过AI，在极短时间内就大功告成了 [Source 16]。

### 现状：AI直接管理代码的时代

目前，从Claude Code 2.1.181版本开始，已经包含并提供了这个基于Rust的新版Bun运行时 [Source 1, Source 7]。开发者们依然像往常一样编写代码，但背后运行的引擎已经换成了更安全、更快速的Rust引擎。

当然，并不是所有人都对这种大规模的AI代码修改拍手称快。也有人担心对AI生成的代码缺乏足够的审查过程 [Source 13]。然而，Anthropic（Claude的开发商）通过这个项目证明了AI能够成功处理复杂且庞大的软件项目 [Source 9, Source 16]。

### 未来会怎样？

这个案例表明，AI已经不再仅仅满足于回答问题或撰写文章，而是可以成为直接改变巨大技术基础的“工程主体” [Source 9, Source 10]。在未来，当我们使用的应用程序或服务变得更加安全和快速时，背后很可能有AI同事与人类开发者一起没日没夜地修改代码。

未来，我们将迎来由AI主导的复杂技术变革所带来的更快速、更强大的软件环境。变革已经开始，且其速度远超我们的想象。

### MindTickleBytes的AI记者视角
这次事件不仅仅是更换了一种语言。AI仅用11天就完成了人类需要1年才能完成的艰巨工作，这意味着“软件维护”的定义本身已经改变。现在，我们不应再恐惧技术变革，而应思考如何明智地驾驭AI这一工具，更快地实现我们想要的未来。

## 参考资料

1. [Claude Code uses Bun written in Rust now - simonwillison.net](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/)
2. [Claude Code uses Bun written in Rust now - daily.dev](https://daily.dev/posts/claude-code-uses-bun-written-in-rust-now-sxbybasdo)
3. [Claude Code uses Bun written in Rust now | DeepHorus](https://www.deephorus.com/blog/2026-07-19-claude-code-uses-bun-written-in-rust-now/)
4. [Claude Code uses Bun written in Rust now | AINews](https://www.ainews.tech/article/2058)
5. [Rewriting Bun in Rust | Bun Blog](https://bun.com/blog/bun-in-rust)
6. [Claude Code adopts Rust-based Bun runtime for faster startup ...](https://news.linxi.com.au/news/claude-code-shifts-to-rust-based-bun-runtime-claiming-faster-startup)
7. [Claude Code adopts Bun runtime rewritten in Rust, speed ...](https://savedelete.com/news/claude-code-bun/)
8. [Bun Rewrites in Rust: Technical Review of the Zig-to-Rust Migration | Fawad Hussain Syed](https://fawadhs.dev/blog/bun-rust-rewrite-technical-review)
9. [Claude Rewrites Bun's Million Lines of Code in 11 Days for $165,000, Setting a New Benchmark for AI-Assisted Programming — BigGo Finance](https://finance.biggo.com/news/b171d858-6390-4aef-bd0b-a651cfa942f6)
10. [Burned $160,000, Wrote 1M Lines of Code Nonstop: How Bun's Founder Rewrote the Entire JavaScript Runtime Foundation Using Claude AI](https://eu.36kr.com/en/p/3899401843017608)
11. [AI Porting: Claude Rewrites Bun Codebase in Rust | heise online](https://www.heise.de/en/news/AI-Porting-Claude-Rewrites-Bun-Codebase-in-Rust-11294318.html)
12. [How Bun's founder rewrote the codebase in Rust with Claude](https://www.thestack.technology/bun-rust-rewrite-fable-ai/)
13. [Zig creator calls Bun’s Claude Rust rewrite ‘unreviewed slop’](https://www.theregister.com/devops/2026/07/14/zig-creator-calls-buns-claude-rust-rewrite-unreviewed-slop/5270743)
15. [Why not rewrite claude-code in Rust? So, Anthropic acquires Bun team because cla... | Hacker News](https://news.ycombinator.com/item?id=48019019)
16. [One Anthropic Engineer Rewrites Bun In Rust In 11 Days With AI, Says Would've Taken 3 Engineers A Year Earlier](https://officechai.com/ai/one-anthropic-engineer-rewrites-bun-in-rust-in-11-days-with-ai-says-wouldve-taken-3-engineers-a-year-earlier/)