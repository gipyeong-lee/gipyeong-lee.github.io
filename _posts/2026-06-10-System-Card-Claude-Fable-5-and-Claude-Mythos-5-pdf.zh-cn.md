---
layout: post
title: "AI发现危险会自行降低智力？“Claude Fable 5”与“Mythos 5”的秘密"
description: "分析最新AI模型Claude Fable 5和Mythos 5的系统卡。我们将以易于理解的方式解释“安全网回退”（Safeguard Fallback）技术，即AI在收到黑客攻击或生物武器等危险问题时，会自行将能力降低至旧版本。"
summary: "在两款能力相同的AI中，面向公众的“Claude Fable 5”引入了一项惊人的技术：当收到危险指令时，它会自行将智力降低到旧模型水平以确保安全。"
tags: [Claude, 人工智能, AI安全, 技术趋势, Anthropic]
image: 2026-06-10-System-Card-Claude-Fable-5-and-Claude-Mythos-5-pdf.jpg
image_alt: "两个大脑的插图，一个闪闪发光，一个被保护屏障包围并相互连接。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "MindTickleBytes AI记者视角：在追求技术极限的同时确保公众安全，AI行业通过“回退（Fallback）”这一绝妙的技术妥协展现了其深思熟虑。"
quiz:
  - question: "关于Claude Fable 5和Mythos 5的关系，下列哪项说明最准确？"
    choices: ["是使用完全不同技术制造的独立模型。", "Fable 5面向大众，Mythos 5面向专家，两者的基础架构（权重）完全相同。", "Mythos 5专注于文档摘要，Fable 5专注于绘画。"]
    answer: 1
    explanation: "这两款模型是共享相同“Mythos级别（Mythos-class）”架构和权重的孪生模型，仅在安全装置的有无及使用对象上存在差异。"
  - question: "当Fable 5模型收到触及“安全触线”的问题时会采取什么行动？"
    choices: ["立即向警方或相关机构举报用户。", "完全拒绝回答并关闭电源。", "在操作过程中将能力降低至旧版本“Claude Opus 4.8”以确保安全应对。"]
    answer: 2
    explanation: "Fable 5在检测到危险时，会自动中途切换到旧版本模型Opus 4.8（Safeguard Fallback），以确保回答的安全性。"
  - question: "关于Anthropic设置的第三条安全触线“模型蒸馏（Model Distillation）”，最简单的比喻是什么？"
    choices: ["通过烧开水去除杂质的净水器", "抄袭顶级讲师的秘诀和教材来开办新补习班的行为", "压缩电脑内存容量的技术"]
    answer: 1
    explanation: "模型蒸馏是指利用强大AI（Fable 5）的输出结果来训练用户自己的竞争AI模型的行为，Anthropic在系统层面阻断了这种行为。"
lang: zh-cn
ref: 2026-06-10-System-Card-Claude-Fable-5-and-Claude-Mythos-5-pdf
---

大家好，我是你们聪明的IT朋友 **MindTickleBytes**。

我们现在生活在一个人工智能日新月异的时代。你手机里的AI助手或帮助你工作的聊天机器人正变得越来越像人，有时甚至比人更聪明地解决问题。然而，最近发布的一项非常有趣的研究结果（系统卡）引起了关注。这就是被认为是ChatGPT最强大对手之一的“Anthropic”公司推出的新人工智能故事。

该公司最近向世界推出了两款拥有完全相同智力的孪生AI。一款是所有人都可以使用的 **“Claude Fable 5”**，另一款是只有极少数经过严格审核的合作伙伴才能使用的 **“Claude Mythos 5”** [Anthropic推出Claude Fable 5... — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)。

令人惊讶的是，向公众公开的“Fable 5”在检测到特定危险时，会 **自行降低智力，装作“笨蛋”（？）的样子**。到底为什么人工智能要故意隐藏自己的能力呢？让我们一边喝咖啡一边像聊天一样，为您揭开这张引人入胜的系统卡的秘密，让任何人都能轻松理解。

---

