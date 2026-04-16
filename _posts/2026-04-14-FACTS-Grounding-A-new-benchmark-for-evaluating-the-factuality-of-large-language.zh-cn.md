---
layout: post
title: "捕捉 AI 的“迷之自信”！Google DeepMind 发布 AI 事实核查测试卷 “FACTS Grounding”"
description: "如何解决 AI 撒谎的“幻觉现象”？通过 Google DeepMind 推出的全新 AI 性能衡量标准 FACTS Grounding，了解提高 AI 准确性的原理。"
summary: "Google DeepMind 发布了衡量 AI 对所提供信息的忠实度的全新基准测试“FACTS Grounding”，致力于解决 AI 的幻觉现象。"
tags: [人工智能, Google DeepMind, 事实核查, AI 幻觉, 技术趋势]
image: 2026-04-14-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language.jpg
image_alt: "机器人用放大镜精确检查文本的形象，象征着 AI 的事实关系核查"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这是 AI 不仅仅变得聪明，更是向成为“值得信赖的伙伴”迈出的重要里程碑。能感受到从性能竞争向可靠性竞争的范式转变。"
quiz:
  - question: "在 FACTS Grounding 基准测试中，以下哪项不是负责对 AI 模型回答进行打分的“评委”模型？"
    choices: ["Gemini 1.5 Pro", "Llama 3", "Claude 3.5 Sonnet"]
    answer: 1
    explanation: "FACTS Grounding 使用 Gemini 1.5 Pro、GPT-4o 和 Claude 3.5 Sonnet 这三种最先进的模型作为评委，自动评估回答的准确性。"
  - question: "在 FACTS Grounding 测试中，AI 需要阅读的文档最大长度是多少？"
    choices: ["1,000 Token", "10,000 Token", "32,000 Token"]
    answer: 2
    explanation: "该基准测试向 AI 提供长达 32,000 Token（约相当于一本书的一部分）的长文档，并要求其从中寻找回答的依据。"
  - question: "FACTS Grounding 的主要目的之一是针对 AI 将错误信息说得像真的一样的现象，这种现象称为什么？"
    choices: ["深度伪造 (Deepfake)", "幻觉 (Hallucination)", "过拟合 (Overfitting)"]
    answer: 1
    explanation: "AI 在接收到复杂输入时生成非事实信息的现象被称为“幻觉 (Hallucination)”，FACTS Grounding 的目的就是减少这种现象。"
lang: zh-cn
ref: 2026-04-14-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language
---

想象一下，在一次非常重要的商务会议前，你把一份超过 100 页的厚厚的市场调查报告交给了 AI。你请求道：“请从这份报告中提取我们公司明年需要关注的 3 个核心数据。”片刻后， AI 非常自信地回答：“好的，根据报告，A 市场的占有率为 15%，增长率为 5%。”但后来你检查发现，报告中根本没有“15%”这个数字。这是 AI 编造出来的谎言。

