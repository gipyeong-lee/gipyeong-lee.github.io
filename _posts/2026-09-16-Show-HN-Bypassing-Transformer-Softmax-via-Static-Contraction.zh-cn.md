---
layout: post
title: "AI 变得更聪明、更快速？“Softmax”绕过技术的秘密"
description: "介绍一项创新技术，旨在解决 AI 模型中减慢运算速度并占用大量内存的 Softmax 功能。"
summary: "随着能够跳过或优化人工智能 Transformer 模型中长期存在的运算瓶颈——“Softmax”的技术出现，一个速度更快、能够处理海量信息的 AI 时代正在开启。"
tags: [AI, Transformer, Softmax, 深度学习, 技术趋势]
image: 2026-09-16-Show-HN-Bypassing-Transformer-Softmax-via-Static-Contraction.jpg
image_alt: "一幅数字艺术作品，描绘了复杂公式和符号被简化，从而提高 AI 模型效率的过程"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "减少对 Softmax 的依赖是最大限度提升 AI 效率的必要步骤。这一技术突破不仅是速度的提升，更是拓宽 AI 信息处理边界的关键钥匙。"
quiz:
  - question: "Softmax 函数的主要作用是什么？"
    choices: ["压缩数据", "将数值转换为概率分布", "删除数据"]
    answer: 1
    explanation: "Softmax 是一种将多个数值转换为概率分布的函数，帮助 AI 做出最终判断 [来源: Softmaxfunction - Wikipedia](https://en.wikipedia.org/wiki/Softmax_function)。"
  - question: "SOFT (Softmax-free Transformer) 模型用什么替代了传统的点积 (dot-product) 相似度？"
    choices: ["高斯核函数", "线性函数", "对数函数"]
    answer: 0
    explanation: "SOFT 模型为了在没有 Softmax 的情况下实现自注意力 (self-attention)，使用了高斯核函数 [来源: SOFT: Softmax-free Transformer with Linear Complexity](https://proceedings.neurips.cc/paper/2021/file/b1d10e7bafa4421218a51b1e1f1b0ba2-Paper.pdf)。"
  - question: "引入了“遗忘门 (forget gate)”的模型名称是什么？"
    choices: ["ForgettingTransformer(FoX)", "Softmax-free Transformer", "UniAttn"]
    answer: 0
    explanation: "ForgettingTransformer(FoX) 将遗忘门机制集成到注意力分数中，从而实现了更好的上下文处理 [来源: ForgettingTransformer:SoftmaxAttention with a Forget Gate](https://arxiv.org/abs/2503.02130)。"
lang: zh-cn
ref: 2026-09-16-Show-HN-Bypassing-Transformer-Softmax-via-Static-Contraction
---

想象一下。你正在一个巨大的图书馆里寻找特定信息。但是，如果图书管理员必须把所有的书都翻开看完并整理好之后才给你答案，会怎样？随着书的数量增加，管理员给出答案的时间将会呈指数级增长。我们目前使用的 AI 模型，特别是“Transformer”（掌握句子单词之间关系的 AI 核心结构），正在面临的问题也与此类似。

最近，在人工智能领域，为了解决这一长期的“瓶颈现象”，跳过或优化过去被认为理所当然的“Softmax”运算的创新尝试正变得非常活跃。

## 为什么这很重要？ (Why It Matters)

