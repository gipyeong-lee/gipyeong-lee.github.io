---
layout: post
title: "AI能一次性做出复杂决策？Perplexity“Decider v1.3”的秘密"
description: "轻松了解Perplexity发布的开源权重多模态决策模型“Decider v1.3”的性能、分类与提取能力及商业应用方法。"
summary: "Perplexity发布了开源权重多模态决策模型“Decider v1.3”和“Decider Flash v1.3”，可一次性执行分类、路由、评分和信息提取。"
tags: [Perplexity, Decider, AI Models, Multimodal, Open-weight]
image: 2026-11-15-Perplexity-Decider-v13-Training-eval-and-use-cases.jpg
image_alt: "表现一目了然分析和分类各种数据与文档的人工智能决策模型概念图的插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Decider v1.3表明，AI正在超越单纯的对话伙伴，演变为直接执行企业复杂决策和数据分类任务的强大实务合作伙伴。"
quiz:
  - question: "Perplexity此次发布的决策模型v1.3系列的特点中，正确的是？"
    choices: ["只能处理文本", "一次性执行分类、评分和信息提取", "输入数据必须在中间被截断（Truncation）"]
    answer: 1
    explanation: "Decider v1.3是一个多模态决策模型，能够基于文本、结构化JSON和图像，以单次遍历（pass）处理分类、路由、评分和信息提取。"
  - question: "Decider v1.3在63个查询分类任务中记录的平均准确率是多少？"
    choices: ["81.2%", "91.6%", "99.4%"]
    answer: 1
    explanation: "在更大的模型标准下，其在63个查询分类任务中记录了91.6%的平均准确率，证明了优于自有生产分类器的性能。"
  - question: "作为Decider v1.3新增的核心功能之一，直接从文本中精准指出特定信息的能力是什么？"
    choices: ["定位（Locate）", "翻译（Translate）", "编译（Compile）"]
    answer: 0
    explanation: "Decider v1.3通过新引入的“定位（Locate）”功能，具备了直接从文本中提取特定信息的能力。"
lang: zh-cn
ref: 2026-11-15-Perplexity-Decider-v13-Training-eval-and-use-cases
---

想象一下。在涌入数千起客户咨询、文件和图像的大型客服中心里，负责员工每次都要对这究竟是退款请求、简单咨询还是紧急投诉进行分类并评分，累得筋疲力尽。然而，人工智能登场了，它能在短短几秒钟内比人类更准确地完成这项复杂而枯燥的判断工作。这就是[Perplexity（基于AI的搜索和对话平台）](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)公开的开源权重（Open-weight，任何人都可以查看内部结构并加以利用的公开权重模型）多模态（Multimodal，同时理解文本、图像、声音等多种形态数据的技术）决策模型**“Decider v1.3”**和**“Decider Flash v1.3”**的故事 [Source 2, Source 7]。

在本文中，我们将逐步探讨Perplexity推出的这款全新决策AI为何备受瞩目，以及它将给我们的日常生活和商业带来怎样的变化。

---

## 为什么这很重要？

企业将AI引入商业时最头疼的痛点是“判断和决策”。打个比方，这就如同在一个巨大的工厂里，为了逐一手动检查无数零部件的缺陷与否而停工一样。为了回答“这封电子邮件是垃圾邮件吗？”、“该客户提交的文件符合规定吗？”、“这件商品评价是好评还是差评？”等问题，以往必须将不同的程序进行复杂的组合。

然而，[Perplexity的Decider v1.3](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)在63个查询分类（Query-classification，按类型划分用户问题或请求意图的任务）任务中记录了**91.6%的平均准确率**，证明了比其以往生产分类器高出6.54个百分点的性能 [Source 2]。 

由于它不仅能阅读文本并回答，还能通过单次遍历处理**分类（Classification）、评分（Scoring）和信息提取（Extraction）** [Source 4, Source 6]，企业能够以更低的成本构建更快、更准确的自动化系统。

---

## 轻松理解：Decider v1.3是如何工作的？

简单来说，Decider v1.3可以比作**“超高速法官”**或**“大型图书馆的天才图书管理员”**。 

该模型一次性接收文本、结构化JSON（用于存储和交换数据的轻量级文本格式）、甚至图像等各种形态的资料 [Source 6]。并且根据是/否问题、用户预先设定的自定义选项、带顺序的评分标准（Rubric），进行彻底审查后输出概率值以及打字输入的正确答案 [Source 6]。

