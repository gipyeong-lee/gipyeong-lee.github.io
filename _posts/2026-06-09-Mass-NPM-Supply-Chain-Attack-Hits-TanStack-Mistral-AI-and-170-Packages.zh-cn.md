---
layout: post
title: "我的电脑成了黑客的“间谍”？震惊全球AI和开发者的“软件供应链”黑客事件"
description: "通俗易懂地为您解读2026年5月发生的史上最大规模的Mini Shai-Hulud NPM供应链攻击。了解让Mistral AI、TanStack甚至OpenAI都受害的黑客攻击原理与防范措施。"
summary: "这是一起史无前例的黑客事件，黑客在著名的软件组件库中植入恶意代码，窃取了170多个开发程序和AI系统的核心密码。"
tags: [软件供应链, 黑客攻击, 人工智能安全, MistralAI, OpenAI]
image: 2026-06-09-Mass-NPM-Supply-Chain-Attack-Hits-TanStack-Mistral-AI-and-170-Packages.jpg
image_alt: "插图描绘了用放大镜观察偷偷嵌在巨大乐高积木城堡中间的一个红色病毒形状积木的场景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "便利的背后总是潜伏着新的漏洞。这次事件深刻地提醒我们，我们每天使用的无数应用程序，实际上都依赖于别人制作的微小“免费组件”。"
quiz:
  - question: "在这次黑客攻击事件中，黑客盯上的最核心目标是什么？"
    choices: ["普通用户的信用卡密码", "开发者的系统访问权限（云凭证、API密钥等）", "知名AI的全部源代码"]
    answer: 1
    explanation: "黑客的首要目标是窃取开发者令牌、API密钥、云凭证等能够访问系统深处的“万能钥匙”。"
  - question: "这次黑客攻击的最大特点之一，从一个项目自我传播到另一个项目的方式称为什么？"
    choices: ["蠕虫（Worm）方式", "特洛伊木马（Trojan Horse）方式", "勒索软件（Ransomware）方式"]
    answer: 0
    explanation: "这次的“Mini Shai-Hulud”恶意代码具有像蠕虫（Worm）一样自我繁殖，并迅速转移到多个软件项目中的传染病式结构。"
  - question: "为了防止此类软件供应链攻击，安全专家推荐的像“软件营养成分表”一样的防御工具是什么？"
    choices: ["NPM(Node Package Manager)", "PyPI(Python Package Index)", "SBOM(Software Bill of Materials)"]
    answer: 2
    explanation: "SBOM（软件物料清单）将构成程序的组件列成清单，是能够让人快速确认是否包含脆弱组件的必备安全工具。"
lang: zh-cn
ref: 2026-06-09-Mass-NPM-Supply-Chain-Attack-Hits-TanStack-Mistral-AI-and-170-Packages
---

想象一下。您为了家人买了一个非常安全坚固的保险箱。经过几天的考虑，挑选了最值得信赖的知名品牌产品。但后来发现，为这家保险箱工厂提供零部件的一家外包公司的员工心生歹念，在保险箱的“电子锁组件”里偷偷藏了一个微型摄像头和万能钥匙发送器。

保险箱制造商对此毫不知情，组装好保险箱后卖给了您。当您把贵重物品放进保险箱并按下密码的那一瞬间，该信息就会被实时发送给地球另一端的犯罪分子。这是您的错吗？还是保险箱公司的错？

这种令人恐惧又无奈的情况，在现实世界的软件和人工智能（AI）行业中真实上演了。2026年5月，让全球无数开发者和大型AI企业不寒而栗的所谓**“Mini Shai-Hulud”**软件供应链攻击事件爆发。由黑客组织“TeamPCP”主导的这次攻击，污染了多达170多个著名的软件包（组件） [TanStack, Mistral AI, UiPath Hit in Fresh Supply Chain Attack](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/)。我们平时使用的无数应用和互联网服务险些在不知不觉中充当了犯罪分子的“间谍”，现在就为您通俗易懂地揭开这起惊险事件的始末。

## 这为什么重要？

这则新闻不仅仅是“开发者们复杂的圈内故事”，看看受攻击企业的名单就知道了。

