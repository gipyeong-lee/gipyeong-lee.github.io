---
layout: post
title: "要把我的提问保存30天？Anthropic的新AI政策为何引发争议"
description: "Anthropic发布了性能最强的AI模型Claude Fable 5和Mythos 5，并强制推行30天数据保留政策。本文将为您浅显易懂地梳理企业为何强烈反对，以及微软限制内部使用的原因。"
summary: "随着功能强大的新AI模型以安全监控为由，强制将用户的提问和回答保留30天，由于担心企业机密泄露，主要企业纷纷限制其使用，引发了越来越大的隐私争议。"
tags: [Anthropic, Claude, 隐私, AI安全, 企业, 网络安全]
image: 2026-06-11-Anthropic-requires-30-day-data-retention-for-Fable-and-Mythos.jpg
image_alt: "一个聪明的机器人在开启安全摄像头的房间里审查重要文件的画面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "为了享受更聪明的AI带来的便利，我们的隐私到底要让步到什么程度？强大的技术控制与数据主权之间激烈的拉锯战，现在才刚刚正式拉开帷幕。"
quiz:
  - question: "Anthropic在Claude Fable 5和Mythos 5中新引入的数据保留期限是多久？"
    choices: ["不保留（立即删除）", "30天", "1年"]
    answer: 1
    explanation: "Anthropic以系统安全监控为名，实施了强制保留所有提示词和生成结果至少30天的政策。"
  - question: "企业客户之前与Anthropic签订的“零保留（数据立即删除）”协议在这一新政策下将如何处理？"
    choices: ["现有协议优先并继续有效", "新的30天保留政策将使现有协议失效并强制执行", "用户可以自由选择是否保留"]
    answer: 1
    explanation: "新的30天强制数据保留政策将强制使企业之前签订的所有零保留协议失效（override），并作为最优先政策执行。"
  - question: "微软限制其员工使用Claude Fable 5的主要原因是什么？"
    choices: ["为了降低竞争对手模型的市场份额", "担心新数据保留政策导致公司机密信息泄露和隐私侵犯", "因为AI模型的编程能力明显下降"]
    answer: 1
    explanation: "微软认为Anthropic强制性的30天数据保留政策对企业数据隐私构成了严重风险，因此全面限制了内部使用。"
lang: zh-cn
ref: 2026-06-11-Anthropic-requires-30-day-data-retention-for-Fable-and-Mythos
---

想象一下，您正在公司起草一份关乎公司命运的极为重要的新产品发布计划，或者是核心技术骨架的设计图。由于独自处理这项庞大的工作实在过于吃力，您决定向一位非常聪明、处理速度极快的AI助手寻求帮助。 

“我会把我们的绝密配方和核心营销战略资料发给你，请帮我完美地整理成明早高管会议的演示文稿。” 

幸运的是，这位优秀的助手已经签署了一份严格的保密协议，承诺“工作一结束，我就会把刚才看过的文件内容从脑海中彻底抹去”。于是，您放心地将关系到公司未来的机密文件交到了这位助手的手中。

然而有一天，这位助手称自己的业务能力得到了大幅升级，并突然改变了态度。“由于我现在变得太聪明了，我担心我处理的信息可能会牵涉到恶性犯罪。因此，为了确认安全性，我必须强制将您提供的所有文件在我的私人保险箱里保留‘30天’并进行监控。我以前签的那份立即删除协议从今天起全面失效。” 

如果是您，还会继续放心地把公司的最高机密交给这位助手吗？恐怕大多数人都会慌忙夺回文件，立刻离开房间。

