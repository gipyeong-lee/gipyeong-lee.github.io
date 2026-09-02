---
layout: post
title: "AI医师写的诊疗记录，真的可信吗？AI无法察觉‘缺失信息’的盲点"
description: "探究为何评估AI诊疗记录准确性的AI裁判难以发现信息缺失的事实，分析其背后的原因与局限性。"
summary: "AI诊疗记录助手生成的文档中常出现“遗漏（Omission）”错误，但负责评估的AI裁判往往只能核实“现有信息”，在寻找“缺失信息”方面表现出明显局限。"
tags: [AI, 医疗AI, 诊疗记录, LLM, 技术分析]
image: 2026-09-02-LLM-Judges-Verify-Presence-Not-Absence-Omission-Blindness-in-AI-Clinical-Notes.jpg
image_alt: "用放大镜查看AI撰写的诊疗记录文档，象征性地表现了AI的评估能力。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "盲目信任AI的评估能力是非常危险的。必须认识到，区分“存在”与“不存在”是完全不同维度的智能。"
quiz:
  - question: "研究结果显示，AI裁判最擅长发现哪种类型的错误？"
    choices: ["信息遗漏 (Omission)", "幻觉 (Hallucination)", "核实现有信息"]
    answer: 2
    explanation: "AI裁判擅长核实记录中包含的信息（即“存在”），但在查找缺失信息（即“缺失”）方面存在困难。"
  - question: "诊疗记录助手AI生成的文档中最常见的错误是什么？"
    choices: ["信息遗漏 (Omission)", "幻觉 (Hallucination)", "拼写错误"]
    answer: 0
    explanation: "环境AI（Ambient AI）生成的诊疗记录中最普遍的错误是重要信息未被记录的遗漏错误。"
  - question: "AI裁判（LLM-as-a-judge）在检测信息遗漏时的表现如何？"
    choices: ["人类水平", "非常出色", "与随机概率相当 (Chance levels)"]
    answer: 2
    explanation: "研究表明，在检测信息的缺失时，AI裁判的表现仅相当于随机猜测。"
lang: zh-cn
ref: 2026-09-02-LLM-Judges-Verify-Presence-Not-Absence-Omission-Blindness-in-AI-Clinical-Notes
---

想象一下：你去医院看病，与医生进行了深入交流。诊疗结束后，AI助手为你写好了诊疗记录。仔细阅读后，你觉得医生说的话都被总结得很到位，于是感到放心。但是，如果医生提到的“从昨天开始出现的胸痛”这一关键信息被漏掉了呢？根据这份不完整的记录开具处方，真的安全吗？

