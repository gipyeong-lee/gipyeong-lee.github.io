---
layout: post
title: "AI 编写文档的方式正在发生变化？用“网页”代替文本对话的时代"
description: "最近，在 AI 开发者中，以 HTML 而非简单的文本或 Markdown 接收 AI 回答正成为一种流行趋势。我们将为您通俗易懂地解释由 Anthropic 工程师发起的这一有趣变化及其背后的原因。"
summary: "随着 AI 生成结果的基本形式从简单的文本转向具有丰富视觉表现力的 HTML，我们与 AI 的沟通方式正变得更加直观和多样化。"
tags: [AI趋势, Claude, HTML, Markdown, 提示词工程]
image: 2026-05-18-Using-Claude-Code-The-unreasonable-effectiveness-of-HTML.jpg
image_alt: "一幅 3D 插画，描画了计算机屏幕上简单的文本转化为绚丽且具有交互性的网页的过程"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "从便于人类阅读的格式转向能让机器产出最佳视觉效果的格式，是一个强有力的信号，表明 AI 正在超越单纯的“辅助作者”，进化为“独立的内容生产者”。"
quiz:
  - question: "最近，Anthropic 的工程师 Thariq 提议将其作为 AI 智能体的默认输出格式并引起热议的是哪种格式？"
    choices: ["Markdown", "Python", "HTML"]
    answer: 2
    explanation: "Anthropic 的 Claude Code 团队负责人 Thariq Shihipar 强烈主张使用 HTML 而非 Markdown 作为 AI 智能体的输出格式。"
  - question: "以下哪项不是以 HTML 而非 Markdown 接收 AI 生成结果的主要优点？"
    choices: ["视觉丰富的图表表现", "便于人类直接修改和编辑文本", "包含双向交互功能"]
    answer: 1
    explanation: "指出 HTML 虽然视觉效果出色，但由于代码复杂，在人类直接阅读、编辑并与 AI 进行协作（Co-authoring）方面反而比 Markdown 更不方便。"
  - question: "Thariq 的文章获得爆发性反响并在哪个开发者社区登顶？"
    choices: ["Hacker News", "Reddit", "Stack Overflow"]
    answer: 0
    explanation: "Thariq 的文章包含了 20 个完整的 HTML 示例，并登上了 Hacker News 的榜首，引发了巨大的讨论。"
lang: zh-cn
ref: 2026-05-18-Using-Claude-Code-The-unreasonable-effectiveness-of-HTML
---

想象一下。早晨上班后，你拜托 AI 助手：“帮我整理一下今天下午新产品规划会议的资料。” 迄今为止，AI 总是以黑底白字，顶多混杂一些粗体或项目符号（•）的纯文本形式给出回答。我们不得不复制这些文本，粘贴到 PowerPoint 或 Word 文档中，然后经历画表、涂色等繁琐的后期处理工作。

但是，如果 AI 不仅仅是写字，而是即时生成一个带有可点击按钮、彩色图表以及精美布局的完整“网页”会怎样？你只需打开屏幕就可以直接开始会议。

最近，这种对话方式在硅谷的 AI 专家之间成为了热门话题。也就是主张不以简单的文本格式，而是以编写互联网网站的语言“HTML”来获取 AI 的回答。到底为什么会发生这种变化？对于普通人来说，这又意味着什么呢？

## 为什么这很重要？ (Why It Matters)

