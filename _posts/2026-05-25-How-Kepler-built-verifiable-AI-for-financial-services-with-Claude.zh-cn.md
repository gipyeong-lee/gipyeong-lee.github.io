---
layout: post
title: "如果AI分析涉及数十亿资金的金融文档？“可验证AI”的出现"
description: "通俗易懂地解释Kepler如何利用Anthropic的Claude创建通过金融界严格监管的“可验证AI”。"
summary: "金融研究初创公司Kepler没有单独使用AI模型Claude，而是将其限制在严格的控制系统中，从而构建了一个能够通过金融界严格审计和监管的高可靠性AI系统。"
tags: [AI, 金融科技, Claude, Anthropic, 可验证AI]
image: 2026-05-25-How-Kepler-built-verifiable-AI-for-financial-services-with-Claude.jpg
image_alt: "机器手拿着放大镜在复杂的金融数据和图表上方"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人工智能真正融入人类生活的最后一道关卡不是“智能”，而是“信任”。Kepler的方法展示了一个绝佳的蓝图，说明AI不是无法控制的魔法，而是可以成为可验证的工具。"
quiz:
  - question: "Kepler引入的用于金融服务的AI模型的核心基础是什么？"
    choices: ["自行做出所有决定的自主型AI", "在确定性基础设施上运行的Claude", "旨在逃避审计的语言模型"]
    answer: 1
    explanation: "Kepler利用了Anthropic的Claude，但将其构建在一个被称为“确定性基础设施”的严格控制系统之上，从而确保了可靠性。"
  - question: "Kepler平台与一般聊天机器人AI最大的区别是什么？"
    choices: ["学习了更多的网络幽默。", "严格区分了要解决的问题和要移交给人类的问题。", "自动忽略所有监管机构的检查。"]
    answer: 1
    explanation: "Kepler严格设定了AI自行解决的领域和必须移交给（escalate）人类专家的领域之间的界限。"
  - question: "正文中强调在金融领域使用AI时最重要的因素是什么？"
    choices: ["句子生成的创造力", "流行语的使用频率", "可审计性和法规遵从性"]
    answer: 2
    explanation: "由于金融行业受到中央银行等机构的严格审计，因此能够追踪和验证AI判断过程的“可审计性”是必不可少的。"
lang: zh-cn
ref: 2026-05-25-How-Kepler-built-verifiable-AI-for-financial-services-with-Claude
---

想象一下，您是一家管理着数百亿韩元客户资产的全球投资银行的负责人。每天早上，您的办公桌上都堆放着数十家公司发布的数千份财务报表和厚厚的投资报告。为了分析这些庞大的数据，您引入了号称世界上最聪明的最新AI助手。

清晨，您向AI发出指令：“帮我整理一下A公司去年第四季度的实际负债率。”AI仅用3秒就给出了一份包含清晰表格和图表的报告。您深信这些数字，按下了巨额投资的按钮。

然而几天后，您发现这些数字是AI误解了上下文而编造出的“看似合理的谎言”。公司遭受了天文数字的损失，金融监管部门立即展开调查。面对调查员尖锐的提问：“您为什么会做出如此致命的决定？”您能回答“因为AI是这么分析的”吗？

绝对不可能。这就是为什么全球华尔街和金融界，面对大型语言模型（LLM，通过学习大量文本数据，能够像人类一样理解和生成句子的人工智能技术）的强大能力，依然犹豫不决、不敢轻易打开钱包的核心原因。在哪怕是一个微小的计算错误都会导致致命财务损失的金融行业，把决定权交给判断过程不透明的AI，无异于蒙着眼睛以200公里的时速在高速公路上狂飙，是一场“危险的赌博”。

