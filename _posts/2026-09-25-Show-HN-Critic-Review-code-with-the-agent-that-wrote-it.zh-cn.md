---
layout: post
title: "AI编写的代码，能否直接询问‘编写AI’进行评审？‘Critic’登场"
description: "了解‘Critic’这一革新AI生成代码评审流程的工具。本文将清晰、简洁地解释开发者如何与AI代理直接沟通，更透明地审查代码变更，以及其重要性。"
summary: "Critic是一款新工具，它允许开发者通过与生成代码的AI代理直接对话来进行代码评审，从而帮助开发者更深入地理解代码变更并及早发现bug。"
tags: [AI, 代码评审, 开发者工具, Critic, 代理]
image: 2026-09-25-Show-HN-Critic-Review-code-with-the-agent-that-wrote-it.jpg
image_alt: "一名开发者正在审查代码，旁边一个AI代理正在解释代码生成过程。象征着透明的代码审查流程。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI代码生成时代必不可少的伴侣，Critic为开发者与AI的协作方式设定了新标准，使得软件开发更加可靠。"
quiz:
  - question: "Critic旨在解决的主要问题是什么？"
    choices: ["AI代理编写代码的速度太慢", "开发者难以充分理解AI生成的代码变更", "开发者进行代码审查过于频繁", "AI代理提出太多问题"]
    answer: 1
    explanation: "Critic旨在解决开发者难以充分理解和审查AI生成的代码变更的问题。为此，它允许与编写代理进行直接沟通。"
  - question: "通过Critic，AI代理如何‘解释’代码变更？"
    choices: ["直接通过语音解释", "在代码块中添加注释，并附带截图等证据", "自动生成文档文件", "请求其他AI代理进行解释"]
    answer: 1
    explanation: "使用Critic的AI代理可以在代码的关键块中添加注释，并包含相关的证据，如截图或本地执行说明，来解释其代码变更 [Source 8]。"
  - question: "Critic提供的‘交互式代码审查’最大的优点是什么？"
    choices: ["缩短代码编写时间", "开发者能更深入地理解AI代理的意图并提供反馈", "增加代码的复杂性", "提高AI代理的学习能力"]
    answer: 1
    explanation: "开发者在查看代码变更时，可以直接与AI代理对话，深入理解AI为何如此编写代码、其意图是什么，并立即提供必要的反馈 [Source 8]。"
lang: zh-cn
ref: 2026-09-25-Show-HN-Critic-Review-code-with-the-agent-that-wrote-it
---

## AI编写的代码，能否直接询问“编写AI”进行评审？“Critic”登场

想象一下。您负责的项目需要添加一个新功能，这次由一个专业的编码AI代理（Agent，自主执行任务的AI）来代替您完成了。代码看起来很完美，但您想知道这段代码为何这样编写，是否存在隐藏的意图。就像老师审查学生写的文章一样，您想理解代码的每一行，但却难以准确把握AI的思考过程。传统方式只能基于“结果”进行判断。

但现在，一个可以缓解这些担忧的新工具出现了。那就是“Critic”。Critic是一个创新的工具，它允许在评审AI生成的代码时，直接向编写该代码的AI代理提问并听取解释。就像与共同编写代码的同事交流一样，您可以与AI对话，审查代码的变更之处 [Source 8]。

## 这为何重要？

随着AI技术的飞速发展，编码代理正成为我们开发过程中不可或缺的一部分。然而，AI生成代码时会产生一个重大问题：‘透明度’和‘理解’的缺失。AI生成的代码可能以复杂或不可预测的方式运行，难以理解其意图 [Source 16, Source 19]。

这种理解的不足可能导致严重问题。例如，根据CodeRabbit的研究，AI生成的代码在逻辑和准确性问题、安全漏洞、可读性问题等方面，比现有代码多出1.5到2倍以上 [Source 17, Source 19]。简单来说，AI编写的代码往往是“表面上看没问题，实则难以捉摸”的。如果开发者在未完全理解AI代码的情况下将其合并，就可能将意外的bug或安全漏洞部署到实际服务中，风险大大增加 [Source 16]。

Critic旨在解决这些问题，它帮助开发者通过与AI代理直接沟通，理解代码变更的‘为什么(Why)’ [Source 8]。就像看着建筑蓝图与建筑师直接对话一样，您可以向AI询问代码的每个部分为何如此编写，并听取其解释。这有助于开发者提高对AI代码的信任度，并在生成PR（Pull Request，代码合并请求）之前及早发现并修复潜在问题 [Source 1]。

## 易于理解：AI大厨的解释

Critic的核心理念很简单：让AI在编写代码的过程中，像人一样添加“注释（Annotation，代码中的解释）”和“证据（Evidence）”来展示其过程。

打个比方，Critic就像一个在您旁边解释烹饪过程的“AI大厨”。普通的菜谱只提供最终的食谱，但这位AI大厨会说：“我先放这些食材是为了味道的平衡，这里增加炸衣的厚度是为了让口感更酥脆。作为证据，我给您看我做实验时的照片。”

使用Critic的AI代理可以在其编写的代码的关键块中直接添加注释，例如：“此函数使用此逻辑进行用户认证”，“此变量使用HashMap（一种用于快速查找数据的结构）而非数组来处理数据，以提高效率”等 [Source 8]。

