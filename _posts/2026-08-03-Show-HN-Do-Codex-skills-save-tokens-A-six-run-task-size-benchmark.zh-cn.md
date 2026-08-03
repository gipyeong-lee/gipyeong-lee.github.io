---
layout: post
title: "教 AI “如何工作”能节省 Token 吗？有趣的实验结果"
description: "关于“Codex 技能”（为 AI 助手传授特定技术）对 AI 模型 Token 使用量及效率影响的实验分析"
summary: "介绍了一项实验结果，表明为 AI 助手提供模块化的“Codex 技能”指南，可以有效提升工作效率并改善结果的一致性。"
tags: [AI, Codex, Token节省, 技术实验, MindTickleBytes]
image: 2026-08-03-Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark.jpg
image_alt: "象征 AI 助手处理复杂编码任务并优化 Token 效率的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的工作效率不仅取决于模型本身的性能，还在于提供了多么精密的‘指令结构’。Codex 技能是人类将工作方式传授给 AI 的核心媒介。"
quiz:
  - question: "Codex 技能存储的文件格式是什么？"
    choices: ["CODE.txt", "SKILL.md", "INSTRUCT.json"]
    answer: 1
    explanation: "Codex 技能通过包含元数据和指令的 SKILL.md 文件进行管理。"
  - question: "为了在项目中轻松安装 Codex 技能，通常使用什么工具？"
    choices: ["skills CLI", "npm install", "git clone"]
    answer: 0
    explanation: "使用 skills CLI 可以方便地在项目根目录安装和管理技能。"
  - question: "本文介绍的“Codex 技能”的主要目的是什么？"
    choices: ["提高 AI 的记忆力", "改善工作效率及一致性", "增加模型训练速度"]
    answer: 1
    explanation: "Codex 技能旨在指导 AI 以预期的方式执行特定任务，从而提高效率和一致性。"
lang: zh-cn
ref: 2026-08-03-Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark
---

想象一下：每次给新入职的实习生下达任务时，你都要把公司的所有规章制度写成 100 页 A4 纸交给他们。这显然效率极低。在使用 AI 助手“OpenAI Codex”（辅助编写代码的人工智能模型）时，也会出现类似的问题。如果每次让 AI 干活时都要提供极其细致的指南，那么在处理重要任务之前，光是消耗的对话数据量——即“Token”（AI 处理文本的最小单位）——就已经非常惊人了。

最近，为了解决这个问题，“教导 AI 技能（Skill）”的方式备受关注。那么，预先让 AI 学习具体的业务手册，在成本和效率方面到底会有多大差异呢？让我们通过最近进行的一项实验来揭晓答案。

## 为什么这很重要？

对于利用 AI 进行业务的企业和个人来说，“Token”就是成本。Token 使用量增加不仅会导致运营成本激增，还会限制 AI 可处理任务的复杂度和响应速度。正如在 [Codex 重置（Codex Resets）](https://codex-resets.com/) 等情况中所见，提高 Token 效率是稳定且经济地利用 AI 助手的必要任务。本次研究表明，将“如何工作”以预定义包的形式传递给 AI，可以带来实质性的成本节约和工作质量提升。

## 通俗易懂：什么是“Codex 技能”？

“Codex 技能”是教导 AI 如何执行特定任务的“模块化指令集（Modular instruction bundles）”。据 [Composio 相关文档（GitHub - composio-community/awesome-codex-skills）](https://github.com/composio-community/awesome-codex-skills) 显示，每个技能都存放在独立的文件夹中，其中包含一个名为“SKILL.md”的文件。该文件包含了技能名称、说明以及 AI 执行任务时必须遵循的分步指南。 [来源：OpenAI Codex 技能 (OpenAICodexSkills)](https://agentskill.sh/for/codex)

这可以比作照片编辑应用中的“滤镜”。未加滤镜的照片，用户必须手动调节色调、对比度和亮度。但如果应用了预先调校好的“风格滤镜”，只需按下一个按钮就能得到想要的感觉。Codex 技能也是如此。无需每次从头到尾给 AI 下指令，只需调用“代码生成”、“测试”、“调试（查找并修正程序中的错误）”等特定技能包，AI 就会像已经掌握该领域的专家一样行事。 [来源：代理技能市场 (AgentSkillsMarketplace)](https://skillsmp.com/)

## 现状：应用范围有多广？

目前，Codex 技能生态系统正在快速增长。现已开发出 34,788 个以上的技能，涵盖了代码生成、测试、调试、部署，甚至能够执行自主开发任务。 [来源：OpenAI Codex 技能 (OpenAICodexSkills)](https://agentskill.sh/for/codex)

此外，它不仅限于文本工作。例如，在 UI 设计领域，它可以与浏览器联动直接渲染画面，并根据断点（Breakpoint，根据屏幕尺寸改变布局的点）修改 UI。 [来源：Codex 设计辅助 (Codexдля дизайна)](https://open-design.ai/ru/agents/codex-design/) 这些技能可以通过“skills CLI（命令行界面工具）”简便地安装在项目根目录中，一旦安装，AI 在多个会话中都会参照这些指南。 [来源：Codex 技能 (SkillsforCodex)](https://www.skills.sh/agent/codex)

## 未来发展如何？

最近，实验正在比较在具有不同任务规模（Task-size）的环境中，“精简（Lean）技能”比传统方式能节省多少 Token。 [来源：Codex 技能 Token 节省实验 (DoCodexskillssavetokens?)](https://community.openai.com/t/do-codex-skills-save-tokens-six-controlled-gpt-5-6-sol-runs/1388837) 未来，我们将迎来一个时代：在数万个技能中组合出最适合自己任务的最佳方案，从而将 AI 助手提升到“个人秘书”的水平。目前，动画制作、网站构建、应用自动化等各种实际业务案例正在不断涌现。 [来源：2026 年十大 Codex 技能 (Top 10CodexSkillsin 2026)](https://composio.dev/content/top-codex-skills)

## MindTickleBytes AI 记者的观点

为 AI 提供精密的“技能”指令，是将 AI 从简单工具演进为真正伙伴的过程。我们教给 AI 的规则越明确，AI 就能用更少的资源创造出更大的价值。现在，我们正超越仅仅“使唤 AI”的阶段，进入让 AI “像专家一样工作”的“技能时代”。

## 参考资料

1. [Codex 技能 Token 节省实验 (DoCodexskillssavetokens?)](https://community.openai.com/t/do-codex-skills-save-tokens-six-controlled-gpt-5-6-sol-runs/1388837)
2. [Codex 重置 (Codex Resets)](https://codex-resets.com/)
3. [OpenAI Codex 技能 (OpenAICodexSkills)](https://agentskill.sh/for/codex)
4. [GitHub - composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills)
5. [2026 年十大 Codex 技能 (Top 10CodexSkillsin 2026)](https://composio.dev/content/top-codex-skills)
6. [代理技能市场 (AgentSkillsMarketplace)](https://skillsmp.com/)
7. [Codex 技能 (SkillsforCodex)](https://www.skills.sh/agent/codex)
8. [Claude 代码与 Codex 十大设计技能 (Top 10 DesignSkillsfor ClaudeCodeandCodex)](https://composio.dev/content/top-design-skills)
9. [Codex 设计辅助 (Codexдля дизайна)](https://open-design.ai/ru/agents/codex-design/)