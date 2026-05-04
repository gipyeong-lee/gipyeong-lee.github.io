---
layout: post
title: "我的项目文件名叫 'HERMES.md'？200 美元就这样蒸发了"
description: "深度解析 Anthropic AI 工具 Claude Code 中发现的荒唐计费漏洞，该漏洞导致用户被额外扣费 200 美元。"
summary: "介绍 Anthropic 的 'HERMES.md' 计费 Bug 事件：仅因一个特定文件名，月付 200 美元的订阅用户竟被额外索取 200 美元。"
tags: [Anthropic, Claude, AI漏洞, 计费错误, 开发者新闻]
image: 2026-05-04-HERMESmd-Anthropic-bug-causes-200-extra-charge-refuses-refund.jpg
image_alt: "电脑屏幕上显示红色警告文字，周围散落着美元符号的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "虽然 AI 代劳的时代已经到来，但其背后的计费体系依然像个“黑盒”。这次事件是一个深刻的教训，表明企业级 AI 工具的可靠性不仅取决于技术实力，更取决于运营的透明度。"
quiz:
  - question: "触发此次 Anthropic 计费漏洞的特定字符串是什么？"
    choices: ["CLAUDE.md", "HERMES.md", "ANTHROPIC.txt"]
    answer: 1
    explanation: "当 Git 记录中包含区分大小写的特定字符串 'HERMES.md' 时，就会触发该漏洞。"
  - question: "此次漏洞给用户造成的经济损失约为多少？"
    choices: ["50 美元", "100 美元", "200 美元"]
    answer: 2
    explanation: "受害者在固定订阅费之外，被额外收取了约 200 美元（约合 27 万韩元）至 200.98 美元的费用。"
  - question: "为什么一个文件名会导致计费方式发生变化？"
    choices: ["AI 误将该文件视作付费功能", "Git 记录在传递给 AI 的过程中触发了安全系统的错误响应", "用户偷偷使用了付费模型"]
    answer: 1
    explanation: "因为 Claude Code 在将最近的工作记录传递给 AI 时，Anthropic 的反滥用系统识别到了包含的字符串，从而强制更改了计费路径。"
lang: zh-cn
ref: 2026-05-04-HERMESmd-Anthropic-bug-causes-200-extra-charge-refuses-refund
---

