---
layout: post
title: "将团队编程风格直接传授给AI？通过“代理技能”实现智能协作"
description: "了解“代理技能”的概念及用法，教导Claude Code或Codex等AI编程工具掌握团队特有的编程标准与工作方式。"
summary: "代理技能是一种模块化软件包，通过向AI编程工具注入专业知识和团队级编程标准，实现工作效率的最大化。"
tags: [AI, 开发, 编程, 工作自动化, 代理]
image: 2026-08-05-Agent-skills-that-bring-team-coding-standards-to-Claude-Code-and-Codex.jpg
image_alt: "象征不同AI编程代理在统一标准下协同工作的数字图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "代理技能不仅超越了个人开发者的工具范畴，更是将整个团队的编程文化以代码为基础进行资产化的重要变革。这将成为AI从个人助手进化为团队成员不可或缺的过程。"
quiz:
  - question: "代理技能的核心特征是什么？"
    choices: ["需要对AI模型本身进行重训练", "通过标准化格式可在多个平台移植", "只能在付费服务中使用"]
    answer: 1
    explanation: "代理技能是遵循开放代理技能规范的模块化软件包，可在Claude Code、Claude API等多种环境下移植使用。"
  - question: "团队让编程代理使用技能的主要原因是什么？"
    choices: ["为了让其直接学习团队特有的编程标准和工作方式", "为了让AI自主创造新的编程语言", "为了无需编程就能创建应用程序"]
    answer: 0
    explanation: "像Codex这类工具可以通过技能学习团队的具体标准和工作流，从而引导其按照团队的方式进行工作。"
  - question: "如何查看市面上公开发布的技能？"
    choices: ["所有技能仅以非公开形式运营", "可以在GitHub等平台上搜索并审核公开技能", "必须从零开始100%重写代码"]
    answer: 1
    explanation: "可以在代理技能市场或GitHub等平台上搜索公开的技能，并在安装前直接审核源代码。"
lang: zh-cn
ref: 2026-08-05-Agent-skills-that-bring-team-coding-standards-to-Claude-Code-and-Codex
---

想象一下：一位新入职的开发人员加入了团队。但他从入职第一天起就完全掌握了团队的编程风格、变量命名规则以及复杂的审批流程。甚至连每天重复的繁琐文档工作，他也能迅速按照团队的既定格式完成。如果这位能干的新人不是“人类”，而是“AI”会怎样？

我们常用的ChatGPT或Claude等AI编程工具，起初似乎无所不能，但真正进入实际业务场景时，往往会让人感到苦恼，因为它们会写出“我们团队根本不这么写代码”的东西。这就是AI具备的通用知识与我们团队特有具体规则之间产生的鸿沟。为了解决这个问题，**代理技能（Agent Skills）**应运而生。

## 为什么这很重要？

到目前为止，我们使用的AI编程工具仅拥有所谓的“开箱即用（Out of the box）”的通用知识。 [参考资料: alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) 但在公司的实际编程场景中，每个团队都有其独特的约定。有的团队要求变量名前加特定前缀，有的团队固执地只使用特定的库组合。

