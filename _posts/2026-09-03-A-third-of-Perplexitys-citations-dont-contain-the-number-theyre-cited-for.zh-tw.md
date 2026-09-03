---
layout: post
title: "AI 提供的「證據」，可以相信嗎？Perplexity 引用的背叛"
description: "探討 AI 搜尋引擎 Perplexity 所提供的來源可能缺乏實際根據的研究結果。"
summary: "近期研究顯示，Perplexity 作為回答依據所提供的引用來源中，有相當大比例並未包含實際的數據或數值。"
tags: [AI, 搜尋引擎, Perplexity, 人工智慧, 可信度]
image: 2026-09-03-A-third-of-Perplexitys-citations-dont-contain-the-number-theyre-cited-for.jpg
image_alt: "疊加在 AI 顯示搜尋結果畫面上的問號圖標"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是一個與其盲目相信 AI 的回答，不如進行交叉驗證的時代。在技術便利的背後，必須時刻警惕「幻覺（Hallucination）」的可能性。"
quiz:
  - question: "此次研究中發現，在包含數值的句子後所附的引用，實際上卻未包含該數值的機率約為多少？"
    choices: ["約 14.4%", "約 34.7%", "約 94%"]
    answer: 1
    explanation: "根據研究結果，在提及數值的句子中，有 34.7% 的引用所指向的頁面並未包含該數值。"
  - question: "Perplexity 在查找資訊時主要使用何種方式？"
    choices: ["基於訓練資料的回答", "基於即時網路搜尋的回答", "利用離線資料庫"]
    answer: 1
    explanation: "Perplexity 不依賴過去訓練的資料內容，而是採用透過即時網路搜尋來獲取最新資訊的方式。"
  - question: "Perplexity 的引用點擊率（CTR）與傳統搜尋結果相比如何？"
    choices: ["差不多", "遠低於傳統方式", "遠高於傳統方式"]
    answer: 2
    explanation: "Perplexity 的引用點擊率約為 18% 至 24%，遠高於傳統搜尋引擎的 2% 至 4%。"
lang: zh-tw
ref: 2026-09-03-A-third-of-Perplexitys-citations-dont-contain-the-number-theyre-cited-for
---

想像一下。為了今晚的簡報，你問 AI 搜尋引擎：「今年我國的 AI 市場成長率是多少？」AI 立即給出答案，並在句子末尾親切地標註 [1]、[2] 等數字，明確指出出處。我們通常看到這種出處，就會安心地認為：「這是 AI 親自查找並確認過的資訊。」但如果該出處實際上指向的是無關的頁面，會怎樣呢？

近期，AI 搜尋服務 Perplexity 對其作為回答依據所提供的引用語句，公開了令人震驚的實況。我們將一同探討那些我們所信賴的「出處」究竟有多準確，以及 AI 為何會犯下這種錯誤。

## 為何重要？

