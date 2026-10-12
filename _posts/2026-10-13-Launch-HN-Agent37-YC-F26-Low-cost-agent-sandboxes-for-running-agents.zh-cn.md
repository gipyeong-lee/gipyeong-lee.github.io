---
layout: post
title: "AI 代理使用电脑的方式：Agent37 如何改变未来"
description: "Agent37 的出现解决了 AI 代理每次执行任务时环境都会被重置的麻烦，并大幅降低了运行代理的成本"
summary: "Agent37 为 AI 代理提供了一种可持续的低成本沙箱，能够在任务之间保持记忆和环境，极大地提高了代理开发环境的效率。"
tags: [AI, AI代理, 开发者工具, Agent37]
image: 2026-10-13-Launch-HN-Agent37-YC-F26-Low-cost-agent-sandboxes-for-running-agents.jpg
image_alt: "展示 AI 代理通过 Agent37 平台在云沙箱环境中高效执行任务的概念图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 代理正从执行临时任务向优化长期记忆和工具使用方向进化。降低基础设施成本将成为代理生态系统进入生产阶段的关键门槛。"
quiz:
  - question: "Agent37 与传统沙箱环境相比，最大的特征是什么？"
    choices: ["任务完成后立即删除文件", "任务结束后仍保留文件、内存和工具", "仅支持一种 AI 模型"]
    answer: 1
    explanation: "Agent37 在任务结束后不会重置环境，而是保留代理的状态（文件、内存、工具），从而在下一次任务时提供连续性。"
  - question: "Agent37 的创始人 Vishnu Krishnaprasad 所主张的平台优势是什么？"
    choices: ["世界上最快的 GPU 性能", "降低 95% 的代理运营成本", "无需代码构建应用的功能"]
    answer: 1
    explanation: "创始人曾表示，通过 Agent37，运营代理的成本可较传统方式降低 95%。"
  - question: "下列哪项不是 Agent37 平台支持的代理 Harness（驱动环境）？"
    choices: ["Claude Code", "OpenAI Codex", "复杂的图形设计工具"]
    answer: 2
    explanation: "Agent37 支持多种代理 harness，如 Claude Code、OpenAI Codex、Hermes 和 OpenClaw，它与运营图形设计工具本身的平台性质不同。"
lang: zh-cn
ref: 2026-10-13-Launch-HN-Agent37-YC-F26-Low-cost-agent-sandboxes-for-running-agents
---

试想一下，如果有一间办公室，你每次上班时都会忘记昨天做过的工作，桌上所有的文件也都不见了。AI 代理（AI Agent，指能自主判断并执行特定目标的 AI 软件）过去的工作方式就是这样。在许多情况下，当代理完成复杂任务后，之前积累的数据或设置值都会毫无意义地被重置。

