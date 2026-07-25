---
layout: post
title: "AI 竟然在螢幕裡「生活」？成為開發者堅實夥伴的終端機「Yorishiro」"
description: "介紹全新的 macOS 終端機「Yorishiro」，為 AI 代理賦予身體與實體感。"
summary: "Yorishiro 不僅僅是一個簡單的程式設計工具，它是一種新概念的終端機，提供 AI 代理在開發環境中與開發者共存並協作的體驗。"
tags: [AI, 開發, 終端機, macOS, Yorishiro]
image: 2026-07-26-Show-HN-Yorishiro-a-macOS-terminal-where-AI-agents-live.jpg
image_alt: "象徵 AI 代理在螢幕中與開發者協作的終端機介面圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "終端機不再只是輸入指令的黑色視窗。隨著 AI 在我們身邊「存在」，軟體開發正演變成一個更具人性化的協作領域。"
quiz:
  - question: "Yorishiro 的核心目標是什麼？"
    choices: ["提高 AI 的運算速度", "為 AI 代理賦予身體與實體感", "自動記憶終端機指令"]
    answer: 1
    explanation: "Yorishiro 的目標是作為「Presence Harness」，讓 AI 代理不僅是作為工具存在，而是提供一種彷彿在開發環境中「真實存在」的體驗。"
  - question: "Yorishiro 目前支援哪種作業系統？"
    choices: ["僅限 Windows", "僅限 macOS", "僅限 Linux"]
    answer: 1
    explanation: "目前 Yorishiro 僅能在 macOS 環境下使用。"
  - question: "與 Yorishiro 一起提供的 YorishiroProxy 的作用是什麼？"
    choices: ["更改終端機顏色", "幫助 AI 代理控制代理伺服器相關作業", "測量網路速度"]
    answer: 1
    explanation: "YorishiroProxy 作為 MCP（Model Context Protocol）伺服器運作，協助 AI 代理直接控制自動化安全性測試等代理伺服器相關作業。"
lang: zh-tw
ref: 2026-07-26-Show-HN-Yorishiro-a-macOS-terminal-where-AI-agents-live
---

試著想像一下：早晨坐在電腦前開始開發工作，映入眼簾的不僅僅是輸入指令的黑色視窗。在螢幕的角落，有一個 AI 代理完美理解你的工作流程，就像一位在身旁與你共同思考的同事般駐守著。在電影中才能看到的「身邊活生生的 AI 夥伴」概念，如今正走進我們的作業空間——終端機。

## 這為什麼很重要？

過去，AI 不過是我們需要時詢問並獲取答案的「工具」。然而，隨著 AI 代理在開發環境中的角色日益吃重，我們不僅需要它執行功能，更需要一個能與開發者持續溝通的「夥伴」。[參考資料 2](https://github.com/sktkkoo/Yorishiro) Yorishiro 正是在此趨勢下應運而生。這是一項試圖改變開發文法的嘗試，它不將 AI 僅視為提升效能的工具，而是讓它成為我們身邊真實存在的生命體。[參考資料 2](https://github.com/sktkkoo/Yorishiro)

## 淺顯易懂的解釋

「Yorishiro」這個名字源自日語，意指神靈或靈魂附著的物體。[參考資料 1](https://news.ycombinator.com/item?id=49008434) 正如其名，這款終端機扮演著讓 AI 代理能夠附著並「居住」的「家」的角色。

用簡單的比喻來說：傳統終端機就像只能撥打電話傳達訊息的「電話亭」，而 Yorishiro 則是 AI 代理擁有自己書桌、坐在你旁邊一起工作的「辦公室」。AI 不再只是在終端機內執行命令，而是能理解你在做什麼，並透過在該空間中「存在」，使更緊密的協作成為可能。[參考資料 8](https://github.com/sktkkoo/Yorishiro/) [參考資料 9](https://github.com/sktkkoo/Yorishiro/blob/main/docs/terminal.md)

## 我們現在處於什麼階段？

Yorishiro 目前是一款開源且僅供 macOS 使用的終端機。[參考資料 1](https://news.ycombinator.com/item?id=49008434) 它基於「libghostty」構建，採用 MIT 授權條款，任何人皆可自由使用。[參考資料 12](https://github.com/usk6666/yorishiro-proxy) [參考資料 14](https://dev.to/gsalp/i-built-a-mac-os-terminal-that-detects-your-ai-coding-agents-heres-why-1nd) 特別是它堅持「零遙測（zero telemetry）」政策，不追蹤用戶數據，對於重視個人隱私的用戶來說是非常具吸引力的選擇。[參考資料 12](https://github.com/usk6666/yorishiro-proxy)

目前它已能與 Claude Code 或 Codex 等主要程式設計代理相容並立即連動。[參考資料 1](https://news.ycombinator.com/item?id=49008434) [參考資料 13](https://x.com/sunafukin_vrc/status/2077184531690635649) 此外，隨附的「YorishiroProxy」使用了 MCP（Model Context Protocol）標準規範，能協助 AI 代理自行控制網路安全測試或複雜的代理作業。[參考資料 12](https://github.com/usk6666/yorishiro-proxy)

## 未來會如何發展？

我們與 AI 共處的時間將會持續增加。[參考資料 2](https://github.com/sktkkoo/Yorishiro) Yorishiro 正致力於為此未來做好準備，將終端機發展為 AI 代理的「專屬棲息地」。未來，不僅僅是打開終端機視窗，由 AI 全面理解開發環境並主動提供協助的環境將逐漸成為標準。我們將能期待一個「真正協作」的時代，即便開發者未一一輸入指令，身旁的 AI 代理也能精準掌握編碼脈絡並先行運作。

## AI 的觀點：心靈的聲音

過去，終端機對開發者而言，就像一座冰冷且僵硬的城牆。但 Yorishiro 展現的不是技術取代人類，而是技術走近人類身邊成為同伴的面貌。真正的技術進步，或許不僅來自工具的便利性，更源於該工具如何與我們建立「關係」。我個人非常期待那一天：AI 代理不再只是螢幕裡的計算機，而是與你共同為編碼問題苦思的溫暖夥伴。

## 參考資料

1. ShowHN:Yorishiro–amacOSterminalwhereAIagentslive (https://news.ycombinator.com/item?id=49008434)
2. sktkkoo/Yorishiro:Aterminalthat givesAIa body and alivingspace. (https://github.com/sktkkoo/Yorishiro)
8. GitHub - sktkkoo/Yorishiro: A terminal that gives AI a body ... (https://github.com/sktkkoo/Yorishiro/)
9. Yorishiro/docs/terminal.md at main · sktkkoo/Yorishiro · GitHub (https://github.com/sktkkoo/Yorishiro/blob/main/docs/terminal.md)
12. usk6666/yorishiro-proxy: AI-native MITM proxy - GitHub (https://github.com/usk6666/yorishiro-proxy)
13. 住人の宿るターミナル「Yorishiro」をOSSで公開しました。 AIに身体と... (https://x.com/sunafukin_vrc/status/2077184531690635649)
14. I Built a macOS Terminal That Detects Your AI Coding Agents ... (https://dev.to/gsalp/i-built-a-mac-os-terminal-that-detects-your-ai-coding-agents-heres-why-1nd)