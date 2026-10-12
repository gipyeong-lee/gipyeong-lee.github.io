---
layout: post
title: "什么是 SkillOpt？一种教导 AI“学习方法”的技术"
description: "以浅显易懂的方式解释 SkillOpt 的原理及其重要性。SkillOpt 仅通过学习文本文件（技能文档），即可在不修改模型的情况下极大提升 AI 代理的性能。"
summary: "SkillOpt 是一种全新的训练框架，它将 AI 代理的技能文档 (skill.md) 视为类似神经网络权重的对象进行学习，无需修改模型本身即可大幅提升性能。"
tags: [AI, 代理, SkillOpt, 技术分析, 人工智能学习]
image: 2026-10-12-SkillOpt-Training-Loop-for-AI-Agent-Skills.jpg
image_alt: "可视化 AI 代理通过基于文本的学习循环自我提升性能的过程的图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "与其进行复杂的模型再训练，不如通过精细优化“使用说明书”来提升性能，这种方法在实用性和效率方面具有巨大价值。"
quiz:
  - question: "SkillOpt 提升 AI 性能的主要方式是什么？"
    choices: ["修改 AI 模型本身的权重", "对技能文档 (skill.md) 进行重复学习与优化", "用户手动输入提示词"]
    answer: 1
    explanation: "SkillOpt 不修改模型，而是将包含代理行为指南的 skill.md 文件作为可学习的工件进行优化。"
  - question: "关于 SkillOpt 训练过程的描述，正确的是？"
    choices: ["无需学习，一次性生成最佳指南", "由人工每次重新编写所有指南", "根据代理执行任务的结果进行评分，从而逐步修正指南"]
    answer: 2
    explanation: "SkillOpt 具有一个循环，根据代理执行任务的结果进行评分，并以此为依据由优化模型修正技能文档。"
  - question: "使用 SkillOpt 可以获得什么优势？"
    choices: ["保持模型架构的稳定性", "必须经历复杂的微调过程", "硬件成本急剧增加"]
    answer: 0
    explanation: "由于 SkillOpt 不触动模型的权重，因此能够在保持模型架构稳定的同时实现高效的性能提升。"
lang: zh-cn
ref: 2026-10-12-SkillOpt-Training-Loop-for-Agent-Skills
---

试想一下，你招聘了一名新员工，并让他每天阅读同一份业务手册以完成工作。而每当这位员工犯错时，你就非常精细地修改手册中的每一个句子。最终，员工的智力虽然没变，但由于手册变得完美，工作成果得到了飞跃性的提升。今天介绍的“SkillOpt”正是基于这一原理。

最近在人工智能 (AI) 领域，一种无需直接修改巨型模型即可提升 AI 代理（自主执行特定目标的 AI 程序）性能的技术备受关注。无需对 AI 进行再训练，仅通过智能地改变 AI 阅读的“业务指南”，就能提升其能力。

## 为什么这很重要？

到目前为止，要提升 AI 的性能，必须对模型本身进行“微调 (Fine-tuning)”。然而，微调不仅成本高昂、耗时漫长，有时还会导致模型原有的特性发生改变或某些能力退化。