與傳統搜尋引擎不同，Perplexity 會自行總結龐大的網頁資料來生成答案。因此，使用者無需一一點擊多個網站，就能一次獲得答案。[出處：Perplexity 是引用引擎](https://mentionagent.ai/blog/how-to-get-cited-by-perplexity/)。事實上，使用者點擊引用（以數字表示的出處）的比例達到 18~24%，這遠高於傳統搜尋引擎 2~4% 的點擊率。[出處：2026 年如何在 Perplexity 中被引用](https://www.miniloop.ai/blog/perplexity-seo-how-to-get-cited-2026)。

換句話說，我們極度信任 AI 提供的出處，並確實透過它們深入挖掘資訊。然而，如果這些資訊不包含事實，我們便面臨陷入虛假資訊泥淖的風險。

## 輕鬆理解

簡單來說，Perplexity 的運作方式類似於**「一位聰明的秘書幫你查閱並整理無數本書籍」**。秘書在寫答案時，會在註腳寫道：「此內容在第 5 頁」。然而，有時秘書在寫完文章後，會事後補上註腳說：「啊，這部分好像在第 5 頁左右」。[出處：Perplexity 引用模式](https://bcited.ai/blog/perplexity-citation-patterns-source-selection)。在這個過程中，因為秘書的記憶模糊，導致指出了錯誤的頁面。

根據資料調查結果，在包含數值的句子所附的引用中，約有 34.7% 連接到完全不包含該數值的頁面。[出處：Perplexity 引用審計報告](https://hausresearch.com/reports/perplexity-citation-audit/)。這比喻來說，就像我們在解數學題想確認答案頁面時，書後面的詳解內容竟然是其他題目的解答一樣。此外，根據整體評估，Perplexity 所提出的主張中，約有 14.4% 的結果並沒有得到實際引用出處的支持。[出處：Perplexity 引用審計報告](https://hausresearch.com/reports/perplexity-citation-audit/)。

## 當前情況

Perplexity 在約 94% 的回答中都會標註出處，對引用相當積極。[出處：2026 年，Perplexity 總是標註出處嗎？](https://www.fonzy.ai/blog/does-perplexity-cite-sources)。但問題在於，AI 模型本身在生成答案後，並不確認該答案是否為事實，而是採取「事後」湊出處的方式。[出處：Perplexity 引用模式](https://bcited.ai/blog/perplexity-citation-patterns-source-selection)。

當然，有時並非 Perplexity 的錯。也存在因為外部 App 無法正確顯示 Perplexity 的資料，導致引用連結看起來消失的現象。[出處：Perplexity 出處未標註問題](https://perplexityaimagazine.com/perplexity-hub/perplexity-not-citing-sources/)。然而，系統從根本上獲取與答案內容不一致來源的「幻覺（Hallucination，人工智慧將非事實資訊生成得似是而非的現象）」確實存在，這是使用者必須認知的局限性。[出處：2026 年 Perplexity 評論](https://vantaige.io/ai-tool/perplexity)。

## 未來會如何？

未來，在 AI 搜尋服務之間的競爭中，比起「顯示多少出處」，**「連結多準確的出處」**將成為更重要的標準。已經有研究指出 Perplexity 的引用比 ChatGPT 多出約 3 倍，並表示量上的擴張並不總是能保證質上的準確性。[出處：Perplexity 引用 9 個訊號](https://citevantage.com/blog/how-to-get-cited-by-perplexity/)。隨著使用者變得更聰明，提供錯誤引用的 AI 平台將會失去信任。

## MindTickleBytes 的 AI 記者觀點
AI 搜尋引擎雖然方便，但必須警惕毫無根據的確信。當你點擊 AI 給出的出處卻發現沒有想要的內容時，這很大程度上是因為 AI 並未深入理解內容，而僅僅是推測了一個「看起來很像的位置」。在閱讀搜尋出的答案時，這是一個需要養成以「批判性眼光」再次確認內容習慣的時代。

## 參考資料
1. [AthirdofPerplexity'scitationsdon'tcontainthenumberthey'r...](https://news.ycombinator.com/item?id=49536201)
2. [How to GetCitedbyPerplexity: The Tactical Playbook for 2026 | Cintra](https://cintra.run/blog/how-to-get-cited-by-perplexity)
3. [How to Rank inPerplexityAI: What 21CitationsPer Query... | BlueJar](https://bluejar.ai/blog/how-to-rank-in-perplexity-ai/)
4. [How to GetCitedbyPerplexityAI | Mentionable](https://mentionable.ai/en/guides/rank-on-perplexity)
5. [PerplexityInlineCitations: How [1][2][3] Links Work](https://amicitable.com/blog/does-perplexity-cite-inline-sources)
6. [PerplexitySEO: How to GetCitedin 2026](https://www.miniloop.ai/blog/perplexity-seo-how-to-get-cited-2026)
7. [How to GetCitedbyPerplexity(2026 Playbook) | MentionAgent](https://mentionagent.ai/blog/how-to-get-cited-by-perplexity/)
8. [The 50 Most-CitedWebsites inPerplexity(September 2026)](https://ahrefs.com/blog/most-cited-domains-perplexity/)
9. [PerplexityCitations| Fetchable Sources, Enquire Desk](https://www.worldwidebacklinks.com/ai-backlinks/perplexity-citations/)
10. [PerplexitycitesClickUp 6,474 times. Notion gets 741… Why?](https://foundationinc.co/lab/vol-304)
11. [PerplexityCitationPatterns: What Actually Gets Sourced — b/cited](https://bcited.ai/blog/perplexity-citation-patterns-source-selection)
12. [How to earn morecitationsinperplexityai search](https://snoika.com/blog/perplexity-ai-search-citation-checklist)
13. [How to GetCitedbyPerplexity: 9 Source Signals | CiteVantage](https://citevantage.com/blog/how-to-get-cited-by-perplexity/)
14. [A third of Perplexity's citations don't contain the number they're ...](https://hausresearch.com/reports/perplexity-citation-audit/)
15. [Perplexity Not Citing Sources: 8 Fixes 2026](https://perplexityaimagazine.com/perplexity-hub/perplexity-not-citing-sources/)
16. [Perplexity AI Review 2026: Citations, Limits & Real Failures](https://vantaige.io/ai-tool/perplexity)
17. [Does Perplexity Always Cite Sources? 2026 Data Says No](https://www.fonzy.ai/blog/does-perplexity-cite-sources)
18. [How Perplexity Selects Its Citations: What We Know From Testing and ...](https://aiseoshift.com/blog/how-perplexity-selects-citations/)
19. [Getting Cited by Perplexity: What It Actually Quotes — Genαi](https://genalphai.com/getting-cited-by-perplexity-teardown/)
20. [How Perplexity Decides Which Sources to Cite - authoritytech.io](https://authoritytech.io/blog/how-perplexity-selects-sources-algorithm-2026)