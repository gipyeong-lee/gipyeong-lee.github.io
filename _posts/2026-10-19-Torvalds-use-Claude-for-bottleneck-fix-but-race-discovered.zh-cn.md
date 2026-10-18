---
layout: post
title: "Linux创始人Linus Torvalds竟然把代码编写交给了AI？结果如何..."
description: "深入了解Linus Torvalds为提升Linux内核性能而进行的AI“Claude Code”实验，以及在此过程中发现的技术局限性。"
summary: "Linux创始人Linus Torvalds引入AI编码工具“Claude Code”以解决性能瓶颈，但在生成的代码中发现了致命的竞争状态（Race Condition）错误。"
tags: [Linux, AI, Claude Code, Linus Torvalds, 编程]
image: 2026-10-19-Torvalds-use-Claude-for-bottleneck-fix-but-race-discovered.jpg
image_alt: "Linus Torvalds在开发环境中使用AI编码工具优化Linux内核源代码"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI虽然能大幅提升开发者的生产力，但此案例再次证明，“验证”环节依然是人类不可或缺的职责。"
quiz:
  - question: "Linus Torvalds试图通过AI解决Linux内核的什么问题？"
    choices: ["修复安全漏洞", "页面缓存引用计数瓶颈", "网络速度下降"]
    answer: 1
    explanation: "Torvalds试图利用AI改善Linux内核页面缓存（page cache）的引用计数（reference-counting）瓶颈。"
  - question: "Linux内核审查人员在AI编写的代码中发现了什么问题？"
    choices: ["内存泄漏", "竞争状态（Race Condition）", "错误的库引用"]
    answer: 1
    explanation: "审查人员在代码发布仅4小时后，就发现了当多个线程同时访问资源时会出现的“竞争状态（race condition）”错误。"
  - question: "关于此次AI应用项目的结果，以下描述正确的是？"
    choices: ["生成了完美的代码并立即被合并。", "在合成基准测试中表现出色，但发现了Bug。", "AI编写的代码完全没有性能提升。"]
    answer: 1
    explanation: "虽然在合成基准测试中读取吞吐量最高提升了23倍，但由于发现了Bug，并未进行实际合并。"
lang: zh-cn
ref: 2026-10-19-Torvalds-use-Claude-for-bottleneck-fix-but-race-discovered
---

想象一下。你准备更换一个打磨了几十年的精密钟表中的一个齿轮。如果不是亲手修改，而是交给一个非常聪明的人工智能（AI）来设计，会怎样？工作速度会快得惊人，但其中是否隐藏着我们未曾预料的小瑕疵呢？

最近，全球最著名的开发者之一、Linux（计算机操作系统的核心部分）的创始人Linus Torvalds进行了一项有趣的实验。他利用Anthropic的AI编码工具“Claude Code”编写了优化Linux内核性能的代码。结果既令人惊叹，同时也真实地展现了AI与人类协作所面临的现实挑战。

## 为什么这很重要？

Linux是现代社会的核心技术，从安卓智能手机到全球超级计算机和云服务器，随处可见其身影。因此，哪怕是Linux内核极其细微的性能提升，也能让全球无数设备的运行速度同时得到改善。

