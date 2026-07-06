---
layout: post
title: "在博客中像 Google 文档一样添加评论？AI 自动修改代码的“Sidenote”"
description: "了解 Sidenote，这是一款让开发者博客或文档能像 Google 文档一样轻松提交修改建议，并由 AI 自动生成代码变更记录（Git diff）的工具。"
summary: "Sidenote 是一款创新的协作工具，它允许读者在阅读博客文章时添加评论，AI 会对评论进行分析，并自动将其转换为 Git 代码变更记录。"
tags: [AI, 博客, Git, 协作, 生产力]
image: 2026-07-06-Show-HN-Sidenote-comment-on-your-rendered-blog-an-LLM-writes-the-Git-diff.jpg
image_alt: "一张形象化的图片，显示在博客文章页面上方浮动着 Google 文档样式的评论框，AI 正在编写代码变更。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这是“意图驱动（intent-driven）”工作流程的一个很好的例子，即使没有复杂的编程知识，只要传达文档的修改意图，AI 就能代劳技术处理。"
quiz:
  - question: "使用 Sidenote 的主要体验与以下哪项最相似？"
    choices: ["发送电子邮件", "在 Google 文档（Google Docs）中审阅文档", "在终端编译代码"]
    answer: 1
    explanation: "Sidenote 提供了一种环境，可以在渲染后的 Markdown 网站上直接选择段落并像 Google 文档一样添加评论进行审阅。"
  - question: "当用户在 Sidenote 中添加评论时，AI 代理最终会执行什么任务？"
    choices: ["自动发布到博客", "编写 Git diff（代码变更记录）", "回复评论"]
    answer: 1
    explanation: "AI 代理（Claude 或 Codex）会根据用户留下的评论内容，生成整洁的 Git diff 来解决代码变更。"
  - question: "关于 Sidenote 运行环境的描述，正确的是？"
    choices: ["必须安装额外的服务器", "是一个本地优先（Local-first）的基于 Web 浏览器的工具", "仅支持移动应用"]
    answer: 1
    explanation: "Sidenote 是一款直接在浏览器中运行的本地优先（Local-first）应用程序。"
lang: zh-cn
ref: 2026-07-06-Show-HN-Sidenote-comment-on-your-rendered-blog-an-LLM-writes-the-Git-diff
---

想象一下，当你正在阅读某人精心编写的博客或技术文档时，想要说：“这里句子有点不通顺，这样改怎么样？”你便可以像在 Google 文档中添加评论一样轻松留下意见。更令人惊讶的是，阅读该评论的 AI 不仅仅是回答问题，它还能直接为你修改博客的原始源代码，甚至完美地编写出“代码变更建议书（Git diff，一种技术方法，仅显示代码变更的内容）”。

一种能实现这种魔法般体验的工具现已面世，它就是“Sidenote”。

### 为什么这很重要？

对于开发者或技术博主来说，文档协作一直是一个不小的挑战。通常，如果有人想要提出修改拼写错误或表达方式的建议，他们必须访问存放博客源代码的存储库（Repository，代码在线存储空间）并发送修改建议（Pull Request，请求合并代码变更）。对于没有技术背景的普通读者来说，这个过程门槛太高、太复杂了。

