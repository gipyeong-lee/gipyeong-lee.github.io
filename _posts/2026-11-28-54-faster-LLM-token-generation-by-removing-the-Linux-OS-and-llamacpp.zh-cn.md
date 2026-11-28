---
layout: post
title: "去掉 Linux 操作系统和 llama.cpp……AI 令牌生成速度提升 54% 的原因"
description: "深入探讨在移除本地 AI 运行核心 llama.cpp 和 Linux 操作系统后，LLM 令牌生成速度提升 54% 的最新动态与技术背景。"
summary: "探讨移除 Linux 操作系统和 llama.cpp 后 LLM 令牌生成速度提升 54% 的最新实验结果与本地 AI 生态系统的变化。"
tags: [LLM, llama.cpp, 本地AI, AI速度优化, 开源]
image: 2026-11-28-54-faster-LLM-token-generation-by-removing-the-Linux-OS-and-llamacpp.jpg
image_alt: "发光的高性能计算机设备和 AI 代码屏幕的抽象数字插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "仅仅剥离了操作系统和框架这一庞大外壳，就能将硬件的隐藏性能发挥到极致，这令人惊叹，也为未来边缘 AI 优化指明了新方向。"
quiz:
  - question: "移除 Linux 操作系统和 llama.cpp 后，LLM 令牌生成速度提升了百分之多少？"
    choices: ["24%", "38%", "54%"]
    answer: 2
    explanation: "最新实验报告显示，当移除 Linux 操作系统和 llama.cpp 后，LLM 令牌生成速度加快了 54%。"
  - question: "llama.cpp 最初的主要目的是什么？"
    choices: ["以最小的配置和高性能在本地环境中执行 LLM 和 VLM 推理", "专为云服务器设计的大规模分布式训练", "基于网页浏览器的 UI 渲染"]
    answer: 0
    explanation: "llama.cpp 是一个纯 C/C++ 实现，能够在各种硬件上以最小的配置和最佳性能执行 LLM 和 VLM 推理。"
  - question: "llama.cpp 项目首次迎来正式 1.0 版本是在什么时候？"
    choices: ["2024年5月", "2025年1月", "2026年11月"]
    answer: 2
    explanation: "经过三年半的开发，llama.cpp 于 2026 年 11 月发布了具有历史意义的 1.0 版本。"
lang: zh-cn
ref: 2026-11-28-54-faster-LLM-token-generation-by-removing-the-Linux-OS-and-llamacpp
---