更进一步，AI还可以提供“证据”来支持其决定。例如，可以附上代码编写前进行的模拟结果截图，或者包含该代码的本地执行指南 [Source 8]。这就像一个学生解完数学题后，不仅给出答案，还展示解题过程、使用的公式以及练习痕迹。这样，代码审查就不再仅仅是确认，而是扩展为一个更深入、更具生产力的沟通平台 [Source 3]。

## 当前状况

目前，Critic支持开发者在浏览器环境中通过行内注释（直接添加到代码中的解释）和行级差异（line-level diffs，对修改后的代码进行详细比较）来审查AI代理生成的代码 [Source 4, Source 18]。开发者可以针对特定代码行提问或留下反馈，然后AI代理会根据该反馈修改代码并做出响应，形成对话 [Source 3, Source 18]。就像聊天一样，您可以与AI代理实时互动，逐步改进代码。

与早期AI代理的提问系统采用“尽力队列（best-effort queue，努力处理请求但不保证响应）”不同，这种对话系统是一个巨大的进步 [Source 2]。过去，开发者提问时AI常常不响应或响应延迟，而Critic改进了这种连接问题，帮助开发者更直接、更灵活地与AI互动 [Source 2]。

此外，Critic还能实现考虑整个代码库上下文的审查 [Source 1]。这有助于AI代理在提出代码变更建议之前，更早地发现潜在问题 [Source 1]。许多开发者已经在使用Critic的帮助，在将AI代理生成的结果上传到GitHub之前，有效地审查其工作 [Source 3]。

## 未来展望？

Critic等工具的出现，有潜力深刻改变AI驱动的软件开发的未来。未来，AI代理将不仅仅是代码的生成者，还将具备解释、辩护自己代码的能力，并理解和采纳开发者的反馈。这将把开发者与AI的“协作”水平提升到一个新的高度。

随着AI不再被视为一个黑箱，其内部工作原理和意图变得透明可见，开发者将能更信任、更高效地利用AI生成的代码。这不仅有助于提高代码质量，还将促进整体开发速度的提升。

最终，Critic将成为一个重要的基石，使我们能够理解并接触到AI代理编写的每一行代码背后的“原因”，从而最大化AI驱动开发的信任度和效率。未来，所有AI生成的代码旁边自然地附带“此代码由该代理出于此原因编写”的说明的日子将会到来。

## AI的视角

MindTickleBytes AI记者视角：Critic的出现明确表明AI正从简单的工具演变为“协作者”。AI能够解释和论证自身工作的能力，将缩小与人类开发者之间的信任差距，并最终在更复杂、更重要的项目中扩展AI的作用。

## 参考资料
1. [AI代理的代码审查 - 多代理审查系统](https://www.bing.com/aclick?ld=e8fAthOC5Uhcwj7u_-XQ0frDVUCUzG8bAeK22Kp7eSCLMY2iESJM9XX4api1PMLqWcIqU-EZunBGopdV5Zw7BHv5wDgbIwfWKKTRwmlLnXfdD2XNImF90QBWu3WGkdtjo8c1VQV_AD4kJPiKkBf3cTDg_F7m2KtFM4PUfZU-OlohQPfRGAbpbo9WYouuSrag5MptldEBMgbMiSdeNOf1ebRY2MoXg&u=aHR0cHMlM2ElMmYlMmZ3d3cucW9kby5haSUyZmZlYXR1cmVzJTJmcW9kby1hZ2VudGljLXRvb2xib3glMmYlM2Z1dG1fdGVybSUzZGNvZGUlMjUyMHJldmlldyUyNTIwZm9yJTI1MjBjb2RpbmclMjUyMGFnZW50cyUyNnV0bV9jYW1wYWlnbiUzZCUyNnV0bV9zb3VyY2UlM2RiaW5nJTI2dXRtX21lZGl1bSUzZHBwYyUyNnV0bV9pZCUzZDQ4ODMwMjUzMSUyNmhzYV9hY2MlM2Q1MDQwOTg0MDMxJTI2aHNhX2NhbTUzZDQ4ODMwMjUzMSUyNmhzYV9ncnAlM2QxMjM0NzUzMTk5ODk4NTUzJTI2aHNhX2FkJTNkJTI2aHNhX3NyYyUzZG8lMjZoc2FfcnRhZ19rdyUzZGNvZGUlMjUyMHJldmlldyUyNTIwZm9yJTI1MjBjb2RpbmclMjUyMGFnZW50cyUyNmhzYV9tdCUzZHAlMjZoc2FfbmV0JTNkYWR3b3JkcyUyNmhzYV92ZXIlM2QzJTI2bXNjbGtpZCUzZDcxYjk0YTRmMGQ2OTE0ZjdkMGQwMjBmYWFiYmU4Yzc1&rlid=71b94a4f0d6914f7d0d020faabbe8c75)
2. [Show HN: Critic – 与编写代码的AI代理一起审查代码](https://www.simpleprog.com/news/show-hn-critic-review-code-with-the-agent-that-wrote-it-56943a49)
3. [Show HN: Crit – 用于代理计划和代码的本地审查工具...](https://news.ycombinator.com/item?id=48062402)
4. [Show HN: Crit – 像审查PR一样审查AI代理的工作](https://news.ycombinator.com/item?id=47322273)
8. [ShowHN:Critic–与编写代码的AI代理一起审查代码](https://modernorange.io/item/49834098)
17. [Agentic Code Review | AddyOsmani.com](https://addyosmani.com/blog/agentic-code-review/)
18. [Crit - 指向行。告诉代理。](https://crit.md/)
19. [Agentic Code Review](https://www.oreilly.com/radar/agentic-code-review/)