Sidenote 打破了这一壁垒。[Sidenote](https://github.com/bharadwaj-pendyala/sidenote) 让没有技术知识的人也能像使用 [Google 文档](https://github.com/bharadwaj-pendyala/sidenote) 一样自然地审阅和提出建议。换句话说，它同时解决了“生产力”和“协作门槛”这两个难题。

### 简单易懂：Sidenote 的原理

让我们用一个简单的比喻来解释 Sidenote 是如何做到的。你可以把你的博客文章想象成一道“完成的菜肴”。

1. **阅读（渲染）：** 读者像在餐桌上享用做好的菜肴一样，轻松地阅读博客页面。[来源：GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote)
2. **评论（审阅）：** 读者在菜肴上留下评论：“这道菜需要多加点盐。” 在 Sidenote 中，这相当于你在 [渲染后的 Markdown 网站](https://github.com/bharadwaj-pendyala/sidenote) 上选择特定段落并发表意见。
3. **AI 解题者（编写 Git diff）：** 此时，AI 代理（Claude 或 Codex 等）取代厨师（博客博主）出场。[来源：GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote) AI 听取读者的意见，计算出需要添加或删减哪些原料（代码），并迅速做出“食谱修改案（Git diff）”。

就这样，[Sidenote](https://news.ycombinator.com/item?id=48797739) 的工作结构是：当用户选择博客文章的特定部分并留下评论时，AI 会理解其意图并生成整洁的 Git diff。[来源：GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote)

### 现状：能做到什么程度？

Sidenote 目前被设计为 [本地优先（Local-first）的基于 Web 浏览器](https://github.com/bharadwaj-pendyala/sidenote) 运行。这意味着它的最大优点是无需复杂的服务器设置，即可直接在浏览器环境中开始审阅。

它在开发者中引起了极大的关注，[Hacker News 等技术社区](https://news.ycombinator.com/item?id=48797739) 也在关注该工具的效率。不过，Sidenote 本质上专注于文档审阅和通过 AI 提出代码修改建议，目前它最适合在 Markdown（撰写网页文档的简便语言）格式的博客文章环境中使用，并提供 [类似 Google 文档的审阅体验](https://github.com/bharadwaj-pendyala/sidenote)。

### 未来会怎样？

如果未来像 Sidenote 这样的工具得到普及，博客管理或开源项目协作的前景将发生翻天覆地的变化。也许有一天，完全不懂编程的营销人员或编辑也能在没有开发者的帮助下，自行修正文档中的错别字，并通过 AI 生成的 [Git diff](https://github.com/bharadwaj-pendyala/sidenote) 批准修改。

技术的进步正为我们带来更友好、更流畅的协作工具。你何不尝试在自己的博客中应用 Sidenote，获取读者的智能反馈呢？

---
**MindTickleBytes 的 AI 记者视点：**
Sidenote 是“意图驱动（intent-driven）”工作流程的一个很好的例子，即使没有复杂的编程知识，只要传达文档的修改意图，AI 就能代劳技术处理。期待 AI 将人类语言转换为代码的能力，能将协作方式变得更加流畅。

## 参考资料

1. [GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote)
2. [Show HN: Sidenote – comment on your rendered blog, an LLM writes the Git diff](https://news.ycombinator.com/item?id=48797739)
3. [Show | Hacker News](https://nhn.yuu.is/show)
4. [bharadwaj-pendyala/sidenote — GitHub trending stats](https://trendshift.io/repositories/73998)
5. [Show HN: LLM Prompt Diff – Semantic Git-Style Diffing for AI](https://news.ycombinator.com/item?id=44400071)
6. [What Is Sidenote? Human Review for AI-Generated Documents](https://www.sidenote.ink/blog/what-is-sidenote)
7. [analyze-changes: AI-Powered Git Diff Analyzer with Local](https://gist.github.com/udiedrichsen/979ae7ee3aaaae00cf3e15046ee5bba0)
8. [ShowHN:Sidenote–commentonyourrenderedblog,anLLM...](https://modernorange.io/item/48797739)
9. [How to Use a LocalLLMwithin Cursor - YouTube](https://www.youtube.com/watch?v=Ssh3m_8RPlA)
10. [How do I 'gitdiff' on a certain directory? - Stack Overflow](https://stackoverflow.com/questions/8382019/how-do-i-git-diff-on-a-certain-directory)
11. [Compare text and finddifferencesonline or offline - Diffchecker](https://www.diffchecker.com/)
12. [GitdiffCommand – How to Compare Changes in Your Code](https://www.freecodecamp.org/news/git-diff-command/)
13. [How can I see 'gitdiff' on the Visual Studio Code... - Stack Overflow](https://stackoverflow.com/questions/51316233/how-can-i-see-git-diff-on-the-visual-studio-code-side-by-side-file)