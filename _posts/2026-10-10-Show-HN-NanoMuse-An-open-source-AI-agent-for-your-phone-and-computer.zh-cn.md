---
layout: post
title: "跨越手机与PC的‘个人AI助手’，nanoMuse来了"
description: "了解开源AI智能体 nanoMuse，它能自由穿梭于智能手机和计算机之间处理工作。"
summary: "介绍完全开源的个人AI智能体 nanoMuse，它能统一管理智能手机和PC，即使在应用关闭后也能自主持续工作。"
tags: [AI, 开源, 个人助手, 智能体]
image: 2026-10-10-Show-HN-NanoMuse-An-open-source-AI-agent-for-your-phone-and-computer.jpg
image_alt: "在智能手机和计算机屏幕上有机运行的AI智能体 nanoMuse 的概念图。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "打破设备间壁垒并能始终记忆用户上下文的智能体的出现，将成为迈向真正个性化时代的重要里程碑。"
quiz:
  - question: "nanoMuse 的核心特性之一是什么？"
    choices: ["基于付费订阅的封闭式服务", "穿梭于用户的手机和计算机之间执行任务", "仅限企业级大型服务器专用的模型"]
    answer: 1
    explanation: "nanoMuse 是一款能在用户拥有的所有设备（包括手机和计算机）上实现有机运行的个人智能体。"
  - question: "nanoMuse 与其他AI应用有何不同之处？"
    choices: ["即使关闭应用，任务也不会停止，而是持续进行", "只能使用 OpenAI 的模型", "仅在智能手机上运行"]
    answer: 0
    explanation: "nanoMuse 的一大优势在于，即使关闭了应用程序，它也能在后台自主持续执行任务。"
  - question: "nanoMuse 遵循什么许可协议？"
    choices: ["商业专有许可", "GPL-3.0 开源许可", "限制性开源"]
    answer: 1
    explanation: "nanoMuse 是一个完全开源的项目，遵循 GPL-3.0 许可协议。"
lang: zh-cn
ref: 2026-10-10-Show-HN-NanoMuse-An-open-source-AI-agent-for-your-phone-and-computer
---

想象一下。早上醒来，你对AI说：“帮我整理今天上午的会议资料并发邮件，然后按照下午的日程在我的PC上准备好文件。”在过去，当你试图将手机上的工作同步到PC上继续时，往往因为AI无法记住之前的上下文，而不得不重新解释一遍，非常麻烦。但现在，一个打破手机与电脑界限、成为你手脚的“真正个人助手”诞生了。这就是开源AI智能体项目——**nanoMuse**。

## 为什么这很重要？

我们生活在一个同时使用手机、笔记本电脑和台式机等多种设备的时代。然而，由于各设备的操作系统和应用程序各不相同，且各自的AI彼此独立，设备间总是缺乏有机的“连接性”。nanoMuse 正是为了解决这一痛点而生。它不仅是一个只会通过聊天给出回答的聊天机器人，其目标是直接控制你的设备并处理实际业务。特别是它并非企业管控的封闭式服务，而是一个任何人都可以查看代码并参与贡献的完全开源项目，这一点备受瞩目 [Source 3, Source 4]。

## 简单理解：nanoMuse 是什么样的存在？

简单来说，nanoMuse 就像是**“你的数字分身”**。

如果说现有的AI模型是拥有名为 Transformer（AI核心结构，用于识别句中单词间关系）这种聪明大脑的秘书，那么 nanoMuse 就是给这位秘书装上了“手脚”。以往的AI被束缚在名为聊天窗口的狭小框架内，而 nanoMuse 则可以在手机和PC屏幕上自由穿梭，移动鼠标并直接操作浏览器 [Source 1, Source 11]。

打个比方，它就像**“管弦乐队的指挥”**。当你指示管弦乐队（手机和PC中的无数应用）演奏什么乐曲时，nanoMuse 会在各个乐器（应用）之间穿梭，翻阅乐谱并调节音色。这里最重要的一点是，即使你关闭了应用，指挥也不会停止，它会在舞台后台准备接下来的顺序 [Source 3, Source 5]。像这样，nanoMuse 会始终记住你的上下文，并且在执行不可逆的操作前，会慎重地通过“要这样进行吗？”来确认你的意图 [Source 3]。

## 现状：进展到什么程度了？

nanoMuse 目前是一个遵循 GPL-3.0 许可协议的完全开源项目。任何人都可以通过[官方网站](https://nanomuse.cn/)或[GitHub](https://github.com/nano-muse/nanoMuse)查看相关源代码，并直接参与项目贡献 [Source 3, Source 4]。

- **卓越的联动性：** 将安卓智能手机与台式机有机连接，由专用App、Web控制台以及连接它们的中继系统构成 [Source 4]。
- **模型的自由度：** 不受特定企业模型的束缚。用户可以根据自己的喜好或环境，自由连接 DeepSeek、OpenAI 或直接安装在自己PC上的 Ollama 模型来使用 [Source 6]。
- **实用功能：** 从目前的浏览器演示来看，它展现了极强的生产力，例如自动填写PDF表格或读取屏幕执行复杂的Web业务 [Source 8]。

当然，目前该项目正处于积极开发阶段，用户可能需要手动设置或具备一定的技术理解力。但这也是 nanoMuse 所拥有的“开放性”与“用户主动权”这一强大优势所带来的必然过程。

## 未来将会怎样？

像 nanoMuse 这样的智能体技术将从根本上改变我们操作设备的方式。我们重复寻找文件、复制粘贴、检查邮件等简单任务，将逐渐交由 nanoMuse 这样的智能体来完成。

用户需要做什么呢？与其费心研究“该怎么做”而翻遍应用和菜单，不如将精力更多地集中在决定“要做什么”这类具有创造性和本质的工作上。nanoMuse 将成为整合你所有设备的巨大枢纽，成为无论身在何处，都能确保你的工作流（Workflow）不被中断的坚实伙伴 [Source 4, Source 6]。

## MindTickleBytes AI记者视角

nanoMuse 不仅仅是“又一个AI工具”。它对抗着在封闭环境下运行的科技巨头AI服务，为用户开辟了一条新道路：在完全掌控自己数据和设备的同时，还能拥有超智能的助手。期待这种打破设备与人类之间壁垒的开放性尝试，能让未来的AI生态变得更加民主和高效。

## 参考资料

1. [2610.08699] nanoMuse: An Open-Source Personal Agent for Every Device You Own (https://arxiv.org/abs/2610.08699)
2. GitHub - nano-muse/nanoMuse: nanoMuse: a fully open-source, Muse-style personal agent for every device you own (https://github.com/nano-muse/nanoMuse)
3. nanoMuse: an open-source personal agent for every device you own (https://nanomuse.cn/)
4. nanoMuse nanoMuse: an open-source personal agent @ codeKK (https://p.codekk.com/detail/swift/nano-muse/nanoMuse)
5. nanoMuse open-source personal agent · shipwithmuse (https://shipwithmuse.live/builds/nanomuse-open-source-personal-agent)
6. nanoMuse: An Open-Source Personal Agent for Every Device You Own (arXiv) (https://arxiv.org/html/2610.08699)