---
layout: post
title: "我的 AI 帳號被駭了嗎？Claude 代幣遭竊事件的真相"
description: "近期人工智慧服務 Claude 的使用者之間，頻傳不明原因的代幣消耗與帳號遭竊災情。我們整理了駭客竊取 AI 帳號的手法與預防方式，讓您一看就懂。"
summary: "駭客利用惡意軟體竊取 Claude 使用者的登入工作階段（Session），擅自挪用帳號的代幣配額，造成使用者嚴重損失。"
tags: [安全, Claude, AI, 資訊保護, 駭客]
image: 2026-09-12-Hackers-are-stealing-Claude-tokens-from-subscribers.jpg
image_alt: "抽象表現螢幕中的鎖頭圖示在數位資料流中遭駭的影像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "僅僅更改密碼已不足以應對當前時代。現在是時候認知到「活動工作階段（Active Session）」安全的重要性，並檢視您的瀏覽器管理習慣了。"
quiz:
  - question: "駭客竊取 Claude 帳號的主要手法為何？"
    choices: ["暴力破解強力密碼", "利用資訊竊取者（Infostealer）惡意軟體", "誘騙使用者點擊釣魚網站"]
    answer: 1
    explanation: "駭客使用資訊竊取者（Infostealer）惡意軟體，直接從使用者的電腦中竊取瀏覽器 Cookie 與登入工作階段資料。"
  - question: "駭客為何能繞過現有的二階段驗證（MFA）？"
    choices: ["AI 模型解除了驗證機制", "竊取了已登入的工作階段資訊", "解密了加密技術"]
    answer: 1
    explanation: "由於竊取的是已處於登入狀態的活動工作階段資訊，駭客利用使用者已通過驗證的狀態，無需進行額外驗證即可存取帳號。"
  - question: "Anthropic 在確認被害事實後的初步應對措施，下列何者正確？"
    choices: ["暫停服務", "強制登出帳號並刪除支付資訊", "刪除使用者帳號"]
    answer: 1
    explanation: "Anthropic 將疑似受害的帳號強制登出，刪除支付方式，並對部分使用者採取退款措施。"
lang: zh-tw
ref: 2026-09-12-Hackers-are-stealing-Claude-tokens-from-subscribers
---

想像一下：您像平常一樣忙完工作，檢查人工智慧（AI）服務「Claude」的使用量，結果被螢幕上的數字嚇了一跳。明明今天連一個問題都沒問過，但代幣配額（AI 可處理的資訊量）卻像是被人熬夜操勞了一整晚一樣大幅減少。[參考資料 4](https://theoutpost.ai/news-story/hackers-drain-claude-accounts-as-security-breach-exposes-stolen-tokens-and-session-keys-30616/) 這確實是近期許多 Claude 付費訂閱者遭遇的荒謬慘劇。

駭客的目標已不再僅限於嘗試免費使用 AI，現在更開始盯上我們昂貴的付費 AI 訂閱帳號。究竟駭客是如何竊取我們的帳號，並隨意使用我們的代幣呢？

## 這為什麼重要？

AI 技術已成為日常生活的必備夥伴。然而，帳號被駭不僅僅是「代幣被偷」這麼簡單。一旦帳號遭駭客竊取，他們會利用您的配額來執行自己的任務。[參考資料 14](https://techround.co.uk/artificial-intelligence/malware-is-now-stealing-claude-sessions-to-drain-paid-ai-usage-how-does-that-work/) 這不僅意味著您支付的費用被他人挪用，更糟的是，您帳號中產出的所有 AI 應用結果，都有可能遭他人窺視，甚至被用於非法或不正當的用途。更大的問題在於，營運商 Anthropic 至今尚未提供詳細的分析工具，讓使用者能精確追蹤自己的代幣究竟消耗在何處。[參考資料 5](https://news.ycombinator.com/item?id=49662941)

## 淺顯易懂的解釋

我們將駭客竊取帳號的手法比喻為「鑰匙」。

我們平日使用的密碼或二階段驗證（MFA，額外的安全確認程序），就像是進入家門（帳號）時使用的「鑰匙」或「電子鎖密碼」，每次進門都要確認鎖頭。然而，駭客使用的 **「資訊竊取者（Infostealer，惡意軟體）」** 則完全繞過了這道程序。

簡單來說，當我們出門時，駭客竊走了我們無意間留在門把上或是隨手放置的 **「複製出的出入證（瀏覽器 Cookie 與活動工作階段資料）」**。[參考資料 7](https://diasporadigitalmedia.com/hackers-are-stealing-claude-tokens-from-subscribers/), [參考資料 12](https://nerdstool.com/blog/hackers-are-stealing-claude-tokens-from-subscribers/) 只要擁有這張證件，駭客即便不知道密碼，也能在系統認定為「已登入」的狀態下，暢通無阻地進入我們的帳號內部。[參考資料 9](https://techmash.blog/blog/hackers-stealing-claude-subscriber-tokens) 系統會誤認為是已經過驗證的「主人」再次連線，因此不會進行任何額外的安全檢查。

## 現狀

目前許多使用者紛紛反應遭遇不明原因的代幣消耗。[參考資料 10](https://relvehq.com/blog/noise/hackers-steal-claude-tokens) 根據其中一位使用者的案例，即使沒有進行特殊業務，代幣使用量仍由 45% 急劇增加至 55%。[參考資料 1](https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/)

Anthropic 已意識到此災情，並向部分受害者發送警告郵件，但也有批評指出並非所有使用者都接獲通知。[參考資料 11](https://www.bestaitools.com/hackers-are-stealing-claude-tokens-from-paying-subscribers-and-anthropic-cant-tell-you-how-much-was-taken/) 目前公司方面採取的應對措施包括：將疑似受害的帳號強制登出、刪除已註冊的支付方式，並針對部分使用者進行退款。[參考資料 12](https://nerdstool.com/blog/hackers-are-stealing-claude-tokens-from-subscribers/) 然而，目前尚未建立出能徹底防禦這種「工作階段劫持（Session Hijacking）」攻擊的結構性工具。[參考資料 2](https://www.gadgetreview.com/hackers-are-stealing-claude-subscribers-ai-tokens)

## 未來展望

專家警告，這類駭客行動將會變得更加精細。惡意軟體會在使用者不知情的情況下滲透電腦，因此未來瀏覽器安全管理將成為個人資料保護的最前線。

提醒各位使用者，應定期檢查帳號使用量，若偵測到異常操作，應養成立即登出後重新登入的習慣。此外，透過資安軟體隨時檢查系統內是否有惡意軟體也至關重要。更進一步地說，AI 服務企業也應儘速建置完善的安全工具，讓使用者能透明地檢視代幣消耗明細，並能快速回報異常徵兆。

## 參考資料

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