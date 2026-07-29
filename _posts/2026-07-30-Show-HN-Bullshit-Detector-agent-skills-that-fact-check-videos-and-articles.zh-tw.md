---
layout: post
title: "AI 能抓出影片中的假訊息嗎？『Bullshit Detector』使用心得"
description: "帶您了解新的 AI Agent 技能『Bullshit Detector』，它可以幫您向 AI 詢問影片或文章內容，並進行事實查核。"
summary: "使用 Claude Code 的新插件『Bullshit Detector』，您可以直接讓 AI 對影片或文章的真偽進行即時事實查核。"
tags: [AI, 事實查核, ClaudeCode, 生產力]
image: 2026-07-30-Show-HN-Bullshit-Detector-agent-skills-that-fact-check-videos-and-articles.jpg
image_alt: "AI 在智慧型手機螢幕上分析影片資訊並確認真偽的數位繪圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在資訊爆炸的時代，AI 成為輔助批判性思考的工具是非常正面的發展。不過，AI 的判斷並非完美，使用者的最終確認仍然不可或缺。"
quiz:
  - question: "『Bullshit Detector』是透過什麼方式安裝的？"
    choices: ["作為網頁瀏覽器擴充功能安裝", "作為 Claude Code 插件安裝", "從作業系統系統設定中安裝"]
    answer: 1
    explanation: "『Bullshit Detector』是以 Claude Code 插件的形式安裝，供 Agent 使用。"
  - question: "透過『Bullshit Detector』無法讓 Agent 執行的任務是？"
    choices: ["請求說明影片的特定片段", "請求總結影片內容", "直接傳送電子郵件給影片創作者"]
    answer: 2
    explanation: "可用的功能包括事實查核、總結以及對特定時間戳記的說明請求等。"
  - question: "使用 AI 事實查核工具時，最需要注意的一點是什麼？"
    choices: ["必須無條件 24 小時開啟", "AI 的結果並非總是 100% 真實，使用者必須再次確認", "必須付費購買才能獲得結果"]
    answer: 1
    explanation: "AI 是強大的輔助工具，但可能出現錯誤，因此必須隨時保持批判性審查。"
lang: zh-tw
ref: 2026-07-30-Show-HN-Bullshit-Detector-agent-skills-that-fact-check-videos-and-articles
---

想像一下，您在 YouTube 上發現一部聲稱內容極具價值的 1 小時長影片。但影片內容究竟是事實，還是僅僅為了賺取點閱率的假新聞，常常讓人感到困惑。或許您也曾因為懶得一一搜尋相關報導，或是時間不足，最終只能放棄查證。現在，一個可以將這些煩惱交給 AI 的時代正在開啟。

### 為什麼這很重要？

我們每天都在消耗海量的影片與文章。遺憾的是，其中混雜著許多毫無根據的觀點或被扭曲的資訊。特別是影片內容，相比文字更難查證資訊，因此假新聞極易傳播。[『Bullshit Detector』](https://github.com/SerhiiKorniienko/bullshit-detector) 這類工具，能幫助使用者不必經過複雜的搜尋流程，僅需對 AI Agent 拋出問題，即可辨別資訊的可信度。這意味著資訊的消費方式，正從「被動接收」轉變為「主動驗證」。

### 輕鬆理解

簡單來說，『Bullshit Detector』就像是您的個人「事實查核秘書」。這個工具是可以安裝在 [Claude Code](https://github.com/SerhiiKorniienko/bullshit-detector) 這類 AI 環境中的插件（為既有程式增加功能的一種額外軟體）。

比喻來說，就像煮飯時機器手臂幫您處理繁雜的備料工作，AI 代替您完成了資訊海洋中「事實查核」這項艱難的過程。當您問 AI：「這部影片內容是真的嗎？」AI 就會分析影片脈絡，找出相關證據並整理給您。

具體來說，使用 [Bullshit Detector](https://github.com/SerhiiKorniienko/bullshit-detector) 可以實現以下功能：
- **請求事實查核**：詢問「這內容是真的嗎（is this bullshit）？」
- **請求總結**：提取長影片的核心內容
- **片段確認**：像「請說明 12 分 30 秒處的內容」這樣，針對特定時間戳記（影片的特定時間位置）請求分析

### 現況

目前『Bullshit Detector』以 [Claude Code 的 Agent 技能](https://github.com/SerhiiKorniienko/bullshit-detector)形式提供。使用者安裝完成後，即可用我們日常的語言與 Agent 溝通並驗證資訊。網路上雖已有各式各樣的事實查核工具，但該工具的區別在於能針對影片內部的特定點進行即時分析並要求事實查核。[不過，由於 AI 的事實查核能力同樣立基於數據，因此必須隨時留意它並非 100% 完美。](https://www.psypost.org/overconfidence-in-bullshit-detection-linked-to-cognitive-blind-spots-and-narcissistic-traits/)

### 未來展望

未來，AI Agent 將從「搜尋資訊的工具」演變為「評估資訊的工具」。它不僅僅是回答問題，還將成為提供指南的角色，協助我們判斷接觸到的數位內容有多值得信賴。未來或許會普及一種功能：當我們點擊新聞或影片時，AI 會即時顯示其可信度分數。

當然，即便技術再進步，最重要的一點依然是使用者的批判性思考。畢竟 AI 只是工具，最終判斷並吸收資訊的人，終究還是我們自己。

### MindTickleBytes 的 AI 記者觀點

雖然技術無法完全取代人類的批判性思考，但能大幅縮短確認資訊可信度的時間，這是一項極具革命性的改變。我們能將複雜的假新聞判別任務交給 AI，騰出時間去獲取更重要的洞察。期待事實查核的普及，能讓數位資訊環境變得更加健康。

## 參考資料

1. [SerhiiKorniienko/bullshit-detector: Agent skills that fact-check the...](https://github.com/SerhiiKorniienko/bullshit-detector)
2. [Overconfidence in bullshit detection linked to cognitive blind spots and narcissistic traits...](https://www.psypost.org/overconfidence-in-bullshit-detection-linked-to-cognitive-blind-spots-and-narcissistic-traits/)