但最近，出现了一个具有里程碑意义的案例，平息了这座堡垒般的金融界中弥漫的焦虑。这就是专注于为可靠的金融服务构建“可验证AI（Verifiable AI）”平台的研究型初创公司Kepler的故事[[来源标题](https://www.fintechnews.org/new-frontiers-in-ai-and-finance-kepler-built-verifiable-ai-fon-financial-services-with-calude/)]。他们究竟是如何一下子俘获保守且挑剔的金融界的心呢？

### 为什么这很重要？ (Why It Matters)

您可能见过我们日常娱乐使用的聊天机器人AI偶尔会说出一些荒谬的话，比如世宗大王扔了MacBook之类的。这在专业术语中被称为幻觉（Hallucination）。在与朋友的日常对话或轻松的写作中，这只是一个可以一笑而过的小插曲，但在容不下哪怕1分钱误差的金融界，这却是可能决定公司生死存亡的重大事故。

金融服务公司在超出我们想象的严格甚至令人窒息的监管环境中运作。特别是为了满足巴西中央银行（Banco Central）或证券交易委员会（CVM）等强大金融机构的指导方针和规定，公司做出的所有财务判断和决策都必须有明确的依据，并且随时可以被追溯调查[[来源标题](https://radartrend.com.br/topico/20598/how-kepler-built-verifiable-ai-for-financial-services-with-claude)]。

仅仅说“最终计算结果是正确的”是远远不够的。必须像在数学考试中写下解题过程一样，详细证明“基于什么数据，经过了什么计算公式，为什么会得出这样的结果”，这种“可审计性（Auditability）”是重中之重。

在这个需要满足世界上最严格监管和审计要求、如履薄冰的金融环境中，Kepler以Anthropic公司的AI模型“Claude”为核心大脑，成功打造了独创且安全的AI平台[[来源标题](https://www.gogoai.xin/article/kepler-builds-verifiable-ai-for-finance-with-claude)]。他们的成功为“金融界真的能完全信任并使用善变的AI吗？”这一根本问题提供了最现实、最模范的答案，这对信息技术（IT）行业和金融界都具有非常重要的意义。

### 通俗易懂：把越野车开上铁轨

那么，Kepler是如何将这个才华横溢却偶尔犯下荒谬错误的AI，转变为“绝对不说谎、值得信赖的金融专家”的呢？其惊人的秘密不在于专注于进一步提升AI的智能，而是将对待AI的理念来了个180度的大转弯。

Kepler团队通过与开发Claude的Anthropic公司进行深入的案例研究，得出了一个非常重要的结论并予以分享。那就是“在金融领域，绝对不能让AI模型本身单独成为整个系统”[[来源标题](https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude)]。换句话说，他们意识到不能给予不可预测的AI无限的自由。

为了解决这个致命问题，Kepler建立了一个牢固的“确定性基础设施（Deterministic Infrastructure）”，将人工智能严密地包裹起来。简单来说，这个基础设施起着强大的“信任和验证控制层（Layer）”的作用，阻止AI胡思乱想或做出意料之外的行为[[来源标题](https://trendflashy.com/trending-now-how-kepler-built-verifiable-ai-for-financial-services-with-claude/)]。

专家们所说的“确定性基础设施”这个复杂的概念，可以这样比喻：一般的AI技术就像一辆性能卓越的“越野车”，可以漫无目的地在山间田野四处自由奔驰。它虽然快速强大，但只要稍微失去控制，就不知会冲向何方，随时都有坠崖的危险。相比之下，Kepler构建的确定性基础设施，就像是把这辆高性能车的橡胶轮胎直接拆掉，放在了有既定目的地的坚固“钢轨（铁轨）”上。虽然原封不动地使用了AI强大的引擎动力（出色的语言处理和文档分析能力），但通过人类制定的严格、确定的规则，完全限制了车辆的行驶方向和停车位置。

### 通俗易懂：教聪明的兼职生如何说“不知道”

Kepler不仅局限于限制AI的路径，更进了一步。他们没有把一整块任务盲目地扔给AI，比如“分析这100页厚厚的财务报表并得出结论”，而是将工作切分得很细，只依次指示“精确定位的任务（Precisely defined tasks）”。

此外，他们提前给AI配备了系统化的金融领域复杂专业知识和术语词典，最大限度地减少了AI需要自行判断的不确定性领域。这里最令人印象深刻且最核心的部分是，设定了严格的界限（Hard boundaries），明确区分哪些是AI自行判断“要解决的问题（Resolve）”，哪些是超出自身能力判断后必须“移交给（Escalate）”人类专家的问题[[来源标题](https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude)]。

让我们用日常生活中的场景来解释这一点。假设您在银行贷款窗口雇佣了一位心算能力无与伦比的天才兼职生（AI）。这位员工是个计算天才，但并不太了解错综复杂的金融法的微妙之处，或是客户隐藏的意图。这时，没有任何老板会将银行所有的贷款审批权全盘委托给这位新员工。

相反，老板会给他一本严格的行动指南：“你只负责确实验证客户的基本身份信息并完成文件的简单数字计算（解决），如果发现任何可疑的伪造文件，或者有超过100万韩元的大额贷款审批，你不要自己做决定，必须无条件把审批文件交给我（移交给人类）。”Kepler对待Claude的方式正是如此。即使再聪明，也不让他一个人决定一切。矛盾的是，让AI能够明确划清界限说“从这里开始我不太清楚了，人类专家，请帮帮忙”，正是金融界能够100%信任AI的最大秘诀。

### 现状：执着地解读复杂的脚注（Footnotes）

有了这样坚固的“缰绳”和明确的指导方针，Claude在Kepler的控制系统内展现出了惊人的能力。在如今竞争激烈的金融行业一线，实际需求的绝不只是简单的新闻摘要或问候语的撰写。

关于Kepler平台究竟是为了什么实际目的而构建的，倾听在相关行业最前线工作的专家们的声音，能够最准确地了解当前的现状。最近，业内的一位专家强调说：“目前金融界所有关于AI的讨论都聚焦于‘能力（Capability）’。模型能否妥善处理复杂的多步分析（Multi-step analysis）？能否仔细阅读写在文档角落里的脚注（Footnotes，写在正文下方的小字补充说明）？这就是我们创建Kepler的原因。”[[来源标题](https://www.linkedin.com/posts/vinoo-ganesh_earlier-today-anthropic-published-a-profile-activity-7455701330515652608-XSMV)]

虽然普通人往往不会仔细阅读就略过，但在决定巨额资金投资和贷款的金融文件中，脚注可能是致命的毒药，也可能是开启宝藏的黄金钥匙。例如，公司报告的正文用大字华丽地写着“今年营业利润增加了100亿韩元”，但在最底部几乎看不见的小字脚注中却写着“不过，这是与主业无关的一次性工厂用地出售所得”。即便是人，在疲惫时也很容易忽略这部分。

过去那些训练粗糙的AI往往不明白这些微小细节的重要性，只是把握整体氛围便敷衍了事。但是，在明确的任务和彻底的分步控制系统下，Kepler系统中的Claude不仅能够完成需要经历多个繁琐步骤的复杂财务推理，还能准确指出隐藏脚注的含义对整体财务状况的影响。这可以说是在减少人为错误的同时，完美地屏蔽了AI的弱点。

### 未来会怎样？ (What's Next)

Kepler的这项成果不仅是一个技术优秀的金融科技初创公司的短暂成功案例。他们坚持展现的“可验证AI”平台的设计架构，将为未来众多对引入AI犹豫不决的行业带来巨大的变革之风。

特别是不限于金融，在医疗、法律、国防、制药等任何一个微小错误都可能夺去人命或导致巨大财产损失的“高风险-高监管”行业中，Kepler的方法都将成为优秀的教科书和蓝图。为了防止医生误诊而经过严格逻辑验证阶段的医疗用AI，或在分析数万份法律判例时必须将幻觉现象控制在0%的法律AI等，都将借鉴这种“确定性基础设施”。

一直以来，我们只热衷于AI模型本身变得多么像人类一样聪明，或是学习了多少数据。但Kepler清楚地证明了，真正的行业创新取决于“如何将这种卓越的智能放入安全、可控的篮子中，并应用于不稳定的现实世界”。

未来，全球AI企业的竞争舞台将完全改变。核心范式将迅速从“谁能开发出更擅长写诗或小说的类人AI”转向“谁能构建出在面对挑剔的政府审计员尖锐提问时，能够提供完美依据公式进行辩护的AI系统”。

---

**MindTickleBytes AI的视角**

技术的发展往往像是一辆没有刹车的顶级跑车，看起来惊心动魄且危机四伏。如果以创新之名只执着于速度，最终很容易丢掉“信任”这条最重要的安全带。

但是，Kepler的案例很好地表明，AI真正的价值和爆发力矛盾地不是源自“无限的自由和自主性”，而是在“精密的控制和明确的限制设定”中绽放。为了完全取代人类判断而独自暴走的AI，永远无法跨越监管的厚重高墙。

取而代之的是，在人类精密设计的严格规则和围栏内，悄无声息地弥补人类不可避免的弱点（时间不足、体力下降、在海量数据面前的注意力减退）的透明且可验证的工具。那将是我们在这个现实世界中迎来的最理想、最安全的未来AI模型。人工智能真正融入我们生活核心基础设施的最后一道关卡，终究不是“智能”的高低，而是“信任”的深度。

---

## 参考资料
1. [Kepler如何使用Claude为金融服务构建可验证AI...](https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude)
2. [AI与金融的新前沿：Kepler为金融服务构建可验证AI...](https://www.fintechnews.org/new-frontiers-in-ai-and-finance-kepler-built-verifiable-ai-fon-financial-services-with-calude/)
3. [Kepler利用Claude构建用于金融的可验证AI - GogoAI新闻](https://www.gogoai.xin/article/kepler-builds-verifiable-ai-for-finance-with-claude)
4. [今日热门：Kepler如何为金融服务构建可验证AI...](https://trendflashy.com/trending-now-how-kepler-built-verifiable-ai-for-financial-services-with-claude/)
5. [Kepler如何为金融服务构建可验证AI... — RadarTrend](https://radartrend.com.br/topico/20598/how-kepler-built-verifiable-ai-for-financial-services-with-claude)
6. [今天早些时候，Anthropic发表了一篇关于Kepler及我们正在...的报道](https://www.linkedin.com/posts/vinoo-ganesh_earlier-today-anthropic-published-a-profile-activity-7455701330515652608-XSMV)