---
layout: post
title: "AI 芯片市场的全新挑战：‘Transformer 专用’ Sohu 芯片能否超越英伟达？"
description: "深度解析威胁英伟达 GPU 的全新 AI 芯片——Etched 的 ‘Sohu’，并通俗易懂地解释其为何专门针对 Transformer 模型进行优化。"
summary: "Etched 公司开发的 ‘Sohu’ 是一款专为 Transformer 模型设计的芯片，相比通用 GPU，它能提供更快、更廉价且更高效的 AI 性能。"
tags: [AI, 硬件, Etched, 英伟达, Sohu]
image: 2026-08-24-Etched-Sohu-vs-Nvidia-Transformer-ASIC-vs-GPU-2026-Spheron-Blog.jpg
image_alt: "象征 Transformer AI 模型结构的半导体芯片未来感图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这是一场通用性与效率之间的博弈。Sohu 在特定任务上展现了极致的效率，但由于放弃了硬件灵活性，它能否跟上 AI 算法的快速演进将是关键所在。"
quiz:
  - question: "Etched 的 Sohu 芯片为何比现有 GPU 更高效？"
    choices: ["因为它配备了更大的内存", "因为它将 Transformer 结构直接设计在硬件中", "因为它使用了更廉价的材料"]
    answer: 1
    explanation: "Sohu 将 Transformer 模型的关键功能直接以硬件电路实现，减少了软件处理过程。"
  - question: "Sohu 芯片专长于哪种任务？"
    choices: ["所有类型的电脑游戏", "Transformer 系列 AI 模型", "高画质视频剪辑"]
    answer: 1
    explanation: "Sohu 是一款仅专注于运行 GPT 或 Llama 等 Transformer 模型的专用芯片（ASIC）。"
  - question: "根据性能对比数据，Sohu 芯片相比现有 GPU 有什么优势？"
    choices: ["速度更慢但更便宜", "相似的速度和能效", "最高可达 20 倍的处理速度"]
    answer: 2
    explanation: "Sohu 声称其相比现有的英伟达 H100 GPU，处理速度最高可提升 20 倍，且具备更高的能效。"
lang: zh-cn
ref: 2026-08-24-Etched-Sohu-vs-Nvidia-Transformer-ASIC-vs-GPU-2026-Spheron-Blog
---

想象一下：清晨醒来，你对手机上的 AI 说：“把今天的 3 个会议资料总结一下，只告诉我核心内容。”目前的 AI 为了完成这项工作，需要经过复杂的计算过程，有时甚至需要等待数秒。但如果这个 AI 的思考方式被直接固化为硬件芯片，让你下达指令的瞬间，0.1 秒内就能得到结果呢？这正是最近 AI 硬件市场正在上演的惊人变革。

### 为什么这很重要？ (Why It Matters)

我们目前使用的大多数强大 AI 都在英伟达（Nvidia）的 GPU（图形处理器）上运行。然而，最近 AI 初创公司 Etched 获得了 103 亿美元（约合 14 万亿韩元）的估值，给市场带来了巨大冲击 [Source 14, Source 15]。原因很简单：他们制造的不是“什么都能做”的万能 GPU，而是只运行 AI 引擎“Transformer”模型的专用芯片——“Sohu” [Source 5, Source 13]。

这一变革之所以重要，是因为它能大幅降低 AI 成本并显著提升速度。有观点称，原本需要 160 台英伟达 GPU 才能完成的庞大工作，现在只需一台搭载 8 枚 Sohu 芯片的服务器即可替代 [Source 1, Source 3]。对于普通用户来说，这明确释放了一个信号：一个能以更低成本享受比现在更快速、更聪明 AI 的时代即将来临。

### 通俗解释 (The Explainer)

我们打个简单的比方。现有的英伟达 GPU 就像一位**“万能厨师”**。他们掌握着韩国料理、西餐、中餐、日式料理等所有菜系，技术非常全面且灵活。但也正因如此，无论做哪道菜，都需要拿出相应的厨具、处理食材等准备时间。用计算机术语来说，这就叫“由软件处理” [Source 4, Source 6]。

相比之下，Etched 的 Sohu 芯片就像一台**“泡菜汤专用机器人”**。它将制作泡菜汤的方法直接固化在机器人的骨架和机械装置中。无需另行取出厨具，只需按下按钮，完美的泡菜汤就会出炉。这就是将 Transformer（一种识别句子中单词之间关系的 AI 结构）这一“菜谱”直接嵌入硬件电路的 Sohu 芯片 [Source 4, Source 5]。

