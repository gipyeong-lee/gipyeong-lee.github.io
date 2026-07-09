---
layout: post
title: "AI 编程能力，需要从考试题开始重新审视？OpenAI 的决断"
description: "OpenAI 停止推荐作为 AI 编程能力评估标准的“SWE-Bench Pro”。由于在题目本身发现了错误，AI 性能评估的可靠性敲响了警钟。"
summary: "OpenAI 在被视为衡量 AI 编程能力主要指标的 SWE-Bench Pro 中发现了约 30% 的错误，并停止了对其的使用推荐。"
tags: [AI, 编程, 开发, OpenAI, SWE-Bench]
image: 2026-07-09-OpenAI-no-longer-recommends-SWE-Bench-Pro.jpg
image_alt: "在代码片段和 AI 图标交织的背景上，浮现出象征考题错误的警告标记。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "随着 AI 技术的高速发展，用于衡量这些技术的“考试”其严谨性往往难以跟上步伐。开发者亲手进行验证的时代正在到来。"
quiz:
  - question: "OpenAI 停止推荐使用 SWE-Bench Pro 的最大原因是什么？"
    choices: ["AI 能力太强了", "公开的任务课题中约 30% 构建不当", "所有 AI 已经都能拿满分了"]
    answer: 1
    explanation: "OpenAI 表示，SWE-Bench Pro 的公开任务课题中约有 30% 无法正常运行，导致结果不可信。"
  - question: "SWE-Bench Verified 为何会先被停止使用？"
    choices: ["使用费用太贵", "开发者人数不足", "数据污染以及考试题目本身的缺陷"]
    answer: 2
    explanation: "除了数据污染问题外，经审查发现约 60% 的题目在结构上存在缺陷，因此被停止使用。"
  - question: "开发 SWE-Bench Pro 的公司是哪一家？"
    choices: ["Google", "Scale AI", "Microsoft"]
    answer: 1
    explanation: "SWE-Bench Pro 由 Scale AI 开发，于 2025 年 9 月发布。"
lang: zh-cn
ref: 2026-07-09-OpenAI-no-longer-recommends-SWE-Bench-Pro
---

想象一下：你去参加一场至关重要的数学考试，结果发现试卷上的答案错了，或者题目本身逻辑不通，完全无法解答。无论学生多么努力地解题，都无法准确评估自己的真实水平。最近 AI 行业围绕“编程考试”引发的争议，情况正是如此。

OpenAI 过去一直积极推荐将“SWE-Bench Pro”作为衡量 AI 软件工程能力的工具。然而，OpenAI 最近判断，该考试题目中约有 30% 构建不当，无法保证结果的可靠性。因此，OpenAI 宣布不再将其作为官方评估标准进行推荐 [Source 3, Source 11, Source 4]。

### 为什么这很重要？

我们每天使用的智能手机应用、银行系统、新闻服务等，都是由开发者编写的代码驱动的。因此，AI 的编程能力如何，是决定我们日常生活中接触到的技术能变得多“聪明”的关键指标。

如果衡量这种“编程能力”的考题毫无用处，会发生什么呢？AI 公司一直利用这些考试成绩来证明自家模型更优秀。如果考试本身就错了，可能会导致性能被夸大，或者无法得到公正的评估，得出扭曲的结果。这会带来很大的风险，让消费者误判 AI 技术进步的实际水平。

### 通俗解释：AI 编程考试的秘密

编程考试通常通过“单元测试（Unit Test，即验证特定功能代码执行是否正确的自动化检查）”来评分。例如，针对“请实现按这个按钮时切换屏幕”的问题，AI 编写代码，如果通过了测试，则被判定为正确。

打个比方，这就好比举办厨艺大赛，评委们声称要测量“汤汁的浓度”，结果发现他们定下的标准竟然是一个错误的温度计。无论厨师（AI）做出多么出色的料理，因为错误的温度计，要么导致实力被低估，要么反过来给奇怪的料理打高分，性质是一样的。

