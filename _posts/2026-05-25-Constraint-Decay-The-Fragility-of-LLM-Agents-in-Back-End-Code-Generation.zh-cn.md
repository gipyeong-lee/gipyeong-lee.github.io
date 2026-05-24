---
layout: post
title: "为什么把复杂任务交给AI开发者它总是会忘记：“约束衰减”的秘密"
description: "浅显易懂地解释了AI编码代理在编写复杂的后端代码时，忘记指令的“约束衰减（Constraint Decay）”现象。"
summary: "AI编码代理在编写简单代码方面表现出色，但随着结构性规则的增加，它会遗忘指令。因此，目前它仍难以胜任实际服务级的后端开发。"
tags: [AI, 编码代理, 后端开发, 约束衰减, LLM, 技术趋势]
image: 2026-05-25-Constraint-Decay-The-Fragility-of-LLM-Agents-in-Back-End-Code-Generation.jpg
image_alt: "机器人在错综复杂的建筑设计图上拼接齿轮碎片，显得十分困惑并抓耳挠腮"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI编程工具并非魔法棒，而是性能强劲的电动工具。在完美的AI架构师出现之前，搭建骨架和协调约束条件依然是人类的职责。"
quiz:
  - question: "文章中描述的“约束衰减（Constraint Decay）”现象是指什么？"
    choices: ["随着时间推移，AI编码速度逐渐变慢的现象", "随着需求和结构性规则的增加，AI忘记先前的指令导致性能下降的现象", "AI忘记很久以前学习过的过去编程语言的现象"]
    answer: 1
    explanation: "指随着结构性需求的不断积累，AI性能大幅下降并忘记指令的现象。"
  - question: "根据论文结论，目前AI编码代理最适合应用于哪个阶段？"
    choices: ["实际服务用的商用后端开发", "复杂的对象关系映射及数据库设计", "快速测试想法的原型制作（Rapid prototyping）"]
    answer: 2
    explanation: "目前的AI在快速原型制作方面值得信赖，但要完全将商用级别的复杂后端开发交给它还很勉强。"
  - question: "当AI试图生成大而复杂的文档时，在屏幕上没有任何错误或警告提示的情况下，悄悄输出空白响应的现象被称为什么？"
    choices: ["输出停滞（Output Stalling）", "幻觉（Hallucination）", "知识冲突（Knowledge Conflict）"]
    answer: 0
    explanation: "AI代理在试图生成体积大且格式复杂的文档时，陷入空白状态的错误被称为“输出停滞（Output stalling）”。"
lang: zh-cn
ref: 2026-05-25-Constraint-Decay-The-Fragility-of-LLM-Agents-in-Back-End-Code-Generation
---

想象一下。你今天早晨来到公司，对新引入的超级智能AI新员工下达指令：“给我们的公司网站建一个员工可以使用的简单建议反馈留言板吧。”这位聪明的AI新员工仅仅用了10分钟，就迅速写出了完美运行的代码并展示在屏幕上。对其惊人速度感到赞叹的你，顺势决定将真正的工作交接给它：“真是太棒了！那么这次请完全符合我们公司的主数据库规则，应用最新的安全模式，并与现有的登录系统完美连接，再重新做一遍。”

然而令人惊讶的事情发生了。刚才还像天才开发者一样的AI，突然开始写出破坏公司现有系统的荒谬代码，或者完全忘记了刚才所说的核心安全规则，开始不知所措。甚至完全拿不出任何成果，画面直接卡死。

这种令人沮丧的情况并非单纯的错误或暂时的Bug。最近，人工智能研究人员在后端开发（用户看不见的服务器和数据库领域的开发）环境中观察类似ChatGPT这样的AI编码代理（能够自行制定计划并编写代码的AI程序）时，发现了一个致命弱点，那就是“约束衰减（Constraint Decay）”现象。在世人期待AI很快就能100%取代人类开发者的背景下，这一现象为AI目前真正的局限性在哪里提供了明确的线索。

## 这为什么很重要？ (Why It Matters)

最近看科技新闻，每天都能听到AI正在彻底改变软件开发格局的消息。许多人经常感到不安：“现在再过一两年，人类开发者是不是就不再被需要了？”实际上，在改变网站按钮颜色或制作简单的页面方面，AI确实比人类更快、更准确。

