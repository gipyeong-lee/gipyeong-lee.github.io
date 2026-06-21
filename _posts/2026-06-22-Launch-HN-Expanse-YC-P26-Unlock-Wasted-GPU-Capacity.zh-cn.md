---
layout: post
title: "AI 训练无需疯狂购买 GPU？揭秘找出“被浪费算力”的诀窍"
description: "了解企业如何更高效地使用现有的 AI 基础设施，探索 Expanse 带来的 GPU 计算效率未来。"
summary: "Expanse 是一个 AI 基础设施智能层，通过分析 AI 训练中不可或缺的 GPU 基础设施的实时状态来发现被浪费的性能，帮助企业在无需购买新硬件的情况下，将效率提升最高 30%。"
tags: [AI, 基础设施, GPU, 科技, YC]
image: 2026-06-22-Launch-HN-Expanse-YC-P26-Unlock-Wasted-GPU-Capacity.jpg
image_alt: "数据中心中复杂连接的 GPU 服务器示意图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "基础设施优化是 AI 竞赛中看不见的决胜点。这种优先考虑软件效率而非硬件扩张的趋势，将为整个行业带来巨大的成本节约。"
quiz:
  - question: "Expanse 提高 GPU 效率的方式是什么？"
    choices: ["更换更强大的 GPU", "分析实时硬件指标以预测资源分配", "强制降低所有任务的速度"]
    answer: 1
    explanation: "Expanse 安装在服务器上，监控硬件的实时状态，并在提交任务时预测所需资源以进行优化。"
  - question: "Expanse 与哪些系统联动？"
    choices: ["Windows 11", "SLURM 或 Kubernetes (K8s) 等调度程序", "智能手机操作系统"]
    answer: 1
    explanation: "Expanse 连接到数据中心常用的 SLURM 或 Kubernetes 调度程序上运行。"
  - question: "使用 Expanse 可以预期到什么效果？"
    choices: ["无需购买硬件即可提升 GPU 性能", "无限扩展数据中心空间", "互联网速度翻倍"]
    answer: 0
    explanation: "Expanse 通过更有效地利用现有基础设施，帮助在无需购买新硬件的情况下提升性能。"
lang: zh-cn
ref: 2026-06-22-Launch-HN-Expanse-YC-P26-Unlock-Wasted-GPU-Capacity
---

在近期的人工智能（AI）热潮中，最炙手可热的无疑是图形处理器（GPU，即能快速处理复杂数学运算的硬件）。为了训练人工智能模型，全球各地的企业都在不惜重金抢购 GPU，这就像当年的淘金热时期人们为了采金而疯狂寻找锄头一样。但如果告诉你，你手中现有的 GPU 其实连一半的性能都没发挥出来呢？

