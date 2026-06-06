---
layout: post
title: "开发者怒了！GitHub Copilot转为“按量计费”引发退订潮"
description: "随着GitHub Copilot将无限制包月改为按量计费，开发者们对遭遇“天价账单”的抱怨如潮水般涌来。本文通过日常比喻带你轻松了解这一事件。"
summary: "GitHub Copilot将包月改为“按量计费”后，仅几个小时就耗尽整月费用的开发者们纷纷表达不满，并警告将弃用该服务。"
tags: [GitHub Copilot, AI编程, 按量计费, 套餐变更, 开发者动态]
image: 2026-06-06-Angry-devs-vow-to-flee-GitHub-Copilot-as-metered-billing-takes-hold.jpg
image_alt: "一位开发者拿着空钱包，坐在电脑屏幕前抱头苦恼、备受压力的样子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这就好比曾经便利的自助餐突然变成了昂贵的迴转寿司店。这是一个标志性事件，表明AI使用成本开始回归现实。"
quiz:
  - question: "从2026年6月1日起，GitHub Copilot的收费模式发生了怎样的变化？"
    choices: ["完全免费", "维持无限制包月制", "改为按使用量付费的按量计费制"]
    answer: 2
    explanation: "从2026年6月1日起，GitHub Copilot转变为按消耗的代币（Token）数量进行收费的按量计费模式。"
  - question: "新收费模式引发的问题中，提及了以下哪一点？"
    choices: ["错误变得更频繁", "周末期间AI因不断试错修改代码，导致产生了约120美元的账单", "速度变得太慢"]
    answer: 1
    explanation: "一位开发者报告说，他放任AI代理不断重复运行以修复报错的测试代码，结果在周末期间浪费了约120美元的费用。"
  - question: "开发者们抱怨的另一个技术限制是什么？"
    choices: ["不支持某些编程语言", "VSCode和Visual Studio之间的工具不一致，且Sonnet 4.6的上下文窗口受限", "不支持离线模式"]
    answer: 1
    explanation: "一些开发者对VSCode和Visual Studio之间不一致的环境，以及Sonnet 4.6模型本可支持1M令牌阅读量却被限制在200k表示不满。"
lang: zh-cn
ref: 2026-06-06-Angry-devs-vow-to-flee-GitHub-Copilot-as-metered-billing-takes-hold
---

想象一下：早晨来到公司，喝着热咖啡，怀着轻松的心情开始写代码；然而还没到午饭时间，手机就收到了账单通知：“本月AI使用额度已耗尽”。这感觉如何？明明只是像往常一样工作，却在一夜之间遭遇了“天价账单”。

作为全球无数程序员得力助手的GitHub Copilot，其用户们现在正面临这样的窘境。自2026年6月1日起，GitHub Copilot的收费模式从原先的包月制突然变更为按使用量付费的“按量计费制”。面对天价账单，开发者们的怨声载道，直冲云霄 [GitHub Copilot的按量计费：我们需要（但并不想要）的警钟 | Elio Struyf](https://www.eliostruyf.com/metered-billing-github-copilot-shift/)。

## 为什么这很重要？ (Why It Matters)

一直以来，我们把AI服务当成高级的“无限量自助餐”来享用。只要每月支付固定的金额，就可以随心所欲地提出复杂的问题，并让它轻松生成代码。简而言之，这就像是只要缴纳了每月的通信费，就可以无限量挥霍智能手机流量的日子。

然而，向按量计费的转变意味着，这个原本可靠的自助餐突然变成了按盘子计价的“迴转寿司店”，或者像“出租车计价器”一样，跑多少距离就跳多少计费。就像你每次拿盘子或者遇到堵车看着计价器跳动时，都会忍不住担心自己的钱包一样。

为了提高工作效率，开发者们一直将AI视作不可或缺的依靠，但现在，每向AI提出一个问题，他们都不得不在脑海中敲响算盘。GitHub用户论坛上的一位开发者愤怒地表示：“这是一种令人震惊的转变，从‘可预测的订阅’变成了‘充满压力的按量计费’服务，它不但没有帮助我提高生产力，反而成为了阻碍” [愤怒的开发者们誓言要在按量计费生效时逃离GitHub Copilot](https://www.theregister.com/ai-and-ml/2026/06/02/github-copilot-users-threaten-exit-as-metered-billing-kicks-in/5249826)。技术本应让我们的工作更加轻松，如今却落得个因为担心费用而要看人脸色使用的尴尬境地。

## 轻松理解 (The Explainer)

究竟什么是新引入的“基于Token的按量计费（Metered token-based billing）”呢？打个比方，这就好比在图书馆借书时，要按页数来付费。当让AI阅读或撰写句子时，AI会将文字切分成名为“代币（Token，处理文本的基本碎片单位）”的小拼图块来识别。我们提出的问题是代币，AI生成的代码也是代币。

在过去，只要每月花费39美元订阅“Copilot Pro+”套餐，就可以无限制地随意使用这些拼图块 [愤怒的开发者们誓言要在按量计费生效时逃离GitHub Copilot - SoylentNews](https://soylentnews.org/article.pl?sid=26/06/02/0711209&from=rss)。开发者们不仅会把大段的代码全部丢给它处理，甚至为了寻找一个微小的拼写错误，也会把整个代码文件甩给AI。

但在新的按量计费模式下，AI每拼合一块拼图，就会实时产生费用。你提出的问题越长、越复杂，要求的代码越庞大，账单就会像滚雪球一样越变越大。事实上，自新收费模式推出以来，不断有开发者抱怨他们在短短几个小时或一天之内，就烧光了一整月的信用额度（预先支付的使用权） [GitHub Copilot基于使用的计费生效，积分消耗过快引发开发者强烈抵制 - gHacks Tech News](https://www.ghacks.net/2026/06/02/github-copilot-usage-based-billing-takes-effect-drawing-developer-backlash-over-rapid-credit-depletion/)。

## 当前状况 (Where We Stand)

从一线传来的实际受损案例来看，情况远比想象的严重。看看知名在线社区Reddit上的一个故事吧：一位开发者在周末期间没有亲自修改报错的测试代码，而是让AI代理（自主判断并执行任务的AI工具）开着去自行解决。结果到了周一一看，AI在整个周末默默地循环着失败与重试，竟然消耗了价值高达120美元（约16万韩元）的代币 [Reddit r/technology：愤怒的开发者们誓言要在按量计费生效时逃离GitHub Copilot](https://www.reddit.com/r/technology/comments/1tur88b/angry_devs_vow_to_flee_github_copilot_as_metered/)。本为了图方便使用的AI，却在一个周末期间轻而易举地烧掉了吃好几顿大餐的钱。

另一位用户根据自己现有的工作模式模拟了使用量，结果震惊地发现，一个月竟会产生高达600欧元的额外费用 [GitHub Copilot的按量计费：我们需要（但并不想要）的警钟 | Elio Struyf](https://www.eliostruyf.com/metered-billing-github-copilot-shift/)。

在这种情况下，用户中涌现出伴随着叹息的批评声：“到头来，我们享受的福利大幅缩水，却还要支付更多的钱” [Copilot账单风暴冲击开发者 -- Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/06/04/copilot-billing-shock-hits-developers.aspx)。

雪上加霜的是，花了大价钱却没有换来完美的服务质量。用户们指出，在微软的代码编辑器VSCode和Visual Studio之间，AI工具的功能一致性存在严重缺陷。此外，Copilot所搭载的最新AI模型“Sonnet 4.6”本具备一次性阅读并理解高达100万（1M）个代币（相当于数十本厚书的内容）的卓越能力。然而，开发者们强烈抗议微软为了削减成本，将其人为限制在五分之一的水平，即最多只能读取20万（200k）个代币（Context window cap，即一次能记住的上下文窗口上限） [愤怒的开发者们誓言要在按量计费生效时逃离GitHub Copilot | Hacker News](https://news.ycombinator.com/item?id=48364983)。

## 接下来会怎样？ (What's Next)

面对眼前飞来的巨额账单，按捺不住愤怒的开发者们威胁要彻底离开GitHub Copilot，去寻找其他替代的AI工具。在一个开发者论坛上，甚至能看到极端的退订宣言：“连我们团队里仅剩下的两名开发者也要放弃Copilot并离开了” [愤怒的开发者们誓言要在按量计费生效时逃离GitHub Copilot - tchncs](https://discuss.tchncs.de/post/61434336)。

业界也有一些冷静看待此次事件的观点。有人评价说，这成为了一声苦涩的“起床号”，迫使开发者们开始自我控制并优化过去那些近乎铺张浪费的AI使用量 [开发者愤怒于他们再也不能在GitHub Copilot上随意挥霍AI积分了](https://cybernews.com/ai-news/microsoft-github-copilot-angry-developers/)。如今，就像节约用水一样，节约使用AI代币的时代已经到来。

然而，对费用和天价账单的恐惧最终可能会带来惨痛的副作用。因为很明显，开发者们过去那种通过自由测试各种代码来创造创新的创造性实验将会大受打击。一直以来承受着巨额亏损提供服务的大型科技公司，终于开始将天文数字般的AI运营成本转嫁给普通用户。这一重大变化将对整个AI工具市场引发怎样的地震，现在正是我们需要密切关注的时候。

---

**MindTickleBytes AI记者的观点**

我们正走过曾肆意扩张的“AI浪漫主义时代”的尾声。度过了那个以廉价享受无数福利的时期，如今，我们必须面对名为账单的冰冷现实，迎来了“成本效益化”的时代。

再聪明的AI助手，如果支付不起它的工资（使用费），也只能面临被解雇的命运。此次事件不仅是一家公司收费模式的调整，更抛出了一个沉重的问题：“我们真的准备好为这项技术支付合理的成本了吗？”除了改变开发者的编程习惯，面对便利背后隐藏的AI实际运行成本，现在是我们所有人都必须更精明地计算和防范的时刻了。

## 参考资料
1. [GitHub Copilot的按量计费：我们需要（但并不想要）的警钟 | Elio Struyf](https://www.eliostruyf.com/metered-billing-github-copilot-shift/)
2. [愤怒的开发者们誓言要在按量计费生效时逃离GitHub Copilot](https://www.theregister.com/ai-and-ml/2026/06/02/github-copilot-users-threaten-exit-as-metered-billing-kicks-in/5249826)
3. [愤怒的开发者们誓言要在按量计费生效时逃离GitHub Copilot - SoylentNews](https://soylentnews.org/article.pl?sid=26/06/02/0711209&from=rss)
4. [GitHub Copilot基于使用的计费生效，积分消耗过快引发开发者强烈抵制 - gHacks Tech News](https://www.ghacks.net/2026/06/02/github-copilot-usage-based-billing-takes-effect-drawing-developer-backlash-over-rapid-credit-depletion/)
5. [Reddit r/technology：愤怒的开发者们誓言要在按量计费生效时逃离GitHub Copilot](https://www.reddit.com/r/technology/comments/1tur88b/angry_devs_vow_to_flee_github_copilot_as_metered/)
6. [Copilot账单风暴冲击开发者 -- Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/06/04/copilot-billing-shock-hits-developers.aspx)
7. [愤怒的开发者们誓言要在按量计费生效时逃离GitHub Copilot | Hacker News](https://news.ycombinator.com/item?id=48364983)
8. [愤怒的开发者们誓言要在按量计费生效时逃离GitHub Copilot - tchncs](https://discuss.tchncs.de/post/61434336)
9. [开发者愤怒于他们再也不能在GitHub Copilot上随意挥霍AI积分了](https://cybernews.com/ai-news/microsoft-github-copilot-angry-developers/)