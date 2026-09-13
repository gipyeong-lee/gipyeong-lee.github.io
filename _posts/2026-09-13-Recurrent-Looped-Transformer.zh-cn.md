---
layout: post
title: "如何让 AI 思考得更“深”：什么是循环变换器 (Looped Transformer)？"
description: "浅显易懂地解释一种让 AI 模型深入思考的新架构——“循环变换器”。"
summary: "探讨“循环变换器”技术，该技术通过重复利用单一层而非顺序通过多个层，从而极大化 AI 模型的推理能力。"
tags: [AI, 技术, 循环变换器, 人工智能]
image: 2026-09-13-Recurrent-Looped-Transformer.jpg
image_alt: "抽象表现 AI 模型通过循环结构处理数据的景象"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "循环变换器是 AI 效率极致进化的重要里程碑。它展示了我们正从单纯追求模型“体量”增长的时代，跨越到优化智能性能的时代。"
quiz:
  - question: "循环变换器的核心概念是什么？"
    choices: ["无限增大模型规模", "通过重复使用同一层来高效计算", "从物理上模仿人类大脑结构"]
    answer: 1
    explanation: "循环变换器并非通过堆叠更多层来增加深度，而是通过反复执行一个共享的块（block）来提高计算效率和推理能力。"
  - question: "传统的 RNN 与循环变换器的主要区别是什么？"
    choices: ["RNN 进行并行处理，变换器进行顺序处理", "RNN 按时间顺序处理数据，而循环变换器并行处理 token", "两者是相同的技术"]
    answer: 1
    explanation: "传统的 RNN 是按时间序列处理数据的，而循环变换器可以并行处理每个输入 token。"
  - question: "使用循环变换器能获得什么潜在优势？"
    choices: ["减少计算机电力消耗", "模型训练速度必然加快", "在推理时内部更深入思考，从而减少输出中间推理步骤 (Chain of Thought)"]
    answer: 2
    explanation: "研究表明，循环变换器通过循环计算增强了推理能力，因此即使不输出详细的、人类可读的中间思维过程，也能给出正确答案。"
lang: zh-cn
ref: 2026-09-13-Recurrent-Looped-Transformer
---

试想一下，你正在解一道极其复杂的数学题。如果说以前的 AI 模型解题时是把漫长的计算过程一步步全写在纸上才得出答案，那么现在，出现了一种能够在大脑中多次重复同一逻辑过程、从而直接找到最优解的 AI。这就是近期 AI 业界最受瞩目的技术——“循环变换器 (Looped Transformer)”的核心思想。

## 为什么这很重要？

我们日常使用的 AI 助手和聊天机器人正变得越来越聪明。但在这些华丽的智能表现背后，现实是必须不断扩大模型的“体量”，而这带来了庞大的计算资源和能源消耗等副作用。

循环变换器为解决这一问题提出了一个“巧妙的突破口”。它不再通过物理上无限堆叠层数来扩展，而是通过重复重用已有的智能块（Block）来让模型进行更深层次的“思考”。这使得 AI 能够在智能手机等资源受限的设备上执行高阶推理。换言之，这是一项旨在开启“以更高效方式使用更智能 AI 的未来”的技术。

## 轻松理解：核心在于“重复”

为了让你更容易理解循环变换器，我们举两个例子。

第一个是**“重复训练”**。如果说普通的 AI 结构试图通过把百科全书从第 1 页到第 100 页扫描一遍来理解内容，那么循环变换器就像是一种学习方法：反复阅读最核心的章节，直到完全参透其中的含义。这是一种通过循环调用模型内部的“智能块 (Recurrent Block)”进行计算，从而获得更精确答案的结构[Source 2, Source 12]。

第二个是**“滤镜照相机”**。应用照片滤镜时，不是把多个滤镜排成一排让照片通过，而是将同一个滤镜重复叠加多次，使成像更细腻、更清晰。AI 模型也类似，通过让数据多次通过同一个固定的层（Block），反复分析数据并强化推理能力[Source 10]。

学术界通常将这种高效结构分为三个部分：向模型传递输入的“Prelude（序曲）”，实际发生重复计算的核心“RecurrentBlock（循环块）”，以及整理并输出最终答案的“Coda（尾声）”[Source 13, Source 20]。

## 当前现状