而这个令人错愕的剧本，正原封不动地在当今全球IT行业的现实中上演。2026年6月9日，著名人工智能公司Anthropic突击发布了其史上性能最强的AI模型“Claude Fable 5”以及更加专业且受限的版本“Mythos 5”[[Anthropic针对Claude Fable 5的新30天数据保留政策是否...](https://www.linkedin.com/pulse/does-anthropics-new-30-day-data-retention-claude-fable-jonathan-milne-qhrfe)]。 

然而，外界热切关注的焦点并不是这些模型所展现出的惊人智力或压倒性的编程能力。人们的目光正严厉地聚焦在他们新抛出的“强制保留数据30天”这一隐藏账单上。

在线社区和互联网空间立刻被强烈的愤怒所淹没[[Claude Fable 5发布后，互联网对Anthropic感到愤怒 - Decrypt](https://decrypt.co/370688/internet-furious-anthropic-claude-mythos-fable-5)]，包括微软在内的主要科技巨头的安全部门也立即拉响了警报。具备世界顶尖水平的AI华丽登场，迎来的却不是掌声与欢呼，而是满天飞的担忧与警惕。这背后究竟发生了什么？

## 这为什么重要？ (Why It Matters)

随着AI技术的飞速发展，现代企业和个人正在将过去无法比拟的极其敏感的信息输入AI系统，并依赖其结果。 

软件工程师在编写企业核心源代码时借助AI缩短工作时间；医生在分析医院复杂的患者数据时希望通过AI得出更准确的诊断；财务专家则让AI提前审查尚未公开的企业业绩报表。当每天都要处理如此致命且敏感的信息时，企业最优先考虑的绝对价值只有一个，那就是隐私（Privacy，个人信息及机密保护）与彻底的数据安全。因为一次泄露就可能直接导致公司破产。

为了消除企业这种巨大的不安感，此前大多数企业客户都会与AI服务提供商签订严格的“零保留（Zero-retention，数据在服务器上不保存哪怕一秒钟，处理完毕后立即删除的政策）”协议。正是得益于这项协议，企业才得以安心地将AI积极应用于实际业务中。也就是说，存在着一个坚定且明确的承诺：无论用户向AI询问了什么机密，得到了怎样出色的回答，只要关闭会话窗口，相关记录就会从服务器上永久销毁。对企业而言，这是将AI引入内部网络的唯一底线。

然而，Anthropic在向世界公开本次新型Claude模型时，抛出了一个惊人的重磅炸弹。他们单方面宣布了一项新政策，强制规定必须将所有用户的提示词（Prompt，给AI下达的命令或问题）以及AI生成的结果流量在其服务器上保留“30天”[[Fable 5和Mythos 5将如何改变AI安全、数据保留...](https://www.forrester.com/blogs/how-fable-5-and-mythos-5-change-ai-security-data-retention-and-vendor-risk/)]。 

尤其让业界感到最为震惊的是，这项新的30天强制保留条款，竟然会强制覆盖（override）并优先于众多企业客户此前花费数百万美元签订的铁桶般的零保留协议[[Anthropic的Claude Fable是公众能够访问的Mythos版本...](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/)]。过去的承诺，现在可以说不再奏效了。

更为严重的是这项可怕政策的适用范围。它并不局限于在Anthropic自家官方网站（第一方服务）上使用模型时。即使是通过亚马逊云科技（AWS）的云平台Bedrock，或是GitHub Copilot等第三方（Third-party）合作伙伴平台间接运行该AI时，这项30天保留义务也会无一例外地无条件适用[[AWS上的Anthropic Claude Fable 5：具备内置保护的Mythos级功能现已上线 | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)][[Anthropic将高风险Fable 5提示词路由至Opus 4.8](https://www.implicator.ai/anthropic-routes-high-risk-fable-5-queries-to-opus-4-8-in-public-rollout/)][[Claude Fable 5数据保留合规指南 | Lushbinary](https://lushbinary.com/blog/claude-fable-5-enterprise-data-retention-compliance-guide/)][[Claude Fable 5发布后，互联网对Anthropic感到愤怒 - Decrypt](https://decrypt.co/370688/internet-furious-anthropic-claude-mythos-fable-5)]。 

打个通俗的比方，这就好比您包下了一间顶级酒店套房（AWS）好几天，准备召开一场完全不受外界干扰的绝密会议。但制造了房间里那张柔软大床的家具公司（Anthropic）却固执地要求：“要用我们公司的床，就必须在房间里安装我们公司的安全摄像头，并且我们必须拿走30天的录像。”这实际上无异于在向全世界所有的企业理直气壮地宣告：“想租用我们最顶级的AI智力，就得把你们视若生命般的机密数据乖乖交到我们手里保管整整一个月。”

## 简单通俗地理解 (The Explainer)

Anthropic到底为什么要在明知会引发最重要客户——企业群体的强烈抗议和流失的情况下，依然强行推行这种无理的要求呢？他们用来作为挡箭牌的理由只有一个，那就是保护人类免受致命风险威胁的“安全（Safety）”。

我们可以用日常使用的工具的危险性来打个比方。当您把在社区游乐场堆沙堡的轻便塑料铲借给邻居时，不需要任何身份审查或文件证明。因为就算用错了，顶多也就是溅起一点沙子罢了。但如果要出租能把整座岩山炸飞的高性能炸药，情况就完全不同了。必须进行彻底的身份背景调查，安装追踪装置以确保炸药究竟用在了哪里，为了防止事故，还必须用闭路电视对整个过程进行严密的监控。 

同理，随着AI模型的能力变得极其强大，达到了过去无法比拟的程度，如果将其用于恶意目的，对全人类可能造成的损害规模也将呈指数级增长。 

此次全新发布的Claude Fable 5在海量知识工作、复杂的视觉信息处理、甚至是自己移动鼠标操作电脑的能力，以及高级编程领域，都具备了目前现存最高水平（State-of-the-art）的能力[[Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable)]。而在这个基础上更进一阶的Mythos 5模型，则是登顶了高度网络安全系统防御网构建、深度生物学研究以及专业医疗领域的终极模型[[ClaudeMythos\Anthropic](https://www.anthropic.com/claude/mythos)]。 

如果这样一个拥有极其庞大的专家级知识和能力的AI落入黑客或恐怖分子之手，在眨眼之间就为他们编写出能够瘫痪国家电网的恶意代码，或者“贴心地”暗中指导如何制造致命的生物武器，那将是一场绝对无法挽回的恐怖灾难。

因此，Anthropic决定全面启动被称为“安全分类器（Safety Classifiers，即一种能实时判别危险征兆的人工智能监控程序）”的24小时主动监控系统，以便在AI与用户对话的过程中，实时监控其是否做出了此类危险行为或违反自身规定的举动[[致所有准备使用Fable 5的组织：他们将保留您的...](https://cybernews.com/ai-news/claude-fable-five-data-retention-collection/)][[出于对数据保留的担忧，微软限制员工使用Claude Fable | The Verge](https://www.theverge.com/report/947575/microsoft-claude-fable-5-restricted-internally)]。 

然而，这个监控系统若想完美掌握对话的前后语境并准确评估实际危险性，就绝对需要“时间”和存储下来的“数据”，以深入分析用户到底带着什么意图提出问题，AI又给出了什么样的回答等前后脉络。 

最终，Anthropic得出的结论是，为了准确无误地执行这项复杂的安全监控任务，最少30天的保留期限是必不可少的。他们果断拔掉了企业们如此信赖和渴望的名为零保留的可靠“文档即时粉碎机”的电源线，取而代之的是在原地安装了一台长达30天强制录像的强大“安全监控摄像头”。

当然，Anthropic为了安抚愤怒的企业客户们的强烈抗议和深切担忧，也急忙补充了一项重要承诺。他们明确表示，强制保留的商业客户的敏感流量数据，将极其严格地仅用于安全监控这一原本的防御性目的，绝不会胡乱收集这些数据来训练（学习）新一代的Claude AI模型[[Anthropic推出Claude Fable 5... — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)]。但尽管有这样积极的解释和承诺，对于想要彻底打消已经被打破的信任和企业心中深深的焦虑感，目前依然显得力不从心。

## 目前的状况 (Where We Stand)

这一破格且颇显单方面的政策一经公布，IT市场和主要企业客户的反应便是冷淡且坚决的。行动最快、反应最敏感的，正是IT界的巨头、以彻底的安全防御为标志的微软（Microsoft）。 

微软对Anthropic这项新数据保留政策提出了沉重的担忧，认为这与自身严格的数据隐私标准发生了正面冲突，于是果断采取了极其强硬的措施：立即限制公司内部大量员工在内部工作网络中访问和使用Claude Fable 5模型[[因担心数据保留问题，微软限制员工访问Anthropic的Claude Fable 5](https://cryptobriefing.com/microsoft-restricts-claude-fable-5-data-retention/)][[出于对数据保留的担忧，微软限制员工使用Claude Fable | The Verge](https://www.theverge.com/report/947575/microsoft-claude-fable-5-restricted-internally)]。即便是世界上在安全方面最严密、对AI趋势最敏感的全球顶尖科技企业，也冷静地断定，他们绝不能承受作为公司骨干的内部机密被长达30天之久地束缚在不受控制的外部服务器上这种令人眩晕的风险。

更让用户们感到不安、乃至夜不能寐的一点在于，数据被留存的期限，可能未必只在短短的（?）30天后就宣告结束。根据相关报道和Anthropic政策的细节内容，如果安全分类器系统将特定用户的提示词或AI的生成结果怀疑为严重的潜在危险因素（例如：精密的黑客攻击尝试、危险化学物质相关讨论等）并亮起红灯时，相关数据为了进行精确分析和深度调查，有可能会在服务器上保留长达2年时间[[出于对数据保留的担忧，微软限制员工使用Claude Fable | The Verge](https://www.theverge.com/report/947575/microsoft-claude-fable-5-restricted-internally)]。 

到底是因为什么模糊又隐秘的标准，会导致自己宝贵的工作数据长达2年之久被关在别家公司的保险箱里？站在用户的立场上，由于缺乏确保其透明度或予以追责追问的适当方法，自然只能担惊受怕。

正因如此，目前全世界众多的跨国大企业和创新型初创公司都陷入了痛苦的进退两难的困境。是雇佣当前现存最聪明、能让员工工作效率飙升数十倍的卓越AI助手（Fable 5、Mythos 5），从而在激烈的市场竞争中拔得头筹？还是为了牢牢守护如同公司生命线一般的绝对数据主权与安全，宁可忍受工作性能略微逊色，也要继续坚持使用能保障传统安全“零保留”的旧版AI或竞争对手那不那么聪明的替代模型？此时此刻，在无数企业的安全主管和管理层的会议室里，连日来正在展开一场场激烈的马拉松式讨论。

最重要的是，互联网社区的大量开发者之所以表达出最深切的忧虑，是因为这项政策具有可怕的扩展性。根据Anthropic断然宣布的表述，这种强制性的保留政策绝不仅仅是适用于本月发布的Fable 5或Mythos 5模型的临时性措施。未来所有发布的功能水平相近、或具备更强大超大智能的“Mythos级别（Mythos-class）”未来巨型模型，都将永久且无例外地适用该政策[[Anthropic通过Claude Fable 5将Mythos推向大众，这是其有史以来最强大的普遍可用模型 | VentureBeat](https://venturebeat.com/technology/anthropic-brings-mythos-to-the-masses-with-claude-fable-5-its-most-powerful-generally-available-model-ever/)][[Claude Fable 5数据保留合规指南 | Lushbinary](https://lushbinary.com/blog/claude-fable-5-enterprise-data-retention-compliance-guide/)][[Claude Fable 5发布后，互联网对Anthropic感到愤怒 - Decrypt](https://decrypt.co/370688/internet-furious-anthropic-claude-mythos-fable-5)]。 

在最先讨论最新IT动向的HackerNews等开发者社区，这一消息也立刻成为了烫手山芋，引发了激烈的赞成与反对的论战[[Anthropic要求对Fable进行30天的数据保留... | HackerNews](https://news.ycombinator.com/item?id=48464258)]。换句话说，为了享受更加卓越和梦幻的人工智能带来的好处，这正暗藏着极大的风险：它可能会成为人类未来必须要支付且无法逃避的“新型过路费”，并固化为整个人工智能行业的新标准（Standard）。

## 未来将会怎样？ (What's Next)

此时此刻，在惊人的人工智能技术发展史上，我们正在经历一个将永远决定人类隐私走向的极其重大而又惊险万分的转折点。 

随着AI变得比人类更聪明，并深入渗透到连人类都难以轻易胜任的极其复杂和精密的领域，为了防患于未然而防止其可能带来的毁灭性风险，相关的控制与监控的强度也必须成比例地、严密地提高。Anthropic“安全优先”的主张，在哲学层面上确实有其合理的一面。为了防止令人目眩的技术发展那可怕的加速度，在某一刻彻底摆脱人类微弱的控制力，提前构建坚固而巨大的“安全网”，也许对于全人类的生存与未来而言，这是某人必须顶着骂名去完成的痛苦却必不可少的任务。

然而，在强制构建和维持这张沉重而巨大的安全网的过程中，个人和企业长期以来艰苦奋斗所守护的“隐私”和“数据主权”这两项决不能让步的根本基本权利，正在发生严重的动摇与尖锐的冲突。微软迅速全面限制内部访问的措施，可能仅仅是这一巨大冲突的冰山一角。 

在未来，但凡一次数据泄露事故就可能决定整个公司存亡的严谨金融界、处理极度敏感且私密的患者生命信息的保守医疗界、以及以严守秘密为生存之本的法律界的众多企业，极有可能会从零开始全面重新评估是否在业务中引入和使用最新的Claude模型。

## AI的视角 (AI's Take)

为了享受更聪明的AI带来的便利，我们的隐私到底要让步到什么程度？强大的技术控制与数据主权之间激烈的拉锯战，现在才刚刚正式拉开帷幕。 

随着人工智能智力的爆炸式增长，人类现在开始将AI不仅仅视为一种方便的简单工具，而是将其视为一种潜在的危险因素。Anthropic此次固执的决定，正是源于AI的能力有朝一日可能彻底摆脱人类控制这一根本性的恐惧。 

但站在企业和个人的立场上来看，自己倾注心血制成的最敏感信息，竟然要在不受控制的他人的服务器上停留30天，甚至根据模糊的标准最长停留达2年之久，这一事实无疑会让人感到极其不安和不适。 

既想尽情自由地利用极具创新和最高性能的AI技术，又希望自己宝贵的信息能够免受外界窥探、得到完美保护，这是人类最根本的欲望。而另一方面，为了全人类的安全，又必须仔细审查和监控一切潜在风险的AI安全网。这两者之间紧绷而令人窒息的紧张对峙感，在未来将会变得更加激烈。最终，哪家企业能够用最优雅的技术手段解决这一巨大的矛盾，也许就能真正主宰未来的AI市场。

在一段时间内，我们将怀着极大的兴趣拭目以待：Anthropic这种坚决而强硬的隐私限制政策，究竟能否战胜看重效率的市场冷酷逻辑，并坚定地成为整个行业的新标准。此外，那些将敏锐地切入这一冲突缝隙的众多竞争AI企业们，为了吸引深感不安的企业客户，又会抛出怎样充满创意的诱饵和富有魅力的替代政策，这也是一个非常重要的看点。因为真正的技术创新，总是会在这样出人意料的激烈冲突和痛苦的阵痛中，找到其明朗的答案。

---

## 参考资料

1. [Fable 5和Mythos 5将如何改变AI安全、数据保留...](https://www.forrester.com/blogs/how-fable-5-and-mythos-5-change-ai-security-data-retention-and-vendor-risk/)
2. [Anthropic针对Claude Fable 5的新30天数据保留政策是否...](https://www.linkedin.com/pulse/does-anthropics-new-30-day-data-retention-claude-fable-jonathan-milne-qhrfe)
3. [Claude Fable 5发布后，互联网对Anthropic感到愤怒 - Decrypt](https://decrypt.co/370688/internet-furious-anthropic-claude-mythos-fable-5)
4. [Anthropic的Claude Fable是公众能够访问的Mythos版本...](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/)
5. [AWS上的Anthropic Claude Fable 5：具备内置保护的Mythos级功能现已上线 | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)
6. [Anthropic将高风险Fable 5提示词路由至Opus 4.8](https://www.implicator.ai/anthropic-routes-high-risk-fable-5-queries-to-opus-4-8-in-public-rollout/)
7. [Claude Fable 5数据保留合规指南 | Lushbinary](https://lushbinary.com/blog/claude-fable-5-enterprise-data-retention-compliance-guide/)
8. [Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable)
9. [ClaudeMythos\Anthropic](https://www.anthropic.com/claude/mythos)
10. [致所有准备使用Fable 5的组织：他们将保留您的...](https://cybernews.com/ai-news/claude-fable-five-data-retention-collection/)
11. [出于对数据保留的担忧，微软限制员工使用Claude Fable | The Verge](https://www.theverge.com/report/947575/microsoft-claude-fable-5-restricted-internally)
12. [Anthropic推出Claude Fable 5... — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)
13. [因担心数据保留问题，微软限制员工访问Anthropic的Claude Fable 5](https://cryptobriefing.com/microsoft-restricts-claude-fable-5-data-retention/)
14. [Anthropic通过Claude Fable 5将Mythos推向大众，这是其有史以来最强大的普遍可用模型 | VentureBeat](https://venturebeat.com/technology/anthropic-brings-mythos-to-the-masses-with-claude-fable-5-its-most-powerful-generally-available-model-ever)
15. [Anthropic要求对Fable进行30天的数据保留... | HackerNews](https://news.ycombinator.com/item?id=48464258)