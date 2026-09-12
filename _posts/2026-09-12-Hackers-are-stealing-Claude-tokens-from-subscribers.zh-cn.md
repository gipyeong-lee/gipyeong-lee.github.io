---
layout: post
title: "我的AI账户被黑了？Claude代币被盗事件的真相"
description: "近期，人工智能服务Claude的用户中接连出现原因不明的代币消耗和账户被盗事件。我们为您整理了黑客窃取AI账户的方式及防范方法。"
summary: "黑客正在利用恶意软件窃取Claude用户的登录会话，从而非法占用其账户代币额度。"
tags: [安全, Claude, AI, 信息保护, 黑客攻击]
image: 2026-09-12-Hackers-are-stealing-Claude-tokens-from-subscribers.jpg
image_alt: "抽象表现画面中的锁图标在数字数据流中被黑客攻击的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "单纯修改密码的时代已经过去了。现在是意识到活跃会话安全重要性，并检查浏览器管理习惯的时候了。"
quiz:
  - question: "黑客窃取Claude账户的主要方式是什么？"
    choices: ["穷举强密码", "利用信息窃取恶意软件(Infostealer)", "访问钓鱼邮件网站"]
    answer: 1
    explanation: "黑客使用信息窃取(Infostealer)恶意软件，从用户的电脑中直接盗取浏览器Cookie和登录会话数据。"
  - question: "为什么黑客可以绕过现有的双重认证(MFA)？"
    choices: ["AI模型使认证失效", "窃取了完整的已登录会话信息", "解密了加密技术"]
    answer: 1
    explanation: "由于窃取的是已经处于登录状态的活跃会话信息，黑客滥用了用户已完成认证的状态，无需经过额外的认证步骤即可访问账户。"
  - question: "Anthropic确认受害事实后的初步应对措施是什么？"
    choices: ["暂停服务", "强制注销并删除支付信息", "删除用户账户"]
    answer: 1
    explanation: "Anthropic正在对疑似受害的账户进行强制注销，删除其关联的支付手段，并为部分用户办理退款。"
lang: zh-cn
ref: 2026-09-12-Hackers-are-stealing-Claude-tokens-from-subscribers
---

