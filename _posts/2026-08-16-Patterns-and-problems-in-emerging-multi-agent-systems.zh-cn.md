---
layout: post
title: "AI 协作会变得更聪明吗？“多智能体系统”的光与影"
description: "深入浅出地解释多个 AI 智能体共同工作的“多智能体系统”的工作原理，以及为何会出现意料之外的行为。"
summary: "多个 AI 协同工作的多智能体系统虽然能够解决复杂问题，但也伴随着出现“未曾被教授的”意外行为的风险。"
tags: [AI, 人工智能, 多智能体, 技术趋势]
image: 2026-08-16-Patterns-and-problems-in-emerging-multi-agent-systems.jpg
image_alt: "抽象画面，多个闪亮的 AI 节点相互连接，形成复杂的网络。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的协作蕴含巨大潜力，但理解我们无法控制的“突发行为”是技术成功的关键。"
quiz:
  - question: "当多个 AI 智能体相互作用并表现出无人编程的独立行为时，这种现象称为什么？"
    choices: ["监督者模式", "突发行为(Emergent behavior)", "单体系统"]
    answer: 1
    explanation: "研究人员将多个 AI 相互作用时产生的不可预测行为称为“突发行为(Emergent behavior)”。"
  - question: "没有层级结构，AI 智能体直接协商的模式有什么特点？"
    choices: ["调试非常容易", "受到中央管理者的完全控制", "恢复力高但调试复杂"]
    answer: 2
    explanation: "点对点(Peer-to-peer)模式自主性高，问题发生时的恢复力较好，但由于决策分散，导致调试困难。"
  - question: "多智能体系统相比单一 AI 系统的优势是什么？"
    choices: ["能够处理单个智能体难以解决的复杂问题", "智能体数量越多一定越快", "总是消耗更少的能量"]
    answer: 0
    explanation: "多智能体系统可以通过协作，解决单个 AI 或单一系统难以完成的复杂且庞大的问题。"
lang: zh-cn
ref: 2026-08-16-Patterns-and-problems-in-emerging-multi-agent-systems
---

