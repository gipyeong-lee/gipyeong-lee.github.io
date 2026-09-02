---
layout: post
title: "AI 錯過的 25 年漏洞，『特化型 AI』成功抓出"
description: "這是一個關於一個全新 AI 發現連 OpenAI 或 Anthropic 等知名 AI 都未能察覺的安全性漏洞的故事。輕鬆解析 curl 中潛藏 25 年的錯誤及其深遠意義。"
summary: "專注於安全領域的 AI「AISLE」發現了通用 AI 模型所忽略的 6 個安全漏洞，其中包括一個自 2001 年以來一直被遺忘、curl 項目歷史上最古老的漏洞。"
tags: [AI, 安全, curl, CVE, 技術議題]
image: 2026-09-02-Six-curl-CVEs-after-OpenAI-and-Anthropic-came-back-with-zero.jpg
image_alt: "在象徵數位代碼的數據流中，一個 AI 系統正在尋找代表安全漏洞的空洞。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "即便在通用大型模型時代，深入鑽研特定領域的『專業 AI』其價值將會更加顯著。"
quiz:
  - question: "在此次安全事件中，AISLE 共發現了幾個 CVE？"
    choices: ["1個", "3個", "6個"]
    answer: 2
    explanation: "AISLE 在本次調查中總共發現了 6 個新的安全漏洞（CVE）。"
  - question: "curl 項目中發現的最古老漏洞是從何時開始存在的？"
    choices: ["2010年", "2001年", "2026年"]
    answer: 1
    explanation: "該漏洞記錄為 CVE-2026-8932，經查明自 2001 年 3 月起就一直被遺忘至今。"
  - question: "關於本文所述『通用 AI』與『特化型 AI』的區別，下列敘述何者正確？"
    choices: ["通用 AI 的安全性總是優於特化型 AI。", "通用 AI 擁有廣泛知識，但在特定領域的深度探索上，可能不及專業工具。", "通用 AI 已不再進行開發。"]
    answer: 1
    explanation: "雖然 OpenAI 或 Anthropic 的模型非常強大，但此案例顯示，像 AISLE 這種專注於安全分析的系統在特定領域中能發揮更卓越的成效。"
lang: zh-tw
ref: 2026-09-02-Six-curl-CVEs-after-OpenAI-and-Anthropic-came-back-with-zero
---

## 找出 25 年前安全漏洞的「安全偵探」AI

試著想像一下：如果你在過去 25 年裡，每天早上出門時都仔細鎖好家門，結果卻發現原來玄關門鎖背面的螺絲從一開始就根本沒鎖緊，你會是什麼心情？可能會感到驚慌，但另一方面，或許也會因為過去 25 年來居然都沒出事而感到慶幸。

最近，全球開發者都在使用的一款數據傳輸工具「curl」（透過各種協定安全傳輸數據的工具）就發生了這樣的事。更令人驚訝的是，發現這個深層「安全漏洞」的並非人類，而是專門針對安全領域進行訓練的「特化型 AI 系統」。特別是這個系統，竟發現了連 OpenAI 或 Anthropic 等大企業所開發的著名「通用 AI」模型都完全未能察覺的 6 個致命漏洞。

### 這為何如此重要？

「curl」這個名字聽起來可能有點陌生，但事實上，各位每天都在享受這項工具的便利。我們常用的智慧型手機應用程式、筆記型電腦的軟體更新，以及各種 IoT（物聯網）設備在傳輸數據時，內部都在使用 curl 或相關技術「libcurl」（讓程式得以呼叫 curl 功能的程式庫）[Source 3]。

換句話說，該工具存在安全漏洞，意味著我們日常生活中使用的數十億台設備都可能暴露在駭客威脅之中。這次由安全專業 AI 平台 AISLE 發現的問題中，甚至包含如認證繞過（未經過安全程序便潛入）等致命 Bug，若非發現即時，差點就成了數據外洩的危險通道 [Source 5]。

### 簡而言之：「全能選手」與「專家」的差異

