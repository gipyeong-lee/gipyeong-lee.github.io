---
layout: post
title: "AI 读书并为你“总结”？亲自打造一个 AI 大脑你就明白了"
description: "好奇大语言模型（LLM）是如何运作的吗？一个旨在通过 TypeScript 从零开始实现 AI 的教育项目正备受关注，它让原本如同黑盒的 AI 变得清晰可见。"
summary: "超越单纯地使用 AI，通过 TypeScript 亲手编写代码来实现 AI 的核心技术——Transformer 和注意力机制，这种教育尝试正受到广泛关注。"
tags: [AI, LLM, TypeScript, 教育, 开发者]
image: 2026-10-14-Show-HN-Building-an-LLM-from-Scratch-in-TypeScript.jpg
image_alt: "表现通过可视化编码界面理解 AI 模型结构的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "将 AI 理解为“数学结构”而非“魔法”，是现代开发者的必经之路。亲手实现一遍，黑盒自会透明。"
quiz:
  - question: "从零实现 LLM 项目的主要目的是什么？"
    choices: ["制造性能最强的商用模型", "以教育为目的学习 AI 原理", "开发比现有模型快 10 倍的模型"]
    answer: 1
    explanation: "最新的项目更关注教育价值，即通过亲手实现来理解 AI 运作的核心机制，而非追求实际业务性能。"
  - question: "亲自实现注意力（Attention）机制的优势是什么？"
    choices: ["可以训练更多数据", "可以节省 GPU 成本", "可以将 AI 视为结构化理解的对象，而非黑盒"]
    answer: 2
    explanation: "通过亲手实现因果掩码（causal mask）等组件，可以从根本上理解 AI 是如何把握上下文的。"
  - question: "从零开始训练的初期 Transformer 模型有哪些局限性？"
    choices: ["完全没有语言理解能力", "能够续写文本，但难以进行推理或执行指令", "运行速度太慢"]
    answer: 1
    explanation: "学习初期的模型仅具备文本续写能力，若要遵循人类指令或进行复杂推理，则需要额外的微调。"
lang: zh-cn
ref: 2026-10-14-Show-HN-Building-an-LLM-from-Scratch-in-TypeScript
---

想象一下，如果你每天使用的 AI 助手突然说：“从今天起，我来告诉你我为什么会这样回答。”事实上，对于许多人来说，我们目前使用的大语言模型（LLM）就像是一个“有问必答的黑盒”。为了探究其内部究竟发生了什么、单词是如何连接的，开发者社区最近出现了一个有趣的趋势：与其从外部调用 AI，不如**亲手从零开始编写代码来实现它**。

### 为什么这很重要？

随着 AI 技术的飞速发展，我们逐渐开始将 AI 视为一种“生命体”或“魔法”，而不是工具。但 AI 归根结底，不过是基于数学和代码的复杂计算器。对于开发者而言，理解 AI 的内部运作原理已不再仅仅是好奇心使然，更是一种必不可少的职业洞察。像“Node-LLM”这样利用 TypeScript 实现 LLM 的指南，正在帮助开发者将 AI 模型的行为从黑盒转化为透明的逻辑结构 [Source 1](https://book.humanexperiences.io/), [Source 3](https://zeli.app/zh/story/50085332)。这标志着开发者正在超越单纯的 AI 用户，迈向能够设计 AI 如何思考的更高阶段。

### 通俗易懂的理解

理解 AI 的核心结构“Transformer”（一种用于识别句子中单词之间关系的 AI 结构）就像拼图。例如，实现注意力（Attention）机制的过程，就是制定规则来决定 AI 在句子中应该“关注”哪些单词 [Source 13](https://rutube.ru/video/65bc64a2ed5b1b16fe86118bded16c96/), [Source 14](https://www.linkedin.com/pulse/building-llm-from-scratch-part-2-6-attention-how-tokens-imamovich-2orce)。

打个比方，如果我们亲手编写代码来实现库函数替我们完成的“因果掩码（causal mask，防止 AI 提前看到未来单词的装置）”或“头切片（head-slicing，将信息分层处理的技术）”，我们就会真正领悟到 AI 是如何解读单词间的上下文联系的 [Source 13](https://rutube.ru/video/65bc64a2ed5b1b16fe86118bded16c96/)。这就像一个人如果不只是买面包吃，而是亲手经历和面、发酵的过程，就能真正理解面包的构造。在初期阶段，从分割文本单元的分词器（Tokenizer，将句子转化为 AI 能理解的数字的工具）开始，经过简单的模型，逐步发展为复杂的 Transformer [Source 7](https://www.linkedin.com/pulse/building-llm-from-scratch-part-2-6-attention-how-tokens-imamovich-2orce)。

### 我们处于什么阶段？

尽管目前有许多学习项目正在进行，但必须认清一个事实：通过这种方式训练出来的模型，并不能立即取代“Claude”或“Gemini”等高性能 AI [Source 9](https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/), [Source 12](https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/)。

初期训练的 Transformer 模型具备了像模像样的文本续写能力，但在回答用户复杂问题时，往往缺乏推理能力或无法准确遵循指令 [Source 11](https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/)。若要获得这些能力，还需要额外增加更复杂的“后训练（Post-Training）”和“对齐（Alignment，将 AI 回答调整至符合人类意图的过程）”步骤 [Source 11](https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/)。简而言之，从零构建 LLM 是学习 AI 大脑基本原理的绝佳教育课程，但并非追求实际业务性能的阶段 [Source 7](https://www.linkedin.com/pulse/building-llm-from-scratch-part-2-6-attention-how-tokens-imamovich-2orce), [Source 9](https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/)。

### 未来会有什么期待？

未来，探究 AI 结构的尝试将持续进行。更多的开发者有望通过仅使用 CPU 就能训练的模型，来降低 AI 的技术门槛 [Source 21](https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/)。这一过程将成为开发更好 AI 服务的基础知识。我们正在告别单纯惊叹 AI 回答结果的时代，未来更重要的是理解这些结果究竟诞生于何种算法和数学数据流之中。

### MindTickleBytes AI 记者视角

我们每天都在与 AI 对话，但几乎没有机会去学习 AI 对话的方式。通过亲手编码从零开始构建 AI 的过程，将 AI 从“神秘存在”还原为“我们可以设计和改进的技术”。不要再将 AI 称为魔法了，何不现在就亲手打开里面的引擎看看呢？

## 参考资料

1. Building an LLM in NodeJS | Building an LLM in NodeJS (https://book.humanexperiences.io/)
2. Node-LLM - Build LLMs from Scratch · Hacker News | Zeli (https://zeli.app/story/50085332)
3. node-llm: 从零构建大型语言模型指南 — Show HN: Building an LLM fro... (https://zeli.app/zh/story/50085332)
4. GitHub - Maugun/llm-from-scratch-ts: A pedagogical mini LLM ... (https://github.com/Maugun/llm-from-scratch-ts)
5. I Trained My Own LLM from Scratch in 2025: What That Viral HN... (https://dev.to/jtorchia/i-trained-my-own-llm-from-scratch-in-2025-what-that-viral-hn-tutorial-doesnt-tell-you-about-the-l66)
6. TrainLLMFromScratch (https://fareedkhan-dev.github.io/train-llm-from-scratch/)
7. BUILDING AN LLM FROM SCRATCH · PART 2 OF 6 Attention: How... (https://www.linkedin.com/pulse/building-llm-from-scratch-part-2-6-attention-how-tokens-imamovich-2orce)
8. 3) Build an LLM from Scratch 3: Coding attention mechanisms (https://rutube.ru/video/65bc64a2ed5b1b16fe86118bded16c96/)
9. Build and Train a 25M Parameter LLM From Scratch on Your CPU (https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu/)