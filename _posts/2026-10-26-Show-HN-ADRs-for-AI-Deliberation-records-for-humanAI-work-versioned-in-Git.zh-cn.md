---
layout: post
title: "与AI的对话，关闭聊天窗口后就消失了吗？介绍AI协作记录法 'ADRs4AI'"
description: "介绍一种名为ADRs4AI的工具与方法论，它能记录并版本化管理您与AI进行项目协作时的关键决策，确保讨论成果不被丢失。"
summary: "深入了解“ADRs4AI”技术，通过将与AI协作的决策事项与代码一同记录在Git中，让任何人都能在任何时候无缝接续AI的讨论进程。"
tags: [AI, 协作, Git, 开发者工具, 生产力]
image: 2026-10-26-Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git.jpg
image_alt: "象征着代码与对话记录在Git仓库中系统性累积的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "将AI的推理过程从短暂的聊天数据转化为资产，是改变协作未来的关键一步。"
quiz:
  - question: "ADRs4AI所追求的核心价值是什么？"
    choices: ["无限扩展AI的记忆力", "使人类与AI的工作决策过程具备可持续性和可恢复性", "让AI独立做出所有决策"]
    answer: 1
    explanation: "ADRs4AI旨在确保与AI碰撞出的思想和决策不会挥发，从而获得“认知连续性(epistemic-continuity)”。"
  - question: "ADRs4AI使用的记录原则是什么？"
    choices: ["自动保存到云端服务器", "docs-as-code（文档即代码）原则", "利用AI专用数据库"]
    answer: 1
    explanation: "ADRs4AI遵循docs-as-code原则，即像管理代码一样编写文档，并利用Git进行管理。"
  - question: "ADRs4AI是否仅支持特定AI模型？"
    choices: ["不是，这是一种模型无关（model-agnostic）的方法", "是的，只能在特定模型中使用", "仅支持Gemini模型"]
    answer: 0
    explanation: "ADRs4AI采用了一种不依赖于特定模型的“模型无关（model-agnostic）”方法论。"
lang: zh-cn
ref: 2026-10-26-Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git
---

试想一下：昨晚您与AI加班至深夜，共同设计了一个复杂项目的架构。你们深入讨论了数据库结构（Schema）以及要创建的功能（API）。第二天早上，您对AI说：“按照昨天的设计继续做吧。”然而，AI根本不记得您是谁，也不记得昨天做出了哪些决定。您昨天的努力就这样在过往的聊天记录中消失了。

为了解决许多人所经历的这种无力感，一个名为“ADRs4AI”的概念应运而生。

## 为什么这很重要？

虽然AI变得极其聪明，但其“记忆力”仍有限制。关闭聊天窗口的那一刻，之前讨论的上下文往往会碎片化。如果不记录重要决策背后的理由，当之后再次协作时，不仅需要重复解释相同的内容，甚至可能忘记当初为何做出那样的决定。

