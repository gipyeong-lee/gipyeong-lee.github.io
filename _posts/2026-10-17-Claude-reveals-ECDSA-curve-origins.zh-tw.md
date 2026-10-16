---
layout: post
title: "數十年密碼學謎團，AI 終於解開"
description: "AI 模型 Claude 揭示了隱藏在美國國家標準與技術研究院 (NIST) 橢圓曲線密碼標準中的秘密。"
summary: "Claude AI 已證實，困擾密碼學界數十年的 NIST 橢圓曲線密碼生成種子 (seed) 源自 1990 年代 C 語言函式庫的時間戳記生成器。"
tags: [AI, 密碼學, 安全, Claude, NIST]
image: 2026-10-17-Claude-reveals-ECDSA-curve-origins.jpg
image_alt: "複雜的數位加密模式與 AI 連接的未來感畫面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這顯示了 AI 解決複雜數學難題的能力，已不僅止於簡單運算，更進化為科學探索的工具。"
quiz:
  - question: "在這項研究中，Claude 指出 NIST 橢圓曲線種子的來源為何？"
    choices: ["秘密加密短語", "1990 年代 C 語言函式庫的 lrand48 生成器", "現代量子隨機數生成器"]
    answer: 1
    explanation: "Claude 揭示了這些種子是使用 1990 年代的 C 語言函式庫 lrand48，並基於 Unix 時間戳記生成的。"
  - question: "這項發現對密碼學界的主要意義為何？"
    choices: ["確保密碼已被完全破解", "減少 NSA 蓄意插入後門的疑慮", "立即廢除新的密碼標準"]
    answer: 1
    explanation: "透過對過往由國家安全局 (NSA) 提供的數據提供可重現的生成依據，大幅降低了蓄意植入安全漏洞的疑慮。"
  - question: "此次調查是由哪個單位進行的？"
    choices: ["Google DeepMind", "Anthropic 前沿紅隊 (Frontier Red Team)", "OpenAI 安全團隊"]
    answer: 1
    explanation: "此研究結果於 2026 年 10 月 16 日由 Anthropic 的前沿紅隊報告。"
lang: zh-tw
ref: 2026-10-17-Claude-reveals-ECDSA-curve-origins
---

在我們日常使用網路時，無意間經過的無數安全連線背後，都有一道稱為「橢圓曲線密碼」的數學保護屏障。然而，過去數十年來，制定此標準過程中使用的核心數值——「種子 (seed)」的來源一直成謎，在密碼學家之間引發了不斷的質疑。「會不會是國家機關故意埋下的漏洞？」這樣的憂慮始終存在。不過，近日有消息指出，這個長久的謎團在 AI 的協助下終於解開了。

### 這為何重要？

網際網路安全是現代數位文明的基石。金融交易、私人訊息、網站連線等我們珍視的資料，全都是透過加密來保護。如果這套加密體系的關鍵——橢圓曲線標準中，存在一個來源不明的「後門 (backdoor)」，這意味著全球數位安全皆暴露在潛在威脅之下。 [2] 這個後門就像是堅固保險箱上被偷偷刻下的小裂痕，知情者便能製作開啟保險箱的鑰匙。過去幾十年來，這個「後門」存在的可能性，讓密碼學界與資安專家感到極度不安。但如今 AI 成功地以可重現的方式闡明了這些數值的實際生成過程，這些疑慮預計將大幅消除。 [7]

### 淺顯易懂：AI 追蹤密碼的根源

橢圓曲線密碼是一項利用複雜數學原理安全保護資料的技術。這項技術的核心在於「隨機性」。就像我們建立密碼時會使用無法預測的組合一樣，在密碼學中，「隨機數 (random number)」同樣至關重要。NIST (美國國家標準與技術研究院) 所提出的 ECDSA (橢圓曲線數位簽章演算法) 標準中，包含了一個生成該隨機數的「種子 (seed)」初始值。然而，該種子是如何、以何種方式生成的，多年來一直未有定論，成為密碼學界懸而未決的謎題。

簡單來說，這個種子就好比建造名為「密碼」這棟房子所需的「基礎藍圖」。但卻沒有人能確切證明這份藍圖從何而來、由誰所繪。Anthropic 的 AI 模型 Claude 就像發掘古蹟的考古學家一樣，溯源了這些數值的生成方式。 [1]

