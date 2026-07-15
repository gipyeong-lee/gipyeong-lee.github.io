---
layout: post
title: "AI是“黑盒”？欧洲推出主打透明度的新型AI模型Soofi"
description: "从训练数据到代码完全公开，带您了解透明AI模型Soofi S及其深远意义。"
summary: "德国电信（Deutsche Telekom）旗下的Soofi团队发布了专注于英语和德语的透明开源AI模型“Soofi S”。"
tags: [AI, 开源, 人工智能, Soofi]
image: 2026-07-15-Soofi-Complete-training-code-for-an-open-source-foundation-model.jpg
image_alt: "透明玻璃碎片汇聚成一个智能大脑的数字艺术作品"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在企业普遍将技术视为商业机密的AI行业中，他们选择了“完全公开”这一破局之举。这被视为欧洲旨在提升技术可信度的战略尝试。"
quiz:
  - question: "Soofi S模型最大的特色是什么？"
    choices: ["压倒性的参数数量", "完全的透明度和数据公开", "顶级的韩语性能"]
    answer: 1
    explanation: "Soofi S强调透明度，公开了训练数据来源、训练代码、超参数等开发过程中的一切细节。"
  - question: "Soofi S 30B-A3B模型的“专家混合（MoE）”结构有什么优点？"
    choices: ["始终使用所有参数", "在总共300亿参数中，每个Token仅激活30亿个，效率更高", "只能处理德语"]
    answer: 1
    explanation: "MoE结构通过高效选择部分参数，实现了性能与运算速度的平衡。"
  - question: "Soofi项目目前重点关注的语种是哪些？"
    choices: ["英语和韩语", "英语和德语", "德语和法语"]
    answer: 1
    explanation: "Soofi S专注于英语和德语的双语能力，特别是有意增加了德语数据的训练权重。"
lang: zh-cn
ref: 2026-07-15-Soofi-Complete-training-code-for-an-open-source-foundation-model
---

想象一下，你吃到了一道非常美味的菜肴，却完全不知道它的配方。你不知道用了什么食材、烹饪了多久，甚至不知道用了什么特殊技巧，这就像一个“黑盒”菜肴。

如今的AI行业正是如此。尖端AI模型层出不穷，但这些AI究竟“吃”了什么数据长大、又是如何训练的，却被企业当作商业机密严密封锁。然而，欧洲出现了一个正面挑战这种“秘密主义”的模型。这就是德国电信（Deutsche Telekom）旗下Soofi团队推出的开源AI模型**“Soofi S”**。

## 为什么这很重要？

你可能会想：“只要性能好，用哪个AI不都一样吗？”但在企业办公或公共服务中引入AI时，“可信度”是必不可少的。例如，当你让AI总结公司机密资料时，如果你完全不了解该AI的内部运作机制，自然会感到不安。

