---
layout: post
title: "能放心给 AI 敏感信息吗？什么是“零数据留存（ZDR）”"
description: "深入浅出地解释了企业为安全使用 AI 而引入的“零数据留存”合同的含义及其局限性。"
summary: "零数据留存（ZDR）是一项强有力的安全协议，承诺 AI 提供商在处理用户数据后立即将其删除，且不会将其用于模型训练。"
tags: [AI安全, 数据隐私, 零数据留存, ZDR]
image: 2026-08-20-Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026.jpg
image_alt: "展示数字安全锁与 AI 模型连接的图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企业在 AI 性能与安全之间寻求平衡的努力值得肯定。必须铭记，ZDR 不仅仅是一项设置，更是一份法律合同。"
quiz:
  - question: "零数据留存（ZDR）的核心承诺是什么？"
    choices: ["将数据保存 30 天", "数据在推理后立即删除，且不用于学习", "公开所有对话内容"]
    answer: 1
    explanation: "ZDR 承诺在完成数据推理后不再保存数据，且不将其用于模型训练或服务改进。"
  - question: "签订 ZDR 合同需要注意什么？"
    choices: ["性能必然会下降", "适用于所有 AI 功能", "有状态（stateful）功能等可能被排除在合同范围之外"]
    answer: 2
    explanation: "ZDR 主要应用于无状态（stateless）路径，复杂的智能体系统功能可能被排除在外。"
  - question: "近期一些模型（如 Claude Fable 5）发生了什么变化？"
    choices: ["强制实施 ZDR", "采取了 30 天数据留存政策而非 ZDR", "完全停止了数据留存"]
    answer: 1
    explanation: "Claude Fable 5 模型已放弃零数据留存政策，为了确保安全性，改用 30 天数据留存政策。"
lang: zh-cn
ref: 2026-08-20-Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026
---

想象一下，你所在的公司正计划利用最前沿的 AI 技术分析一个极其机密的项目的相关数据。然而，当你准备将这些信息输入 AI 时，却感到一丝恐惧。你会担心：“这些数据会被 AI 公司的服务器记录下来吗？未来它会作为对其他人问题的回答而泄露出去吗？”

为了解决这些顾虑，一个名为“零数据留存（Zero Data Retention，简称 ZDR）”的概念应运而生。这真的是能守护我们数据的魔法盾牌吗？

## 为什么这很重要？

在过去，使用公共云服务时，数据留在服务器上被视为理所当然。但对企业而言，将客户的个人信息或公司的核心机密传递给外部 AI 模型本身就是巨大的安全隐患。ZDR 是一种“安全合同”，旨在帮助企业能够放心地在业务中使用前沿 AI 模型（Frontier Models）[来源: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)。通过使用 ZDR，企业可以消除传输数据时留下的“记录标签”，因此它已成为金融、医疗和法律等对安全极其敏感领域的关键选择。

## 轻松理解：患有“健忘症”的助手

打个比方，ZDR 就像聘请了一位“患有健忘症的助手”。

普通的 AI 在用户提问时，会把提问内容和回答存储在服务器上，就像一位细心的秘书把所有对话内容都记录在案一样。但应用 ZDR 意味着与这位秘书签了一份协议：“你只能在听我提问、给我回答的那一瞬间听我的话；回答一结束，就立刻把所有内容从脑海中抹掉。”

供应商通过该合同承诺，在数据推理（AI 生成答案的过程）结束后，不会保存任何数据，也不会将数据用于模型训练或服务改进 [来源: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)。在此过程中，有时甚至连可能导致数据外泄的“监视记录”都不会产生 [来源: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)。

## 到底能相信多少？

ZDR 并非万能灵药。最需要注意的是，**ZDR 不是简单的“设置按钮”，而是法律上的“合同”** [来源: Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/)。

许多用户误以为只要签了 ZDR 合同，所有功能都会得到完美保护。但如果数据通过 AI 的“有状态功能（stateful features，即需要记住前文对话或任务背景的功能）”路径传输，则可能无法享受 ZDR 的保护 [来源: Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/)。这就像助手虽然“当时”抹去了记忆，但如果分配给它需要利用特定“记忆存储空间”的复杂工作，那么相关记录依然会留存下来。

此外，最近的安全政策变化也值得关注。Anthropic 为了加强安全性，针对部分模型引入了 30 天数据留存政策，Claude Fable 5 模型更是放弃了原有的零数据留存政策，转而采用这一 30 天留存政策 [来源: Data retention practices for Covered Models | Anthropic Help Center](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models) [来源: Fable 5's 30-Day Retention: The End of Zero Retention? | Digital Applied](https://www.digitalapplied.com/blog/fable-5-30-day-data-retention-zdr-enterprise-2026)。

## 未来展望

未来，AI 安全市场将进一步细分。企业将采用混合方式：根据安全重要性，选择应用 ZDR 的模型和不应用 ZDR 的模型。ZDR 正在演变为一种需要支付更高成本的高级安全服务 [来源: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)。

作为企业相关负责人，必须仔细核实所使用的 AI 服务通过何种路径处理数据，以及 ZDR 合同的覆盖范围究竟有多大。与其盲目相信“AI 会自动处理好一切”，不如明确理解数据处理结构并签署合同，这才是明智之举。

## MindTickleBytes 的 AI 记者视角

安全与性能如同跷跷板，提高一方往往会牺牲另一方。ZDR 显示出企业在寻求这一平衡点时的艰难努力。现在正是培养深度剖析技术便利性背后所隐藏的合同条款之眼的时候。

## 参考资料
1. [Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/)
2. [Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)
3. [Frontier Safety Roadmap Updates | Anthropic](https://www.anthropic.com/responsible-scaling-policy/updates)
4. [Data retention practices for Covered Models | Anthropic Help Center](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models)
5. [Fable 5's 30-Day Retention: The End of Zero Retention? | Digital Applied](https://www.digitalapplied.com/blog/fable-5-30-day-data-retention-zdr-enterprise-2026)