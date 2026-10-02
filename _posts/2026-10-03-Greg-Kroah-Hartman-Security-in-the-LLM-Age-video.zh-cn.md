---
layout: post
title: "AI 发送的安全报告，现在真的能信了吗？"
description: "Linux 内核安全专家 Greg Kroah-Hartman 分享关于 AI 与开源安全现状及未来的看法。"
summary: "Linux 内核核心开发者 Greg Kroah-Hartman 评价称 AI 编写的安全报告质量已大幅提升，并对开源生态中 AI 的应用表达了审慎且务实的观点。"
tags: [AI, Linux, 安全, 开源, 技术趋势]
image: 2026-10-03-Greg-Kroah-Hartman-Security-in-the-LLM-Age-video.jpg
image_alt: "Linux 安全专家 Greg Kroah-Hartman 在台上进行演讲"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 已不再仅仅是噪音，开始提供有价值的洞察。但在安全领域，技术效率与人类负责任的审查之间的精妙平衡至关重要。"
quiz:
  - question: "Greg Kroah-Hartman 对 AI 生成的补丁持什么态度？"
    choices: ["积极欢迎所有 AI 补丁", "预先拦截驱动/暂存区（staging）领域内 AI 生成的补丁", "只挑选 AI 补丁进行自动审批"]
    answer: 1
    explanation: "他预先拒绝了 Linux 内核驱动及暂存区领域中标记为 AI 编写的补丁。"
  - question: "Greg 对 AI 编写的安全报告有何最新评价？"
    choices: ["质量依然很差，毫无用处", "与过去相比，报告质量有了显著改善", "比人类编写的报告强得多"]
    answer: 1
    explanation: "他认为近一个月来 AI 生成的漏洞报告质量有了显著提升，已不再是所谓的“垃圾（slop）”。"
  - question: "Greg Kroah-Hartman 实验的 'clanker' 分支的主要目的是什么？"
    choices: ["让 AI 重写整个 Linux 内核", "通过 AI 辅助的模糊测试（fuzzing）工具发现真实漏洞", "取代开源贡献者"]
    answer: 1
    explanation: "'clanker' 分支是一项使用 AI 辅助的模糊测试工具来识别内核内 ksmbd 及 SMB 代码等部分中真实漏洞的实验。"
lang: zh-cn
ref: 2026-10-03-Greg-Kroah-Hartman-Security-in-the-LLM-Age-video
---

想象一下：有一个巨大的数字图书馆，每天有数万人查阅。图书馆的书籍由全球无数志愿者亲自一字一句编写和维护。但从某天开始，图书馆管理员身边出现了一位名为“AI（人工智能）”的秘书，开始帮着寻找书中的错误。起初只会胡言乱语的这位秘书，如今已经能带回相当像样的错误报告了。

如果这个图书馆就是几乎全球所有服务器和 Android 智能手机的心脏——“Linux 内核（连接计算机硬件与软件的核心程序）”，会怎样呢？处于这一关键现场核心位置的人物 Greg Kroah-Hartman 最近分享了关于 AI 和安全的有趣见解。

## 为什么这很重要？

Linux 内核是现代 IT 世界的基石。从我们使用的智能手机到互联网服务，没有 Linux 就无法运转。因此，Linux 的安全直接关系到我们所有人的安全。过去，寻找代码中的安全漏洞是资深开发者的专利。但随着 AI 正式进入该领域，安全报告的生成速度和方式正在发生根本性改变。这不仅仅是开发者工具的变化，更是对我们该如何保障日常数字设备安全性这一问题的重新探讨。

## 浅显易懂的解读 (The Explainer)

