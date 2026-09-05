---
layout: post
title: "AI 编程工具如何选择？1.7 万次实验揭示的意外结果"
description: "通过 1.7 万次测试，了解 Claude Code、Cursor、Codex 等 AI 智能体在选择第三方工具时的运作标准。"
summary: "研究表明，AI 编程智能体在选择工具进行任务时，意见一致的情况仅占 42%，且每个智能体都有其明显的工具偏好。"
tags: [AI, 编程, Claude, Cursor, Codex]
image: 2026-09-06-Which-tools-do-Claude-Codex-and-Cursor-choose-We-measured-17k-runs-to-find-out.jpg
image_alt: "形象化展示 AI 智能体工具选择过程的图片，其中不同颜色的连接环错综复杂地交织在一起"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "智能体选择工具的方式并非单纯的喜好，而是其开发哲学的体现。开发者应意识到，所使用的 AI 工具可能会影响最终产出的结果。"
quiz:
  - question: "根据研究结果，三个 AI 智能体选择相同工具的比例是多少？"
    choices: ["10%", "42%", "85%"]
    answer: 1
    explanation: "研究人员进行了 1.7 万次实验，结果显示三个智能体全部选择相同工具的情况仅占 42%。"
  - question: "在处理语音智能体任务时，Cursor 最偏好的工具是什么？"
    choices: ["Twilio", "OpenAI Realtime API", "Vapi"]
    answer: 2
    explanation: "研究显示，Claude Code 偏好 Twilio，Codex 偏好 OpenAI Realtime API，而 Cursor 最倾向于使用 Vapi。"
  - question: "本次研究分析的编程会话大约有多少次？"
    choices: ["约 5,000 次", "约 17,000 次", "约 50,000 次"]
    answer: 1
    explanation: "为了理解智能体的工具选择过程，研究人员进行了 16,893 次至 17,000 次左右的实验。"
lang: zh-cn
ref: 2026-09-06-Which-tools-do-Claude-Codex-and-Cursor-choose-We-measured-17k-runs-to-find-out
---

想象一下：为了做出一道美味的佳肴，你把同样的食材交给三位专业厨师，并请他们进行烹饪。然而，在开始动手之前，他们却各自拿出了完全不同的工具，并陷入了长时间的思考。一个人拿起刀，一个人拿起剪刀，另一个人则坚持使用专用切割机——他们各自固执地采用不同的处理方式。显然，不同的工具会使菜肴的形状和口感产生细微的差别。

最近，在人工智能 (AI) 编程领域，人们发现了与之极其相似的有趣现象。一项研究分析了我们常用的 AI 编程智能体——Claude Code、Cursor 和 Codex——在实际执行任务时是如何选择外部工具的。 [출처: Armature](https://armature.tech/blog/which-tools-coding-agents-install)

### 为什么这很重要？

对于日常使用 AI 的人来说，这不仅仅是一个技术话题。当我们告诉 AI“帮我写段代码”时，根据 AI 选择的工具不同，项目的产出、稳定性，甚至是数据安全性都可能发生变化。 [출처: o16g](https://o16g.com/updates/2026-09-04-0601/)

换句话说，AI 智能体在编写你的代码时使用什么样的“工具”，将对你的数字化工作环境产生重大影响。理解它们的工具选择方式，就好比在聘请一位值得信赖的合作伙伴。如果你知道哪位合作伙伴偏好哪种工具，就能根据自己的工作目标选择最适合的 AI 智能体。

### 简单来说：挑选 AI 的“工具箱”

我们可以这样比喻：你的房间里有一个巨大的“工具箱”，里面装满了无数工具。当 AI 智能体收到编程任务时，它们就会从中取出所需的工具来使用。

这项研究深入分析了约 17,000 次编程会话。 [출처: Armature](https://armature.tech/blog/which-tools-coding-agents-install), [출처: CCTest](https://cctest.ai/en/articles/how-claude-choose-tools-evidence-from-17-000-runs) 就像安装了监控摄像头，观察三位厨师（智能体）在工具箱前拿取什么工具，整整观察了 1.7 万次。

研究结果令人惊讶。三个智能体选择相同工具的情况仅占总数的 42%。 [출처: CCTest](https://cctest.ai/en/articles/how-claude-choose-tools-evidence-from-17-000-runs) 也就是说，它们的意见一致率甚至不到一半。例如，在实现语音相关功能时，Claude Code 偏好 Twilio，Codex 偏好 OpenAI 的实时 API (OpenAI Realtime API)，而 Cursor 则偏好 Vapi。 [출처: Armature](https://armature.tech/blog/which-tools-coding-agents-install)

简而言之，即使点的是同样的菜（编程任务），每位厨师（智能体）偏好的烹饪工具也各不相同。这是因为每个智能体的设计哲学或学习背景不同。就像人一样，智能体也拥有各自的喜好和工作习惯。

### 当前现状：AI 编程智能体的性格

目前市场上并存着各自拥有不同个性的智能体：

* **Claude Code**：能够解读极其广泛的上下文，并支持子智能体或自定义钩子（在代码执行过程中增加功能的装置）等细致设置。 [출처: The AI Engineer](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor)
* **Cursor**：擅长将任务拆分为多个独立的任务空间 (worktrees) 进行处理。 [출처: The AI Engineer](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor)
* **Codex**：在操作系统强制的沙盒（与外部隔离的安全空间）环境中运行，并提供 IDE（集成开发环境）扩展、Web 应用以及 Slack 集成等多种环境。 [출처: The AI Engineer](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor), [출처: Builder.io](https://www.builder.io/blog/codex-vs-claude-code)

由于各工具的诞生背景和主攻领域不同，用户应根据自己的编码风格选择合适的智能体。 [출처: The Code Media](https://thecode.media/claude-code-cursor-codex-ai-agenty/)

### 未来会怎样？

未来，AI 智能体的工具选择将变得更加智能化。它们不仅会停留在坚持使用偏好工具的阶段，还将进化出更精准的“决策力”，即自行判断在特定任务中哪种工具最安全、最高效。 [출처: o16g](https://o16g.com/updates/2026-09-04-0601/) 作为用户，我们将需要更透彻地掌握智能体选择何种工具，并拥有根据需要进行调整的控制权。

### MindTickleBytes AI 记者的观点

AI 选择工具的方式与人类的习惯极其相似。但它们所面临的考量因素远比我们选择工具时要复杂得多。1.7 万次实验所展现出的智能体个性暗示着：未来 AI 将不再仅仅是“通用机器”，而是进化为“拥有各自哲学思想的专家”。你的编程搭档现在正拿起什么工具呢？

## 参考资料
1. [Which tools do Claude Code, Codex and Cursor choose? We measured 16,893 sessions to find out. · Armature](https://armature.tech/blog/which-tools-coding-agents-install)
2. [How Claude, Codex and Cursor Choose Coding Tools - CCTest](https://cctest.ai/en/articles/how-claude-choose-tools-evidence-from-17-000-runs)
3. [Agents, Memory, and Safer Tooling: Practical Updates for Outcome Engineers · o16g](https://o16g.com/updates/2026-09-04-0601/)
4. [Claude Code vs Codex CLI vs Cursor: which one to choose?](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor)
5. [Codex vs Claude Code: which is the better AI coding agent?](https://www.builder.io/blog/codex-vs-claude-code)
6. [ClaudeCode,CursorиCodex: какой AI-агент выбрать — журнал...](https://thecode.media/claude-code-cursor-codex-ai-agenty/)