此次尝试是对“AI是否能够直接修改人类所创造的最高水准的复杂系统”这一问题的挑战。这不仅停留在让AI写代码的层面，而是将优化性能的核心工作全权交给AI，这在开发者社区中引起了巨大的反响。[出处: ZDNET](https://www.zdnet.com/innovation/linus-torvalds-uses-ai-to-write-linux-kernel-patch/)

## 简单来说

此次Torvalds试图与AI共同解决的是Linux内核“页面缓存（page cache，一种将常用数据临时存储在内存中以实现高速读取的技术）”中出现的引用计数瓶颈（reference-counting bottleneck）现象。

打个比方，就像在图书馆借书时，图书管理员需要记录并确认借书人的名单。当借书人只有一两个时没问题，但当成千上万的人同时涌入时，管理员面前就会排起长队，从而产生瓶颈。在Linux系统中，当多个程序（进程）同时试图读取数据时，逐一确认是谁在使用这些数据的过程也会变慢。

Torvalds使用“Claude Code”编写了代码来跳过或优化这个确认过程。[出处: Linus Torvalds Uses Claude Code to Improve Linux Kernel](https://joho-todai.com/en/linus-torvalds-claude-code-linux-kernel-performance/) 令人惊讶的是，AI直接完成了这项工作的具体实现、编写测试代码以及相关的文档编写。[出处: Linus Torvalds let Claude Code fix the Linux page cache. Then ...](https://daily.dev/posts/linus-torvalds-let-claude-code-fix-the-linux-page-cache-then-reviewers-found-a-race--weudloreo)

## 进展如何？

实验结果相当振奋人心。在Torvalds的Threadripper（高性能计算机处理器）系统上进行的合成基准测试显示，数据读取吞吐量提升了最高23倍。[出处: The New Stack](https://thenewstack.io/torvalds-claude-code-kernel/) 即便在普通笔记本环境下，小型读取任务的速度也提高了近3倍，成果显著。[出处: HwBusters](https://hwbusters.com/news/linus-torvalds-uses-ai-to-rework-the-linux-page-cache-tripling-small-read-throughput/)

然而，乐观也仅止于此。Torvalds创建了一个名为“noref-filemap-read-with-llm”的新内核分支来分享成果，仅仅不到4小时，人类开发者就从中发现了一个致命的“竞争状态（race condition）”。[出处: Verboo.ai](https://verboo.ai/en/blog/torvalds-claude-code-kernel)

“竞争状态”简单来说，就是当多个程序同时试图修改同一数据时，执行顺序错乱导致数据损坏或系统崩溃的错误。AI生成的代码表面上看非常快且性能优越，但内部却存在着损害系统稳定性的漏洞。[出处: Linus Torvalds let Claude Code fix the Linux page cache. Then ...](https://thenewstack.io/torvalds-claude-code-kernel/)

## 未来会有什么改变？

这一事件清楚地表明，虽然AI可以成为优秀开发者的工具，但目前还无法完全替代人类严谨的验证过程。Torvalds通过此次实验确认了AI在起草初稿或解决复杂问题方面能够提供巨大帮助。

未来，在开发一线利用AI进行性能优化的尝试将会进一步增加。不过，“越是AI编写的代码，人类越需要进行更加仔细的审查”这一原则，将成为开发者社区共识。

## MindTickleBytes的AI记者视角

技术发展的速度远超我们的想象。然而，正如再精密的机器也需要每一个齿轮的配合，人类的直觉和敏锐的校验能力在AI时代依然是不可替代的核心价值。这次案例证明，虽然AI可以为我们插上翅膀，但掌握方向盘的依然是人类的双手。

## 参考资料

1. [LinusTorvaldsisusingAI to develop Linux kernel code now - ZDNET](https://www.zdnet.com/innovation/linus-torvalds-uses-ai-to-write-linux-kernel-patch/)
2. [Linus Torvalds let Claude Code fix the Linux page cache. Then ... - The New Stack](https://thenewstack.io/torvalds-claude-code-kernel/)
3. [Torvalds and Claude Code on the Linux kernel: the patch and ... - Verboo.ai](https://verboo.ai/en/blog/torvalds-claude-code-kernel)
4. [Linus Torvalds Uses Claude Code to Improve Linux Kernel ... - joho-todai.com](https://joho-todai.com/en/linus-torvalds-claude-code-linux-kernel-performance/)
5. [Linus Torvalds Uses Claude Code on a New Linux Kernel ... - blog.quadmeup.com](https://blog.quadmeup.com/2026/10/13/linus-torvalds-uses-claude-code-on-a-new-linux-kernel-performance-branch/)
6. [Linus Torvalds let Claude Code fix the Linux page cache. Then ... - daily.dev](https://daily.dev/posts/linus-torvalds-let-claude-code-fix-the-linux-page-cache-then-reviewers-found-a-race--weudloreo)
7. [Linus Torvalds Uses Claude Code to Rework the Linux Page ... - hwbusters.com](https://hwbusters.com/news/linus-torvalds-uses-claude-code-to-rework-the-linux-page-cache-tripling-small-read-throughput/)
8. [Linus Torvalds Uses Claude Code to Speed Up the Linux Kernel - krasa.ai](https://www.krasa.ai/news/linus-torvalds-claude-code-linux-kernel-page-cache-patch)