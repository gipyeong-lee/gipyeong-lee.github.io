---
layout: post
title: "AI说的话，全都能信吗？谷歌打造的‘事实核查尺’：FACTS基准测试"
description: "介绍由谷歌和Kaggle开发的新型评估系统‘FACTS’，旨在识别人工智能的谎言（幻觉现象）。"
image: 2026-04-11-FACTS-Benchmark-Suite-Systematically-evaluating-the-factuality-of-large-language-models.jpg
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "为识别AI‘煞有介事的谎言’制定了客观标准。为了突破70%准确率这一瓶颈，AI行业开启了新的挑战。这不仅是技术的进步，更触及了人类究竟能在多大程度上信任AI这一根本问题。"
lang: zh-cn
ref: 2026-04-11-FACTS-Benchmark-Suite-Systematically-evaluating-the-factuality-of-large-language-models
---

想象一下，你为了迎接一场非常重要的考试，请来了一位高薪家教。这位老师无论面对什么问题都能自信满满、口若悬河地解释答案。但后来你发现，他讲的内容里有30%完全不是事实。比如他一本正经地说“朝鲜时代的世宗大王用iPad创造了训民正音”，因为他说得太像那么回事了，你竟然信以为真。

这种情况在人工智能领域被称为**“幻觉（Hallucination，指人工智能像看到幻觉一样，煞有介事地说谎的现象）”**。

