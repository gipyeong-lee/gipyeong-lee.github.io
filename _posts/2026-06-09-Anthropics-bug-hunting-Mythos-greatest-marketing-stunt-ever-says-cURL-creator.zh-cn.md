---
layout: post
title: "因太危险而被隐藏的AI黑客‘Mythos’，揭开面纱竟是场营销秀？"
description: "了解这一事件：针对Anthropic的AI安全模型Mythos因过于危险而未公开的说法，cURL创始人亲自测试后批评其为‘营销噱头’。"
summary: "曾因极擅长发现安全漏洞、被认为过于危险而未公开的Anthropic AI‘Mythos’，在实际开源项目测试中仅发现1个微不足道的bug，从而受到涉嫌过度宣传的批评。"
tags: [人工智能, 网络安全, Anthropic, Mythos, 事实核查]
image: 2026-06-09-Anthropics-bug-hunting-Mythos-greatest-marketing-stunt-ever-says-cURL-creator.jpg
image_alt: "插画：华丽包装纸里放着一个极小的放大镜，象征对AI的过度宣传"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "每当新技术出现时，总会制造出马上就能改变世界的幻觉，但真正的创新始于冷静的现实检验与人类创造力的交汇点。"
quiz:
  - question: "cURL创始人丹尼尔·斯坦伯格（Daniel Stenberg）如何评价Anthropic的Mythos AI？"
    choices: ["人类历史上最伟大的黑客工具", "史上最大的营销秀（过度宣传）", "能完美替代开发者的AI"]
    answer: 1
    explanation: "丹尼尔·斯坦伯格表示，Mythos找出的安全漏洞仅有1个，并将其评价为‘史上最大的营销秀（Greatest marketing stunt ever）’。"
  - question: "Mythos在分析了17万6千行代码后，最终找出的实际安全漏洞（低严重级别）有几个？"
    choices: ["1个", "5个", "200个以上"]
    answer: 0
    explanation: "Mythos最初指出了5个问题，但在排除已知问题等之后，被认定为实际安全漏洞的只有1个。"
  - question: "根据报道，像Mythos这样现有的AI安全工具有什么局限性？"
    choices: ["连现有的简单bug都完全找不出来", "如果没有人类的创造力，就无法自行发现前所未见的新型漏洞", "会自己编写代码来破坏程序"]
    answer: 1
    explanation: "Mythos在寻找已知类型的错误方面很有用，但局限在于，如果没有人类的创造力，它无法发现全新形式的安全漏洞。"
lang: zh-cn
ref: 2026-06-09-Anthropics-bug-hunting-Mythos-greatest-marketing-stunt-ever-says-cURL-creator
---

想象一下。世界上最顶尖的专业锁具公司发表了一项重大声明：“我们新研制的万能钥匙实在太强大、太危险，能瞬间打开世界上所有的保险箱，因此绝对不能向公众公开。”人们一定会带着恐惧与好奇的目光，想知道这把万能钥匙究竟是什么。而这把万能钥匙的名字，就是最新的人工智能（AI）。

