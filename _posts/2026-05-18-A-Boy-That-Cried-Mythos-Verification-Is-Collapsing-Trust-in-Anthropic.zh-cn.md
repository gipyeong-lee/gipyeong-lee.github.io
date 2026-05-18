---
layout: post
title: "AI 代替黑客寻找安全漏洞？围绕“Mythos”的 Anthropic“狼来了”争议"
description: "Anthropic 的新 AI 模型“Mythos”在 Firefox 浏览器中发现了多达 271 个安全漏洞。本文将为您深入浅出地解释为什么白宫高度关注此模型，以及为何安全专家批评其为夸大营销。"
summary: "Anthropic 的 AI 模型 Mythos 以惊人的速度发现系统安全漏洞并引起了白宫的关注，但与此同时，由于缺乏内部验证的夸大宣传和荒唐的自身安全泄露事件，它正在失去信任。"
tags: [Anthropic, Mythos, Cybersecurity, AI]
image: 2026-05-18-A-Boy-That-Cried-Mythos-Verification-Is-Collapsing-Trust-in-Anthropic.jpg
image_alt: "插画：一个手持巨大放大镜的机器人正在错综复杂的计算机代码中仔细寻找隐藏的锁状孔洞"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在夸耀惊人技术成就的同时，却连自身基本安全都无法保障，这种透明度的缺失只会加剧公众的疲劳感。不可信的警告最终只会在最关键时刻演变成无人理会的“狼来了”式的呼喊。"
quiz:
  - question: "Anthropic 的 AI 模型‘Mythos’预览版在 Firefox 浏览器中发现了多少个致命的安全漏洞？"
    choices: ["147个", "244个", "271个"]
    answer: 2
    explanation: "在初步评估过程中，Mythos 预览版发现了 Firefox 浏览器中 271 个连人类专家都忽略的零日漏洞，这些漏洞已在最新更新中得到修复。"
  - question: "在 Mythos 相关事件中，导致 Anthropic 信任度降至谷底的近期安全泄露事故的直接原因是什么？"
    choices: ["黑客物理潜入了 Anthropic 总部服务器机房。", "使用了被盗的第三方承包商登录信息，并以猜测内部 URL 的初级方式访问了模型。", "利用强大的量子计算机破解了 Anthropic 的核心密码。"]
    answer: 1
    explanation: "标榜拥有顶级黑客防御技术的 Anthropic，讽刺地因为被盗的第三方公司登录信息和猜测网页地址这种极其基础和初级的方式，遭遇了未发布模型泄露的屈辱。"
  - question: "在 Anthropic 发布的大量 Mythos 系统卡（System Card）文档中，真正用于支持其‘该模型极其危险，无法发布’这一核心主张的内容共有多少页？"
    choices: ["244页全篇", "约占一半的120页", "仅7页"]
    answer: 2
    explanation: "分析长达 244 页（容量 23MB）的海量安全文档后发现，真正涉及警告模型严重风险并主张阻止发布的核内容仅有 7 页，因此遭到了强烈批评。"
lang: zh-cn
ref: 2026-05-18-A-Boy-That-Cried-Mythos-Verification-Is-Collapsing-Trust-in-Anthropic
---

试想一下。在我们每天习惯性使用的浏览器、与朋友聊天的手机信使，以及存有毕生积蓄的银行应用中，可能到处都隐藏着连天才开发者都未能发现的微小“后门”。

通常，隶属于企业的白帽黑客（以防御为目的的正义安全专家）或图谋不轨的恶意黑客，为了寻找这些隐藏的漏洞，往往需要熬夜数周甚至数月，执着地翻找数百万行复杂的计算机代码。这好比是在广阔的沙滩中央，仅凭肉眼寻找一根丢失的针，是一项枯燥且痛苦的工作。

但是，如果能将这一漫长而痛苦的过程完全交给人工智能（AI）会怎样呢？如果你下令：“扫描我们所有的程序源代码，找出黑客可能潜入的所有隐蔽漏洞”，而它在几分钟内就能分毫不差地找出数百个致命漏洞，而且还是通过普通人类穷其一生也难以想象的奇思妙想和巧妙绕过方式找出来的。这并非遥不可及的科幻电影，而是正发生在我们眼前的现实。