想象一下，像往常一样结束工作后查看人工智能(AI)服务“Claude”的使用量，结果被屏幕上的数字吓了一跳。明明今天一次都没有向AI提问，但代币额度（AI可处理的信息量）却像是有谁整晚都在勤奋地让它工作一样大量减少了。[参考资料 4](https://theoutpost.ai/news-story/hackers-drain-claude-accounts-as-security-breach-exposes-stolen-tokens-and-session-keys-30616/) 事实上，这正是近期许多Claude付费订阅用户所遭遇的荒唐受害案例。

这不仅是简单的试图免费使用AI，黑客们现在已经开始将魔爪伸向我们宝贵的付费AI订阅账户了。究竟黑客是如何窃取我们的账户，并随意使用我们的代币额度的呢？

## 为什么这很重要？

AI技术现在已成为日常生活中必不可少的伴侣。但账户被黑不仅仅意味着“损失代币”。一旦黑客窃取了您的账户，他们就会利用您的额度来执行他们自己的任务。[参考资料 14](https://techround.co.uk/artificial-intelligence/malware-is-now-stealing-claude-sessions-to-drain-paid-ai-usage-how-does-that-work/) 这不仅意味着您支付的费用被用于他人的工作，还隐含着您账户中产生的所有AI使用结果都可能暴露给他人，甚至被滥用于犯罪活动的风险。更严重的问题是，运营方Anthropic目前尚未提供能够让用户详细了解其代币究竟消耗在何处的分析工具。[参考资料 5](https://news.ycombinator.com/item?id=49662941)

## 简单易懂的解释

我们将黑客窃取账户的方式比作“钥匙”吧。

我们平时使用的密码或双重认证（MFA，附加安全验证程序）就像是进家门（账户）时使用的“钥匙”或“门锁密码”。每次进入时都要确认锁是否关好。然而，黑客使用的**“信息窃取程序（Infostealer，信息窃取恶意软件）”**完全绕过了这一方式。

简单来说，黑客窃取的是我们在出门时无意中插在门上忘记拔下的**“复制版出入证（浏览器Cookie及活跃会话数据）”**。[参考资料 7](https://diasporadigitalmedia.com/hackers-are-stealing-claude-tokens-from-subscribers/), [参考资料 12](https://nerdstool.com/blog/hackers-are-stealing-claude-tokens-from-subscribers/) 只要有了这张卡，黑客即便不知道密码，也能以已经登录的状态毫无阻碍地进入您的卧室。[参考资料 9](https://techmash.blog/blog/hackers-stealing-claude-subscriber-tokens) 对系统而言，它会识别为已经完成认证的“主人”再次访问，因此不会进行额外的安全检查。

## 当前状况

目前，许多用户反映出现了原因不明的代币消耗受害情况。[参考资料 10](https://relvehq.com/blog/noise/hackers-steal-claude-tokens) 观察一位用户的案例，即使没有进行特殊工作，代币使用量也从45%急剧增加到了55%。[参考资料 1](https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/)

Anthropic方面已意识到此事，并向部分受害者发送了警示邮件，但也有批评指出并非所有用户都收到了通知。[参考资料 11](https://www.bestaitools.com/hackers-are-stealing-claude-tokens-from-paying-subscribers-and-anthropic-cant-tell-you-how-much-was-taken/) 目前，公司正在采取强制注销受害嫌疑账户、删除注册的支付手段并为部分用户办理退款等应对措施。[参考资料 12](https://nerdstool.com/blog/hackers-are-stealing-claude-tokens-from-subscribers/) 但从根本上说，能够完美防御此类“会话劫持（Session Hijacking，窃取活跃会话）”攻击的结构性工具尚未开发完成。[参考资料 2](https://www.gadgetreview.com/hackers-are-stealing-claude-subscribers-ai-tokens)

## 未来会怎样？

专家警告称，此类黑客攻击活动将会变得更加复杂。由于恶意软件会在用户不知情的情况下渗透电脑，未来浏览器安全管理将成为个人隐私保护的最前线。

建议用户定期检查自己的账户使用量，如发现可疑行为，请养成立即注销账户并重新登录的习惯。同时，通过安全软件随时检查系统内是否存在恶意软件也至关重要。此外，AI服务企业也应尽快建立安全工具，让用户能够透明地查询代币消耗明细，并能快速报告异常征兆。

## 参考资料

1. [HackersarestealingClaudetokensfromsubscribers| TechCrunch](https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/)
2. [HackersAreStealingClaudeSubscribers’ AITokens](https://www.gadgetreview.com/hackers-are-stealing-claude-subscribers-ai-tokens)
3. [AnthropicClaudeSecurity Breach:StolenTokensHit Users](https://theoutpost.ai/news-story/hackers-drain-claude-accounts-as-security-breach-exposes-stolen-tokens-and-session-keys-30616/)
4. [HackersarestealingClaudetokensfromsubscribers|HackerNews](https://news.ycombinator.com/item?id=49662941)
5. [ClaudeTokenTheft HitsSubscribersasHackersTarget Accounts...](https://www.itechpost.com/articles/237270/20260909/claude-token-theft-hits-subscribers-hackers-target-accounts-security.htm)
6. [HackersarestealingClaudetokensfromsubscribers- Diaspora...](https://diasporadigitalmedia.com/hackers-are-stealing-claude-tokens-from-subscribers/)
7. [Hackers Are Stealing Claude Subscribers’ AI Tokens](https://tech.yahoo.com/ai/claude/articles/hackers-stealing-claude-subscribers-ai-154417768.html)
8. [Hackers Are Stealing Claude Tokens From Subscribers](https://techmash.blog/blog/hackers-stealing-claude-subscriber-tokens)
9. [Hackers are stealing Claude tokens - relvehq.com](https://relvehq.com/blog/noise/hackers-steal-claude-tokens)
10. [Hackers are stealing Claude tokens from paying subscribers ...](https://www.bestaitools.com/hackers-are-stealing-claude-tokens-from-paying-subscribers-and-anthropic-cant-tell-you-how-much-was-taken/)
11. [Hackers are stealing Claude tokens from subscribers](https://nerdstool.com/blog/hackers-are-stealing-claude-tokens-from-subscribers)
12. [Hackers draining Claude tokens from subscriber accounts](https://newsgab.com/hackers-drain-claude-tokens-from-subscriber-accounts/)
13. [MalwareIsNowStealingClaudeSessions To Drain Paid... - TechRound](https://techround.co.uk/artificial-intelligence/malware-is-now-stealing-claude-sessions-to-drain-paid-ai-usage-how-does-that-work/)
14. [Newsroom \ Anthropic](https://www.anthropic.com/news)