今天介绍的这家初创公司 Expanse 就是基于这样一个疑问而诞生的。他们开发了一种“智能层”（即用于控制和管理基础设施效率的软件），旨在让企业无需购买新硬件，仅通过现有的基础设施就能大幅提升 AI 训练效率。[参考资料 1](https://www.ycombinator.com/launches/QCF-expanse-unlock-wasted-gpu-capacity), [参考资料 5](https://expanse.sh/)

## 为什么这很重要？

对于企业而言，AI 训练是一场与“时间”和“成本”的激烈竞争。每张 GPU 的价格一路飙升，维护基础设施的运营成本也相当高昂。但如果通过 Expanse 能将现有资源的效率再提升 30%，会怎样呢？[参考资料 9](https://wainews.com.br/posts/30-mehr-gpu-leistung-wie-expanse-hpc-revolutioniert) 这带来的经济效益相当于投入数十亿元购买新硬件。[参考资料 5](https://expanse.sh/)

此外，性能的可预测性直接关系到服务的稳定性。运营 AI 企业的公司最担心突然的任务中断或系统故障，而 Expanse 能从任务提交阶段开始预测潜在的故障风险，从而帮助预防问题的发生。[参考资料 5](https://expanse.sh/)

## 浅显易懂的解释

我们可以将 Expanse 的角色比作一家大型餐厅的厨房。这个厨房里有几十名顶尖厨师（GPU）。但由于厨房太忙，谁也不知道该把订单交给哪位厨师才能最快完成。订餐（AI 训练任务）源源不断地进来，有的厨师在闲着，有的却超负荷运转忙得汗流浃背。

Expanse 就像这个厨房的“资深经理”。经理会实时查看每位厨师的状态，准确把握每道菜需要的时间，以及谁现在疲惫不堪、中途倒下（发生故障）的概率较高。[参考资料 2](https://news.ycombinator.com/item?id=48356312), [参考资料 5](https://expanse.sh/) 因此，一旦有订单进来，它会立即下达指令：“将此任务交给这位厨师最高效。”最终，整个厨房的烹饪速度大大加快。

技术上，Expanse 会安装在数据中心的所有计算机上，仔细检查硬件的实时状态（DCGM、CUPTI 等）。这类似于为了确认汽车状态而收集仪表盘上显示的各种数值。[参考资料 2](https://news.ycombinator.com/item?id=48356312) 基于这些数据，它会制作一份关于当前基础设施性能的“数字地图”，并为接下来的任务寻找最佳路径。[参考资料 6](https://www.linkedin.com/posts/y-combinator_expanse-is-the-intelligence-layer-for-compute-activity-7457081682429521920-s68c)

## 当前状况

Expanse 是一家得到硅谷顶级加速器 Y Combinator (YC) 支持的初创公司，目前在 AI 行业备受瞩目。[参考资料 2](https://news.ycombinator.com/item?id=48356312), [参考资料 7](https://natural20.com/c/m6r0pc) 他们已经与 SLURM 或 Kubernetes（用于管理数据中心计算机资源的程序）等数据中心标准调度程序联动，在实际的高性能计算（HPC）环境中提升了效率。[参考资料 2](https://news.ycombinator.com/item?id=48356312), [参考资料 5](https://expanse.sh/) 

在硬件本就紧缺的企业中间，“GPU 是新时代的石油”这一说法广为流传，资源获取是战略核心，而 Expanse 正在教授如何不浪费这些珍贵的资源。[参考资料 3](https://ycstartups.co/company/expanse)

## 未来展望

未来，人工智能训练模型将会变得越来越大、越来越复杂。随之而来的是，基础设施的高效管理将成为企业的生存问题，而非选答题。随着 Expanse 在更多大规模集群中得到应用，它将引领一种“软件中心化”的思维方式，即企业不再仅仅靠买入硬件，而是更聪明地优化现有基础设施。我们所使用的 AI 服务能运行得更便宜、更稳定，大概都要归功于这类“资深经理”式的解决方案。[参考资料 5](https://expanse.sh/)

## MindTickleBytes AI 记者视角

将硬件性能发挥到极致的软件技术，一直都在加速人类的技术进步。Expanse 的出现是一个有趣的指标，显示 AI 产业已经从“量变扩张”进入了“质变管理”阶段。

## 参考资料

1. [Launch YC: Expanse - Unlock wasted GPU capacity | Y Combinator](https://www.ycombinator.com/launches/QCF-expanse-unlock-wasted-gpu-capacity)
2. [Launch HN: Expanse (YC P26) – Unlock Wasted GPU Capacity](https://news.ycombinator.com/item?id=48356312)
3. [Expanse · YC Spring 2026](https://ycstartups.co/company/expanse)
4. [progscrape: gpu](https://progscrape.com/?search=gpu)
5. [Expanse | Intelligence Layer for HPC and GPU Clusters](https://expanse.sh/)
6. [Expanse is the intelligence layer for compute infrastructure that...](https://www.linkedin.com/posts/y-combinator_expanse-is-the-intelligence-layer-for-compute-activity-7457081682429521920-s68c)
7. [Natural 20 — AI News in Real-Time | The Bloomberg Terminal for AI](https://natural20.com/c/m6r0pc)
8. [Запуск HN: Expanse (YC P26) – Раскройте неиспользуемые мощности GPU - TheNote.app](https://thenote.app/post/ru/zapusk-hn-expanse-yc-p26-raskroite-neispol-zuemye-moshchnosti-gpu-zzq3ojgwhi)
9. [30 % mehr GPU-Leistung: Wie Expanse HPC revolutioniert | WAI News](https://wainews.com.br/posts/30-mehr-gpu-leistung-wie-expanse-hpc-revolutioniert)