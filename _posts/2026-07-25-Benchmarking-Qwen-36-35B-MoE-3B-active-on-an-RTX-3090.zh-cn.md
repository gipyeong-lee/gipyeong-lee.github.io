---
layout: post
title: "我的电脑能流畅运行 AI 了？从 Qwen 3.6 35B MoE 看本地 AI 的世界"
description: "通过在 RTX 3090 显卡上运行高性能 AI 模型 Qwen 3.6 35B MoE 的实测结果，深入浅出地介绍本地 AI 的应用方法。"
summary: "在 RTX 3090 上运行 Qwen 3.6 35B-A3B 模型，每秒可生成超过 100 个 Token，体验远超一般的 27B 密集模型。"
tags: [AI, 本地LLM, Qwen, RTX3090, 硬件]
image: 2026-07-25-Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090.jpg
image_alt: "在 RTX 3090 显卡上测试 Qwen 3.6 AI 模型性能的画面。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在本地环境中高效运行大模型，在数据隐私和成本方面具有巨大优势。特别是通过 MoE 架构，可以巧妙地克服硬件限制。"
quiz:
  - question: "MoE (Mixture-of-Experts) 架构模型比一般密集模型快的原因是什么？"
    choices: ["因为始终使用所有参数", "因为一次只处理 3B (30亿) 左右的活跃参数", "因为其中只包含为 RTX 3090 优化的代码"]
    answer: 1
    explanation: "MoE 模型在整个模型中只挑选部分专家（参数）进行运作，因此即便模型总规模为 35B，运算时也仅使用约 3B 的活跃参数，从而提高了运算速度 [Source 5]。"
  - question: "在 RTX 3090 上运行 Qwen 3.6 35B-A3B 模型时表现如何？"
    choices: ["每秒 5~10 个 Token", "每秒 50~100 个 Token 以上", "每秒 1,000 个 Token 以上"]
    answer: 1
    explanation: "根据测试结果，根据设置不同，每秒可显示 50 到 100 个以上的 Token 生成速度 [Source 2], [Source 5], [Source 7]。"
  - question: "如果在性能更强的 27B 密集模型和 35B-A3B MoE 模型之间选择，该如何决策？"
    choices: ["35B 模型绝对更好", "如果看重回答质量，建议选择 27B 密集模型", "两者性能完全没有差异"]
    answer: 1
    explanation: "在基准测试结果中，27B 密集模型比 MoE 模型领先 1 到 10 分左右，因此在回答质量优先时更推荐使用 [Source 3]。"
lang: zh-cn
ref: 2026-07-25-Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090
---

想象一下，如果你每天使用的电脑里的 AI 助手，无需联网就能在 1 秒内回答非常复杂的问题，那会怎样？拥有一个不必担心数据泄露、只在自己电脑内安全运行的“专属 AI”，这已不再是科幻电影里的情节。最近推出的强大 AI 模型“Qwen 3.6 35B-A3B”是如何将这一切变为现实的呢？我们用连高中生都能理解的方式为你拆解。

### 为什么这很重要？(Why It Matters)

过去，高性能 AI 模型体量庞大，普通用户的电脑根本无从谈起。但现在情况不同了。“本地 AI（无需联网、在用户设备上直接运行的 AI）”技术突飞猛进，仅凭家中现有的 RTX 3090 这样的显卡，就足以体验高水平的 AI [Source 8]。

本地 AI 备受关注的原因主要有两点。首先是**隐私**。你的数据不会流向外部服务器，而是直接在你的电脑内处理，因此更加安心。其次是**速度与经济性**。不受网速影响，运行流畅；只要下载一次模型，无需额外支出即可随心使用。此次测试的 Qwen 3.6 35B-A3B 模型在本地 AI 环境中表现出了卓越的性价比和性能，备受瞩目 [Source 6]。

### 通俗解释 (The Explainer)

Qwen 3.6 35B-A3B 模型的核心在于一种名为 **MoE（Mixture-of-Experts，专家混合架构）**的特殊设计。

我们来做一个简单的比喻。假设你正在管理一个巨大的图书馆，如果所有书都由一名管理员负责，他肯定会力不从心。于是，你雇佣了多名领域专家管理员。在这里，“35B”指的是管理员总数（总参数量），而“3B active”则代表当问题输入时，为了寻找答案而实际调用的管理员人数（活跃参数量） [Source 5]。

普通的“密集模型 (Dense Model)”是每位管理员都要参与工作的结构，而 MoE 模型则根据问题的内容，只调用相关领域的专家。多亏了这一点，模型虽然拥有 350 亿个参数，显得非常聪明，但实际工作时只需要计算 30 亿个参数，从而能够极快地给出结果 [Source 5]。

### 现状 (Where We Stand)

最近在实际 RTX 3090 显卡上进行的基准测试结果令人惊叹。