作为 ChatGPT 最强劲的对手，拥有全球顶尖技术实力的 AI 企业 Anthropic 开发出了具备这种惊人能力的新 AI 模型。今年 4 月初，Anthropic 大张旗鼓地公开了名为“Mythos Preview”的新模型 [什么是 Anthropic 的 Claude Mythos，它带来了哪些风险？](https://www.bbc.com/news/articles/crk1py1jgzko)。

然而，他们在向市场推出这一伟大的发明时，却发表了一个非常奇怪的声明。他们宣称：“我们虽然制造出了历史上最强大、最了不起的 AI，但如果它哪怕有一丁点落入恶徒之手，破坏力都将极其巨大，因此绝对无法向公众完全公开。”

这一声明随即在 IT 业界和政界点燃了巨大争议的火种。人们开始提出根本性的疑问：我们是否应该全盘相信这些自称模型“太危险”的说法？这会不会只是为了向投资者夸耀自家 AI 多么厉害而进行的巧妙“恐惧营销”？在美国白宫最高层都亲自出面关注该模型风险的情况下，为何前线的实际安全专家们正针对 Anthropic 提高分贝，指责其为童话中的“放羊娃”（狼来了的故事）？让我们来通俗易懂地揭开真相。

## 这为什么对我们很重要？

首先需要理解的是，这一尖端技术问题为何与我们普通人看似平凡的日常生活息息相关。在现代社会，我们每天使用的智能手机、网银系统、股票交易所服务器，甚至医院的生命维持设备和国家电网，所有这些数字系统归根结底都是由名为“计算机代码”的宏大文本设计图构成的。如果这份设计图中留有微小的缺陷，黑客就能乘虚而入，窃取个人信息和资金，甚至引发社会混乱。在 IT 世界里，这些致命的缝隙被称为“安全漏洞”。

一直以来，防御和寻找这些安全漏洞被认为是少数经过高度训练的人类安全专家才能拥有的特权。然而，Anthropic 的 Mythos 彻底击碎了这一长久以来的常识。根据“红队评估（red-teams，源自军事术语，指扮演攻击者以进行极限测试的专家组）”的分析，Mythos 在“计算机安全任务中展现出了惊人的卓越能力” [什么是 Anthropic 的 Claude Mythos，它带来了哪些风险？](https://www.bbc.com/news/articles/crk1py1jgzko)。它以与人类大脑旋转速度完全不在一个量级的运算能力，无情地钻研系统的弱点。

最令人震惊的事件发生在拥有数亿用户的著名 Web 浏览器“Firefox”上。在将初期版本的 Mythos Preview 投入到 Firefox 庞大的源代码中后，它在瞬间找出了多达 271 个零日漏洞（Zero-day vulnerability） [Claude Mythos 在 Firefox 中发现了 271 个零日漏洞... - Schneier 谈安全](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html)。

这里的“零日”是指连软件制作者都不知道缺陷的存在，因此如果黑客立刻发动攻击，制作者准备防御对策的时间字面上只有“0 天”，是最致命的状态。Mozilla 基金会大为震惊，不得不匆忙在向全球发布的 Firefox 最新版本中包含了对 Mythos 发现的 271 个漏洞的修复方案 [Claude Mythos 在 Firefox 中发现了 271 个零日漏洞... - Schneier 谈安全](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html)。简单来说，这原本是数十名优秀安全专家花费数年时间夜以继日地努力才勉强可能完成的工作量，却被 AI 一举攻克，堪称奇迹 [感谢 Mythos AI，修复了 271 个 Firefox 缺陷：IT 安全的突破...](https://audiosex.pro/threads/271-firefox-flaws-closed-thanks-to-mythos-ai-breakthrough-for-it-security.84467/)。

然而，这一惊人的结果在带来欢呼的同时，也带来了令人脊背发凉的恐惧。如果这项旨在帮助人类的强大黑客技术首先落入恶意犯罪组织或敌对国家之手会怎样？电网、通信网、金融结算系统可能瞬间被攻破，所有控制权将被夺走。Anthropic 首席执行官（CEO）达里奥·阿莫迪（Dario Amodei）之所以迫切地警告说“我不希望 AI 被用来对付我们自己的人民（即被用作无情攻击我们自己的武器）”，正是因为这种破坏力 [Reddit 上的 r/Anthropic：Anthropic 主管 Dario Amodei：‘我不希望 AI 对付我们自己的人民’](https://www.reddit.com/r/Anthropic/comments/1sopno0/anthropic_chief_dario_amodei_i_dont_want_ai/)。

意识到事态严重性的美国白宫也没有袖手旁观。白宫并未将其仅仅视为一场新产品发布闹剧，而是采取了前所未有的措施，将 Mythos AI 预先整合到旨在防御国家关键基础设施的“联邦网络安全战略”中 [Reddit 上的 r/cybersecurity：白宫将 Anthropic 的 Mythos AI 整合到联邦网络安全战略中以加固关键基础设施](https://www.reddit.com/r/cybersecurity/comments/1srp248/white_house_integrating_anthropics_mythos_ai_into/)。这是国家安全层面发出的强烈信号，表明不能仅凭企业的自觉来管理这种恐怖的能力，而必须由国家直接控制和管理 [Reddit 上的 r/cybersecurity：白宫将 Anthropic 的 Mythos AI 整合到联邦网络安全战略中以加固关键基础设施](https://www.reddit.com/r/cybersecurity/comments/1srp248/white_house_integrating_anthropics_mythos_ai_into/)。

## 通俗理解：为何危险却又难以置信

为了直观了解 Mythos 有多厉害，以及为什么它会同时收获赞美与批评，我们可以做个类比。

Mythos 的能力就像是一个无敌的“超级 AI 建筑检查员”，他在短短几秒钟内就能扫视一遍世界上最宏大、最复杂的高层建筑（软件程序）的数万张难懂的设计图，然后准确指出：“那里 3 楼第 4 个窗户旁边的砖块比设计松动了 1 毫米，可能会漏雨；地下 3 楼的通风口少了一颗螺丝，小偷可以完美潜入。”

那么，既然这种 AI 如此聪明且从长远来看似乎大有裨益，为什么许多专家还要贬低和批评它呢？批评的核心在于其“验证（Verification）”与“透明度（Transparency）”的完全缺失。

打个比方。假设我们开发出了一种能征服所有癌症的划时代新药。但制药公司突然宣布：“各位，这是一种奇迹药。但如果暴露给普通人，它可能会引发极其致命的副作用，甚至毁灭世界。因此，我们只秘密供应给极少数特定的医院。虽然不能出示证据，但总之它很危险，请相信我们！”如果是你，你能心平气和地接受这种傲慢的发布吗？

理所当然地，外部独立的医疗专家必须对药物成分进行透明的分析和验证。在 AI 世界中，这种记录模型功能、局限性、运作方式以及内在风险的官方说明书被称为“系统卡（System Card）”。

然而，Anthropic 给出的 Mythos 系统卡反而留下了深深的疑虑。一位分析师通宵分析了这份容量达 23MB、长达 244 页的海量文档。令人荒唐的是，纵观整份文档，支撑他们所谓“该模型极其危险，无法向公众发布”这一宏大主张的核心内容竟然只有区区“7 页” [放羊娃 Mythos：验证缺失正在崩溃对 Anthropic 的信任 | Rick's Cafe AI](https://cafeai.home.blog/2026/04/21/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic/)。剩下的数百页全都是些混淆视听、生搬硬套的内容。

更根本的问题在于其彻底的封闭性。Anthropic 声称，为了风险管理，他们仅向极少数获得许可的合作伙伴提供极为受限的 Mythos。但外部既没有可以客观验证这一点的“公开证明体系”，也没有定期的透明度报告。甚至没有任何迹象表明有第三方审计（third-party audit）在确认究竟是谁、具备何种资格在接触这个恐怖的模型 [Reddit 上的 r/cybersecurity：放羊娃 Mythos：验证缺失正在崩溃对 Anthropic 的信任 [ Mythos 200 多页报告的真实内容 ]](https://www.reddit.com/r/cybersecurity/comments/1sst5g4/the_boy_that_cried_mythos_verification_is/)。

最终，Anthropic 的态度可以总结为：“危险程度足以毁灭世界，所以别废话，我们在密室里管得很好，大众只需要盲目相信我们公司就行了。”这种过时的方式引起了在安全领域摸爬滚打数十年的专家们的强烈批评，因为他们深知，这种从源头上拒绝外部验证的傲慢方式最终往往会输得最惨 [Reddit 上的 r/cybersecurity：放羊娃 Mythos：验证缺失正在崩溃对 Anthropic 的信任 [ Mythos 200 多页报告的真实内容 ]](https://www.reddit.com/r/cybersecurity/comments/1sst5g4/the_boy_that_cried_mythos_verification_is/)。

因此，专家们建议，与其听信那些为了吸引投资而一味进行夸大恐惧营销的供应商（卖家）之言，不如去倾听那些每天与黑客进行殊死博弈的安全从业者的客观评价 [感谢 Mythos AI，修复了 271 个 Firefox 缺陷：IT 安全的突破...](https://audiosex.pro/threads/271-firefox-flaws-closed-thanks-to-mythos-ai-breakthrough-for-it-security.84467/)。

## 现状：被攻破的无敌之盾

就在这种被指责为缺乏透明证据、刻意进行恐惧营销的舆论压力下，屋漏偏逢连夜雨，发生了一起极其致命且令人羞愧的大型事件，让人从根本上怀疑 Anthropic 实际的安全能力。

据彭博社报道，身份不明的攻击者非法访问了 Claude Mythos 的核心模型数据，并发生了夺取宝贵资产的严重泄露事故。Anthropic 不得不立即承认这一沉痛事实并展开紧急调查 [Mozilla 使用 Claude Mythos AI 预览版协助修复... | GamingOnLinux](https://www.gamingonlinux.com/2026/04/mozilla-using-claude-mythos-ai-preview-to-help-fix-major-security-issues-in-firefox/)。

而最令大众感到荒唐和不可思议的是黑客那草率的攻击手法。动用了电影《碟中谍》里那种华丽的尖端黑客技术吗？不，现实更接近于一出黑色幽默。攻击者只是窃取了安全管理松懈的外部外包公司的登录信息（账号和密码），厚颜无耻地登录后，用基础的猜测方式摸索出了 Anthropic 服务器的内部网站地址，然后便长驱直入，访问了多个“未发布的最高机密模型” [Mozilla 使用 Claude Mythos AI 预览版协助修复... | GamingOnLinux](https://www.gamingonlinux.com/2026/04/mozilla-using-claude-mythos-ai-preview-to-help-fix-major-security-issues-in-firefox/)。

我们可以给这个荒唐的局面做个形象的比喻：用世界上最坚硬的钛合金打造了一个最先进的铁制保险箱，并拿着扩音器大喊“这里面有能炸掉世界的武器，严禁靠近！”，结果保险箱的后门却敞开着，出入密码也被随手设成了谁都能猜到的“1234”。一家自称发明了世界上最顶尖智能黑客专用 AI 的公司，竟然在公司内部密码管理这种最基本的安全环节上被轻易攻破，丢尽了脸面。

理所当然地，这种言行不一的情况引发了巨大的嘲讽和激烈的反弹。人们尖锐地指出，技术卖家们虽然满口都是威胁世界的恐怖主张，但看看实际发生的黑客事件那卑微的真相，就能知道他们的傲慢不过是沙上楼阁般的虚像 [获取你的 Anthropic Mythos 纪念胸针 | flyingpenguin](https://www.flyingpenguin.com/get-your-anthropic-mythos-novelty-pin/)。

一些目光敏锐的专家更是切中要害：如果 Mythos 真如 Anthropic 所说，是比人类黑客“快数千倍的漏洞发现工具”，那么它带来的正面效果不应该是攻击速度变快导致世界毁灭，而应该是防守者修补系统漏洞的“补丁（patching）速度”大幅提升，让世界变得更安全 [放羊娃 Mythos：验证缺失正在崩溃对 Anthropic 的信任](https://www.flyingpenguin.com/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic/)。

因为在 AI 像垃圾一样倾倒出的数万个漏洞中，逐一核查哪些是真正能让系统崩溃的“真炸弹”的“验证（Verification）”工作，依然是需要高度智能的人类判断的真正瓶颈（bottleneck） [Mythos 账本，第一部分：Firefox 分水岭与新...](https://www.sakurasky.com/blog/mythos-ledger-part-1/)。也就是说，批评的核心在于 Anthropic 故意缩小了 Mythos 带来的有益防御效果，而极力夸大了刺激恐惧感的威胁。

## 未来将会如何？

随着对其创新技术的刻意夸大以及背后隐藏的松懈安全实情大白于天下，人们对曾作为创新偶像的 Anthropic 的不信任感正呈几何倍数增长。美国白宫核心 AI 顾问、硅谷颇具影响力的人物大卫·萨克斯（David Sacks）代表了业界日益冷淡的目光，他表示：“越来越多的人正合理地怀疑 Anthropic 是否是 AI 业界欺骗大众的‘放羊娃’（boy who cried wolf）” [白宫似乎突然对 Anthropic 感到非常恐惧](https://futurism.com/artificial-intelligence/white-house-terrified-anthropic-mythos/)。

当然，即便营销夸张且公司内部安全被攻破丢了脸，Mythos AI 能够一举找出 Firefox 中 271 个难攻不落的零日漏洞这一历史性成果本身是不容抹杀的。负责安全事务的白宫和政府机构为了应对可能发生的恐怖网络战争，依然没有放松极度的警惕。我们将在一段时间内每天关注 Mythos 是否真的具备国家崩溃级的能力，以及政府前所未有的防御措施是否合理 [白宫似乎突然对 Anthropic 感到非常恐惧](https://futurism.com/artificial-intelligence/white-house-terrified-anthropic-mythos/)。

在激烈的 AI 时代，真正的胜利者绝非那些侥幸握有能像暴雨般随机吐出无数漏洞的机器的人。只有那些具备敏锐验证能力，能够从无数漏洞中智能筛选出真正能破坏系统的威胁并完美证明其有效性的专业安全团队，才能成为最后的幸存者 [Mythos 账本，第一部分：Firefox 分水岭与新...](https://www.sakurasky.com/blog/mythos-ledger-part-1/)。

Anthropic 是否能反思过去的傲慢，坦然接受透明的外部审计，从而奇迹般地恢复已经崩溃的大众信任？还是会像童话中那个谎称狼来了欺骗大众的放羊娃一样，在真正恐怖的危机降临时，世界上再也没有人愿意相信他们迫切的警告，从而亲手迎来凄凉的结局？全球的目光正集中在 Anthropic 的下一步行动上。

## AI 的视角 (MindTickleBytes AI)
即便取得了足以改变世界的惊人技术成就，却因为“秘密主义导致的透明度缺失”和“基础的自身安全失败”这种荒唐错误而踢翻大众的信任，这是大型技术产业反复上演的最惨痛的矛盾。无论拥有多么压倒性的技术，如果不与大众坦诚沟通而只是制造恐惧，那么这项创新就无法获得完整的欢迎。如果 Anthropic 披着安全的幌子将技术彻底隐藏在幕后，却连自己的基本盘都守不住，这种虚伪不停止的话，大众对不可控 AI 破坏力的恐惧，将远不及对那些试图控制一切的大型企业的不负责任与傲慢的恐惧。真正的创新并非源于封闭密室里的恐惧煽动，而是在世人面前的透明证明与沟通中完成的。

## 参考资料
1. [放羊娃 Mythos：验证缺失正在崩溃对 Anthropic 的信任...](https://www.flyingpenguin.com/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic/)
2. [Claude Mythos 在 Firefox 中发现了 271 个零日漏洞... - Schneier 谈安全](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html)
3. [Mozilla 使用 Claude Mythos AI 预览版协助修复... | GamingOnLinux](https://www.gamingonlinux.com/2026/04/mozilla-using-claude-mythos-ai-preview-to-help-fix-major-security-issues-in-firefox/)
4. [Mythos 账本，第一部分：Firefox 分水岭与新...](https://www.sakurasky.com/blog/mythos-ledger-part-1/)
5. [放羊娃 Mythos - ~comp - Tildes](https://tildes.net/~comp/1u5g/the_boy_that_cried_mythos)
6. [感谢 Mythos AI，修复了 271 个 Firefox 缺陷：IT 安全的突破...](https://audiosex.pro/threads/271-firefox-flaws-closed-thanks-to-mythos-ai-breakthrough-for-it-security.84467/)
7. [什么是 Anthropic 的 Claude Mythos，它带来了哪些风险？](https://www.bbc.com/news/articles/crk1py1jgzko)
8. [Reddit 上的 r/cybersecurity：放羊娃 Mythos：验证缺失正在崩溃对 Anthropic 的信任 [ Mythos 200 多页报告的真实内容 ]](https://www.reddit.com/r/cybersecurity/comments/1sst5g4/the_boy_that_cried_mythos_verification_is/)
9. [放羊娃 Mythos：验证缺失正在崩溃对 Anthropic 的信任 | Rick's Cafe AI](https://cafeai.home.blog/2026/04/21/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic/)
10. [Reddit 上的 r/Anthropic：Anthropic 主管 Dario Amodei：‘我不希望 AI 对付我们自己的人民’](https://www.reddit.com/r/Anthropic/comments/1sopno0/anthropic_chief_dario_amodei_i_dont_want_ai/)
11. [Reddit 上的 r/cybersecurity：白宫将 Anthropic 的 Mythos AI 整合到联邦网络安全战略中以加固关键基础设施](https://www.reddit.com/r/cybersecurity/comments/1srp248/white_house_integrating_anthropics_mythos_ai_into/)
12. [获取你的 Anthropic Mythos 纪念胸针 | flyingpenguin](https://www.flyingpenguin.com/get-your-anthropic-mythos-novelty-pin/)
13. [Anthropic 将你的数据交给埃隆·马斯克 | flyingpenguin](https://www.flyingpenguin.com/anthropic-gives-your-data-to-elon-musk/)
14. [白宫似乎突然对 Anthropic 感到非常恐惧](https://futurism.com/artificial-intelligence/white-house-terrified-anthropic-mythos)