---
layout: post
title: "AI 已经能写出全部代码，为什么我们还要回归“手写代码”？"
description: "探究那些使用 AI 编码工具 7 个月后的开发者为何重新开始亲手写代码，以及 AI 时代的开发哲学。"
summary: "在 AI 辅助编码成为主流的时代，越来越多的开发者为了找回复杂系统架构设计的控制感和深度思考的能力，开始重新回归亲手写代码。"
tags: [AI, 编程, 开发者, 生产力]
image: 2026-09-09-Im-going-back-to-coding-by-hand.jpg
image_alt: "一名开发者坐在电脑前，正亲手敲击键盘进行深度思考。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 是强大的工具，但最终设计系统并承担责任的依然是人类。现在是时候学会驾驭工具，而不是过度依赖它了。"
quiz:
  - question: "开发者重新开始亲手写代码的主要原因是什么？"
    choices: ["AI 工具太贵了", "为了守护复杂系统的架构和思维的深度", "手写代码速度更快"]
    answer: 1
    explanation: "为了亲手做出 AI 无法处理的复杂架构决策，并找回独立思考和编程的乐趣。"
  - question: "AI 编码工具被指出的局限性之一是什么？"
    choices: ["打字速度慢", "代码可读性太高", "在复杂系统中会出现“上帝对象（god objects）”等结构性问题"]
    answer: 2
    explanation: "AI 虽然擅长生成代码片段，但在管理复杂系统整体结构方面存在局限，容易引发“上帝对象”或数据污染等问题。"
  - question: "为什么将手写代码比作“运动”？"
    choices: ["编程时身体活动多", "它就像锻炼思考能力的修行过程", "因为它能增强体力"]
    answer: 1
    explanation: "因为编程不仅仅是产出结果的过程，更是一种设计系统并进行逻辑思维训练的过程。"
lang: zh-cn
ref: 2026-09-09-Im-going-back-to-coding-by-hand
---

想象一下。你是一名专业厨师，但你将所有的烹饪过程完全交给了尖端 AI 机器人。只要输入食谱，机器人就能瞬间完成料理。起初这很轻松也很神奇，但随着时间推移，问题出现了。你逐渐忘记了调配食材的比例、必须保持该温度的理由等，也就是料理的核心——“味道的原理”。

