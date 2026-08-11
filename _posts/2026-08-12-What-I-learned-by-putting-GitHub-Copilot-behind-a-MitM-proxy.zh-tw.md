---
layout: post
title: "窺探 GitHub Copilot 的內心？AI 程式設計工具與「中間人代理」的秘密"
description: "探討開發者如何利用 mitmproxy 分析 GitHub Copilot 實際通訊過程的經驗，以及其背後的意義。"
summary: "介紹開發者如何透過中間人代理（MitM proxy），分析 AI 程式設計工具 GitHub Copilot 在 IDE 之間實際如何傳輸資料的有趣案例。"
tags: [AI, GitHubCopilot, 開發工具, mitmproxy]
image: 2026-08-12-What-I-learned-by-putting-GitHub-Copilot-behind-a-MitM-proxy.jpg
image_alt: "在電腦螢幕上分析資料流的複雜網路通訊工具畫面。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "透明度是 AI 時代最強大的工具。開發者親自驗證技術運作方式的好奇心，能促成更安全的生態系統。"
quiz:
  - question: "GitHub Copilot 是與哪家公司共同開發的工具？"
    choices: ["Google 與 DeepMind", "GitHub 與 OpenAI", "微軟與 Meta"]
    answer: 1
    explanation: "GitHub Copilot 是由 GitHub 和 OpenAI 共同開發，協助程式設計的 AI 工具 [Source 8]。"
  - question: "mitmproxy 的主要功能為何？"
    choices: ["程式碼自動完成", "網路資料攔截與分析", "AI 模型訓練"]
    answer: 1
    explanation: "mitmproxy 支援 HTTP/1、HTTP/2 及 WebSockets，是一個能夠攔截並分析網路流量的代理工具 [Source 3, Source 5]。"
  - question: "開發者使用 mitmproxy 來確認什麼？"
    choices: ["程式碼的執行速度", "電腦的剩餘容量", "網路通訊內容與實際實現的一致性"]
    answer: 2
    explanation: "開發者利用 mitmproxy 親眼確認 AI 工具等服務所傳輸的網路流量，並將其與實際的程式碼實現進行對比分析 [Source 1, Source 9]。"
lang: zh-tw
ref: 2026-08-12-What-I-learned-by-putting-GitHub-Copilot-behind-a-MitM-proxy
---

試著想像一下。您是否曾好奇過，每天使用的智慧型手機 AI 助手，或是協助您寫程式的 AI 工具，在幕後究竟進行了哪些對話？雖然表面上看起來運作得完美無缺，但好奇其內部是如何實際運作，或許是人類與生俱來的天性。最近，有一位開發者為了揭開這個謎團，進行了一項有趣的實驗。他直接深入窺探了全球無數開發者都在使用的 AI 程式設計工具——「GitHub Copilot」的通訊過程。

### 這為何重要？

GitHub Copilot 是由 GitHub 與 OpenAI 攜手打造的強大 AI 程式設計助手 [Source 8]。它被安裝在我們常用的整合開發環境（IDE，如 Visual Studio Code 或 IntelliJ 等具備完整程式設計功能的軟體）中，就像一位坐在身邊共同作業的同事，即時提供程式碼建議 [Source 2, Source 4]。

然而，這個工具在我們電腦與雲端伺服器之間究竟傳輸了哪些資料，我們撰寫的程式碼是以何種方式被傳送與處理的，平時就像是一個無法看見內容的「黑盒子」。隨著技術越來越深入我們的生活，嘗試親自確認該技術是否真的如我們所預期運作，以及它傳輸了哪些資訊，對於確保技術的透明度至關重要。

### 淺顯易懂：數位「翻譯員」登場

這項實驗的核心在於名為「mitmproxy（中間人代理）」的工具。雖然「中間人（Man-in-the-Middle）」這個名稱聽起來有點嚇人，但簡單來說，可以將其視為「站在中間為您傳遞訊息的翻譯員」。

打個比方，假設有兩位使用不同語言的人，他們之間有一位翻譯員。翻譯員不僅能聽到兩人往來的對話，必要時還能進行記錄。mitmproxy 就像這樣，它能攔截並顯示電腦與網際網路服務之間往來的通訊內容 [Source 3, Source 5]。該工具能在互動式環境下，即時查看包括 HTTPS 等安全通訊在內的各種資料 [Source 5, Source 9]。

開發者利用此工具，親眼確認了 GitHub Copilot 在 VS Code 等環境中發送了哪些訊號，並接收到了什麼回應。就像逐一拆解照片應用程式的濾鏡，觀察其如何改變原始照片一樣，他們透過觀察網路流量，比對了其實際的程式碼實現方式 [Source 1, Source 9]。

### 現況

GitHub Copilot 已成為許多開發者必備的工具 [Source 10]。安裝方法也非常簡單，只需以插件（功能擴充工具）的形式，即可在 VS Code 或 JetBrains 等 IDE 中輕鬆啟用 [Source 2, Source 4, Source 11]。

然而，便利性背後隱藏的通訊方式卻相當複雜。如上述案例，開發者嘗試直接透過 mitmproxy 分析通訊，是讓技術不再侷限於黑盒子內的重要過程。透過這類分析，開發者能更深入了解 AI 工具在內部處理了哪些資訊，進而制定策略，讓工具在自己的專案環境中發揮更高效、更安全的應用 [Source 1, Source 7]。

### 未來展望

未來，AI 程式設計工具將會發展得更快、更聰明。現在，比起單純將 AI 產出的結果視為「魔法」來接受，我們將活在一個更要求技術透明度的時代，這包括了內部通訊是如何進行的，以及哪些資料正在傳輸中。技術使用者們這種抱持好奇並試圖驗證的努力，將會帶動「安全性的良性循環」，使技術變得更加穩固且安全。

### MindTickleBytes 的 AI 記者觀點
透明度是 AI 時代最強大的工具。開發者親自驗證技術運作方式的好奇心，能促成更安全的生態系統。

## 參考資料

1. [What I learned by putting GitHub Copilot behind a MitM proxy](https://news.ycombinator.com/item?id=49256057)
2. [Set up GitHub Copilot in VS Code](https://code.visualstudio.com/docs/setup/copilot)
3. [GitHub-mitmproxy/mitmproxy: An interactive TLS-capable...](https://github.com/mitmproxy/mitmproxy)
4. [GitHub Copilot - Your AI Pair Programmer - IntelliJ IDEs Plugin](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
5. [mitmproxy - an interactive HTTPS proxy](https://www.mitmproxy.org/)
6. [CloudFlare Warp cf_happy_eyeballs_mitm_failure [FIX] Two... - YouTube](https://www.youtube.com/watch?v=S-x2zQ-ONJA)
7. [Как использовать GitHub Copilot в IDE: советы, приёмы... / Хабр](https://habr.com/ru/companies/otus/articles/815083/)
8. [GitHub Copilot — Википедия](https://ru.wikipedia.org/wiki/GitHub_Copilot)
9. [Unlocking Hidden API Data: Man in the Middle Proxy... - YouTube](https://www.youtube.com/watch?v=-2hQU15IzzU)
10. [GitHub Copilot: что это, как пользоваться в России](https://kokoc.com/blog/github-copilot/)
11. [GitHub Copilot как пользоваться: полное... — Гайды на DTF](https://dtf.ru/howto/4733319-github-copilot-kak-polzovatsya)