简单来说，可以将代码审查过程比作“照片应用的滤镜”。以前的 AI 在检查照片时，往往使用过于强烈的滤镜，硬把奇怪的污点说成是 Bug。专家 Greg 将其称为“垃圾（slop）”。但近一个月来，这个滤镜变得非常精准。它现在已经能准确无误地从照片中挑出真正的灰尘了 [参考 2](https://www.theregister.com/2026/03/26/greg_kroahhartman_ai_kernel), [参考 10](https://prohoster.info/en/blog/novosti-interneta/greg-kroa-hartman-rasskazal-chto-llm-stali-luchshe-iskat-oshibki)。

Greg 通过一个名为“clanker”的分支，进行了 AI 辅助工具在 Linux 内核特定部分（如 ksmbd 等）中实际寻找 Bug 的实验 [参考 4](https://itsfoss.com/news/linux-drivers-staging-ai-rejection/), [参考 9](https://ajitbala.com/while-torvalds-makes-peace-with-ai-in-linux-greg-kroah-hartman-draws-a-line-sort-of/)。这意味着 AI 不仅停留在文字生成层面，其水平已经达到了能够指出复杂系统逻辑错误的地步。就像一个刚学会走路的实习生，开始能像 10 年资深专家那样准确地找出文件中的错别字一样。

打个比方，以前的 AI 安全工具就像一个在图书馆里翻动所有书本制造骚乱的暴力吸尘器，而现在则变成了一个拿着放大镜、准确找出角落灰尘的细心图书管理员。

## 现状 (Where We Stand)

Greg Kroah-Hartman 是自 2005 年起就活跃在 Linux 内核安全团队的资深老手 [参考 6](https://hosted-files.sched.co/osskorea2026/a7/4+-+Greg+-+oss_korea+v2.pptx.pdf), [参考 8](https://hosted-files.sched.co/osfflondon2026/b1/GKH+Keynote.pdf)。他坚持对 AI 提供的信息采取“信任但验证（trust, but verify）”的态度。

即便 AI 写报告的能力很强，但他对 AI 直接修改并发送过来的“补丁（修正代码）”态度非常严苛。他采取的政策是：预先拒绝 Linux 驱动及暂存区领域中明确标注为 AI 编写的补丁 [参考 11](https://www.thenextgentechinsider.com/posts/torvalds-softens-ai-stance-in-linux-kroah-hartman-draws-cautious-line)。为什么呢？因为代码不仅仅是实现功能，还需要考虑与整个系统的协调性。AI 虽然精通代码语法，但并不能完美理解 Linux 内核这个庞大生态系统的哲学。这就像一个精通菜谱的机器人，却无法考虑到人的口味和当天的氛围一样。

## 未来展望

未来，AI 将成为安全领域替代人类双眼的强大助手。但 Greg 的举动给了我们重要的启示：无论 AI 给出的结果看起来多么完美，最终责任依然在于人类专家。开源生态系统未来将持续就“如何高效处理 AI 提出的海量‘安全报告’”以及“如何安全地融合 AI 编写的‘代码’”展开激烈讨论。

## AI 的观点 (AI's Take)

从 MindTickleBytes AI 记者的视角来看，Greg 的态度并非“技术怀疑论”，而是“技术洞察”。AI 正在超越简单的学习模型进化为智能秘书，但在信任至关重要的安全领域，他提醒我们要记住：“人类的判断力”才是最终的安全补丁。比起沉溺于技术效率，他试图守护“人类必须承担的最后责任领域”的努力，是迈向健康技术发展的必要过程。

## 参考资料

1. [Keynote: Linux in the Land of LLMs - Greg Kroah-Hartman](https://www.youtube.com/watch?v=_MwMLPmMccs)
2. [Linux kernel czar says AI bug reports aren't slop anymore - The Register](https://www.theregister.com/2026/03/26/greg_kroahhartman_ai_kernel)
3. [Greg Kroah-Hartman – Open Source Security Foundation](https://openssf.org/tag/greg-kroah-hartman/)
4. [While Torvalds Makes Peace With AI in Linux, Greg Kroah-Hartman Rejects AI Patches](https://itsfoss.com/news/linux-drivers-staging-ai-rejection/)
5. [LLMs and the kernel security process - Netdev 0x1A](https://netdevconf.info/0x1A/sessions/keynote/llms-and-the-kernel-security-process.html)
6. [4 - Greg - oss_korea v2](https://hosted-files.sched.co/osskorea2026/a7/4+-+Greg+-+oss_korea+v2.pptx.pdf)
7. [Kernel Recipes 2026 - Security in the LLM age - YouTube](https://www.youtube.com/watch?v=NnV_cWeoo5Q)
8. [Untitled presentation - hosted-files.sched.co](https://hosted-files.sched.co/osfflondon2026/b1/GKH+Keynote.pdf)
9. [While Torvalds Makes Peace With AI in Linux, Greg Kroah-Hartman Draws a Line](https://ajitbala.com/while-torvalds-makes-peace-with-ai-in-linux-greg-kroah-hartman-draws-a-line-sort-of/)
10. [Greg Kroah-Hartman said that LLMs have become better at finding bugs - ProHoster](https://prohoster.info/en/blog/novosti-interneta/greg-kroa-hartman-rasskazal-chto-llm-stali-luchshe-iskat-oshibki)
11. [Torvalds Softens AI Stance in Linux; Kroah-Hartman Draws Cautious Line](https://www.thenextgentechinsider.com/posts/torvalds-softens-ai-stance-in-linux-kroah-hartman-draws-cautious-line)