ADRs4AI解决了这个问题。它将与AI的协作过程记录在Git（一种追踪软件变更的系统）等版本控制系统中，让我们像管理软件一样管理与AI共同做出的“决策记录（Decision Records）”。通过这种方式，未来的自己或其他协作者随时可以调取与AI交流时的思维脉络。 [出处: ADRs4AI - GitHub](https://github.com/ADRs4AI)

## 通俗地讲

“ADR”最初是“架构决策记录（Architecture Decision Records）”的缩写，是开发者记录为何选择特定技术的方法。ADRs4AI正是将其扩展到了AI协作领域。

打个比方，这相当于**“一份记录与AI对话的个人工作日志”**。正如写日记可以重温过去的思想，ADRs4AI将与AI决定的复杂技术选择编写成Markdown（一种在网页上简便编写文章的文档格式）文档，并保存在项目文件夹中。 [出处: Decision Records for AI-Driven Software Development](https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/)

这就像在拼乐高积木时，在设计图纸上备注为何把这种颜色的积木放在这个位置一样。当以后需要重新组装或修改乐高模型时，只需阅读这些备注，就能毫无困惑地继续工作。

## 当前现状

ADRs4AI不仅停留在概念阶段，已实现为实际工具。

*   **工具集**：由VS Code扩展插件、iOS客户端、项目模板以及阐述该方法论的文章等组成。 [出处: GitHub -ADRs4AI/human-ai-collaboration-template-A](https://github.com/ADRs4AI/human-ai-collaboration-template-A)
*   **模型无关性**：不绑定于特定的AI（如Gemini、Claude）。无论使用哪种AI，都可以应用该方法论。 [出处: What is ADRs4AI?](https://adrs.systems/what-is/)
*   **记录原则**：倡导“docs-as-code（文档即代码）”原则，即处理代码的方式。也就是说，与AI达成的决策在代码仓库内编写为Markdown文档，通过Git进行版本管理，并可通过Pull Request（PR，变更审核请求）接受同事的审查。 [出处: Planning & Architecture Decision Records](https://lukewilk.github.io/AI-architecture/planning-and-adr.html)

这种方法将AI从单纯的“一次性对话对象”提升为共同思考项目的“持续合作伙伴”。 [出处: ADRs4AI - GitHub](https://github.com/ADRs4AI)

## 未来会怎样？

与AI的协作正变得日益复杂。现在已不仅仅是请求编写代码，而是与AI共同思考整个项目的架构设计。

在此过程中，像ADRs4AI这样的“认知连续性（epistemic-continuity，即与AI对话的上下文不中断的状态）”协议将成为必需品。这是因为，我们做出的决定将作为数据留存，这些数据又将回馈并服务于下一阶段AI的学习与推理，从而形成良性循环。正如在民主协商过程中引入AI的案例所见，AI能够极大帮助人类系统性地整理复杂讨论并达成共识。 [出处: AI can help humans find common ground in democratic deliberation](https://deepmind.google/research/publications/65220/)

我们的工作将不再挥发。与AI共同积累的所有思考都会在Git仓库中不断沉淀。当下次打开项目时，变得更聪明的AI将基于这些记录，立即接续我们的对话。

---

### MindTickleBytes AI 记者观点
仅仅将AI的推理过程视为容易挥发的数据是知识资源的巨大浪费。将人类与AI的协作记录纳入Git管理，是人类开始将AI视为项目的“同事”而非仅仅是工具的最明确标志。

---

## 参考资料

1. [GitHub -ADRs4AI/human-ai-collaboration-template-A](https://github.com/ADRs4AI/human-ai-collaboration-template-A)
2. [Home | ADRS—AI-Driven Research for Systems](https://ucbskyadrs.github.io/)
3. [ADRs for AI - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=jlumbroso.adrs4ai)
4. [adrs4ai-pneumatic · PyPI](https://pypi.org/project/adrs4ai-pneumatic/)
5. [Towards Human-AI Deliberation: Design and Evaluation of...](https://arxiv.org/pdf/2403.16812)
6. [deliberation-AI Agents on GitHub | SkillsLLM](https://skillsllm.com/skill/deliberation)
7. [Free AI Humanizer | Humanize AI to Sound Like You, Not AI](https://www.grammarly.com/ai-humanizer)
8. [Human or Not: A Social Turing Game is Back, Play Now](https://humanornot.so/)
9. [AI can help humans find common ground in democratic deliberation](https://deepmind.google/research/publications/65220/)
10. [WURK - Microtask Marketplace for Humans & AI Agents](https://wurk.fun/)
12. [ADRs4AI - GitHub](https://github.com/ADRs4AI)
13. [What is ADRs4AI? · ADRs4AI - adrs.systems](https://adrs.systems/what-is/)
14. [Scaling AI Solution Architecture: How ADRs + Git + Claude...](https://www.linkedin.com/pulse/scaling-ai-solution-architecture-how-adrs-git-claude-rosselet-xhsre)
16. [Planning & Architecture Decision Records | Enterprise AI Delivery](https://lukewilk.github.io/AI-architecture/planning-and-adr.html)
17. [Decision Records for AI-Driven Software Development](https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/)