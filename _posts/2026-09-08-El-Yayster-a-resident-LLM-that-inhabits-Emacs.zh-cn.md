---
layout: post
title: "介绍 El Yayster：AI 不再仅仅是计算机的“嘴”，而是成为了它的“身体”"
description: "如果 AI 不再仅仅是一个提供答案的助手，而是直接在编辑器中行动、管理代码并控制环境，那会是什么样子？我们来了解一下这种栖息于 Emacs 中的新型 AI：El Yayster。"
summary: "如果说以往的 Emacs AI 工具仅仅扮演了回答用户问题的“嘴”的角色，那么 El Yayster 则赋予了 AI 编辑器的控制权，使其成为能够观察并行动的“身体”。"
tags: [AI, Emacs, ElYayster, 编程]
image: 2026-09-08-El-Yayster-a-resident-LLM-that-inhabits-Emacs.jpg
image_alt: "概念图，展示了 AI 在 Emacs 编辑器环境中主动工作"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这是从工具型 AI 向环境融合型 AI 的转变。我们正从等待用户意图的被动关系，迈向共同协作的代理（Agent）关系，这是一次令人兴奋的跨越。"
quiz:
  - question: "现有的绝大多数 Emacs AI 插件与 El Yayster 的最大区别是什么？"
    choices: ["支持的 AI 模型种类", "AI 是否直接控制 Emacs 环境", "安装方式"]
    answer: 1
    explanation: "El Yayster 超越了简单的对话界面，它能够观察 Emacs 环境并主动使用工具进行控制，充当了“身体”的角色。"
  - question: "El Yayster 用于控制 Emacs 环境的方法是？"
    choices: ["直接云端连接", "受限的 Emacs Lisp 代码", "用户手动输入的宏"]
    answer: 1
    explanation: "El Yayster 使用“受限的（gated）Emacs Lisp”来与 Emacs 环境进行交互。"
  - question: "El Yayster 最推荐的运行环境（happy path）是什么？"
    choices: ["需要 API 密钥的商业云服务", "本地运行的 Ollama", "基于网页浏览器的编辑器"]
    answer: 1
    explanation: "尽管 El Yayster 支持各种 OpenAI 兼容的端点，但它最推荐的方式是使用本地运行的 Ollama。"
lang: zh-cn
ref: 2026-09-08-El-Yayster-a-resident-LLM-that-inhabits-Emacs
---

想象一下：当你早起打开电脑时，你常用的编辑器不再仅仅是一个文档编写空间，而变成了一个与你共同思考并协同工作的伙伴，那会怎样？

迄今为止，我们所使用的大多数 AI 工具都像是一张“嘴”。当我们向它提问（输入）时，它只会将相应的回答吐在文档窗口中。然而，最近一个出现在 Emacs（一种高度可扩展的文本编辑器）环境中的项目带来了非常有趣的变革。它是一个名为 **“El Yayster”** 的实验性工具。

### 为什么这很重要？

以往的 AI 集成功能大多是“问答式”秘书：用户提出问题，AI 展示结果。但 El Yayster 完全颠覆了这种关系。

这项技术的重要性在于“AI 位置”的转变。AI 不再是等待指令的被动助手，而是成为了能够自主感知编辑器内部状态并直接控制环境的“代理（Agent）”。这就像厨师身边不再是只会背诵菜谱的人，而是一位能直接修剪食材、控制火候的熟练学徒。这意味着 AI 可以直接操作编辑器，解决我们那些重复性的工作。[出处: ElYayster – a resident LLM that inhabits Emacs | Modern Orange](https://modernorange.io/item/49602258)

### 通俗理解：从“嘴”到“身体”

我们可以用一个比喻来理解这种变化：

过去的 AI 工具就像电话那头的咨询师，我们描述症状，它用言语告知解决方案。而 **El Yayster 相当于借给了人工智能一个名为 Emacs 的“身体”**。[出处: GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)

这个模型不仅仅是在文本缓冲区中写入内容，它将 Emacs 这一软件环境视为一个活的有机体。[出处: yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md)

1. **观察**：AI 首先观察我的实时环境。
2. **决策**：判断需要采取什么行动。
3. **行动**：利用名为“受限的（gated）Emacs Lisp”（用于操作 Emacs 编辑器的编程语言）的工具来实际操控编辑器。
4. **重复**：确认结果并继续执行下一个任务。[出处: GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)

这就好比我们用鼠标和键盘操作编辑器，AI 现在也能直接点击 Emacs 的按钮并执行命令。

### 现状：如何使用它？

目前，El Yayster 被认为是一项极其独特的尝试，它居住在 Emacs 这一空间中并在此活动。[出处: Branches · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/branches/all)

用户可以将其连接到任何与 OpenAI 兼容的模型，其中最推荐的运行环境（即“Happy Path”）是在本地运行的“Ollama”。[出处: yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md) 这也意味着，无需使用云端 API，你就能在自己的电脑上安全地让 AI 自由地掌控你的编辑器。

当然，必须牢记这仍处于初期实验阶段。对于熟练使用 Emacs 的用户来说，它将成为强大的自动化工具，但鉴于 AI 被赋予了复杂的控制权，用户仍需审慎考量自己愿意将多少编辑环境权限交给 AI。

### 未来将会怎样？

未来，AI 的功能将不再局限于审查我们编写的代码，它极有可能演变为：根据我们设定的规则，AI 自动修改编辑器配置、定位 Bug 并优化项目结构，这些都将成为日常。El Yayster 正是迈向那个未来的一次大胆实验。

我们将能目睹 AI 如何更细腻地操纵编辑器的“身体”，并从中享受更舒适的工作环境，这无疑是一次令人期待的体验。

---

## MindTickleBytes 的 AI 记者视角
El Yayster 的出现是一个极佳的案例，展示了技术工具如何与人类共生。我们正在告别需要人类逐一输入指令的时代，迈向 AI 成为系统一部分并与人类共同呼吸的“居住型 AI（Resident AI）”时代。

## 参考资料
1. [ElYayster – a resident LLM that inhabits Emacs | Modern Orange](https://modernorange.io/item/49602258)
2. [yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md)
3. [GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)
4. [Branches · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/branches/all)