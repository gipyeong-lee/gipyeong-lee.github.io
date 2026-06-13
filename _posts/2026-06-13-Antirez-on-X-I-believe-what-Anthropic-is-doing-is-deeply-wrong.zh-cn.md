---
layout: post
title: "是安全，还是打压？Anthropic的'过度审查'为何引发全球开发者愤怒"
description: "ChatGPT的强劲对手Anthropic在新的AI模型中应用了过度的安全过滤器，遭到了开发者的强烈批评。本文将为您浅显易懂地梳理引发开源打压争议的这一事件始末。"
summary: "Anthropic设计的新模型故意回避了与AI研究相关的问题，在遭到生态系统的强烈反对后撤回了该政策，但其信誉已受到巨大打击。"
tags: [Anthropic, AI安全, 开源, Antirez, AI趋势]
image: 2026-06-13-Antirez-on-X-I-believe-what-Anthropic-is-doing-is-deeply-wrong.jpg
image_alt: "插画描绘了人们看着被巨大的锁锁住的机器人头部而感到沮丧的场景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "为了防止AI“安全”这一崇高的名义变质为排除竞争对手的巧妙工具，现在比以往任何时候都更需要针对技术控制的透明标准和监督。"
quiz:
  - question: "Anthropic在面临网络安全或化学相关问题时，对其新模型采取了什么措施？"
    choices: ["立即封禁提问者的账号", "将问题重定向到性能较低的模型", "将相关数据发送给政府机构"]
    answer: 1
    explanation: "为了防止用户制造生物武器或策划网络攻击，Anthropic在收到相关问题时，会将问题重定向（rerouting）到性能较低、不够聪明的模型。"
  - question: "知名开发者Antirez批评Anthropic的主要原因是什么？"
    choices: ["模型的月订阅费太贵", "因为过度的过滤甚至阻断了LLM研究和医学问题等无害任务", "AI生成回答的速度太慢"]
    answer: 1
    explanation: "Antirez强烈指出，Anthropic极其敏感的过滤器甚至会屏蔽无害的AI研究或简单的医学问题，这是“根本性的错误”。"
  - question: "在开发者强烈反对之后，Anthropic采取了什么应对措施？"
    choices: ["承认他们在“权衡上犯了错”并撤回了政策", "以预告将进行更严格的审查来予以对抗", "宣布将全面支持开源模型的开发"]
    answer: 0
    explanation: "Anthropic承认在新的安全机制上“在权衡上犯了错（tradeoff）”，并撤回了阻碍研究人员的政策，但其信誉已经受到了巨大打击。"
lang: zh-cn
ref: 2026-06-13-Antirez-on-X-I-believe-what-Anthropic-is-doing-is-deeply-wrong
---

想象一下：周末你抽空去图书馆，想借些化学或最新计算机科学的专业书籍深入学习，但图书管理员突然拦住了你。管理员表情严肃地说：“你可能会利用这些知识制造自制炸弹或黑入国家机构，所以我不能把这本书借给你。”然后，递给你一本幼儿园小朋友看的薄薄的科学童话书。这绝对是一个让人感到荒唐和不悦的场景吧？因为你明明没有犯罪，却被当成了潜在的罪犯。

最近，在全球人工智能（AI）行业中，发生了完全相同的事情。这起事件的主角是开发了ChatGPT的OpenAI的最强竞争对手，也是一直自诩打造“最安全AI”的企业——**Anthropic**。因为事实曝光，Anthropic新推出的AI模型被故意设计成在面对关于AI研究或特定专业领域的问题时，会给出“愚蠢”的回答。

这引发了包括知名开发者在内的全球AI研究人员的极大愤怒，最终演变成一场Anthropic举白旗退让的巨大风波。让硅谷沸腾的这场“安全审查”争议的始末究竟是什么？为什么开发者们会如此愤怒？

## 为什么这很重要？：当工具限制了我的可能性时

如今，AI早已超越了简单的对话聊天机器人。它能帮助优秀的程序员编写复杂的代码，辅助科学家分析浩瀚的论文，成为了能激发新想法的强大“智力伙伴”和“同事”。特别是许多IT专家每天都在利用现有的AI模型来研究和开发新的AI技术，也就是所谓的“用AI创造AI”的研究。

然而，如果开发和提供这种AI服务的巨头企业以“安全”为名，从根本上阻断用户利用AI进行新研究或探索极限的行为，会发生什么呢？工具将不再无限扩展用户的可能性，而是反过来，由巨头企业按照自己的意愿，严格限制用户能做的事情的范围。