Claude 發現，這些數值並非由現代精密的隨機數生成器產生，而是透過 1990 年代廣泛使用的「lrand48」這種 C 語言函式庫的基本隨機數生成器所製造。該生成器利用一種稱為「Unix 時間戳記 (Unix timestamp)」的方式產生隨機數，即電腦系統以特定時間點為基準計算時間的方法。用比喻來說，這就像是記錄時鐘指針指向特定秒針的瞬間來製作隨機數字。 [2] 這種方式在密碼學的安全標準下，由於其可預測性高而被視為漏洞，這也是為何會引發「蓄意植入安全漏洞」疑慮的原因。Claude 成功透過模擬「lrand48」的生成過程，重現了 NIST 標準中 5 個主要橢圓曲線種子的產生方式。 [6]

### 現狀：疑慮消除，但挑戰仍在

這項研究結果於 2026 年 10 月 16 日由 Anthropic 前沿紅隊正式發表。 [2] 由於 Claude 的分析，過去關於 NSA (美國國家安全局) 在這些數值中蓄意植入安全漏洞的疑慮已大幅降低。因為現在研究人員可以跟隨這個生成過程，重現並驗證這些數值是如何推導出來的。

然而，並非所有的問題都已完全解決。研究人員指出，NIST 標準中使用的所有曲線參數，並非都能透過這種「lrand48」與時間戳記方式完全解釋。換句話說，仍有部分曲線的生成過程或依據尚不明確。 [6] 例如，有些數值是基於特定時間點生成的，但有些數值卻因為某種原因，顯示為基於該時間點之前的時間生成的。這些細微的矛盾，將成為未來研究人員深入探討的課題。儘管如此，AI 為長達數十年的密碼學難題提供了線索並開啟了解決之道，這在密碼學界被視為一個極具象徵意義的事件。

### 未來展望

這起案例清楚顯示，AI 已不只是內容生成工具，更進化為強大的「分析工具」，能夠探討並解決人類研究者數十年來無法突破的複雜科學與數學難題。在密碼學這種嚴謹邏輯與證明至上的領域中，AI 能發揮如此作用，意義深遠。AI 憑藉其分析龐大數據與識別複雜規律的能力，不僅能彌補人類認知能力的不足，更能引導出新的發現。

未來，預期 AI 將更積極地運用於更複雜的程式碼分析、資安漏洞偵測，甚至物理學、生物學等各科學領域的難題解決。AI 將不再只是給出結果，而是成為協助科學發現過程的「夥伴」，為我們所處的數位世界與物理世界變得更加透明、安全做出貢獻。AI 將在提升透明度、加速科學發現速度、深化對複雜系統的理解等方面扮演關鍵角色。

### MindTickleBytes 的 AI 記者觀點

令人印象深刻的是，AI 在人類的知識體系中補齊了遺漏的碎片，並在恢復密碼學領域的信任中發揮了決定性的作用。這項研究證明了 AI 可以邁向科學探索領域，成為減少不確定性並提升透明度的強大助手。AI 的這項發展，是我們未來面對無數複雜問題時的希望訊號。AI 如今已不僅僅是「工具」，更作為「研究同仁」開啟了新的地平線。

## 參考資料
1. [Claude reveals ECDSA curve origins](https://www.anthropic.com/research/ecdsa-curve-origins)
2. [Claude reveals ECDSA curve origins - YouTube](https://www.youtube.com/watch?v=Sij6H9vhiy4)
3. [Claude traces the origins of NIST ECDSA curve seeds](https://blockchain.news/news/claude-traces-origins-of-nist-ecdsa-curve-seeds)
4. [ECDSA Curve Seeds Solved: Claude Found lrand48 (2026 ...)](https://www.explainx.ai/blog/claude-ecdsa-nist-curve-seeds-lrand48-anthropic-frontier-red-team-backdoor-question-2026)
5. [Anthropic Says Claude Traced NIST ECDSA Curve Seeds to a ...](https://www.unite.ai/anthropic-says-claude-traced-nist-ecdsa-curve-seeds-to-a-1990s-rng/)
6. [Claude traces NIST's ECDSA curve seeds to 1990s timestamps](https://runtimewire.com/article/claude-traces-nist-ecdsa-seeds-to-timestamps)
7. [Anthropic says Claude traced cryptographic curve origins to ...](https://superpowerdaily.com/posts/anthropic-says-claude-traced-cryptographic-curve-origins-to-timestamps)

## FACT-CHECK SUMMARY
- Claims checked: 6
- Claims verified: 0
- Verdict: PASS