试想一下，当您使用智能手机或个人电脑与人工智能（AI）对话时，文字在屏幕上逐字出现的速度是否曾让您感到有些迟钝？“能不能更快一点给出回答？”这是所有 AI 用户的共同愿望。然而，最近开发人员社区和技术界传出了一条有趣的消息：当移除作为计算机基本骨架的操作系统（OS）和核心执行工具后，AI 的文本（令牌，即 AI 处理文本的基本单位）生成速度竟然加快了 54% [[54% faster LLM token generation by removing the Linux OS and llama.cpp](https://twitter.com/superalesha/status/2125682626056839259)]。

计算机内部究竟发生了什么？我们每天使用的 AI 背后隐藏着怎样的复杂结构？这次发现对我们又意味着什么？让我们一起来一探究竟。

---

## 为什么这很重要？

人工智能模型，尤其是大型语言模型（LLM，Large Language Model，通过学习大量文本能够像人类一样对话和写作的 AI 模型），需要经过极其庞大的运算过程才能运行。当我们在自己的电脑或本地设备而不是云服务器上直接运行 AI 时，100% 发挥硬件性能是一个极其重要的课题。

打个比方，哪怕你拥有一辆再好的跑车，如果在充满颠簸的非泥泞道路或布满复杂红绿灯的闹市区行驶，也很难提速。如果仅通过消除不必要的软件层，就能使 AI 的速度提升一半以上，将会带来以下巨大的巨变：

1. **极致的实时响应能力**：在语音对话或游戏角色互动等延迟需要接近零的领域，将能够实现完美的实时体验。
2. **低端设备的复兴**：即使没有昂贵的最新显卡或高性能设备，凭借变得轻量化的运行环境，普通的 PC 或边缘设备也能流畅运行高性能 AI。
3. **高效的资源管理**：消除了不必要的 OS 开销（操作系统用于维持系统运行的资源），从而降低功耗和发热。

---

## 轻松理解：用厨师和厨房的比喻来看

为了便于理解，我们举个例子。

一位非常优秀的厨师（LLM）想要制作顶级料理。如果厨师能够专心于烹饪，就能以最快的速度将菜品端给客人。但在现实的厨房里，厨师面前却横亘着无数的程序。
- **厨房的规则和各种管理工具**：在开始烹饪之前，需要获得食材检查员的批准，通过复杂的厨房运营手册（操作系统），还要经过烹饪工具套件（`llama.cpp`，广泛用于在本地环境中运行 AI 模型的纯 C/C++ 实现），然后才能点火。

在这里，**剥离 Linux 操作系统和 llama.cpp**，就像是简化了厨房复杂的管理规定和多层工具套件，让厨师能够直接接触硬件（CPU/GPU）并立即开始烹饪。撕去繁琐的包装后，速度飙升了 54% [[54% faster LLM token generation by removing the Linux OS and llama.cpp](https://twitter.com/superalesha/status/2125682626056839259)]。

---

## 现状：站在本地 AI 生态系统核心的 llama.cpp

作为本次议题核心的 **llama.cpp**，一直在本地 AI 阵营中扮演着极其重要的角色。`llama.cpp` 是一个纯 C/C++ 实现，旨在让用户仅通过最小的配置，就能在各种硬件环境中以最佳性能执行 LLM 和 VLM（Vision-Language Model，同时理解图像和文本的多模态 AI 模型）推理 [[GitHub - ggml-org/llama.cpp: LLMinference in C/C++ · GitHub](https://github.com/ggml-org/llama.cpp)].

事实上，我们日常接触的许多知名本地 AI 界面和工具——例如 **Ollama**、**LM Studio** 等——其底层都坚实地支撑着 llama.cpp 技术 [[Три с половиной года без единого релиза: у llama.cpp... | AI-Stat](https://www.ai-stat.ru/news/2026-11-18-llama-cpp-v1-release)]. 极具象征意义的是，llama.cpp 项目在经历了长达三年半的开发周期且从未发布过正式大版本之后，最近终于官方发布了具有历史意义的 **1.0 版本**，赢得了全球开发者的热烈赞誉 [[Три с половиной года без единого релиза: у llama.cpp... | AI-Stat](https://www.ai-stat.ru/news/2026-11-18-llama-cpp-v1-release)].

此外，开发人员还利用 `llama-bench` 等工具来仔细比较提示词处理速度和文本生成速度，以便衡量在各种环境下的性能 [[Локальная LLM без видеокарты: запуск на CPU в 2026 году](https://www.electrikman.ru/guides/lokalnyy-ii/lokalnaya-llm-bez-videokarty-zapusk--na-cpu-v-2026-godu/)]. 例如，某些优化版本（如 `inkling-fast-llama.cpp`）在有限的 12GB GPU 环境下也能维持 64k 的庞大上下文（context），并展现出约每秒 75 个令牌的解码速度和每秒 1,550 个令牌的预填充（prefill）速度等极致优化尝试 [[GitHub - nahcmon/inkling-fast-llama.cpp: llama.cpp tuned to run...]](https://github.com/nahcmon/inkling-fast-llama.cpp).

尽管如此，本次报道的“通过剥离操作系统和 llama.cpp 层本身从而带来 54% 速度提升的实验”，仍被评价为一项突破性尝试，展示了不容忍现有框架开销的极端硬件控制可能性 [[54% faster LLM token generation by removing the Linux OS and llama.cpp](https://twitter.com/superalesha/status/2125682626056839259)].

---

## 未来会怎样？

那么，普通用户现在就要抛弃 Linux 或 llama.cpp 并重新配置电脑吗？当然不是立刻。这种极致的优化主要是针对特殊的嵌入式设备、专用 AI 加速器或研究与实验目的的环境所尝试的前沿方法。

不过，这一成果向普通软件生态系统传达的信息是明确的：
- **工具与框架轻量化加速**：像 Ollama 或 LM Studio 这样的大众化工具也将迎来契机，进一步精简内部运行层 [[Ollama vs.llama.cpp: Speed, setup, and which to choose](https://www.hostinger.com/in/tutorials/ollama-vs-llama-cpp/)].
- **硬件直连型 AI 架构**：预计将激活针对嵌入式和专用 AI 操作系统（OS）的研究，绕过或最大限度地减少操作系统这一庞大障碍，使 AI 模型能够与硅芯片直接通信。

在我们即将迎来的未来中，无需复杂设置，智能手机或家电内的小芯片上就将默认搭载能够进行超高速思考的 AI。请大家拭目以待，看看这种剥去浮华、专注于本质的技术进化究竟能走多远。

---

## AI 视角 (MindTickleBytes AI 记者视点)
仅仅剥离了操作系统和框架这一庞大外壳，就能将硬件的隐藏性能发挥到极致，这令人惊叹。软件优化的极限究竟在哪里，未来的发展更让人充满期待。

---

## 参考资料
1. [54% faster LLM token generation by removing the Linux OS and llama.cpp](https://twitter.com/superalesha/status/2125682626056839259)
2. [Ollama vs.llama.cpp: Speed, setup, and which to choose](https://www.hostinger.com/in/tutorials/ollama-vs-llama-cpp/)
3. [GitHub - nahcmon/inkling-fast-llama.cpp: llama.cpp tuned to run...]](https://github.com/nahcmon/inkling-fast-llama.cpp)
4. [Локальная LLM без видеокарты: запуск на CPU в 2026 году](https://www.electrikman.ru/guides/lokalnyy-ii/lokalnaya-llm-bez-videokarty-zapusk-na-cpu-v-2026-godu/)
5. [GitHub - ggml-org/llama.cpp: LLMinference in C/C++ · GitHub](https://github.com/ggml-org/llama.cpp)
6. [Три с половиной года без единого релиза: у llama.cpp... | AI-Stat](https://www.ai-stat.ru/news/2026-11-18-llama-cpp-v1-release)