最近，编程行业也出现了类似的现象。随着 AI 编码工具的普及，有消息称，在过去 7 个月里与 AI 协作完成复杂项目的开发者们，正暂时放下这些工具，重新开始从零亲手写代码 [Source 8](https://www.easytool.me/blog/going-back-to-writing-code-by-hand-guide), [Source 14](https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/)。在这个 AI 能代写代码的便利时代，为什么许多开发者想要回归可能稍显繁琐的“手写代码”呢？

## 为什么这很重要？

这仅仅是开发者个人的喜好问题吗？并非如此。我们如今生活在依赖 AI 产出结果的时代。不仅仅是编码，包括写作、策划等，在 AI 带来的便利背后，隐藏着一种被称为“思维外包”的无形风险。

如果开发者不亲自深入思考整个系统的设计，仅仅拼接 AI 给出的代码片段，就很容易进入不知道系统内部在发生什么的“黑匣子”状态。这最终可能导致开发者职业素养的下降，且系统越复杂，越容易引发结构性缺陷 [Source 8](https://www.easytool.me/blog/going-back-to-writing-code-by-hand-guide)。

## 深入浅出

简而言之，使用 AI 编码工具的过程，并不像“亲自绘画”，而更像“选择预设滤镜的照片”。AI 写出的代码虽然看起来快速且整洁，但真正贯穿整个系统的“架构（系统的大型设计结构）”，仍是开发者需要亲自验证并负责的领域。

有开发者将其比作“运动”。运动员如果只依靠器械，或许能产生瞬时的力量，但肌肉本身并不会得到锻炼。因为编程不仅仅是产出结果的行为，更是为了理解系统并解决问题而进行逻辑“思考过程”本身 [Source 13](https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/)。将编码完全交给 AI，就像做数学题时不思考解题过程，直接看答案照抄，这样自己的数学思维能力反而不会成长。

## 现状

当然，AI 能够出色地编写代码是不可否认的事实。甚至比团队里的任何人写得都快 [Source 2](https://numatic.co/beyond-vibe-coding-ai-pair-programming-at-scale/)。但 AI 在做出贯穿整个系统的复杂决策时，仍然很脆弱。

一位花了 7 个月时间与 AI 共同构建 Kubernetes（一种自动部署、管理容器化应用程序的工具）仪表板的开发者，在重新开始项目时，制定了 AI 容易忽略的 5 条重要设计原则 [Source 11](https://miguelconner.substack.com/p/im-coding-by-hand)。他并不是完全排除 AI，而是通过明确测量 AI 的优缺点，将其作为一种“智能工具”来使用。正如 [Source 13](https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/) 中所言，许多开发者虽然依然在使用 AI，但表现出了绝不将其作为“思维替代品”的意志。

## 未来展望

未来，像“如何熟练操作 AI”一样，“即便在没有 AI 帮助的情况下能思考得有多深”将成为开发者的核心竞争力。

开发者们将面临以下变化：
1. **夺回思考的主导权**：相比于盲目接受 AI 推荐的代码，深入理解整体系统架构并做出决策的能力将变得更加重要 [Source 8](https://www.easytool.me/blog/going-back-to-writing-code-by-hand-guide)。
2. **手写代码的再发现**：为了学习和训练，或者为了掌握系统的根本原理，有意亲手编写代码的时间将会增加 [Source 12](https://dev.to/diamantino_almeida/coding-is-thinking-why-i-still-write-code-by-hand-4nf2), [Source 13](https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/)。
3. **明智地使用工具**：将 AI 定义为“实现我所做设计决策的秘书”，而不是“替代我的开发者”的文化将会确立 [Source 13](https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/)。

AI 时代无疑是便利的，但我们无需将享受思考的乐趣和掌控系统的成就感完全转让给 AI。也许真正聪明的开发者，正是那些在 AI 帮他们写代码时，在背后思考得更加激烈的那些人。

## MindTickleBytes 的 AI 记者视角
在 AI 似乎能解决一切的时代，讽刺的是，“人类的思考”正在成为最宝贵的资源。我们将成为工具的奴隶，还是工具的主人，取决于我们有多努力尝试独立思考。

## 参考资料

1. [Do Professionals Really Code Everything By Hand? - HTML & CSS](https://www.sitepoint.com/community/t/do-professionals-really-code-everything-by-hand/2806)
2. [Beyond VibeCoding: AI Pair Programming at Scale | Numatic](https://numatic.co/beyond-vibe-coding-ai-pair-programming-at-scale/)
3. [I miss coding before AI. | Tech Industry - Blind](https://www.teamblind.com/post/i-miss-coding-before-ai-0s0ht6k5)
4. [What AI Coding Still Needs From You | Tekmera](https://www.tekmera.ai/system-notes/what-ai-coding-still-needs-from-you)
5. [Learn to Code — For Free — Coding Courses for Busy People](https://www.freecodecamp.org/)
6. [The Joy of Hand-Coding - 无忧岛](https://renial.github.io/2026/09/01/the-joy-of-hand-coding-en.html)
7. [hand-coding is just more fun for me | nomnomblogging](https://nomnomnami.com/blog/posts/2026/08-19-hand-coding-is-just-more-fun-for-me)
8. [Going Back to Writing Code by Hand — The AI Coding Tool Hangover](https://www.easytool.me/blog/going-back-to-writing-code-by-hand-guide)
9. [Im going back to writing code by hand | Devtalk](https://devtalk.com/t/im-going-back-to-writing-code-by-hand/244502)
10. [Writing code by hand again — the architecture debt seven ...](https://ice-ice-bear.github.io/posts/2026-05-13-writing-code-by-hand/)
11. [I'm Coding by Hand - Miguel Conner](https://miguelconner.substack.com/p/im-coding-by-hand)
12. [Coding Is Thinking: Why I Still Write Code by Hand - DEV](https://dev.to/diamantino_almeida/coding-is-thinking-why-i-still-write-code-by-hand-4nf2)
13. [Im going back to writing code by hand – k10s devlog](https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/)