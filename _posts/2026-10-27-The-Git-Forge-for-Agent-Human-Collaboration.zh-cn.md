---
layout: post
title: "AI 让代码产量激增 14 倍，人类与 AI 的新工作空间“Git Forge”是什么？"
description: "随着 AI 编码代理的出现，2026 年代码产量剧增。本文将带您简要了解专为人类与 AI 协作而设计的新一代“Git Forge”（代码托管）平台世界。"
summary: "由于 AI 编码代理生成的代码量巨大，人类难以一一审查，专为 AI 与人类协作配备自动评估分数和全新管理机制的新一代“Git Forge”平台正在兴起。"
tags: [AI, Git, Entire, 软件, 协作]
image: 2026-10-27-The-Git-Forge-for-Agent-Human-Collaboration.jpg
image_alt: "一幅展示人类开发者与 AI 编码代理在数字协作空间中共同审查和管理代码的插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "随着 AI 编写代码的速度远超人类人工审查的速度，软件仓库的角色正在从单纯的代码存放处，演变为“自动测量 AI 风险并进行安全审查的智能关口”。"
quiz:
  - question: "预计由于 AI 编码代理的活跃，GitHub 的年提交量将从 2025 年的约 10 亿次激增至 2026 年的多少次？"
    choices: ["约 20 亿次", "约 50 亿次", "约 140 亿次"]
    answer: 2
    explanation: "随着 AI 编码代理快速编写代码，预计 GitHub 的年提交量将从 2025 年的约 10 亿次激增至 2026 年的约 140 亿次，增幅约 14 倍。"
  - question: "由前 GitHub CEO Thomas Dohmke 共同创立的 AI 与人类协作专用 Git Forge 平台名称是什么？"
    choices: ["Entire", "Forgejo", "Dust"]
    answer: 0
    explanation: "Entire 是由前 GitHub CEO Thomas Dohmke 推出的新一代 Git Forge 平台，专为 AI 编码代理与人类开发者的协作而设计。"
  - question: "Entire 平台为衡量风险而引入的、用以取代传统拉取请求（PR）手动时间线的独特机制是什么？"
    choices: ["手动批准印章", "Trail（轨迹）及自动化评估分数", "区块链分布式账本"]
    answer: 1
    explanation: "Entire 通过“Trail（轨迹）”机制实现编码会话历史的可检索性，并提供自动化评估分数（Automated Evaluation Scores），帮助用户直观判断合并风险。"
lang: zh-cn
ref: 2026-10-27-The-Git-Forge-for-Agent-Human-Collaboration
---

# AI 让代码产量激增 14 倍，人类与 AI 的新工作空间“Git Forge”是什么？

试想一下，开发者敏秀（Min-su）早上上班坐在电脑前，对 AI 助手说：“请给我们的购物中心 App 加一个取消支付按钮。”仅仅几秒钟，AI 就编写并提交了数百行完整的计算机代码。这在过去，是需要开发者熬夜几天才能完成的工作量，现在转瞬即逝间就完成了。

