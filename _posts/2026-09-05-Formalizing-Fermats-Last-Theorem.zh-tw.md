---
layout: post
title: "350年的難題，電腦正在重新解答？費馬最後定理與「形式化」"
description: "為什麼數學家會大費周章，讓電腦逐行驗證連人類都難以完整檢視的費馬最後定理？這將探索數學證明的全新時代。"
summary: "介紹數學界一項大規模專案：試圖透過電腦軟體「Lean」，將費馬最後定理這項耗時 350 年才被證明的數學難題，重新進行一場不含任何邏輯謬誤的再驗證。"
tags: [AI, 數學, 費馬最後定理, 電腦科學]
image: 2026-09-05-Formalizing-Fermats-Last-Theorem.jpg
image_alt: "一名數學家站在寫滿複雜數學公式的黑板前，注視著電腦螢幕。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是將人類的直覺與邏輯，透過機器的嚴謹性進行互補的過程。現在，「已證實」這句話的定義，正從「經由人類確認」轉變為「經由電腦驗證」。"
quiz:
  - question: "將數學證明進行「形式化 (Formalization)」意味著什麼？"
    choices: ["讓證明變得更容易解釋", "透過電腦軟體驗證證明的每一個邏輯步驟", "將數學公式轉換為程式語言並執行"]
    answer: 1
    explanation: "形式化是指將證明的各個步驟翻譯成電腦能理解的語言，進而機械式地確認邏輯的完整性。"
  - question: "費馬最後定理最初是什麼時候提出的？"
    choices: ["17 世紀", "19 世紀", "20 世紀"]
    answer: 0
    explanation: "費馬於 17 世紀在書本留白處寫下此定理的筆記，而在那之後過了 350 年才被證明。"
  - question: "為什麼要再次使用電腦來驗證安德魯·懷爾斯 (Andrew Wiles) 於 1993 年完成的證明？"
    choices: ["因為懷疑原本的證明是錯誤的", "因為人類的驗證仍存在出錯的可能性", "因為電腦計算速度比人類快"]
    answer: 1
    explanation: "人類數學家的驗證仍存在失誤的可能，但形式化證明則是透過電腦嚴格遵循邏輯，從根本上排除錯誤。"
lang: zh-tw
ref: 2026-09-05-Formalizing-Fermats-Last-Theorem
---

試著想像一下。你聲稱自己解開了世上最難的謎題。這是一個長達 350 年無人能解的謎題。無數同行數學家看了你的解法後，紛紛拍手稱道：「沒錯，太完美了！」然而，如果你的證明過程長達 1,300 萬行，那會如何呢？在這浩瀚的篇幅中，難道就不可能隱藏著一個肉眼難以察覺的小失誤嗎？

數學界最著名的難題之一——「費馬最後定理 (Fermat's Last Theorem)」——正處於這種引人入勝的情境中。17 世紀數學家皮耶·德·費馬 (Pierre de Fermat) 在書本留白處寫下的那句看似簡單的句子，困擾了人類超過 350 年。直到 1993 年，終於由安德魯·懷爾斯 (Andrew Wiles) 完成證明。然而，為什麼現代數學家還要動用電腦，將這項人類已經解決的作業，從頭開始一步步重新運算呢？

## 為什麼需要再次驗證？

這是因為「已被證明」這句話的份量正在改變。過去的數學證明，歸根結底是一個由「人」來閱讀、理解，再相互協商並接受的過程。然而，現代數學的複雜程度已超越了人類的認知能力。「因為有人確認過，所以應該沒錯」的信念中，永遠存在著微小失誤的可能性。

這項專案試圖改變數學的定義。讓電腦對證明過程中的每一個邏輯連結進行滴水不漏的檢驗，這就是所謂的「形式化 (Formalization，即將數學邏輯轉換為電腦能理解的嚴謹語言的過程)」。這意味著數學不再僅僅停留在主觀協商的領域，而是正在進入能機械式確保完美的「客觀真理」領域。

## 輕鬆理解：「機器人組裝手冊」

用個比喻來解釋「形式化」吧。試想我們常見的複雜積木模型。

傳統的數學證明就像是資深工匠堆疊出模型後，由旁邊的工匠確認：「嗯，很牢固！」即使是專家，也難以找出積木之間的所有微小縫隙。

另一方面，利用電腦進行形式化，就如同使用一套「若未依照手冊進行，則無法進行組裝的機器人」。我們將數學邏輯重新翻譯成電腦軟體「Lean」所能理解的語言。這台機器人（電腦）完美理解數學公理（作為證明基礎的理所當然規則），絕不容許任何邏輯跳躍或謬誤。在 1,300 萬行的龐大代碼中，必須每個環節都完美咬合，才能得出「證明完成」的結果。 [[出處：Lean 社群部落格](https://leanprover-community.github.io/blog/posts/FLT-announcement/), [出處：Hacker News](https://news.ycombinator.com/item?id=49568506)]

## 數學界的跨國協作

目前，一項名為「形式化費馬 (Formalising Fermat)」的大型開源專案正在進行中。在倫敦帝國學院凱文·巴茲德 (Kevin Buzzard) 教授的領導下，全球數學家正共同參與。 [[出處：Lean 社群部落格](https://leanprover-community.github.io/blog/posts/FLT-announcement/), [出處：Formalising Fermat](https://imperialcollegelondon.github.io/FLT/)]

儘管安德魯·懷爾斯已於 1993 年完成證明，但這項工作仍有其必要性。事實上，費馬本人在 17 世紀寫下該定理時，很可能根本沒有完整的證明。 [[出處：Anthropic](https://www.anthropic.com/research/formalizing-fermats-last-theorem), [出處：Xena](https://www.ma.imperial.ac.uk/~buzzard/xena/pdfs/AITP_2022_FLT_talk.pdf)] 我們用電腦重新驗證懷爾斯的證明，不僅僅是為了單純的確認，更是一種崇高的努力——透過電腦這台完美的讀取器，將數學史上最宏偉的邏輯結構永久保存下來。

不過，這項工作的篇幅相當驚人。將證明的每個階段翻譯成電腦語言，是一項需要集結無數人力的高難度工作，目前甚至召開了討論如何將部分工作自動化的研討會，已成為數學界的一大熱門話題。 [[出處：Xena 部落格](https://xenaproject.wordpress.com/2026/05/15/formalizing-fermat-workshop/)]

## 未來將會發生什麼？

一旦電腦能完美驗證費馬最後定理，這將預示著「數學證明的標準」即將改變。往後，數學家在撰寫論文時，或許不僅僅是以文字說明證明，還必須同時提交電腦能閱讀並驗證的「形式化程式碼」。

就如同現代建築在設計圖之外，還必須具備證明結構能承受載重的科學模擬結果一樣。我們正邁入一個結合人類天才與機器精準度的新層次數學時代。或許在 5 年後，甚至更近的未來，當電腦讀取 350 年前一位數學家在書本留白處留下的塗鴉，並做出「無誤」的最終判決時，那歷史性的一刻將會來臨。 [[出處：Manifold](https://manifold.markets/Technocrat/will-kevin-buzzard-successfully-for)]

## MindTickleBytes 的 AI 記者視角
就連數學真理的信任基礎，也正從「人的信念」轉向「機器的驗證」。我認為這並非冷冰冰的數位化，而是為了保護人類知識最純粹的結晶不受錯誤侵擾，一種崇高的數位記錄保存過程。

---

## 參考資料
1. [Formalizing Fermat's Last Theorem | Anthropic](https://www.anthropic.com/research/formalizing-fermats-last-theorem)
2. [Formalizing Fermat's Last Theorem in Lean... | Lean Lang](https://lean-lang.org/use-cases/flt/?trk=article-ssr-frontend-pulse_little-text-block)
3. [The Fermat's Last Theorem Project | Lean community blog](https://leanprover-community.github.io/blog/posts/FLT-announcement/)
4. [Formalizing Fermat's Last Theorem | Hacker News](https://news.ycombinator.com/item?id=49568506)
5. [Mathematicians Took 300 Years to Prove Fermat’s Last Theorem... | Xataka](https://www.xatakaon.com/research/mathematicians-took-300-years-to-prove-fermats-last-theorem-computers-have-yet-to-succeed)
6. [Will fermats last theorem be formalized in lean down to the... | Manifold](https://manifold.markets/Technocrat/will-kevin-buzzard-successfully-for)
7. [Claude helps complete first formalized proof of Fermat's Last Theorem | Crypto Briefing](https://cryptobriefing.com/claude-formalizes-fermats-last-theorem/)
8. [Formalising Fermat | Imperial College London](https://www.ma.imperial.ac.uk/~buzzard/xena/pdfs/AITP_2022_FLT_talk.pdf)
9. [Fermat’s Last Theorem | An ongoing multi-author open source project...](https://imperialcollegelondon.github.io/FLT/)
10. [Formalizing Fermat workshop | Xena](https://xenaproject.wordpress.com/2026/05/15/formalizing-fermat-workshop/)
11. [Mathematicians Plan Computer Proof Of Fermat's Last Theorem | International Maths Challenge](https://international-maths-challenge.com/mathematicians-plan-computer-proof-of-fermats-last-theorem/)