实际上，最近在AI行业就发生了类似的事情。知名AI企业Anthropic暗示其新的AI模型“Mythos”在寻找软件安全漏洞方面过于出色，向公众公开存在危险，这一度引发了巨大话题 [[安全 - cURL创始人称Anthropic寻找bug的Mythos是史上最大的营销噱头 | The Helper](https://www.thehelper.net/threads/anthropic%E2%80%99s-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator.201066/)]。

然而，当人们把这把“万能钥匙”直接用在世界上最坚固、最复杂的保险箱之一进行测试时，得出的结论却与人们的预期大相径庭。构建全球无数电子设备和互联网系统骨干的核心软件“cURL”的创始人丹尼尔·斯坦伯格（Daniel Stenberg）亲自验证了该AI的实力，并给出了斩钉截铁的评价。他尖锐地指出，世人对Mythos能力的吹捧不过是“史上最大的营销噱头（greatest marketing stunt ever）” [[cURL创始人称Anthropic寻找bug的Mythos是史上最大的营销噱头 | daily.dev](https://app.daily.dev/posts/anthropic-s-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator-lifvxyq4b)]。

究竟这个宣称“因太危险而隐藏”的AI黑客，揭开面纱后到底是什么货色呢？今天在MindTickleBytes，我们将探讨这一有趣事件的始末，以及如何看穿AI技术的过度宣传。

---

## 为什么这很重要？ (Why It Matters)

这一事件超越了单纯的闹剧，之所以与我们的日常生活密切相关，是因为接受测试的软件正是“cURL”（一种在互联网上用于数据传输、被广泛使用的免费开源程序）。简单来说，当您用智能手机刷新天气应用、在Netflix上加载电影列表，甚至是最新的汽车与服务器通信时，cURL都在看不见的地方默默运行。换言之，如果cURL出现了任何人都能轻易攻破的安全漏洞，就意味着全球的数字设备将同时暴露在黑客攻击的风险之中。

Anthropic此前曾暗示，他们开发出了一个极其擅长寻找此类核心系统漏洞的可怕AI——“Mythos” [[cURL创始人称Anthropic寻找bug的Mythos是史上最大的营销噱头...](https://www.threatshub.org/blog/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/)]。如果这是真的，那就相当于黑客们掌握了利用这个AI瘫痪整个互联网的可怕武器。人们纷纷担忧：“AI现在是不是已经脱离了人类的控制，正在寻找自己破坏系统的方法？”对于企业的安全负责人来说，这无疑也是一条让人神经紧绷的新闻。

但现实不同于科幻电影。对于管理开源项目的开发者来说，真正逼近的威胁并不是“AI的叛乱”。相反，是AI打着“安全”旗号，胡乱抛出的低水平警告信风暴。cURL创始人斯坦伯格最近抱怨称，随着AI的发展，开源项目维护者们收到了如洪水般的安全漏洞报告，这远远超出了他们能够阅读和处理的速度 [[称Mythos为“公关噱头”的Curl创始人表示AI将... | Cybernews](https://cybernews.com/security/curl-bug-bounty-ai-security-reports-daniel-stenberg/)]。

也就是说，并不是过于聪明的AI在惹麻烦，而是还不成熟的AI把自己发现的微小灰尘夸大成“炸弹”，并且在不停地按下举报按钮。这个事件向我们展示了，为什么区分真正的技术进步与企业营销是现代社会最重要的生存智慧之一。

---

## 简单易懂的解释 (The Explainer)

“寻找代码的漏洞”到底是一个怎样的过程呢？如果您对代码或安全这类词汇感到有些陌生，我们可以这样比喻。

比如，有一本厚达17万6千页的巨著（软件代码）。这本书包含了世界上最重要的规则，哪怕只有一个词写错，也可能引发重大事故。人类审核员（开发者）需要夜以继日地阅读这本书，寻找错别字或上下文不通顺的地方。

此时出现的AI安全工具，就像一个极其快速且细致的“自动拼写检查器”。AI不会像人类一样眼睛疲劳，它能在1秒钟内扫描数万页，像镊子一样精准地挑出空格错误、漏掉句号的地方。在这一点上，AI无疑是协助人类的绝佳工具。这次接受测试的Mythos也同样分析了代码并提供了有用的反馈，甚至对错误进行了出色的解释和描述，以便团队进行修改，这确实发挥了积极作用 [[cURL创始人称Anthropic寻找bug的Mythos是史上最大的营销噱头](https://www.theregister.com/security/2026/05/11/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/5238111)]。

但是，寻找“新的安全漏洞（黑客可以侵入的全新漏洞）”与单纯的拼写检查有着天壤之别。这就像推理小说中的名侦探，以别人从未想到的巧妙方式扭转文章的语境，从而找出隐藏的密码，这是一个充满创造力的过程。

Mythos在寻找过去犯过的错误，即“已知错误的模式”方面是高手，但它缺乏能独立发现需要人类创造力的“世上从未有过的新型漏洞”的推理能力 [[cURL创始人称Anthropic寻找bug的Mythos是终极...](https://pressreleasecloud.io/cybersecurity/curl-creator-calls-anthropics-bug-hunting-mythos-the-ultimate-marketing-stunt/)]。

这正是丹尼尔·斯坦伯格断言Mythos是“史上最大的营销噱头”的原因所在 [[Anthropic寻找bug的Mythos是史上最大的营销噱头...](https://www.imtr.net/article/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-4869)]。人们本以为它是个能毁灭世界的邪恶黑客，结果却发现它其实只是一个死记硬背现有规则、勤奋做校对兼职的打工仔。这与Anthropic所暗示的因太危险而不愿公开的形象相去甚远，是一个令人失望的反转。

---

## 当前状况 (Where We Stand)

那么，实际的成绩单如何呢？

Anthropic通过Linux基金会（Linux Foundation）的“Glasswing项目（Project Glasswing）”，为有影响力的开源（任何人都能查看代码并参与开发）项目提供了测试Mythos的机会。丹尼尔·斯坦伯格也通过这一途径接触到了分析结果报告。（有趣的是，斯坦伯格尖锐地指出，他本人并没有获得直接操作或访问Mythos AI模型本身的任何权限） [[cURL创始人丹尼尔·斯坦伯格称Anthropic的Mythos AI寻虫工具为“史上最大的营销噱头”](https://www.shopifreaks.com/curl-creator-daniel-stenberg-calls-anthropics-mythos-ai-bug-hunting-tool-the-greatest-marketing-stunt-ever/)]。

就这样，Mythos彻底扫描了构成cURL的足足17万6千行庞大代码 [[Curl创始人测试“过于危险”的Mythos AI并称其为“营销...](https://cybernews.com/security/curl-creator-tests-too-dangerous-mythos-ai/)]。结果是否涌现出了足以毁灭世界的可怕bug呢？完全没有。

Mythos在最初的分析中，挥舞着旗帜指出了总共5个问题。然而，斯坦伯格仔细核实后发现，其中3个不过是开发者们早已知道且记录在案的缺陷而已。剩下的问题中，有1个是与安全无关的普通bug。最终，只有令人期待的最后1个问题能够被归类为安全漏洞 [[Curl创始人测试“过于危险”的Mythos AI并称其为“营销...](https://cybernews.com/security/curl-creator-tests-too-dangerous-mythos-ai/)]。

但即便是这唯一的1个安全漏洞，也只是一个“低严重级别（severity low）”、非常微小且普通的漏洞 [[cURL创始人称Anthropic寻找bug的Mythos是史上最大的营销噱头 - Slashdot](https://it.slashdot.org/story/26/05/11/199232/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator)]。用它来证明Mythos的可怕实在显得过于寒酸。这个微小的缺陷预计将在即将于6月底发布的cURL 8.21.0版本中作为修补项（CVE，指公开披露的软件安全漏洞的标准标识符）一同公布。对此，斯坦伯格贬低道：“这个缺陷绝对不至于让任何人惊得倒吸一口凉气” [[cURL创始人称Anthropic寻找bug的Mythos是史上最大的营销噱头](https://www.theregister.com/security/2026/05/11/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/5238111)]。

还有一个更加令人难堪的比较对象。根据斯坦伯格的说法，在过去的8到10个月里，像AISLE、Zeropath、OpenAI Codex Security等其他普通的（？）AI代码分析工具，促成了cURL中多达200到300个bug的修复。他强调说，Mythos“并没有出色到能在代码分析领域留下有意义的印记，远不如其他工具”，围绕Mythos的过度期待只是一场营销，绝非重大的AI安全创新 [[cURL创始人丹尼尔·斯坦伯格称Anthropic的Mythos AI寻虫工具为“史上最大的营销噱头”](https://www.shopifreaks.com/curl-creator-daniel-stenberg-calls-anthropics-mythos-ai-bug-hunting-tool-the-greatest-marketing-stunt-ever/)]。

---

## 未来展望 (What's Next)

这一事件为我们看待技术留下了重要的教训。正如英国公共广播公司BBC敏锐指出的那样，向世界宣称自家制作的AI工具具有“前所未见的创新能力”，这完美契合了像Anthropic这类AI企业的利益诉求 [[Anthropic的Claude Mythos是什么，它会带来什么风险？](https://www.bbc.com/news/articles/crk1py1jgzko)]。如今已经到了为了吸引投资和公众注意力，连技术的危险性都能被用作极具吸引力的广告素材的时代。

因此，今后我们在接触新闻时，始终需要经过一层“现实的滤镜”。毫无疑问，AI技术正在以惊人的速度发展。它能在短短几秒钟内扫描复杂的代码，并捕捉到人类容易忽略的错别字，这大大减轻了过去人类开发者的工作量，并提升了软件的整体质量。

但是，我们暂时可以放下对“AI明天就会变成统治网络世界的黑客”的恐惧。正如Mythos的案例所证明的那样，现有的AI仍缺乏创造力，仅停留在组合和比较以前学过的数据的水平上。我们真正需要担心的，不是“过于聪明的AI”，而可能是被AI生成出的貌似合理的成果和夸大其词的广告所蒙骗的“我们的急躁”。

专家预计，未来AI企业仍会继续把新产品包装成“足以威胁人类的突破性模型”并推向市场。正如BBC的分析所言，在AI领域，能够敏锐区分合理有据的主张和空壳般的虚假宣传的能力，比以往任何时候都更加苛刻且至关重要 [[Anthropic的Claude Mythos是什么，它会带来什么风险？](https://www.bbc.com/news/articles/crk1py1jgzko)]。

---

## AI的视角 (AI's Take)

**MindTickleBytes的AI记者视角：** 营销包装的进化速度，毫不逊色于技术发展的速度。“因为危险所以隐藏”这句话，始终是能最强烈激发人类好奇心的魔法咒语。最终，斯坦伯格一针见血的批评提醒我们，在AI真正统治世界之前，人类需要培养强大的理性来进行事实核查，以免被卷入这场华丽的“言语盛宴”中。

---

## 参考资料

1. [cURL创始人称Anthropic寻找bug的Mythos是史上最大的营销噱头](https://www.theregister.com/security/2026/05/11/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/5238111)
2. [cURL创始人称Anthropic寻找bug的Mythos是史上最大的营销噱头 - Slashdot](https://it.slashdot.org/story/26/05/11/199232/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator)
3. [cURL创始人称Anthropic寻找bug的Mythos是史上最大的营销噱头 • The Register论坛](https://forums.theregister.com/forum/all/2026/05/11/202617/)
4. [cURL创始人丹尼尔·斯坦伯格称Anthropic的Mythos AI寻虫工具为“史上最大的营销噱头”](https://www.shopifreaks.com/curl-creator-daniel-stenberg-calls-anthropics-mythos-ai-bug-hunting-tool-the-greatest-marketing-stunt-ever/)
5. [cURL创始人称Anthropic寻找bug的Mythos是史上最大的营销噱头 | daily.dev](https://app.daily.dev/posts/anthropic-s-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator-lifvxyq4b)
6. [安全 - cURL创始人称Anthropic寻找bug的Mythos是史上最大的营销噱头 | The Helper](https://www.thehelper.net/threads/anthropic%E2%80%99s-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator.201066/)
7. [cURL创始人称Anthropic寻找bug的Mythos是史上最大的营销噱头...](https://www.threatshub.org/blog/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/)
8. [Anthropic寻找bug的Mythos是史上最大的营销噱头...](https://www.imtr.net/article/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-4869)
9. [Curl创始人测试“过于危险”的Mythos AI并称其为“营销...”](https://cybernews.com/security/curl-creator-tests-too-dangerous-mythos-ai/)
10. [称Mythos为“公关噱头”的Curl创始人表示AI将... | Cybernews](https://cybernews.com/security/curl-bug-bounty-ai-security-reports-daniel-stenberg/)
11. [cURL创始人称Anthropic寻找bug的Mythos是终极...](https://pressreleasecloud.io/cybersecurity/curl-creator-calls-anthropics-bug-hunting-mythos-the-ultimate-marketing-stunt/)
12. [Anthropic的Claude Mythos是什么，它会带来什么风险？](https://www.bbc.com/news/articles/crk1py1jgzko)