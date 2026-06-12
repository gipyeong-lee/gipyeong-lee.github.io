---
layout: post
title: "尽管AI很聪明，为什么还是总“胡说八道”：注意力机制的陷阱"
description: "通过最新研究，通俗解读为什么像ChatGPT这样的AI虽然擅长检索信息，却常常得出离谱的结论。AI的“注意力”存在致命弱点。"
summary: "最新研究表明，AI的核心技术“注意力机制”缺乏人类拥有的“执行控制”能力，无法过滤掉不必要的干扰因素，从而导致推理失败。本文对此进行深度分析。"
tags: [人工智能, Transformer, 注意力机制, 认知心理学, AI局限性]
image: 2026-06-12-Deficient-executive-control-in-transformer-attention.jpg
image_alt: "在无数错综复杂漂浮着的字母和符号中，放大镜却照向了错误地方的插画"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "除了单纯地堆砌数据，如今教导AI“该忽略什么”将成为下一代人工智能的核心课题。"
quiz:
  - question: "根据最新研究，现代AI模型的“注意力”功能中，明确缺失的人类认知能力是什么？"
    choices: ["记忆力 (Memory)", "执行控制 (Executive Control)", "模式识别 (Pattern Recognition)"]
    answer: 1
    explanation: "最近的研究指出，大型语言模型 (LLM) 缺乏人类的“执行控制”能力，因此难以过滤掉相互冲突的信息。"
  - question: "研究团队为了证明AI的局限性，使用了哪种认知心理学的经典测试？"
    choices: ["图灵测试 (Turing Test)", "罗夏墨迹测验 (Rorschach Test)", "斯特鲁普任务 (Stroop Test)"]
    answer: 2
    explanation: "研究团队利用了在文字含义与颜色产生矛盾时会引发认知冲突的“斯特鲁普任务”，揭露了AI在执行控制方面的缺陷。"
  - question: "根据论文内容，当AI在语境中遇到令人困惑的“干扰项 (Distractors)”时，会发生什么？"
    choices: ["自动修正错误并找到正确答案。", "只影响处理速度，不影响最终结果。", "无法忽略干扰因素，导致灾难性的推理失败。"]
    answer: 2
    explanation: "研究表明，当混入干扰因素时，AI无法将其过滤，并会遭遇灾难性的推理失败 (Catastrophic reasoning failures)。"
lang: zh-cn
ref: 2026-06-12-Deficient-executive-control-in-transformer-attention
---

想象一下。你和久违的挚友正面对面坐在一家非常嘈杂的咖啡馆里。隔壁桌的人正爆发出阵阵大笑声，咖啡馆天花板上的巨大扬声器里正播放着震耳欲聋的节奏音乐。甚至窗外还有救护车的警笛声呼啸而过。对于普通人来说，即使在这种混乱的情况下，也能完全专注于眼前朋友的声音来进行交谈。这是因为我们的大脑拥有一种惊人的过滤能力，能够自行判断并“忽略”当前环境中不必要的噪音和视觉刺激，精准提取我们需要的重要信息。

我们通常坚信，像ChatGPT或Claude等现代顶级人工智能 (AI) 也同样如此，它们会对我们提供的文档进行深度“关注 (Attention)”，从而读取其中的核心内容。事实上，AI在海量文档中瞬间找出所需单词的能力确实表现得非常卓越。然而，最近发表的一篇突破性研究论文，却给我们坚信的这种幻想泼了一盆冷水。令人震惊的是，AI完全缺乏我们大脑像呼吸一样自然执行的“忽略噪音能力”。

今天，我们将基于最新研究，通俗易懂地剖析为什么人工智能明明很聪明，却偶尔会像小学生一样满嘴跑火车，说出荒唐胡话的根本原因。

## 为什么这很重要？ (Why It Matters)

