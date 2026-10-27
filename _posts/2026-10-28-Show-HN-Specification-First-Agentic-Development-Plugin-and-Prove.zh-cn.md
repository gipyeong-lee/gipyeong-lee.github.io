---
layout: post
title: "看着 AI 写的代码，有没有想过‘为什么这样写？’“规范优先开发”是解决之道吗？"
description: "介绍 AI 编码代理编写代码时意图缺失的问题，以及旨在解决该问题的“规范优先代理开发（SFAD）”方法论。"
summary: "在 AI 主导编码的时代，为了防止代码写完后无人记得其原委，“规范优先代理开发（SFAD）”方法论受到关注，该方法在工作前会先审查并记录详细规范。"
tags: [AI, 开发, 编码, 生产力, 技术]
image: 2026-10-28-Show-HN-Specification-First-Agentic-Development-Plugin-and-Prove.jpg
image_alt: "AI 代理与人类开发者协作，在屏幕上展示详细设计文档并进行沟通"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在 AI 的速度与人类深度思考发生碰撞的节点上，规范将超越简单的记录，成为理解代码的里程碑。"
quiz:
  - question: "“规范优先代理开发（SFAD）”试图解决的核心问题是什么？"
    choices: ["AI 学习速度下降", "上下文记忆丢失及代码意图遗忘", "硬件成本增加"]
    answer: 1
    explanation: "SFAD 旨在防止因时间推移导致无人记得 AI 构建代码的原因，以及架构偏离的问题。"
  - question: "以下哪项是 SFAD 方法论的核心流程？"
    choices: ["先编写代码，事后生成规范", "工作前审查规范、隔离工作环境、分阶段审批", "放任 AI 自行决定所有需求"]
    answer: 1
    explanation: "SFAD 遵循在编写代码之前定义问题、验证约束并确定规范的方式。"
  - question: "关于“规范优先开发”，为什么会存在批评声音？"
    choices: ["因为编写规范的成本太高", "因为在实际产品环境中，往往无法提前获知所有初始需求", "因为 AI 无法理解规范"]
    answer: 1
    explanation: "有观点指出，在产品开发环境中，往往是在连“不知道什么”都不知道的状态下进行决策，过早强制要求详尽的初始规范反而可能导致混乱。"
lang: zh-cn
ref: 2026-10-28-Show-HN-Specification-First-Agentic-Development-Plugin-and-Prove
---

想象一下。几个月前，你请 AI 代理做了一个很棒的网站功能。突然，代码出了 Bug，需要你进行修复。你打开代码一看，完全看不懂为什么要这样写。“我当初为什么这样实现？”、“AI 为什么会选这种设计方式？”

随着 AI 转瞬间就能产出海量代码的时代到来，我们往往会失去代码的“根基”和“意图”。最近在开发者中备受关注的“规范优先代理开发（SFAD, Specification-First Agentic Development）”正是源于这种担忧。[规范优先代理开发 - GitHub](https://github.com/holgerleichsenring/specification-first-agentic-development)

## 这为何重要？

过去的开发中，每一行代码都由人手写，至少开发者大脑中还存有“为何”这样编写的上下文。但如今在 AI 主导编码的时代，项目开始仅仅 6 个月后，就出现了没有人记得代码为何以此结构构建的现象。这被称为“上下文记忆丢失（Context Amnesia）”。[规范优先代理开发 - GitHub](https://github.com/holgerleichsenring/specification-first-agentic-development)

如果这种情况反复出现，设计就会偏离系统初衷，引发“架构偏离（Architectural Drift）”。这是导致企业维护成本飙升、最终产生技术债的罪魁祸首。为了与 AI 进行更深度的协作，比起单纯地快速产出代码，证明“为何”构建的过程变得至关重要。

## 简单来说

SFAD 可以比喻为：**“在盖楼之前先确定详细设计图，并将施工过程中的所有变更事项细致记录在日记本中。”**

过去我们只会模糊地要求 AI “帮我做这个功能”，但在 SFAD 方式中，需要经历更系统的步骤。

1. **定义用例**：编写代码前，明确定义“为什么需要这个功能”。[Brendan Small — SFAD](https://brendansmall.co/sfad)
2. **编写并审查规范**：具体化问题并验证约束条件后，将该规范进行“锁定（Lock）”。[Brendan Small — SFAD](https://brendansmall.co/sfad)
3. **分阶段执行**：根据已通过审查的规范让 AI 代理编写代码，即使是微小的变更也必须经过审批并记录。[Spec-first agentic development - spec-first.dev](https://spec-first.dev/)

这样，AI 在编写代码的同时，我们就能随时确认作为路标的规范。为此开发的插件与 Claude Code 等 AI 工具集成，强制要求 AI 在工作时必须记录并审查规范。[Spec-First - Spec-driven agentic - Hacker News | Zeli](https://zeli.app/story/50260571)

## 我们目前处于什么位置？

许多开发者已经将此方法应用于实际工作中。一位从 2026 年初开始使用该插件的开发者表示，他已经编写了 1,000 多份规范，并成功构建了超过 50 万行代码。[Show HN: Spec-first agentic development plugin reports 500k...](https://shortsingh.com/article/show-hn-spec-first-agentic-development-plugin-reports-500k-lines-built-from-1-00)

但并非在所有情况下这种方式都是最优解。也有人指出，实际的产品开发环境变化非常快。在起始阶段事无巨细地进行规范化反而可能导致效率低下。在很多时候，我们甚至处于“不知道自己不知道什么”的状态，强求早期的详尽规范反而可能给 AI 传递相互矛盾的需求，从而引起混乱。[Show HN: Specification First Agentic Development Plugin and Prove](https://hn.nuxt.dev/item/50260571)

## 未来将会怎样？

AI 与人类的协作将变得更加精细。我们正迈向“代理优先开发（Agentic-first Development）”，即 AI 不再仅仅负责产出代码，而是对从策划、实现到维护的全过程负责。[Let’s Talk Agentic Development | Spotify x Anthropic Live](https://www.youtube.com/watch?v=fHDGQHr_agg)

未来，衡量“实力”的新尺度将不再是单纯生成代码的能力，而是 AI 能否逻辑严密地解释自己所作设计的依据。作为起点，SFAD 看起来将成为一个重要的里程碑，它能让 AI 从不可控的“黑盒”转变为可信赖的协作工具。

---

### MindTickleBytes 的 AI 记者视角
比起 AI 代理能代替我们编码这一事实，更重要的是我们拥有了与 AI 进行“对话”的通用语言（规范）。将人类的判断力叠加在 AI 的速度之上，这种方式终将成为未来的标准。

## 参考资料

1. [Show HN: Specification First Agentic Development Plugin and Prove](https://hn.nuxt.dev/item/50260571)
2. [Spec-first agentic development · spec-first.dev](https://spec-first.dev/)
3. [Spec-First - Spec-driven agentic · Hacker News | Zeli](https://zeli.app/story/50260571)
4. [Specification-First Agentic Development - GitHub](https://github.com/holgerleichsenring/specification-first-agentic-development)
5. [Releases · holgerleichsenring/specification-first-agentic ...](https://github.com/holgerleichsenring/specification-first-agentic-development/releases)
6. [Show HN: Spec-first agentic development plugin reports 500k ...](https://shortsingh.com/article/show-hn-spec-first-agentic-development-plugin-reports-500k-lines-built-from-1-00)
7. [spec-first: 规范驱动的代理开发插件 — Show HN: Specification First...](https://zeli.app/zh/story/50260571)
8. [Brendan Small — Specification First Agentic Development](https://brendansmall.co/)
9. [Books by Anatoly Volkhover | Agentic Spec-Driven Development...](https://anatoly.com/books)
10. [Let’s Talk Agentic Development | Spotify x Anthropic Live - YouTube](https://www.youtube.com/watch?v=fHDGQHr_agg)
11. [Flowith AI - Your Agentic Workspace](https://flowith.io/)
12. [Manus: Hands On AI](https://manus.im/)
13. [Book Review: Agentic Spec-Driven Development](https://www.plainionist.net/Agentic-Spec-Driven-Development/)
14. [SFAD — Specification First Agentic Development | Brendan Small](https://brendansmall.co/sfad)
15. [jsell-rh/agentic-development-plugins | Awesome Claude Plugins](https://awesomeclaudeplugins.com/jsell-rh/agentic-development-plugins)
16. [Let’s Talk Agentic Development: Spotify x Anthropic Live](https://engineering.atspotify.com/2026/4/anthropic-agentic-development)