这种 AI 将非事实信息说得像真的一样自信的现象，我们称之为**“幻觉 (Hallucination，人工智能生成错误信息的现象)”**[FACTS Grounding：评估大语言模型事实性的新基准...](https://www.linkedin.com/posts/michaelyung_facts-grounding-a-new-benchmark-for-evaluating-activity-7275106400496709633-dJed)。尽管大语言模型 (LLM) 已深入我们的生活，但这种“迷之自信”仍然是让 AI 难以获得 100% 信任的一大障碍。

最近，Google DeepMind 为了正面突破这一问题，提出了新的解决方案。那就是衡量 AI 说话是否有事实依据的严苛测试卷——**“FACTS Grounding”**。

## 为什么这对我们很重要？

现在我们遇到疑问时，会找 AI 而不是百科全书。但 AI 传达信息的方式并不像我们预期的那样完美[FACTS Grounding：评估大语言模型事实性的新基准...](https://www.linkedin.com/posts/deepakchaubey_facts-grounding-a-new-benchmark-for-evaluating-activity-7275894260241985536-KpqS)。特别是在分析复杂文档或在教育领域处理重要信息时，AI 的错误答案可能是致命的[FACTS Grounding：评估大语言模型事实性的新基准...](https://www.asugsvsummit.com/schedule/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)。**简单来说**，错误的信息不仅仅是一个插曲，还可能导致业务决策失败或学习偏差。

为了提高业务效率并更安全地使用人工智能，必须有一个工具来衡量 AI 不仅仅是“说得好”，而是“在多大程度上准确遵循了所提供的依据 (Grounding)”[评估 AI 的事实准确性：语言模型的新基准](https://www.elevateaiconsulting.com/post/evaluating-factual-accuracy-in-ai-new-benchmark-for-language-models)。此次发布的 FACTS Grounding 正是扮演了这一角色，有望成为行业的新标杆[FACTS 基准套件提升了对 LLM 事实性的审查](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny)。

## 为 AI 准备的“超精细开卷考试”

如果打个比方，FACTS Grounding 可以说是给 AI 的**“超精细开卷考试”**。这与我们考试时把课本放在旁边寻找正确答案类似。

考试方式如下：首先给 AI 一份非常长的文档（最多 32,000 Token，约相当于一本书的一大部分）。然后根据该文档内容提出需要详细回答的问题[FACTS Grounding 排行榜：衡量 LLM 的依据能力...](https://arxiv.org/abs/2501.03200)。AI 必须读完这篇长文，且不能根据自己已有的知识，而必须**仅在提供的文档中**寻找依据来撰写回答[FACTS Grounding 排行榜 - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)。

在此过程中，核心有以下两点：
1. **依据 (Grounding，明确提供回答的根据)**：回答的所有内容是否都基于提供的输入信息？[FACTS Grounding - 评估依据的前沿基准...](https://www.aibase.com/tool/35169)
2. **防幻觉**：是否随意编造了文档中没有的内容？[FACTS Grounding：评估大语言模型事实性的新基准...](https://news-tech.io/en/news/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language)

通过这一由总共 1,719 个示例问题组成的测试，非常仔细地推敲 AI 的“真实性”[FACTS Grounding 排行榜 - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)。

## 谁来打分？“由 AI 教授组成的评审团”

令人惊讶的是，这项苛刻考试的评分并不是由人直接完成的。Google DeepMind 团队任命了三种最先进的 AI 模型作为“评委”。

*   **Google 的 Gemini 1.5 Pro**
*   **OpenAI 的 GPT-4o**
*   **Anthropic 的 Claude 3.5 Sonnet**

这三位“AI 教授”组成一个团队，自动评估其他 AI 给出的答案与文档的一致程度，以及是否混入了谎言[FACTS Grounding：评估大语言模型事实性的新基准...](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)。通过来自不同公司的最高性能模型进行交叉验证，提高了评估的公平性和准确性。如果是人来评分，可能需要数月时间处理海量内容，而 AI 则能精准且迅速地完成。

## 现状：实时公开的 AI 成绩单

不仅仅是公开了测试卷。Google DeepMind 还建立了一个**“在线排行榜 (Leaderboard)”**，实时显示全球各种 AI 模型在这次考试中的得分[FACTS Grounding：评估大语言模型事实性的新基准...](https://news-tech.io/en/news/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language)。

通过这个排行榜，任何人都可以查看哪个模型更善于总结信息，哪个模型产生的幻觉现象更少[FACTS Grounding 排行榜：衡量 LLM 的依据能力...](https://arxiv.org/abs/2501.03200)。这不仅仅是为了排名，今后它将成为企业根据自身目的选择最准确 AI 的客观标准。

## 未来展望：从“智能”到“信任”

Google DeepMind 的 FACTS 团队解释说，该项目是“为了衡量 AI 模型利用源材料的准确程度以及避免虚假信息而迫切需要的工具”[FACTS Grounding：评估大语言模型事实性的新基准...](https://news-tech.io/en/news/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language)。

以后，为了在这个排行榜上获得更高分，AI 开发商将不仅仅致力于使句子流畅，而是会投入更多努力来提高“基于事实的准确性”[FACTS 基准套件提升了对 LLM 事实性的审查](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny)。最终，我们离这样的场景又近了一步：当我们使用的聊天机器人该说“不知道”时会诚实地说不知道，而说“这是事实”时则能提供可靠的依据。

---

### AI 视角
**MindTickleBytes AI 记者的视角**
如果说之前的 AI 是“口才出众的社交达人”，那么现在正是其转型为“拿证据说话的缜密专家”的时候。我认为 FACTS Grounding 作为一个指标，开始为 AI 的“诚实度”而非仅仅是智力打分，这展示了技术的成熟。未来，市场的主流将不再仅仅是聪明的 AI，而是用户可以放心交付任务的“负责任的 AI”。

---

## 参考资料
1. [FACTS Grounding：评估大语言模型事实性的新基准...](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)
2. [FACTS Grounding：评估大语言模型事实性的新基准...](https://www.linkedin.com/posts/michaelyung_facts-grounding-a-new-benchmark-for-evaluating-activity-7275106400496709633-dJed)
3. [FACTS Grounding：评估大语言模型事实性的新基准...](https://news-tech.io/en/news/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language)
4. [FELM：大语言模型事实性评估基准。Advances in Neural Information Processing Systems, 36, 2024b.](https://arxiv.org/pdf/2501.03200)
5. [FACTS 基准套件发布用于评估事实性... - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)
6. [FACTS Grounding - 评估依据的前沿基准...](https://www.aibase.com/tool/35169)
7. [FACTS Grounding：评估大语言模型事实性的新基准...](https://www.linkedin.com/posts/deepakchaubey_facts-grounding-a-new-benchmark-for-evaluating-activity-7275894260241985536-KpqS)
8. [FACTS Grounding 排行榜：衡量 LLM 的依据能力...](https://arxiv.org/abs/2501.03200)
9. [FACTS Grounding 排行榜 - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)
10. [FACTS Grounding：评估大语言模型事实性的新基准...](https://www.asugsvsummit.com/schedule/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)
11. [评估 AI 的事实准确性：语言模型的新基准](https://www.elevateaiconsulting.com/post/evaluating-factual-accuracy-in-ai-new-benchmark-for-language-models)
12. [FACTS 基准套件提升了对 LLM 事实性的审查](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny)