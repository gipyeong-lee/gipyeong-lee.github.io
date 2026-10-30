---
layout: post
title: "AI 写代码前先写“计划书”？——如何与 AI 安全协作"
description: "深入了解“规划模式（Plan Mode）”与代码验证的重要性，防止 AI 代理擅自修改代码。"
summary: "介绍一种通过“规划模式”确保 AI 代理在修改代码前必须先获得人工批准的协作机制，从而有效预防 AI 协作过程中可能出现的各种错误。"
tags: [AI, 代理, 编码, 规划模式, AI安全]
image: 2026-10-30-Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it.jpg
image_alt: "人类在平板电脑屏幕上审阅 AI 的计划书并按下批准按钮"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在信任 AI 能力的同时，必须保持严格的验证。规划模式是让 AI 与人类相互理解、建立信任的桥梁。"
quiz:
  - question: "AI 的“规划模式（Plan Mode）”的核心作用是什么？"
    choices: ["让 AI 自动完成部署", "确保 AI 在修改代码前获得人工批准", "将 AI 的运算速度提高两倍"]
    answer: 1
    explanation: "规划模式是一项安全保障措施，强制要求 AI 代理在修改代码或创建文件之前必须先编写计划书并经过人类审批。"
  - question: "在以代理为中心的开发环境中，为了提高代码质量会采用什么方法？"
    choices: ["由人类直接编写所有代码", "利用独立的评审员代理和 CI 工具", "在没有 AI 批准的情况下直接部署"]
    answer: 1
    explanation: "在最新的 AI 开发工作流中，除了 CI（持续集成）工具外，还会引入独立的评审员代理，通过对比代码与计划书进行评估，从而保证质量。"
  - question: "在安全敏感的环境中，AI 应用修改方案的标准是什么？"
    choices: ["仅在客户批准的范围内进行测试后应用", "由 AI 自行判断并立即应用", "先应用再后续核对"]
    answer: 0
    explanation: "在安全至关重要的平台中，修改方案仅可在客户批准的范围内经过测试，并在获得明确批准后才能应用。"
lang: zh-cn
ref: 2026-10-30-Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it
---

想象一下：你委托他人进行室内装修，装修师傅却一声不吭地把墙全拆了，事后才问你“现在怎么改？”。这一定会让你感到惊慌且愤怒。我们使用的 AI 编码工具也一样。如果你对 AI 说“帮我实现这个功能”，而它不加思索地把代码改得一团糟，那后果将不堪设想。

随着 AI 技术的进步，我们正迎来“代理（Agent，能够自主判断并执行特定任务的 AI）”时代。然而，要让这些代理准确无误地按照我们的意图行动，该怎么办呢？今天，我们就来聊聊一种名为“规划模式（Plan Mode）”的安全保障机制，它能强制要求 AI 在修改代码前必须先写一份“计划书”。

## 为什么这很重要？

对于日常使用 AI 的人来说，这是一个至关重要的问题。如果 AI 不按你的意图行事，比如意外触碰了网站的支付功能，或者误删了系统运行所必需的配置文件，业务可能会瞬间瘫痪。

虽然 AI 看起来像人类一样会思考和行动，但事实上，AI 往往无法 100% 理解我们所处环境的“上下文（Context）”。因此，在 AI 修改代码之前，由人类预先审阅计划并认可“是的，按这个方向改”，这一流程是必不可少的。通过这种方式，我们可以预先防止 AI 可能犯下的致命错误。

## 易于理解：规划模式即“施工图审阅流程”

“规划模式”可以形象地比作建筑施工开始前的“施工图审阅流程”：

1. **探索阶段**：AI 代理读取你的电脑（代码库）并调研所需工作。此时它仅处于“只读（Read-only）”状态。它完全没有修改或删除文件的权限。[출처: PlanMode: Make ClaudeCodeThink BeforeItTouches...](https://articles.gg/a/plan-mode-make-claude-code-think-before-it-touches-anything)
2. **规划阶段**：AI 编写一份详细的计划书，说明自己将要进行哪些变更。这就像建筑师在动工前展示施工图纸一样。
3. **批准阶段**：你查看这份计划书，如果满意，就点击“批准”按钮。只有在获得批准后，AI 才会开始修改代码。[출처: Google Antigravity use case - The HQ Digital](https://thehqdigital.com/google-antigravity-use-case/)

通过这种方式，我们可以在 AI 拆错“墙”之前及时阻止它。实际上，许多安全的工作流都严格禁止 AI 在没有计划的情况下即兴编写代码。[출처: arXiv Review Paper Harness](https://appautomaton.renocrypt.com/latex-arxiv-SKILL/)

## 当前的验证水平

在当前的 AI 开发一线，工作流程已不仅仅止步于计划书的审批，而是配备了更严密的验证体系：

- **评审员代理的登场**：AI 完成代码编写后，无需人类逐行审阅，精密的“评审员代理”便会登场。该代理会自动验证“AI 是否按照计划实现了功能”，并与人类编写的代码和计划进行对比。[출처: Two Gates and a Night Shift | Vinny Carpenter](https://vinny.dev/blog/2026-07-06-two-gates-and-a-night-shift/)
- **强化安全防护**：在安全敏感型企业中，AI 提出的修改方案必须仅在客户批准的范围内进行测试。“不是让你盲目修改”，而是遵循“在这一范围内确认安全后方可修改”的规则。[출처: Oracle Announces AI Security Mesh Powered by OpenAI Cyber Models](https://www.unite.ai/oracle-announces-ai-security-mesh-powered-by-openai-cyber-models/)

## 未来趋势

未来，使用“计划书”作为协作通用语言将成为与 AI 合作的常态。目前这种模式主要应用于编码领域，但预计未来在文档撰写、财务整理、数据分析等 AI 处理专业任务的各个领域，“规划模式”都将成为必备标准。当你给 AI 指派任务时，它会首先递上一份计划书说：“我准备这样处理。”

MindTickleBytes AI 记者观点：技术虽然进步神速，但安全是不容妥协的价值。这种强制 AI 代理不得逾越人类指令的“验证系统”，是让 AI 真正融入我们日常生活必不可少的“信任围栏”。

## 参考资料

1. [Making Cursor’s agent write plans as artifacts so I can comment on them inline](https://forum.cursor.com/t/making-cursor-s-agent-write-plans-as-artifacts-so-i-can-comment-on-them-inline/175414)
2. [arXiv Review Paper Harness](https://appautomaton.renocrypt.com/latex-arxiv-SKILL/)
3. [PlanMode: Make ClaudeCodeThink BeforeItTouches...](https://articles.gg/a/plan-mode-make-claude-code-think-before-it-touches-anything)
4. [Google Antigravity use case - The HQ Digital](https://thehqdigital.com/google-antigravity-use-case/)
5. [Oracle Announces AI Security Mesh Powered by OpenAI Cyber Models](https://www.unite.ai/oracle-announces-ai-security-mesh-powered-by-openai-cyber-models/)
6. [Two Gates and a Night Shift | Vinny Carpenter](https://vinny.dev/blog/2026-07-06-two-gates-and-a-night-shift/)