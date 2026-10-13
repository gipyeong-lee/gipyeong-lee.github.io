---
layout: post
title: "AI 更聪明、更快速的秘诀：'3D DRAM' 的崛起"
description: "介绍一项将大幅提升生成式 AI 推理速度的半导体新技术——d-Matrix 的 'Raptor' 3D-DRAM 技术。"
summary: "d-Matrix 公布的 'Raptor' 采用了将运算单元与内存垂直堆叠的 3D-DRAM 结构，通过解决数据移动的瓶颈问题，大幅提升了 AI 的推理性能。"
tags: [AI, 半导体, d-Matrix, 3D-DRAM, HotChips2026]
image: 2026-10-13-D-Matrix-Raptor-3D-DRAM-Accelerator-for-Generative-Inference-at-Hot-Chips-2026.jpg
image_alt: "象征半导体芯片层层堆叠的未来主义风格图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "让内存与运算单元在物理上尽可能靠近，是 AI 加速器的未来。Raptor 作为 HBM 的替代方案，证明了其在能源效率方面的潜力，为 AI 推理基础设施开启了新的可能。"
quiz:
  - question: "d-Matrix 公布的 'Raptor' 技术核心结构是什么？"
    choices: ["水平排列 SRAM", "将运算单元与 DRAM 垂直堆叠", "分布式云服务器"]
    answer: 1
    explanation: "Raptor 是一种 3D-DRAM 结构，将 TSMC 4nm 运算单元与定制 DRAM 以 36 微米间距垂直堆叠在一起。"
  - question: "Raptor 技术与现有的 HBM 相比具有什么优势？"
    choices: ["更高的功耗", "约 1/10 水平的能源效率", "降低数据传输速度"]
    answer: 1
    explanation: "与 HBM 相比，Raptor 能以约 1/10 的功耗实现高效运算。"
  - question: "Raptor 旨在解决的核心问题是什么？"
    choices: ["数据传输过程中产生的 '内存瓶颈'", "互联网连接速度问题", "AI 训练数据不足"]
    answer: 0
    explanation: "Raptor 的设计初衷是为了解决生成式 AI 基础设施中数据移动时的瓶颈问题，即所谓的 '内存墙' 问题。"
lang: zh-cn
ref: 2026-10-13-D-Matrix-Raptor-3D-DRAM-Accelerator-for-Generative-Inference-at-Hot-Chips-2026
---

想象一下，你在图书馆里要找一本非常重要的书。但这本书存放在地下深处的仓库里，而阅览室却在顶楼。如果每借一本书都要爬几十次楼梯，那该有多累？我们现在使用的生成式 AI 也面临着类似的情况。AI 的“大脑”（运算单元）为了从存储信息的仓库（内存）中获取数据而浪费了能量，速度也因“内存瓶颈”而变得缓慢。

在最近举行的“Hot Chips 2026”学术大会上，半导体公司 d-Matrix 公布了一项解决这一困扰的技术——名为“Raptor”的 3D-DRAM 加速器。现在，AI 不需要再为了找数据而奔波到遥远的仓库了。这就好比在 AI 的大脑下方直接贴上了一个书架。

## 为什么这很重要？