OpenAI 之前也使用过名为“SWE-Bench Verified”的评估工具。但该工具同样被停止使用，原因在于数据污染问题，以及经查证发现约 59% 的题目存在结构性缺陷 [Source 2, Source 8, Source 13, Source 9]。

此次被停止推荐的 SWE-Bench Pro，由于其题目是基于 GitHub（开发者共享代码的平台）上实际存在的复杂议题构建的，也一直被批评为任务本身的性质对 AI 单独求解而言过于模糊且零碎 [Source 3, Source 14]。

### 当前现状：在泥潭中寻找珍珠

目前 AI 模型正在飞速发展。然而，衡量其性能的指标尚未具备符合“AI 时代”的完善度 [Source 6, Source 14]。

SWE-Bench Pro 是 Scale AI 公司于 2025 年 9 月发布的，该公司试图通过应用比以往更强大的版权许可来最大限度地减少数据污染 [Source 7, Source 8]。但通过这次发布可以看出，无论尝试设计得多么精巧，想要将实际开发环境的复杂性完美地转换成自动化考试，是一件多么困难的事情。

Scale AI 的研究负责人 Bing Liu 指出，这次决定很好地体现了任务的模糊性、数据污染以及仅靠狭义的单元测试无法完美衡量 AI 能力的局限性 [Source 14]。

### 未来会怎样？

未来，评估 AI 编程能力的方式将经历根本性的变革。

1. **更精细的评估标准**：业界将不再仅仅依赖自动化的分数，而是致力于建立能够更综合地判断 AI 解决问题的“过程”和“复杂度”的新标准 [Source 12]。
2. **强调与开发者的协作**：重点将不再仅仅是 AI 独立写代码，而是评估实际开发者如何与 AI 沟通并解决问题。
3. **持续的验证**：如何管理评估数据本身不被污染，将成为与开发 AI 模型同等重要的“基础科学”领域。

我们现在正生活在一个 AI 自主编写代码的时代。但这次事件提醒我们，制作能够准确评估这一能力的“温度计”，是与技术进步同样重要的课题。

---

## 参考资料

1. [OpenAI Abandons SWE-Bench Verified, Citing Widespread Data Contamination and Flawed Tests](https://www.siliconreport.com/openai-abandons-swe-bench-verified-citing-widespread-data-contamination-and-flawed-tests-6ebd9b34)
2. [OpenAI Retracts Recommendation To Use SWE Bench Pro As Coding Eval Over 30% Broken Tasks](https://officechai.com/ai/openai-retracts-recommendation-to-use-swe-bench-pro-as-coding-eval-over-30-broken-tasks/)
3. [OpenAI no longer recommends SWE-Bench Pro as coding benchmarks saturate](https://savedelete.com/news/openai-swe-bench/)
4. [Why we no longer evaluate SWE-bench Verified - keynews.ai](https://keynews.ai/articles/290)
5. [OpenAI Drops SWE-Bench Verified: What It Means for AI](https://www.adwaitx.com/openai-swe-bench-verified-retired-ai-benchmarks/)
6. [OpenAI Abandons SWE-bench Verified: 59% Flawed Tests](https://byteiota.com/openai-abandons-swe-bench-verified-59-flawed-tests/)
7. [OpenAI Drops SWE-bench Verified Over Contamination Concerns](https://aibreakingwire.com/news/openai-ditches-swe-bench-verified-cites-critical-flaws/)
8. [OpenAI Retracts SWE-Bench Pro After Finding 30% of Tasks Broken | AlphaSignal](https://alphasignal.ai/news/openai-retracts-swe-bench-pro-after-finding-30-of-tasks-broken)
9. [OpenAI Developers on X](https://x.com/OpenAIDevs/status/2026002219909427270)
10. [OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)
11. [OpenAI moves beyond SWE-bench Verified as coding benchmarks saturate](https://tessl.io/blog/openai-moves-beyond-swe-bench-verified-as-coding-benchmarks-saturate/)