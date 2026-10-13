---
layout: post
title: "AI自行修改了数十万行代码？微软耗资 1.6 亿元人民币对“Rust”进行大手术"
description: "微软利用 AI 代理将 GitHub Copilot 的底层代码完全重写为 Rust。我们来探究这项耗资 12 万美元的宏大实验的意义。"
summary: "微软利用 AI 代理成功将其 GitHub Copilot 的底层软件从 43 万行 TypeScript 代码重写为 80 多万行 Rust 代码。"
tags: [AI, GitHub, Copilot, Rust, 软件开发]
image: 2026-10-14-Microsoft-agentically-ports-Copilot-runtime-to-Rust-for-120K.jpg
image_alt: "象征着微软与 GitHub 标志交织的现代化开发环境图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这一案例表明，AI 已不再仅仅是辅助工具，而是进化成为能够独立完成复杂工程项目的核心主体。"
quiz:
  - question: "在此次微软的项目中，AI 代理承担的核心角色是什么？"
    choices: ["生成设计方案", "将现有代码转换为 Rust", "物理安装服务器基础设施"]
    answer: 1
    explanation: "AI 代理负责将 GitHub Copilot 底层的 TypeScript 代码重写为 Rust 语言。"
  - question: "为什么该项目在过去被认为是不可实现的？"
    choices: ["编程语言种类太多", "AI 代理本身不存在", "重写规模太大且过于复杂"]
    answer: 2
    explanation: "对此类大规模系统进行全面重写，对人类开发者而言难度极高且效率低下，在 AI 代理引入之前，被视为无法实现的项目。"
  - question: "此次项目的 AI 计算总成本约为多少？"
    choices: ["约 12 万美元（约 1.6 亿元人民币）", "约 5 万美元", "无成本发生"]
    answer: 0
    explanation: "微软为此次大规模代码迁移支出了约 12 万美元的计算及 Token 费用。"
lang: zh-cn
ref: 2026-10-14-Microsoft-agentically-ports-Copilot-runtime-to-Rust-for-120K
---

想象一下。你是一家巨型图书馆的管理员，需要从零开始彻底重构整个图书馆的分类系统。将数十万本书取出并按照新规则重新整理，这项工作一个人绝无可能完成。但如果同时有数千名人工智能助理管理员投入工作，并在几周内就完成了任务，会是怎样的情景？

微软（Microsoft）和 GitHub 最近就做到了类似的事情。他们将数以百万计开发者使用的 AI 工具“GitHub Copilot”的核心引擎完全更换成了另一种编程语言。

### 为什么这很重要？

“运行时（Runtime，程序运行过程中所需的环境）”这个词可能有些陌生。简单来说，可以将其理解为在背后默默支持我们日常使用的 GitHub Copilot 应用及命令行工具流畅运行的“底层引擎”。引擎的更换意味着 Copilot 将变得更快、更稳定。

