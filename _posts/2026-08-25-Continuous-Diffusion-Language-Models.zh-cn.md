---
layout: post
title: "如果AI能像绘图一样写作？“连续扩散”语言模型的挑战"
description: "为什么作为图像生成AI核心技术的“扩散模型”难以应用于文本语言模型？为您浅析连续扩散语言模型的原理与潜力。"
summary: "介绍将图像生成中的“连续扩散”技术应用于文本的最新AI研究动态、技术难点及其发展前景。"
tags: [AI, 语言模型, 扩散模型, 人工智能原理]
image: 2026-08-25-Continuous-Diffusion-Language-Models.jpg
image_alt: "抽象图形，展现复杂的点数据沿着平滑的流向排列"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "尝试用数学空间的几何结构解决文本的离散性问题非常令人兴奋。期待扩散模型能成为填补图像与文本之间鸿沟的钥匙。"
quiz:
  - question: "与图像生成AI不同，将“连续扩散”技术应用于文本模型的主要难点在于什么？"
    choices: ["计算能力不足", "文本是单词单位的离散型数据", "文本数据量比图像小"]
    answer: 1
    explanation: "图像具有连续的像素值，而文本由单词这种独立的（离散的）单位构成，导致现有的连续扩散方法无法直接运行。"
  - question: "在连续扩散语言模型研究中，用于表达单词分布的数学概念是什么？"
    choices: ["统计流形(statistical manifold)", "线性回归方程", "量子力学"]
    answer: 0
    explanation: "最新研究——黎曼扩散语言模型(RDLM)利用统计流形（如超球面）的几何结构对单词分布进行建模。"
  - question: "扩散模型目前应用最广泛的领域是哪里？"
    choices: ["文本翻译", "图像及视频生成", "简单的四则运算"]
    answer: 1
    explanation: "扩散模型是目前图像和视频生成领域最主流的生成式AI方法。"
lang: zh-cn
ref: 2026-08-25-Continuous-Diffusion-Language-Models
---

想象一下：早上起床，你对AI助手说：“帮我总结今天的会议资料并发送邮件。”如果说之前的AI是根据固定的概率一个接一个地衔接单词，那么新一代的AI就像画家在画布上逐步完善画作一样，从模糊的想法开始，逐步润色句子。这正是近期AI研究界的热门话题——“连续扩散（Continuous Diffusion）语言模型”所憧憬的未来。

### 为什么这项技术很重要？

目前我们使用的大多数大语言模型（LLM，通过学习海量文本数据进行写作的AI）都使用“自回归（autoregressive）”方式，即按固定顺序一个接一个地生成单词。这就像只顾眼前的一小步，难以从全局视角俯瞰整个句子的结构，存在局限性。

