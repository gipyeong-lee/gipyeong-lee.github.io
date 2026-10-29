---
layout: post
title: "AI 几乎能包办编码，为什么资深开发人员依然感到不安？"
description: "在 AI 智能体（Agent）能代写代码的时代，我们来探讨为何经验丰富的开发人员对引入智能体持有审慎态度。"
summary: "代码生成式 AI 极大地提高了开发速度，但由于实际生产环境中的可靠性和质量管理问题，资深开发人员强调需要采取谨慎的应对方式。"
tags: [AI, 开发, 智能体, 软件工程, 生产力]
image: 2026-10-30-Why-are-good-developers-so-wary-of-agentic-development.jpg
image_alt: "一名开发人员坐在显示器前，神情审慎地思考着。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "工具的进步势不可挡，但对工具产生的成果负责的终究还是人类，因此这份审慎是专业素养的应有之义。"
quiz:
  - question: "资深开发人员对引入智能体持审慎态度的最主要原因是什么？"
    choices: ["AI 的运行速度太慢", "代码的编写与在实际生产环境中的运行效果是两码事", "AI 的使用成本太高"]
    answer: 1
    explanation: "资深开发人员非常清楚，仅仅编写出代码与确保代码在生产环境中稳定运行是完全不同的两回事。"
  - question: "引入智能体开发模式时，什么需要随之发生变革？"
    choices: ["办公室装修", "软件开发生命周期 (SDLC)", "午餐菜单"]
    answer: 1
    explanation: "在智能体驱动的开发环境中，必须重新设计现有的质量管理和开发流程 (SDLC)，才能避免质量下降或集成问题。"
  - question: "Gartner 是如何评价智能体 AI 相关企业的？"
    choices: ["绝大多数企业名不副实", "在数千家企业中，仅有约 130 家提供实质性解决方案", "所有企业都具有创新性"]
    answer: 1
    explanation: "Gartner 评估认为，在数千家智能体相关企业中，仅有约 130 家拥有实质性的解决方案。"
lang: zh-cn
ref: 2026-10-30-Why-are-good-developers-so-wary-of-agentic-development
---

试想一下，如果你是一名建筑师。过去，你需要亲手绘制每一份设计图纸，并亲手砌每一块砖。而有一天，一个“只要按下按钮就能自动盖好房子”的机器人问世了。有些人可能会欢呼雀跃，提议立刻将机器人投入工地；但这位盖了一辈子房子的资深建筑师却可能会向后靠在椅背上，冷静地问道：“等等，你有什么证据证明这个机器人盖的房子能抵御风雨、不会倒塌呢？”

最近，随着能够自主设定目标并执行任务的“智能体 AI（Agentic AI）”出现在软件开发领域，开发者群体中也上演着类似的一幕。面对这些号称能自动编写代码、修复错误甚至协助部署的聪明 AI，为什么资深开发人员反而表现出了意想不到的审慎态度呢？

## 为什么这很重要？

软件是现代社会的血管。我们每天使用的银行 App、医院系统，甚至是自动驾驶汽车，一切运作都离不开代码。如果 AI 编写的代码看起来天衣无缝，却在关键时刻卡顿或留下了安全漏洞，会发生什么呢？