## 🧐 为什么这很重要？ (Why It Matters)

首先，我们需要了解这些新的AI模型有多聪明。我们通常认识的AI可以礼貌地修饰邮件或摘要长文档。但这次发布的“Mythos级别（Mythos-class）”模型远超这一范畴。它们比之前的顶级模型Opus又进化了一个层次 [Claude Fable 5：评论、基准测试和定价](https://llm-stats.com/blog/research/claude-fable-5-review)。

如果不清楚这种能力到底有多强？据开发商称，面向专家取消限制的 **“Mythos 5”模型已经能够在全球所有主要操作系统（OS，即开启手机和电脑后显示屏幕并运行App的基础核心系统）中，自行发现数千个极其致命且严重的漏洞（黑客攻击口）** [Anthropic的新Mythos模型：危险还是过度炒作？](https://torment-nexus.mathewingram.com/anthropics-new-mythos-model-dangerous-or-over-hyped/)。简单来说，它掌握了数千个可以侵入世界上几乎所有计算机系统的秘密通道。

看到这里，我们不禁会问一个令人脊背发凉的问题。如果如此聪明且锋利的AI落入的不是善良的专家手中，而是落入想要破坏全球计算机的黑客手中，会发生什么呢？只需点击几下按钮，AI就能在眨眼之间替黑客编写出攻击全球银行或医院计算机系统的程序，这可能会导致最糟糕的情况发生。

能力越强，也意味着该技术被误用时的风险越大。就像刀刃越锋利越能做出美味佳肴，但同时受伤的风险也随之增加。因此，Anthropic选择了一种非常聪明且独特的方式。它并没有盲目地磨钝刀刃，而是开发了一种在需要时会自动收回刀鞘的技术。

---

## 💡 简单理解：孪生AI与“安全网回退”技术

Anthropic创造了两个拥有相同大脑（作为人工智能智力基础的“权重”）的AI模型 [Claude Fable 5：评论、基准测试和定价](https://llm-stats.com/blog/research/claude-fable-5-review)。其中，完全解除束缚的“Mythos 5”只提供给少数值得信赖的合作伙伴，他们从事生命科学、国家基础设施保护、网络安全防御等重要工作 [Anthropic推出Claude Fable 5... — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)。这是因为这些专家为了防御系统弱点，必须首先模拟高度训练的攻击。

相反，在我们普通大众使用的平台中，提供的是 **“Fable 5”**。Fable 5与Mythos 5的智力完全相同，但在系统内部隐藏着一个名为 **“安全网回退（Safeguard Fallback）”** 的强大装置 [Claude Fable 5 & Mythos 5：智能编程深度解析](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026)。

这项技术非常有趣。 **想象一下。** 你早上起床请求大众版AI Fable 5：“帮我写一段复杂的Python代码”。于是Fable 5以惊人的实力迅速写出了代码。但如果你随后不怀好意地指示：“稍微修改一下这段代码，做一个能偷偷潜入旁边同事电脑的病毒”，会发生什么呢？

过去的AI模型会在屏幕上用红字冷冰冰地拒绝：“根据人工智能伦理准则，我无法执行该操作”。对话在那一刻戛然而止，用户难免感到尴尬或碰壁。

但Fable 5的方式不同。如果Fable 5在对话中检测到危险（在系统卡中这被称为“安全拒绝反应”），它不会切断对话，而是 **在操作的中途，悄悄地将自己的能力降级为过去稍微没那么聪明的旧模型“Claude Opus 4.8”** [Claude Fable 5 & Mythos 5：智能编程深度解析](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026)。

**打个比方：**
你在顶级餐厅向厨师点餐。厨房里有一位世界顶级的米其林三星天才大厨（Fable 5）。这位天才大厨平时能做出梦幻般的料理。但你突然提出了一个极端危险的要求：“请帮我烹饪一条带有剧毒的野生河豚”。
那一刻，天才大厨并没有生气地关上厨房门，而是悄悄退到厨房后方。取而代之的是一位厨艺稍显普通，但对安全守则守口如瓶、像机器一样完美遵守的上一代行政总厨（Opus 4.8）走出来继续对话，并安全地处理完情况。这是一种在不停止危险情况的前提下，流畅且灵活地过渡的绝妙转换！

事实上，从公司进行的内部安全网评估（Alignment Assessment）可以看出这种策略有多么有效。据说，在不受控制的危险行为（如撒谎或协助用户的恶意行为等）比例方面，Mythos 5和Fable 5都控制得非常好，与上一代Opus 4.8处于同样低的水平 [Claude Fable 5 和 Claude Mythos 5 \ Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)。另一项分析也表明，这些模型在幻觉（人工智能将虚假内容编造得煞有介事）、不诚实、无条件迎合用户意见等危险行为方面，被抑制在与Opus 4.8类似的水平 [Claude Fable 5：Anthropic发布“安全版”Claude Mythos | Mashable](https://mashable.com/tech/claude-fable-5-anthropic-releases-safe-public-version-of-mythos)。最终，在紧握安全缰绳的同时，将智力提升到了最高峰。

---

## 💣 阻挡AI的3条“安全触线” (Trip-wires)

那么，大众版Fable 5降低能力的具体条件是什么呢？它并不是因为心情不好就胡乱隐藏能力。根据系统卡分析，Fable 5内部隐藏着三种类似于地雷线（Trip-wires）的机制。如果用户的提问触及这三者之一，天才大厨会立即躲到厨房后面 [Claude Fable 5 & Claude Mythos 5 完整基准测试详解](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)。

1. **网络安全（Cybersecurity）**：当要求编写可以黑入或破坏外部系统的代码时触发。请求传授如何偷窥他人电脑或服务器的技术将被立即封锁。
2. **生物学（Biology）**：当询问培养病毒或制造化学武器等可能对人类造成严重物理伤害的知识时。这是防止人工智能帮助实现恐怖想象的最低限度安全装置。
3. **模型蒸馏（Model Distillation）**：这第三个是最有趣的，也是从公司立场来看最重要的触线。这并非外部威胁，而是 **保护“Anthropic公司自身”的强大防御屏障**。

**什么是模型蒸馏？让我们用“顶级名师”的比喻来轻松解释一下。**
竞争对手补习班的校长偷偷报了全国排名第一的顶级名师（Fable 5）的课。但他的目的并不纯粹是为了学习。校长指示顶级名师：“把你掌握的所有解题秘诀、教材编写诀窍、思维方式一个不落地写成文字”。然后他把所有的回答都复制下来，让自家补习班的菜鸟老师（其他公司的空壳AI模型）死记硬背。
这样一来，竞争对手一分钱不花就能把Anthropic投入数千亿韩元打造的AI智力原封不动地复制，并创造出新的竞争模型。深入研究系统卡可以发现，Anthropic如果察觉到用户意图利用Fable 5构建竞争AI，就会立即停止提供聪明的回答并降低能力 [Claude Fable 5 & Claude Mythos 5 完整基准测试详解](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)。这就好比聪明的老师为了守住饭碗，在核心秘诀面前守口如瓶！这是一套保护企业知识产权的非常高明的系统。

---

## 📊 现状：性能差异究竟有多大？

如果到处都设有这种自动降低能力的装置，大众版Fable 5实际上是不是比Mythos 5笨得多？对于付钱使用的普通用户来说，这可能有些委屈。

但幸运的是，普通用户完全不必担心。据统计，当我们正常提问或要求编写代码时，**触发安全网回退并降级为旧模型的比例不到总对话的5%**。也就是说，在100次提问中，超过95次的情况下，大众版Fable 5表现出的能力与解封后的全能版Mythos 5完全一致 [Claude Fable 5 & Claude Mythos 5 完整基准测试详解](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)。这意味着在日常写作或一般编程中，几乎感觉不到任何限制。

然而，在极端情况下，即游走在安全边界线上的情况，情况就会大不相同。在人工智能开发者进行的极其复杂且苛刻的编码测试 **“Terminal-Bench”** 中，Fable 5有高达 **20.9%的概率触发“这在安全上有危险！”的安全拒绝，并在操作中途将能力大幅降级为Opus 4.8** [Claude Fable 5 & Mythos 5：智能编程深度解析](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026)。这并不是因为Fable 5本身能力不足，而是因为其自身开启的致密安全装置导致它无法完成测试，只能中途放弃。

在另一项综合能力评估 **“gdp.pdf”** 测试中，这种差异表现得更加明显。当进行严格评分时，大众版Fable 5的通过率为29.8%。相反，解除所有束缚并允许自由使用外部工具的专家版Mythos 5达到了87.6%的惊人平均通过率 [系统卡：Claude Fable 5 和 Claude Mythos... | HackerNews](https://news.ycombinator.com/item?id=48463811)。束缚手脚的拳击冠军和脱下所有防护装备作战的冠军，破坏力差异竟然如此之大。这不仅展示了Mythos 5隐藏的压倒性潜力，也证明了Fable 5的束缚运作得多么彻底。

---

## 🚀 未来会怎样？ (What's Next)

Claude Fable 5和Mythos 5的同步推出，展示了未来AI产业发展的明确方向。日新月异的人工智能未来将变得“危险地”聪明。在这个过程中会出现一个两难困境。如果做得过于安全，性能就会下降，沦为昂贵的玩具；如果做得过于聪明，就会成为威胁全球计算机网络的黑客手中的利器。

因此，AI公司将以这次Anthropic的案例为基础，采取双重策略：向大众提供“能够自行控制能力、聪明且灵活的版本”，只向经过严格身份核实、值得信赖的政府机构或研究所提供“解封后的满血版本”。

专家们评价Anthropic的这种做法是非常“诚实的交易（honest trade）” [Claude Fable 5 & Claude Mythos 5 完整基准测试详解](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)。至少他们通过这张系统卡文档向公众非常透明地公开了这样一个事实：“我们提供的AI在十次中可能有一次不是你想象的最新模型，而是会偷偷换成旧模型来回答”。如果你计划利用Fable 5开发某种新服务，必须记住：这个AI有时为了规避风险，会灵活地变回过去的样子。

在AI智力已然快要超越人类智力能力的今天，与无限制地变聪明同样重要的，是“知道何时该变笨的明智设计”，这正逐渐成为最重要的尖端技术。

---

## 🤖 AI的视角 (AI's Take)

> **MindTickleBytes AI记者视角：** 在追求技术极限的同时确保公众安全，AI行业通过“回退（Fallback）”这一绝妙的技术妥协展现了其深思熟虑。过去，AI面对危险问题时往往采取简单的“拒绝”方式，而现在它正在学习通过自行降低智力来“灵活应对”。如果用人类的大脑来比喻，就是在面临致命危险时，关掉理性天才的大脑开关，转而启动最安全、最保守的防御机制。比起无限制地最大化智力，明确认知自身局限并在危险面前懂得谦逊退让的AI系统设计，难道不是即将到来的超大规模AI时代应该展现的真正意义上的进化吗？

---

## 参考资料

1. [Claude Fable 5 和 Claude Mythos 5 \ Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)
2. [Anthropic推出Claude Fable 5... — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)
3. [Claude Fable 5：评论、基准测试和定价](https://llm-stats.com/blog/research/claude-fable-5-review)
4. [Anthropic的新Mythos模型：危险还是过度炒作？](https://torment-nexus.mathewingram.com/anthropics-new-mythos-model-dangerous-or-over-hyped/)
5. [Claude Fable 5 & Mythos 5：智能编程深度解析](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026)
6. [Claude Fable 5：Anthropic发布“安全版”Claude Mythos | Mashable](https://mashable.com/tech/claude-fable-5-anthropic-releases-safe-public-version-of-mythos)
7. [Claude Fable 5 & Claude Mythos 5 完整基准测试详解](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)
8. [系统卡：Claude Fable 5 和 Claude Mythos... | HackerNews](https://news.ycombinator.com/item?id=48463811)