另一方面，在图像和视频生成领域占据统治地位的“扩散模型”，通过逐步精化数据的方式，能够创造出卓越的成果。[参考资料 4](https://www.youtube.com/watch?v=WqvCxdoVb64), [参考资料 9](https://discuss.pytorch.kr/t/elf-continuous-diffusion-language-model/10215) 如果能将这种方式成功应用于文本，未来将有望实现具备更强创造力和逻辑结构的写作。[参考资料 16](https://www.emergentmind.com/topics/diffusion-reasoner)

### 简单来说：为什么文本与图像不同？

扩散模型本质上是从充满“噪声（noise，即无数据的随机状态）”的空间中，逐步去除噪声并还原清晰图像的过程。照片的亮度或色彩信息即“像素值”，由于是由连续的数字组成，因此这一过程衔接得非常自然。[参考资料 11](https://wandb.ai/byyoung3/ml-news/reports/Block-Diffusion-Language-Models-Combining-autoregression-and-diffusion--VmlldzoxMTg3MjU2OQ)

然而，文本是完全不同的世界。打个比方，图像世界像平缓的山丘，而文本世界则像断开的阶梯。“苹果”和“梨”这两个单词之间没有中间值。文本由“离散的标记（discrete tokens）”构成，因此很难像图像那样在平滑去除噪声的同时生成文字。[参考资料 11](https://wandb.ai/byyoung3/ml-news/reports/Block-Diffusion-Language-Models-Combining-autoregression-and-diffusion--VmlldzoxMTg3MjU2OQ)

为了解决这一问题，研究人员利用“嵌入（embedding，将单词含义放置在数学向量空间的技术）”，将文本表现为存在于连续空间中的坐标。[参考资料 12](https://www.themoonlight.io/fr/review/diffusion-of-thoughts-chain-of-thought-reasoning-in-diffusion-language-models) 近期出现的“黎曼扩散语言模型（RDLM）”等研究，将单词分布方式绘制成一种称为“统计流形（statistical manifold，数据所处的复杂几何空间）”的数学地图。通过将单词处理为在巨大球体（hypersphere）上滚动的点，从而开辟了以连续方式处理文本的途径。[参考资料 3](https://liner.com/review/continuous-diffusion-model-for-language-modeling), [参考资料 14](https://en.papernotes.org/NeurIPS2025/image_generation/continuous_diffusion_model_for_language_modeling/)

### 进展如何？

事实上，自2022年出现“Diffusion-LM”等尝试以来，文本扩散模型的研究就已经开始了。[参考资料 1](https://sander.ai/2026/08/24/continuous-dlms.html) 遗憾的是，目前的连续扩散方式在性能上普遍被认为略逊于现有的基于单词单位写作的模型。[参考资料 2](https://www.linkedin.com/posts/hangke-sui_langflow-continuous-diffusion-rivals-discrete-activity-7450571557388828674-Lv6p), [参考资料 15](https://openreview.net/forum?id=VGv5y60sXC) 虽然运用数学几何的新模型层出不穷，但如何在“语言的离散性”与“连续的扩散过程”之间架起桥梁，仍是人工智能研究最前沿难以攻克的难题。[参考资料 6](https://ai-search.io/papers/continuous-diffusion-model-for-language-modeling)

### 有什么期待？

展望未来，人工智能不仅能写出好文章，还有可能利用扩散模型作为一种“潜在推理者（latent reasoner）”，按步骤对复杂思想进行推理。[参考资料 16](https://www.emergentmind.com/topics/diffusion-reasoner), [参考资料 17](https://www.microsoft.com/en-us/research/publication/coevolutionary-continuous-discrete-diffusion-make-your-diffusion-language-model-a-latent-reasoner/) 在文本和图像同时处理的多模态（multimodal）时代，连续扩散技术将成为打破文本、视频与图像之间界限的关键技术。你未来将会遇到的AI助手，不仅思考会更深刻，而且表达思想的能力也会更加圆润自然。

### MindTickleBytes的AI记者视角
如果扩散模型能够像排列图像像素一样排列文本含义，我们看到的将不再只是单纯的句子生成，而是AI思维过程的一种“收敛过程”。这将成为人机沟通进一步精细化的重要转折点。

## 参考资料
1. [Continuous diffusion language models – Sander Dieleman](https://sander.ai/2026/08/24/continuous-dlms.html)
2. [LangFlow: Continuous Diffusion Rivals Discrete Models in... | LinkedIn](https://www.linkedin.com/posts/hangke-sui_langflow-continuous-diffusion-rivals-discrete-activity-7450571557388828674-Lv6p)
3. [Continuous Diffusion Model for Language Modeling [Quick Review]](https://liner.com/review/continuous-diffusion-model-for-language-modeling)
4. [Advances in Continuous Diffusion Language Models - YouTube](https://www.youtube.com/watch?v=WqvCxdoVb64)
5. [Continuous Diffusion for Discrete Text](https://www.emergentmind.com/topics/continuous-diffusion-for-discrete-text)
6. [Continuous Diffusion Model for Language Modeling - AI for...](https://ai-search.io/papers/continuous-diffusion-model-for-language-modeling)
7. [Diffusion Language Models: How a New AI Paradigm Is Challenging...](https://www.libertify.com/interactive-library/diffusion-language-models-new-ai-paradigm/)
8. [Simple Diffusion Language Models - YouTube](https://www.youtube.com/watch?v=WjAUX23vgfg)
9. [ELF: 임베딩 공간에 머무는 연속 확산 언어 모델(Continuous Diffusion...](https://discuss.pytorch.kr/t/elf-continuous-diffusion-language-model/10215)
10. [Think In Diffusion: Continuous Latent Diffusion Language Model](https://mail.bycloud.ai/p/think-in-diffusion-continuous-latent-diffusion-language-model)
11. [Block Diffusion Language Models: Combining autoregression and...](https://wandb.ai/byyoung3/ml-news/reports/Block-Diffusion-Language-Models-Combining-autoregression-and-diffusion--VmlldzoxMTg3MjU2OQ)
12. [[Revue de papier] Diffusion of Thoughts: Chain-of-Thought Reasoning in Diffusion Language Models](https://www.themoonlight.io/fr/review/diffusion-of-thoughts-chain-of-thought-reasoning-in-diffusion-language-models)
13. [Models — Google DeepMind](https://deepmind.google/models/)
14. [[Paper Note] Continuous Diffusion Model for Language Modeling](https://en.papernotes.org/NeurIPS2025/image_generation/continuous_diffusion_model_for_language_modeling/)
15. [Continuous Diffusion Model for Language Modeling | OpenReview](https://openreview.net/forum?id=VGv5y60sXC)
16. [Diffusion Reasoners: Iterative Inference Models](https://www.emergentmind.com/topics/diffusion-reasoner)
17. [Coevolutionary Continuous Discrete Diffusion... - Microsoft Research](https://www.microsoft.com/en-us/research/publication/coevolutionary-continuous-discrete-diffusion-make-your-diffusion-language-model-a-latent-reasoner/)