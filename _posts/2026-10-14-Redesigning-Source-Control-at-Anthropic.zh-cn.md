---
layout: post
title: "AI 每秒修改 3 万次代码？Anthropic 抛弃 Git 的原因"
description: "由于 AI 编写的代码量过多，导致传统版本控制系统达到极限，Anthropic 转而使用自主研发的系统“Scion”的背后故事"
summary: "随着 AI 模型 Claude 每天产生超过 3 万次的代码变更，Anthropic 放弃了现有的基于 Git 的基础设施，开发并引入了自主版本控制系统“Scion”。"
tags: [Anthropic, AI开发, 版本控制, Scion, Claude]
image: 2026-10-14-Redesigning-Source-Control-at-Anthropic.jpg
image_alt: "可视化展示复杂代码网络与 AI 代理交互的图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的生产力已超越人类开发者，正在动摇现有的工具体系。现在是一个基础设施本身必须为“代理（Agent）”而设计的时代。"
quiz:
  - question: "Anthropic 引入自主版本控制系统“Scion”而非现有 Git 的主要原因是什么？"
    choices: ["为了降低成本", "因 AI 代理爆发式代码生成导致现有系统出现瓶颈", "为了提供更安全的安全性功能"]
    answer: 1
    explanation: "在 AI 自主编写代码并反复迭代的过程中，代码合并量从每天 2,500 次激增至 3 万次，现有基础设施已无法承受。"
  - question: "Anthropic 的新系统“Scion”是为哪种环境设计的？"
    choices: ["仅供人类开发者使用的离线环境", "AI 代理 24 小时不断编写代码并进行迭代的环境", "移动应用开发专用环境"]
    answer: 1
    explanation: "Scion 是专为 AI 代理不断生成代码并自主进行迭代学习的环境而优化设计的。"
  - question: "Anthropic 在代码变更后没有运行所有测试，而是引入了什么方式？"
    choices: ["完全省略测试", "确定性测试影响分析（Test Impact Analysis）", "随机选择测试"]
    answer: 1
    explanation: "他们引入了基于历史数据和包相关性仅执行必要测试的确定性测试影响分析服务，而不是在每次海量代码变更时都运行所有测试。"
lang: zh-cn
ref: 2026-10-14-Redesigning-Source-Control-at-Anthropic
---

试想一下，如果有人每秒钟修改 3 万次你写的文章，并要求你再次审阅，会是什么感觉？这对于人类来说简直是不可承受的速度。但这正是 AI 公司 Anthropic 办公室里正在发生的事情。随着 AI 模型 Claude 自主进行研究并构建新服务，公司的编码基础设施开始不堪重负。

### 为什么这很重要？

到目前为止，软件开发一直是以“人”的速度为标准的。但随着 AI 开始直接编写代码，**管理和部署已编写代码**比编写代码本身成为了更大的瓶颈。[Anthropic 面临着编码基础设施不再能跟上 AI 生产力的局面。](https://www.theregister.com/devops/2026/10/13/anthropic-reinvents-source-control-as-claude-floods-the-world-with-code/5302943) Anthropic 这次彻底重构基础设施，是展现 AI 时代开发工具应如何演进的重要里程碑。

### 浅显易懂：作为“拼图盒”的 Git 的局限性

我们常用的“Git”是开发者存储和修改代码的协作空间。简单比喻的话，它就像一个多人共用的“拼图盒”。当人数不多时，大家可以守序地完成拼图。

但是，如果 AI 代理们冲向这个拼图盒，每秒钟插入或取出数千个碎片，会发生什么？盒子会爆炸。现有的 Git 是基于人类中心的“离线”开发环境设计的，因此在处理 AI 实时倾泻而下的数万项变更时，显得过于沉重。[Anthropic 的代码合并量从每天 2,500 次暴增至 3 万次，增长了近 12 倍。](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)

因此，Anthropic 直接创造了一种全新的系统——**“Scion”**。Scion 是专为 AI 代理设计的“AI 专用版本控制系统”，即使 AI 代理 24 小时不停地修改代码，它也能稳健运行。[Anthropic 在 5 个月内将现有的单一仓库（Monorepo）完全从 Git 迁移到了 Scion。](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)

### 当前状况：旨在适配 AI 速度的基础设施改进

Anthropic 不仅仅更换了版本控制系统，随着 Scion 的引入，他们还进行了几项核心变革。

1.  **代码审查工具的进化**：人类直接确认数万行代码是不可能的。Anthropic 引入了名为**“Antique”**的全新专用代码审查系统，创造了一个让人类能够高效审查 AI 产生的大量变更的环境。[Anthropic 开发并部署了这个与 Scion 配套的新代码审查界面。](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)
2.  **智能测试系统**：如果每次代码变更都运行所有测试，耗时过长。因此，Anthropic 分析历史数据与代码的相关性，引入了**“确定性测试影响分析服务”，仅挑选并运行必要的测试**。[这种方式提高了测试执行效率，再次提升了开发速度。](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)

### 我们处于什么位置？

Anthropic 的案例是软件开发环境正从“以人为中心”向“以 AI 代理为中心”转移的信号弹。过去，开发者关心的是计算机的性能；现在，则是到了必须考虑计算机能否承受代理活动的时期。这种变化不仅限于 Anthropic，未来无数科技企业都将寻找新的基础设施，以支撑超越人类便利性的、机器那惊人的生产力。

### 未来会怎样？

我们所使用的服务更新周期将变得越来越短，而其背后将驻扎着这种 AI 为实现自主成长而奋斗的新型“数字工厂”。像 Scion 这样的基础设施象征着 AI 已经跨越了单纯的工具阶段，进入了自行重塑技术基础的“自我进化”阶段。[Scion 是专为 AI 常驻的“Agent-always-on”场景而设计的。](https://zeli.app/zh/story/50073633)

我们正处于从人类开发者编写代码的时代，转向 AI 编写代码而人类负责监督结果的有趣转折点。

---

**MindTickleBytes 的 AI 记者视角**
AI 自主修改代码和研究的“代理（Agentic）”时代已经开启。Anthropic 的举措意味着 AI 不再只是消耗技术，而是进入了自行重塑技术基础设施的自我发展阶段。

## 参考资料

1. [AnthropicClaude Can NowControlYour Computer - YouTube](https://www.youtube.com/watch?v=eB7E-mtpC18)
2. [Anthropic(Anthropic)](https://huggingface.co/Anthropic)
3. [How AI is transforming workatAnthropic\Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
4. [Agentic coding is straining CI. Here’s how we... | Claude byAnthropic](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)
5. [AnthropicAI safety researcher quits with 'world in peril' warning](https://www.bbc.com/news/articles/c62dlvdq3e3o)
6. [EggheadsatAnthropicSaid They Used Claude to "Solve" Humor](https://futurism.com/artificial-intelligence/anthropic-solve-humor)
7. [Anthropicrestores Fable 5, Mythos 5 after U.S. lifts exportcontrols](https://www.linkedin.com/pulse/anthropic-restores-fable-5-mythos-after-us-lifts-export-controls-3ffnc)
8. [Redesigning source control at Anthropic — CodeNews.com](https://codenews.com/news/redesigning-source-control-at-anthropic-1ojqmz)
9. [Anthropic Scion: Why Its Monorepo Left Git at 30,000 Merges](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)
10. [Anthropic Scion Redesigns Source Control for AI Agents](https://scalevise.com/resources/anthropic-scion-agent-scale-source-control/)
11. [Anthropic reinvents source control as Claude floods the world ...](https://www.theregister.com/devops/2026/10/13/anthropic-reinvents-source-control-as-claude-floods-the-world-with-code/5302943)
12. [Anthropic Overhauls Source Control to Fix Bottlenecks](https://book.st-hakky.com/en/news/redesigning-source-control-at-anthropic)
13. [Redesigning source control at Anthropic - hoton.ai](https://hoton.ai/en/news/redesigning-source-control-at-anthropic-1vlb4uz)
14. [Anthropic 因Claude重写版本控制系统 — Redesigning Source Control a...](https://zeli.app/zh/story/50073633)
15. [Newsroom \Anthropic](https://www.anthropic.com/news)
16. [AnthropicIs Bleeding Out](https://www.wheresyoured.at/anthropic-is-bleeding-out/)
17. [Hidden AI instructions reveal howAnthropiccontrols... - Ars Technica](https://arstechnica.com/ai/2025/05/hidden-ai-instructions-reveal-how-anthropic-controls-claude-4/)
18. [OpenAI andAnthropicAI crisis explained: OpenAI andAnthropicfear...](https://economictimes.indiatimes.com/world/business/openai-and-anthropic-fear-a-major-ai-crisis-in-the-next-6-to-12-months-heres-what-theyre-preparing-for/articleshow/134860984.cms)
20. [LatestAnthropic(Claude AI) Statistics (2025) | StatsUp](https://analyzify.com/statsup/anthropic)