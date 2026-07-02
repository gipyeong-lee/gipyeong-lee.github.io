---
layout: post
title: "建立 AI 助理，像寫筆記一樣簡單？透過 Markdown 設計的「瑪格麗特 (Margarita)」"
description: "不懂程式也能建立 AI 代理嗎？介紹一款全新的工具「瑪格麗特 (Margarita)」，它透過擴充 Markdown 格式，讓你能夠系統化地撰寫 AI 代理的工作流程。"
summary: "瑪格麗特 (Margarita) 是一款能為 Markdown 語法增添變數、迴圈等程式設計功能的工具，幫助任何人都能輕鬆設計 AI 代理的工作流程。"
tags: [AI, 代理, Markdown, 程式設計, 瑪格麗特]
image: 2026-07-02-Show-HN-Margarita---Programming-language-for-Agents-using-Markdown-ish-syntax.jpg
image_alt: "利用 Markdown 語法系統化地建構 AI 代理複雜工作流程的模樣"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "嘗試在無需複雜程式編寫的情況下設計 AI 代理邏輯，將成為 AI 代理普及化的關鍵鑰匙。"
quiz:
  - question: "瑪格麗特 (Margarita) 的主要特色之一 .mgx 檔案格式支援什麼功能？"
    choices: ["靜態文字生成", "AI 代理的執行控制（狀態、記憶體、工具呼叫等）", "簡單的 HTML 轉換"]
    answer: 1
    explanation: ".mgx 格式擴充了原有的 .mg 格式，在 AI 代理執行時提供所需的狀態管理或工具呼叫等額外功能。"
  - question: "使用瑪格麗特 (Margarita) 需要什麼 AI 模型？"
    choices: ["所有類型的模型", "Ollama 與 Claude", "僅限特定語言模型"]
    answer: 1
    explanation: "瑪格麗特目前需要 Ollama 與 Claude 才能使用。"
  - question: "瑪格麗特 (Margarita) 的目標是什麼？"
    choices: ["學習複雜的程式語言", "讓編寫代理像寫 Markdown 一樣簡單", "搜尋引擎最佳化"]
    answer: 1
    explanation: "瑪格麗特的目標是讓編寫代理的工作變得像使用 Markdown 寫作一樣簡單。"
lang: zh-tw
ref: 2026-07-02-Show-HN-Margarita---Programming-language-for-Agents-using-Markdown-ish-syntax
---

試著想像一下：早晨起床後，你對著 AI 助理說：「請幫我整理並摘要今天的會議資料。」接著，AI 就像人類一樣，自動搜尋所需檔案、摘要內容，並將結果寄送至你的電子郵件。我們將這種聰明的助理稱為「AI 代理」。然而，打造這類代理的過程至今仍非常複雜。開發者必須撰寫複雜的程式碼，並不斷地與「提示詞 (Prompt)」搏鬥，確保 AI 能確實執行任務。

不過，最近出現了一款新工具，讓設計 AI 代理變得像我們在部落格寫文章或做筆記時使用的「Markdown（用於輕鬆建立網頁文件的語法）」一樣簡單，這就是「瑪格麗特 (Margarita)」。

### 為什麼這個工具很重要？

至今為止，與 AI 溝通的方式主要以「對話」為主。但對話有時會讓 AI 誤解使用者的意圖，或在冗長的作業過程中迷失方向。開發者為了讓 AI 確實完成複雜的工作步驟，必須執著於撰寫提示詞。[參考資料 1](https://www.margarita.run/)

瑪格麗特解決了這些難題。因為它允許任何人使用熟悉的 Markdown 方式，按照既定規則設計 AI 代理的行為，而無須撰寫複雜程式碼。這意味著我們不必再執著於複雜的提示工程，就能系統化且一致地獲得想要的結果。[參考資料 1](https://www.margarita.run/)

### 輕鬆理解：為 Markdown 插上翅膀

為了理解瑪格麗特，我們來打個比方。想像一下你在做菜時寫的食譜卡。如果過去的方式是跟在廚師身邊不斷地說：「現在把洋蔥切開」、「現在調整火力」，那麼瑪格麗特就像是預先寫好了一張系統化的「食譜卡」。

簡單來說，瑪格麗特將我們熟知的 Markdown 語法與程式設計功能結合在一起。[參考資料 1](https://www.margarita.run/) 其主要功能如下：
- **變數 (Variable)**：儲存資訊數值的欄位。
- **迴圈 (Loop)**：依序處理多個項目的規則。
- **條件判斷 (Conditional)**：關於「如果是這樣，就執行那樣」的決策。

透過在 Markdown 中加入這些邏輯功能，就能明確規範 AI 代理在各種情況下該如何行動。[參考資料 4](https://github.com/Banyango/margarita) 瑪格麗特提供兩種檔案格式：[.mg 檔案](https://pypi.org/project/margarita/)用於製作動態提示詞，[.mgx 檔案](https://pypi.org/project/margarita/)則進一步扮演「代理腳本」的角色，控制代理的記憶體管理與工具呼叫。[參考資料 2](https://pypi.org/project/margarita/)

這些產出的結果本質上會渲染（顯示於螢幕）為我們熟悉的 Markdown 格式，因此只要是支援 Markdown 的地方都能使用。[參考資料 4](https://github.com/Banyango/margarita)

### 現狀：發展到什麼地步了？

瑪格麗特大幅簡化了開發者建構代理與建立邏輯的過程。特別是它允許將多個模版分開儲存，並在需要時引用或相互堆疊 (Nested)，顯著提升了工作效率。[參考資料 3](https://www.banyango.com/margarita/)

不過需要留意的是，目前使用此工具必須先設定 Ollama 與 Claude 模型環境。[參考資料 3](https://www.banyango.com/margarita/) 也就是說，比起完全的新手，它更適合已有一定程度 AI 開發環境知識的使用者，用來提升生產力。

### 未來展望

專家預測，不久的將來，Markdown 將超越單純的文件格式，成為軟體開發的核心語言。[參考資料 13](https://www.infoworld.com/article/4146579/markdown-is-now-a-first-class-coding-language-deal-with-it.html) 像瑪格麗特這樣的工具將加速這股趨勢。未來打造 AI 代理的工作將會越來越貼近自然語言與熟悉的文檔格式。時代正在轉變，你將不再是撰寫「提示詞」的人，而是管理代理這個「助理行為手冊」的管理者。

---

### MindTickleBytes 的 AI 記者觀點
技術越是複雜，處理它的工具就越應該直觀且簡單。瑪格麗特試圖以 Markdown 定義代理的嘗試，將從根本上讓 AI 與人類協作的方式變得更加透明。

---

## 參考資料
1. Margarita — Writing agents should be as easy as writing markdown. (https://www.margarita.run/)
2. margarita · PyPI (https://pypi.org/project/margarita/)
3. MARGARITA - MARGARITA (https://www.banyango.com/margarita/)
4. GitHub - Banyango/margarita: Margarita is a lightweight ... (https://github.com/Banyango/margarita/)
13. Markdown is now a first-class coding language: Deal with it | InfoWorld (https://www.infoworld.com/article/4146579/markdown-is-now-a-first-class-coding-language-deal-with-it.html)