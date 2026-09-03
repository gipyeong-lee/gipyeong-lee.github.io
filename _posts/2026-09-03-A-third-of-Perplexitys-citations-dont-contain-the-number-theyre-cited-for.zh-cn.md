---
layout: post
title: "AI 提供的“依据”，可信吗？Perplexity 引用的背叛"
description: "探讨 AI 搜索引擎 Perplexity 所提供的出处可能缺乏实际依据的研究结果。"
summary: "最新研究显示，Perplexity 作为回答依据所列出的出处中，有相当一部分并未包含实际的数据或数值。"
tags: [AI, 搜索引擎, Perplexity, 人工智能, 可信度]
image: 2026-09-03-A-third-of-Perplexitys-citations-dont-contain-the-number-theyre-cited-for.jpg
image_alt: "叠加在 AI 搜索结果画面上的问号图标"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在这个时代，相比盲目相信 AI 的回答，交叉验证已成为必修课。必须时刻警惕技术便利性背后隐藏的“幻觉（Hallucination）”可能性。"
quiz:
  - question: "此次研究中发现，在包含数值的句子后面所附的引用，实际上并未包含该数值的概率约为多少？"
    choices: ["约 14.4%", "约 34.7%", "约 94%"]
    answer: 1
    explanation: "研究结果显示，在提及数值的句子的引用中，有 34.7% 指向了并未包含该数值的页面。"
  - question: "Perplexity 在查找信息时主要使用哪种方式？"
    choices: ["基于学习数据的回答", "基于实时网页搜索的回答", "利用离线数据库"]
    answer: 1
    explanation: "Perplexity 不依赖于学习过的数据，而是使用通过实时网页搜索获取最新信息的方式。"
  - question: "与传统搜索结果相比，Perplexity 的引用点击率（CTR）如何？"
    choices: ["差不多", "远低于传统方式", "远高于传统方式"]
    answer: 2
    explanation: "Perplexity 的引用点击率为 18~24% 左右，远高于传统搜索引擎 2~4% 的水平。"
lang: zh-cn
ref: 2026-09-03-A-third-of-Perplexitys-citations-dont-contain-the-number-theyre-cited-for
---

想象一下。为了准备今晚的演讲，你问 AI 搜索引擎：“今年我国的 AI 市场增长率是多少？”AI 立即给出了回答，并在句子末尾贴心地附上了 [1]、[2] 这样的数字，注明了出处。通常看到这样的出处，我们会因“这是 AI 亲自查阅并确认过的信息”而感到安心。但如果这些出处实际上指向的是毫不相关的页面呢？

最近，AI 搜索服务 Perplexity 作为回答依据所列出的引文，其冲击性的真实情况被公开。让我们一起看看我们所信任的那些“出处”到底有多准确，以及 AI 为什么会犯这种错误。

## 为什么重要？