### 用比喻来看核心功能
- **X射线安检仪**：正如机场安检仪扫描行李一样，Decider v1.3在庞大的数据中毫无误差地挑选出违规项或特定项目。
- **全新的“定位（Locate）”功能**：新增了直接从文本中精准指出特定信息的能力 [Source 1, Source 7]。这项技术就像在巨大的百科全书里用美工刀精准裁切出写有特定单词的页面一样。

所有这些过程都在一个模型内部有机地发生，这是与现有AI最大的区别 [Source 4, Source 6]。

---

## 当前现状：进展到什么地步了？

[Perplexity Decider v1.3](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)是继承了前代版本v1、v1.1、v1.2以及Flash v1.2优秀血统而诞生的最新模型 [Source 2]。目前了解到的技术特征和规格如下：

1. **强大的多模态处理**：不仅能同时评估文本，还能评估图像和结构化数据 [Source 6]。
2. **庞大的上下文窗口**：提供高达**256K（约25.6万个）**的超大上下文窗口（Context window，AI单次能记忆和处理的信息量），可以将整本书的分量直接放入并进行分析 [Source 6]。
3. **输入数据的无损保存**：在训练过程中使用了长达**30,720个token（Token，AI阅读和处理句子的基本单位）**的序列，坚持绝不在中间截断（Truncation）输入数据的原则 [Source 9]。
4. **灵活的问题限制**：问题数量没有固定限制，在允许的长度范围内可以一次性抛出大量问题 [Source 9]。

开发者和企业可以通过OpenRouter或Vercel AI Gateway等平台轻松测试该模型并以API形式调用 [Source 6, Source 8]。

---

## 未来会如何发展？

随着[Perplexity](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)以开源权重模型形式全面开放[Decider v1.3和Decider Flash v1.3](https://lapaasvoice.com/perplexity-open-sources-decider-v1.3-and-decider-flash-v1-3-with-new-locate-feature/) [Source 2, Source 7]，预计未来无数企业和开发者将在各自的服务中移植这一“智能判断引擎”。

在客服中心的自动分类系统、大规模合同及法律文件审查、实时内容审核等“准确判断”决定商业成败的领域，Decider v1.3有望成为核心基础设施。AI不仅能说会道，更在飞速演变为真正的“高效能参谋”。

---

## AI的视角

MindTickleBytes的AI记者视角：AI的发展不仅超越了单纯的擅长写作，更向着做出“正确判断”的精密性演进。Decider v1.3证明了AI不仅是个健谈者，更能成为在商业最苛刻决策者身边工作的可靠参谋。

---

## 参考资料

1. [Perplexity Decider v1.3: Training, eval, and use cases](https://www.perplexity.ai/hub/blog/perplexity-decider)
2. [Perplexity Ships Decider v1.3 Classifier, 91.6% on 63 Tasks](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)
3. [Perplexity's Decider v1.3 lets one model · 21 HN comments | Zeli](https://zeli.app/story/50488464)
4. [Decider v1.3: Release, Decision Index Score, Performance ...](https://artificialanalysis.ai/decision-models/pplx-decider-v1-3)
5. [Decider V1.3 API, Pricing & Playground | Vercel AI Gateway](https://vercel.com/ai-gateway/models/pplx-decider-v1.3)
6. [Perplexity Open-Sources Decider v1.3 and Decider Flash v1.3 ...](https://lapaasvoice.com/perplexity-open-sources-decider-v1-3-and-decider-flash-v1-3-with-new-locate-feature/)
7. [DeciderV1.3(free) - API Pricing & Providers | OpenRouter](https://openrouter.ai/perplexity/pplx-decider-v1.3:free)
8. [perplexity-ai/pplx-decider-v1.3 · Hugging Face](https://huggingface.co/perplexity-ai/pplx-decider-v1.3)
9. [Perplexity Decider v1.2 27B Benchmarks & Pricing | BenchLM.ai](https://benchlm.ai/models/pplx-decider-v1.2)
10. [How To Use Decision Models for Evals – Hamel’s Blog](https://hamel.dev/blog/posts/decision-model-evals/)
11. [Perplexity Decider V1.2 API Pricing & Benchmarks | LMSpeed](https://lmspeed.net/model/pplx-decider-v1.2)