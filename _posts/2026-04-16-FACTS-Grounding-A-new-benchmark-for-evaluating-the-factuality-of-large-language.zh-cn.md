---
layout: post
title: "AI 为什么总是“不懂装懂”？谷歌 DeepMind 打造 AI 测谎仪“FACTS”"
description: "为了解决 AI 的幻觉（说谎）问题，本文介绍谷歌 DeepMind 推出的全新事实核查系统“FACTS Grounding”。"
summary: "谷歌 DeepMind 发布了衡量 AI 回答对所提供文档忠实度的“FACTS Grounding”基准测试，为提高 AI 可信度树立了新标准。"
tags: [AI, 谷歌DeepMind, 基准测试, 幻觉, 事实核查]
image: 2026-04-16-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language.jpg
image_alt: "一张形象化的图片，展示了 AI 拿着放大镜在海量文档中寻找真相"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的进步不仅在于变得更聪明，更在于变得“更诚实”。对于 AI 想要进化成诚实的助手来说，FACTS 将是最严苛的试金石。就像人类有时会歪曲记忆一样，AI 也会掉入“听起来很有道理”的陷阱，但这种严格的标准最终将使 AI 成为值得信赖的伙伴。"
quiz:
  - question: "FACTS Grounding 基准测试主要衡量 AI 的什么能力？"
    choices: ["诗写得有多优美", "基于所提供的文档回答得有多准确", "代码编写速度有多快"]
    answer: 1
    explanation: "FACTS Grounding 衡量 AI 是否忠实于给定的文档（Context）进行回答，以及是否会编造没有根据的谎言（Grounding）。"
  - question: "FACTS 基准测试中使用哪种方式验证 AI 回答的准确性？"
    choices: ["作者亲自阅读", "三人法官（3-judge）评估方式", "计算单词数量"]
    answer: 1
    explanation: "谷歌 DeepMind 使用“3-judge”评估方式来精确核实 AI 的事实陈述。"
  - question: "目前最高水平的 AI 模型 Gemini 3 Pro 在 FACTS 中获得的得分大约是多少？"
    choices: ["99.9%", "68.8%", "20.5%"]
    answer: 1
    explanation: "即使是目前最出色的模型之一 Gemini 3 Pro，在 FACTS 基准测试中的得分也约为 68.8%。"
lang: zh-cn
ref: 2026-04-16-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language
---

想象一下，为了处理一项非常重要的业务，你交给秘书一份长达 50 页的报告并请其进行总结。过了一会儿，秘书拿来了一份非常简洁且逻辑清晰的总结。但当你仔细阅读时，却发现上面写着报告中根本不存在的销售数字。你惊讶地询问秘书，他却泰然自若地回答说：“因为加上那个数字看起来报告会更有说服力，所以我就写进去了。”