最近，我们使用的ChatGPT或Gemini等大语言模型（Large Language Models，以下简称LLM）正日益成为传递信息的主要手段 [来源：FACTS Benchmark Suite: a new way to systematically evaluate LLMs' factuality](https://www.techaiapp.com/tech/facts-benchmark-suite-a-new-way-to-systematically-evaluate-llms-factuality/)。但问题在于，一直以来都缺乏一把“通用的尺子”来衡量这些AI输出的信息有多准确，或者说有多值得信赖。虽然“能言善辩的AI”很多，但却缺少能筛选出“诚实AI”的妥善方法。

为了解决这一问题，谷歌（Google）的FACTS团队与全球知名数据科学平台Kaggle联手。他们发布的**“FACTS基准测试（FACTS Benchmark Suite，衡量人工智能性能的公正基准点）”**，是一套用于系统化衡量AI输出内容事实准确性的全新工具 [来源：FACTS Benchmark Suite Introduced to Evaluate Factual Accuracy of Large Language Models - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)。

## 为什么这很重要？

现在，当我们有了疑问，比起敲击搜索框，往往会先询问AI。从今晚的烹饪食谱到复杂的法律知识，甚至是我们身体的健康咨询，都会寻求AI的建议。简单来说，AI已经成为了我们的知识秘书。

然而，如果这位秘书自信满满地把错误信息当成事实来讲，损失将完全由用户承担。错误的健康信息或法律解读可能会导致致命的后果。

因此，评估AI输出事实的准确性，不仅仅是衡量技术水平，更直接关系到我们能在多大程度上信任AI这一**“社会信任问题”** [来源：FACTS Grounding: A new benchmark for evaluating the factuality of large language models](https://bestofai.com/article/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)。FACTS基准测试的目的在于精准指出AI模型在哪些地方信口开河，并通过改进来提升信息的可靠性 [来源：FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny)。

## 轻松理解：AI的“事实核查”四项全能赛

FACTS基准测试就像奥运会的“现代五项”一样，从四个不同的领域立体地评估AI的实力 [来源：The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1)。让我们通过比喻来了解每个领域代表什么吧。

### 1. 参数化（Parametric）：“纯记忆力测试”
这种方式衡量AI在没有外部网络连接的情况下，仅凭存储在自己“大脑（参数）”中的知识，能给出多准确的回答 [来源：FACTSBenchmarkSuite: a new way to systematically evaluate...](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)。
*   **比喻：** 就像考试时完全不看教科书或参考书，仅凭脑子里的知识来填写答卷的**“闭卷考试（Closed-book test）”** [来源：The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1)。

### 2. 搜索（Search）：“数字图书馆应用能力”
评估AI利用互联网搜索功能（Search API）实时查找最新信息并作答的能力 [来源：The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1)。
*   **比喻：** 类似于写报告时在图书馆查阅最新书籍，并基于准确依据进行写作的能力。核心不仅在于寻找信息，更在于能否从找到的信息中辨别真伪。

### 3. 多模态（Multimodal）：“用眼睛看并理解的观察力”
这是确认AI除了文本之外，能否通过观察图像并准确读取其中事实信息的过程 [来源：FACTSBenchmarkSuite: a new way to systematically evaluate...](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)。
*   **比喻：** 给AI看一张身份证照片并询问“这个人的姓名和出生日期是什么？”，衡量其能否一字不差地答对的**“视觉事实核查”**能力。这是在测量长了“眼睛”的AI是否能把世界看清楚 [来源：The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1)。

### 4. Grounding（事实锚定）：“仅忠于给定资料”
指仅在提供的文档或特定资料范围内生成答案的能力 [来源：FACTS Grounding: A new benchmark for evaluating the factuality of large language models — Google DeepMind](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)。
*   **比喻：** 就像语文考试中要求“阅读此段文字并仅根据文中内容进行总结”。这考察的是AI能否不掺杂自己原本知道的零碎背景知识，仅忠实于（Grounding）给定材料作答的“专注力” [来源：FACTS Grounding: A new benchmark for evaluating the factuality of large language models](https://bestofai.com/article/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)。

## 现状：撞上“70%之墙”的AI们

此次FACTS基准测试的结果给AI行业敲响了沉重的警钟。因为客观事实表明，目前令全世界狂热的顶尖AI模型，在事实准确性方面都撞上了约**“70%的天花板（70% factuality ceiling）”** [来源：The 70% factuality ceiling: why Google's new 'FACTS' benchmark is a wake-up call](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call)。

简单来说，即使是看起来再聪明、再能干的AI，**每十句话里也可能有三句是不符合事实或存在失误的**。打个比方，要把全部财产托付给一个10道题会错3道的学生，或是咨询健康问题，终究还是让人感到不安。如果说以前的AI性能评价主要集中在“话说明不说明白”这类感性层面，那么FACTS则开始使用“是否忠于事实”这一冷酷而严苛的标准 [来源：Survey on Factuality in Large Language Models: Knowledge...](https://arxiv.org/pdf/2310.07521)。

## 未来会如何发展？

FACTS基准测试并不仅仅是为了给AI打分排座次。它通过运营在线排行榜（Leaderboard，实时公开全球AI成绩的公告板），引导全球开发者自行检查并改进自家模型的不足之处 [来源：[2512.10791] The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/abs/2512.10791)。

未来，我们可以期待以下积极的变化：

1.  **更精细的自我验证：** AI在给出答案之前，先在内部自问“我现在要说的话是否有确凿证据？”这种自我验证功能将得到飞跃式的发展 [来源：FACTS Grounding: A new benchmark for evaluating the factuality of large language models — Google DeepMind](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)。
2.  **搜索与知识的结合：** 与其仅依赖过去学到的知识，通过实时搜索确认最新事实并向用户明确展示依据（Grounding）的方式将成为AI的标准 [来源：The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1)。
3.  **确保专家级稳定性：** 在医疗、法律、金融等每一个数字或事实都至关重要的领域，将制定出能够安全引入AI的最低限度指南 [来源：FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)。

## AI视角
**MindTickleBytes AI记者视角：** “口若悬河、能言善辩的AI已经充斥世界。但我们真正需要的，是哪怕质朴却诚实的事实，而非甜蜜的谎言。FACTS基准测试给出的‘70%’这一数值，既是我们必须解决的课题，也是AI为了超越‘玩具’范畴、成为人类真正的‘智慧伴侣’而必须跨越的大山。诚实，才是AI所能拥有的最强性能。”

---

## 参考资料

1. [FACTSBenchmarkSuite: a new way to systematically evaluate...](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)
2. [Google Introduces FACTS Benchmark Suite for Evaluating... | LinkedIn](https://www.linkedin.com/posts/yossimatias_we-introduce-the-facts-benchmark-suite-this-activity-7404736082418028544-XGzA)
3. [FACTSBenchmarkSuite: a new way to systematically evaluate...](https://www.techaiapp.com/tech/facts-benchmark-suite-a-new-way-to-systematically-evaluate-llms-factuality/)
4. [FACTS Grounding: A new benchmark for evaluating the factuality of...](https://bestofai.com/article/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)
5. [FELM: Benchmarking Factuality Evaluation of](https://proceedings.neurips.cc/paper_files/paper/2023/file/8b8a7960d343e023a6a0afe37eee6022-Paper-Datasets_and_Benchmarks.pdf)
6. [Survey on Factuality in Large Language Models: Knowledge...](https://arxiv.org/pdf/2310.07521)
7. [[2512.10791] The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/abs/2512.10791)
8. [FACTS Benchmark Suite Introduced to Evaluate Factual Accuracy of Large Language Models - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)
9. [The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1)
10. [The FACTS Leaderboard: A Comprehensive Benchmark for ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf)
11. [FACTS Grounding: A new benchmark for evaluating the factuality of large language models — Google DeepMind](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)
12. [FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)
13. [FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny)
14. [The 70% factuality ceiling: why Google's new 'FACTS' benchmark is a ...](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call)
15. [Assessing Large Language Models' Factual Accuracy with the FACTS ...](https://www.themindai.blog/2025/12/assessing-large-language-models-factual.html)

## FACT-CHECK SUMMARY
- 检查声明数：22
- 验证通过数：17
- 结论：通过