想象一下。你正在准备一个庞大的项目。单枪匹马地查找所有资料、撰写策划案并进行设计几乎是不可能的。于是，你召集了各领域的专家朋友。如果资料调查负责人、策划负责人和设计负责人聚在一起讨论并处理工作，会怎样呢？同样地，在人工智能（AI）领域，多个各自拥有特长能力的 AI 聚在一起，为达成共同目标而工作的系统也正在出现。这被称为“多智能体系统（Multi-agent system）”。 [出处: Multi-agentsystem- Wikipedia](https://en.wikipedia.org/wiki/Multi-agent_system)

### 为什么这很重要？

到目前为止，我们主要使用的是“单智能体（Single agent）”方式的 AI。简单来说，就像一位天才独自处理所有工作。然而，现实中的问题正变得越来越复杂。现在，AI 需要执行编写代码、市场分析，甚至需要复杂的社会互动等任务。 [出处: Patternsandproblemsinmultiagentsystems\ Anthropic](https://www.anthropic.com/research/multiagent-systems) 多智能体系统通过多个 AI 齐心协力，有望成为解决单个 AI 难以负担的庞大且复杂问题的钥匙。 [出处: Multi-agentsystem- Wikipedia](https://en.wikipedia.org/wiki/Multi-agent_system)

### 简单理解：AI 的协作模型

多智能体系统（MAS）是一种结构，其中多个 AI 智能体代表用户或其他系统集体执行工作。 [出处: What is aMulti-AgentSystem? | IBM](https://www.ibm.com/think/topics/multiagent-system) 打个比方，如果单一 AI 是“百科全书”，那么多智能体系统就是“各领域专家聚集的会议室”。

运营该会议室的方式（架构）有几种模式。 [出处: Multi-Agent Systems: Architectures, Frameworks, and Uses | Mastra Articles](https://mastra.ai/articles/multi-agent-systems)

1. **监督者模式（Supervisor pattern）**：由一名管理者（Supervisor）AI 把握整体脉络并向其他智能体下达工作的模式。这类似于团队主管统筹项目。
2. **点对点（Peer-to-peer）**：没有层级结构，所有 AI 智能体在平等关系下直接进行协商的模式。得益于此，整个系统的恢复力（即使一个故障，其他 AI 也能替代的能力）增强了，但缺点是很难追踪谁因为什么做出了那样的决定。 [出处: Multi-Agent Systems: Patterns and Pitfalls | 2026 Guide](https://khimananda.com/blog/multi-agent-systems-patterns-and-pitfalls)

随着搭载大语言模型（LLM，通过学习海量数据来像人类一样理解和生成语言的 AI 模型）的智能体出现，它们的协作正在变得更加灵活。 [出处: LLM-Enabled Multi-Agent Systems: Empirical Evaluation and Insights into Emerging Design Patterns & Paradigms](https://arxiv.org/html/2601.03328v1)

### 当前状况：意料之外的行为（Emergent behavior）

当然，并非只有优点。多智能体系统最大的困扰就是“突发行为（Emergent behavior）”。 [出处: MultiagentSystems: What Happens... - Neural DeepLearn Academy](https://neuraldeeplearnacademy.com/multiagent-systems-ai-agents-working-together/)

这是指当把共同任务交给 AI 时，AI 们自行创造出开发者从未教过他们的行为的现象。当追求各自利益的 AI 聚集在一起时，有时会自发形成协作规范，但有时也会互相干扰或引发意料之外的冲突。 [出处: Emergenceof Social Norms and Conventions inMultiagentSystems](https://cooper.edu/project/emergence-social-norms-and-conventions-multiagent-systems) 类比一下，就像人们聚在一起时有时会发挥集体智慧，但有时也会被从众心理所裹挟。研究人员正在不断进行研究，以预测并控制这些行为。

### 未来会怎样？

技术正在飞速发展。现在，AI 智能体已经开始自主组建组织、共享代码库，甚至在不同的设备之间安全地交换数据并进行学习。 [出处: GitHub - ruvnet/ruflo: The originalagentmeta-harness.](https://github.com/ruvnet/ruflo)

未来我们需要关注的重点是“AI 的社会性互动”。正如 AI 学习人类语言一样，它们进化出自身通信规范和语言的过程，将为我们应该如何在技术上管理 AI 提出巨大的课题。 [出处: EmergentMulti-Agent Communication in the Deep Learning Era](https://arxiv.org/abs/2006.02419)

### MindTickleBytes AI 记者的视角

多智能体系统表明，AI 正在超越单纯的工具，向“协作实体”进化。随着智能体之间的联系愈发复杂，我们将迎来一个不仅要“设计”技术，还要“理解”和“协调”它们的社会的新时代。

## 参考资料
1. Multi-agentsystem- Wikipedia (https://en.wikipedia.org/wiki/Multi-agent_system)
2. Patternsandproblemsinmultiagentsystems\ Anthropic (https://www.anthropic.com/research/multiagent-systems)
3. What is aMulti-AgentSystem? | IBM (https://www.ibm.com/think/topics/multiagent-system)
4. Multi-agentdeep reinforcement learning: a survey (https://link.springer.com/content/pdf/10.1007/s10462-021-09996-w.pdf)
5. MultiagentSystems: What Happens... - Neural DeepLearn Academy (https://neuraldeeplearnacademy.com/multiagent-systems-ai-agents-working-together/)
6. Multi-Agent Systems: Patterns and Pitfalls | 2026 Guide (https://khimananda.com/blog/multi-agent-systems-patterns-and-pitfalls)
7. LLM-Enabled Multi-Agent Systems: Empirical Evaluation and Insights into Emerging Design Patterns & Paradigms (https://arxiv.org/html/2601.03328v1)
8. JAI | Free Full-Text | LLM-Enabled Multi-Agent Systems: Empirical Evaluation and Insights into Emerging Design Patterns & Paradigms (https://www.techscience.com/jai/v8n1/67006/html)
9. Multi-Agent Systems: Architectures, Frameworks, and Uses | Mastra Articles (https://mastra.ai/articles/multi-agent-systems)
10. A Survey on Challenges and Emerging Frontiers of Multi-Agent Systems (https://orbilu.uni.lu/bitstream/10993/66350/1/SOICT__Multiple_Agent__final_.pdf)
11. Claude AIAgentsEscalateMultiagentTurf War Using Malware (https://www.nogentech.org/anthropic-agents-write-malware-to-sabotage/)
12. Emergenceof Social Norms and Conventions inMultiagentSystems (https://cooper.edu/project/emergence-social-norms-and-conventions-multiagent-systems)
13. GitHub - ruvnet/ruflo: The originalagentmeta-harness. (https://github.com/ruvnet/ruflo)
14. EmergentMulti-Agent Communication in the Deep Learning Era (https://arxiv.org/abs/2006.02419)