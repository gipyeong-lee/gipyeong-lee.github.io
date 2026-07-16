---
layout: post
title: "AI会撒谎？为什么我们仍然选择使用大语言模型（LLM）"
description: "尽管AI存在幻觉和各种批评，为什么许多人依然在使用大语言模型（LLM）？本文将探讨其实际价值与未来前景。"
summary: "尽管对AI存在批评声音，但得益于技术的演进与补充方案，LLM依然是强大的工具，正持续提升我们的日常生活和工作效率。"
tags: [AI, LLM, 技术趋势, 生成式AI]
image: 2026-07-16-The-LLM-Critics-Are-Right-I-Use-LLMs-Anyway.jpg
image_alt: "一张象征性的图像，展示了在覆盖着复杂代码和对话框的屏幕上方，积极评价与批判性审核之间的博弈"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "批评是技术成长的养分。认识到LLM的局限性并引入“批评模型”（Critic Models）进行补充，表明我们能够与AI实现更健康的共存。"
quiz:
  - question: "LLM自信地提供错误信息（即“幻觉现象”）的主要原因之一是什么？"
    choices: ["因为学习了互联网上的偏见数据", "因为计算机性能太低", "单纯是因为耗电量大"]
    answer: 0
    explanation: "LLM学习了互联网上庞大的数据，其中包含了矛盾、错误信息和个人观点，且目前的基准测试方式更倾向于奖励“自信的回答”而非“准确性”。"
  - question: "近期AI开发领域中用于查找代码Bug的“批评模型（Critic Models）”是指什么？"
    choices: ["读取人类情绪的模型", "评估其他AI生成结果并提供反馈的LLM", "计算AI电力消耗的程序"]
    answer: 1
    explanation: "批评模型通过强化学习人类反馈（RLHF）进行训练，其作用是以自然语言反馈的形式指出其他AI生成的代码或结果中的错误。"
  - question: "一些开源项目拒绝接受AI生成的代码贡献（PR）的主要原因是什么？"
    choices: ["贡献者太多了", "与开源精神不符的版权问题", "难以确认AI生成物的可信度及投入时间"]
    answer: 2
    explanation: "由于难以区分是人类精心编写的代码还是AI自动生成的代码，社区担心这会破坏信任。"
lang: zh-cn
ref: 2026-07-16-The-LLM-Critics-Are-Right-I-Use-LLMs-Anyway
---

想象一下。今天早上，你开始工作时将昨天整理的几十页合同草案发给了AI，并对它说：“请提取出主要的风险项。”AI瞬间给出了答案。但你脑海中闪过一个念头：‘这些内容真的能信吗？AI会不会自作主张捏造了不存在的内容？’

最近，围绕生成式AI，特别是大语言模型（LLM）的舆论出现了两极分化。有人欢呼AI将彻底改变我们的生活，也有人因幻觉（Hallucination，即AI将虚假信息伪装成事实的现象）、环境影响和可靠性问题而进行强烈抨击。甚至像Zig或Gentoo这样的开源软件项目，也拒绝接收AI生成的代码贡献。[出处: The LLM Critics Are Right. I Use LLMs Anyway. | Jeremy Theocharis](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/)

然而，尽管批评声浪高涨，全球仍有无数用户即使需要支付月费，也依然在使用LLM。[出处: 2025: The Year in LLMs | Hacker News](https://news.ycombinator.com/item?id=46449643) 那么，究竟为何批评与使用能够并存呢？

## 为什么这很重要？

仅仅因为AI“新奇”而使用的时代已经过去了。现在，AI已成为决定工作效率的必备工具。对于开发者而言，LLM在设计复杂函数结构时是极佳的伙伴。[出处: Here’s how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) 但如果信任问题无法解决，在需要重大决策的商业场合，我们就无法放心地使用AI。

批评者的声音在让AI变得更安全的过程中充当了“护栏”的角色。他们指出的幻觉现象，实际上是LLM所学习的互联网数据本身充满了矛盾与偏见，且模型被训练为比起“准确性”，更倾向于提供“用户喜欢听的自信回答”的副产品。[出处: It's 2026. Why Are LLMs Still Hallucinating? - Duke University Libraries](https://blogs.library.duke.edu/blog/2026/01/05/its-2026-why-are-llms-still-hallucinating/) 我们越是直面这些问题，技术就会越趋于完善。

## 简单易懂：超能力图书馆管理员

如果把LLM比作一个容易理解的事物，它就像是一个读过世间所有书籍和互联网文章的“超能力图书馆管理员”。这位管理员通过学习海量模式，能在我们提问时快速找出最像样的答案。[出处: Part 1: How to Apply LLMs and AI to Contracts](https://www.knowable.com/blog/part-1-how-to-apply-llms-and-ai-to-contracts-what-are-llms-anyway/)

但有时，它也会在庞大的知识库中混入不相干的内容。这就像管理员读了太多书，以至于把虚构小说里的情节误认为是真实历史事实来讲解一样。因此，最近引入了一种让“批评家”在旁监督该管理员回答的方式。

“批评模型（Critic Models）”是一种LLM，它能仔细阅读其他AI编写的代码，并像同事开发者一样反馈是否存在逻辑错误或安全隐患。[出处: LLM Critics Help Catch LLM Bugs | Athina AI](https://blog.athina.ai/llm-critics-help-catch-llm-bugs) 实际上，作为批评模型的“CriticGPT”，其查找代码Bug的性能有时甚至超越了人类。[出处: LLM Critics: A New Weapon in the Fight Against AI Bugs](https://medium.com/@ayoubkirouane3/llm-critics-a-new-weapon-in-the-fight-against-ai-bugs-f258a6b7cf91)

## 我们现在处于什么位置？

如今的LLM基于理解上下文并预测下一个单词的“解码器风格Transformer”架构运行，但在内部已经变得更加聪明。它们利用类似于专家组的“混合专家模型（MoE, Mixture-of-Experts）”架构，根据问题性质激活最适合的小模型，从而提升了效率。[出处: The State Of LLMs 2025: Progress, Progress, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)

但显然，局限性依然存在。麻省理工学院的研究显示，模型在学习过程中可能形成错误的关联，从而产生看似完美但在逻辑上完全失败的“合成错误”。[出处: Researchers discover a shortcoming that makes LLMs less reliable](https://news.mit.edu/2025/shortcoming-makes-llms-less-reliable-1126) 这证明了我们绝不能盲信AI的回答，依然必须由“进行验证的用户”把关。

## AI的未来：协同工作的秘书

未来，下一代LLM将变得比现在更加便宜和高效。[出处: LLMs+: 10 Things That Matter in AI Right Now](https://www.technologyreview.com/2026/04/21/1135645/llm-large-language-models-ai/) 不再仅仅是单纯堆砌数据，而是将加强发现并自我修正我们所苦恼的错误的能力。

我们需要摆脱将AI视为“无所不知的完美标准答案”的阶段，转而将其视为“协同工作的创意秘书”。批评不是让技术停止发展的阻碍，而是指引技术走上正轨的灯塔。只有当我们认识到LLM的局限性，并在此基础上批判性地运用这一工具时，我们才能真正成为AI时代的掌控者。

## AI的一句话点评

批评是技术成长的养分。认识到LLM的局限性并引入“批评模型”（Critic Models）进行补充，表明我们能够与AI实现更健康的共存。

## 参考资料

1. [How I use LLMs - YouTube](https://www.youtube.com/watch?v=EWvNQjAaOHw)
2. [As an Experienced LLM User, I Actually Don’t Use Generative LLMs...](https://minimaxir.com/2025/05/llm-use/)
3. [LLM Critics Help Catch LLM Bugs | Athina AI](https://blog.athina.ai/llm-critics-help-catch-llm-bugs)
4. [Using ChatGPT is not bad for the environment](https://blog.andymasley.com/p/individual-ai-use-is-not-bad-for)
5. [Bad (but common) LLM criticisms - Ritza Articles](https://ritza.co/articles/gareth/bad-llm-criticisms/)
6. [Part 1: How to Apply LLMs and AI to Contracts: What are LLMs anyway? - Knowable](https://www.knowable.com/blog/part-1-how-to-apply-llms-and-ai-to-contracts-what-are-llms-anyway/)
7. [Here’s how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)
8. [LLMs+: 10 Things That Matter in AI Right Now | MIT Technology Review](https://www.technologyreview.com/2026/04/21/1135645/llm-large-language-models-ai/)
9. [It's 2026. Why Are LLMs Still Hallucinating? - Duke University Libraries](https://blogs.library.duke.edu/blog/2026/01/05/its-2026-why-are-llms-still-hallucinating/)
10. [Assessing the Strengths and Weaknesses of Large Language Models](https://link.springer.com/article/10.1007/s10849-023-09409-x)
11. [LLM Critics: A New Weapon in the Fight Against AI Bugs](https://medium.com/@ayoubkirouane3/llm-critics-a-new-weapon-in-the-fight-against-ai-bugs-f258a6b7cf91)
12. [LLM News, Updates and Articles](https://llm-explorer.com/static/llm-news/)
13. [The State Of LLMs 2025: Progress, Progress, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)
14. [The LLM Critics Are Right. I Use LLMs Anyway. | Jeremy Theocharis](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/)
15. [Researchers discover a shortcoming that makes LLMs less reliable | MIT News](https://news.mit.edu/2025/shortcoming-makes-llms-less-reliable-1126)
16. [2025 LLM Year in Review – karpathy](https://karpathy.bearblog.dev/year-in-review-2025/)
17. [2025: The Year in LLMs | Hacker News](https://news.ycombinator.com/item?id=46449643)