当生成式 AI 生成复杂答案时，实际上是在瞬间反复进行将海量数据从内存取出并传输到运算单元的过程。这一过程中产生的数据移动成了制约 AI 性能的巨大障碍，专业术语称之为“内存墙（Memory Wall）”。 [参考资料 d-Matrix Raptor 3D-DRAM Architecture at Hot Chips 2026](https://www.partgenie.ai/insights/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026-9)

为了让我们手机里的 AI 助手反应更快，或者让实时生成复杂视频的 AI 服务变得更便宜，必须推倒这堵墙。Raptor 正是为了突破这一技术限制而诞生的。 [参考资料 d-Matrix's Raptor puts stacked DRAM to work on inference bandwidth](https://runtimewire.com/article/d-matrix-raptor-stacked-dram-inference)

## 易于理解的比喻

简单来说，传统的 AI 芯片就像“厨房和餐厅离得很远的一家餐馆”。厨师（运算单元）想要做菜，必须走很远的路去仓库（内存）取食材。而 Raptor 则像是一位“厨师在手边就能取出食材的最新型开放式厨房”。

Raptor 采用了将 TSMC 4nm 超微工艺制造的运算单元晶片直接贴在定制 DRAM 之上的方式。 [参考资料 Hot Chips 2026: d-Matrix stacks AI accelerator directly on custom DRAM for 100 TB/s per card](https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card) 这被称为“3D-DRAM”结构。由于内存被垂直堆叠在运算单元正下方，数据移动的物理距离被极大地缩短了。 [参考资料 d-Matrix stacks DRAM directly · Hacker News | Zeli](https://zeli.app/story/49695065)

得益于此，Raptor 能够提供每卡 100TB/s（每秒太字节）的惊人数据传输带宽，从而大幅缓解了传统 AI 芯片长期面临的瓶颈问题。 [参考资料 d-Matrix's Raptor 3D-DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)

## 当前现状

根据 d-Matrix 首席技术官 Sudeep Bhoja 在 Hot Chips 2026 上的演讲，该技术是与 Meta 合作开发的。 [参考资料 Hot Chips 2026 - d-Matrix](https://www.d-matrix.ai/event/hot-chips-2026/) 目前的高性能 AI 芯片大多使用名为 HBM（高带宽内存）的昂贵内存，而 Raptor 的一大特点是，它能以仅相当于 HBM 约 1/10 的功耗实现相当甚至更好的性能。 [参考资料 d-Matrix's Raptor 3D-DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)

不过，这项技术并不会立即取代市场上的所有 HBM。目前 Raptor 专门针对推理（Inference，即已训练好的 AI 实际生成回答的过程）效率进行了优化，预计将成为处理海量数据的整个 AI 基础设施中的重要一环。 [参考资料 d-Matrix's Raptor Chip Hits 105 TB/s in Real Silicon Tests, But It's Not an HBM Replacement Yet](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2p6bnJUdEVSRkNfcUU2bE9OWjlpZ0FQAQ?hl=en-PK&gl=PK&ceid=PK:en)

## 未来展望

我们现在正从仅仅投入“更多电力”的时代，跨越到通过“更高效的结构”来加速 AI 的时代。如果像 Raptor 这样的 3D-DRAM 技术得到普及，你所使用的 AI 服务响应速度将会更快，而功耗则会降低。这也意味着运行 AI 的社会成本正在下降。 [参考资料 d-Matrix's Raptor 3D-DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)

半导体行业未来将以怎样更小、更智能的方式结合内存与运算单元，Raptor 提出的这张新蓝图又将把人工智能的未来引向何方，非常值得期待。

## 参考资料

1. [d-Matrix Raptor 3D-DRAM Accelerator for Generative Inference](https://www.servethehome.com/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026/)
2. [d-Matrix Raptor 3D-DRAM Architecture at Hot Chips 2026](https://www.partgenie.ai/insights/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026-9)
3. [Hot Chips 2026 - d-Matrix](https://www.d-matrix.ai/event/hot-chips-2026/)
4. [Hot Chips 2026: d-Matrix stacks AI accelerator directly on custom DRAM for 100 TB/s per card](https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card)
5. [Hot Chips 2026: d-Matrix Raptor 3D-DRAM - lukebest.github.io](https://lukebest.github.io/papers/hc2026-dmatrix-raptor-3d-dram)
6. [d-Matrix stacks DRAM directly · Hacker News | Zeli](https://zeli.app/story/49695065)
7. [D-Matrix Raptor 3D-DRAM Accelerator for Generative Inference at Hot Chips 2026](https://vk.ru/wall-238001969_5418)
8. [Hot Chips 2026 - Hot Chips 2026](https://hc2026.hotchips.org/?ref=vlsi.kr)
9. [d-Matrix Raptor: 3D-DRAM with 100 TB/s for AI inference](https://www.igorslab.de/en/d-matrix-raptor-3d-dram-over-100-tb-s-stacks-memory-beneath-compute-logic/)
10. [d-Matrix's Raptor 3D DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)
11. [Jobs and Employment at d-Matrix | Simplify Jobs](https://simplify.jobs/c/d-Matrix)
12. [d-Matrix's Raptor 3D DRAM performance - Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2p6bnJUdEVSRkNfcUU2bE9OWjlpZ0FQAQ?hl=en-PK&gl=PK&ceid=PK:en)
13. [d-Matrix's Raptor puts stacked DRAM to work on inference bandwidth](https://runtimewire.com/article/d-matrix-raptor-stacked-dram-inference)