近年来，在医疗现场，能够听取医生与患者对话并自动撰写诊疗记录草稿的“环境AI（Ambient AI，诊疗现场记录助手）”应用日益广泛。虽然带来了极大便利，但重要信息被意外忽略的“遗漏（Omission）”错误，依然是一个亟待解决的难题。[参考 12](https://arxiv.org/abs/2608.31016) 今天，我们就来浅显易懂地剖析一下，为解决该问题而引入的“AI裁判”为何并不像想象中那么聪明，以及它背后的原因与局限。

## 为什么这很重要？

在医疗领域，诊疗记录是维护患者健康最基础且最核心的数据。一旦记录中漏掉关键症状，可能会导致医生误诊或处方错误。为了防止这种情况，医院引入了AI作为裁判（LLM-as-a-Judge）来检查记录。[参考 10](https://www.linkedin.com/posts/catherine-chen-5851a6a0_continual-monitoring-of-note-quality-at-scale-activity-7496283957693448192-ksR_) 

但如果连这位“AI裁判”都无法准确发现遗漏的信息，后果会怎样呢？医疗事故的风险依然存在，而我们所使用的AI助手实际上在制造“漏洞百出的记录”，且评估系统也无法发现这些漏洞，这无疑将我们置于极其严重的境地。

## 通俗理解：没有“标准答案”的试卷评分

AI裁判为何找不到缺失的信息？我们可以用“试卷评分”来打比方。

把AI裁判想象成“手握标准答案、为学生试卷打分的老师”。

*   **存在核实（Presence）：** 确认学生是否在答题纸上写了“1题答案是A”非常容易。因为答题纸上可以清楚地看到“A”这个字。AI在确认特定关键词是否包含在记录中方面，能力非常出色。[参考 2](https://arxiv.org/pdf/2608.31016)
*   **缺失核实（Absence）：** 相反，老师要确认“学生是否漏写了应该写的内容”，则是完全不同维度的挑战。因为要找出学生没写的内容，必须在脑海中完整呈现整份标准答案，并将试卷上的每一行与标准答案进行逐一对比。

根据最近的“OmissionBench”项目结果，AI裁判虽然能强有力地核实记录中“包含了什么”，但在寻找“漏掉了什么”时，表现出的性能几乎与随机猜测（chance levels）相当。[参考 3](https://github.com/composo-ai/omission-bench), [参考 13](https://arxiv.org/html/2608.31016v1) 换言之，AI只能看到记录所呈现的“结果”，却缺乏感知记录中未被记载的“空白区域”的能力。学术界将此称为“遗漏盲点（Omission Blindness）”。

## 现状如何？

目前，许多医疗AI系统已经在利用AI裁判来评估诊疗记录的质量。[参考 10](https://www.linkedin.com/posts/catherine-chen-5851a6a0_continual-monitoring-of-note-quality-at-scale-activity-7496283957693448192-ksR_) 但其现实性能却很冷峻。研究结果显示，实际上AI撰写的诊疗记录中，约有3.45%包含信息遗漏错误（幻觉错误为1.47%）。[参考 18](https://www.nature.com/articles/s41746-025-01670-7) 

问题在于，本应过滤掉这些遗漏的AI裁判只能看到“存在”，却看不到“缺失”。[参考 2](https://arxiv.org/pdf/2608.31016) 甚至负责评估的AI与生成记录的AI思维方式相似，导致其重复同样的错误，或者直接将错误放过。[参考 4](https://www.youtube.com/watch?v=BPXFDC7WHSk)

## 未来会怎样？

随着AI裁判的局限性变得愈发明确，业界正在进行多种尝试来克服这一瓶颈：

1.  **引入确定性验证工具：** 不再仅依赖AI的判断，而是结合使用诸如检查必要关键词等、由简单且确定的代码编写的规则。[参考 4](https://www.youtube.com/watch?v=BPXFDC7WHSk)
2.  **多重评估体系：** 不再只依靠一名AI裁判，而是利用多个模型或多智能体系统进行信息交叉验证。[参考 14](https://www.nature.com/articles/s41746-025-02005-2)
3.  **人类参与：** 归根结底，在安全性至上的医疗领域，与其让AI进行所有评估，由人类专家（医生）最终核实AI的审查结果的“以人为中心的评估”依然是最重要的核心。[参考 17](https://arxiv.org/html/2607.18828)

我们现在已经到了不仅仅要看AI“能做什么”，更要仔细审视它“漏掉了什么”的阶段。

## MindTickleBytes AI记者视角

将AI作为裁判确实方便，但区分“存在”与“缺失”是智力层面上截然不同的维度。对于无法读懂未被记载的“沉默”的AI，我们将健康完全托付给它还为时尚早。

## 参考资料
1. [2608.31016] LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes and What Recovers It (https://arxiv.org/abs/2608.31016)
2. LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes and What Recovers It (https://arxiv.org/pdf/2608.31016)
3. GitHub - composo-ai/omission-bench: OmissionBench harness: code (https://github.com/composo-ai/omission-bench)
4. Replace Your LLM Judge With 10 Lines of pytest - YouTube (https://www.youtube.com/watch?v=BPXFDC7WHSk)
5. LLM-as-a-judge: a complete guide to using LLMs for evaluations (https://www.evidentlyai.com/llm-guide/llm-as-a-judge)
7. LLM-as-a-Judge Simply Explained: The Complete Guide (https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)
8. Position Bias in LLM Judges: Measurement and Mitigation (https://mbrenndoerfer.com/writing/position-bias-in-llm-judges)
9. LLMs bow to pressure, changing answers when challenged (https://www.computerworld.com/article/4023989/llms-bow-to-pressure-changing-answers-when-challenged-deepmind-study.html)
10. Continual Monitoring of Note Quality At Scale (https://www.linkedin.com/posts/catherine-chen-5851a6a0_continual-monitoring-of-note-quality-at-scale-activity-7496283957693448192-ksR_)
11. LLM Judges Are Unreliable (https://www.cip.org/blog/llm-judges-are-unreliable)
12. LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes (https://arxiv.org/abs/2608.31016v1)
13. LLM Judges Verify Presence, Not Absence (https://arxiv.org/html/2608.31016v1)
14. Evaluating clinical AI summaries with large language models as judges (https://www.nature.com/articles/s41746-025-02005-2)
17. Evaluating medical AI under missing information (https://arxiv.org/html/2607.18828)
18. A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation (https://www.nature.com/articles/s41746-025-01670-7)