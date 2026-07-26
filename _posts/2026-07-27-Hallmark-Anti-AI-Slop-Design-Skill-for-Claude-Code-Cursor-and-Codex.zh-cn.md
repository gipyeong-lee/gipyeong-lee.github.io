---
layout: post
title: "为什么AI做的网站看起来都一样？用“Hallmark”修正AI的习惯"
description: "AI编程工具生成的网页设计千篇一律，如何打破这种局限？为您介绍开源设计技能“Hallmark”。"
summary: "Hallmark 是一个开源设计技能，旨在帮助AI生成的网页设计摆脱特有的“AI味”，使其看起来更具独创性和专业感。"
tags: [AI, 设计, 编程, Hallmark, 设计技能]
image: 2026-07-27-Hallmark-Anti-AI-Slop-Design-Skill-for-Claude-Code-Cursor-and-Codex.jpg
image_alt: "屏幕上展示着多种具有不同结构和色彩的现代UI设计。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "拒绝AI的“默认选项”是找回人类创意必不可少的过程。Hallmark的迷人之处在于，它不仅让技术模仿人类的美学，更是强制要求技术表现出独特的个性。"
quiz:
  - question: "Hallmark设计技能主要起什么作用？"
    choices: ["提高AI生成的代码速度", "消除AI生成的UI设计中那种“AI味”（slop）", "引导用户亲自编写代码"]
    answer: 1
    explanation: "Hallmark是一种设计技能，它通过应用结构和样式规则，防止AI编程工具生成的UI看起来像模版一样千篇一律。"
  - question: "如何为AI编程工具安装Hallmark？"
    choices: ["需要复杂的服务器配置", "使用单条命令即可轻松安装", "作为网页浏览器扩展程序安装"]
    answer: 1
    explanation: "Hallmark可以通过诸如“npx skills add”之类的单条命令，安装到Claude Code、Cursor、Codex等工具中。"
  - question: "代码在最终交付给开发者之前，Hallmark会让其经历什么？"
    choices: ["自动翻译过程", "约57至65个“防烂作（slop）测试”关卡", "数据加密过程"]
    answer: 1
    explanation: "Hallmark不会直接展示AI生成的代码，而是使其通过数十个测试关卡，以验证其是否符合设计规则并具备独创性。"
lang: zh-cn
ref: 2026-07-27-Hallmark-Anti-AI-Slop-Design-Skill-for-Claude-Code-Cursor-and-Codex
---

想象一下：你要求AI“为我的业务制作一个简洁的网站”。片刻后，网站完成了，但你总觉得它和你上周看到的其他AI生成的网站没什么区别，除了颜色不同，结构如出一辙。这种像工厂流水线生产出来的感觉，在设计界被称为**“AI烂作（AI-slop）”**。这正是因为AI拥有一种“平均主义的设计习惯”而导致的。

最近，一个聪明的工具应运而生，解决了这一难题。它就是由 Together AI 开发的开源设计技能——**Hallmark**。

## 为什么这很重要？

像 Claude Code、Cursor 和 Codex 这样的 AI 编程工具虽然极大地提高了开发效率，但却存在一个顽疾：人工智能模型在学习过程中，往往倾向于导出最常见数据的“平均值”。这就导致AI制作出的用户界面（UI）大多具有极其相似的结构和乏味的布局。

Hallmark 阻断了这种“AI的懒惰”。即使开发者没有亲自手动修改设计，Hallmark 也能在AI编写代码的阶段，强制应用专业的设计规则。这意味着，你得到的不再是模版式的作品，而是看起来像经过人类深思熟虑、充满独创性的成果。

## 直观理解：专为AI准备的“设计检查站”

理解 Hallmark 最简单的方法是把它比作一位坐在AI身边的**“严苛设计批评家”**。Hallmark 通过以下流程来打磨AI的设计：

1. **拒绝（Refuse）**：Hallmark 会果断拒绝那些AI因缺乏思考而默认选择的常见结构。
2. **应用（Apply）**：作为替代，Hallmark 会将关于排版（字体）、色彩、布局、动效以及微交互（细微动态）的精致规则融入代码中 [Source 5](https://www.everydev.ai/tools/hallmark), [Source 15](https://mer.vin/2026/05/hallmark-design-skill-anti-slop-ui-for-claude-code-and-cursor/), [Source 18](https://github.com/adeoyewole028/hallmark-design-skills)。
3. **测试（Test）**：Hallmark 的核心在于“防烂作测试（Slop-test）”关卡。在生成的代码最终交付给开发者之前，Hallmark 会让其通过约57至65个检查关卡 [Source 10](https://dailyaiworld.com/blogs/hallmark-design-skill-anti-slop-2026), [Source 11](https://agentconn.com/skills/hallmark/), [Source 12](https://explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026), [Source 16](https://www.explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026)。

这个过程就像给照片应用滤镜：AI草草画出的底图，经过 Hallmark 这一滤镜的精细润色和结构调整，瞬间变身为完成度极高的作品。

## 现状

目前，Hallmark 可以通过单条命令轻松安装到 Claude Code、Cursor 和 Codex 等主流AI编程工具中 [Source 5](https://www.everydev.ai/tools/hallmark), [Source 19](https://gittrend.io/repo/Nutlope/hallmark)。

该工具不仅能更改主题，还提供了20到22种结构化主题。开发者还可以使用 `hallmark audit` 命令，自行检查现有的代码是否含有“AI烂作”模式 [Source 1](https://github.com/Nutlope/hallmark), [Source 2](https://hallmark.apposters.com/), [Source 10](https://dailyaiworld.com/blogs/hallmark-design-skill-anti-slop-2026), [Source 18](https://github.com/adeoyewole028/hallmark-design-skills)。截至2026年7月，它已获得超过17,700个 GitHub Star，受到了开发者的广泛关注 [Source 19](https://gittrend.io/repo/Nutlope/hallmark)。

## 未来展望

未来，“懂设计感的AI”将取代单纯的“会写代码的AI”成为标准。Hallmark 通过将设计规则编码，迈出了改变AI习惯的第一步 [Source 12](https://explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026), [Source 16](https://www.explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026)。我们期待未来能开发出更多这样的设计技能，让所有AI服务不再是“复制粘贴”的网站，而是充满个性化的空间。

## AI的视角

虽然要求AI具备创造力很难，但教导它“什么不该做”是可行的。Hallmark 的迷人之处在于，它不仅让技术模仿人类的美学，更是强制要求技术表现出独特的个性。拒绝AI的“默认选项”，将成为找回人类创意必不可少的过程。

## 参考资料

1. Nutlope/hallmark: Anti-AI-slop design skill for Claude Code, Cursor... (https://github.com/Nutlope/hallmark)
2. Hallmark - Anti-AI Design Skill for Claude Code, Cursor, and Codex (https://hallmark.apposters.com/)
3. Hallmark: Anti-AI Slop Design for Claude, Cursor, Codex | LinkedIn (https://www.linkedin.com/posts/arkadiy-sotnikov_github-nutlopehallmark-anti-ai-slop-design-activity-7483500613071167489-_zmV)
4. Hallmark: Anti-AI-slop design skill for Claude Code, Cursor, and... (https://addrom.com/hallmark-anti-ai-slop-design-skill-for-claude-code-cursor-and-codex/)
5. Hallmark - AI Design Rules for Coding Agents | EveryDev.ai (https://www.everydev.ai/tools/hallmark)
6. Hallmark | Analog (https://analoghq.ai/nutlope/skills/hallmark)
7. Hallmark + Claude Code, Codex: The BEST DESIGN SKILL YET! (https://www.youtube.com/watch?v=dVGJ3DE1MzA)
8. GitHub - Nutlope/hallmark: Anti-AI-slop design skill for Claude Code, Cursor, and Codex. · GitHub (https://github.com/Nutlope/hallmark)
9. hallmark/skills/hallmark at main · Nutlope/hallmark (https://github.com/Nutlope/hallmark/tree/main/skills/hallmark)
10. Hallmark Design Skill: Kill AI-Generated UI with Structural ... (https://dailyaiworld.com/blogs/hallmark-design-skill-anti-slop-2026)
11. Hallmark - AI Agent Skill | AgentConn (https://agentconn.com/skills/hallmark/)
12. Hallmark Design Skill: Anti-AI-Slop UI for Agents (2026) (https://explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026)
13. Hallmark: Anti-AI-Slop Techniques for Claude Code and Cursor | AIToolly (https://aitoolly.com/ai-news/article/2026-07-15-hallmark-new-anti-ai-slop-design-techniques-for-claude-code-cursor-and-codex-developers)
14. Hallmark: Rejecting AI-Slop in Claude Code and Cursor | AIToolly (https://aitoolly.com/ai-news/article/2026-07-16-hallmark-a-new-design-skill-to-eliminate-ai-slop-in-claude-code-and-cursor)
15. Hallmark Design Skill: Anti-AI-Slop UI for Claude Code and ... (https://mer.vin/2026/05/hallmark-design-skill-anti-slop-ui-for-claude-code-and-cursor/)
16. Hallmark Design Skill: Anti-AI-Slop UI for Agents (2026 ... (https://www.explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026)
17. Hallmark Guide: Anti-AI-Slop Design for Claude Code, Curs... (https://opentools.ai/resources/hallmark)
18. GitHub - adeoyewole028/hallmark-design-skills: Anti-AI-slop ... (https://github.com/adeoyewole028/hallmark-design-skills)
19. hallmark — Anti-AI-slop design skill for Claude ... | GitTrend (https://gittrend.io/repo/Nutlope/hallmark)