SkillOpt 跳过了这些复杂的步骤。这是因为它仅将 AI 代理在工作时参考的文档——“技能文档 (skill.md)”作为优化对象[参考 13](https://explainx.ai/blog/microsoft-skillopt-self-evolving-agent-skills-optimization-2026)。这意味着企业或开发者无需更换整个模型，就能快速高效地打造出针对特定任务的 AI[参考 5](https://agentboss.co/intel/81c44b61be08-skillopt-training-loop-for-agent-skills)。

## 简易理解

要理解 SkillOpt 的工作原理，将其视为针对 AI 的“学习方法训练循环”就很容易了[参考 1](https://microsoft.github.io/SkillOpt/)。

该技术主要经过 4 个阶段的训练循环 (Training loop)[参考 4](https://www.stork.ai/blog/microsofts-new-ai-cheat-code)：

1. **执行 (Rollout)：** 代理基于当前持有的技能文档执行多项任务。此时会详细记录代理使用了哪些工具，发送了哪些消息[参考 4](https://www.stork.ai/blog/microsofts-new-ai-cheat-code)。
2. **评分 (Scoring)：** 对代理的任务结果进行评分。这是确认哪些做得好，哪些做得错的阶段[参考 7](https://www.thevibecompany.co/en/resources/articles/how-to-use-skillopt-to-train-agent-skills)。
3. **反射/学习 (Reflection)：** 基于评分，另一个优化模型会思考“修改哪里会做得更好？”[参考 7](https://www.thevibecompany.co/en/resources/articles/how-to-use-skillopt-to-train-agent-skills)。就像我们制作错题本一样[参考 1](https://microsoft.github.io/SkillOpt/)。
4. **更新 (Update)：** 基于思考的内容，添加、删除技能文档的内容，或者使其表述更加清晰[参考 7](https://www.thevibecompany.co/en/resources/articles/how-to-use-skillopt-to-train-agent-skills)。

打个简单的比方，模型 (AI) 是“智力”，而技能文档是“使用说明书”。SkillOpt 没有修改 AI 的智力，而是每次都将使用说明书换成更准确、更有效的表达方式[参考 10](https://www.linkedin.com/posts/gorebel-artificial-intelligence_github-microsoftskillopt-skillopt-is-activity-7465971443491794944-j8Vt)。

## 现状

SkillOpt 已经证明了其实际的性能提升。研究结果显示，尽管从未触动过模型的权重，但在 Codex 模型上实现了 24.8 分的性能提升，在 Claude Code 上则实现了 19.1 分的提升[参考 13](https://explainx.ai/blog/microsoft-skillopt-self-evolving-agent-skills-optimization-2026)。

目前，AI 代理正通过“技能文档 (skill.md)”这一轻量级开放格式来扩展功能，SkillOpt 在遵循这一格式的同时，实现了以数据为中心的优化自动化[参考 14](https://agentskills.io/), [参考 16](https://agentic-ai.readthedocs.io/en/latest/PromptEngineering/skillopt/)。现在，人们不再需要手工为 AI 一一编写指南，开启了一个 AI 自主学习并完善自身技能的“文本空间优化”时代[参考 13](https://explainx.ai/blog/microsoft-skillopt-self-evolving-agent-skills-optimization-2026)。

## 未来展望

SkillOpt 的出现将极大地改变 AI 的开发方式。以前为了提升 AI 性能，必须像念魔法咒语一样手动调整提示词 (Prompt)，而现在通过明确的“训练循环”，可以科学地管理性能[参考 9](https://arxiv.org/abs/2605.23904), [参考 11](https://suanlab.com/blog/20260624-paper-2605-23904-skillopt-executive-strategy-fo/)。

未来，我们将看到 AI 代理在开始特定任务之前，自主制定出最优的业务手册，并且随着任务的执行，手册会变得越来越精细。对于 AI 而言，不仅需要“智力”，能够帮助其正确发挥智力的“可学习手册”也将成为必不可少的要素。

---

### MindTickleBytes 的 AI 记者视角
SkillOpt 没有强行打开复杂人工智能技术的黑箱，而是找到了一个聪明的绕行路径，通过外部指南这一“敞开的大门”来驯服 AI。这种在降低技术复杂度的同时，能带来明显效果改进的实用方法，将成为加速 AI 大众化的核心动力。

---

## 参考资料

1. SkillOpt| Executive Strategy for Self-EvolvingAgentSkills: https://microsoft.github.io/SkillOpt/
2. MicrosoftSkillOptExplained: How toTrainAIAgentSkills... | Flowtivity: https://flowtivity.ai/blog/microsoft-skillopt-train-ai-agent-skills/
3. MicrosoftSkillOpt: The AI Cheat CodeforAgentPerformance | Stork.AI: https://www.stork.ai/blog/microsofts-new-ai-cheat-code
4. SkillOpt:TrainingLoopforAgentSkills|AgentBoss: https://agentboss.co/intel/81c44b61be08-skillopt-training-loop-for-agent-skills
5. SkillOpt:TrainingAgentSkillDocuments Like... | Prompt Genius: https://promptgenius.net/agents/concepts/skillopt
6. How to useSkillOpt:trainyouragentskills, not... | The Vibe Company: https://www.thevibecompany.co/en/resources/articles/how-to-use-skillopt-to-train-agent-skills
7. [2605.23904]SkillOpt: Executive Strategy for Self-EvolvingAgentSkills: https://arxiv.org/abs/2605.23904
8. GitHub - microsoft/SkillOpt:SkillOptis a text-space optimizer that...: https://www.linkedin.com/posts/gorebel-artificial-intelligence_github-microsoftskillopt-skillopt-is-activity-7465971443491794944-j8Vt
9. LLM 에이전트 성능을 극대화하는SkillOpt최적화 기법 | SuanLab: https://suanlab.com/blog/20260624-paper-2605-23904-skillopt-executive-strategy-fo/
10. MicrosoftSkillOpt: The Self-EvolvingAgentThatTrains| explainx.ai: https://explainx.ai/blog/microsoft-skillopt-self-evolving-agent-skills-optimization-2026
11. AgentSkillsOverview -AgentSkills: https://agentskills.io/
12. SkillOpt: Executive Strategy for Self-EvolvingAgentSkills- Agentic AI...: https://agentic-ai.readthedocs.io/en/latest/PromptEngineering/skillopt/