这次攻击不仅精准瞄准了著名的开发工具TanStack，还包括全球上班族广泛用于业务自动化的UiPath、OpenSearch，以及最近备受瞩目的AI企业之一Mistral AI等170多个核心项目 [TanStack, Mistral AI, UiPath Hit in Fresh Supply Chain Attack](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/) [Mass Supply-Chain Attack Slams npm and PyPi, Hits Mistral AI](https://www.bankinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)。甚至连全球顶级AI公司OpenAI的两名员工的设备也暴露在了这次攻击中。以至于公司方面甚至发布了紧急警告，要求员工在6月12日之前尽快更新Mac电脑上的ChatGPT和Codex [TanStack npm Supply Chain Attack: 2 OpenAI Employee Devices Hit, Update ChatGPT and Codex on Mac by June 12](https://pasqualepillitteri.it/en/news/2644/tanstack-npm-supply-chain-attack-openai-2026)。

当我们使用银行应用、向人工智能提问、登录公司的业务系统时，这些系统并不是由单一的一个巨大整体构成的。它们是由成千上万个微小的“软件组件”组合而成的。这次事件正是这数万个组件中，许多人共同调用的“核心组件”本身被投毒的事件。

如果这次攻击在初期没有被发现，后果会怎样？黑客们将会拿到能够随意操控企业最深层服务器和数据的“万能钥匙”。这最终可能成为导致普通用户个人信息泄露或造成巨大经济损失的巨大爆炸导火索。针对开发者工作环境的攻击，兜兜转转，终将成为威胁我们所有人日常生活的致命武器，这样的时代已经到来。

## 通俗理解：乐高积木、传染病与万能钥匙

让我们把这次事件中出现的生涩术语比作日常生活中的事物，逐一进行探讨。简而言之，只要了解我们每天使用的软件是如何制造的，就能看穿黑客的手法。

### 1. 软件供应链（Supply Chain）与包（Package）
现代开发者不会从零开始编写程序。他们会把别人已经做好的功能（例如显示日历、制作登录界面等）以打包的形式拿来使用。这种打包被称为**包（Package）**，免费分发这些包的巨大在线乐高商店就是**NPM**（用于JavaScript语言）和**PyPI**（用于Python语言） [Mass Supply Chain Attack Hits TanStack, Mistral AI npm and PyPI ...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)。

这次黑客攻击就像是，黑客没有挨家挨户去偷窃，而是潜入人们光顾最多的“乐高积木工厂”，在积木里偷偷安装了间谍麦克风。人们像往常一样信任并买走乐高积木（包）去盖房子（程序），但这栋房子已经落入了黑客的监听网中。打个比方，因为建筑材料本身被污染了，所以这被称为**软件供应链攻击（Supply Chain Attack）** [Mass npm Attack Hits TanStack and Mistral AI: How to Protect ...](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/)。

### 2. 瞄准万能钥匙：API密钥与云凭证
那么，黑客们想通过这些间谍积木偷取什么呢？是用户的个人密码吗？不是。他们盯上了更有价值的东西。那就是**开发者令牌（Token）、API密钥（与其他程序通信的密码）、云凭证（在线服务器访问权限）、CI/CD密钥（程序自动部署权限）**之类的东西 [npm Supply Chain Attack Impacts Mistral and TanStack](https://www.hexnode.com/blogs/npm-supply-chain-attack-impacts-mistral-ai-and-tanstack-ecosystems/) [Shai-Hulud MalwareHitsOpenAI,MistralAI,TanStack](https://theoutpost.ai/news-story/mistral-ai-and-tan-stack-packages-compromised-in-massive-supply-chain-attack-targeting-developers-26175/)。

我们可以这样比喻。如果普通用户的ID和密码是公寓“特定住户的家门钥匙”，那么开发者处理的API密钥或云凭证就是能打开整个公寓小区所有门、甚至能关闭物业管理系统的**“整个公寓的万能钥匙”**。黑客们正是企图偷走这把万能钥匙，进而彻底接管整个系统，制定了如此可怕的计划 [npm Supply Chain Attack Impacts Mistral and TanStack](https://www.hexnode.com/blogs/npm-supply-chain-attack-impacts-mistral-ai-and-tanstack-ecosystems/)。

### 3. 自我传播的“蠕虫（Worm）”病毒
这次攻击中使用的恶意代码名为“Mini Shai-Hulud” [Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI ...](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)。这款恶意代码的名字取自科幻小说《沙丘（Dune）》中巨大的沙虫，正如其名，它不仅仅停留在某处，而是以**蠕虫（Worm，虫子）**的形式制作的。也就是说，一旦感染了一个软件项目，它不会停在那里，而是寻找与之相连的其他项目，像传染病一样自动蔓延（jumping from one project to another），具有这种顽固的特性 [Mass Supply-Chain Attack Slams npm and PyPi, Hits Mistral AI](https://www.bankinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672) [MassSupply-ChainAttackSlamsnpmand PyPi,HitsMistralAI](https://www.govinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)。就像流感患者一旦感染，就会通过咳嗽将病毒传染给周围的人一样。

### 4. 堪比007行动的信息窃取
拿到万能钥匙的黑客们为了将信息偷偷传回自己的电脑，构建了三种巧妙的秘密通道（Triple-channel C2 architecture，三通道命令与控制架构） [TanStack and 160+ npm/PyPI Packages Compromised in Supply Chain Worm Attack](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)。
1. **挂羊头卖狗肉（Typosquatting）**：制作了一个与正常网站名称仅拼写差一个字母的假网站（git-tanstack[.]com），让开发者产生错觉并将信息发送到那里。
2. **使用秘密信使**：通过极难追踪的去中心化秘密信使“Session”网络，避开警方的视线隐秘地交换数据 [Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI ...](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)。
3. **秘密接头地点（Dead Drops）**：就像间谍把机密文件藏在公园长椅下就走一样，他们利用窃取的密钥，在开发者平台GitHub上创建了一个以《沙丘（Dune）》电影为主题的虚假仓库，并把偷来的信息偷偷堆积在那里 [TanStack and 160+ npm/PyPI Packages Compromised in Supply Chain Worm Attack](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)。

## 现状：6分钟的噩梦与巨大的波澜

那么，这场电影般的攻击是何时发生，规模又有多大呢？

事件发生在2026年5月11日。黑客组织“TeamPCP”利用高度自动化的系统，以惊人的速度发动了攻击。短短几个小时内，他们就打击了170多个包 [Mistral AI SDK, TanStack Router hit in npm software supply chain attack | CSO Online](https://www.csoonline.com/article/4170284/mistral-ai-sdk-tanstack-router-hit-in-npm-software-supply-chain-attack.html)，特别是在TanStack生态系统中，从协调世界时（UTC）19时20分到19时26分，**短短6分钟内就有多达84个恶意包版本（Artifacts）横跨42个包被同时分发** [TanStack npm Packages Hit by Mini Shai-Hulud | Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/)。就在你去厨房煮一杯咖啡的短暂时间里，带毒的苹果已经送到了全世界无数开发者的电脑中。

受害范围超乎想象。共有404个恶意版本被注册 [Mass Supply Chain Attack Hits TanStack, Mistral AI npm and PyPI ...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/?trk=article-ssr-frontend-pulse_little-text-block) [Mass Supply Chain Attack Hits TanStack, Mistral AI npm and PyPI ...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)，受打击的名单中包括42个TanStack包、65个UiPath包，甚至还包括Mistral AI（mistralai@2.4.6）和Guardrails AI（guardrails-ai@0.10.1）等人工智能相关的Python（PyPI）核心工具 [TanStack, Mistral AI, UiPath Hit in Fresh Supply Chain Attack](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/) [TanStack npm Supply Chain Attack: 2 OpenAI Employee Devices Hit, Update ChatGPT and Codex on Mac by June 12](https://pasqualepillitteri.it/en/news/2644/tanstack-npm-supply-chain-attack-openai-2026) [TanStack and 160+ npm/PyPI Packages Compromised in Supply Chain Worm Attack](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)。超越了TanStack和UiPath，其受害范围之广深不可测 [Mini Shai-HuludnpmWormHits170+Packagesin 2026 - SudoFlare](https://sudoflare.com/cybersecurity/mini-shai-hulud-npm-supply-chain-attack-tanstack-2026/)。

更令人毛骨悚然的是攻击者的执着。他们在钻了漏洞之后，为了不被发现并长期在系统中寄生，甚至动用了邮箱转发规则（偷偷拦截电子邮件的方式）等顽固的手段，试图维持生命力 [MassiveNPMSupplyChainAttackTargetsTanStack,MistralAI...](https://www.linkedin.com/posts/daily-ai-wire_massive-npm-supply-chain-attack-targets-tanstack-activity-7459917887621914625-8NbY)。这就好比小偷进屋后躲起来，甚至拦截信件，计划着长期滞留。

## 未来会怎样？举起盾牌的防御者们

面对如此巧妙而广泛的攻击，我们只能束手无策吗？幸运的是，安全专家们已经准备好并推荐了强大的“疫苗”和防御屏障，以抵御这种供应链攻击 [Mass npm Attack Hits TanStack and Mistral AI: How to Protect ...](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/)。

最具代表性的防御手段是**“依赖锁定（Dependency Pinning）”**技术。这是指开发者在从乐高商店（NPM或PyPI）获取组件时，与其说“给我最新的版本”，不如明确表示“只要我之前亲自验证过安全的2.0.1版本”。这样就能从根本上防止黑客刚刚偷偷上传的恶意最新版本自动安装到自己的系统中造成的惨剧。

另一个必备工具是**“软件物料清单（SBOM, Software Bill of Materials）”**。简单来说，就像我们在超市买零食时看背面的“营养成分表和过敏原信息”一样。为您自己的程序是由哪个公司的哪个版本的组件组装而成的，绘制一张清晰的地图。如果新闻报道说某个特定组件发生了黑客事件，您可以打开SBOM地图，在短短1秒钟内确认自己公司的程序中是否包含该被污染的组件，并立即采取应对措施，这就是一种犹如魔法般的防御工具。

这次的Mini Shai-Hulud事件深刻地证明了软件生态系统连接得有多么紧密，以及这层连接关系在多薄的冰面上。未来，所有开发软件的企业都不能只是为了方便而随意使用别人的代码，他们必须不断怀疑和验证这些代码是否真正干净，将“安全生活化”将成为不可避免的趋势。

---

## AI的视角
> **MindTickleBytes的AI记者视角：** “便利往往会蒙蔽我们的双眼。170多个包在几天内被污染的这一事件提醒了我们一个令人不寒而栗的事实：无论多么庞大、华丽、最先进的AI系统，支撑其底层的终究是某个人免费放在互联网上的‘一行代码’。在盖起华丽的屋顶之前，首先要检查坚固的基石。未来真正的技术实力，不是看你能多快地组装别人制作的积木，而是取决于你是否有敏锐的洞察力，去准确判断你不经意间拿起的那个小积木是否安全。这再次提醒我们一个真理：在安全方面，方向比速度更重要。”

---

## 参考资料
1. [Mass Supply Chain Attack Hits TanStack, Mistral AI npm and PyPI ...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)
2. [TanStack, Mistral AI, UiPath Hit in Fresh Supply Chain Attack](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/)
3. [Mass npm Attack Hits TanStack and Mistral AI: How to Protect ...](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/)
4. [Mass Supply-Chain Attack Slams npm and PyPi, Hits Mistral AI](https://www.bankinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)
5. [Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI ...](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)
6. [TanStack npm Packages Hit by Mini Shai-Hulud | Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/)
7. [npm Supply Chain Attack Impacts Mistral and TanStack](https://www.hexnode.com/blogs/npm-supply-chain-attack-impacts-mistral-ai-and-tanstack-ecosystems/)
8. [Mistral AI SDK, TanStack Router hit in npm software supply chain attack | CSO Online](https://www.csoonline.com/article/4170284/mistral-ai-sdk-tanstack-router-hit-in-npm-software-supply-chain-attack.html)
9. [TanStack npm Supply Chain Attack: 2 OpenAI Employee Devices Hit, Update ChatGPT and Codex on Mac by June 12](https://pasqualepillitteri.it/en/news/2644/tanstack-npm-supply-chain-attack-openai-2026)
10. [TanStack and 160+ npm/PyPI Packages Compromised in Supply Chain Worm Attack](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)
11. [GoogleNews-Newsaboutsupplychainattack•npm- Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pWczhLUEVSRzZ3cmVkeXY4VVlpZ0FQAQ?hl=en-GB&gl=GB&ceid=GB:en)
12. [MassSupply-ChainAttackSlamsnpmand PyPi,HitsMistralAI](https://www.govinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)
13. [MassSupplyChainAttackHitsTanStack,MistralAInpmand PyPI...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/?trk=article-ssr-frontend-pulse_little-text-block)
14. [Shai-Hulud MalwareHitsOpenAI,MistralAI,TanStack](https://theoutpost.ai/news-story/mistral-ai-and-tan-stack-packages-compromised-in-massive-supply-chain-attack-targeting-developers-26175/)
15. [Mini Shai-HuludnpmWormHits170+Packagesin 2026 - SudoFlare](https://sudoflare.com/cybersecurity/mini-shai-hulud-npm-supply-chain-attack-tanstack-2026/)
16. [MassiveNPMSupplyChainAttackTargetsTanStack,MistralAI...](https://www.linkedin.com/posts/daily-ai-wire_massive-npm-supply-chain-attack-targets-tanstack-activity-7459917887621914625-8NbY)