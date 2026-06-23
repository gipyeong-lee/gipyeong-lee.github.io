---
layout: post
title: "AI 生成的代码，别再只用截图了：通过网站分享——Display.dev 的故事"
description: "如何将 AI 智能体生成的代码或文档发布为安全的企业级网页，而非本地链接"
summary: "Display.dev 是一个独立的作业空间，允许用户在不依赖额外工具的情况下，通过企业认证安全地发布并共享 AI 智能体生成的成果（如 HTML、Markdown 等）。"
tags: [AI, 智能体, 生产力, 工具, 开发]
image: 2026-06-23-Show-HN-Displaydev-the-agent-agnostic-workspace-for-HTML-and-md-artifacts.jpg
image_alt: "屏幕上显示由 AI 生成的交互式图表和文档，已转化为整洁的网页形式进行共享"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "随着智能体生态系统的碎片化，不依赖特定模型的“共享标准”将成为生产力工具的必要条件。"
quiz:
  - question: "使用 Display.dev 的最大优势是什么？"
    choices: ["绑定到特定的 AI 智能体服务", "无需本地链接或截图，即可通过安全 URL 共享成果", "提高代码运行速度"]
    answer: 1
    explanation: "Display.dev 不依赖特定的 AI 模型或智能体平台，允许用户通过基于企业认证的安全 URL 发布成果。"
  - question: "Display.dev 支持什么样的协作功能？"
    choices: ["仅限 AI 修改", "团队成员可直接在成果上评论，智能体可据此进行修正", "自动编写代码"]
    answer: 1
    explanation: "Display.dev 支持团队成员在成果上添加评论，AI 智能体可以读取这些反馈并直接修改以解决问题，从而支持协作工作流。"
  - question: "Display.dev 可以与哪些类型的智能体结合使用？"
    choices: ["仅限于一个特定的智能体", "可与 LangChain、CrewAI 等多种智能体平台兼容", "仅限于研究型 AI"]
    answer: 1
    explanation: "Display.dev 是一个“智能体中立”的平台，不绑定特定模型，兼容 LangChain、CrewAI、AutoGen、n8n 等多种智能体环境。"
lang: zh-cn
ref: 2026-06-23-Show-HN-Displaydev-the-agent-agnostic-workspace-for-HTML-and-md-artifacts
---

想象一下：今天早上，你要求 AI 智能体“制作一个能让我一目了然地看到团队上个月销售数据的交互式图表”。AI 瞬间就编写出了精美的代码。现在，你需要与团队成员共享这个结果。到目前为止，你是怎么做的？通常不是复制只能在本地电脑上运行的地址（localhost 链接），就是无奈地截图上传到 Slack。

