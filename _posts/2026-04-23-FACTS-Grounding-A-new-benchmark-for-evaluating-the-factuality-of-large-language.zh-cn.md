---
layout: post
title: "捕捉AI“似是而非的谎言”的严苛试卷，谷歌 FACTS 亮相！"
description: "介绍谷歌 DeepMind 发布的全新 AI 事实核查基准 FACTS Grounding。了解这款基于 32,000 token 庞大文档的验证工具，旨在解决 AI 的幻觉问题。"
summary: "谷歌 DeepMind 发布了“FACTS Grounding”基准，用于衡量 AI 在给定文档中的回答准确度和详细程度，为 AI 的可靠性树立了新标准。"
tags: [AI, 谷歌 DeepMind, FACTS, 事实核查, 人工智能, 幻觉]
image: 2026-04-23-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language.jpg
image_alt: "机器人手持放大镜在庞大的文档堆中挑选准确事实并打钩的插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这标志着 AI 从单纯的‘聪明’迈向‘值得信赖’的重要关口。确认 70% 的性能墙，体现了开发者承认技术局限并致力于精细化改进的坚定决心。"
quiz:
  - question: "FACTS Grounding 基准中 AI 需要阅读的文档最大长度是多少？"
    choices: ["1,000 token", "12,000 token", "32,000 token"]
    answer: 2
    explanation: "FACTS Grounding 基于长达 32,000 token 的长文档来测试 AI 把握事实关系的能力。"
  - question: "截至目前，顶尖模型在该基准中表现出的准确率处于什么水平？"
    choices: ["约 50%", "约 74%", "约 99%"]
    answer: 1
    explanation: "即使是顶尖模型目前也仅停留在约 74% 的准确率水平，表明仍有很大的改进空间。"
  - question: "为确保 FACTS 基准评估的公正性而引入的系统是什么？"
    choices: ["单人评审系统", "三人法官 (Judge) 系统", "随机选拔系统"]
    answer: 1
    explanation: "FACTS 框架采用由三个法官模型进行评估的系统，以提高评估的准确性和公正性。"
lang: zh-cn
ref: 2026-04-23-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language
---

想象一下，你把一份长达 50 页的重要业务报告交给 AI，并嘱咐道：“请准确提取其中最重要的 3 个数字。”AI 在一秒钟内就给出了非常自信的回答。但当你稍后亲自核对时，却发现其中一个数字在报告中根本找不到，是 AI 自行捏造的。那一刻，你可能会感到背脊发凉。

这种现象我们称之为**幻觉 (Hallucination)**，即人工智能自信地将虚假信息当作事实说出来。简单来说，就是“一本正经地胡说八道”。无论 AI 变得多么聪明，这个顽疾总是如影随形。但现在，一个严密审视 AI 是在诚实回答还是在不懂装懂的“显微镜”出现了，那就是谷歌 DeepMind 公布的 **“FACTS Grounding”**。

## 为什么这很重要？

如果我们想在日常生活中真正信任 AI，除了文字流畅，还必须有确凿的**“根据”**。特别是在总结专业医学论文或分析企业机密文档时，哪怕 AI 只说了一句谎话，也可能导致致命事故，而不仅仅是简单的失误。

谷歌 DeepMind 建立这一基准 (Benchmark) 的目的非常明确：为了确保 AI 模型生成的回答不仅能让用户满意，更要针对给定的输入数据做到**事实准确且足够详尽** [FACTS Grounding: 评估大语言模型事实性的新基准 — Google DeepMind](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)。

