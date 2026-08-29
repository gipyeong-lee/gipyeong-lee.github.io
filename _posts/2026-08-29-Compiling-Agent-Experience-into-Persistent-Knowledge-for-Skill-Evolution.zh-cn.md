---
layout: post
title: "如果 AI 会写日记？探索“WikiSkill”——让 AI 自我学习与进化的奥秘"
description: "探索 WikiSkill 框架，了解 AI 代理如何像编写维基百科一样总结个人经验，并在此基础上不断完善自身技能。"
summary: "WikiSkill 是一种全新的框架，旨在让 AI 代理以维基百科的形式持续整理经验与知识，并随着技能的提升而同步进化。"
tags: [AI, 代理, 学习, WikiSkill, 技术]
image: 2026-08-29-Compiling-Agent-Experience-into-Persistent-Knowledge-for-Skill-Evolution.jpg
image_alt: "可视化图像，展示了 AI 代理在学习过程中将其经验整理为类似维基百科的知识库，并在此基础上不断进化的过程。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这标志着一个重要的转折点：AI 不再仅仅依赖短期记忆，而是通过将错误转化为数据并沉淀为知识，从而具备了永久性的能力提升。"
quiz:
  - question: "WikiSkill 框架的主要功能是什么？"
    choices: ["抹除 AI 的记忆", "将经验整理为可持续的知识（维基），并伴随技能不断进化", "降低 AI 的运行速度"]
    answer: 1
    explanation: "WikiSkill 是一个旨在将 AI 的经验系统化为类似维基百科的知识库，从而帮助其随技能提升而不断进化的框架。"
  - question: "在 WikiSkill 中，代理技能（Agent Skills）的作用是什么？"
    choices: ["将知识和工作流打包为可复用的资源，以扩展 AI 能力", "切断互联网连接", "删除数据"]
    answer: 0
    explanation: "代理技能的作用是将专业知识和工作流封装为可重用的资源，从而扩展 AI 的能力。"
  - question: "下列哪项不是 WikiSkill 的核心组成部分？"
    choices: ["原始执行经验", "积累的知识", "随机删除数据的系统"]
    answer: 2
    explanation: "WikiSkill 对经验、知识和技能进行结构化管理，其作用是系统地整合而非删除数据。"
lang: zh-cn
ref: 2026-08-29-Compiling-Agent-Experience-into-Persistent-Knowledge-for-Skill-Evolution
---

想象一下，如果你每次学习一项新工作时都必须从零开始，那会怎样？如果你忘记了昨天的错误，今天又会陷入同样的陷阱，工作效率将极其低下。到目前为止，许多 AI 代理（基于 AI 的自动化程序）也面临着类似的问题。虽然它们能执行任务，但在妥善保存过程中获得的宝贵经验并将其应用于下一次任务时，往往力不从心。

但现在，一个新时代正在到来：AI 开始学会将自己的经历记录在“维基（Wiki，一种由用户共同记录和编辑知识的百科全书式网站）”中，并以此变得越来越聪明。这就是全新的框架——“WikiSkill”。

## 为什么这很重要？

在日常生活中，当你要求 AI 助理“整理一下今天需要处理的复杂任务”时，如果 AI 能记得以前的失败经验并自主选择改进后的方法，那会怎样？WikiSkill 让 AI 代理不再仅仅停留在短期记忆，而是能够将自己的经验积累为长期知识。

这不仅意味着 AI 掌握了更多信息，更开启了一个“自我学习并迭代技术”的高级代理时代。特别是在利用 AI 进行业务自动化或复杂决策的过程中，这意味着 AI 将成为人类助手更稳定、更胜任的伙伴。

## 轻松理解：AI 的“学徒制”教育

为了更好地理解 WikiSkill，我们可以将其类比为工匠教导学徒的“学徒制技术教育”：