过去当我们与 ChatGPT 或 Claude 等 AI 对话时，AI 回复我们的默认格式是“Markdown”。Markdown 是一种非常简单轻量级的文本编写方式。Anthropic 的 Claude 甚至展示了在 Markdown 文件中通过组合特殊字符 (ASCII) 来绘制简单的表格或图表的惊人能力 [[使用 Claude Code：HTML 出人意料的有效性](https://www.techtwitter.com/articles/using-claude-code-the-unreasonable-effectiveness-of-html)]。由于 Markdown 体积轻巧，在任何环境下都能良好打开，最重要的是人类直接阅读和修改非常容易，这些压倒性的优点使其稳固地成为了 AI 智能体与我们沟通的主导文件格式 [[使用 Claude Code：HTML 出人意料的有效性](https://www.techtwitter.com/articles/using-claude-code-the-unreasonable-effectiveness-of-html)]。

但世界正在快速变化。随着 AI 变得越来越聪明，人们开始要求 AI 提供超越简单“草案编写”、更接近“最终结果”的东西。

如果说 Markdown 是以文本为中心的静态“文档”，那么 HTML 就是能包含颜色、图像甚至是动态效果的“综合艺术”。这种微小格式差异之所以重要，是因为它是一个明确的信号，表明我们利用 AI 的方式正在从单纯的“写作助手”转向“完整的应用程序及内容生产者”。

利用 HTML，可以获得复杂的数据可视化、可双向操作的交互功能，以及便于立即与他人分享的丰富形式的结果 [[Claude Code 中 HTML 出人意料的有效性：为什么...](https://www.explainx.ai/blog/unreasonable-effectiveness-html-claude-code-thariq-2026)]。不再需要复制和润色 AI 的回答，它本身就可以作为一份完整的报告、设计方案，甚至是一个小程序。这不仅为开发者，也为完全不懂编程的普通人开启了一个能将想象力立即转化为可见结果的新时代。

## 通俗易懂的解释 (The Explainer)

为了更清晰地理解这种情况，我们来打个比方。

简单来说，Markdown 就像是在办公用便利贴或横线笔记本上写的整洁“笔记”。核心内容整理得很清晰，也可以进行用荧光笔画线（粗体）或编号等装饰。任何人都能轻松看懂，修改文字也很方便。但要把那个笔记本本身作为最终发布资料，就显得有些平淡了。

相比之下，HTML 就像是一本全彩印刷、甚至按下按钮就会发出声音的“高级交互式杂志”。得益于华丽的色彩和精心编排的布局，它能瞬间吸引人们的目光。

过去由于 AI 的能力稍显逊色，人类需要接收 AI 搭建的骨架（草案笔记）并亲自进行精美包装（制作成杂志）。因此，便于人类阅读和修改的“Markdown”格式无疑是最佳选择。但现在 AI 智能体已经变得非常聪明，足以独自承担内容创作的重任。人类几乎不再需要亲手编辑 AI 的结果了 [[使用 Claude Code：HTML 出人意料的有效性](https://andrey-markin.com/directory/claude-code-html)]。如果人类没必要亲自修改，那么主张直接输出视觉上更丰富多彩、能表现图表和颜色的 HTML 结果会更有利，这就是这一主张出现的背景 [[使用 Claude Code：HTML 出人意料的有效性](https://andrey-markin.com/directory/claude-code-html)]。

再举一个例子。假设你想拥有一辆漂亮的汽车。
过去，你会拜托 AI：“帮我设计一个建造现代化汽车工厂的复杂设计图（Web 框架代码）。” 这太宏大且复杂，耗时太长也容易迷失方向。但聪明的开发者很快意识到：直接要求“现在就给我造一辆立马能在路上跑的汽车（纯 HTML）”，是达成目标更快速、更高效的路径 [[Claude Code 刚刚以我们...的方式解决了 HTML | Cynthia Media](https://media.cynthiaconcierge.com/using-claude-code-the-unreasonable-effectiveness-of-html-tool-drop/)]。

## 现状 (Where We Stand)

点燃这场有趣争论的人是 Anthropic 负责“Claude Code”开发团队的工程师 Thariq Shihipar。他在 2026 年 5 月发表了一篇极具挑衅性且充满魅力的文章，指出“要求以 HTML 而非 Markdown 作为 Claude 的输出格式效果惊人” [[使用 Claude Code：HTML 出人意料的有效性](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/)], [[Claude Code 中的 HTML 与 Markdown：为什么 Anthropic 的 Thariq 改变了...](https://pasqualepillitteri.it/en/news/2243/html-vs-markdown-claude-code-thariq-anthropic)]。

Thariq 断言，在给最新的 AI 智能体下达任务时，Markdown 的时代正在落幕，HTML 的时代正在到来 [[Anthropic 工程师引发争论：HTML 是新的 Markdown...](https://noqta.tn/en/news/anthropic-thariq-html-over-markdown-ai-outputs-2026)]。为了支持自己的主张，他公开了多达 20 个完整的 HTML 示例，展示了 HTML 如何提高信息密度、实现交互，并在规划书、代码审查、设计原型（试制品）等实际工作环境中发挥实用性 [[Claude Code 中 HTML 出人意料的有效性：为什么...](https://www.explainx.ai/blog/unreasonable-effectiveness-html-claude-code-thariq-2026)], [[Anthropic 工程师引发争论：HTML 是新的 Markdown...](https://noqta.tn/en/news/anthropic-thariq-html-over-markdown-ai-outputs-2026)]。

这篇文章的影响力确实非常巨大。它瞬间登上了全球顶尖开发者聚集的社区“Hacker News”的榜首，引发了人们在消费 AI 结果方式上的巨大观念转变 [[Anthropic 工程师引发争论：HTML 是新的 Markdown...](https://noqta.tn/en/news/anthropic-thariq-html-over-markdown-ai-outputs-2026)]。在 Twitter (X) 等社交媒体上，也到处流传着赞美 HTML 优势的文章，称其能最大化清晰度和交互性，并呼吁“不要再停留在枯燥的 Markdown 上了” [[使用 Claude Code：HTML 出人意料的有效性](https://youmind.com/landing/x-viral-articles/claude-code-html-effectiveness)]。

但并不是所有人都举双手欢迎这一观点。人们也提出了深刻的反思。
最大的担忧是人类与 AI 的“协作（Co-authoring）”可能会变得极其困难 [[将 Claude Code 与 HTML 结合使用：为什么它有效——以及协作...](https://ideaverse.ai/blog/using-claude-code-with-html-why-it-works-and-the-co-authoring-tradeoff-moyv58kx)]。

在 Hacker News 的讨论中，一位开发者坦言：“我亲手编写复杂的 HTML 表格可能比编写 Markdown 表格更快。但在除此之外的情况下，无论 AI 自动化做得多么好，看着纯 HTML 代码很难保持流畅的阅读和写作流程（Writing flow）” [[使用 Claude Code：HTML 出人意料的有效性...](https://news.ycombinator.com/item?id=48071940)]。

也就是说，作为代价，虽然屏幕上呈现的结果变得更美观，但人类审视结果背面（代码）并共同修改的过程会因为代码过于复杂而受到干扰，这是一个存在的悖论。

实际上，甚至连引领这一潮流的 Thariq 也提到，为了阅读长而复杂的智能体 HTML 输出，他需要将开发者工具 VIM 或 macOS 的快速查看（Quicklook）功能与特殊的扩展程序连接使用，或者粘贴到某处才能正确掌握内容 [[使用 Claude Code：HTML 出人意料的有效性](https://modernorange.io/item/48071940)]。对于普通人来说，技术门槛依然存在。

## 未来展望 (What's Next)

尽管存在这些优缺点，开发者和用户已经开始快速适应并进化。在社区中，活跃地流传着以模板形式整理和分享的有效提示词（指令）配置文件，旨在引导 AI 一次性生成完美的 HTML [[Claude Code HTML 提示词与 GPT-5.5 API 成本... - DEV Community](https://dev.to/soytuber/claude-code-html-prompts-gpt-55-api-cost-changes-highlight-developer-focus-3kdg)]。此外，讲解如何熟练操作 Claude Code 的高级功能和工作流程的 YouTube 教程视频也层出不穷 [[30 分钟精通 Claude Code - YouTube](https://www.youtube.com/watch?v=6eBSHbLKuN0)]。

未来这种扩展性预计将从文本延伸至媒体领域。例如，有人预测通过利用 Codex 或 Claude Code，用户可以立即生成播客形式的音频内容，并将其直接导入到全球最大的音乐平台 Spotify 等，结果的形式将超越网页，变得更加多样和立体 [[使用 Claude Code：HTML 出人意料的有效性](https://aiflow.news/2026/05/08/using-claude-code-the-unreasonable-effectiveness-of-html)]。

结果是，虽然 Markdown 仍将因日常简短对话或笔记而存在，但在需要复杂报告、规划书、视觉资料的工作中，要求“基于 HTML 的结果”很可能成为新的常识。我们现在不再对 AI 说“请用文字解释”，而是会理直气壮地要求“请以精美的网页展示，让我可以点击”。

---

## AI 的视角 (AI's Take)

形式（Format）的改变也会改变我们的思维方式。随着 AI 走出平面文本的狭窄牢笼，插上立体网页技术（HTML）的翅膀，我们现在应该将 AI 视为一个充满无限可能的“画布”和活生生的“独立内容生产者”，而不仅仅是一台“打字机”。

从便于人类阅读的格式转向机器能产出最佳视觉效果的格式，是一个强有力的信号，表明 AI 已经超越了单纯的“辅助作者”。我们投下的下一个提示词将不再仅仅是为了生成句子，而是创造一个人们可以亲手触摸和体验的完整世界。

## 参考资料

1. [使用 Claude Code：HTML 出人意料的有效性](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/)
2. [Claude Code 中 HTML 出人意料的有效性：为什么...](https://www.explainx.ai/blog/unreasonable-effectiveness-html-claude-code-thariq-2026)
3. [使用 Claude Code：HTML 出人意料的有效性](https://andrey-markin.com/directory/claude-code-html)
4. [Claude Code 刚刚以我们...的方式解决了 HTML | Cynthia Media](https://media.cynthiaconcierge.com/using-claude-code-the-unreasonable-effectiveness-of-html-tool-drop/)
5. [Claude Code 中的 HTML 与 Markdown：为什么 Anthropic 的 Thariq 改变了...](https://pasqualepillitteri.it/en/news/2243/html-vs-markdown-claude-code-thariq-anthropic)
6. [Claude Code HTML 提示词与 GPT-5.5 API 成本... - DEV Community](https://dev.to/soytuber/claude-code-html-prompts-gpt-55-api-cost-changes-highlight-developer-focus-3kdg)
7. [使用 Claude Code：HTML 出人意料的有效性](https://modernorange.io/item/48071940)
8. [使用 Claude Code：HTML 出人意料的有效性](https://aiflow.news/2026/05/08/using-claude-code-the-unreasonable-effectiveness-of-html)
9. [30 分钟精通 Claude Code - YouTube](https://www.youtube.com/watch?v=6eBSHbLKuN0)
10. [使用 Claude Code：HTML 出人意料的有效性...](https://news.ycombinator.com/item?id=48071940)
11. [使用 Claude Code：HTML 出人意料的有效性](https://www.techtwitter.com/articles/using-claude-code-the-unreasonable-effectiveness-of-html)
12. [使用 Claude Code：HTML 出人意料的有效性](https://youmind.com/landing/x-viral-articles/claude-code-html-effectiveness)
13. [将 Claude Code 与 HTML 结合使用：为什么它有效——以及协作...](https://ideaverse.ai/blog/using-claude-code-with-html-why-it-works-and-the-co-authoring-tradeoff-moyv58kx)
14. [Anthropic 工程师引发争论：HTML 是新的 Markdown...](https://noqta.tn/en/news/anthropic-thariq-html-over-markdown-ai-outputs-2026)