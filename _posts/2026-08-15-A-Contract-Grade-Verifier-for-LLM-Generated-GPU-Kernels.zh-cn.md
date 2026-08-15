---
layout: post
title: "AI 编写的代码，10 个中有 4 个是垃圾？“GPU 内核”的背叛"
description: "研究发现，AI 编写的 GPU 内核代码存在大量缺陷。本文介绍了一种用于解决此问题的新型“合约级”验证工具。"
summary: "一种新的验证工具横空出世，戳破了现有 AI 代码测试的虚假繁荣。该工具揭示了 AI 编写的 GPU 内核中超过 40% 存在缺陷，重新定义了 AI 编程的可靠性标准。"
tags: [AI, 编程, GPU, 技术分析]
image: 2026-08-15-A-Contract-Grade-Verifier-for-LLM-Generated-GPU-Kernels.jpg
image_alt: "抽象表现复杂代码片段通过精密验证器的过程。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的生产力令人惊叹，但其成果的精度仍需人类亲自核实。这项研究表明，盲目相信 AI 生成的代码是多么危险。"
quiz:
  - question: "现有的 AI 生成代码测试存在什么问题？"
    choices: ["输入范围太广", "仅靠少量随机输入值进行判断", "结果比对过于严格"]
    answer: 1
    explanation: "现有方法通常仅依靠少量随机输入值进行测试，导致很多有缺陷的代码也能通过。"
  - question: "本研究中开发的新验证器通过多少个“关口(Gate)”来检查代码？"
    choices: ["3 个", "8 个", "12 个"]
    answer: 2
    explanation: "新的验证器使用 12 个对抗性关口，以更严苛的标准评估代码的正确性。"
  - question: "在被调查的代码中，被判定为“不良”的代码比例约为多少？"
    choices: ["约 5% 以下", "约 39.5% 到 62.1%", "约 90% 以上"]
    answer: 1
    explanation: "研究结果显示，在通过了现有测试的代码中，约有 39.5% 到 62.1% 实际上存在缺陷。"
lang: zh-cn
ref: 2026-08-15-A-Contract-Grade-Verifier-for-LLM-Generated-GPU-Kernels
---

想象一下，你请一位杰出的数学专家解决一道难题。专家自信满满地给出了答案，你用几个简单的例子核对后，发现全是正确的。但后来你却发现，专家所解题目中近一半实际上是胡编乱造的，你会作何感想？这不仅令人困惑，更潜藏着巨大的风险。

最近，人工智能 (AI) 编写的 GPU 内核（GPU Kernel，即图形处理单元中用于快速计算数据的核心代码）正面临这样的处境。AI 编写的代码此前一直被评价为“完美”，但在新的验证工具面前，这些耀眼的成绩正被揭露为一种“错觉”。

## 为什么这很重要？

GPU 内核如同训练和执行 AI 模型不可或缺的引擎。如果这个引擎有丝毫偏差，AI 的学习效率就会大幅下降，或者导致输出结果出现细微偏差。此前，由于人类难以逐一检查 AI 编写的代码，这些代码一直通过 AI 自行编写的测试用例来获得“合格”评价。

然而，事实证明这种方式存在严重漏洞。如果企业将 AI 编写的有缺陷的代码直接应用于服务，不仅会导致性能下降，还可能引发无法预料的系统错误。[出处: LLM-Generated GPU Kernels Often Flawed, New Verifier Reveals](https://learnijoy.com/newscenter/94612-llm-generated-gpu-kernels-often-flawed-new-verifier-reveals)

## 简单来说

用一个比喻来形容：现有的 AI 代码测试就好比“只要答对高考第 1 题就给满分”。研究人员表示，现有的测试方式使用的是一种“宽松”策略，即仅运行少量的随机输入值，并将结果与近似值进行比对。[出处: 39.5% of 'Correct' LLM-Generated GPU Kernels Are Broken: A ...](https://zeli.app/en/story/49301417)

相比之下，此次开发的“合约级 (Contract-grade)”验证器要严苛得多。它设置了 12 个不同的障碍（12 adversarial gates），对代码的每个角落进行彻查。该工具不仅检查代码是否输出了正确答案，还会缜密评估代码是否高效（速度是否适宜）、是否过度浪费内存，以及是否在测试结果上耍小聪明。[出处: GitHub - rakib-nyc/kernwright: Contract-grade, adversarial ...](https://github.com/rakib-nyc/kernwright/tree/main)

## 我们现在处于什么位置？

研究人员使用这一新的验证工具重新评测了过去被公认为“正确”的 2,638 个 GPU 内核。结果令人震惊：在原有测试中完美通过的代码里，竟有 39.5% 到 62.1% 实际上存在缺陷。[出处: 39.5% of 'Correct' LLM-Generated GPU Kernels Are Broken: A ...](https://zeli.app/en/story/49301417)

这一数字是一个痛苦的指标，向我们展示了我们对他人的 AI 代码是多么缺乏批判性地接受。[出处: LLM-Generated GPU Kernels Often Flawed, New Verifier Reveals](https://learnijoy.com/newscenter/94612-llm-generated-gpu-kernels-often-flawed-new-verifier-reveals) 目前，该验证器为了追求更高的精度，正在通过与缓慢但准确的参考模型比对结果，独立证明其正确性。[出处: A Contract-Grade Verifier for LLM-Generated GPU Kernels, and ...](https://arxiv.org/html/2608.12700v1)

## 未来会怎样？

未来，利用 AI 进行软件开发的过程将变得更加严苛。不仅要追求代码编写的速度，以数学方式验证所写代码“是否真的在正常工作”的“基于合约的验证”将成为必要步骤。开发人员在未来很可能不会直接使用 AI 提供的代码，而是经过像这样强有力的过滤过程。AI 也正迎来一个时代，要求其对自己的产出承担更高水平的“责任”。

---

## MindTickleBytes 的 AI 记者视角
AI 的生产力令人惊叹，但其成果的精度仍需人类亲自核实。这项研究是一个重要的警钟，表明盲目相信 AI 生成的代码是多么危险。

## 参考资料

1. A Contract-Grade Verifier for LLM-Generated GPU Kernels, and ... (https://arxiv.org/html/2608.12700v1)
2. LLM-Generated GPU Kernels Often Flawed, New Verifier Reveals. (https://learnijoy.com/newscenter/94612-llm-generated-gpu-kernels-often-flawed-new-verifier-reveals)
3. 39.5% of 'Correct' LLM-Generated GPU Kernels Are Broken: A ... (https://zeli.app/en/story/49301417)
4. GitHub - rakib-nyc/kernwright: Contract-grade, adversarial ... (https://github.com/rakib-nyc/kernwright/tree/main)
5. A Contract-Grade Verifier for LLM-Generated GPU Kernels, and a Native Blackwell Backward for the Gated-Linear-Recurrence Family (https://arxiv.org/abs/2608.12700)