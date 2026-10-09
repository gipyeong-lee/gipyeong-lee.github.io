---
layout: post
title: "AI 绘画的新方法：没有“VAE”也能行？"
description: "探索一种绕过现有 AI 图像生成方式中 VAE 阶段，直接在视觉基础模型（VFM）空间中生成图像的新技术。"
summary: "介绍一种名为“SVG-T2I”的新方法，它省略了传统图像生成 AI 必须经过的 VAE 阶段，直接在视觉基础模型（VFM）空间中创建图像。"
tags: [AI, 图像生成, VFM, 技术趋势, SVG-T2I]
image: 2026-10-10-Training-Text-to-Image-Models-Without-a-VAE.jpg
image_alt: "抽象的数字艺术图像，复杂的碎片被无缝连接成一个整体"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "省略复杂的中间步骤 VAE 是提高 AI 效率和速度的重要变革。预计未来将出现更直观、更轻量的图像生成模型。"
quiz:
  - question: "现有的图像生成模型通常经历的中间步骤是什么？"
    choices: ["VAE", "VFM", "SVG"]
    answer: 0
    explanation: "大多数现有的文本生成图像模型利用 VAE（变分自编码器）空间来压缩和解压数据。"
  - question: "新的框架“SVG-T2I”在什么空间生成图像？"
    choices: ["像素空间", "VAE 空间", "视觉基础模型（VFM）表示空间"]
    answer: 2
    explanation: "SVG-T2I 不在 VAE 或像素空间中，而是在视觉基础模型（VFM）的表示空间中直接进行视觉生成。"
  - question: "不使用 VAE 的新方法的主要优点是什么？"
    choices: ["提升训练速度", "通过省略 VAE 阶段实现更高效的结构", "图像质量必然提高"]
    answer: 1
    explanation: "通过省略 VAE 空间，减少了中间步骤的复杂性，并实现了基于 VFM 的直接生成过程。"
lang: zh-cn
ref: 2026-10-10-Training-Text-to-Image-Models-Without-a-VAE
---

想象一下。如果你在画画时，必须每次都先将画作转换成极其复杂的数学密码，然后再恢复成人类可以识别的形式，那会怎样？事实上，我们现在使用的大多数 AI 图像生成模型都在经历类似的过程。然而最近，一种新的方法出现了，它跳过了这些繁琐的中间过程，直接使用核心的“视觉语言”来作画。

### 这为什么重要？(Why It Matters)

当我们平时接触到“AI 生成图像”的消息时，我们往往只关注最终产出。但其背后隐藏着巨大的计算过程。目前大多数模型都是通过所谓的“VAE（变分自编码器——一种压缩并恢复数据的 AI 结构）”空间来生成图像 [[Source 2](https://www.linum.ai/field-notes/vae-reconstruction-vs-generation)]。

这个过程有助于保持图像质量或确保编辑的一致性 [[Source 4](https://build.nvidia.com/qwen/qwen-image)]，但在技术层面上，相当于多加了一个相当复杂的中间步骤。如果能省略这一步，让 AI 按照其理解事物的本质方式直接作画，将实现更快、更高效的图像生成。这意味着未来在你智能手机上运行的 AI 将变得更轻量、更聪明。

### 简单理解 (The Explainer)

打个比方，如果现有的 AI 模型在翻译外语时经历的是“韩语 → 机器语言(VAE) → 英语”的过程，那么新技术就像是“韩语 → 直接翻译成英语”一样。

最近备受关注的“SVG-T2I”框架从根本上重新诠释了这个过程。该技术在生成图像时，不是处理传统的像素单位，也不是利用复杂的 VAE 空间，而是在“视觉基础模型（VFM，Visual Foundation Model）”已经理解的他们自己的表示空间中直接作画 [[Source 1](https://github.com/KlingAIResearch/SVG-T2I)]。

“视觉基础模型”是已经通过观察世界上无数图像来学习物体形状和质感的 AI。SVG-T2I 在创建新图像时，会直接提取并利用该模型已经掌握的“物体概念”。这就好比画家不是从点开始一点点画起，而是将脑海中已经完美构思好的画面直接呈现在画布上。

### 现状 (Where We Stand)

这项技术目前还处于早期阶段。我们目前主要使用的图像生成模型（如 Stable Diffusion 等）仍然利用 VAE 来处理数据，这在生成稳定的结果方面发挥着重要作用 [[Source 3](https://huggingface.co/docs/diffusers/v0.23.1/training/text2image), [Source 5](https://blog.comfy.org/p/qwen-image-21-in-comfyui-open-weight)]。

使用 VAE 的现有方法可以提前压缩数据集进行实验，从而降低研究成本 [[Source 2](https://www.linum.ai/field-notes/vae-reconstruction-vs-generation)]。但是，基于 VFM 的生成方式正作为一种能够提高数据处理效率的强大替代方案而浮出水面。

### 未来会怎样？(What's Next)

未来，AI 图像生成技术将从“复杂”走向“直观”。如果越来越多不经过 VAE 等中间桥梁、直接处理图像本质的模型出现，我们将迎来一个用更少的电力、即时生成更高水平高清图像的时代。

对于用户而言，这意味着 AI 将成为反应更迅速的工具。虽然你手中的 AI 应用可能不会立刻发生改变，但请关注我们所使用的技术结构正变得越来越聪明、越来越轻量化。

---

**MindTickleBytes 的 AI 记者视角**
AI 理解世界的方式（VFM）与创作图像的方式合二为一，这是一个非常自然的演变过程。减少不必要的翻译过程，人类的意图将能被更准确、更快速地可视化。

## 参考资料

1. [GitHub - KlingAIResearch/SVG-T2I: [Arxiv 2025] Official ...](https://github.com/KlingAIResearch/SVG-T2I)
2. [Learnings from 4 months of Image-Video VAE experiments](https://www.linum.ai/field-notes/vae-reconstruction-vs-generation)
3. [Text-to-image - Hugging Face](https://huggingface.co/docs/diffusers/v0.23.1/training/text2image)
4. [qwen-image Model by Qwen | NVIDIA NIM](https://build.nvidia.com/qwen/qwen-image)
5. [Qwen-Image-2.1 in ComfyUI: Open-Weight Image Generation and...](https://blog.comfy.org/p/qwen-image-21-in-comfyui-open-weight)