与传统搜索引擎不同，Perplexity 会自动汇总海量的网页数据来生成答案。因此，用户无需逐一点击多个网站，即可一次性获得答案。[出处: Perplexity 是一个引用引擎](https://mentionagent.ai/blog/how-to-get-cited-by-perplexity/)。实际上，用户点击引文（用数字标注的出处）的比例达到了 18~24%，这远高于传统搜索引擎 2~4% 的点击率。[出处: 2026 年在 Perplexity 中被引用的方法](https://www.miniloop.ai/blog/perplexity-seo-how-to-get-cited-2026)。

也就是说，我们非常信任 AI 提供的出处，并确实通过它们深入挖掘信息。然而，如果这些信息并不包含事实，我们将面临陷入虚假信息泥潭的风险。

## 通俗理解

简单来说，Perplexity 的工作方式类似于**“一位精明的秘书为你查阅并整理无数书籍”**。秘书在写回答时，会在脚注处写道：“此内容在第 5 页”。然而，有时秘书写完文章后，会事后补上脚注说：“啊，这段内容好像在第 5 页左右吧”。[出处: Perplexity 引用模式](https://bcited.ai/blog/perplexity-citation-patterns-source-selection)。在这个过程中，因为秘书的记忆模糊，导致它指出了错误的页面。

调查数据显示，在带有数值的句子所附的引文中，约 34.7% 连接到了完全不包含该数值的页面。[出处: Perplexity 引用审计报告](https://hausresearch.com/reports/perplexity-citation-audit/)。比喻来说，就像我们要查看数学题的答案页，结果书后的解析却写着完全不同题目的解析。此外，根据综合评估，Perplexity 所提出的主张中，约 14.4% 的内容并未得到所引出处的支持。[出处: Perplexity 引用审计报告](https://hausresearch.com/reports/perplexity-citation-audit/)。

## 现状

Perplexity 在约 94% 的回答中都会注明出处。[出处: 2026 年，Perplexity 总是注明出处吗？](https://www.fonzy.ai/blog/does-perplexity-cite-sources)。但问题在于，AI 模型本身在生成回答后，并不去确认该回答是否属实，而是采取一种“事后”拼凑出处的做法。[出处: Perplexity 引用模式](https://bcited.ai/blog/perplexity-citation-patterns-source-selection)。

当然，有时并非 Perplexity 的错。也存在因为外部应用无法正确显示 Perplexity 的数据，导致出处链接看起来消失了的现象。[出处: Perplexity 未标注出处问题](https://perplexityaimagazine.com/perplexity-hub/perplexity-not-citing-sources/)。但从根本上讲，系统抓取与回答内容不符的来源，这种“幻觉（Hallucination，人工智能制造出看似合理但并非事实的信息的现象）”确实存在，这是用户需要意识到的局限性。[出处: 2026 年 Perplexity 评价](https://vantaige.io/ai-tool/perplexity)。

## 未来会怎样？

未来，在 AI 搜索服务的竞争中，**“连接到多准确的出处”**将比“展示多少出处”成为更重要的标准。已有研究指出，Perplexity 的引用次数比 ChatGPT 多出约 3 倍，这说明数量上的扩张并不总是能保证质量上的准确性。[出处: Perplexity 引用的 9 个信号](https://citevantage.com/blog/how-to-get-cited-by-perplexity/)。随着用户变得越来越聪明，那些给出错误引用的 AI 平台终将失去信任。

## MindTickleBytes AI 记者的视角
AI 搜索引擎虽然方便，但应警惕毫无根据的自信。当你点击 AI 给出的出处却找不到想要的内容时，这极有可能是因为 AI 并没有深入理解内容，而仅仅是推测了“看起来像样的位置”。在阅读搜索结果时，一定要养成以“批判性视角”再次核实内容的习惯。

## 参考资料
1. [AthirdofPerplexity'scitationsdon'tcontainthenumberthey'r...](https://news.ycombinator.com/item?id=49536201)
2. [How to GetCitedbyPerplexity: The Tactical Playbook for 2026 | Cintra](https://cintra.run/blog/how-to-get-cited-by-perplexity)
3. [How to Rank inPerplexityAI: What 21CitationsPer Query... | BlueJar](https://bluejar.ai/blog/how-to-rank-in-perplexity-ai/)
4. [How to GetCitedbyPerplexityAI | Mentionable](https://mentionable.ai/en/guides/rank-on-perplexity)
5. [PerplexityInlineCitations: How [1][2][3] Links Work](https://amicitable.com/blog/does-perplexity-cite-inline-sources)
6. [PerplexitySEO: How to GetCitedin 2026](https://www.miniloop.ai/blog/perplexity-seo-how-to-get-cited-2026)
7. [How to GetCitedbyPerplexity(2026 Playbook) | MentionAgent](https://mentionagent.ai/blog/how-to-get-cited-by-perplexity/)
8. [The 50 Most-CitedWebsites inPerplexity(September 2026)](https://ahrefs.com/blog/most-cited-domains-perplexity/)
9. [PerplexityCitations| Fetchable Sources, Enquire Desk](https://www.worldwidebacklinks.com/ai-backlinks/perplexity-citations/)
10. [PerplexitycitesClickUp 6,474 times. Notion gets 741… Why?](https://foundationinc.co/lab/vol-304)
11. [PerplexityCitationPatterns: What Actually Gets Sourced — b/cited](https://bcited.ai/blog/perplexity-citation-patterns-source-selection)
12. [How to earn morecitationsinperplexityai search](https://snoika.com/blog/perplexity-ai-search-citation-checklist)
13. [How to GetCitedbyPerplexity: 9 Source Signals | CiteVantage](https://citevantage.com/blog/how-to-get-cited-by-perplexity/)
14. [A third of Perplexity's citations don't contain the number they're ...](https://hausresearch.com/reports/perplexity-citation-audit/)
15. [Perplexity Not Citing Sources: 8 Fixes 2026](https://perplexityaimagazine.com/perplexity-hub/perplexity-not-citing-sources/)
16. [Perplexity AI Review 2026: Citations, Limits & Real Failures](https://vantaige.io/ai-tool/perplexity)
17. [Does Perplexity Always Cite Sources? 2026 Data Says No](https://www.fonzy.ai/blog/does-perplexity-cite-sources)
18. [How Perplexity Selects Its Citations: What We Know From Testing and ...](https://aiseoshift.com/blog/how-perplexity-selects-citations/)
19. [Getting Cited by Perplexity: What It Actually Quotes — Genαi](https://genalphai.com/getting-cited-by-perplexity-teardown/)
20. [How Perplexity Decides Which Sources to Cite - authoritytech.io](https://authoritytech.io/blog/how-perplexity-selects-sources-algorithm-2026)