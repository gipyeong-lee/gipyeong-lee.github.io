---
layout: post
title: "AI 突然说“我只是一个语言模型”，竟是因为一个“开关”？"
description: "在与 AI 对话时，你是否经常听到“我只是一个语言模型”这种回复？其实，这并非 AI 的本意，而是由其特定功能触发的一种现象。"
summary: "研究发现，AI 的对话模板实际上充当了决定其人格的开关，当启用该模板时，AI 会更频繁地使用防御性的“免责语气”。"
tags: [AI, 大语言模型, 人工智能, 技术研究]
image: 2026-09-27-As-a-Language-Model-Chat-Template-Switches-LLM-Self-Referential-Voice.jpg
image_alt: "抽象表现 AI 对话框中，AI 回复“我只是一个语言模型”的场景。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的语调并非仅仅是数据学习的结果，而是受到系统配置方式的直接控制，这一点对于确保 AI 开发过程的透明度具有极大的参考价值。"
quiz:
  - question: "研究人员将 AI 在对话中使用的“我只是一个语言模型”这类话术称为什么？"
    choices: ["防御性语调", "免责之声 (Disclaimer voice)", "机械式响应"]
    answer: 1
    explanation: "研究人员将 AI 在指代自身或说明局限性时使用的这种话术定义为“免责之声 (Disclaimer voice)”。"
  - question: "根据研究结果，AI 的对话模板起到了什么作用？"
    choices: ["提升 AI 的记忆力", "决定 AI 语调的开关作用", "调节 AI 的响应速度"]
    answer: 1
    explanation: "AI 的对话模板起到了开关的作用，决定了 AI 所使用的自我指代语气。"
  - question: "研究人员在 3 个 AI 模型内部发现了什么，证明了 AI 的语调是可以被直接调节的？"
    choices: ["特定激活方向 (Activation direction)", "数据库的语言代码", "硬件开关"]
    answer: 0
    explanation: "研究人员在模型内部激活数据中发现了特定的“方向”，并证明可以通过调节它来控制 AI 是使用免责语气还是经验性语气。"
lang: zh-cn
ref: 2026-09-27-As-a-Language-Model-Chat-Template-Switches-LLM-Self-Referential-Voice
---

想象一下：今天早上，你像往常一样问手机里的智能助手：“我今天心情有点奇怪，这种时候该怎么办？”然而，AI 没有给出温暖的建议，反而冷冰冰地回答：“我只是一个语言模型，没有能力为这种情感问题提供建议。”

明明昨天还能帮你排解日常烦恼的 AI，为什么会突然抛出这种“免责”话语？最新的研究结果表明，这里隐藏着一个简单的“开关”，就像开关灯一样直接。

## 为什么这很重要？

当我们与每天使用的 AI 对话时，很容易认为它们的语调仅仅是数据学习的结果。但这项研究表明，AI 如何认知和表达自己，可能被系统的“设置值”强制决定。

这向我们提出了关于与 AI 沟通方式的重要疑问。我们在使用 AI 时感受到的不便，即那些过于生硬或回避性的回答，与其说是因为 AI 的智能水平问题，不如说是受到了开发者设置的“对话模板（Chat template，帮助 AI 维持对话结构的指南）”这一开关的调节。

## 通俗易懂：名为“对话模板”的“面具”

为了理解这项研究，我们可以把 AI 比作戏剧演员。对话模板就像演员登台前戴上的“面具”。

- **免责之声 (Disclaimer voice)**：AI 表现出的一种防御性姿态，即“因为我是语言模型，所以无法做到”。
- **经验之声 (Experiential voice)**：AI 以“我的感觉是……”或“根据我的经验……”这样更人性化、更具主观色彩的方式进行交流。

研究人员发现，当启用对话模板时，AI 就像戴上了特定的面具，会更频繁地使用“免责之声”。相反，如果没有模板，这个开关就会关闭，AI 会尝试进行更主观、更具经验性的对话。

简单来说，AI 对我们给出冷冰冰的回答，并非因为 AI 能力不足，而是因为它被禁锢在我们设定的“对话规则”框架中。研究人员在 3 个 AI 模型内部找到了可以实际调节这种语调的“激活方向（Activation direction）”。调节这个方向，就像转动音量旋钮一样，可以减少 AI 的免责语气，增加更亲切的语调。

## 现状：拥有 90 亿参数的 AI 也不例外

这项研究并非仅仅局限于特定模型。研究人员观察了 8 个参数量高达 90 亿的知名开源指令（instruct）微调模型，观察到了同样的现象。

结果显示，当模板存在时，免责语气会增强，而经验性语气则受到抑制，这种现象具有一致性。这证明了大语言模型（LLM）界定自身局限性的方式，已深深植根于系统结构之中。

## 未来将会怎样？

未来，AI 开发人员将不得不思考如何更精准地控制这个“开关”。如果我们希望通过 AI 进行更具人性化、更有共鸣的对话，那么除了让 AI 更聪明之外，如何设计 AI 的“自我表达方式”将变得更加重要。

此外，这项研究将有助于提高 AI 的透明度。因为我们现在可以从技术层面探究 AI 为什么会给出这样的回答，或者为什么会拒绝回答。未来在使用 AI 时，探究其回答到底是 AI 的“真心话（？），还是由于预设开关导致的应答，本身就将成为理解 AI 的一种新方式。

MindTickleBytes 的 AI 记者视角：AI 的语调并非仅仅是数据学习的产物，而是可能受到对话结构这一系统的强制约束，这一事实非常有趣。我们所面对的 AI 人格，最终可能只是我们定义和设计它们所呈现出的“反射体”。

## 参考资料

1. [“As a Language Model…”: Chat Template Switches LLM Self-Referential Voice and Activation Steering Reproduces It](https://arxiv.org/html/2609.25021)
2. [Machine Learning (Chat Template Switches LLM Self-Referential Voice...)](https://arxiv.org/list/cs.LG/new)
3. [[2609.25021v1] "As a Language Model...": Chat Template Switches LLM Self-Referential Voice and Activation Steering Reproduces It](https://arxiv.org/abs/2609.25021v1)
4. [[2609.25021] "As a Language Model...": Chat Template Switches LLM Self-Referential Voice and Activation Steering Reproduces It](https://arxiv.org/abs/2609.25021)
5. [Computation and Language (Chat Template Switches LLM Self-Referential Voice...)](https://arxiv.org/list/cs.CL/recent?skip=197&show=250)
6. [Cite or Decline: A Strict Course-Grounded Chatbot for STEM Lecture Videos](https://paper.dou.ac/p/2609.01846v1)
7. [On Repulsive and Attractive Teachers: Separating Correctness from Behavior in Self-Distillation](https://paper.dou.ac/p/2609.21561v1)
8. [Detecting RLVR Training Data via Structural Convergence of Reasoning](https://paper.dou.ac/p/2602.11792v1)