* **速度**：应用特定设置（UD-Q4_K_XL 量化）后，短问题生成速度约为每秒 101.7 个 Token（AI 生成文本的单位），长问题生成速度约为每秒 80.9 个 Token [Source 7]。在其他环境下也能稳定保持每秒 50~100 个 Token 的水平，这比 27B 密集模型（每秒约 35 个 Token）快得多 [Source 5]。
* **局限**：当然，体量大、速度快的 MoE 模型并不总是最优解。与 27B 密集模型相比，在回答的准确度（质量）方面，27B 密集模型在基准测试结果中高出 1 到 10 分左右 [Source 3]。换句话说，如果最看重速度，选择 MoE 模型；如果最看重回答质量，选择密集模型是更明智的选择 [Source 3]。
* **优化**：此外，在 RTX 3090 这类环境下，AI 学习技巧之一的“推测解码 (Speculative Decoding)”对速度提升的帮助其实并不显著 [Source 4]。

### 未来会怎样？(What's Next)

未来，本地 AI 技术将变得更加轻便、更加智能。此次测试的专家们正在分享各种根据用户 PC 配置高效驱动模型的设置方法 [Source 3], [Source 11]。用户如今不再仅仅处于挑选优秀模型的阶段，而是根据显卡性能选择最佳的“量化（通过调节数据精度来缩小模型大小的技术）”级别，亲自调整出属于自己的 AI 环境的时代已经到来 [Source 2], [Source 14]。

### MindTickleBytes 的 AI 记者视角

本地 AI 不仅仅是技术上的成就，更是夺回“设备主权”的过程。Qwen 3.6 35B-A3B 这类高效模型的出现，正加速开启一个人人都能在个人 PC 上无需高价服务器即可享受高性能 AI 的未来。AI 不再是远在天边的大企业服务器，而是逐渐成为你桌面上与你同呼吸的伙伴。

## 参考资料

1. [Qwen/Qwen3.6-35B-A3B · My RTX 3090 ran out of excuses: Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/discussions/37)
2. [Qwen 3.6-35B-A3B Local Hardware Guide — GPU & VRAM (2026) | Compute Market](https://www.compute-market.com/blog/qwen-3-6-local-hardware-guide-2026)
3. [GitHub - tfriedel/qwen3.6-rtx3090-lab: Benchmarks, compose files, and findings for running Qwen3.6 (27B dense + 35B-A3B MoE) on 4× RTX 3090](https://github.com/tfriedel/qwen3.6-rtx3090-lab)
4. [GitHub - thc1006/qwen3.6-speculative-decoding-rtx3090](https://github.com/thc1006/qwen3.6-speculative-decoding-rtx3090)
5. [Best Way to Run Qwen 3.6 35B MoE Locally: VRAM, Speed, Setup | InsiderLLM](https://insiderllm.com/guides/best-way-run-qwen-3-6-35b-moe-locally/)
6. [I Benchmarked Qwen3.6–35B-A3B Model on 3090, 4090, 5090 and M5 Max. Here’s What Nobody Tells You. | Medium](https://medium.com/@ttio2tech_28094/i-benchmarked-qwen3-6-35b-a3b-model-on-3090-4090-5090-and-m5-max-heres-what-nobody-tells-you-62fbb2f4e64a)
7. [Qwen 3.6 Complete Guide: 27B Dense, 35B-A3B MoE, and Which to Use | InsiderLLM](https://insiderllm.com/guides/qwen-3-6-local-ai-guide/)
8. [Benchmarking Qwen 3.6 35B MoE (3B active) on an RTX 3090](https://www.gilesthomas.com/2026/07/benchmarking-qwen-3-6-35b-moe-rtx-3090)
9. [From 25 to 283 tok/s: Serving Qwen3.6 on Dual RTX 3090s](https://alexander-ollman.github.io/qwen3.6-on-rtx3090/qwen3.6-on-rtx3090.html)
10. [Qwen3.614B A3BFableVibes benchmarked and tested vs... - YouTube](https://www.youtube.com/watch?v=DBEd5dpxaNQ)
11. [Qwen/Qwen3.6-35B-A3B· Hugging Face](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
12. [Qwen3.635B-A3BonRTX3060 12GB: Local LLM | SpecPicks](https://specpicks.com/reviews/qwen-36-35b-a3b-rtx-3060-12gb-local-2026)
13. [ЗапускаемQwen3.635B-A3B+ opencode локально наRTX... / Хабр](https://habr.com/ru/articles/1026482/)
14. [Qwen3.627B vs35B-A3BMoEMTP наRTX5080 16GB... | AiManual](https://ai-manual.ru/article/rtx-5080-16gb-qwen36-27b-mtp-ili-35b-a3b-moe-mtp---chto-vyibrat-dlya-lokalnogo-kodinga/)