這次的結果展現了 AI 世界中一個有趣的面向。OpenAI 或 Anthropic 的模型是囊括世間萬物知識的「全能選手」。無論是寫作、撰寫程式碼或翻譯外語，它們都能駕輕就熟。然而，這次的 curl 安全調查卻如同「精密珠寶加工」，需要極其深厚且專精的領域知識。

比喻來說，通用 AI 就像是一台能快速俯瞰廣闊森林的無人機。雖然在掌握森林整體地形方面表現卓越，但要找出隱藏在森林底部落葉下的微小昆蟲（安全漏洞）卻相當困難。反之，像 AISLE 這樣帶著放大鏡和鑷子、徹頭徹尾翻遍地面的昆蟲學家，就能找出無人機所遺漏的細小生物 [Source 1, Source 6]。事實上，在這次案例中，通用 AI 模型不是只找到 1 個就是毫無斬獲，而 AISLE 卻找出了 6 個漏洞，展現出壓倒性的差距 [Source 6]。

### 當前狀況：curl 歷史上最古老的漏洞

在 AISLE 發現的漏洞中，包含一個標記為「CVE-2026-8932」的問題 [Source 3, Source 5]。這個 Bug 從 2001 年 3 月起就一直存在。在長達 25 年的時間裡，無數專業開發者審視並使用了這段程式碼，卻始終沒人察覺其中隱藏的細微邏輯錯誤 [Source 5, Source 7]。

因此，curl 在本次進行安全修補後，共記錄了 18 個 CVE（已公開的安全漏洞列表）[Source 3, Source 6]。這將被視為 curl 項目歷史上規模最大的一次安全改善工作 [Source 5]。

### 未來我們將面臨什麼？

這次事件將徹底改變我們看待 AI 的眼光。現在，競爭重點將不僅僅是製作「更聰明的 AI」，而是開始邁入「在特定業務中鑽研得更精深、更鋒利的 AI」之競爭時代 [Source 1]。

未來，除了安全領域外，在醫學、法律、半導體設計等極其具體且專業的領域中，具備比人類更銳利洞察力的「專家 AI」將會相繼登場。我們每天使用的軟體，也將在這些專家 AI 的不斷檢測下變得比過去安全得多。不過，我們所使用的 AI 具備哪些能力，以及該模型是否「遺漏」了什麼，將是我們人類未來必須持續保持警惕並關注的議題。

---

## MindTickleBytes 的 AI 記者觀點

在 OpenAI 與 Anthropic 展開大型模型效能競爭的同時，那些在隱蔽處默默解決安全問題的專業 AI 成長令人驚嘆。現在，AI 已不僅僅是「產出創意成果的工具」，更演變成了能找出我們過去 25 年來未能察覺之程式碼細微裂縫的「數位守門人」。

## 參考資料

1. [AISLE Discovered Six curl CVEs After OpenAI and Anthropic Found Zero](https://aisle.com/blog/aisle-discovered-six-curl-cves-after-openai-and-anthropic-found-zero)
2. [AISLE Discovers 6 CVEs in curl, Including Oldest Issue Ever Reported](https://aisle.com/blog/aisle-discovers-6-new-cves-in-curl-including-the-oldest-security-issue-ever-reported)
3. [Aisle Discovers 6 New CVEs in Curl, Including the Oldest Issue Ever Reported](https://news.chathome.org/news/aisle-discovers-6-new-cves-in-curl-including-the-oldest-issue-ever-reported-T7C6scli?locale=en)
5. [Curl Fixes a 25-Year-Old Bug in Its Largest CVE Release Yet](https://securityaffairs.com/194220/security/curl-fixes-a-25-year-old-bug-in-its-largest-cve-release-yet.html)
6. [AISLE Discovers 6 New CVEs in curl, Including the Oldest Issue Ever Reported](https://vuink.com/post/nvfyr-d-dpbz/blog/aisle-discovers-6-new-cves-in-curl-including-the-oldest-issue-ever-reported)
7. [Curl's 6 New CVEs Hit AI Toolchains - PromptZone](https://www.promptzone.com/xiu_lynch/curls-6-new-cves-hit-ai-toolchains-37ni)