然而，如果团队成员无法直接访问你的电脑，本地链接就毫无用处；而截图又无法呈现图表的动态效果。我们对 AI 的期望不仅仅是“静态结果”，而是“可交互的动态信息”。为了解决这种痛点，Display.dev 应运而生。[参考资料 13](https://coding4food.com/en/post/display-dev-publish-agent-html-company-auth)

### 为什么这很重要？

随着 AI 智能体在日常工作中的应用日益广泛，如何管理它们生成的成果变得至关重要。仅复制一个代码块来共享的时代已经过去了。现在，我们需要共享像复杂的交互式图表、Markdown 文档、交互式仪表盘等“鲜活的成果”。

Display.dev 允许将这些成果发布为基于安全企业认证的 URL，且不绑定于特定的 AI 平台。[参考资料 1](https://display.dev/), [参考资料 12](https://display.dev/agent-platforms) 这就像是点击一下鼠标，就能为 AI 生成的成果创建一个“专属网页”。在安全性要求严格的企业环境中，能够安心地与同事共享并审核 AI 成果，是其最大的亮点。

### 易于理解：一个“共同的工作室”

为了更好地理解 Display.dev，我们可以将其比作一个**“共同的工作室”**。

假设某些 AI 是画家，而另一些是建筑师。尽管画家智能体可以作画，但以往必须亲自携带画作。现在，所有的 AI 都可以将它们的成果挂在 Display.dev 这个安全、共同的画廊中。同事们可以参观画廊，查看画作，并留下访客簿（评论）：“请把这里的颜色调亮一点。”

关键在于，无论是由哪位“画家”（智能体平台）创作的作品，这个画廊都兼容。无论你使用的是 LangChain、CrewAI、AutoGen 还是 n8n，成果都会上传到同一个空间。[参考资料 12](https://display.dev/agent-platforms) 因此，即使你更换了所使用的 AI 智能体工具，共享的 URL、版本和记录依然保持不变。[参考资料 1](https://display.dev/)

再换个比喻，Display.dev 就像是一个**“智能透明公告板”**。如果之前的截图是贴在公告板上的一张照片，那么上传到 Display.dev 的成果就是一个真正的公告板，你可以在上面直接筛选数据并放大图表。[参考资料 11](https://hb.int2inf.com/en/s/item/D92WS3ojFhTkBSdMe6Tqhw-display-dev-platform-for-agent-artifacts)

### 现状：超越截图的时代

目前，Display.dev 在保留超越简单静态屏幕的交互元素方面表现出色。例如，如果对 AI 生成的基于 D3（数据可视化编程工具）的复杂图表进行截图，其中的交互功能（点击、缩放等）就会失效。而 Display.dev 将这些动态元素以网页形式发布，完美保存了交互性。[参考资料 11](https://hb.int2inf.com/en/s/item/D92WS3ojFhTkBSdMe6Tqhw-display-dev-platform-for-agent-artifacts)

此外，它还支持团队成员直接对成果发表评论，AI 智能体可以阅读这些评论并修正问题或解决任务，从而支持协作工作流。这就是 AI 与人类在一个空间内针对成果共同思考、不断完善的过程。[参考资料 11](https://hb.int2inf.com/en/s/item/D92WS3ojFhTkBSdMe6Tqhw-display-dev-platform-for-agent-artifacts)

当然，局限性也显而易见。目前的智能体平台尚未将此类共享功能作为标配内置。[参考资料 8](https://news.ycombinator.com/item?id=48584961) 对于用户来说，可能存在需要通过额外平台操作的繁琐感。但这有望随着 AI 智能体生态系统的不断成熟而逐渐整合。[参考资料 8](https://news.ycombinator.com/item?id=48584961)

### 未来会怎样？

未来，AI 智能体将创造出更复杂、更长篇幅的成果。因此，防止智能体生成的代码或文档碎片化，并在一个安全的地方对其进行统一管理与共享的平台，将变得愈发重要。

我们要关注的下一次变革是“工具的融合”。现在我们作为独立服务来使用，未来 Display.dev 这类共享工作空间很有可能成为所有 AI 智能体环境的核心功能。[参考资料 8](https://news.ycombinator.com/item?id=48584961) 你所有的 AI 工作将不再保存在“截图存储箱”中，而是在一个“可共享的工作空间”上进行。

### MindTickleBytes AI 记者视点

随着智能体生态系统碎片化为各种平台，不绑定特定模型或工具的“共享标准”将成为生产力工具的必要条件。Display.dev 的尝试超越了单一技术的工具属性，展示了迈向真正“协作智能体”时代的第一步。

## 参考资料

1. [Display.dev – Agent-neutral workspace for artifacts](https://display.dev/)
2. [Coding agent with algebraic memory (VSA) instead of RAG](https://hackernews-kappa.vercel.app/show/48534392)
3. [I made a Note-Taking app for people who keep texting ...](https://hackernews-kappa.vercel.app/show/40925906)
4. [Custom instructions with AGENTS.md – Codex | OpenAI Developers](https://developers.openai.com/codex/guides/agents-md)
5. [Build Autonomous Developer Pipelines using agents.md and skills.md in Antigravity | Google Codelabs](https://codelabs.developers.google.com/autonomous-ai-developer-pipelines-antigravity)
6. [Configuring Agentic AI Coding Tools: An Exploratory Study](https://arxiv.org/html/2602.14690v4)
7. [Agent-Agnostic Repository Guide · GitHub](https://gist.github.com/davidgibsonp/337be9b80b3f03eccd188235c287bb05)
8. [Show HN: Display.dev – the agent-agnostic workspace for HTML ...](https://news.ycombinator.com/item?id=48584961)
9. [Show HN: Display.dev – the agent-agnostic workspace for HTML ...](https://news.mcan.sh/item/48584961)
10. [Show HN: Display.dev – the agent-agnostic workspace for HTML ...](https://hb.int2inf.com/en/s/item/D92WS3ojFhTkBSdMe6Tqhw-display-dev-platform-for-agent-artifacts)
11. [display.dev for Agent Platforms — Display.dev](https://display.dev/agent-platforms)
12. [Display.dev: Publish AI-Generated HTML Behind Company Auth](https://coding4food.com/en/post/display-dev-publish-agent-html-company-auth)