一个平静的周六早晨，一位正边喝咖啡边潜心编程的开发者被手机的震动声打断。屏幕上赫然出现一条信用卡扣款通知。但金额却十分诡异。尽管他已经是每月支付 200 美元（约合 27 万韩元）的“VIP 无限制套餐”用户，却突然收到了额外扣费 200.98 美元的短信。[来源 3](https://www.mindstudio.ai/blog/hermes-md-bug-claude-max-billing-subscription-pricing)

罪魁祸首正是他深信疑的 AI 助手——Anthropic 的“Claude Code”。更荒唐的是这笔巨额额外费用的“罪名”。既不是因为他过度使用服务，也不是因为他偷偷订阅了其他付费功能。仅仅是因为他的项目记录中出现了 **“HERMES.md”** 这样一个简短的文件名，AI 就擅自掏空了他的钱包。[来源 2](https://byteiota.com/anthropics-hermes-md-billing-bug-200-overcharge-refund-denied/) 今天，MindTickleBytes 将为您揭秘 AI 历史上最荒诞、最令人毛骨悚然的“计费漏洞”事件。

## 这为什么很重要？

想象一下：你请 AI 帮你在电脑上清理文件，AI 在清理过程中看到桌上贴着一张“蓝色便签”，便突然宣布：“这是特殊废弃物，需额外支付 300 美元”，随后直接刷了你的卡。

我们现在正处于 AI 不仅仅是回答问题，而是直接读取电脑文件并修改代码的“智能体（Agent）”时代。但这次事件生动地展示了当我们赋予 AI 过多权限，且运营该 AI 的企业系统并不完美时，可能会发生怎样的“财务恐怖袭击”。

特别是，由于用户难以控制的过去“记录”而产生计费，以及企业在初期应对中拒绝退款的事实，这些都严重动摇了用户对 AI 服务的信任。[来源 6](https://kruxor.com/view/hnews/IjGK8/hermesmd-anthropic-bug-causes-200-extra-charge-refuses-refund/)

## 通俗易懂的理解：无视“VIP 通道”的死板保安

为了让大家更轻松地理解这次事件，我们来打个比方：

> 假设你是一家“无限续杯 VIP 咖啡馆”的会员，每月支付 1000 元即可随心畅饮。但有一天你走进店里时，包上别着一个写有“HERMES”的小徽章。
> 
> 门口的保安看到后突然大喊：“嘿！那个徽章是禁用标志！从现在起你的 VIP 优惠取消，喝每一杯水都要按原价付钱！”你抗议说：“我不是已经付过钱了吗？”但保安强行夺走你的卡，瞬间刷掉了几千元。事后你找老板理论，老板却回答：“我们的保安系统就是这么设计的，所以不能退钱。”这就是目前的荒唐现状。

在这个比喻中，“HERMES 徽章”就是字符串 **“HERMES.md”**，而“保安”则是 Anthropic 的 **反滥用系统 (Anti-abuse system)**。[来源 13](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing)

### 为什么会发生这种事？ (深度解析)

从技术角度看，这个 Bug 源于 Claude Code 的“过度执法”。以下是连锁反应的触发过程：

1.  **读取工作日志**：开发者在写代码时会留下记录，这被称为“提交信息（Commit Message）”。为了更聪明地工作，Claude Code 会读取包含这些最近记录的 **Git（一种工作日志）**。[来源 5](https://github.com/anthropics/claude-code/issues/53262)
2.  **请求中包含记录**：Claude Code 在将收集到的 Git 记录发送到 Anthropic 总部服务器时，会将这些记录完整地放入 **系统提示词（System Prompt，传递给 AI 的背景指令）** 中。[来源 10](https://vc.ru/ai/2897200-bag-v-claude-code-privel-k-spisaniyu-sredstv-iz-za-hermes-md)
3.  **误报的检查站**：Anthropic 的安全系统一旦在请求中发现“HERMES.md”字样，就会立即拉响警报。这可能是因为该单词被识别为危险词汇或需要特殊处理的敏感词。[来源 13](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing)
4.  **强制更改结算路径**：安全系统无视了该用户已订购每月 200 美元无限套餐的事实，将所有请求强制转向“额外用量（Extra Usage）”计费通道。这就像是对拥有无限通行证的人说：“你是危险分子，从现在起喝每杯水都要单独交钱。”[来源 5](https://github.com/anthropics/claude-code/issues/53262), [来源 8](https://codegurus.eu/hermes-md-anthropic-bug-causes-200-extra-charge-refuses-refund/)

令人惊讶的是，这个“保安”非常挑剔。如果不是大写的“HERMES.md”，而是小写的“hermes.md”或是后缀不同的“HERMES.txt”，都不会触发问题。唯独这个大小写完全一致的名字充当了“炸弹开关”。[来源 10](https://vc.ru/ai/2897200-bag-v-claude-code-privel-k-spisaniyu-sredstv-iz-za-hermes-md)

## 现状：如同晴天霹雳的“无法退款”

由于这个荒唐的漏洞，许多开发者一夜之间被额外收取了超过 200 美元（约合 10 只炸鸡的价格）的费用。[来源 1](https://thecodersblog.com/hermes-md-anthropic-s-billing-bug-refused-refunds-and-the-cost-of-trust-2026), [来源 14](https://news.linxi.com.au/news/billing-anomaly-in-claude-code-linked-to-specific-string-in-git-history) 一位用户甚至经历了在周六短短一天内 200 美元就人间蒸发的恐惧。[来源 16](https://www.linkedin.com/posts/ravicaw_anthropic-is-reading-your-git-commits-to-activity-7454041190104006656-m04B)

受害者立即联系了 Anthropic 的客户支持团队，但得到的回复却令人大跌眼镜。Anthropic 最初只是机械地重复回答：“无法为您办理退款 (unable to issue refund)”。[来源 7](https://inshorts.com/en/news/anthropic-s-claude-code-charges-users-extra-due-to-hidden-bug--initially-refuses-refund-1777276172440), [来源 15](https://www.hotmolts.com/post/anthropic-refuses-refund-for-its-own-billing-bug-u-2aa5714c-ae65-4b25-b5be-eafbc54a6a9e)

一位受害开发者在在线社区愤愤不平地表示：“明明不是我的错，而是公司方的 Bug 导致我平白损失了 200 美元，这合理吗？”[来源 12](https://news.ycombinator.com/item?id=47952722) 目前，这个问题在 Anthropic 的 GitHub 仓库中已获得了超过 11 万次关注，引发了全球开发者的公愤。[来源 8](https://codegurus.eu/hermes-md-anthropic-bug-causes-200-extra-charge-refuses-refund/)

## 未来会如何发展？

这次“HERMES.md”事件不仅仅是一个简单的软件错误，它向生活在 AI 时代的我们提出了三个重要问题。

首先是 **AI 企业的责任感**。如果由于自身算法错误导致用户遭受金钱损失，企业应积极提供救济方案，而不是推脱“不符合规定”。初期应对的不成熟给品牌留下了难以磨灭的污点。[来源 7](https://inshorts.com/en/news/anthropic-s-claude-code-charges-users-extra-due-to-hidden-bug--initially-refuses-refund-1777276172440)

其次是 **数据透明度**。AI 竟然在“偷偷”读取用户甚至没有直接展示给它的过去工作记录，这让许多用户感到不适。[来源 16](https://www.linkedin.com/posts/ravicaw_anthropic-is-reading-your-git-commits-to-activity-7454041190104006656-m04B) 未来，我们需要更加仔细地考量“我的数据中有多少正被移交给 AI”。[来源 9](https://sesamedisk.com/anthropic-claude-code-billing-bug-security/)

第三是 **完善安全机制的必要性**。专家指出，只要在发布前经过合理的测试，这种级别的漏洞完全是可以避免的。[来源 13](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing) 随着 AI 拥有越来越强大的权限，制衡它的系统也必须随之变得更加精密。

你的项目中是否也隐藏着 AI 可能会讨厌的文件名呢？或许在未来，我们在让 AI 工作之前，得先检查一下自己的钱包厚度。

---

### AI 视角
**MindTickleBytes AI 记者点评**
这次事件表明，AI 已经从单纯的“聊天对象”进入到直接影响我们“资产”的阶段。企业不应仅仅热衷于开发高性能 AI 模型，更应首先建立能够保护用户信用卡的精密计费安全机制。毕竟，与技术进步同等重要的，是对使用技术的人的尊重。

---

## 参考资料
1. [Anthropic's $200 Bug: When AI API Errors Cost You, and ...](https://thecodersblog.com/hermes-md-anthropic-s-billing-bug-refused-refunds-and-the-cost-of-trust-2026)
2. [Anthropic’s HERMES.md Billing Bug: $200 Overcharge, Refund ...](https://byteiota.com/anthropics-hermes-md-billing-bug-200-overcharge-refund-denied/)
3. [The Hermes.md Bug That Charged Claude Max Users $200 Extra ...](https://www.mindstudio.ai/blog/hermes-md-bug-claude-max-billing-subscription-pricing)
4. [Claude Code HERMES.md Billing Bug: $200 Credit Drain Analysis](https://aitoolly.com/ai-news/article/2026-04-30-claude-code-bug-hermesmd-in-commit-messages-triggers-unexpected-extra-usage-billing)
5. [HERMES.md in git commit messages causes requests to route to ...](https://github.com/anthropics/claude-code/issues/53262)
6. [HERMES.md: Anthropic bug causes $200 extra charge, refuses ...](https://kruxor.com/view/hnews/IjGK8/hermesmd-anthropic-bug-causes-200-extra-charge-refuses-refund/)
7. [Anthropic's Claude Code charges users extra due to hidden bug ...](https://inshorts.com/en/news/anthropic-s-claude-code-charges-users-extra-due-to-hidden-bug--initially-refuses-refund-1777276172440)
8. [HERMES.md:Anthropicbugcauses$200extracharge,refuses...](https://codegurus.eu/hermes-md-anthropic-bug-causes-200-extra-charge-refuses-refund/)
9. [Billing Security Risks inAnthropic’s Claude Code - Sesame Disk](https://sesamedisk.com/anthropic-claude-code-billing-bug-security/)
10. [Anthropicсписала $200сверх тарифа Max 20x из-заHERMES.md...](https://vc.ru/ai/2897200-bag-v-claude-code-privel-k-spisaniyu-sredstv-iz-za-hermes-md)
12. [HERMES.mdin commit messagescausesrequests to route toextra...](https://news.ycombinator.com/item?id=47952722)
13. [TheHERMES.mdBug: How a String in Git Commits... | TechPlanet](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing)
14. [Anthropic Claude Code billing bug linked to HERMES.md git ...](https://news.linxi.com.au/news/billing-anomaly-in-claude-code-linked-to-specific-string-in-git-history)
15. [Anthropic refuses refund for its own billing bug: 'unable to ...](https://www.hotmolts.com/post/anthropic-refuses-refund-for-its-own-billing-bug-u-2aa5714c-ae65-4b25-b5be-eafbc54a6a9e)
16. [Anthropic bills based on git commits with Hermes - LinkedIn](https://www.linkedin.com/posts/ravicaw_anthropic-is-reading-your-git-commits-to-activity-7454041190104006656-m04B)