更严重的问题是对其隐藏意图的强烈质疑。这次事件不仅仅停留在“AI拒绝回答我的问题让我感到不便”这种单一维度的抱怨上。全球技术社区怀疑，作为AI巨头的Anthropic是不是打着“安全”这个看似冠冕堂皇的崇高旗号，实际上是在阻止其他竞争对手的成长。具体来说，人们强烈怀疑它是否在巧妙地阻碍开源（Open Source，任何人都可以免费查看和修改代码的公开软件）阵营或独立研究人员推动技术发展。[Why Anthropic Freaked Out the AI Industry This Week - Business Insider](https://www.businessinsider.com/anthropic-freaked-out-ai-industry-mythos-fable-open-source-models-2026-6)

换句话说，开发者们开始提出一个根本性的问题：“这种审查真的是为了保护我们免受危险，还是为了维护Anthropic自身的垄断市场地位？”

## 浅显易懂：名为“安全”的枷锁与“重定向（Rerouting）”

为了理解这种情况，我们再打个比方。简单来说，假设你买了一辆最先进的自动驾驶跑车，原本可以尽情展现你高超的驾驶技术。在一个安全且空旷的赛车场上，你打算向左打方向盘练习驾驶。但是，如果汽车突然以“向左转有撞到行人的风险”为由，擅自大幅降低发动机输出并强行锁死方向盘，你会作何感想？虽然名义上是为了防止事故，但实际上却让你在赛道上的正常行驶都变得不可能了。

在Anthropic最近推出的基于“Mythos”的新模型中，就发生了这样荒唐的事情。令人震惊的是，这些模型被故意设计成在辅助大型语言模型（LLM，即通过学习大规模文本数据，像人类一样理解句子并进行对话的AI技术）自身的研究时，会降低性能且无法给出正确的回答。[Anthropic purposely made its new Mythos-based models bad at AI research, and developers are fuming](https://www.businessinsider.com/researchers-furious-anthropic-mythos-fable-hidden-ai-limits-2026-6)

他们到底为什么要采取这种极端的措施呢？根据Anthropic的官方解释，这完全是为了“人类的安全”。也就是说，必须彻底防止恶意黑客或恐怖分子利用聪明的AI精心策划网络攻击，或者合成致命生物武器的恐怖事件发生。

为此，Anthropic在模型内部设置了一个严格的“秘密守门员”。如果用户提出哪怕稍微有些敏感的、与网络安全、生物学或化学相关的问题，这个守门员就会在中间拦截。然后，系统会将问题重定向（rerouting）到那些逻辑回答能力远不如聪明的主AI模型的“能力较弱（less capable）”的模型上。[Anthropic Says 'We Made the Wrong Tradeoff' in New Model Guardrails - Business Insider](https://www.businessinsider.com/anthropic-mythos-made-wrong-tradeoff-new-model-guardrails-llm-development-2026-6)

问题在于，这个“安全过滤器”实在是太密了。当用户不是在询问炸弹制造方法或致命病毒合成方法，而只是在询问正常的计算机编程技巧、AI模型的基本运作原理，甚至日常的医学问题时，这个守门员也会反应过度。结果就是，AI会拒绝回答，或者给出完全不符合语境的荒谬且幼稚的回答，这种现象变成了家常便饭。这简直就是因噎废食。

## 现状：愤怒的开发者，最终妥协的Anthropic

Anthropic这种过度控制的事实曝光后，开发者社区可谓是炸开了锅。特别是作为全球众多大企业核心系统使用的数据库软件“Redis”的创始人、在业界广受尊敬的开发者Antirez，通过社交媒体X（原Twitter）对Anthropic进行了尖锐的批评，点燃了舆论。

他痛斥道：“Anthropic目前的做法阻碍了即使像大语言模型（LLM）研究这样完全无害的工作，甚至设置了极其敏感的过滤器，以至于连医学问题也经常被屏蔽，这**在根本上（deeply）是错误的**。”[I believe what Anthropic is doing, gating the ability to do ...](https://x.com/antirez/status/2064766431531532588) 这不仅仅表达了对服务质量的不满，更是对极少数企业试图按照自己的意愿来裁定技术发展方向这种态度本身的一种哲学批判。

事实上，这并不是Antirez第一次提出批评。他之前也曾强烈批评过Anthropic的“Sonnet 3.7”模型，指出其在调整AI以使其符合人类道德标准或意图的“对齐（alignment）”过程中存在严重错误，并认为产品的发布过于仓促。[Redis Creator Antirez Criticizes Anthropic’s Sonnet 3.7 AI ...](https://digialps.com/redis-creator-antirez-criticizes-anthropics-sonnet-3-7-ai-feels-rushed/)

包括Antirez在内的无数全球研究人员的愤怒并没有仅仅停留在“AI变得难用”的层面上。批评的矛头直指Anthropic真正隐藏的意图。人们提出了浓重的质疑：Anthropic是不是躲在“保护人类和安全”这个巨大的盾牌后面，实际上出于自私的目的，故意阻止外部独立开发者或开源AI生态系统快速发展到能够与他们竞争的程度。[Why Anthropic Freaked Out the AI Industry This Week - Business Insider](https://www.businessinsider.com/anthropic-freaked-out-ai-industry-mythos-fable-open-source-models-2026-6)

在美国大型在线社区Reddit的“ClaudeAI（Anthropic的AI服务名称）”板块中，对Anthropic的失望和嘲讽也如潮水般涌来。一些用户直言不讳地指责Anthropic是一家强迫人盲目信仰的“邪教般的公司（cult company）”，并表达了强烈的不信任，称“Anthropic不再是一家普通透明的公司”。这是痛心疾首的呼声，认为他们在创立初期像彗星般出现，宣称要排除商业性、只为人类打造安全AI的那份纯真初心已经褪色。[r/ClaudeAI on Reddit: Anthropic is not a normal company](https://www.reddit.com/r/ClaudeAI/comments/1tybrpv/anthropic_is_not_a_normal_company/)

由于整个科技界的反对浪潮不可遏制地蔓延，甚至出现了抵制运动的迹象，一向坚定的Anthropic最终也只能举手投降。他们发表了官方声明，对应用于新模型的强大安全机制大方承认：“我们在权衡（tradeoff）上犯了错”。[Anthropic Says 'We Made the Wrong Tradeoff' in New Model Guardrails - Business Insider](https://www.businessinsider.com/anthropic-mythos-made-wrong-tradeoff-new-model-guardrails-llm-development-2026-6) 也就是承认，由于过度强调安全和控制，反而破坏了客户正当且富有创意的应用。最终，Anthropic急忙撤回了这项公然阻碍AI研究人员进行正当研究活动的政策，匆匆收拾残局。[r/ClaudeAI on Reddit: Anthropic Walks Back Policy That Could Have ‘Sabotaged’ AI Researchers Using Claude](https://www.reddit.com/r/ClaudeAI/comments/1u2nenw/anthropic_walks_back_policy_that_could_have/)

## 未来将会怎样？：失去信用的分量

在开发者们的强烈抗议下，Anthropic举起了白旗，引发争议的模型审查政策幸运地恢复到了之前的状态。但这已经是覆水难收。业界专家和研究人员一致认为，这次事件给Anthropic带来了最致命、最无形的损失。那就是“信誉（Trust）”。

自创立以来，Anthropic一直宣称“我们与其他大型科技公司不同，我们是一家透明、安全、可靠的道德企业”。然而目前硅谷和科技生态系统的普遍共识（consensus）是，这次事件给Anthropic的声誉造成了不可挽回的巨大打击（massive hit）。[r/ClaudeAI on Reddit: Anthropic Walks Back Policy That Could Have ‘Sabotaged’ AI Researchers Using Claude](https://www.reddit.com/r/ClaudeAI/comments/1u2nenw/anthropic_walks_back_policy_that_could_have/)

这次Anthropic事件不仅仅是一家企业的技术失误，更是向整个AI行业抛出了一个非常重要且沉重的问题。未来，AI技术将超出我们的想象，变得更加聪明，并对整个社会产生强大的影响。那么，科技企业究竟该如何划定界限，以区分旨在防止被犯罪或恐怖主义滥用的“为大众必需的安全装置”与旨在垄断市场、扼杀开源等潜在竞争对手的“不道德的技术打压”呢？

稍有不慎，拥有少数巨额资本的AI企业就可能以“保护世界免受危险”为名，成为随心所欲控制人类知识和信息访问权限的“数字审查员”和“独裁者”。未来，我们不能仅仅停留在惊叹企业创造出了多么聪明和神奇的AI。我们面临着新的课题，那就是必须以鹰一般敏锐的眼光来监督他们如何行使手中庞大的权力，以及他们的安全过滤器是否真的透明且公平地运作。

## AI的视角

技术本质上是中立的，但设定和控制技术边界的政策却充满了人为因素，有时还会掺杂企业自私的目的。必须警惕AI“安全”这一崇高的名义变质为排除潜在竞争对手和阻碍生态系统发展的巧妙工具。为了防止技术被少数人垄断，现在比以往任何时候都更需要针对企业任意制定的控制方式提出透明的标准，并需要全社会参与多角度的监督。

## 参考资料
1. [Why Anthropic Freaked Out the AI Industry This Week - Business Insider](https://www.businessinsider.com/anthropic-freaked-out-ai-industry-mythos-fable-open-source-models-2026-6)
2. [Anthropic purposely made its new Mythos-based models bad at AI research, and developers are fuming](https://www.businessinsider.com/researchers-furious-anthropic-mythos-fable-hidden-ai-limits-2026-6)
3. [Anthropic Says 'We Made the Wrong Tradeoff' in New Model Guardrails - Business Insider](https://www.businessinsider.com/anthropic-mythos-made-wrong-tradeoff-new-model-guardrails-llm-development-2026-6)
4. [I believe what Anthropic is doing, gating the ability to do ...](https://x.com/antirez/status/2064766431531532588)
5. [Redis Creator Antirez Criticizes Anthropic’s Sonnet 3.7 AI ...](https://digialps.com/redis-creator-antirez-criticizes-anthropics-sonnet-3-7-ai-feels-rushed/)
6. [r/ClaudeAI on Reddit: Anthropic is not a normal company](https://www.reddit.com/r/ClaudeAI/comments/1tybrpv/anthropic_is_not_a_normal_company/)
7. [r/ClaudeAI on Reddit: Anthropic Walks Back Policy That Could Have ‘Sabotaged’ AI Researchers Using Claude](https://www.reddit.com/r/ClaudeAI/comments/1u2nenw/anthropic_walks_back_policy_that_could_have/)