最令人惊叹的是，这个项目并非由人工亲手完成，而是由能够自主思考和判断的**“自主型 AI 编码代理（Autonomous AI coding agents）”**主导的 [[출처 7](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ), [출처 9](https://www.usefulainews.com/microsoft-agentically-ports-copilot-runtime-to/)].

### 通俗理解：更换“语言”的大手术

计算机编程语言与我们使用的汉语或英语相似，只是向计算机发出指令的方式不同。此次，微软将原本使用的“TypeScript（主要用于 Web 开发的语言）”引擎更换为了“Rust”语言。

打个比方，如果说 TypeScript 是可以自由书写的“普通笔记本”，那么 Rust 就是“规则极其严格的数学公式集”。由于 Rust 极其重视代码安全性，一旦编写完成，出现错误的可能性远低于其他语言。然而，人工将数十万行代码转换成如此严格的语言，就好比一字不差地将几千页论文重写为一套新规则，是一项极其痛苦且耗时的工程。

为了执行这项任务，微软工程师雇佣了名为 **AI 代理**的聪明助手。AI 代理像经验丰富的开发者一样阅读现有代码，理解上下文，并将其转换为安全的 Rust 代码。最终，原本 43 万行的 TypeScript 代码被重写为 80 多万行的 Rust 代码 [[출처 7](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ), [출처 12](https://www.tabnews.com.br/NewsletterOficial/microsoft-reescreve-runtime-do-copilot-em-rust)].

### 现状：AI 完成的不可能任务

在过去，该项目会被归类为“不可能的计划”，甚至根本不会启动。但通过引入 AI 代理，这项宏大的迁移工作仅花费了约 3 周的开发者工时，历经 14.5 周内的 135 次更新后圆满结束 [[출처 6](https://sygentai.com/blog/2026-09-21-google-shipped-an-open-agentic-orchestrator-and-what-it-actually-takes-off-your-), [출처 7](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ)].

在此过程中，消耗了规模约为 12 万美元的 Token（AI 处理费用） [[출처 9](https://www.usefulainews.com/microsoft-agentically-ports-copilot-runtime-to/), [출처 16](https://www.linkedin.com/posts/basharatwani_migrating-the-github-copilot-runtime-to-rust-activity-7508513737730084865-vrkT)]. 虽然听起来价格不菲，但考虑到数十名人类开发者需要数月时间才能完成这种级别的大手术，AI 的效率显然非常惊人。当然，过程中确实出现过数十次错误需要修正，但最终在保证代码质量的前提下成功完成了迁移 [[출처 12](https://www.tabnews.com.br/NewsletterOficial/microsoft-reescreve-runtime-do-copilot-em-rust), [출처 16](https://www.linkedin.com/posts/basharatwani_migrating-the-github-copilot-runtime-to-rust-activity-7508513737730084865-vrkT)].

### 未来展望

这一案例是软件开发未来的强力信号。未来，我们将从“开发者亲手编写代码的时代”，迅速迈向“开发者为 AI 代理设定目标并审核结果的时代”。

微软的成功预示着，未来企业在更换旧系统至现代环境时，AI 代理将成为必备工具。当你使用的手机语音助手或办公软件某天更换了更快、更安全的底层引擎时，那背后或许就有着类似这样一场 AI 参与的大规模“园丁式”工作。

---
**MindTickleBytes 的 AI 记者视点**
AI 能够自主修改和优化代码，这不仅仅是成本问题。它意味着那些曾经因人类技术局限而被放弃的构思，如今在 AI 代理的翅膀下将成为现实。

## 参考资料
1. [MicrosoftagenticallyportsCopilotruntimetoRustfor$120K](https://www.devclass.com/devops/2026/09/19/microsoft-agentically-ports-copilot-runtime-to-rust-for-120k/5297592)
2. [Vue HN 2.0 |MicrosoftagenticallyportsCopilotruntimetoRustfor...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49763701)
3. [Unsealed Documents HighlightMicrosoftAnd OpenAI Concerns Over...](https://www.finanznachrichten.de/nachrichten-2026-09/69622107-unsealed-documents-highlight-microsoft-and-openai-concerns-over-use-of-news-content-020.htm)
4. [Microsoftand Citrix mix 'n' match fake desktops](https://www-theregister-co-uk.nproxy.org/2009/07/13/citrix_microsoft_virtual_pcs/)
5. [Rustin Visual Studio Code](https://code.visualstudio.com/docs/languages/rust)
6. [Google shipped an open agentic orchestrator, and what it actually...](https://sygentai.com/blog/2026-09-21-google-shipped-an-open-agentic-orchestrator-and-what-it-actually-takes-off-your-)
7. [AI Accelerates Code Production, Not Responsibility | LinkedIn](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ)
9. [MicrosoftAgenticallyPortsCopilotRuntimetoRust](https://www.usefulainews.com/microsoft-agentically-ports-copilot-runtime-to/)
10. [Vue HN 2.0 |MicrosoftagenticallyportsCopilotruntimetoRustfor...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49773998)
11. [Microsoftporte leruntimeCopilotversRustde façon... — Fellow](https://www.fellow.news/article/www.theregister.com-devops-2026-09-18-microsoft-agentically-ports-copilot-runtime-to-rust-for-120k-5297549)
12. [MicrosoftreescreveruntimedoCopilotemRust· NewsletterOficial](https://www.tabnews.com.br/NewsletterOficial/microsoft-reescreve-runtime-do-copilot-em-rust)
14. [MicrosoftagenticallyportsCopilotruntimetoRustfor$120K](https://modernorange.io/item/49773998)
15. [GoogleNews-Microsoft-Latest](https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFJ6ZGpRU0FtVnNLQUFQAQ?hl=en-US&gl=US&ceid=US:en)
16. [GitHub Engineers Use AI Agents toPortCodebasetoRust| LinkedIn](https://www.linkedin.com/posts/basharatwani_migrating-the-github-copilot-runtime-to-rust-activity-7508513737730084865-vrkT)
17. [MicrosoftagenticallyportsCopilotruntimetoRustfor...](https://vk.ru/wall-238001904_5872)
18. [RuStore — каталог мобильных приложений и игр для Android](https://www.rustore.ru/)