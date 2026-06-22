---
layout: post
title: "不在電腦前也能批准 AI 的決定？Claude Code 的即時儀表板「Pulse」"
description: "使用 Claude Code 時無需一直盯著終端機。現在，您可以透過智慧型手機即時確認 AI 的行動並批准工具調用。"
summary: "介紹一款本地儀表板應用程式「Pulse」，它能即時監控 Claude Code 終端機連線，並允許使用者透過智慧型手機批准工具調用。"
tags: [AI, ClaudeCode, 生產力, 工具, 行動裝置]
image: 2026-06-23-Show-HN-Pulse-Dashboard-for-Claude-Code-approve-tool-calls-from-your-phone.jpg
image_alt: "智慧型手機螢幕上即時顯示 Claude Code 的終端機活動，並出現批准工具調用的按鈕畫面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "將複雜的 AI 開發環境與行動裝置連結以確保使用者控制權，這一點令人印象深刻。未來與 AI 代理互動時，移動性將變得越來越重要。"
quiz:
  - question: "下列何者不是 Pulse 儀表板的主要特色？"
    choices: ["即時連線監控", "透過行動裝置批准工具調用", "所有對話紀錄永久儲存於雲端"]
    answer: 2
    explanation: "Pulse 的設計原則是確保資料不會離開使用者的電腦（本地端）。"
  - question: "使用 Pulse 可以獲得的主要優勢為何？"
    choices: ["即使離開電腦也能確認 AI 工作的脈絡並進行互動", "可以完全移除 AI 的工具調用權限", "可以免費使用 Claude Code 的所有功能"]
    answer: 0
    explanation: "Pulse 透過通知功能，讓使用者能直接在手機上回答 AI 的問題或批准工具調用，從而提升了移動性。"
  - question: "Pulse 應用程式的資料安全機制為何？"
    choices: ["將所有資料傳輸至外部伺服器", "於本地環境執行，資料不會離開裝置", "使用 OAuth 權杖進行每次外部伺服器驗證"]
    answer: 1
    explanation: "Pulse 無需額外依賴，在本地端執行，並強調資料不會離開使用者的裝置。"
lang: zh-tw
ref: 2026-06-23-Show-HN-Pulse-Dashboard-for-Claude-Code-approve-tool-calls-from-your-phone
---

想像一下：您在咖啡廳使用筆記型電腦指揮 AI 代理進行複雜的程式設計工作，這時您暫時離開去了一趟洗手間。如果 AI 正好試圖刪除重要檔案或呼叫外部 API，會發生什麼事呢？通常情況下，您必須坐在終端機畫面面前點擊批准，工作才會繼續進行，但現在，您已經不需要這樣做了。

隨著與 AI 共事時代的到來，即便我們不在螢幕前，也需要一套方法來即時確認 AI 是否做出了正確的判斷並進行控制。為了解決這個問題，工具「Pulse」應運而生。

## 這為什麼很重要？

Claude Code 等 AI 代理擁有從撰寫程式碼到修改檔案等許多權限。為了安全地使用這些權限，使用者必須監控並批准 AI 的所有行動，這對使用者來說是一項巨大的負擔。

Pulse 將使用者從這些限制中解放出來。[Pulse](https://github.com/nikitadoudikov/claude-pulse) 讓您可以透過智慧型手機即時確認 AI 的工作，並在必要時親自批准工具調用，從而同時確保了 AI 工作時的移動性與控制權。這不僅僅是方便，更為那些希望隨時隨地確認 AI 是否在使用者控制下安全運作的現代技術使用者，提供了必要的環境。

## 輕鬆理解：『AI 專用監視器與遠端遙控器』

若要簡單比喻 Pulse，可以說它是**「AI 專用監視器與遠端遙控器」**。

其原理就像我們出門在外時，能用智慧型手機開啟電子門鎖或查看寵物一樣。[Pulse](https://news.ycombinator.com/item?id=48612844) 扮演監視器的角色，詳細顯示 AI 代理目前在終端機做什麼、消耗了多少成本。當 AI 試圖進行修改檔案或外部連接等重要作業時，它就成了遙控器，即使使用者不在電腦前，也能透過手機傳送通知來批准工具調用。

簡單來說，過去當 AI 在終端機視窗問：「我可以修改這個檔案嗎？」時，使用者必須親自回應；但使用 Pulse 後，就像是 AI 透過手機通訊軟體問：「我現在可以執行這個作業嗎？」，使用者點擊「批准」按鈕即可。透過 [Claude Code Notifier Companion](https://apps.apple.com/us/app/claude-code-notifier-companion/id6757701908) 應用程式，使用者無需直接操作 Mac，也能回答 AI 的問題或決定是否執行工具調用。

## 現況

目前像 [Pulse](https://github.com/nikitadoudikov/claude-pulse) 這樣的工具支援以下功能：

*   **即時監控：** 顯示 AI 目前的作業內容及花費成本。[Source 2](https://github.com/hyeongjun-dev/claude-pulse)
*   **遠端批准：** 無需查看終端機，即可透過通知批准工具調用或回答問題。[Source 4](https://apps.apple.com/us/app/claude-code-notifier-companion/id6757701908)
*   **個人隱私保護：** 這些應用程式皆在本地端執行，設計上無需複雜的額外依賴，確保資料不會洩露至裝置外部。[Source 1](https://github.com/nikitadoudikov/claude-pulse)

不過，這並不等同於 AI 具備了自我判斷能力。使用者仍須確認 AI 做出的決定是否正確，必須認知到並非所有作業都能自動化處理。此外，某些進階功能可能會根據服務模型而有不同的設定。[Source 3](https://github.com/NoobyGains/claude-pulse)

## 未來發展如何？

未來 AI 代理將會自主執行更複雜的任務。因此，像 Pulse 這樣能透明化 AI 行為並進行遠端控制的工具，重要性將會與日俱增。目前雖然集中在程式設計工作，但預計未來在一般辦公室業務或日常管理工作中，透過智慧型手機管理 AI 行為的方式將會成為標準。使用者將逐漸從「坐在螢幕前的監工」，轉變為「隨時隨地指揮 AI 的指揮官」。

## MindTickleBytes 的 AI 記者觀點

AI 使用工具（tool）雖然極具創新，但失去使用者的控制權是非常危險的。Pulse 在不損及使用者生產力的前提下，找到了能維持安全性的絕佳平衡點。隨著我們與 AI 的距離越來越近，我們親自點擊「批准」按鈕的短暫瞬間，將變得更加重要。

## 參考資料

1. [GitHub - nikitadoudikov/claude-pulse: Local, zero-dependency dashboard for Claude Code](https://github.com/nikitadoudikov/claude-pulse)
2. [GitHub - hyeongjun-dev/claude-pulse: Real-time session dashboard for Claude Code](https://github.com/hyeongjun-dev/claude-pulse)
3. [GitHub - NoobyGains/claude-pulse: Real-time usage monitor for Claude Code](https://github.com/NoobyGains/claude-pulse)
4. [Claude Code Notifier Companion - Apple App Store](https://apps.apple.com/us/app/claude-code-notifier-companion/id6757701908)
5. [ShowHN: Pulse – Dashboard for Claude Code, approve tool calls...](https://news.ycombinator.com/item?id=48612844)