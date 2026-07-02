---
layout: post
title: "让 AI 更轻巧、更聪明：'非对称量化'带来的变革"
description: "轻松了解'非对称量化'技术，它能将 AI 模型的数据压缩高达 97%，同时几乎不损失任何性能。"
summary: "介绍数据压缩技术'非对称量化'，解释其如何在大幅降低 AI 模型存储空间的同时，保持极高的信息准确度。"
tags: [AI, 数据压缩, 量化, 技术趋势]
image: 2026-07-02-Asymmetric-Quantization-Near-Lossless-Retrieval-with-97-Storage-Reduction.jpg
image_alt: "展示复杂 AI 数据结构通过非对称量化实现高效压缩过程的视觉材料"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "数据效率是 AI 融入我们日常生活核心的关键。非对称量化能够减轻沉重技术的负担，从而实现更广泛的应用。"
quiz:
  - question: "非对称量化优于传统量化方式的地方是什么？"
    choices: ["无条件删除数据", "使用非对称偏移量以减少信息损失", "增加存储容量"]
    answer: 1
    explanation: "非对称量化利用偏移量更精确地保存信息，从而减少损失。"
  - question: "在文档检索系统中应用该技术可获得什么益处？"
    choices: ["检索速度变慢 100 倍", "节省高达 32 倍的存储空间", "准确度降为 0"]
    answer: 1
    explanation: "将文档向量压缩为二进制符号，可节省高达 32 倍的存储空间。"
  - question: "在 LLM 中，非对称量化主要应用于哪里？"
    choices: ["主要是激活 (Activations) 层", "硬件设备本身", "网络线缆"]
    answer: 0
    explanation: "相比权重，将其应用于激活层能获得更大的性能提升，因此主要应用于激活数据。"
lang: zh-cn
ref: 2026-07-02-Asymmetric-Quantization-Near-Lossless-Retrieval-with-97-Storage-Reduction
---

想象一下。当你在智能手机上搜索数万份文档时，有一个 AI 能在瞬间找到答案。但如果这个 AI 使用的数据大小比原来小 32 倍呢？就像把巨大的图书馆里装满的书籍压缩成一张薄纸且内容丝毫不损一样，这样的技术正在成为现实。今天，我们就来介绍一种魔法般的技术——“非对称量化（Asymmetric Quantization）”，它能在保留 AI 核心智能的同时，大幅压缩模型容量。

## 为什么这项技术很重要？

近年来，AI 模型正变得异常庞大。随着模型变得更加聪明，其中包含的信息量也变得非常巨大。然而，这意味着用户的智能手机或企业服务器需要巨大的存储空间。例如，如果一台本来只能处理 1 个人数据的设备需要处理 100 个人的数据，那将非常低效。

这项技术让 AI 能在日常生活的小型设备上更加自由地使用。存储空间变小也意味着运营成本的降低。最终，这将为我们身边的智能设备即使在没有网络连接的情况下也能具备更聪明的 AI 功能奠定坚实基础。 [Source 12](https://news.ycombinator.com/item?id=48724127)

## 轻松理解：如何给数据“减肥”

“量化（Quantization）”简而言之，就像将高分辨率照片降低分辨率，同时尽可能保留原始图像。简单来说，就是将以往由 32 位这种非常精密且复杂的数字表达的数据，转换为 8 位这种简单的数字的工作。 [Source 15](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization)

如果说传统的“对称量化”是围绕固定的基准点对数字进行“一刀切”处理，那么“非对称量化”则承认这些基准点可能会向一侧偏移。比喻来说，就像调整照片亮度时，分别设置最暗处和最亮处以保留细节信息一样。该技术通过单独存储块比例和偏移量（基准点校正值），在减少数字位数的同时，更精准地保留数据的细微差别。 [Source 8](https://arxiv.org/html/2601.14277v1), [Source 13](https://www.emergentmind.com/topics/asymmetric-quantization)

特别是在文档检索系统中，它采用了更极端的方式。AI 理解问题的“问题向量”保持极高精度，而作为搜索对象的“文档向量”则转换为简单的“二进制符号（0 和 1 的组合）”进行存储。这样一来，文档存储空间节省了 32 倍，同时检索准确度几乎保持不变。 [Source 11](https://mixedbread.com/blog/asymmetric-quant)

## 我们现在处于什么阶段？

目前，非对称量化正作为最大限度提升 AI 模型效率的实用工具被广泛利用。特别是在大语言模型（LLM）中，该技术主要应用于模型的“激活（Activations，模型处理输入信息中间过程的数据）”层。因为相比应用于权重（模型的基础知识），应用于作为中间处理过程的激活数据时，性能提升更加显著。 [Source 5](https://arxiv.org/html/2507.17417v2)

实际上，应用了非对称量化技术的模型，在将存储容量压缩至原有最高 97% 的同时，人类所感受到的信息准确度几乎保持在无损水平。 [Source 12](https://news.ycombinator.com/item?id=48724127), [Source 13](https://www.emergentmind.com/topics/asymmetric-quantization)

## 未来会是什么样子？

未来，AI 将变得更轻、更快。我们将迎来一个在我们的智能手机、笔记本电脑，甚至家用电器中搭载比现在聪明得多的 AI 的时代。像非对称量化这样的技术，将不再把 AI 局限于互联网云端后的巨大服务器中，而是加速将其带到我们手中的小巧设备上，实现“AI 日常化”。随着 AI 模型变得轻量化，技术将变得更加亲切且实用。

---

### MindTickleBytes 的 AI 记者视角
无论技术多么聪明，如果因为过于沉重而无法使用，那它就毫无用处。非对称量化是实现 AI “智能”与“效率”双赢的巧妙策略。未来，比起简单地比较“模型有多大”，关注“信息压缩和利用的效率有多高”将成为 AI 竞争的核心指标。

## 参考资料

1. [Statistically-Lossless Quantization of Large Language Models](https://arxiv.org/html/2605.02404)
2. [A Comprehensive Evaluation on Quantization Techniques for Large Language Models](https://arxiv.org/pdf/2507.17417)
3. [Asymmetric Deep Semantic Quantization for Image Retrieval](https://arxiv.org/pdf/1903.12493)
4. [[1903.12493] Asymmetric Deep Semantic Quantization for Image Retrieval](https://arxiv.org/abs/1903.12493)
5. [A Comprehensive Evaluation on Quantization Techniques for Large Language Models](https://arxiv.org/html/2507.17417v2)
6. [Reducing Storage of Pretrained Neural Networks by Rate- ...](https://arxiv.org/pdf/2505.18758)
8. [Which Quantization Should I Use? A Unified Evaluation of llama.cpp Quantization on Llama-3.1-8B-Instruct](https://arxiv.org/html/2601.14277v1)
10. [Towards 10 Million Context Length LLM Inference with KV ...](https://www.stat.berkeley.edu/~mmahoney/pubs/neurips-2024-kvquant.pdf)
11. [AsymmetricQuantization:Near-LosslessLateinteractionRetrieval...](https://mixedbread.com/blog/asymmetric-quant)
12. [AsymmetricQuantization:Near-LosslessRetrieval... | HackerNews](https://news.ycombinator.com/item?id=48724127)
13. [AsymmetricQuantizationTechniques](https://www.emergentmind.com/topics/asymmetric-quantization)
14. [LLMQuantizationGuide: Run 70B Models... | Space Services Research](https://spaceservices.org/learn/llm-quantization-compression)
15. [A Visual Guide toQuantization- by Maarten Grootendorst](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization)