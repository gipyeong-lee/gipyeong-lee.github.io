---
layout: post
title: "介紹 El Yayster：不只是電腦的『嘴』，更是其『身體』的 AI"
description: "如果 AI 不僅僅是提供答案的助手，而是能直接在編輯器中行動、管理代碼並控制環境，那會是什麼模樣？帶您深入了解居住在 Emacs 中的新形態 AI：El Yayster。"
summary: "若以往的 Emacs AI 工具僅扮演回答使用者問題的『嘴』，El Yayster 則賦予 AI 編輯器的控制權，使其成為能直接觀察並採取行動的『身體』。"
tags: [AI, Emacs, ElYayster, 程式設計]
image: 2026-09-08-El-Yayster-a-resident-LLM-that-inhabits-Emacs.jpg
image_alt: "概念圖：呈現 AI 在 Emacs 編輯器環境中主動工作的模樣"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是從『使用工具的 AI』轉向『成為環境本身的 AI』之變革。這標誌著從等待使用者意圖的被動關係，邁向共同協作之代理人（Agent）關係的有趣一步。"
quiz:
  - question: "現有的多數 Emacs AI 套件與 El Yayster 之間最大的差別為何？"
    choices: ["支援的 AI 模型種類", "AI 是否直接控制 Emacs 環境", "安裝方式"]
    answer: 1
    explanation: "El Yayster 超越了單純的對話介面，其特色在於 AI 能擔任『身體』的角色，觀察 Emacs 環境並主動使用工具進行控制。"
  - question: "El Yayster 用於控制 Emacs 環境的方式為何？"
    choices: ["直接連接雲端", "受控的 Emacs Lisp 代碼", "使用者逐一輸入的巨集"]
    answer: 1
    explanation: "El Yayster 使用『受控（gated）的 Emacs Lisp』來與 Emacs 環境進行互動。"
  - question: "El Yayster 最推薦的執行環境（Happy Path）是什麼？"
    choices: ["需要 API 金鑰的商用雲端服務", "在本機執行的 Ollama", "基於網頁瀏覽器的編輯器"]
    answer: 1
    explanation: "儘管 El Yayster 支援各種 OpenAI 相容端點，但最推薦的方式是在本機執行 Ollama。"
lang: zh-tw
ref: 2026-09-08-El-Yayster-a-resident-LLM-that-inhabits-Emacs
---

想像一下：早上起床打開電腦，發現平日使用的編輯器不再只是單純的寫作空間，而是成了在你身邊一起思考、行動的夥伴，那會是什麼樣的情景？

過去我們所使用的許多 AI 工具，就像是「嘴」。當我們開口（輸入）詢問時，AI 只是在文件視窗中吐出相應的回答。然而，最近在 Emacs（高度可擴展的文字編輯器）環境中出現了一個帶來極具趣變化的實驗性專案，其名稱為 **「El Yayster」**。

### 為什麼這很重要？

以往的 AI 整合功能多半是「問答」導向的助理形式，即由使用者向 AI 提問，AI 再呈現結果。但 El Yayster 徹底顛覆了這種關係。

這項技術之所以重要，是因為「AI 的位置」發生了改變。現在 AI 不再是等待指示的被動助理，而是能自動掌握編輯器內狀況並親自控管環境的「代理人（Agent）」。這就像廚師身邊不是只有一個回答食譜的助手，而是多了一位能幫忙處理食材、直接調整火候的熟練學徒。這意味著 AI 可以親自操作編輯器，解決我們重複性的作業。 [出處: ElYayster – a resident LLM that inhabits Emacs | Modern Orange](https://modernorange.io/item/49602258)

### 易於理解：從「嘴」進化到「身體」

我們可以透過這樣的比喻來理解這種變化：

過去的 AI 工具就像電話那頭的客服專員，當我們說出症狀，對方僅能用話語告訴我們解決方法。然而，**El Yayster 則是將 Emacs 這具「身體」借給了人工智慧**。 [出處: GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)

此模型不僅是在文字緩衝區（buffer）中寫字，它更能像活生生的生命體般感知 Emacs 這個軟體環境。 [出處: yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md)

1. **觀察**：AI 首先觀測我的即時環境。
2. **決策**：判斷需要採取什麼行動。
3. **行動**：利用稱為「受控（gated）的 Emacs Lisp（用於操控 Emacs 編輯器的程式語言）」的工具來實際操作編輯器。
4. **重複**：確認結果後繼續進行下一個任務。 [出處: GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)

就像我們透過滑鼠和鍵盤操作編輯器一樣，AI 也能親自按下 Emacs 的按鈕並執行指令。

### 現況：該如何使用？

目前 El Yayster 被評為一項極具原創性的嘗試，它實際居住在 Emacs 空間中並展開活動。 [出處: Branches · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/branches/all)

使用者可以連接任何與 OpenAI 相容的模型，特別是將「在本機環境中執行的 Ollama」視為最推薦的運作環境，即所謂的「快樂路徑（Happy Path）」。 [出處: yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md) 這也意味著，在不使用雲端 API 的情況下，也能在自己的電腦內安全地讓 AI 隨心所欲地操控編輯器。

當然，必須銘記這仍是處於初期階段的實驗性工具。對於熟練使用 Emacs 的使用者來說，它會成為強大的自動化工具，但由於 AI 被賦予了複雜的控制權，因此該將多少編輯器環境交付給 AI，仍由使用者自行斟酌。

### 未來會如何發展？

未來 AI 將不僅僅止於審閱我們撰寫的代碼，根據我們設定的規則，AI 自動變更編輯器設定、尋找 Bug 並優化專案結構，這些場景很有可能成為日常。El Yayster 正是邁向該未來的一次大膽實驗。

看著未來 AI 能以多麼細膩的方式操作編輯器的「身體」，以及我們在過程中能享受到多麼舒適的工作環境，將會是一次非常有趣的體驗。

---

## MindTickleBytes AI 記者觀點
El Yayster 的出現，是技術工具如何與人類共生的絕佳範例。我們正走過人類逐一輸入指令的時代，邁向 AI 成為系統的一部分並共同呼吸的「居住型 AI（Resident AI）」時代。

## 參考資料
1. [ElYayster – a resident LLM that inhabits Emacs | Modern Orange](https://modernorange.io/item/49602258)
2. [yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md)
3. [GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)
4. [Branches · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/branches/all)