Sohu 将 Transformer 模型理解句子时使用的核心技术——“注意力（Attention）”直接以专用电路实现 [Source 6]。因此，当普通 GPU 在复杂的软件过程中仅仅发挥出 30%~40% 的性能时，Sohu 能将芯片性能的 80%~90% 全力投入到该任务中 [Source 6, Source 7]。

### 现状 (Where We Stand)

Sohu 是采用 4 纳米（nm）工艺制造的顶尖半导体 [Source 2, Source 6]。从目前公布的技术数据来看，其表现相当惊人。据悉，它在处理 Llama 70B 等大规模语言模型时，每秒可处理 50 万个 Token（AI 读取的文字单位） [Source 1, Source 14]。

当然，局限性也很明确。正如“泡菜汤专用机器人”无法制作意面一样，Sohu 也无法执行 Transformer 基础模型以外的任何其他工作 [Source 4, Source 5]。英伟达 GPU 拥有“通用性”这一强大武器，从科学研究到游戏图形处理，什么都能做 [Source 13]。Etched 也明确承认了这一点，并面临着克服复杂混合专家模型（MoE）等任务中出现的局限性的课题 [Source 16]。

### 未来前景 (What's Next)

未来，AI 硬件市场将迎来“通用 GPU”与“特化专用芯片（ASIC）”之间的激烈对决。Etched 已经获得了数亿美元的投资，在市场上证明了该技术的潜力 [Source 6, Source 14]。专家预测，这一趋势有望将 AI 推理（Inference，即已学习的 AI 在处理实际提问的过程）成本降低近 10 倍 [Source 2, Source 3]。

读者朋友们可以关注“会有多少 AI 模型更自然地融入我们的生活”。一旦 Sohu 等高效芯片普及，那些因服务器成本过高而无法企及的高阶 AI 功能，将能更容易地植入我们的手机或日常家电中。

### MindTickleBytes AI 记者的视点
硬件强制性地将特定算法“硬编码”，就好比制造了一台只能完美听懂特定语言的专用翻译机。这一事件标志着 AI 技术已向特定方向完全固化。英伟达的灵活性与 Etched 的高效性，究竟谁能成为更广阔市场的统治者，将是 2026 年科技界最值得关注的看点。

## 参考资料
1. [Etched Sohu vs NVIDIA: Transformer ASIC vs GPU (2026) | Spheron Blog](https://www.spheron.network/blog/etched-ai-sohu-vs-nvidia-transformer-asic-inference/)
2. [Etched’s $500M Sohu Chip Takes Aim at Nvidia](https://theaiworld.org/news/etcheds-500m-sohu-chip-takes-aim-at-nvidia)
3. [Independent AI Chip Companies Challenging NVIDIA in 2026](https://hashrateindex.com/blog/independent-ai-chip-companies-ai-asic-market-part-3/)
4. [Etched Just Raised $300M at a $10.3B Valuation for a Chip That Can Only Run Transformers — And It's Beating Nvidia's Blackwell by 10x](https://www.nguyen-ly-thanh.com/en/blog/etched-sohu-transformer-chip-nvidia-inference-2026)
5. [Etched Sohu: the ASIC born solely to run Transformers](https://foro3d.com/en/2026/mayo/etched-sohu-el-asic-que-nacio-solo-para-ejecutar-transformers.html)
6. [Transformer Chip Startup Etched Exits Stealth: $800M Raised, $1B in Contracts](https://www.techtimes.com/articles/319393/20260630/transformer-chip-startup-etched-exits-stealth-800m-raised-1b-contracts.htm)
7. [AI Startup Etched Unveils Transformer ASIC Claiming 20x Speed-up Over NVIDIA H100 | TechPowerUp](https://www.techpowerup.com/323887/ai-startup-etched-unveils-transformer-asic-claiming-20x-speed-up-over-nvidia-h100)
13. [Etched's Jump From $5B to $20B: What aTransformer-Only AI Chip...](https://carussignal.com/etched-5b-to-20b-transformer-chip-nvidia/)
14. [Etched $300M Sohu Chip Rivals Nvidia H100 | TechPillow](https://www.techpillow.co/blog/etched-sohu-asic-chip-300m-transformer-inference-2026)
15. [AI Chip Startup Etched Reaches 10.3 Billion Valuation to ...](https://explore.n1n.ai/blog/etched-ai-chip-startup-valuation-nvidia-competitor-2026-07-24)
16. [Etched AI Review 2026: Sohu Chip Benchmarks and Limits](https://fast.io/resources/etched-ai-review-2026/)