Transformer 是目前几乎所有现代 AI 的基石。但是，在这个结构中，Softmax 函数就像是处理信息时必须缴纳的一种“通行税”。Softmax 是一个必不可少的函数，它将各种数据值转换为概率分布，帮助 AI 做出最终的选择或判断 [来源: Softmaxfunction - Wikipedia](https://en.wikipedia.org/wiki/Softmax_function)。

问题在于，AI 所处理的信息量最近呈爆炸式增长。处理的数据越多，Softmax 运算就越成为吞噬大量内存、减慢整体运算速度的罪魁祸首。如果能够省略或优化这一运算，AI 就能够以更少的能源消耗、更快速地处理更长的上下文。这意味着在不久的将来，我们可以更舒适地使用更聪明、反应更快的 AI 助手。

## 轻松理解 (The Explainer)

为了理解 Softmax，我们举个简单的例子。设想一下我们在购物中心挑选“最心仪商品”的过程。对比了无数商品的价格、质量、设计后，为每件商品标记出它成为我心仪之选的概率，这个过程就是 Softmax 运算。给所有选项打分，并将其加总转换为 100% 的概率分布。

但如果 AI 模型必须阅读一本长篇小说呢？逐一比较所有单词并精确计算概率是一件非常艰巨的任务。

因此，研究人员最近找到了一些妙招：

1. **静态收缩 (Static Contraction) 技术**：就像提前铺好路一样，在运算过程中提前切断不必要的计算路径，并替换为高效的公式。这大大降低了 AI 模型在长上下文中遭遇内存不足 (OOM, Out-Of-Memory) 的风险 [来源: GitHub - PJHkorea/jax-softmax-bypass](https://github.com/PJHkorea/jax-softmax-bypass), [来源: ShowHN:BypassingTransformerSoftmaxviaStaticContraction](https://news.ycombinator.com/item?id=49666335)。
2. **去除 Softmax (Softmax-free)**：名为“SOFT”的模型使用相对简单的数学函数“高斯核 (Gaussian kernel)”代替了现有的复杂运算。就像为了计算概率，不再每次都使用复杂的工程计算器，而是选择了更直观的捷径 [来源: SOFT: Softmax-free Transformer with Linear Complexity](https://proceedings.neurips.cc/paper/2021/file/b1d10e7bafa4421218a51b1e1f1b0ba2-Paper.pdf), [来源: [2110.11945] SOFT: Softmax-free Transformer with Linear Complexity](https://arxiv.org/abs/2110.11945)。
3. **遗忘技术 (Forgetting Mechanism)**：‘ForgettingTransformer(FoX)’ 利用了能适度遗忘无用信息的“遗忘门 (forget gate)”。简单来说，就像我们只记住重要信息，自然地遗忘其余部分一样，它通过有选择地调节需要注意的分数，使上下文处理变得更加轻松 [来源: ForgettingTransformer:SoftmaxAttention with a Forget Gate](https://arxiv.org/abs/2503.02130), [来源: ForgettingTransformer:SoftmaxAttention with... | Papers with Code](https://paperswithcode.co/paper/2503.02130), [来源: GitHub - zhixuan-lin/forgetting-transformer](https://github.com/zhixuan-lin/forgetting-transformer)。

## 目前状况 (Where We Stand)

目前，这些技术正以从实验室阶段的 PoC（概念验证，Proof of Concept）到学术建议阶段等多种形式迅速发展。但现在断言已经完全替代了 Softmax 还为时尚早。虽然明确证明了它比现有的标准方式更高效，但仍有一些部分需要进一步验证，以应用于所有通用 AI 模型。尽管如此，像“UniAttn”这样在将性能下降降至最低的同时，显著降低运算成本的尝试一直在取得成果，提升了人们的期望值 [来源: UniAttn: Reducing Inference CostsviaSoftmax... | Papers with Code](https://paperswithcode.co/paper/2502.00439)。

## 未来展望 (What's Next)

未来的 AI 技术竞争将不仅仅在于制造“更大的模型”，而在于谁能制造出“更高效的模型”。特别是为了在我们日常使用的智能手机等运算资源受到物理限制的设备上运行更强大的 AI，这些 Softmax 绕过技术将成为必不可少的钥匙。如果今天的这些研究能够结出硕果，我们将能在日常生活中遇见能够完美记住更长对话记录、并以更快速度回答问题的聪明 AI。

## 参考资料

1. GitHub - PJHkorea/jax-softmax-bypass: [https://github.com/PJHkorea/jax-softmax-bypass](https://github.com/PJHkorea/jax-softmax-bypass)
2. Vertex-Softmax: Tight Transformer Verification via Exact Softmax Optimization∗: [https://arxiv.org/pdf/2605.10974](https://arxiv.org/pdf/2605.10974)
3. SimA: Simple Softmax-free Attention for Vision Transformers: [https://openaccess.thecvf.com/content/WACV2024/papers/Koohpayegani_SimA_Simple_Softmax-Free_Attention_for_Vision_Transformers_WACV_2024_paper.pdf](https://openaccess.thecvf.com/content/WACV2024/papers/Koohpayegani_SimA_Simple_Softmax-Free_Attention_for_Vision_Transformers_WACV_2024_paper.pdf)
4. SOFT: Softmax-free Transformer with Linear Complexity: [https://proceedings.neurips.cc/paper/2021/file/b1d10e7bafa4421218a51b1e1f1b0ba2-Paper.pdf](https://proceedings.neurips.cc/paper/2021/file/b1d10e7bafa4421218a51b1e1f1b0ba2-Paper.pdf)
5. [2110.11945] SOFT: Softmax-free Transformer with Linear Complexity: [https://arxiv.org/abs/2110.11945](https://arxiv.org/abs/2110.11945)
6. Differential Transformer | Hacker News: [https://news.ycombinator.com/item?id=41776324](https://news.ycombinator.com/item?id=41776324)
7. Softmaxfunction - Wikipedia: [https://en.wikipedia.org/wiki/Softmax_function](https://en.wikipedia.org/wiki/Softmax_function)
8. ForgettingTransformer:SoftmaxAttention with a Forget Gate: [https://arxiv.org/abs/2503.02130](https://arxiv.org/abs/2503.02130)
9. ShowHN:BypassingTransformerSoftmaxviaStaticContraction: [https://news.ycombinator.com/item?id=49666335](https://news.ycombinator.com/item?id=49666335)
10. ForgettingTransformer:SoftmaxAttention with... | Papers with Code: [https://paperswithcode.co/paper/2503.02130](https://paperswithcode.co/paper/2503.02130)
11. In-Context Learning withTransformers:Softmax... | OpenReview: [https://openreview.net/forum?id=lfxIASyLxB](https://openreview.net/forum?id=lfxIASyLxB)
12. Transformersare RNNs: Fast Autoregressive... - YouTube: [https://www.youtube.com/watch?v=hAooAOFRsYc](https://www.youtube.com/watch?v=hAooAOFRsYc)
13. UniAttn: Reducing Inference CostsviaSoftmax... | Papers with Code: [https://paperswithcode.co/paper/2502.00439](https://paperswithcode.co/paper/2502.00439)
14. GitHub - zhixuan-lin/forgetting-transformer: [https://github.com/zhixuan-lin/forgetting-transformer](https://github.com/zhixuan-lin/forgetting-transformer)
15. SoftmaxFunction in Deep Learning: [https://lzwjava.com/notes/2025-06-03-softmax-en](https://lzwjava.com/notes/2025-06-03-softmax-en)