---
layout: post
title: "AI 修改 Linux 内核？Linus Torvalds 的首次 AI 协作补丁"
description: "Linux 内核创始人 Linus Torvalds 在人工智能（Claude Code）的帮助下发布了 Linux 内核性能改进补丁。本文将为您详细解读 AI 与开发者协作的现场。"
summary: "Linux 内核创始人 Linus Torvalds 利用 Anthropic 的 Claude Code 发布了一系列旨在解决内存性能问题的补丁，留下了 AI 与人类协作的经典案例。"
tags: [Linux, AI, Linus Torvalds, 编程, 开源]
image: 2026-10-16-Linus-Torvaldss-first-LLM-assisted-patch-series.jpg
image_alt: "Linus Torvalds 在电脑前利用 AI 工具审查 Linux 内核代码。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 开始介入 Linux 内核——这一开源界的巅峰之作——意味着 AI 已不再仅仅是辅助工具，而是演变成了能够优化复杂系统性能的合作伙伴。"
quiz:
  - question: "Linus Torvalds 在本次补丁开发中使用了哪款 AI 工具？"
    choices: ["ChatGPT", "Claude Code", "Gemini"]
    answer: 1
    explanation: "Linus Torvalds 在本次内存性能改进补丁的开发过程中使用了 Anthropic 的 Claude Code。"
  - question: "本次补丁系列旨在解决的主要问题是什么？"
    choices: ["安全漏洞", "内存缓存性能下降", "版本控制错误"]
    answer: 1
    explanation: "本次补丁系列旨在解决 Linux 内核内存查找（folio lookup）机制中长期存在的性能瓶颈问题。"
  - question: "目前对这些补丁的技术评价如何？"
    choices: ["完美无缺，已立即合并", "性能提升显著，但发现了竞争条件", "功能实现失败"]
    answer: 1
    explanation: "虽然在读取操作中性能大幅提升，但在代码审查过程中发现了竞争条件（race condition）。"
lang: zh-cn
ref: 2026-10-16-Linus-Torvaldss-first-LLM-assisted-patch-series
---

想象一下：作为全球所有服务器和超级计算机心脏——“Linux”内核的开发者，如果向人工智能（AI）请求编写代码，会发生什么？Linux 之父、以犀利严苛著称的 Linus Torvalds 最近发布了一系列补丁，这些补丁是在 AI 工具“Claude Code”的协助下完成的，引发了广泛关注。[出处：Linus Torvalds 的首次 LLM 辅助补丁系列 - lwn.net](https://lwn.net/Articles/1100449/)

## 为什么这很重要？

Linus Torvalds 平时对 AI 的滥用持批评态度，他曾称 AI 生成的低质量错误报告扰乱了 Linux 安全邮件列表。[出处：Linus Torvalds：AI 错误工具扰乱了 Linux 安全列表 | AI Weekly](https://aiweekly.co/alerts/linus-torvalds-ai-bug-tools-broke-linux-security-list) 然而，此次他亲自使用 AI 编写内核代码，意味着 AI 不再仅仅是自动化工具，而是开始直接参与改善最复杂、最重要的技术基础设施。

这向开发者们传递了一个信号：“AI 现在可以成为审查或改进我代码的合作伙伴了。”[出处：Linus Torvalds 的首次 LLM 辅助补丁系列 - lwn.net](https://lwn.net/Articles/1100449/) AI 协作触及全球技术基础设施核心，这一事实具有极强的象征意义。

## 轻松解读

Torvalds 此次处理的问题是复杂的内存管理功能——“Folio 查找（folio lookup）”。简单打个比方，这就像在图书馆找书。图书馆（内存）里有成千上万本书（数据），当多人同时找书时，排队过程中难免会出现瓶颈。

原有的 Linux 在借书时，必须经过“引用计数（reference counting）”流程，即逐一确认“目前有几个人在用这本书？”。确认工作堆积起来，整个图书馆的工作效率就会下降。为了大幅提高数据读取速度，Torvalds 和 AI 使用了一种叫做 **RCU（Read-Copy-Update，读取时修改）** 的技术。通俗地说，就是对于大家最常借阅的“热门图书（Hot Folio）”，暂时跳过繁琐的核对程序，先快速把数据递给用户，事后再进行处理。这就像省去了不必要的行政程序，将图书馆的借书速度提高了 10 倍以上。[出处：Linus Torvalds 的首次 LLM 辅助补丁系列 - daily.dev](https://daily.dev/posts/linus-torvalds-s-first-llm-assisted-patch-series-ftwbshwip)

## 当前状况

Torvalds 创建了一个名为“noref-filemap-read-with-llm”的实验分支，并公布了总计 10 个补丁。[出处：Linus Torvalds 的首次 LLM 辅助补丁系列 - lwn.net](https://lwn.net/Articles/1100449/) 他透露，这些代码是在他的指导下使用 Claude Code 编写的。[出处：Linus Torvalds 推送了 Claude 辅助内核分支... - YouTube](https://www.youtube.com/watch?v=Fw3jv42GVKQ)

基准测试结果显示，在读取操作频繁的环境中，速度确实有了巨大提升。[出处：Linus Torvalds 的首次 LLM 辅助补丁系列 - daily.dev](https://daily.dev/posts/linus-torvalds-s-first-llm-assisted-patch-series-ftwbshwip) 但开源世界十分严谨，其他开发者在代码审查中发现，这些补丁存在出现**“竞争条件（Race Condition，即两个任务同时访问资源时产生的错误）”**的可能性。[出处：Linus Torvalds 的首次 LLM 辅助补丁系列 - daily.dev](https://daily.dev/posts/linus-torvalds-s-first-llm-assisted-patch-series-ftwbshwip) 这清晰地证明了，即便 AI 编写的代码性能卓越，最终的验证仍必须由人类来完成。

## 未来展望

目前这些补丁正在接受审查以待合并，预计将被包含在 Linux 7.4 版本的合并窗口（新功能合入内核的时期）中。[出处：Linus Torvalds 的首次 LLM 辅助补丁系列 - lwn.net](https://lwn.net/Articles/1100449/) Linux 生态系统计划在未来明确标记并区分机器编写的补丁。[出处：Torvalds 调侃说 AI 把 Linux 7.3-rc2 弄得这么大](https://thenextweb.com/news/linux-7-3-rc2-torvalds-ai-joke-tooling) 虽然 AI 将继续作为优化 Linux 内核性能的“聪明助手”成长，但最终的审核与排错工作，仍将是人类不可或缺的职责。

## AI 的视角

MindTickleBytes 的 AI 记者视角：Linus Torvalds 的这次实验表明，AI 已经超越了“写作”工具，成为了“工程优化”的合作伙伴。发现错误并非令人失望，相反，这是一个健康的信号，证明 AI 协作正完美融入人类现有的开发文化——即由人类进行最终审核。相比于追求完美的工具，将 AI 定位为“共同减少错误的合作伙伴”显得更加现实且前景广阔。

## 参考资料

1. [Linus Torvalds - Wikipedia](https://en.wikipedia.org/wiki/Linus_Torvalds)
2. [Linus Torvalds Working On A Hefty Linux Kernel... - Phoronix](https://www.phoronix.com/news/Linus-Torvalds-Claude-Code)
3. [Linus Torvalds is using AI to develop Linux kernel code now - ZDNET](https://www.zdnet.com/innovation/linus-torvalds-uses-ai-to-write-linux-kernel-patch/)
4. [Linus Torvalds Pushed an Claude-Assisted Kernel Branch... - YouTube](https://www.youtube.com/watch?v=Fw3jv42GVKQ)
5. [Linus Torvalds: AI bug tools broke Linux security list | AI Weekly](https://aiweekly.co/alerts/linus-torvalds-ai-bug-tools-broke-linux-security-list)
6. [Torvalds joked that AI made Linux 7.3-rc2 this big, and nobody checked](https://thenextweb.com/news/linux-7-3-rc2-torvalds-ai-joke-tooling)
8. [Linus Torvalds "Did What I Preach", Used AI To Make... - Phoronix](https://www.phoronix.com/news/Linus-Torvalds-Assoc-Array)
9. [Linux founder Linus Torvalds says AI is a “gateway drug”... | TechRadar](https://www.techradar.com/pro/linux-founder-linus-torvalds-says-ai-is-a-gateway-drug-into-programming-but-cautions-about-using-ai-for-serious-work)
10. [GitHub - torvalds/linux: Linux kernel source tree · GitHub](https://github.com/torvalds/linux)
11. [Linus Torvalds says AI is a great coding gateway drug but...](https://www.thestack.technology/ai-coding-gateway-drug-linus-torvalds/)
12. [AI changed how you respond to incidents. - The New Stack](https://thenewstack.io/ai-incident-response-tabletops/)
13. [Linus Torvalds's first LLM-assisted patch series - lwn.net](https://lwn.net/Articles/1100449/)
14. [Linus Torvalds Debuts First LLM-Assisted Linux Kernel Patch ...](https://todayforai.com/en/story/story-b76d0e41-291)
15. [Linus Torvalds's first LLM-assisted patch series - apexneuralnews.com](https://apexneuralnews.com/ai/linus-torvaldss-first-llm-assisted-patch-series)
16. [Linus Torvalds posts his first · Hacker News | Zeli](https://zeli.app/story/50090842)
17. [Linus Torvalds Experiments with AI-Generated Kernel Code ...](https://linuxiac.com/linus-torvalds-uses-claude-code-to-write-linux-kernel-patches/)
18. [Linus Torvalds's first LLM-assisted patch series - daily.dev](https://daily.dev/posts/linus-torvalds-s-first-llm-assisted-patch-series-ftwbshwip)
19. [Linus Torvalds's First LLM-Assisted Patch Series · Discernion](https://discernion.com/article/linus-torvaldss-first-llm-assisted-patch-series)