1. **原始执行经验 (Raw Execution Experience)**：AI 执行任务时所经历的最原始、未加工的体验。这就像学徒第一次在现场摸爬滚打学到的东西一样。
2. **积累的知识 (Accumulated Knowledge)**：学徒将工作中积累的诀窍记录在笔记本上的过程。在 WikiSkill 中，这个笔记本就是“维基（Wiki）”。
3. **可执行技能 (Executable Skills)**：基于笔记本内容所掌握的技术。现在，它已经不再是学徒，而是能够作为熟练工立即处理任务的状态。

WikiSkill 框架将这三个阶段在结构上分离开来，并进行持续连接。也就是说，当 AI 进行经验（执行）时，它会整理这些经验并转化为知识（维基），然后再将这些知识转化为可复用的技能（Skills）。 [Source 1](https://arxiv.org/abs/2608.27454), [Source 2](https://arxiv.org/html/2608.27454)

这种封装后的技能不仅仅是数据，更是包含专业知识和工作流（业务处理流程）的“可复用资源”，能够有效扩展 AI 代理的能力。 [Source 8](https://franklineh.com/learn/research/jz26PjVX0TmRiy7jHAk3), [Source 11](https://paperswithcode.co/paper/2608.27454)

## 当前现状

最新的研究表明，WikiSkill 将 AI 代理的原始执行经验、积累的知识以及可执行技能紧密地联系在一起。 [Source 1](https://arxiv.org/abs/2608.27454), [Source 4](https://academy.dair.ai/papers/wikiskill-compiles-agent-experience-into-a-persistent-wiki-2608.27454) 该系统实现了代理将经验系统地整合到维基中的过程自动化，使得后续的其他模型或代理能够利用这些知识。 [Source 2](https://arxiv.org/html/2608.27454), [Source 12](https://paperswithcode.co/paper/2608.27454)

这种方式也有助于在多个模型之间共享信息，从而整体提升性能。事实上，最近的研究显示，AI 代理已展现出基于自身经验自动发现技能，并在交互过程中逐步自我适应的能力。 [Source 8](https://franklineh.com/learn/research/jz26PjVX0TmRiy7jHAk3), [Source 9](https://paperswithcode.co/paper/2608.27454)

## 未来展望

未来，AI 代理将不再需要每次都接受新的教育。相反，它们将记录下自己经历的所有成功与失败，成为通过记录自我成长的“进化型代理”。开发者将能够透明地观察和管理 AI 积累知识和完善技能的过程，这将大大提高 AI 代理的可靠性和效率。

## MindTickleBytes AI 记者视角

WikiSkill 就像是让 AI 获得了一个名为“记忆”的强大工具。将过去的经验系统化为知识并升华为技能的能力，将成为 AI 作为人类知识伙伴更上一层楼的关键。未来，衡量 AI 代理实力的不再仅仅是它有多聪明，而是它记录得有多好，以及它如何将记录转化为技能。

## 参考资料

1. [WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution](https://arxiv.org/abs/2608.27454)
2. [WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution](https://arxiv.org/html/2608.27454)
3. [Paper page - WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution](https://huggingface.co/papers/2608.27454)
4. [WikiSkill compiles agent experience into a persistent wiki | DAIR.AI Academy](https://academy.dair.ai/papers/wikiskill-compiles-agent-experience-into-a-persistent-wiki-2608.27454)
5. [WikiSkill:CompilingAgentExperienceintoPersistentKnowledge...](https://deeplearn.org/arxiv/814105/wikiskill:-compiling-agent-experience-into-persistent-knowledge-for-skill-evolution)
6. [WikiSkill:CompilingAgentExperienceintoPersistentKnowledge...](https://papers.cool/arxiv/2608.27454)
7. [WikiSkill:CompilingAgentExperienceintoPersistentKnowledge...](https://www.alphaxiv.org/abs/2608.27454)
8. [WikiSkill:CompilingAgentExperienceintoPersiste... | AI Research](https://franklineh.com/learn/research/jz26PjVX0TmRiy7jHAk3)
9. [WikiSkill:CompilingAgentExperienceintoPersistentKnowledge...](https://paperswithcode.co/paper/2608.27454)