但是，我们要开发日常中可以放心使用的实际商用服务（Production）级别的软件，并不仅仅是在白纸上敲击出看似合理的代码那么简单。简而言之，这就像是建造一个只有外表华丽的模型房屋，与建造一栋人们实际居住、使用水电的坚固真公寓之间的区别。

真正的软件必须安全地隔离并保存数百万用户的数据，必须在不发生冲突的情况下与旧有的银行系统通信，并且必须严格遵守既定的框架，以便其他同事以后能够轻松修改代码。总而言之，它必须像保护生命一样遵守复杂而严苛的规则和骨架。为了使当前的AI成为能够完全胜任复杂工作的真正“同事开发者”，它必须具备在这种严苛环境中不迷失方向的能力。我们之所以不能将公司的核心业务系统完全交给AI，真正的原因就隐藏于此。

## 浅显易懂的解释 (The Explainer)

科学家们集中研究了为什么当规则变多时AI会做出荒谬的行为，并将这种现象命名为“约束衰减（Constraint Decay）”。[[2605.06445] Constraint Decay: The Fragility of LLM Agents in Backend Code Generation](https://arxiv.org/abs/2605.06445)

这种现象为什么会发生？让我们稍微通俗地看看AI模型的内部情况吧。AI的神经网络层（Neural network layers，像人类大脑神经细胞一样连接的AI信息处理结构）就像智能手机照片修图软件的滤镜一样。就像原图依次经过亮度滤镜、色彩滤镜、降噪滤镜，变成一张精美照片一样，你“建个留言板”的简单输入，也会经过数百层的处理转化为编程代码。在这个过程中，AI将代码拆解成被称为“Token（人工智能读写的最基本数据单位）”的微小拼图碎片来理解。其原理是在几十万个拼图碎片中，通过概率计算出接下来最自然的一块并不断拼接上去。

那么，在这里不断添加“约束条件”意味着什么呢？这已经超越了单纯完成一幅漂亮画作的范畴，就像是叠加了几十个严苛的指令，比如“红色拼图不能放在蓝色拼图旁边，边缘拼图的背面必须印有公司徽标，每隔10行画一条黑边”。当指令接连不断地积累时，AI的信息处理能力就会超载，最终会逐渐忘记前面提到的那些重要规则。

打个比方，想象一下为了教刚在训练营完成基础训练的聪明小狗新把戏，对其进行微调（Fine-tuning，为了特定目的对AI进行额外训练的过程）的情况。对于完成基础训练的小狗，只要下达“坐下！”一个指令，它就能乖乖听从。在只执行单一任务的宽松条件（Loose specifications）下，它能发挥卓越的能力。但是，如果同时下达多个条件：“坐下后举起右前脚，摇三次尾巴，然后只有我拍手两次时才叫一声”，会发生什么呢？即使是再聪明的天才小狗也会陷入混乱转圈圈，最终连第一个指令“坐下”也忘得一干二净，直接躺在地板上。

AI编码代理的大脑也是一样的。在几乎没有规则需要遵守的自由环境中，它能极其出色地编写出代码。但是，一旦投入到需要严格处理表面看不见的服务器和数据库的后端开发中，情况就会急剧改变。决定将哪些数据存储在何处、如何存储的数据规则，作为整个系统骨架的架构模式（Architecture pattern，构成软件骨架的标准设计方式），以及对象关系映射（ORM，连接编程语言和数据库结构的翻译技术）等繁重的“结构性约束条件”，会像标签一样在整个工作过程中如影随形。当这样严苛的需求积累起来时，AI的编码性能就像跌下悬崖一样直线下降，并无视最初的指令。[[2605.06445v1] Constraint Decay: The Fragility of LLM Agents ...](https://arxiv.org/abs/2605.06445v1)

特别值得一提的是，研究团队像做手术一样仔细解剖了AI失败的原因。结果发现，根本错误的种子主要源于“数据层（Data-layer）”的缺陷，这是一个负责物理存储和调用数据的极深且极其重要的领域。[Constraint Decay: The Fragility of LLM Agents in Backend Code ...](https://arxiv.deeppaper.ai/papers/2605.06445v1) 在需要分步骤连续思考的复杂任务中，前一步的小失误会像滚雪球一样在下一步演变成致命错误，最终导致整个规则崩溃。计算机专家将这种现象称为“推理衰减（Reasoning decay，逻辑思考流逐渐崩塌的现象）”。[Why LLM Agents Fail: Four Mechanisms of Cognitive Decay and the Reasoning Harness Layer - DEV Community](https://dev.to/frank_brsrk/why-llm-agents-fail-four-mechanisms-of-cognitive-decay-and-the-reasoning-harness-layer-3148)

## 目前情况 (Where We Stand)

这项有趣且重要的研究是受欧盟（EU）支持的“AI4SWeng”项目的一部分，由弗朗西斯科·登特（Francesco Dente）和达里奥·萨特里亚尼（Dario Satriani）两位专家主导进行。[Can LLM coding agents follow strict architectural rules? In ...](https://www.linkedin.com/posts/papotti_can-llm-coding-agents-follow-strict-architectural-activity-7459949167545819136-Ziig)

为了客观证明“AI能够在多长时间内很好地记住并遵守各种严苛的结构性约束条件？”，他们搭建了一个巨大的测试舞台。构建了多达8种不同的Web框架（Web framework，用于快速安全地创建网站的标准建筑工具集）环境。然后，他们让AI执行了80个从零开始编写代码的全新生成任务（Greenfield generation）以及20个在现有代码上添加新功能的附加任务。[Constraint decay: The fragility of LLM agents in backend code ...](https://www.eurecom.fr/en/publication/8745) 打个人类能理解的比方，就是扔给它统一的建筑法规，让它在8个不同的环境中建造100栋房子，然后用放大镜仔细检查它到底多大程度上遵守了规定。

实验结论非常冷酷且明确。根据论文所述，这个结果也向普通用户传达了明确的信息。目前的AI编码代理“虽然是一个非常可靠的魔法工具，能够快速将脑海中的想法呈现到屏幕上进行测试原型制作（Rapid prototyping），但是要将其完全投入到视规则和骨架为生命的商用服务级后端开发（Production-grade backend development）中，它仍处于无法完全信任的状态”。[Constraint decay: The Fragility of LLM Agents in Backend Code Generation](https://arxiv.org/html/2605.06445)

在这里，我们很容易陷入一个盲点。目前市面上存在的许多“AI编码性能评估测试”，只要AI生成的代码在功能上“能运行”，就被视为正确答案。尽管这些测试忽视了公司实际商用软件中必不可少的复杂架构模式或严格的安全规则等看不见的非功能性元素，但人们看到“AI在编码考试中得了满分”，就会产生AI已经完全取代了开发者的错觉。[Constraint Decay: The Fragility of LLM Agents in Backend Code ...](https://www.catalyzex.com/paper/constraint-decay-the-fragility-of-llm-agents)

甚至还存在更为怪异和严重的错误形式。不堪约束条件重负的AI不仅会吐出荒谬的代码，甚至会出现直接闭嘴的症状。研究团队发现，当指示AI代理编写格式庞大且复杂的文档时，屏幕上没有任何错误警告，它只是静悄悄地输出空白响应并停止运行，这种现象被称为“输出停滞（Output stalling，因过载无法给出结果而停止的错误）”。[When Agents Go Quiet: Output Generation Capacity and Format-Cost Separation for LLM Document Synthesis](https://arxiv.org/html/2604.16736) 这就像是一个人被老板扔下复杂的指令炸弹后，大脑一片空白，索性放弃回答一样。

## 未来会怎样？ (What's Next)

那么，AI注定永远无法进行规则错综复杂的后端软件开发吗？现在放弃所有期望还为时过早。研究系统结构的专家们的分析指向了一个截然不同的、积极的解决方案。

一位敏锐的分析师指出，这种频繁失败的现象并非AI本身的“智力不足”。真正的问题在于让AI工作的“架构（系统运作结构）”设计不良。他强调：“失败并不是从AI的大脑中开始的。真正的原因在于我们最初喂给AI什么信息，以及AI输出的结果随后经历了怎样的过滤过程。”[The LLM Reliability Paradox: Agents Aren’t Broken, Your Architecture Is](https://plainenglish.io/artificial-intelligence/the-llm-reliability-paradox-agents-aren-t-broken-your-architecture-is) 换言之，这不是AI自身的故障，而是我们驱使AI的“工作方式”存在问题。

因此，未来的AI编码工具将摆脱单纯增加大脑容量这种简单粗暴的方式。就像一丝不苟的人类开发者每写一行代码就会随时运行测试、检查是否符合规则一样，AI内部也必将配备一个“独立的验证层（Validation layer，负责确认代码质量和规则遵守情况的监督员角色的系统）”，用于在旁边即时审查AI吐出的代码并捕捉错误。实际上，在当前的开发一线，已经不再盲目信任AI的成果，而是必须通过额外的安全装置和解析器（Parser，读取代码并分析其是否符合语法的工具），这种双重甚至三重的安全网机制正在成为主流。[Why Does the LLM Stop Computing: An Empirical Study of User-Reported Failures in Open-Source LLMs](https://arxiv.org/html/2601.13655v1)

## AI记者的视角 (AI's Take)

我们日常接触到的AI编码工具并非魔杖，而是一套性能强劲的高端“电钻套装”。在快速组装一张宜家桌子时，它能表现出压倒苦苦挣扎的人类的极高效率；但如果把复杂大型医院的建筑图纸塞给它，让它建造一栋摩天大楼，它就会连顺序都搞不清楚，在错误的柱子上打洞，从而引发灾难。

尽管如今，遗忘约束条件的“约束衰减”现象看起来像是AI的阿喀琉斯之踵，但这只不过是技术走向成熟的过程中必然经历的成长的阵痛。在不久的将来，AI将进化成为一个不仅能自己编写代码，同时还能严格审查自己代码的成熟伙伴。

但是，在能够自主完美控制错误的真正AI架构师出现之前，负责搭建项目大框架、不断协调众多约束条件并引导至正确方向的“洞察力”，依然会是我们人类开发者最可靠且闪耀的武器。无论技术发展得多么耀眼，负责指挥巨大齿轮精准咬合运转的，终究还得是人。

## 参考资料

1. [[2605.06445] Constraint Decay: The Fragility of LLM Agents in Backend Code Generation](https://arxiv.org/abs/2605.06445)
2. [Constraint decay: The Fragility of LLM Agents in Backend Code Generation](https://arxiv.org/html/2605.06445)
3. [[2605.06445v1] Constraint Decay: The Fragility of LLM Agents ...](https://arxiv.org/abs/2605.06445v1)
4. [Constraint Decay: The Fragility of LLM Agents in Backend Code ... (DeepPaper)](https://arxiv.deeppaper.ai/papers/2605.06445v1)
5. [Why LLM Agents Fail: Four Mechanisms of Cognitive Decay and the Reasoning Harness Layer - DEV Community](https://dev.to/frank_brsrk/why-llm-agents-fail-four-mechanisms-of-cognitive-decay-and-the-reasoning-harness-layer-3148)
6. [Can LLM coding agents follow strict architectural rules? In ...](https://www.linkedin.com/posts/papotti_can-llm-coding-agents-follow-strict-architectural-activity-7459949167545819136-Ziig)
7. [Constraint decay: The fragility of LLM agents in backend code ... (Eurecom)](https://www.eurecom.fr/en/publication/8745)
8. [Constraint Decay: The Fragility of LLM Agents in Backend Code ... (CatalyzeX)](https://www.catalyzex.com/paper/constraint-decay-the-fragility-of-llm-agents)
9. [When Agents Go Quiet: Output Generation Capacity and Format-Cost Separation for LLM Document Synthesis](https://arxiv.org/html/2604.16736)
10. [The LLM Reliability Paradox: Agents Aren’t Broken, Your Architecture Is](https://plainenglish.io/artificial-intelligence/the-llm-reliability-paradox-agents-aren-t-broken-your-architecture-is)
11. [Why Does the LLM Stop Computing: An Empirical Study of User-Reported Failures in Open-Source LLMs](https://arxiv.org/html/2601.13655v1)