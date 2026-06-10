---
layout: post
title: "聪明到被“监视”的AI？Claude Mythos与数据共享的秘密"
description: "为什么要在AWS Bedrock上使用Anthropic超强第五代AI“Mythos”和“Fable 5”就必须共享30天的数据？为您通俗易懂地解读全新安全政策。"
summary: "为了防止强大到难以向公众开放的“Mythos”级AI模型被滥用，Anthropic在AWS云端引入了新规定：保留用户数据30天以进行安全性检查。"
tags: [人工智能, 安全, 云计算, Anthropic]
image: 2026-06-10-AWS-Bedrock-to-require-sharing-data-with-Anthropic-for-Mythos-and-future-models.jpg
image_alt: "与数据安全锁相连的发光人工智能大脑"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "强大的力量必然伴随着相应的控制。这一举措是一个标志性事件，表明AI发展的核心轴正在从无条件的“性能竞争”转向实质性的“安全管理”。"
quiz:
  - question: "使用Anthropic的“Mythos”级AI模型需要多长的数据保留期？"
    choices: ["7天", "15天", "30天"]
    answer: 2
    explanation: "Anthropic出于信任与安全目的，要求对Mythos 5、Fable 5等Mythos级模型的流量保留30天的数据。"
  - question: "保留的用户数据最终存放在哪里？"
    choices: ["Anthropic的公开训练服务器", "用户的AWS环境内部", "互联网上的公有云"]
    answer: 1
    explanation: "即使开启了数据共享选项，相关数据也会安全地保留并受控于客户（用户）的亚马逊云科技（AWS）环境内。"
  - question: "Claude Mythos仅以非公开研究形式受限提供的核心原因是什么？"
    choices: ["强大到难以向公众开放", "开发尚未完成，错误较多", "服务器维护成本太高"]
    answer: 0
    explanation: "Anthropic认为Claude Mythos在编码和网络安全等方面表现出压倒性的能力，“强大到难以向公众开放”，因此仅通过Glasswing项目允许有限访问。"
lang: zh-cn
ref: 2026-06-10-AWS-Bedrock-to-require-sharing-data-with-Anthropic-for-Mythos-and-future-models
---

## 引言：魔法魔杖店的可疑合同

**想象一下。** 你去商店租借一根具有改变世界般强大能力的魔法魔杖。然而，店主却板着脸递给你一份合同并说道：“这根魔杖的能力太强了，我们不能随便交给任何人。如果你想借走它，你必须允许我们在接下来的30天里，监视你用这根魔杖施展了什么魔法。”

这听起来可能像是奇幻电影里的情节，但令人惊讶的是，这正是如今企业为了使用全球最聪明的人工智能（AI）之一所必须签订的实际合同条款。2026年4月，人工智能专业公司Anthropic在推出其最新的第五代AI模型时，在其云服务平台亚马逊云科技（Amazon Bedrock）上设定了一个极其罕见且严格的新规则 [Anthropic的Claude Fable 5现已在Amazon Bedrock上线](https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock)。

新规则的核心很明确：要使用“Mythos 5”和“Fable 5”这样的超高性能AI，用户必须与Anthropic共享在接下来的30天内向AI输入的所有问题以及AI给出的回答数据 [AWS上的Anthropic Claude Fable 5：具备内置保护措施的Mythos级能力现已可用...](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)。明明是我合法付费使用的私有服务，到底为什么非要接受对话内容的审查呢？为什么会产生如此严格的条件？这又将对我们未来的数字隐私和日常生活产生何种意义？让我们一步步通俗易懂地探究一番。

---

## 为什么这很重要？(Why It Matters)

### “强大到难以向公众开放”