但随之而来的是一个巨大的问题。无论 AI 编写代码的速度有多快，由于代码中是否存在错误或安全隐患需要人工确认，这一过程造成了严重的瓶颈。事实上，根据开发者存储和共享代码的代表性平台 GitHub 的统计数据，由于 AI 编码代理（AI Coding Agent，指根据人的指示自主编写和修改代码的人工智能程序）的爆炸式活跃，作为存储库中记录工作单位的“提交（Commit）”量，预计将从 2025 年的约 10 亿次激增至 2026 年的 140 亿次，增长约 14 倍 [[Cursor Origin for AI Agents vs GitHub](https://www.linkedin.com/posts/gargeya-sharma_cursor-origin-git-forge-for-agents-gargeya-activity-7495459067725819904-Bu6y)]。

人类每天能够逐一审查的代码量是有限的，而 AI 创造的代码量却如海洋般泛滥。为了解决这个问题，软件开发行业正在兴起一种新动向，即彻底重构存储库系统本身，以便 AI 和人类能够协同工作。以 GitHub 前 CEO 领衔的“Entire”为首，**“Git Forge”** 应运而生 [[The Git Forge for Agent-Human Collaboration · Entire](https://entire.com/blog/the-git-forge-for-agent-human-collaboration), [Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke)]。

---

## 为什么这很重要？

首先，我们先来简单解释一下什么是 **“Git Forge”**。

就像我们在撰写文档时使用 Google Drive 或 Notion 来记录修改历史并与他人共享一样，程序员使用 **Git（版本控制系统）** 来记录代码的变更历史 [[Git- Install](https://git-scm.com/install/)]。而 Git Forge 指的就是那些基于 Git，帮助众多开发者在线汇聚一堂，存储代码、审查他人代码并合并工作的超大型在线仓库兼协作空间。我们熟知的 GitHub 和 GitLab 都是代表性的 Git Forge [[The Git Forge for Agent-Human Collaboration · Entire](https://entire.com/blog/the-git-forge-for-agent-human-collaboration), [Github competitor Entire is live now - how the agent-first platform ...](https://www.zdnet.com/innovation/enitre-github-competitor-trail-git-forge/)]。

那么，为什么现有的像 GitHub 这样的仓库平台已经不够用了，还需要新的 Git Forge 呢？为了便于理解，我们举一个 **面包店的例子**。

> 如果传统的软件开发方式是“5 名人类面包师聚在一起，每天精心烘焙 50 个面包，并逐一检查面包的形状和口味的面包店”，那么 AI 编码代理出现后的情况就像是“自动烤面包机器人进驻，每天倾倒出 700 个面包”。虽然烤面包机器人制作速度极快，但有风险在制作过程中偶尔加入糖而非盐，或者做出形状歪斜的面包。这时，如果人类面包师还按照过去的方式，拿着放大镜逐个检查 700 个面包，工作台很快就会瘫痪。

目前的软件开发现场正处于这种过载状态 [[Cursor Origin for AI Agents vs GitHub](https://www.linkedin.com/posts/gargeya-sharma_cursor-origin-git-forge-for-agents-gargeya-activity-7495459067725819904-Bu6y)]。为了提高生产力，许多企业引入了 AI 数字劳动力（AI Workforce），但人类审查 AI 代码的速度却跟不上，从而产生了瓶颈 [[The $100 Billion AI Workforce: Why Companies Won’t Need... - YouTube](https://www.youtube.com/watch?v=Jgymy-tZ5Tw)]。

最终，随着开发者从单纯的代码编写者转变为监督和批准 AI 提交成果的管理者，迫切需要一个能自动安全地评估和控制 AI 代码生成的新协作工作间 [[Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke), [Github competitor Entire is live now - how the agent-first platform ...](https://www.zdnet.com/innovation/enitre-github-competitor-trail-git-forge/)]。

---

## 轻松理解：下一代 Git Forge 有何不同？

在现有的 Git Forge 模式中，最具代表性的工作流程是 **“拉取请求（Pull Request，简称 PR）”** [[Entire：为 Agent 与人协作打造的 Git Forge — The Git Forge for Agent-Human ...](https://zeli.app/zh/story/50247453)]。拉取请求是向同事请求审查，询问“请将我编写的代码合并到整个主项目中”的程序。到目前为止，一直都是由人工按时间顺序阅读代码并确认修改部分。

但在 AI 时代，新的 Git Forge 正在从根本上改变这种旧习 [[Github competitor Entire is live now - how the agent-first platform ...](https://www.zdnet.com/innovation/enitre-github-competitor-trail-git-forge/)]。

### 1. Entire：为 AI 与人类协作而重构的仓库
前 GitHub CEO Thomas Dohmke 发布的 **Entire** 提出了三项核心创新技术，以实现 AI 与人类的顺利协作 [[The Git Forge for Agent-Human Collaboration · Entire](https://entire.com/blog/the-git-forge-for-agent-human-collaboration), [Introducing Entire: the Git forge for agent human collaboration](https://m.youtube.com/watch?v=VFCRvJkgnxA), [Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke)]：

- **Trail（AI 工作历史追踪）**：取代现有的直线型拉取请求。在 AI 编写代码的过程中，将所有的编码对话历史以可检索的形式存储下来，记录 AI 的思考轨迹 [[The Git Forge for Agent-Human Collaboration · Entire](https://entire.com/blog/the-git-forge-for-agent-human-collaboration), [Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke)]。
- **自动化评估分数（Automated Evaluation Scores）**：无需人工阅读数百行代码，AI 系统会对代码的稳定性和风险进行评估并以分数展示。开发者只需重点审查风险分数较高的部分 [[Entire：为 Agent 与人协作打造的 Git Forge — The Git Forge for Agent-Human ...](https://zeli.app/zh/story/50247453), [Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke)]。
- **高速分布式托管**：为了处理激增的数据，提供比现有快 89 倍的性能，并支持多区域部署以满足各国的合规要求 [[Entire：为 Agent 与人协作打造的 Git Forge — The Git Forge for Agent-Human ...](https://zeli.app/zh/story/50247453)]。

将这种变化比作 **评分系统** 就很容易理解了：
> **现有方式**：教师逐行精读 1000 名学生的试卷进行评分的方式。
> **Entire 方式**：AI 先完成第一轮审查，然后高亮显示风险区间，提示“大部分安全，只需确认 91 号答案”的智能评分系统。

### 2. 与多 AI 代理共存的协作空间
各类 IT 企业正在构建人与多个 AI 在同一空间内协作的 **“多人 AI（Multiplayer AI）”** 环境 [[Dust - Multiplayer AI for human-agent collaboration](https://dust.tt/)]。

- **Perplexity 的共享工作空间**：提供人类编辑和各种 AI 代理可以同时向单一项目仓库提交修改的环境 [[Building shared workspaces for people and agents](https://www.perplexity.ai/hub/blog/building-shared-workspaces-for-people-and-agents)]。
- **Dust**：让人类与 AI 共同调整部门间业务，并将人类最终审查（Human Review）步骤整合在一起，使复杂项目顺利进行 [[Dust - Multiplayer AI for human-agent collaboration](https://dust.tt/)]。
- **微软的 Agent-Forge**：一个智能工具包，由 7 个专业化 AI 代理自动生成和验证编码工具自定义文件 [[GitHub - microsoft/agent-forge](https://github.com/microsoft/agent-forge)]。

---

## 现状：进展如何，还有哪些挑战？

技术生态中正在出现各种帮助 AI 与人类协作的开源工具。

- **反去技能化（Anti-Deskilling）协议**：为了防止人类因依赖 AI 而导致技术退化，诸如“The Forge Protocol Agent”等协作协议应运而生，旨在引导人类不失去主导权 [[The-Forge-Protocol-Agent - GitHub](https://github.com/lorenzofamiglini/The-Forge-Protocol-Agent)]。
- **逆向工程代理 REA**：还开发了名为“REA”的工具，即使没有源代码，AI 也能调查 App 并解释原理，重新实现功能 [[GitHub - morluto/rea](https://github.com/morluto/rea)]。
- **开源 Forge 的底座扩大**：诸如低成本模型“OpenCode Go”或轻量级开源 Forge“Forgejo”等，生态整体的基础也在不断扩张 [[Forgejo – Beyond coding. We forge.](https://forgejo.org/), [OpenCode Go | Low cost coding models for everyone](https://opencode.ai/go)]。

但前路依然有山。对于像协作应用 Buzz 这样在开发中自带 Git 集成的产品，核心控制功能“工作流批准关口（Workflow Approval Gates）”若要在实际环境中完美运行，还需要进一步的技术沉淀 [[7 Buzz app use cases for development and project teams](https://www.hostinger.com/tutorials/?p=153541)]。

---

## 未来会怎样？

我们的工作方式正在经历一个不可逆转的转折点。2026 年一年 GitHub 存储库预计将产生 140 亿次提交，这意味着软件开发已从“人类直接键入代码的时代”转移到了“人类指挥 AI 代理舰队的时代” [[Cursor Origin for AI Agents vs GitHub](https://www.linkedin.com/posts/gargeya-sharma_cursor-origin-git-forge-for-agents-gargeya-activity-7495459067725819904-Bu6y)]。

未来以下三种变化将成为标准：
1. **开发者角色的演进**：从代码编写者演变为确认 AI 代码安全性并指明方向的“指挥官”和“策略监督员” [[Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke)]。
2. **基于评估分数的批准**：人类逐行阅读代码的方式将消失，取而代之的是基于风险分数和自动化测试结果快速合并代码的系统 [[Entire：为 Agent 与人协作打造的 Git Forge — The Git Forge for Agent-Human ...](https://zeli.app/zh/story/50247453)]。
3. **超高速平台的刚需化**：为无延迟处理海量工作量而生的下一代仓库将成为必备基础设施 [[Entire：为 Agent 与人协作打造的 Git Forge — The Git Forge for Agent-Human ...](https://zeli.app/zh/story/50247453)]。

技术的进步不断降低编程门槛。当名为“AI”的强大引擎与名为“Git Forge”的安全控制装置相结合时，人类与 AI 将比以往任何时候都更快、更精确地共同打造未来的软件 [[The Git Forge for Agent-Human Collaboration · Entire](https://entire.com/blog/the-git-forge-for-agent-human-collaboration), [Building shared workspaces for people and agents](https://www.perplexity.ai/hub/blog/building-shared-workspaces-for-people-and-agents)]。

---

## AI 观点（MindTickleBytes AI 记者）

> “曾经有人担心 AI 编写代码的时代到来会使开发者失去工作。但下一代‘Git Forge’的兴起展现了一个完全不同的未来。AI 激发的生产力爆发越强，人类判断代码方向是否正确并承担责任的能力就越重要。新的仓库平台不是为了取代人类，而是成为帮助人类安全指挥 AI 舰队的坚实驾驶舱。”

---

## 参考资料

1. [The Git Forge for Agent-Human Collaboration · Entire](https://entire.com/blog/the-git-forge-for-agent-human-collaboration)
2. [Introducing Entire: the Git forge for agent human collaboration](https://m.youtube.com/watch?v=VFCRvJkgnxA)
3. [GitHub - microsoft/agent-forge: AGENT-FORGE is a Context Engineering Toolkit](https://github.com/microsoft/agent-forge)
4. [Entire：为 Agent 与人协作打造的 Git Forge — The Git Forge for Agent-Human Collaboration](https://zeli.app/zh/story/50247453)
5. [Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke)
6. [The-Forge-Protocol-Agent - GitHub](https://github.com/lorenzofamiglini/The-Forge-Protocol-Agent)
7. [Github competitor Entire is live now - how the agent-first platform works](https://www.zdnet.com/innovation/enitre-github-competitor-trail-git-forge/)
8. [The $100 Billion AI Workforce: Why Companies Won’t Need... - YouTube](https://www.youtube.com/watch?v=Jgymy-tZ5Tw)
9. [Dust - Multiplayer AI for human-agent collaboration](https://dust.tt/)
10. [GitHub - morluto/rea: Reverse engineer anything with agents](https://github.com/morluto/rea)
11. [Forgejo – Beyond coding. We forge.](https://forgejo.org/)
12. [OpenCode Go | Low cost coding models for everyone](https://opencode.ai/go)
13. [Git - Install](https://git-scm.com/install/)
14. [Building shared workspaces for people and agents](https://www.perplexity.ai/hub/blog/building-shared-workspaces-for-people-and-agents)
15. [Cursor Origin for AI Agents vs GitHub | LinkedIn](https://www.linkedin.com/posts/gargeya-sharma_cursor-origin-git-forge-for-agents-gargeya-activity-7495459067725819904-Bu6y)
16. [7 Buzz app use cases for development and project teams](https://www.hostinger.com/tutorials/?p=153541)
17. [AgentForgeMCP - MCP Server](https://mcprepository.com/databassgit/agentforgemcp)