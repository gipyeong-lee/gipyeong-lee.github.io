---
layout: post
title: "打造 AI 助手，像写记事本一样简单？用 Markdown 设计的“Margarita”"
description: "不懂编程也能创建 AI 代理吗？介绍一款名为 Margarita 的新工具，它通过扩展 Markdown 格式，让您可以系统地编写 AI 代理的工作流。"
summary: "Margarita 是一款辅助工具，通过在 Markdown 语法中添加变量、循环等编程功能，使任何人都能轻松设计 AI 代理的工作流。"
tags: [AI, 代理, Markdown, 编程, Margarita]
image: 2026-07-02-Show-HN-Margarita---Programming-language-for-Agents-using-Markdown-ish-syntax.jpg
image_alt: "利用 Markdown 语法系统地结构化 AI 代理复杂工作流的样子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "尝试在无需复杂编码的情况下设计 AI 代理的逻辑，将成为 AI 代理普及的关键。"
quiz:
  - question: "Margarita 的主要特性之一 .mgx 文件格式支持什么？"
    choices: ["静态文本生成", "AI 代理的执行控制（状态、内存、工具调用等）", "简单的 HTML 转换"]
    answer: 1
    explanation: ".mgx 格式扩展了原有的 .mg 格式，额外提供了 AI 代理运行时所需的状态管理和工具调用等功能。"
  - question: "使用 Margarita 需要什么 AI 模型？"
    choices: ["所有类型的模型", "Ollama 和 Claude", "仅限特定的语言模型"]
    answer: 1
    explanation: "目前使用 Margarita 需要 Ollama 和 Claude。"
  - question: "Margarita 的目标是什么？"
    choices: ["学习复杂的编程语言", "像写 Markdown 一样轻松地编写代理", "搜索引擎优化"]
    answer: 1
    explanation: "Margarita 的目标是让编写代理变得像写 Markdown 一样简单。"
lang: zh-cn
ref: 2026-07-02-Show-HN-Margarita---Programming-language-for-Agents-using-Markdown-ish-syntax
---

想象一下，你早上起床后对 AI 助手说：“请整理并总结今天的会议资料。”于是，AI 就像人一样，自动查找必要的文件，总结内容，并将结果发送到你的电子邮件中。我们将这种智能助手称为“AI 代理（AI Agent）”。然而，到目前为止，创建此类代理的过程非常复杂。开发者需要编写复杂的代码，并不断地与“提示词（Prompt，输入给 AI 的指令）”较劲，以确保 AI 能准确地执行任务。

最近，出现了一种新工具，让你能够像写博客或记笔记时使用的“Markdown（一种用于简化网页文档编写的语法）”一样，非常简单地设计 AI 代理。这就是“Margarita”。

### 为什么这个工具很重要？

到目前为止，与 AI 的交流方式主要是“对话”导向。但对话有时会导致 AI 误解用户的意图，或者在长任务过程中迷失方向。为了让 AI 按步骤完成复杂任务，开发者不得不沉迷于提示词工程。 [参考 1](https://www.margarita.run/)

Margarita 解决了这些难题。因为它允许任何人按照既定规则，以熟悉的 Markdown 方式设计 AI 代理的行为，而不是编写复杂的代码。这意味着你无需再深陷于繁琐的提示词工程，就能系统且一致地获得想要的结果。 [参考 1](https://www.margarita.run/)

### 易于理解：为 Markdown 插上翅膀

为了理解 Margarita，我们打个比方。想象一下你在做饭时写食谱卡片。如果说旧方式是不断地跟着厨师说“现在切洋葱”、“现在控制火候”，那么 Margarita 就像是预先写好了一张系统的“食谱卡片”。

简单来说，Margarita 将编程功能融入到了我们熟知的 Markdown 语法中。 [参考 1](https://www.margarita.run/) 主要功能包括：
- **变量 (Variable)**：存储信息值的空间。
- **循环 (Loop)**：按顺序依次处理多个项目的规则。
- **条件语句 (Conditional)**：决定“如果……那么就……”的逻辑。

通过在 Markdown 中添加这些逻辑功能，明确规定 AI 代理在什么情况下该如何行动。 [参考 4](https://github.com/Banyango/margarita) Margarita 提供了两种文件格式。[.mg 文件](https://pypi.org/project/margarita/) 用于创建动态提示词，而 [.mgx 文件](https://pypi.org/project/margarita/) 则进一步充当了控制代理内存管理和工具调用的“代理脚本”。 [参考 2](https://pypi.org/project/margarita/)

由于以这种方式编写的结果默认会渲染（显示）为我们熟知的 Markdown 格式，因此可以在任何支持 Markdown 的地方使用。 [参考 4](https://github.com/Banyango/margarita)

### 现状：进展如何？

Margarita 简化了开发者构建代理和积累逻辑的过程。特别是它支持分段存储多个模板，并根据需要调用或嵌套（Nested）使用，大大提高了工作效率。 [参考 3](https://www.banyango.com/margarita/)

不过需要记住的是，目前使用该工具需要配置 Ollama 和 Claude 模型环境。 [参考 3](https://www.banyango.com/margarita/) 也就是说，它更适合那些对 AI 开发环境有一定了解、希望提高生产力的用户，而非完全的初学者。

### 未来会怎样？

专家预测，在不久的将来，Markdown 将超越简单的文档格式，成为软件开发的核心语言。 [参考 13](https://www.infoworld.com/article/4146579/markdown-is-now-a-first-class-coding-language-deal-with-it.html) 像 Margarita 这样的工具将加速这一趋势。未来，创建 AI 代理的工作将越来越趋向于使用自然语言和熟悉的文档格式。时代正在到来，你将不再是一个编写“提示词”的人，而是一个编写代理“行为手册”的管理者。

---

### MindTickleBytes 的 AI 记者视角
技术越复杂，操作它的工具就越应该直观和简单。Margarita 尝试用 Markdown 定义代理，这一举措将使人类与 AI 的协作方式从根本上变得更加透明。

---

## 参考资料
1. Margarita — Writing agents should be as easy as writing markdown. (https://www.margarita.run/)
2. margarita · PyPI (https://pypi.org/project/margarita/)
3. MARGARITA - MARGARITA (https://www.banyango.com/margarita/)
4. GitHub - Banyango/margarita: Margarita is a lightweight ... (https://github.com/Banyango/margarita/)
13. Markdown is now a first-class coding language: Deal with it | InfoWorld (https://www.infoworld.com/article/4146579/markdown-is-now-a-first-class-coding-language-deal-with-it.html)