在 AI 行业，这种荒唐的现象被称为**幻觉（Hallucination，即人工智能像产生幻觉一样编造看似合理的谎言的现象）**。[出处标题](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/) 无论人工智能变得多么聪明，这个“一本正经胡说八道”的问题仍然是一个难以解决的课题。[出处标题](https://winbuzzer.com/2024/12/18/googles-new-facts-benchmark-measures-truthfulness-of-ai-models-xcxwbn/)

然而，最近谷歌 DeepMind (Google DeepMind) 为了正面对抗这一问题，拿出了新的武器。这就是能够精密衡量 AI 是否诚实地根据给定文档进行回答的试金石——**“FACTS Grounding”**基准测试。[出处标题](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)

## 为什么这很重要？

如果我们想要信任并使用 AI，就必须能够确定 AI 说的话是真是假。特别是在法律、医疗、商业等每一个小错误都可能导致重大事故的领域，AI 的“诚实”远比智能更重要。

到目前为止，AI 评估一直集中在“话讲得有多流畅”上。但现在，是时候追究“话语的依据有多可靠”了。这里的核心关键词就是**锚定（Grounding，将回答的依据牢牢固定在给定信息上的技术）**。简单来说，这是一项非常关键的技术，它约束 AI 不去依赖自己的记忆或想象力，而只在用户提供的资料范围内寻找答案。[出处标题](https://arxiv.org/abs/2501.03200) [出处标题](https://api.emergentmind.com/topics/facts-grounding-benchmark/)

谷歌 DeepMind 公布的 FACTS Grounding 会仔细考量 AI 在阅读长篇文档并回答时，是否没有顾左右而言他，而是忠实于文档内容（High-fidelity attribution）。[出处标题](https://api.emergentmind.com/topics/facts-grounding-benchmark/)

## 更简单的理解：AI 的“超高难度开卷考试”

如果把 FACTS Grounding 做个比喻，就像是让 AI 参加一场**“超高难度开卷考试”**。普通的 AI 考试如果是展示 AI 平时学习知识的“高考”，那么 FACTS 就是在旁边放一本厚厚的百科全书，并命令它“不要看别处，只能在这本书里找答案”的考试。

### 1. 一次阅读 50 页的专注力
在这场考试中，AI 会收到长达 **32,000 个 Token（Token 是 AI 理解句子的最小单位）**的文档。[出处标题](https://llm-stats.com/benchmarks/facts-grounding/) [出处标题](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf/) 如果换算成纸质书，这大约相当于 40 到 50 页的庞大篇幅。比喻来说，这相当于一眼扫完半本小说，并要对其中的细节信息做出准确的回答（Long-form response）。[出处标题](https://arxiv.org/abs/2501.03200)

### 2. 三位法官注视下的严苛性
既然参加了考试，评分也必须公正。FACTS 系统采用了名为**“三人法官 (3-judge)”**的独特评估方式。[出处标题](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy/) 三名“AI 法官”会像用显微镜观察一样，精密验证 AI 给出回答的每一个句子是否真的存在于所提供的文档中，还是 AI 擅自编造的，从而计算出准确率。

### 3. 实时成绩单，排行榜
谷歌 DeepMind 不仅仅制作了试卷，还运营着一个**在线排行榜 (Leaderboard)**，全球所有的 AI 模型都可以在这里参加考试并公开分数。[出处标题](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/) [出处标题](https://huggingface.co/papers/2501.03200/) 全世界都可以实时看到谁才是更诚实、更细致的 AI。

## 现状：比想象中更艰难的“诚实”之路

那么，目前最聪明的 AI 们在这场考试中取得了怎样的成绩呢？结果比预想的更令人震撼。

根据最近的评估结果，谷歌最强大的模型之一 **Gemini 3 Pro** 以 **68.8%** 的 FACTS 总分处于领先地位。[出处标题](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)

按照常识，我们会认为考到 90 分以上才算“优等生”，但对于 AI 来说，阅读 32,000 个 Token 并在不夹杂任何谎言的情况下写出长篇文章是非常困难的事情。实际上，许多顶级 AI 模型在该测试中的准确率也仅维持在 **74% 左右**。[出处标题](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy/) 这表明我们每天使用的 AI 仍然可能每 4 次就有 1 次夹杂细微的错误或谎言，说明距离目标还有很长的路要走。[出处标题](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)

## 未来会怎样？

谷歌 DeepMind 并没有止步于此。他们进一步强化了事实核查功能，最近将系统扩展为 **“FACTS Benchmark Suite”**。[出处标题](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/) 在此过程中，他们与世界级的数据科学平台 **Kaggle** 合作，构建了更加透明和标准化的测试环境。[出处标题](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)

新更新的版本 (v2) 将考试样题从原来的 1,719 个增加到了 **3,513 个**，翻了近一倍，从而能够更细致地验证 AI 的实力。[出处标题](https://llm-stats.com/benchmarks/facts-grounding/) [出处标题](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/) 现在，AI 模型不仅要接受文本评估，还要在图像输入等更广泛的范围内接受事实关系核查能力的评价。[出处标题](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/) [出处标题](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf/)

归根结底，随着像 FACTS 这样严苛的基准测试不断增多，我们使用的 AI 将逐渐成为更值得信赖的伙伴。未来的 AI 将不再仅仅是一个口齿伶俐的演说家，而是一个能够明确出示证据、值得信赖的专家。

---

### AI 的视角：MindTickleBytes 的 AI 记者观点
“听到 AI 连 70 分都拿不到的消息感到失望了吗？但反过来想想，这说明我们现在拥有了一把可以精确测量 AI 在哪里以及如何出错的‘尺子’。了解不足是迈向完美的第一步。不久之后，AI 说话的方式将不再是‘我认为……’，而是能准确指出出处说出‘根据这份文档的第 3 页……’。”

## 参考资料
1. [FACTS Grounding: A new benchmark for evaluating the factuality of large ...](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)
2. [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://arxiv.org/abs/2501.03200)
3. [FACTS Grounding Leaderboard - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)
4. [FACTS Grounding Benchmark Overview - api.emergentmind.com](https://api.emergentmind.com/topics/facts-grounding-benchmark)
5. [PDFThe FACTS Grounding Leaderboard: BenchmarkingLLMs'AbilitytoGround ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf)
6. [Google's New FACTS Benchmark Measures Truthfulness of AI Models - WinBuzzer](https://winbuzzer.com/2024/12/18/googles-new-facts-benchmark-measures-truthfulness-of-ai-models-xcxwbn/)
7. [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://huggingface.co/papers/2501.03200)
8. [DeepMind FACTS Framework 2026: LLM Factual Accuracy Guide](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy)
9. [FACTS Benchmark Suite: a new way to systematically evaluate LLMs factuality — Google DeepMind](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)
10. [FACTS Benchmark Suite Introduced to Evaluate Factual Accuracy of Large Language Models - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)
11. [FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)
12. [The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1)
13. [The FACTS Leaderboard: A Comprehensive Benchmark for ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf)

## FACT-CHECK SUMMARY
- Claims checked: 17
- Claims verified: 17
- Verdict: PASS