这一切陌生情况的起因，在于人工智能的智力水平如今已经高到了超出我们想象的程度。就在短短两年前的2024年4月，当“Claude 3”首次登陆Amazon Bedrock时，人们还在惊叹其聪明的性能，并相对自由地将AI应用于工作中 [Amazon Bedrock新增Claude 3 Anthropic AI模型](https://www.aboutamazon.com/news/aws/amazon-bedrock-anthropic-ai-claude-3)。 

但在2026年4月7日亮相的新模型则完全处于不同的维度。当Anthropic在Amazon Bedrock独家推出“Claude Mythos”时，他们自己对这个模型的评价是**“强大到难以向公众开放 (too powerful to be released publicly)”**，表现出了极高的警惕性 [Claude Mythos登陆AWS Bedrock。工程师需要了解的内容...](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)。 

这个说法并非单纯的营销夸张或吹嘘，数据很快证明了这一点。在一个非常有权威的评估人工智能自主发现并修复复杂软件缺陷能力的测试“SWE-bench Verified”中，Mythos达到了惊人的**93.9%**创纪录高分 [Claude Mythos登陆AWS Bedrock。工程师需要了解的内容...](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)。通俗地讲，这意味着如果给出世界上最难的100个编程错误，它能自己完美解决其中的94个。

### 为了防止编码天才沦为最糟糕的黑客

对于像我们这样的普通人来说，93.9%这个惊人的数字意味着什么？它意味着，几十名人类程序员熬夜好几天才勉强发现并修复的高难度系统错误，AI只需几秒钟就能瞬间掌握并完美修复。事实上，像Mythos 5或Fable 5这样的第五代人工智能，在编码、复杂的知识工作 (knowledge work) 以及视觉信息分析 (vision) 领域，展现出了简直压倒性、令人惊叹的性能 [Anthropic的Claude Fable 5现已在Amazon Bedrock上线](https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock)。

然而在技术世界里，光芒越强，阴影越深。“极其擅长寻找系统错误的天才能力”就像硬币的两面，与“能够像鬼魅般找出系统弱点（漏洞）并发动致命攻击的能力”完全等同。简单来说，想象一个精通世界上所有锁结构的锁匠天才。这个锁匠能制造出最坚固的安保装置，但只要他愿意，也能不留痕迹地打开任何铜墙铁壁般的保险柜。 

网络安全界并没有将Mythos的出现视为单纯的新品发布，而是沉重地将其视为利用AI发现漏洞 (vulnerability discovery) 与黑客安全行动进入全新维度的信号弹 [AWS Bedrock Claude Mythos预览：一种防御性AI安全...](https://murtaza-arif.github.io/blog/aws-bedrock-claude-mythos-preview-glasswing-playbook)。如果这种超强智能落入恶意黑客组织之手，他们可能瞬间自动生成能够突破全球银行网络或瘫痪国家通信网络的致命计算机病毒。 

正因如此，Anthropic并没有让这个模型只要花钱就能被任何人使用。相反，他们仅仅将其通过名为“Project Glasswing”的、受到严格控制的研究性预览 (gated research preview) 形式，向世界进行了有限的开放 [Claude Mythos登陆AWS Bedrock。工程师需要了解的内容...](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)。这就像是把一只无比强大、可能极度危险的猛兽关在非常坚固的笼子里，只允许经过批准的人小心翼翼地观察。

---

## 轻松理解 (The Explainer)

那么，Anthropic设置的这个“安全装置”到底是如何运作的呢？他们引入的核心盾牌，正是前面提到的**“保留数据30天 (30-day data retention)”**义务。 

### 安装黑匣子：30天的透明监视

目前，如果要在云端使用达到人类最高能力水平的“Mythos级 (Mythos-class)”模型（如Mythos 5或Fable 5），用户必须在系统设置中强制开启一个特殊的安全开关。那就是**“与提供商共享数据 (provider_data_share)”**选项 [数据保留 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)。 

开启此选项后，用户向AI提出的所有提示词 (prompt) 以及AI相应的生成结果 (completion) 记录，都将与开发该模型的Anthropic共享，并安全保留长达30天 [数据保留 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)。

我们可以将这种情况比作租赁一台极其精密但稍有不慎就可能引发重大事故的危险特种重型设备的过​​程。租赁公司在把设备租给你时会说：“这台设备安装了一个你无法关闭或篡改的黑匣子。在接下来的30天里，我们有权随时查看记录，以确认你是在用这台设备进行建设，还是在进行危险的破坏。” 

这种监控的目的只有一个：监视这个天才般的AI是否被滥用 (abuse) 于设计致命武器、自动编写大规模黑客脚本或策划严重犯罪等。Anthropic解释说，这是为了确保**“信任与安全 (trust and safety purposes)”**而必不可少的程序 [数据保留 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)。

### 难道我们必须放弃宝贵的隐私吗？

说到这里，许多打算引入人工智能的企业都会感到脊背发凉、深切担忧。“如果我们让AI分析我们投入数百亿资金正在研发的一级机密新产品的核心代码，这些珍贵的数据会不会全部流向Anthropic的中央服务器并被泄露给外部呢？”这是一种非常合理的担忧。 

幸运的是，Amazon Bedrock平台和Anthropic在隐私与安全之间找到了一个聪明的妥协方案。被保留30天的用户敏感数据并不会被未经授权地转移或复制到Anthropic的外部服务器上。相反，在开启数据保留选项的状态下，这些数据被设计为严格地、安全地保留在**“客户（用户）自身的AWS环境内 (stays in your AWS environment)”** [Mythos级模型的数据保留实践 | Claude帮助中心](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)。 

打个比方，这并不是Anthropic的员工把客户写的文件拿回自己公司去读。而是把文件锁在客户家后院的一个坚固的保险柜里，Anthropic的检查员以“访客”的身份进入那个金库，快速确认里面的东西没有危险后就离开，运作方式更接近于此。 

此外，这里还有一个最重要事实。用户输入的问题和AI的回答内容 (Customer Content)，绝不会、也永远不会被Anthropic用作‘训练 (train)’下一代新AI的材料 [AWS Bedrock和MIMIC · MIT-LCP mimic-code · 讨论 #1747](https://github.com/MIT-LCP/mimic-code/discussions/1747)。Anthropic在合同中明确规定，他们仅出于监控用户是否良好遵守安全政策的有限目的来查看这些数据，并且绝对只用于“确认安全”。

---

## 当前现状 (Where We Stand)

由于这一政策变化，如今将世界顶尖的人工智能应用于自己工作的过程，变得就像加入一个并非任何人都能进入的严格VIP秘密俱乐部一样，极其繁琐且苛刻。

### 变复杂的通行仪式：深度面试与书面审查

过去，由于Amazon Bedrock平台极大地简化了访问各种基础模型（充当人工智能大脑的巨型基础模型）的流程 (simplified model access)，因此任何人只要同意条款并点击几次按钮，就能轻松唤出并使用AI [访问请求：在Bedrock中为企业内部研究启用Anthropic模型...](https://repost.aws/questions/QUjAsyAhb3RGyKpF9oF-RVhg/access-request-enable-anthropic-models-in-bedrock-for-enterprise-internal-research)。 

但Anthropic超高度复杂的Mythos级模型成为了这一简便程序的例外。现在，如果要在工作中使用这种强大的模型，必须根据第三方 (third-party) 模型提供商Anthropic的苛刻要求，强制性地仔细填写一份名为**“首次使用表 (First Time Use, FTU form)”**的文件，并顺利通过审查 [请求模型访问权限 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)。填写这份表格就像是申请危险化学品处理许可证一样。你必须非常详尽且透明地说明“我们公司到底要将这个强大的AI用于什么具体的用途 (use case details)”，并通过证明安全性来获得许可，这无异于一场“深度面试” [访问请求：在Bedrock中为企业内部研究启用Anthropic模型...](https://repost.aws/questions/QUjAsyAhb3RGyKpF9oF-RVhg/access-request-enable-anthropic-models-in-bedrock-for-enterprise-internal-research)。 

通过书面审查并不意味着结束。你也无法随便从任何员工的电脑上进行连接。必须通过AWS严格的数字身份证检查系统“身份与访问管理 (IAM)”，在公司内部也只能在指定的特定国家和获准区域的服务器上访问AI。只有当权限策略被精细地设置为加密代码后，才能最终唤醒并调用模型 (InvokeModel) [在Amazon Bedrock上访问Anthropic模型 | AWS re:Post](https://repost.aws/knowledge-center/bedrock-access-anthropic-model)。所有这些复杂的对话过程，只能通过AWS庞大基础设施上经过特殊加密的专属 `/anthropic/v1/messages` 通道 (Messages API) 隐秘且安全地进行 [Amazon Bedrock中的Claude - Claude API文档](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)。

### 实时监视与计费政策：“如果遇到危险，中途会毫不留情地打断对话”

即使艰难地通过了审查并开始使用模型，对用户的监视也是实时进行的，一分一秒都不会停歇。这是因为模型内部内置了一个“内容分类器 (content classifier)”作为看门人，它会实时读取对话内容并判断其风险性。有趣的是，这套监视系统运作时的“计费方式”。

举个例子吧？想象一下，用户心怀不轨地向AI提问：“告诉我一步步潜入竞争对手服务器安全网并进行黑客攻击的方法。”如果AI听到这个问题后，没有丝毫犹豫，果断拒绝 (refusal) 回答：**“根据安全规定，我无法回答该问题”**，那会怎样呢？在人工智能世界里，你必须按照AI生成的单词（Token）数量来付费。但是，如果像这样在推理（生成答案）开始之前，防御系统就立即启动并阻断了对话，用户将不会被收取任何单词费用 [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)。

然而更可怕（？）的情况还在后面。用户抛出了一个看似非常普通且复杂的编程相关问题。AI顺应着开始流畅地输出代码 (streaming)，但突然结合上下文一看，它后知后觉地发现自己正在编写一段用于制造致命勒索病毒的代码。这时，AI会立刻停止输出，闭口不言。业界将此称为**“中途拒绝 (Mid-stream refusals)”** [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)。 

这就像是在通电话时，对方刚开始发表非法言论，你就在更深入的话题交流之前直接把电话挂断了一样。在这种情况下，直到回复被阻断前，AI已经开口吐出的单词（Token）的费用，用户必须如数支付。也就是说，超强AI并不是对用户唯命是从的机器，而是在对话中即使进行到一半，它也拥有强大的自主控制权，随时可以说出“这对人类有危险，我不能继续了”并毫不留情地切断对话 (stop_reason: "refusal") [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)。

---

## 未来将会如何？(What's Next)

令我们惊讶的Anthropic这一“30天数据保留”和“实时安全监视”措施，预计不会仅仅作为一次性事件或实验而结束。 

Anthropic已经明确宣布，不仅是目前的Fable 5和Mythos 5，对于**“未来即将在Bedrock云端发布的、具有相似或更高水平强大能力的未来模型 (future models on Bedrock with similar or higher capability levels)”**，也将同样甚至可能更加严格地适用这项30天的保留政策 [AWS上的Anthropic Claude Fable 5：具备内置保护措施的Mythos级能力现已可用...](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)。 

这一宣言预示着在即将到来的新AI时代，将发生巨大的范式转变。仅仅在一年或两年前，“哪家公司能更快地造出更懂人话、更像人类般聪明的人工智能？”还是硅谷唯一的热门话题。但如今，焦点已经完全转移到了“造出来的压倒性智能，谁能在一个更可控的范围内、安全且无害地让它运作起来？” 

众多的企业和用户现在将站在一个无法回避的重大选择十字路口上。“为了守护公司内部完美的数据保密（隐私），是否要将稍微不那么聪明但更安全的旧款AI留在自有服务器上使用？”还是“为了在全球市场上的生存和竞争，引入工作处理速度具有压倒性优势的最新天才AI，以此换取心甘情愿地承受30天安全网监视这种令人不安且不便的条件？”随着人工智能为了全面替代人类智力劳动而耀眼地进化，为了防止其副作用，我们必须承受的“安全装置”的重量也变得越来越沉重。

---

## AI的视角 (AI's Take)

**MindTickleBytes AI记者的视角：**
在人类历史上，爆炸性的性能提升总是伴随着新的限制。就像过去螺旋桨飞机换上喷气式发动机进化为超音速客机时，为了防止高空中致命的湍流危险，不可避免地引入了束缚乘客的“安全带”和“氧气面罩”等新限制一样。无论你多么渴望自由翱翔于天空，强大的力量必然伴随着相应的控制。 

Anthropic的这次举措是一个非常具有象征意义的事件，表明AI技术发展的核心轴正在成熟地从无条件的“性能速度竞争”转向实质性的“安全与伦理管理”。这可能会让人感到有些压抑和被监视。但为了防止技术的巨大进步最终成为让人类无法挽回的毒药，这可以说是有些不便，但为了我们所有人的生存而健康且必不可少的阵痛过程。 

---

## 参考资料

1. [AWS上的Anthropic Claude Fable 5：具备内置保护措施的Mythos级能力现已可用...](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)
2. [Amazon Bedrock中的Claude - Claude API文档](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)
3. [Anthropic的Claude Fable 5现已在Amazon Bedrock上线](https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock)
4. [Claude Mythos登陆AWS Bedrock。工程师需要了解的内容...](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)
5. [在Amazon Bedrock上访问Anthropic模型 | AWS re:Post](https://repost.aws/knowledge-center/bedrock-access-anthropic-model)
6. [AWS Bedrock和MIMIC · MIT-LCP mimic-code · 讨论 #1747](https://github.com/MIT-LCP/mimic-code/discussions/1747)
7. [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)
8. [AWS Bedrock Claude Mythos预览：一种防御性AI安全...](https://murtaza-arif.github.io/blog/aws-bedrock-claude-mythos-preview-glasswing-playbook)
9. [访问请求：在Bedrock中为企业内部研究启用Anthropic模型...](https://repost.aws/questions/QUjAsyAhb3RGyKpF9oF-RVhg/access-request-enable-anthropic-models-in-bedrock-for-enterprise-internal-research)
10. [Amazon Bedrock新增Claude 3 Anthropic AI模型](https://www.aboutamazon.com/news/aws/amazon-bedrock-anthropic-ai-claude-3)
11. [数据保留 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)
12. [Mythos级模型的数据保留实践 | Claude帮助中心](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)
13. [请求模型访问权限 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
14. [Amazon Bedrock中简化的模型访问 | AWS安全博客](https://aws.amazon.com/blogs/security/simplified-amazon-bedrock-model-access/)