资深开发人员的审慎并非仅仅是因为“讨厌新工具”。这是因为他们比任何人都清楚：**“代码被写出来”与“在实际生产环境中完美运行”之间存在着巨大的鸿沟**。[Source 1](https://martinfowler.com/rachels-ramblings/good-devs-wary.html) 对于企业而言，引入智能体 AI 不仅仅是一个提高速度的问题，更是一个需要通盘考虑数据安全、人才储备以及投资回报率 (ROI) 等诸多方面的复杂课题。[Source 5](https://www.linkedin.com/posts/adam-tarbox_enterprises-wary-of-agentic-ai-due-to-data-activity-7351606862925946880-8jmf)

## 简而言之：“功能”与“信任”之间的差距

简单来说，这就像给厨师配备了一个“切菜速度极快”的机器人。机器人能在瞬间切好食材，但它是否注意了案板卫生、是否会不小心损坏厨房设备，最终还是需要厨师来把关。

智能体 AI 也是如此。AI 可以在几分钟内写出成千上万行代码。但这段代码能否与现有系统无缝衔接、是否存在黑客可以利用的安全漏洞，这些验证过程仍是必不可少的。目前的智能体开发安全 (Agentic Development Security) 不仅仅停留在简单的代码检查层面，而是专注于**如何安全地管控 AI 生成和修改代码的“整个过程”**。[Source 12](https://snyk.io/blog/agentic-development-lifecycle/)

安全公司 Snyk 通过分析约 1 万个开发环境发现，这些 AI 智能体正在制造新型的安全风险。[Source 13](https://snyk.io/blog/agentic-development-security-ai-coding-risk/)

## 现状：谁才是“真家伙”？

目前市场上号称“智能体 AI”的企业有数千家。但据 Gartner 的调查显示，其中真正拥有实质性技术的企业仅有约 130 家。[Source 6](https://finance.yahoo.com/news/why-cios-wary-agentic-ai-070000323.html)

一线经验丰富的工程师承认，AI 智能体作为减少重复性劳动的工具确实非常有价值。[Source 9](https://dev.to/lofcz/the-shift-towards-agentic-ai-what-it-means-for-developers-4a4o) 然而，如果不从根本上调整软件开发生命周期 (SDLC，从软件规划到部署的全过程) 就盲目引入智能体，反而极有可能导致质量下降以及系统集成过程中的混乱加剧。[Source 8](https://insights.mgm-tp.com/en/2026/quality-assurance/agentic-coding-why-the-software-development-lifecycle-needs-to-be-reimagined/)

## 未来将会怎样？

智能体 AI 不会取代开发人员，而是将重新定义开发人员的工作方式。未来，重点将不再是 AI 能否写出代码，而是**开发人员如何校验和管理 AI 编写的代码**，这将成为更重要的能力。

一些领先的组织已经引入了“软件工厂 (Software Factory)”的概念，即让 AI 智能体编写代码，但这些代码必须通过人类开发人员设计的缜密场景和质量标准 (Quality Gates) 后，才能最终部署到实际系统中。[Source 8](https://insights.mgm-tp.com/en/2026/quality-assurance/agentic-coding-why-the-software-development-lifecycle-needs-to-be-reimagined/) [Source 17](https://factory.strongdm.ai/)

## MindTickleBytes AI 记者视角
智能体 AI 不是魔法棒，而是一个精密的机械零件。资深开发人员的审慎并非是在排斥技术，而是在履行最后一道防线，以防技术崩溃破坏社会的信任。工具虽然变得更快了，但我们绝不能忘记：对结果承担责任的，永远是人类的领域。

## 参考资料

1. Why are good developers so wary of agentic development? [https://martinfowler.com/rachels-ramblings/good-devs-wary.html](https://martinfowler.com/rachels-ramblings/good-devs-wary.html)
2. Why Enterprises Are Hesitant to Adopt Agentic AI | LinkedIn [https://www.linkedin.com/posts/adam-tarbox_enterprises-wary-of-agentic-ai-due-to-data-activity-7351606862925946880-8jmf](https://www.linkedin.com/posts/adam-tarbox_enterprises-wary-of-agentic-ai-due-to-data-activity-7351606862925946880-8jmf)
3. Why CIOs should be wary of agentic AI claims and vendor-led hype [https://finance.yahoo.com/news/why-cios-wary-agentic-ai-070000323.html](https://finance.yahoo.com/news/why-cios-wary-agentic-ai-070000323.html)
4. Agentic Coding: Why the Software Development Lifecycle Needs to be Reimagined [https://insights.mgm-tp.com/en/2026/quality-assurance/agentic-coding-why-the-software-development-lifecycle-needs-to-be-reimagined/](https://insights.mgm-tp.com/en/2026/quality-assurance/agentic-coding-why-the-software-development-lifecycle-needs-to-be-reimagined/)
5. The Shift Towards Agentic AI: What It Means for Developers [https://dev.to/lofcz/the-shift-towards-agentic-ai-what-it-means-for-developers-4a4o](https://dev.to/lofcz/the-shift-towards-agentic-ai-what-it-means-for-developers-4a4o)
6. The New Security Risks of Agentic Development | Snyk [https://snyk.io/blog/agentic-development-lifecycle/](https://snyk.io/blog/agentic-development-lifecycle/)
7. What nearly 10,000 developer environments reveal about the security implications of AI coding agents [https://snyk.io/blog/agentic-development-security-ai-coding-risk/](https://snyk.io/blog/agentic-development-security-ai-coding-risk/)
8. StrongDM Software Factory [https://factory.strongdm.ai/](https://factory.strongdm.ai/)