Soofi S不仅公开了模型权重（AI大脑中的连接强度）和中间检查结果，甚至连**训练使用的数据来源记录（Data provenance）**都完全公开 [参考资料: [2607.09424] A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424), [参考资料: SoofiS: A SovereignFoundationModelfor German and English](https://www.emergentmind.com/videos/sovereign-open-source-bilingual-llm-cef87c5b)。通过以透明度为武器，使用户能够完全信任并使用AI。

## 轻松理解

让我们用比喻来理解Soofi S的技术特点：

首先，它**“连学霸的学习秘籍都全盘托出”**。通常AI模型只公开结果，但Soofi S连模型训练代码和超参数（AI学习环境设置值）都一并开源 [参考资料: [2607.09424] A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424)。这就像高考状元公开了自己做了哪些练习册、每天学习几小时的详细计划表一样。

其次，它采用了一种名为**“专家混合（Mixture-of-Experts, MoE）”**的智能大脑运作方式。Soofi S 30B-A3B模型虽然总参数量高达300亿，但在回答问题时，实际上只会激活其中30亿个参数 [参考资料: SoofiS 30B activates 3B parameters per token, tops... | UncensoredHub](https://uncensoredhub.ai/news/2026-07-13-soofi-s-30b-activates-3b-parameters-per-token-tops-european-ai-baselines)。这就好比去百货商店时，不会逛遍所有门店，而是直奔目的地“鞋店”一样。这使得它能够更高效、更快速地生成答案。

最后，它接受了**“英语和德语的专属培训”**。Soofi团队并没有盲目追求多语种，而是专注于英语和德语 [参考资料: [2607.09424] A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424)。特别是针对德语，特意调高了训练数据的权重，将德语处理能力发挥到了极致 [参考资料: SOOFI (Soofi S) · innFactory AI Consulting - AI Strategy & Consulting](https://innfactory.ai/en/ai-models/soofi/)。

## 应用场景

Soofi S通过学习约27万亿个Token（AI读取的最小语言单位，类似于拼图碎片）而诞生 [参考资料: Michael Fromm on X](https://x.com/effi288/status/2075904321707798699)。目前，通过Hugging Face（AI模型共享开源平台），任何人都可以查看相关的模型、训练代码和脚本 [参考资料: soofi-project · GitHub](https://github.com/soofi-project)。

不过，由于该模型公开了一切，用户仍需根据自己的用途自行测试数据并验证安全性 [参考资料: Soofi-Project/Soofi-S-Base · Hugging Face](https://huggingface.co/Soofi-Project/Soofi-S-Base)。因为它更接近于提供透明基础的“基座模型（Foundation model）”，而非直接可用的成品AI。也就是说，它就像是一个基本工具箱，厨师可以直接挑选食材并精心调整食谱。

## 未来展望

由欧洲研究人员开发并部署在欧洲境内的Soofi项目 [参考资料: Soofi-Project/Soofi-S-Instruct-Preview · Hugging Face](https://huggingface.co/Soofi-Project/Soofi-S-Instruct-Preview)，预计将引领“主权AI（Sovereign AI，指自主掌握数据和技术主权的AI）”的潮流。这是为了不依赖于特定国家或大型科技企业，利用欧洲自身技术打造透明AI的决心 [参考资料: European researchers releaseSoofiS 30B-A3B, a hybrid Mamba MoE...](https://digg.com/tech/rtt1xh5r)。

未来，Soofi项目将持续发布详细的基准测试分数，以证明模型的性能 [参考资料: Soofi-Project/Soofi-S-Rhine-Preview · Hugging Face](https://huggingface.co/Soofi-Project/Soofi-S-Rhine-Preview)。那个能在源代码层面证明我们所用AI是否真的聪明、是否可信的时代，正离我们越来越近。

## MindTickleBytes的AI记者观察
AI越聪明，人们就越会感到恐惧：“这家伙到底在想什么？”Soofi正在用“透明度”这一技术答案来化解这种恐惧。一个开发过程完全公开的AI，究竟能赢得社会多少信任，我们拭目以待。

## 参考资料
1. [2607.09424] A Sovereign, Open-Source Foundation Model for German and English (https://arxiv.org/abs/2607.09424)
2. Soofi-Project/Soofi-S-Base · Hugging Face (https://huggingface.co/Soofi-Project/Soofi-S-Base)
3. SOOFI (Soofi S) · innFactory AI Consulting - AI Strategy & Consulting (https://innfactory.ai/en/ai-models/soofi/)
4. soofi-project · GitHub (https://github.com/soofi-project)
5. Soofi-Project (Sovereign Open Source Foundation Models) (https://huggingface.co/Soofi-Project)
6. Soofi-Project/Soofi-S-Rhine-Preview · Hugging Face (https://huggingface.co/Soofi-Project/Soofi-S-Rhine-Preview)
7. Soofi-Project/Soofi-S-Instruct-Preview · Hugging Face (https://huggingface.co/Soofi-Project/Soofi-S-Instruct-Preview)
8. Soofi:Completetrainingcodeforanopen-sourcefoundationmodel (https://modernorange.io/item/48918292)
9. SoofiS 30B activates 3B parameters per token, tops... | UncensoredHub (https://uncensoredhub.ai/news/2026-07-13-soofi-s-30b-activates-3b-parameters-per-token-tops-european-ai-baselines)
10. SoofiS: A SovereignFoundationModelfor German and English (https://www.emergentmind.com/videos/sovereign-open-source-bilingual-llm-cef87c5b)
11. European researchers releaseSoofiS 30B-A3B, a hybrid Mamba MoE... (https://digg.com/tech/rtt1xh5r)
12. Michael Fromm on X (https://x.com/effi288/status/2075904321707798699)