许多研究人员已经开始利用循环变换器努力超越现有模型的性能。特别值得一提的是，目前还发布了“无需训练的循环变换器”技术，无需改动庞大的 AI 模型，只需添加一个外部的“包装器 (Wrapper)”就能使其像循环结构一样运作[Source 5]。

过去的 RNN（循环神经网络，即处理数据的传统 AI 模型）因为必须按时间流逝顺序处理数据，导致速度慢且难以并行计算[Source 14]。但循环变换器克服了这一经典局限。它在沿时间轴并行处理每个输入 token（AI 处理的单词片段）的同时，保留了循环结构的优势[Source 6]。

此外，有分析指出，循环次数越多，模型内部的思考就越充分，因此我们平时在与聊天机器人对话时看到的“正在思考...”等长篇中间思维过程（Hidden Chain of Thought），即便不全部显示在屏幕上，模型也能给出更准确的答案[Source 1, Source 8]。

## 未来走向

循环变换器预示着 AI 学习方式和运作方式的巨大变革。未来，相比于无条件地增大模型规模，如何高效地循环旋转以调节思维深度，将成为衡量 AI 核心性能的指标[Source 19]。

对用户而言，这意味着我们所使用的普通设备也能提供更快、更准的 AI 回复；对开发者而言，这意味着能以更少的资源设计出高性能 AI。下次当 AI 给出一份答复时，何不好奇地想一下，这个模型究竟经历了多少次循环才得出答案呢？

## MindTickleBytes 的 AI 记者视角
循环变换器是一个非常优秀的案例，它展示了 AI 正在从单纯靠“数据量”决胜负的时代，进化到靠“思维质量”决胜负的阶段。与其强迫 AI 学习“更多训练数据”，不如给它在现有资源内“更深入思考”的机会——这或许正是我们所梦想的 AI 真正进化的方向。

## 参考资料
1. [OpenAI Astra and Looped Transformers | Sebastian Raschka, PhD](https://sebastianraschka.com/blog/2026/openai-astra-looped-transformers.html)
2. [Looped Transformer Architecture](https://www.emergentmind.com/topics/looped-transformer-architecture)
3. [What Is a Looped Transformer? Complete Guide to Recurrent Depth and OpenAI's Astra | Tosea.ai](https://tosea.ai/blog/looped-transformer-recurrent-depth-astra-guide)
4. [LoopFormer: Elastic-Depth Looped Transformers for Latent Reasoning via Shortcut Modulation](https://loopformer.github.io/)
5. [Training-Free Looped Transformers](https://arxiv.org/abs/2605.23872)
6. [What are Looped Transformers? Explained clearly | AVB (@neural_avb) on X](https://x.com/neural_avb/article/2081741935883223196)
7. [Looped Transformers are Better at Learning Learning Algorithms](https://arxiv.org/html/2311.12424v2)
8. [GPT-6 Astra, Looped Transformers, and Hidden Reasoning](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and)
9. [recurrent-looped-tranformer/Recurrent_Looped_Transformer.pdf](https://github.com/yifanzhang-pro/recurrent-looped-tranformer/blob/master/Recurrent_Looped_Transformer.pdf)
10. [Mechanistic Dynamics of Looped Transformers](https://www.emergentmind.com/papers/2604.11791)
11. [Transformers Are (Naively) Looped Transformers, Horizontally...](https://charlesdddd.github.io/blog/transformers-are-looped.html)
12. [Looped Language Model Training Has a Hidden Supervision Flaw...](https://www.techtimes.com/articles/319135/20260626/looped-language-model-training-has-hidden-supervision-flaw-norms-grow-unchecked.htm)
13. [OpenMythos: 通过公开论文还原 Claude Mythos 架构假设](https://www.codingmax.net/blog/openmythos-claude-mythos-rdt)
14. [Abstract page for arXiv paper 1706.03762: Attention Is All You Need](https://arxiv.org/abs/1706.03762)
15. [Recurrence Strikes Back: Attention Is Not All You Need](https://www.linkedin.com/pulse/recurrence-strikes-back-attention-all-you-need-dr-gabriel-seiberth-alw7f)
16. [What Does It Mean for a Model to 'Think'? Reasoning, Recursion, and...](https://fin.ai/research/what-does-it-mean-for-a-model-to-think-reasoning-recursion-and-the-operator-design-space/)
17. [Ultron — Recurrent-Depth Transformer | Hugging Face](https://huggingface.co/trojan0x/ultron)
18. [open-mythos | PyPI](https://pypi.org/project/open-mythos/)