代理技能的作用就是培养AI的这种“团队眼力”。通过使用代理技能，开发团队可以直接向AI注入自己专属的编程标准、独特的工作流（Workflow）以及偏好的协作方式。 [参考资料: Codex in ChatGPT | AICodingAgents for Software... | OpenAI](https://openai.com/codex/) 最终，这能让AI像团队成员一样行事，大幅减少因反复修改代码或指出风格问题而产生的沟通成本。

## 浅显易懂：给AI的“工作手册”

如果要形象地理解代理技能，可以这样类比：AI是一位以优异成绩修完基础课程的“聪明实习生”。但如果没告知这位实习生我们公司的具体内部规定或风格指南，他当然会犯错。

“代理技能”就是交给这位实习生的**“团队工作完美手册”**。该手册以模块（零件）形式存在，可以根据团队需求随时插入使用。 [参考资料: alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)

简单来说，某些技能专门负责制作幻灯片（演示文稿）。当你用自然语言请求“帮我制作本次项目的成果报告书”时，它会在约20分钟内输出一份完美草案，其中包含了我们公司使用的布局、图表风格，甚至连演讲者备注都一应俱全。 [参考资料: 20 Best Claude Skills in 2026: The List That Actually Helps](https://www.browseract.com/blog/best-claude-skills) 当然，最终的“设计润色”仍需人工完成，但AI已经完美代劳了最痛苦的“从0到1的过程”。

从技术角度看，这些技能使用了标准化的`SKILL.md`格式。 [参考资料: Top 10 Design Skills for Claude Code and Codex | Composio](https://composio.dev/content/top-design-skills) 因此，这些技能不仅适用于Claude.ai，在Claude Code、Claude API等多种环境下也具备可移植性，无论在哪都能同样运作。 [参考资料: GitHub - ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)

## 进展如何？

目前，代理技能已形成活跃的生态系统。 [参考资料: Discover Agent Skills](https://claude-plugins.dev/skills) 用户可以在市场上轻松找到已经创建好的公开技能。 [参考资料: AgentSkills Marketplace | Codex & Claude Skills | SkillsMP](https://skillsmp.com/)

最重要的一点是，所有这些技能都像“开源软件”一样共享。你可以在安装前直接审核（Inspect）源代码，确认你想要安装的技能运行原理是什么，以及它是如何处理你宝贵的代码的。 [参考资料: AgentSkills Marketplace | Codex & Claude Skills | SkillsMP](https://skillsmp.com/) 对于将安全放在首位的开发团队来说，这是非常重要的信任指标。

目前市面上已经出现了诸如从“玻璃拟态（Glassmorphism）”到极简主义等，能立即应用60多种设计风格的专用设计技能，应用范围非常广泛。 [参考资料: UI UX Pro Max Skill — Design Intelligence for Claude Code](https://ui-ux-pro-max-skill.com/)

## 未来趋势

未来的AI编程，竞争焦点将不再是“谁使用的模型更聪明”，而是“谁能更好地构建适合团队的技能”。开发人员将不再需要从头到尾亲自编写所有代码。相反，他们将集中精力将包含团队标准的代理技能组合起来，打造“团队专属的定制化AI协作工具”。

在不久的将来，与其单个安装技能，不如使用订阅式管理的“技能包”。我们使用技能时，它将自动反映最新的团队标准，这样的时代已经不远了。 [参考资料: grill-with-docs Hermes AI Agent Skill | LLMBase](https://llmbase.ai/skills/mattpocock/grill-with-docs/)

## MindTickleBytes的AI记者视角

代理技能的出现表明，AI正在从单纯的“工作工具”进化为团队的“文化资产”。当我们不再仅仅将编程标准留在文档中，而是以AI能理解的技能形式传承时，AI才真正不仅仅是助手，而是成为团队中名副其实的一员。

## 参考资料

1. [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
2. [20 Best Claude Skills in 2026: The List That Actually Helps](https://www.browseract.com/blog/best-claude-skills)
3. [AgentSkills Marketplace | Codex & Claude Skills | SkillsMP](https://skillsmp.com/)
4. [Top 10 Design Skills for Claude Code and Codex | Composio](https://composio.dev/content/top-design-skills)
5. [grill-me Hermes AI Agent Skill | LLMBase](https://llmbase.ai/skills/mattpocock/grill-me/)
6. [Discover Agent Skills](https://claude-plugins.dev/skills)
7. [HermesAgent: 10 functions that upgrade Claude Code...](https://thecode.media/hermes-agent-claude-code-codex-gemini/)
8. [GitHub - ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
9. [grill-with-docs Hermes AI Agent Skill | LLMBase](https://llmbase.ai/skills/mattpocock/grill-with-docs/)
10. [UI UX Pro Max Skill — Design Intelligence for Claude Code](https://ui-ux-pro-max-skill.com/)
11. [Codex in ChatGPT | AICodingAgents for Software... | OpenAI](https://openai.com/codex/)