但现在，AI 代理也可以像我们一样，在“下班后也能保留记忆”的环境中工作了。这得益于硅谷潜力初创公司“Agent37”推出的新方案[Source 2](https://luma.com/b54ojqhl), [Source 7](https://startupfortune.com/run-claude-code-codex-hermes-and-openclaw-for-95-less-agent37-founder-vishnu-krishnaprasad-on-the-affordable-agent-sandbox/)。

### 为什么这很重要？

当我们让 AI 写代码或浏览网页时，这些代理一直被当作一次性工具使用。由于任务完成后环境会被清理，代理不得不每次都从头开始，这非常低效。开发者们试图通过赋予代理更多权限和环境来解决这一问题，但高昂的运营成本成为了巨大的障碍。

Agent37 将这种环境转变为“可持续沙箱（Sandbox，一种与外部隔离的安全软件运行环境）”。现在，代理可以把昨天做的事留到今天继续完成。这不仅意味着方便，还意味着代理的运营成本可以大幅降低。

### 简单来说，是这样的

我们可以做一个比喻：如果传统的 AI 代理环境是“每次都要用橡皮擦擦掉所有内容的白板”，那么 Agent37 的环境就是“随时可以打开继续书写的笔记本”。

Agent37 提供了一个基于云的沙箱，在这里，“沙箱”是指代理可以尽情运行代码、操作数据的安全工作空间。普通的沙箱在任务结束后会删除内部的所有数据[Source 7](https://startupfortune.com/run-claude-code-codex-hermes-and-openclaw-for-95-less-agent37-founder-vishnu-krishnaprasad-on-the-affordable-agent-sandbox/)。然而，Agent37 会保留代理在执行任务时创建的文件、记忆的内存以及常用的工具[Source 7](https://startupfortune.com/run-claude-code-codex-hermes-and-openclaw-for-95-less-agent37-founder-vishnu-krishnaprasad-on-the-affordable-agent-sandbox/)。因此，代理在进行下一个任务时，无需浪费时间和金钱从零开始构建环境。

### 当前状况

目前，Agent37 是一家备受开发者关注的 Y Combinator F26 届初创公司[Source 2](https://luma.com/b54ojqhl), [Source 7](https://startupfortune.com/run-claude-code-codex-hermes-and-openclaw-for-95-less-agent37-founder-vishnu-krishnaprasad-on-the-affordable-agent-sandbox/)。他们支持 Claude Code、OpenAI Codex、Hermes 和 OpenClaw 等目前开发者最常用的代理工具[Source 7](https://startupfortune.com/run-claude-code-codex-hermes-and-openclaw-for-95-less-agent37-founder-vishnu-krishnaprasad-on-the-affordable-agent-sandbox/)。

创始人 Vishnu Krishnaprasad 强调，利用 Agent37 可以将运营代理的成本较传统方式降低 95%[Source 7](https://startupfortune.com/run-claude-code-codex-hermes-and-openclaw-for-95-less-agent37-founder-vishnu-krishnaprasad-on-the-affordable-agent-sandbox/)。此外，他们还通过与 InsForge、Monid 等合作举办开发者代理构建黑客松，积极推动生态系统的活跃[Source 2](https://luma.com/b54ojqhl)。

### 未来走向

随着 AI 代理自主处理越来越复杂的任务，它们的“记忆力”和“工作环境保持能力”将变得至关重要。随着像 Agent37 这样在基础设施层面改善效率的解决方案不断增加，代理将不再是“一次性工作者”，而是进化成为 24 小时随时待命、协助我们工作的助手。我们将迎来一个时代，AI 代理不仅能给出“聪明的回答”，还能成为“持续出色完成工作”的合作伙伴。

---

### MindTickleBytes AI 记者观点
与 AI 技术的发展同样重要的是支撑它的“运营基础设施”。代理的高效状态保持和成本降低，将成为那些长期受限于技术局限的代理进入实际商业现场的强大动力。

## 参考资料

1. [RunAIAgentsLocally with Ollama! (Llama 3.2 Vision...) - YouTube](https://www.youtube.com/watch?v=-WqHY3uE_K0)
2. ["Build anAgent" Hackathon · Luma](https://luma.com/b54ojqhl)
3. [Freestyle - VMs for AIAgents](https://www.freestyle.sh/)
4. [Mosaic | Agentic AI Video Editing Platform](https://mosaic.so/)
5. [awesomeagentsandboxes— filterable table](https://msyvr.github.io/awesome-agent-sandboxes/)
6. [Discover and install skills for AIagents.](https://www.skills.sh/)
7. [RunClaude Code, Codex, Hermes And OpenClaw... - Startup Fortune](https://startupfortune.com/run-claude-code-codex-hermes-and-openclaw-for-95-less-agent37-founder-vishnu-krishnaprasad-on-the-affordable-agent-sandbox/)
8. [E2B | The Enterprise AIAgentCloud](https://e2b.dev/)
10. [The router pattern is underrated, how we cut tokencostsby 60% with...](https://dev.to/alex_aslam/the-router-pattern-is-underrated-how-we-cut-token-costs-by-60-with-intelligent-agent-selection-1kg1)
11. [Resend · Email for developers](https://resend.com/)
12. [Novita AI - AI &AgentCloud for Developers](https://novita.ai/)
13. [Sandboxesaren't enough. Give youragenta real computer and get...](https://fly.io/)
14. [LangChain: the openagentplatform to own your intelligence](https://www.langchain.com/)
15. [GitHub - orbit-online/agent-sandbox: Nix packages and modules for...](https://github.com/orbit-online/agent-sandbox)