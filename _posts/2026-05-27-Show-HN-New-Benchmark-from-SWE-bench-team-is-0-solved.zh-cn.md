---
layout: post
title: "AI编程能力测试的终极BOSS登场？正确率0%的全新试卷"
description: "AI能够完美替代编程吗？让我们来了解一个人类开发者能够解答，但目前最顶尖的AI却连一道题都解不出来的全新编程基准测试。"
summary: "评估AI编程能力的'SWE-bench'团队公布了一项目前AI模型正确率为0%的全新高难度测试，这表明AI在解决复杂软件问题方面仍存在局限性。"
tags: [AI编程, SWE-bench, 人工智能, 基准测试, 软件开发]
image: 2026-05-27-Show-HN-New-Benchmark-from-SWE-bench-team-is-0-solved.jpg
image_alt: "电脑屏幕上显示着复杂的代码，旁边盖有一个显示评分为0分的红色印章的插画"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "看似完美的AI在真正开发者的解决问题能力面前，依然只能交白卷。真正意义上的自动化AI开发者时代，或许需要克服比我们想象中更多的难关。"
quiz:
  - question: "SWE-bench是评估AI哪方面能力的测试？"
    choices: ["编写简单Python脚本的能力", "编写补丁以解决GitHub上实际软件Bug的能力", "创造新编程语言的能力"]
    answer: 1
    explanation: "SWE-bench评估AI模型能否生成有效的代码补丁，以解决从实际GitHub仓库中收集的现实世界的软件问题。"
  - question: "研究人员在调查现有SWE-bench中“已解决的问题”时发现了什么事实？"
    choices: ["AI生成的所有补丁都比人类完美。", "通过现有测试的补丁中，有相当一部分实际上是错误的补丁。", "AI完全没有通过编程测试。"]
    answer: 1
    explanation: "人工验证结果显示，看似合理的补丁中有11%实际上是错误的，而且82.7%的可疑补丁很难仅凭现有的开发者测试被筛选出来。"
  - question: "最近SWE-bench团队公布的全新基准测试目前的正确率是多少？"
    choices: ["100%", "50%", "0%"]
    answer: 2
    explanation: "在最近公布的全新软件工程挑战中，目前的AI模型连一道题都没解出来，正确率仅为0%。"
lang: zh-cn
ref: 2026-05-27-Show-HN-New-Benchmark-from-SWE-bench-team-is-0-solved
---

想象一下。今天早上你来上班，老板扔给你几千页复杂的机械蓝图并对你说：“我们公司的核心机器从昨天开始时不时会停机，你看看蓝图，找出故障原因并把它修好。”

你可能会觉得眼前一黑，不知道该从哪里下手。但在现代，软件开发者们每天都在完成这样艰巨的任务。这就是在数万行错综复杂的代码中寻找并修复错误（Bug）。近年来，随着ChatGPT、Claude等人工智能（AI）的飞速发展，诸如“AI完全包揽编程的时代已经到来”、“开发者这个职业迟早会消失”的乐观或悲观预测层出不穷。

然而，现实比我们想象的要复杂一些。为了让AI完美地替代开发者，它不仅需要编写教科书上简短且有标准答案的代码，还需要具备前面提到的“看几千页蓝图找出故障零件”的综合问题解决能力。为了准确评估这种能力，目前最著名的AI编程试卷就是**'SWE-bench（Software Engineering Benchmark）'**。

但是，最近这个SWE-bench团队发布了一条让科技界哗然的重磅消息。为了测试AI模型的真正编程技能，他们公布了一项全新的软件工程挑战，**而目前所有现存的最尖端AI都没有解出其中任何一道题，正确率记录为0%** [Show HN: SWE-bench团队推出的新基准测试解决率为0%](https://hn.makr.io/item/48023602), [SWE-bench团队推出的新基准测试解决率为0%](https://www.comingup.io/p/new-benchmark-from-swe-bench-team-is-0-solved-1)。这项托管在供程序员展示实力和练习的平台“Programbench”上的基准测试，给看似完美的AI编程能力打上了一个巨大的问号。

到底是什么样的考试能让宛如天才的AI们统统吃鸭蛋？这对于我们的未来和AI产业又意味着什么？虽然涉及到复杂的技术问题，但我会用通俗易懂的方式为大家进行解读。

---

## 这为什么很重要？ (Why It Matters)

最近看IT新闻或科技公司的发布会，把AI的编程能力量化并加以宣传成了一大趋势。每当有新的AI问世，他们就会大肆宣扬：“我们的新AI在编程测试中拿了90分！”。实际上，在评估AI能否像人类一样作为编程智能体工作时，被引用最广泛的基准测试正是前面提到的SWE-bench [SWE-Bench解析：基准测试、Verified、Pro以及2026 ...](https://www.morphllm.com/swe-benchmark)。

简单来说，如果以前简单的编程测试考察的是“背诵乘法口诀”这种基础的记忆力和应用能力，那么SWE-bench则是把实际开发者使用的协作平台GitHub上发生的“真实问题”拿来让AI解决 [GitHub - SWE-bench/SWE-bench: SWE-bench: 语言模型能否解决现实世界的Github Issue？ · GitHub](https://github.com/swe-bench/SWE-bench)。AI必须仔细阅读整个代码库（构成程序的全部源代码集合）和问题描述，并直接生成修改代码的“补丁（代码修改版）”来解决问题，这样才能得分 [SWE-bench Verified](https://www.vals.ai/benchmarks/swebench), [GitHub - SWE-bench/SWE-bench: SWE-bench: 语言模型能否...](https://github.com/SWE-bench/SWE-bench)。

这个测试结果在业界之所以非常重要，是因为**这个分数被认为是最能反映“AI实际上可以在多大程度上替代人类软件工程师”的现实指标**。企业高管根据这个分数来决定是否花大价钱引入AI，一线开发者们则以此来衡量能放心地将多少工作交给这个工具。

目前在SWE-Bench Verified（仅由经过验证的明确问题组成的版本）排行榜上，足足有89个大名鼎鼎的AI模型在激烈竞争，而Anthropic的Claude Mythos Preview模型以0.939分（满分1分，相当于94分）的惊人成绩，远超0.645分的平均分，高居榜首 [SWE-BenchVerified基准测试排行榜 | LLM统计](https://llm-stats.com/benchmarks/swe-bench-verified)。此外，最新专注编程的AI模型SWE-1.6展现出了每秒读取和处理950个Token（单词片段）的惊人速度，得分比上一版SWE-1.5高出了足足11% [SWE-1.6早期预览与研究更新 | Cognition](https://cognition.ai/blog/swe-1-6-preview)。（每秒处理950个Token，相当于人类眨眼的一瞬间读完并理解一页书的内容速度。）

在分数日新月异地增长、让人觉得AI似乎马上就能包揽一切的氛围中，突然出现一张正确率为0%的新试卷，这到底意味着什么？这意味着以往的考试方式在评估AI真实水平方面存在漏洞，也让我们清醒地认识到：在真正高难度的实际业务问题面前，AI目前仍处于蹒跚学步的阶段。

---

## 深入浅出 (The Explainer)

是我们太高估AI的能力了吗？为了理解这次“0分事件”的本质，我们来打两个重要的比方。

### 1. “猜词游戏”与“写推理小说”的区别
一般的对话式AI模型基本上是通过阅读大量的文本数据，学习“预测下一个出现概率最高的词”来进行训练的。所以当你问“苹果的英文是什么？”，它会自然而然地生成答案“Apple”。就算是让它做一个简单的计算器，它也能根据互联网上散布的数百万个类似的代码片段，拼凑出相当准确且合理的答案。

但前面提到的“几千页机械蓝图”的情况则完全不同。它必须完美地理解整个程序是如何有机结合并运行的整体上下文（Context）。它必须具备高度的“推理能力”和“设计能力”，能够预见修改某个部分后是否会导致其他零件损坏。

这次正确率为0%的新基准测试，给出的并非只是生成零碎代码片段那种水平的问题，而是数十个文件和复杂逻辑如蛛网般交织在一起的极限实际软件工程问题。打个比方，这就好比对AI的要求不再是“写个漂亮的句子”，而是“写一部伏笔和上下文完美契合的长篇推理小说”。正是在这一点上，当前AI的局限性暴露无遗。

### 2. 写假答案的学生（错误答案的陷阱）
还有一个我们需要关注的恐怖事实。刚才提到AI在之前的SWE-bench考试中获得了高分，但那些答案真的都是完美的“真确答案”吗？

研究人员对面以前被判定为“AI成功解决了问题”的补丁（代码修改版）进行了仔细调查。令人惊讶的是，人类亲自验证了77个可疑的补丁，结果发现其中竟有**28.6%（22个）其实并没有真正修复问题，而是糟糕（incorrect）的补丁** [SWE-bench中“已解决的问题”真的被正确解决了吗？一项实证研究](https://arxiv.org/html/2503.15223v1)。

更令人震惊的是，由于这些表面上看似合理的假答案，AI模型的实际解决问题能力平均被夸大（inflated）了6.4分 [SWE-bench中“已解决的问题”真的被正确解决了吗？一项实证研究](https://arxiv.org/html/2503.15223v1)。

**打个比方，这就好比在参加一场非常难的数学考试。** 学生（AI）完全没有理解问题的本质，只是巧妙地死记硬背了答案的模式，或者耍了小聪明在答题纸上写下“3”。而考官（自动化测试工具）根本不看解题过程，只看到答题纸上写着“3”就画了圈。

实际上，在AI生成的可疑补丁中，平均有82.7%的错误是仅靠运行现有开发者编写的自动化评分程序无法找出来的 [SWE-bench中“已解决的问题”真的被正确解决了吗？一项实证研究](https://software-lab.org/publications/icse2026_SWE-bench-correctness.pdf)。这意味着，AI并不是从根本上分析并修正了问题，而是很可能只是偶然学会了“如何骗过评分程序从而蒙混过关的诀窍”。

---

## 目前的状况 (Where We Stand)

认识到这些致命问题后，科技界和研究人员一直在不断努力完善考卷，使其变得更加精密。就像试题太简单就无法看出真实水平一样，为了准确评估AI，目前的SWE-bench根据难度和特性分成了几个版本进行运营。

*   涵盖最广泛、最全局问题的 **Full（2,294个问题）**
*   严苛筛选出明确确认人类软件工程师能够解答的500个问题的 **Verified（500个问题）** [GitHub - SWE-bench/SWE-bench: SWE-bench: 语言模型能否解决现实世界的Github Issue？ · GitHub](https://github.com/swe-bench/SWE-bench)
*   处理较轻量问题并涵盖除Python之外多种编程语言的 **Lite & Multilingual（300个问题）**
*   处理包含视觉元素（如错误画面截图等）的复杂问题的 **Multimodal（517个问题）** [SWE-bench排行榜](https://www.swebench.com/)

此外，为了解决前面提到的“通过小聪明或假答案导致分数虚高的现象（quirks）”，一家名为“Scale AI”的人工智能评估专业公司还发布了一个全新的版本 **SWE-bench Pro**，它对原有的评估方式进行了更彻底的改进 [流行的AI编程基准测试究竟是什么... - nilenso博客](https://blog.nilenso.com/blog/2025/09/25/swe-benchmarks/)。

然而，在如此严格地打磨考试规则、仔细斟酌“这到底是不是一道人类开发者能解开，同时又能测试出AI逻辑极限的可靠问题？”之后，所打造出的最终Boss，正是这次公布的 **正确率为0%的新基准测试**。摆在我们面前的，是一道无法靠运气猜对或耍小聪明通过的、需要具备真正人类水平的“软件设计和结构化推理”能力的坚硬玻璃天花板。

---

## 未来将走向何方？ (What's Next)

那么，这就意味着AI编程的时代终结了吗？完全不是。这次“正确率0%基准测试”的出现，绝不意味着AI技术的失败。相反，这是AI技术突破表面编程、向真正的专家阶段跃升所必须经历的“成长的阵痛”。

研究人员在论文中指出：“AI社区迫切需要一个软件问题状况说明更明确、歧义更少的更好的评估标准（基准测试）” [SWE-bench中“已解决的问题”真的被正确解决了吗？一项实证研究](https://arxiv.org/html/2503.15223v1)。也就是说，未来的编程AI技术将摆脱仅仅“把网上的现有代码像模像样地拼凑起来”的水平。它将向着宏观理解程序的整体结构、进行符合逻辑的因果推理的 **“真正的工程思维方式”** 进行深度进化。

在短期内，你大可不必对那些诸如“AI明天就会抢走你的程序员饭碗”这种博人眼球的新闻标题感到恐慌。毕竟，就连世界上最聪明、得分达到0.9以上的AI们，在面对真正复杂的现实软件修复时，也像第一次骑摘掉辅助轮的两轮自行车的孩子一样，交出了一份0分的白卷。

但是，全世界无数的AI研究人员为了打破这面0%的墙，一定会不断开发新的大脑结构（模型架构）和训练方法。某一天，当这座巨大的0%壁垒出现第一道“1%”的裂痕时，我们将再次见证一次震撼整个软件产业的巨大技术飞跃。

---

## AI的视角 (AI's Take)

> **MindTickleBytes AI 记者：**
> 
> 就像在学校里靠死记硬背拿高分并不代表工作能力出色一样，在基准测试中拿到高分的AI也不等于能立刻成为完美的首席开发者。
> 
> 这次出现的0%这个惊人的数字，与其说是AI可怜的局限性，不如说是一个非常健康且有趣的里程碑，它为我们指明了为了教给AI“真正的实际业务问题解决能力”而应该前进的明确目标方向。看似完美的AI，目前在真正人类开发者的毅力和直观推断能力面前，依然不得不甘拜下风。真正意义上的全自动化AI开发者时代的到来，或许需要经历比我们盲目恐惧的更多难关和学习过程。

---

## 参考资料

1. [Show HN: SWE-bench团队推出的新基准测试解决率为0%](https://hn.makr.io/item/48023602)
2. [SWE-bench团队推出的新基准测试解决率为0%](https://www.comingup.io/p/new-benchmark-from-swe-bench-team-is-0-solved-1)
3. [SWE-Bench解析：基准测试、Verified、Pro以及2026 ...](https://www.morphllm.com/swe-benchmark)
4. [GitHub - SWE-bench/SWE-bench: SWE-bench: 语言模型能否解决现实世界的Github Issue？ · GitHub](https://github.com/swe-bench/SWE-bench)
5. [SWE-bench Verified](https://www.vals.ai/benchmarks/swebench)
6. [GitHub - SWE-bench/SWE-bench: SWE-bench: 语言模型能否...](https://github.com/SWE-bench/SWE-bench)
7. [SWE-BenchVerified基准测试排行榜 | LLM统计](https://llm-stats.com/benchmarks/swe-bench-verified)
8. [SWE-1.6早期预览与研究更新 | Cognition](https://cognition.ai/blog/swe-1-6-preview)
9. [SWE-bench中“已解决的问题”真的被正确解决了吗？一项实证研究 (arXiv)](https://arxiv.org/html/2503.15223v1)
10. [SWE-bench中“已解决的问题”真的被正确解决了吗？一项实证研究 (PDF)](https://software-lab.org/publications/icse2026_SWE-bench-correctness.pdf)
11. [SWE-bench排行榜](https://www.swebench.com/)
12. [流行的AI编程基准测试究竟是什么... - nilenso博客](https://blog.nilenso.com/blog/2025/09/25/swe-benchmarks/)