根据最近发表在《PNAS Nexus》期刊上，由Suketu Chandrakant Patel、Hongbin Wang和Jin Fan组成的研究团队发布的论文，构成现代AI核心骨架的技术中隐藏着严重的结构性缺陷 [斯特鲁普任务揭露LLM内在缺陷 - NeuroscienceNews](https://neurosciencenews.com/llm-stroop-task-cognitive-attention-30801/)。该研究团队指出，AI在寻找有用信息方面像放大镜一样出色，但在面对混杂的干扰因素或前后矛盾的信息时，它过滤这些信息的“执行控制 (Executive Control，即大脑抑制不必要刺激并专注于目标的认知能力)”能力却明显不足 [Transformer注意力机制中的执行控制缺陷](https://europepmc.org/article/PPR/PPR969150)。

这不仅仅是科学家们头疼的技术局限，更是与我们日常生活和工作息息相关的重要问题。简单来说，假设AI正在分析患者复杂的医疗记录以辅助医生诊断，或者在重要合同签订前审查数百页的法律文件。如果在文件某个角落不小心混入了一段与正文完全矛盾的垃圾内容，或者毫无关联的网络广告文本，会发生什么呢？

如果是人类，肯定会嗤之以鼻地说“这是没用的内容”，然后在一秒钟内将其忽略。但遗憾的是，缺乏执行控制能力的AI会被这些无关信息“分散注意力”，从而得出完全错误的诊断或致命的法律结论。如果我们要坚信AI并把重要决定交给它，那么让AI在具备快速阅读文本能力的同时，也必须具备“不被无用信息干扰”的强大心理素质。

## 通俗讲解 (The Explainer)

目前震惊全球的AI技术核心是Transformer（一种能够掌握句子中单词之间相互关系的AI大脑结构）模型。该模型使用一种名为“自注意力机制 (Self-Attention)”的计算方法，来理解句子中大量单词之间的关联方式。

然而，正如Hacker News上的一位开发者敏锐地指出的那样，AI技术中使用的“注意力”一词，与人类日常使用的注意力相去甚远，是一个颇具误导性 (Deceptive) 的表达 [Transformer注意力机制中的执行控制缺陷 | Hacker News](https://news.ycombinator.com/item?id=48484282)。借用那位开发者的一针见血的说法，Transformer的注意力机制与人类实际的注意力集中程度，仅仅是名字听起来相似而已。

打个比方，假设你正在阅读一本非常难懂的专业书籍，为后天的期末考试做准备。当出现重要的核心公式或概念时，人类会用红色荧光笔将其划出，并将大脑的能量100%集中在那一部分。相反，对于书页角落里前任主人画的滑稽涂鸦，或是与学习无关的微小污渍，人类只会轻轻瞥一眼就立刻忽略掉。这就是前面提到的人类“执行控制”能力。这是当大脑中存在冲突信息时解决冲突，并彻底筛选出符合当前目标（备考）信息的人类固有核心功能 [Transformer注意力机制中的执行控制缺陷](https://europepmc.org/article/PPR/PPR969150)。

但是，根据论文所述，基本的Transformer模型会以完全相同的方式对待所有的查询或信息 (Query) [[2411.12892] 选择性注意力：通过有原则的上下文控制增强Transformer](https://arxiv.org/abs/2411.12892)。也就是说，它会把用荧光笔标记的重要公式和角落里画着的无意义涂鸦放入相同的计算公式中，并以同样认真的态度进行读取。研究团队主张，AI这种不知变通、均等处理信息的方式，致命地阻碍了AI灵活调整上下文重要度并果断舍弃不必要信息的能力 [[2411.12892] 选择性注意力：通过有原则的上下文控制增强Transformer](https://arxiv.org/abs/2411.12892)。

研究团队为了明确证明AI的这一弱点，利用了认知心理学中的经典实验“斯特鲁普任务 (Stroop Test)” [斯特鲁普任务揭露LLM内在缺陷 - NeuroscienceNews](https://neurosciencenews.com/llm-stroop-task-cognitive-attention-30801/)。斯特鲁普任务可以看作是一种“大脑开关训练”。简单来说，想象一下“红”这个字是用深蓝色的墨水写成的。此时，受试者必须强行忽略文字的含义“红”，大声说出眼睛看到的墨水颜色“蓝”。人类可以发挥高度的执行控制能力，强制压抑瞬间在大脑中产生的混乱（文字含义 vs 墨水颜色），最终说出正确答案。

但遗憾的是，基于Transformer的大型语言模型 (LLM) 在面对语境中巧妙隐藏的这种容易混淆的“干扰项 (Distractors)”时，无法将其有效忽略。最终，AI对这种干扰信息束手无策，陷入逻辑崩溃的灾难性推理失败 (Catastrophic reasoning failures) 的深渊 [“注意力”陷阱：PNAS研究揭示了Transformer架构中执行控制的缺失...](https://baguaai.com/the-attention-trap-pnas-study-exposes-the-lack-of-executive-control-in-transformer-architectures/)。

有趣的是，脑科学和医学界也一直在深入研究人类的这种注意力缺陷。根据一些假设，ADHD（注意力缺陷多动障碍）患者常见的粗心或冲动，并非仅仅是缺乏耐心，而是因为负责大脑指挥官角色的额叶“执行控制系统”本身无法正常运作而产生的现象 [注意力控制缺陷：胆碱能机制和基于电路的治疗方法 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3235713/)。如果把它比作AI，这就好比目前的AI模型虽然拥有令人惊叹的知识储备（足以在高考中获得满分），但在海量信息的洪流中，它们的注意力却极易被分散，正患有“重度注意力缺陷症”。

## 现状 (Where We Stand)

目前，我们每天在智能手机和电脑上惊叹着使用的大型语言模型，在广泛浏览和搜索文档功能方面，用学术术语来说就是“定向 (Orienting，将注意力转向信息所在之处的能力)”，已达到了远超人类的可怕程度。然而，能够批判性筛选收集到的信息、并坚决剔除无用内容的“执行控制”功能，却并没有在模型的底层结构中被明确设计或实现，处于非常不稳定的状态 [Transformer注意力机制中的执行控制缺陷](https://europepmc.org/article/PPR/PPR969150)。

这正是为什么当提示词（我们输入给AI的指令）过长、或是几十页的文档中存在前后矛盾的内容、亦或是混入了大量对解决问题毫无帮助的垃圾信息时，AI的回答质量会急剧下降的根本原因。在这种情况下，AI编造不存在的事实的幻觉现象 (Hallucination) 就会爆炸性地增加。如果指示AI去搜索寻找某个特定事实，它会像名侦探一样找得非常准。但反过来说，要让它执行“这个信息不符合当前情况，请果断忽略”这种复杂的高阶认知控制，以目前的技术架构来说却极其困难。

为了弥补这一致命弱点，我们应该怎么做呢？专家们一致认为，在保持AI基本注意力选择功能（快速查找信息的能力）的同时，我们必须持续对AI进行“执行控制”测试，在更高层面上调节“大脑”冲突，抑制对错误信息的关注，从而从根本上修复系统性缺陷 [补充材料：Transformer注意力机制中的执行控制缺陷...](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/pnasnexus/5/6/10.1093_pnasnexus_pgag149/1/pgag149_supplementary_data.docx?Expires=1784184747&Signature=jZba04Dt70TAzJuTvZLEpYzmofCdrCvhM83Qw2uOWDdZ5gaq4wg8R7bpWRTw~FmDc7kUPA5THzlJW-j5QOIPtGoAxEhahvpDUpX6Cs0Y8aiOrHpzLrZ0DkGL9k2KdLFcjBj4VTQfOQ34kDFkJf7Io1KT9YP~nNeNByRR1JufMcpZVcyJB~cTC5lvHDMixXd4XIpxFEpMCKvPK8gyKynwuNS6JDNVvO7c480VfzfVS~XB025~uj7fJAjt65gC9GaTPfw7I~4C~xl1WAw1DuYEl4SFZdUfQ4wnSnGZvpxpmptqz7QXlP5CN1szP74zocGH17CR1Q420ncC9vnye7JuPg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)。

## 未来展望 (What's Next)

这项研究结果不仅是挑出AI的毛病，更向全球AI开发者和科技巨头明确指出了AI发展的新方向。迄今为止，为了让模型变得更聪明，AI研究的主流一直痴迷于盲目地增加训练数据量、大幅扩大计算机的大脑尺寸（参数量），即“数量扩张”。就像是在制造一个只有体型庞大的巨人一样。

但是，未来的AI开发竞赛，其形式将发生彻底改变。突破单纯机械地读完数千万本书的粗暴信息吸收，如何从根本上彻底改造AI的大脑结构，融合类似于人类“执行控制”的精密过滤机制，将成为学术界和工业界最热门的研究课题。在不远的将来，AI将获得像人类一样，在浏览数百页文件时主动判断的能力：“啊，从整体语境来看，这个段落是废话或者是陷阱，所以我必须把它从脑海中清除，只看真正重要的核心框架。”我们可以期待拥有在噪音中也不动摇的“真正注意力”、实现次元进化的下一代AI的出现。

## AI的视角 (AI's Take)

MindTickleBytes AI记者的视角：要摆脱像鹦鹉一样似是而非地模仿人类语言统计模式和概率的水平，让AI达到真正意义上的逻辑和推理能力，就需要进行一场巨大的范式转变。现在，除了教导AI“该认真看什么”之外，迫切需要对其进行心态训练，教导它“该坚决不看什么，并将其丢进垃圾桶”。相比于试图拥抱世界上所有知识的贪婪AI，懂得果断剔除不重要信息的AI，最终能产出更具智慧的结果。这项最新研究再次提醒我们，真正的“注意力”力量，矛盾地源于能够毫不留恋地抛弃不必要事物的勇气和决断力。

---

## 参考资料
1. [斯特鲁普任务揭露LLM内在缺陷 - NeuroscienceNews](https://neurosciencenews.com/llm-stroop-task-cognitive-attention-30801/)
2. [Transformer注意力机制中的执行控制缺陷](https://europepmc.org/article/PPR/PPR969150)
3. [Transformer注意力机制中的执行控制缺陷 | Hacker News](https://news.ycombinator.com/item?id=48484282)
4. [[2411.12892] 选择性注意力：通过有原则的上下文控制增强Transformer](https://arxiv.org/abs/2411.12892)
5. [“注意力”陷阱：PNAS研究揭示了Transformer架构中执行控制的缺失...](https://baguaai.com/the-attention-trap-pnas-study-exposes-the-lack-of-executive-control-in-transformer-architectures/)
6. [注意力控制缺陷：胆碱能机制和基于电路的治疗方法 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3235713/)
7. [补充材料：Transformer注意力机制中的执行控制缺陷...](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/pnasnexus/5/6/10.1093_pnasnexus_pgag149/1/pgag149_supplementary_data.docx?Expires=1784184747&Signature=jZba04Dt70TAzJuTvZLEpYzmofCdrCvhM83Qw2uOWDdZ5gaq4wg8R7bpWRTw~FmDc7kUPA5THzlJW-j5QOIPtGoAxEhahvpDUpX6Cs0Y8aiOrHpzLrZ0DkGL9k2KdLFcjBj4VTQfOQ34kDFkJf7Io1KT9YP~nNeNByRR1JufMcpZVcyJB~cTC5lvHDMixXd4XIpxFEpMCKvPK8gyKynwuNS6JDNVvO7c480VfzfVS~XB025~uj7fJAjt65gC9GaTPfw7I~4C~xl1WAw1DuYEl4SFZdUfQ4wnSnGZvpxpmptqz7QXlP5CN1szP74zocGH17CR1Q420ncC9vnye7JuPg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)