打个比方，这就像是训练 AI 不要成为那个靠粗略浏览互联网海量信息来充当“万事通”的搜索达人，而是要成为一名钻研老师给出的教科书并寻找正确答案的“笃实优等生”。其意图在于提升实际业务场景中对 AI 的信任度，并为将其应用于更专业的领域奠定基础 [FACTS Grounding: 评估大语言模型事实性的新基准](https://bestofai.com/article/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)。

## 通俗理解：FACTS 是一场什么样的考试？

如果用一句话定义 FACTS Grounding，那就是**“超大型开卷测试”**。但问题在于，这本“开卷”比我们想象的要厚得多、难得多。

### 1. 篇幅庞大的试卷：“读完一整本书？”
给学生 (AI) 的试卷长度高达 **32,000 token (Token，AI 处理文字的最小单位)** [FACTS Grounding 排行榜：基准测试大语言模型的落地能力 ...](https://arxiv.org/abs/2501.03200)。

你可能对 32,000 token 没有概念，简单来说，它相当于一本长达数十页的厚报告或一部中篇小说。AI 必须从头到尾一字不落地读完，然后针对用户的复杂问题给出详尽具体的回答 [FACTS Grounding 排行榜 - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)。这项测试由 **1,719 个示例**组成，设计得非常精密，AI 无法靠一两次蒙对的侥幸心理过关 [FACTS Grounding 排行榜 - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)。

### 2. 挑剔的三位法官：“公正即生命”
考试之后当然要评分。为了确保评分的公正性，FACTS 引入了**“三人法官 (Judge) 系统”** [DeepMind FACTS 框架 2026：大语言模型事实准确性指南](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy)。

由于一个人评分可能会掺杂主观判断或出现失误，因此由三位经过高度训练的人工智能法官出马。他们会仔细核实每个模型的回答是否真的以给定文档为**根据 (Grounding)**，还是在巧妙地混入从别处听来的知识，假装文档里有这些内容。

### 3. 是否“落地”：Grounding 的含义
这里的核心关键词是 **“落地 (Grounding)”**。它意味着 AI 在回答时，不是引用悬浮在半空、毫无根据的知识，而是像脚踏实地 (Ground) 一样，**紧紧依附于给定的根据文档** [FACTS Grounding 排行榜：基准测试大语言模型的落地能力 ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf)。只要混入一丁点文档中没有的内容，该回答就会被视为“未落地 (Ungrounded)”，从而面临严厉扣分 [FACTS Grounding 基准概述 - api.emergentmind.com](https://api.emergentmind.com/topics/facts-grounding-benchmark)。

## 现状：撞上“70% 之墙”的 AI 真相

这场严苛的考试暴露了当前 AI 技术的局限性。研究人员指出，即使是目前全球公认最聪明的顶尖模型，在这项测试中的**准确率也仅约为 74%** [DeepMind FACTS 框架 2026：大语言模型事实准确性指南](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy)。

对此，专家们使用了 **“70% 事实性天花板 (70% factuality ceiling)”** 这一表述 [70% 事实性天花板：为什么谷歌的新 FACTS 基准是一声警钟](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call)。这意味着无论投入数亿美元开发多么先进的模型，要在海量信息中 100% 完美地筛选事实并回答，仍然存在瓶颈。这既是给人工智能行业的一封“警告信”，也是 AI 想要成为“可靠工具”必须跨越的明确门槛 [70% 事实性天花板：为什么谷歌的新 FACTS 基准是一声警钟](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call)。

此外，该基准是与被称为数据科学圣地的平台 **Kaggle** 合作开发的，增加了其专业性 [引入 FACTS 基准套件以评估大语言模型的事实准确性 - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)。全球顶尖的数据专家共同建立了一套精密的监测体系，能够准确指出 AI 在哪些地方犯错 [FACTS 基准套件提升了对大语言模型事实性的审查](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny)。

## 未来会怎样？

谷歌 DeepMind 并不满足于此，已于 2025 年 12 月推出了搭载性能大幅提升的法官模型的 **“FACTS Grounding v2”** [FACTS 基准套件：系统评估大语言模型事实性的新方法 — Google DeepMind](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)。这意味着更挑剔的法官将开始监督 AI [FACTS 排行榜：大语言模型事实性的全面基准](https://arxiv.org/html/2512.10791v1)。

未来，我们可以通过在线 **排行榜 (Leaderboard)** 实时查看哪款 AI 最诚实、最聪明 [FACTS Grounding 排行榜：基准测试大语言模型的落地能力 ...](https://huggingface.co/papers/2501.03200)。就像家电的“能效等级”一样，这将开启我们在选择 AI 服务时直接确认“准确度等级”并放心使用的时代。

在处理复杂庞大的信息时，将 AI 可能出现的失误减少到趋近于零，这一艰苦的过程将是人工智能从简单的玩具蜕变为我们生活中真正伙伴的最关键的一步 [FACTS Grounding：评估大语言模型事实性的新基准 | ASU+GSV 峰会日程](https://www.asugsvsummit.com/schedule/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)。

## AI 视角
**MindTickleBytes AI 记者的观点**

AI 仅靠编造华丽词藻而获得“创造力”赞誉的浪漫时代正在远去。现在，证明其准确性和诚实度的“验证时代”已经到来。74% 的成绩单绝非耻辱，反而更像是一个希望的信号，揭示了我们需要征服的山峰。迈向一个“不知道就说不知道”、“只说事实”的人格化 AI 的旅程，终于正式步入正轨。

## 参考资料
1. [FACTS Grounding: 评估大语言模型事实性的新基准 — Google DeepMind](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)
2. [FACTS 基准套件：系统评估大语言模型事实性的新方法 — Google DeepMind](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)
3. [FACTS Grounding：评估大语言模型事实性的新基准 | ASU+GSV 峰会日程](https://www.asugsvsummit.com/schedule/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)
4. [Reddit 上的 r/LocalLLaMA：FACTS Grounding：评估大语言模型事实性的新基准](https://www.reddit.com/r/LocalLLaMA/comments/1hgyp2d/facts_grounding_a_new_benchmark_for_evaluating/)
5. [FACTS 排行榜：大语言模型事实性的全面基准](https://arxiv.org/html/2512.10791v1)
6. [FACTS Grounding：评估大语言模型事实性的新基准](https://bestofai.com/article/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)
7. [引入 FACTS 基准套件以评估大语言模型的事实准确性 - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)
8. [FACTS Grounding 排行榜：基准测试大语言模型的落地能力 ...](https://arxiv.org/abs/2501.03200)
9. [PDF - FACTS Grounding 排行榜：基准测试大语言模型的落地能力 ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf)
10. [FACTS Grounding 排行榜 - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)
11. [FACTS Grounding 排行榜：基准测试大语言模型的落地能力 ...](https://huggingface.co/papers/2501.03200)
12. [DeepMind FACTS 框架 2026：大语言模型事实准确性指南](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy)
13. [FACTS Grounding 基准概述 - api.emergentmind.com](https://api.emergentmind.com/topics/facts-grounding-benchmark)
14. [70% 事实性天花板：为什么谷歌的新 FACTS 基准是一声警钟](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call)
15. [FACTS 基准套件提升了对大语言模型事实性的审查](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny)