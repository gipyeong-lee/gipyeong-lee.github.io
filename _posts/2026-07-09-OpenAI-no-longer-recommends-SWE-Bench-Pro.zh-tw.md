---
layout: post
title: "AI 程式設計能力，該從試題重新審視？OpenAI 的決斷"
description: "OpenAI 已停止推薦使用過去作為 AI 程式設計能力評估標準的『SWE-Bench Pro』。隨著試題本身發現缺陷，AI 效能評估的可靠性亮起了紅燈。"
summary: "OpenAI 在用於衡量 AI 程式設計能力的指標『SWE-Bench Pro』中發現約 30% 的錯誤，並已停止推薦使用。"
tags: [AI, 程式設計, 開發, OpenAI, SWE-Bench]
image: 2026-07-09-OpenAI-no-longer-recommends-SWE-Bench-Pro.jpg
image_alt: "在程式碼片段與 AI 圖示交織的背景上，浮現著象徵試題錯誤的警告標誌。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "隨著 AI 技術的飛速發展，用於衡量這些技術的『考試』精確度已跟不上發展速度。我們正邁向一個需要由開發者親自進行驗證的時代。"
quiz:
  - question: "OpenAI 停止推薦使用 SWE-Bench Pro 的最大原因為何？"
    choices: ["AI 的能力太強了", "公開的工作任務中約有 30% 組成錯誤", "所有 AI 已經都拿到滿分了"]
    answer: 1
    explanation: "OpenAI 表示，SWE-Bench Pro 的公開工作任務中約有 30% 無法正常運作，導致結果不可信。"
  - question: "SWE-Bench Verified 為何先被停止使用？"
    choices: ["使用費太貴了", "開發者不足", "資料污染與試題本身的缺陷"]
    answer: 2
    explanation: "除資料污染問題外，經審查後發現約 60% 的試題在結構上存在缺陷，因此被停止使用。"
  - question: "開發 SWE-Bench Pro 的公司是哪一家？"
    choices: ["Google", "Scale AI", "Microsoft"]
    answer: 1
    explanation: "SWE-Bench Pro 是由 Scale AI 開發並於 2025 年 9 月發布。"
lang: zh-tw
ref: 2026-07-09-OpenAI-no-longer-recommends-SWE-Bench-Pro
---

想像一下。您去參加一場非常重要的數學考試，結果發現考卷上的答案是錯的，或者題目本身根本不成立。無論學生多麼努力解題，都無法獲得對其實際能力的準確評估。最近 AI 業界發生的「程式設計考試」爭議，情況正是如此。

長期以來，OpenAI 一直積極推薦將「SWE-Bench Pro」作為衡量 AI 軟體工程能力的工具。然而，OpenAI 最近認定，該考試中約 30% 的試題配置錯誤，無法確保結果的可靠性。因此，OpenAI 宣布不再推薦將其作為官方評估標準 [Source 3, Source 11, Source 4]。

### 為什麼這很重要？

我們每天使用的智慧型手機應用程式、銀行系統、新聞服務等，全都是由開發者編寫的程式碼所驅動。因此，AI 程式設計能力的高低，是決定我們日常接觸到的技術能變得多「聰明」的重要指標。

但如果用來測量這些「程式設計能力」的考題本身毫無用處，會發生什麼事？AI 企業一直利用這些考試成績來證明自家模型的優越性。如果考試本身就有問題，可能會導致效能數據被誇大，或是無法得到公正的評估，產生扭曲的結果。這將極大風險地誤導消費者，使大眾誤解 AI 技術的實質進步水準。

### 簡單易懂：AI 程式設計考試的秘密

程式設計考試通常透過「單元測試（Unit Test，一種自動化檢測，用於確認程式碼是否能正確執行特定功能）」來計算分數。例如，針對「請製作一個按下此按鈕後能切換畫面的功能」這樣的題目，由 AI 撰寫程式碼，如果通過了測試，就會被判為正確。

比喻來說，就像舉辦一場料理大賽，評審們聲稱要測量「湯頭濃度」，結果發現他們定下的標準竟然是錯誤的溫度計。無論廚師（AI）做出了多麼頂級的料理，都會因為錯誤的溫度計，導致實力被低估，或者反過來對完全不對味的料理給予高分。

OpenAI 過去也曾使用過名為「SWE-Bench Verified」的評估工具。但該工具在面臨資料污染問題的同時，也被揭露約有 59% 的題目存在結構性缺陷，隨後已被停止使用 [Source 2, Source 8, Source 13, Source 9]。

這次被停止推薦的 SWE-Bench Pro，由於是以真實的 GitHub（開發者共享程式碼的平台）上複雜議題為基礎進行出題，也一直被指出任務本身的性質過於模糊且破碎，難以讓 AI 單獨解決 [Source 3, Source 14]。

### 當前現狀：在泥濘中尋找珍珠

目前，AI 模型正呈現飛躍式的發展。然而，衡量其效能的指標卻尚未具備足以匹配「AI 時代」的完整度 [Source 6, Source 14]。

SWE-Bench Pro 是 Scale AI 公司於 2025 年 9 月發布的，該公司嘗試應用比以往更嚴格的版權授權，以最大限度地減少資料污染 [Source 7, Source 8]。然而，透過這次的聲明可以發現，無論如何精心設計，要將真實開發環境的複雜性完美地轉移到自動化測試中，是一件多麼困難的事。

Scale AI 的研究負責人 Bing Liu 指出，這次的決策充分反映了任務模糊性、資料污染，以及單靠狹義的單元測試無法完美測量 AI 實力的局限性 [Source 14]。

### 未來將如何發展？

未來，AI 程式設計能力的評估方式將經歷根本性的改變。

1. **更精確的評估標準**：業界將致力於建立新的標準，不僅僅依賴自動化評分，而是能綜合判斷 AI 解決問題的「過程」與「複雜度」 [Source 12]。
2. **強調與開發者的協作**：評估重點將從單純「AI 獨自撰寫程式碼」，轉向「真實開發者如何與 AI 溝通並解決問題」的方式 [Source 12]。
3. **持續性的驗證**：管理評估資料本身不被污染，將如同 AI 模型開發一樣，成為不可或缺的「基礎科學」領域。

我們正生活在 AI 能自主編寫程式碼的時代。然而，這次事件提醒了我們，打造出能精準評估該能力的「溫度計」，與技術發展本身同樣是一項重要的課題。

---

## 參考資料

1. [OpenAI Abandons SWE-Bench Verified, Citing Widespread Data Contamination and Flawed Tests](https://www.siliconreport.com/openai-abandons-swe-bench-verified-citing-widespread-data-contamination-and-flawed-tests-6ebd9b34)
2. [OpenAI Retracts Recommendation To Use SWE Bench Pro As Coding Eval Over 30% Broken Tasks](https://officechai.com/ai/openai-retracts-recommendation-to-use-swe-bench-pro-as-coding-eval-over-30-broken-tasks/)
3. [OpenAI no longer recommends SWE-Bench Pro as coding benchmarks saturate](https://savedelete.com/news/openai-swe-bench/)
4. [Why we no longer evaluate SWE-bench Verified - keynews.ai](https://keynews.ai/articles/290)
5. [OpenAI Drops SWE-bench Verified: What It Means for AI](https://www.adwaitx.com/openai-swe-bench-verified-retired-ai-benchmarks/)
6. [OpenAI Abandons SWE-bench Verified: 59% Flawed Tests](https://byteiota.com/openai-abandons-swe-bench-verified-59-flawed-tests/)
7. [OpenAI Drops SWE-bench Verified Over Contamination Concerns](https://aibreakingwire.com/news/openai-ditches-swe-bench-verified-cites-critical-flaws/)
8. [OpenAI Retracts SWE-Bench Pro After Finding 30% of Tasks Broken | AlphaSignal](https://alphasignal.ai/news/openai-retracts-swe-bench-pro-after-finding-30-of-tasks-broken)
9. [OpenAI Developers on X](https://x.com/OpenAIDevs/status/2026002219909427270)
10. [OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)
11. [OpenAI moves beyond SWE-bench Verified as coding benchmarks saturate](https://tessl.io/blog/openai-moves-beyond-swe-bench-verified-as-coding-benchmarks-saturate/)