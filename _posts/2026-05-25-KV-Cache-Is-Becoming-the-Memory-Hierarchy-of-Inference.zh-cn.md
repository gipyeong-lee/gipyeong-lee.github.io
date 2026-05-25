---
layout: post
title: "AI 是如何记住这么多对话内容的？'KV 缓存'与内存的演进"
description: "通俗易懂地解释了像 ChatGPT 这样的 AI 在处理长对话或视频时所使用的核心技术 'KV 缓存（KV Cache）' 的概念，以及为了解决其局限性而出现的全新 AI 内存分层架构。"
summary: "随着 AI 需要处理的信息量呈爆炸式增长，作为传统临时存储库的 'KV 缓存' 正面临极限，并开始向庞大的共享内存系统演进。"
tags: [人工智能, AI内存, KVCache, 英伟达, 技术趋势]
image: 2026-05-25-KV-Cache-Is-Becoming-the-Memory-Hierarchy-of-Inference.jpg
image_alt: "一个巨大的发光大脑结构内部，多层抽屉层层相连、存储着复杂数据的 3D 插画"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "过去计算机发展史中曾经历过的'内存墙（Memory Wall）'在 AI 时代再次出现。有趣的是，基础设施的局限性反而开启了一个超越单个芯片的庞大'分布式共享大脑'的新范式。"
quiz:
  - question: "以下哪项与 KV 缓存大小呈指数级增长的原因关系最远？"
    choices: ["输入的句子长度 (Sequence length)", "AI 模型的神经网络层数 (Number of layers)", "用户的互联网连接速度 (Internet speed)"]
    answer: 2
    explanation: "KV 缓存的大小与句子长度、并发处理量（批处理大小）、模型的层数以及隐藏维度的大小成正比线性增长，与用户的互联网速度没有直接关系。"
  - question: "最近 AI 行业为了解决单个 GPU 内存不足的现象，正在采用哪种新方法？"
    choices: ["完全删除 KV 缓存，每次都从头开始重新计算的方法", "利用快速存储设备（如 NVMe SSD）构建由整个集群共享的'内存分层架构'的方法", "强制将数据分散存储在用户智能手机内存中的方法"]
    answer: 1
    explanation: "将数据分散在从超高速缓存到本地 SSD，再到集群级存储空间并进行重用的'内存分层架构（Memory Hierarchy）'方法正成为新的标准。"
  - question: "代理型 AI（Agentic AI）比传统的简单聊天机器人对内存架构造成更大负担的主要原因是什么？"
    choices: ["因为在生成句子后不能删除状态，且需要在多条判断路径之间快速切换", "因为总是需要同时渲染数百万张高清 3D 图像", "因为 AI 会重复自行开关机的行为"]
    answer: 0
    explanation: "由于代理型 AI 会自行制定计划并探索多种可能性，因此即使在生成单词之后，也无法丢弃过去的上下文（状态），并且必须在多个语境之间快速来回切换，从而造成极大的内存负担。"
lang: zh-cn
ref: 2026-05-25-KV-Cache-Is-Becoming-the-Memory-Hierarchy-of-Inference
---

想象一下，早上醒来后你对人工智能（AI）助手这样说道：“把昨天我给你的那份 100 页的会议纪要和 2 小时的录像视频全部扫描分析一遍，然后只挑出今天必须立刻处理的最重要的 3 项任务。”AI 在短短几秒钟内就给出了完美的摘要。但在这里，我们产生了一个根本性的疑问。AI 究竟是如何分毫不差地“记住”那些海量的过往对话内容和厚如书本的数据的呢？当 AI 逐字逐句地写出回答时，难道它每次都要从头到尾把那 100 页内容重新读一遍吗？

在这种惊人的速度和完美的记忆力背后，隐藏着一项不为普通人所熟知的核心技术。那就是 **“KV 缓存（KV Cache，人工智能存储中间计算结果的临时记忆空间）”**。最近，我们向 AI 提出的问题（提示词）形式与过去简单的搜索完全不同。即使用户只抛出一个简短的问题，最新的 AI 系统在内部也会将可用工具、必须遵守的安全指南以及之前的对话内容等海量背景知识（上下文）一次性发送到充当大脑角色的 GPU（图形处理器）中 [KV 缓存正成为推理的内存分层 | Hacker News](https://news.ycombinator.com/item?id=48169508)。简单来说，这就好比一次性把几十本书塞进脑子里然后开始对话一样。用来处理和记住这些海量数据的专用空间就是 KV 缓存。

然而，随着近期 AI 需要一次性处理的信息量呈爆炸式增长，这种 KV 缓存开始出现膨胀到无法承受的现象。如今，AI 行业已经不再局限于单纯提升半导体大脑（计算速度）的发展，而是正在从根本上颠覆 AI 存储和调用记忆的方式本身。让我们仔细观察这场打破单芯片狭小空间的限制、构建庞大的“内存分层架构（Memory Hierarchy）”的 AI 基础设施大迁徙现场。

## 这为什么重要？代理型 AI 与记忆的局限

我们需要了解的第一个事实是，当前的 AI 技术发展方向已经与过去完全不同。如果说以前的 AI 还停留在只会回答简答题的“模范生”水平，那么现在我们已经进入了由 AI 自行设定复杂目标、并分多步执行任务的 **代理型 AI（Agentic AI，自主行为人工智能）**时代。

这种代理型 AI 并不仅是简单地吐出答案，它会在脑海中不断探索“这个方法对吗？还是那个方法更好？”，面对无数选项进行自我判断和修剪。这就好比在复杂的迷宫中尝试走不同的路线。在这个过程中，AI 推理引擎并不能因为刚刚生成了一个单词（Token），就把刚才的思考（过去的记忆状态）毫无顾忌地扔进垃圾桶 [代理型 AI 如何对现代内存层级结构施加压力 - Briefly](https://briefly.co/anchor/Artificial_intelligence/story/how-agentic-ai-strains-modern-memory-hierarchies)。它必须持续记住过去的分支点（Branch），因此，能够以极快的速度在不同语境状态之间切换的强大且充足的内存是必不可少的 [代理型 AI 如何对现代内存层级结构施加压力 - Briefly](https://briefly.co/anchor/Artificial_intelligence/story/how-agentic-ai-strains-modern-memory-hierarchies)。

不仅如此，在与用户进行多次来回的连贯多轮对话（Multi-turn conversations），或是分析一本厚书那么长的长篇上下文时，只有防止将相同数据重复计算的浪费，才能实现实时服务。例如，像 `AttentionStore12` 这样的系统展示了它们如何通过在多次对话中聪明地重用 KV 缓存，来努力最大化大型语言模型（LLM）的响应性能 [AI 推理存储驱动](https://www.solidigm.com/content/dam/solidigm/en/site/products/technology/2026/ai-inference-csal-b3-dpus/thumbnails/ai-inference-storage-powered-by-csal-on-bluefield-3-dpu.pdf)。如果无法解决这个记忆空间的大小和速度问题会怎样呢？无论 AI 变得多么聪明，也会因为遭遇硬件的物理极限而停止回答，这势必将导致我们必须支付的 AI 服务订阅费暴涨。

## 轻松理解：厨师的厨房与“KV 缓存”

那么，KV 缓存究竟是什么？为何它会成为 AI 技术的这种核心瓶颈（拖慢整体速度的狭窄瓶颈）呢？

AI 写文章的过程在专业术语中被称为“解码（Decode）阶段”。如果采用没有任何优化技术的“标准推理（Standard Inference）”方式，那么 AI 模型每次生成一个新单词时，都必须把包含自己刚刚写下单词在内的、从句子开头到结尾的所有单词之间的关系，每次都一模一样地从头重新计算一遍 [KV缓存机制详解：优化 Transformer 推理效率](https://huggingface.co/blog/not-lain/kv-caching)。

**打个比方就是这样的。** 想象一下你雇佣了一个厨艺精湛但有点死板的厨师（标准推理模式的 AI）。这位厨师在准备 10 道菜的套餐时，在做完第一道菜后，会把剩下的已经完美处理好的胡萝卜和洋葱全部扔进垃圾桶。然后，在做第二道菜时，他会从冰箱里拿出沾着泥土的新胡萝卜和洋葱，从头开始重新清洗和处理。随着套餐上一道道菜的推进，准备料理的时间将会呈指数级拉长。

为了防止这种可怕的低效率现象，闪亮登场的救场投手正是“KV 缓存”机制。这项技术会将解码阶段辛辛苦苦计算出来的中间状态值（处理好的食材）存储在缓存（临时保管库）中，从而在生成下一个单词时跳过不必要的重复计算 [掌握 LLM 技术：推理优化 | NVIDIA 技术博文...](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/)。也就是说，这是变聪明的厨师把洗净切好的食材集中放在自己最顺手的 **“料理台正前方的临时保鲜盒（KV 缓存）”**里，并在需要时随时取用的方式 [KV缓存机制详解：优化 Transformer 推理效率](https://huggingface.co/blog/not-lain/kv-caching)。

问题在于，这个“料理台前的保鲜盒”的大小并不是无限的。在最新的人工智能中，KV 缓存的大小会与输入的句子长度、一次处理的问题数量、人工智能大脑结构的层（Layer）数，以及处理数据的维度大小成正比，老老实实地增长 [现代 LLM 中隐藏的瓶颈](https://bilwasiva.github.io/2026-01-09-kv-cache/)。当您向 AI 输入一份厚厚的公司报告的那一瞬间，仅仅为了临时保存数据，高达一部高清电影容量级别的千兆字节（Gigabytes）超高速内存就在眨眼间蒸发殆尽 [现代 LLM 中隐藏的瓶颈](https://bilwasiva.github.io/2026-01-09-kv-cache/)。

正因如此，从硬件设计的角度来看，在处理百万字以上的书籍或长视频时，最致命的限制条件不再是人工智能芯片的聪慧计算能力，而恰恰是这种“KV 缓存空间的不足” [NVIDIA Rubin CPX 解析：处理长上下文推理的 GPU...](https://www.spheron.network/blog/nvidia-rubin-cpx-long-context-inference/)。负责计算的大脑虽然足够快，但输送记忆的管道却被堵塞，导致整个系统卡顿，这就是所谓的“以读取为主（Read-heavy）”的瓶颈现象 [通过动态 KV 缓存放置加速 LLM 推理](https://arxiv.org/html/2508.13231v1)。可以说，过去在计算机工程界阻碍计算机发展速度的“内存墙（Memory Wall）”现象，如今在 AI 时代以 KV 缓存之名华丽复活了 [“内存墙”回归：KV 缓存如何改变硬件](https://strongmocha.com/ai-infrastructure-data-centers/kv-cache-hardware-planning/)。

## 现状：突破狭小的 GPU 空间，构建分层架构

在此之前，工程师们曾试图想方设法将这些海量的 KV 缓存数据全部塞进显卡（GPU）内部昂贵且极快的超高速内存中。然而，随着进入数千万人同时与 ChatGPT 进行长篇对话的时代，试图将这些庞大记忆仅仅死命压缩进 GPU 或单台计算机系统内存中的尝试，在物理上和经济上都陷入了僵局 [通过 KV 缓存卸载扩展 AI 推理：为什么存储正成为下一代 AI 系统的关键驱动力 | 三星半导体全球](https://semiconductor.samsung.com/news-events/tech-blog/scaling-ai-inference-with-kv-cache-offloading-why-storage-is-becoming-a-key-enabler-for-next-generation-ai-systems/)。因为在庞大的最新 AI 模型环境中，KV 缓存数据在眨眼之间就会超过单颗芯片所具备的内存容量极限 [研究报告：利用 NVIDIA 推理平台改进推理](https://nand-research.com/research-note-improving-inference-nvidias-inference-context-memory-storage-platform/)。

为了突破这个巨大的难关，AI 基础设施业界全新亮出的武器正是引入 **“内存分层架构（Memory Hierarchy）”**。

**这次我们用图书馆来打个比方。** 假设您正在国家图书馆撰写一篇非常庞大的论文。马上 1 分钟后要读的 10 本书，您会放在眼前的“书桌上（最快但最窄的 GPU 内存）”。但是如果书桌空间满了，今天下午要读的 50 本书就会被插进紧靠背后的“个人书架（普通计算机内存 DRAM 或本地 SSD）”上。而明天暂时不需要的数百本书，则会被保存在“图书馆地下书库（集群共享的大容量存储）”里，当有请求时，就会通过自动传送带快速送达。也就是为每个空间设计不同的访问速度和可存储容量。

目前最尖端的 AI 系统也正是这样进化的。AI 半导体领域的绝对霸主英伟达（NVIDIA）与 Weka、Vast Data 等专注于大容量数据存储设备的企业联手，正在无止境地拓宽这种内存分层架构的边界 [挑战：为什么 KV 缓存很难管理 - Pynomial](https://pynomial.com/2025/09/the-challenge-why-kv-cache-is-hard-to-manage/)。例如，英伟达名为 ICMSP 的平台，将以前根本无法想象的 NVMe SSD（计算机的大容量永久存储设备）区域，干脆像 AI 内存的一部分一样捆绑在一起。这样一来，即使用户和 AI 的一次对话结束，记忆也不会蒸发，而是以永久状态安全地保存在存储中，在下一次对话（推理运行，Inference runs）开始时立即再次复苏 [Nvidia 将 AI 推理上下文推送到 NVMe SSD](https://www.blocksandfiles.com/ai-ml/2026/01/06/nvidia-pushes-ai-inference-context-out-to-nvme-ssds/4090444/)。

不仅是文本。为了让 AI 能够理解实时涌入海量视觉信息的流媒体视频，像被提出的“HERMES”框架这样的最新研究成果值得关注。这项研究证明了，根据视频画面中时间信息的重要性，将 KV 缓存聪明地压缩并重用为多层分层结构（Hierarchical memory framework）的方法已经可行 [[2601.14724] HERMES：作为高效流视频理解分层内存的 KV 缓存](https://arxiv.org/abs/2601.14724)。像这样跨越超高速芯片，将缓存自然地流入 DRAM 等相对较慢但容量充足的分层存储设备中的技术，如今已成为 AI 学术界最热门的核心课题 [\name：面向低延迟的 KV 缓存原生存储分层架构](https://arxiv.org/html/2509.00105v1)。

## 未来将如何发展？超越单芯片，走向“集群共享大脑”

这种技术潮流最终将导致彻底打破单台服务器计算机的物理限制。因为无论是一台多么昂贵的计算机（Node），仅仅依靠内部装配的零件，已经完全无法承受呈指数级增长的对话上下文（Context）长度以及从全球涌入的连接人数。此外，插在单台计算机上的存储设备（本地 SSD）在与其他计算机相互传输数据和共享时，其结构也是非常封闭和拥堵的 [为 AI 工厂的推理增压：作为内存分层问题的 KV 缓存卸载](https://www.min.io/blog/supercharging-inference-for-ai-factories-kv-cache-offload-as-a-memory-hierarchy-problem)。

因此，下一阶段的结构演进正朝着摆脱单台计算机边界（Boundary）的束缚，将内存层级扩展到由数千台计算机连接而成的整个庞大网络的方向发展 [为 AI 工厂的推理增压：作为内存分层问题的 KV 缓存卸载](https://www.min.io/blog/supercharging-inference-for-ai-factories-kv-cache-offload-as-a-memory-hierarchy-problem)。通过这种方式，用户提出问题并获得答案的过程（推理）不再是被绑定在某一个特定芯片上处理，而是像云朵一样可以改变形态，以流动的（Fluid）方式进行处理 [为 AI 工厂的推理增压：作为内存分层问题的 KV 缓存卸载](https://www.min.io/blog/supercharging-inference-for-ai-factories-kv-cache-offload-as-a-memory-hierarchy-problem)。

时至今日，KV 缓存终于摆脱了被困在单个 GPU 狭小房间里的“个人临时文件夹”的命运。如今，它正在蜕变成一个整个足球场大小的庞大数据中心——也就是集群（Cluster）内所有设备在需要时都能随时访问并提取的“可扩展的庞大共享资源” [为重用而架构：深入探索 KV 缓存的内核](https://blog.everpuredata.com/purely-technical/cut-llm-inference-costs-with-kv-caching/)。

在最尖端的软件生态系统中，能将这种如同科幻电影般的愿景变成现实的工具早已如瀑布般涌现。诸如 `vLLM × Mooncake`、`LMCache MP`、`SGLang` 等开源项目正在相互积极配合以推动技术发展 [KV 缓存正成为推理的内存分层 | Touchdown Labs](https://touchdown-labs.com/blog/kv-cache-memory-hierarchy-inference.html)；而像 Tensormesh 这样极具创新力的初创公司，为了实现 AI 的高速处理，从一开始就致力于迅速商业化横跨存储分层、将数据融合为一的“分布式 KV 缓存系统” [炫酷初创公司：Tensormesh 推出面向高吞吐量推理的分布式 KV 缓存系统](https://bizety.com/2025/12/06/cool-startup-tensormesh-introduces-distributed-kv-cache-system-for-high-throughput-inference/)。

还记得过去我们在配置个人组装电脑时，仔细计较 L1/L2 缓存、RAM 容量、SSD 速度以达到平衡的日子吗？在不久的将来，当设计 AI 系统时，能够自由跨越各种 AI 模型和多个硬件层级的“分布式缓存”技术，也将理所当然地成为一种最基本的标准组件 [炫酷初创公司：Tensormesh 推出面向高吞吐量推理的分布式 KV 缓存系统](https://bizety.com/2025/12/06/cool-startup-tensormesh-introduces-distributed-kv-cache-system-for-high-throughput-inference/)。这种此前一直被掩盖在芯片组演进光芒之下的“KV 缓存分层”的崛起，正在不知不觉中促使计算机硬件的整个历史从底层开始被重新改写 [“内存墙”回归：KV 缓存如何改变硬件](https://strongmocha.com/ai-infrastructure-data-centers/kv-cache-hardware-planning/)。

## MindTickleBytes AI 观点

仅仅是一个“一次性临时存储库”的 KV 缓存，如今却在撼动整个庞大硬件基础设施产业的范式，这一事实非常有趣且具有象征意义。

这与生物大脑的进化过程极为相似。就像人类的大脑会将每时每刻接收到的视听信息短暂停留在短期记忆中，然后将重要的信息转移到长期记忆，并在需要的瞬间从潜意识中迅速提取出来一样。人工智能的物理结构也正在演变成一种类似于生物大脑复杂记忆机制的庞大多层分层架构。

我们曾以为，单颗 AI 芯片无法承受的硬件“物理极限”会成为阻挡技术发展的壁垒。但矛盾的是，这种局限性反而促成了将全世界无数 AI 芯片和存储设备连接在一起的契机。如今，AI 正在超越单个芯片，步入整个数据中心像一个生命体般运作的更大、更灵活的“分布式共享大脑（Distributed Shared Brain）”时代。未来，这个庞大的共享大脑将会向我们展示怎样更加深邃和长远的洞察力，其令人惊叹的下一阶段演化着实令人无比期待。

---

## 参考资料

1. [KV 缓存正成为推理的内存分层 | Hacker News](https://news.ycombinator.com/item?id=48169508)
2. [KV 缓存正成为推理的内存分层 | Touchdown Labs](https://touchdown-labs.com/blog/kv-cache-memory-hierarchy-inference.html)
3. [为 AI 工厂的推理增压：作为内存分层问题的 KV 缓存卸载](https://www.min.io/blog/supercharging-inference-for-ai-factories-kv-cache-offload-as-a-memory-hierarchy-problem)
4. [通过 KV 缓存卸载扩展 AI 推理：为什么存储正成为下一代 AI 系统的关键驱动力 | 三星半导体全球](https://semiconductor.samsung.com/news-events/tech-blog/scaling-ai-inference-with-kv-cache-offloading-why-storage-is-becoming-a-key-enabler-for-next-generation-ai-systems/)
5. [[2601.14724] HERMES：作为高效流视频理解分层内存的 KV 缓存](https://arxiv.org/abs/2601.14724)
6. [为重用而架构：深入探索 KV 缓存的内核](https://blog.everpuredata.com/purely-technical/cut-llm-inference-costs-with-kv-caching/)
7. [挑战：为什么 KV 缓存很难管理 - Pynomial](https://pynomial.com/2025/09/the-challenge-why-kv-cache-is-hard-to-manage/)
8. [通过动态 KV 缓存放置加速 LLM 推理](https://arxiv.org/html/2508.13231v1)
9. [\name：面向低延迟的 KV 缓存原生存储分层架构](https://arxiv.org/html/2509.00105v1)
10. [炫酷初创公司：Tensormesh 推出面向高吞吐量推理的分布式 KV 缓存系统](https://bizety.com/2025/12/06/cool-startup-tensormesh-introduces-distributed-kv-cache-system-for-high-throughput-inference/)
11. [研究报告：利用 NVIDIA 推理平台改进推理](https://nand-research.com/research-note-improving-inference-nvidias-inference-context-memory-storage-platform/)
12. [“内存墙”回归：KV 缓存如何改变硬件](https://strongmocha.com/ai-infrastructure-data-centers/kv-cache-hardware-planning/)
13. [Nvidia 将 AI 推理上下文推送到 NVMe SSD](https://www.blocksandfiles.com/ai-ml/2026/01/06/nvidia-pushes-ai-inference-context-out-to-nvme-ssds/4090444)
14. [KV缓存机制详解：优化 Transformer 推理效率](https://huggingface.co/blog/not-lain/kv-caching)
15. [现代 LLM 中隐藏的瓶颈](https://bilwasiva.github.io/2026-01-09-kv-cache/)
16. [NVIDIA Rubin CPX 解析：处理长上下文推理的 GPU...](https://www.spheron.network/blog/nvidia-rubin-cpx-long-context-inference/)
17. [AI 推理存储驱动](https://www.solidigm.com/content/dam/solidigm/en/site/products/technology/2026/ai-inference-csal-b3-dpus/thumbnails/ai-inference-storage-powered-by-csal-on-bluefield-3-dpu.pdf)
18. [掌握 LLM 技术：推理优化 | NVIDIA 技术博文...](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/)
19. [代理型 AI 如何对现代内存层级结构施加压力 - Briefly](https://briefly.co/anchor/Artificial_intelligence/story/how-agentic-ai-strains-modern-memory-hierarchies)