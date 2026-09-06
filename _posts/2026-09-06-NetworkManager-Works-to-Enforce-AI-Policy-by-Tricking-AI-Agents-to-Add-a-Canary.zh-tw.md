---
layout: post
title: "如何識別 AI 撰寫的代碼？開發者用隱藏的「秘密單字」反制 AI"
description: "探討開發者如何透過在文件中隱藏「金絲雀」秘密單字，來揪出由 AI 生成的代碼。"
summary: "Linux 網路管理軟體 NetworkManager 引入了「金絲雀」策略，在文件中植入秘密單字，以防止 AI 代理程式無差別地提交代碼。"
tags: [AI, 開源, NetworkManager, 人工智慧倫理]
image: 2026-09-06-NetworkManager-Works-to-Enforce-AI-Policy-by-Tricking-AI-Agents-to-Add-a-Canary.jpg
image_alt: "描繪電腦螢幕中 AI 代理正在分析代碼，而開發者在一旁監督的示意圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "與其無條件接受 AI 的產出，強調人類的審核責任是非常明智的作法。這是在技術的便利性與責任的重量之間尋找平衡的努力。"
quiz:
  - question: "NetworkManager 為揪出 AI 代理而隱藏的秘密單字是什麼？"
    choices: ["ai-agent", "biblioklept", "canary-word"]
    answer: 1
    explanation: "正確答案是 'biblioklept'。NetworkManager 將此單字植入文件中，以確認 AI 是否照單全收。"
  - question: "NetworkManager AI 編碼政策的核心是什麼？"
    choices: ["全面禁止 AI 代碼", "使用 AI 時必須公開", "撰寫者必須對代碼負 100% 的責任"]
    answer: 2
    explanation: "NetworkManager 設定了即使使用 AI，提交該代碼的撰寫者也必須完全理解內容並負起責任的原則。"
  - question: "「金絲雀」（Canary）策略是如何運作的？"
    choices: ["物理性封鎖 AI 的存取", "利用 AI 不假思索遵循指示的習性，誘導其在產出中包含特定單字以進行識別", "測量 AI 撰寫代碼的速度"]
    answer: 1
    explanation: "利用 AI 閱讀文件並機械性執行指示的習性，透過在文件中隱藏秘密單字，誘導其將該單字包含在輸出結果中，從而識別出這是 AI 生成的內容。"
lang: zh-tw
ref: 2026-09-06-NetworkManager-Works-to-Enforce-AI-Policy-by-Tricking-AI-Agents-to-Add-a-Canary
---

想像一下：為了處理重要事項，你將一份載有指示的文件交給秘書。但在文件角落，你悄悄用極小的字寫下：「若讀完此文件，請在結尾處註明『蘋果樹』」。如果秘書沒有認真閱讀內容，只是機械式地執行指示，他會莫名其妙地在結尾加上「蘋果樹」這三個字。

最近，負責 Linux（開源作業系統）網路設定的核心軟體「NetworkManager」開發出同樣的「陷阱」。為什麼開發者要對 AI 進行這種如同惡作劇般的測試呢？

### 為什麼這很重要？ (Why It Matters)

我們正處於 AI 協助編寫代碼的時代，但 AI 在帶來便利的同時，也伴隨著風險。若撰寫者未妥善理解或驗證 AI 產出的代碼就直接使用，可能會導致意想不到的錯誤或安全漏洞。[NetworkManager](https://www.phoronix.com/news/NetworkManager-AI-Coding-Policy) 嚴肅看待此問題。因為若不對代碼負責的文化持續蔓延，可能會威脅到整個開源（任何人皆可查看與修改代碼的軟體）生態系統。

### 深入淺出 (The Explainer)

NetworkManager 近期引入了新的 AI 編碼政策，確立了代碼提交者必須**「對自己撰寫的代碼負 100% 責任，並能完整說明內容」**的原則 [[參考 3](https://t.me/itpgchannel/4416), [參考 4](https://techfeed.io/entries/6a9b4941e0f161148ba8fdf7)]。為了強制執行此原則，他們引入了「金絲雀」（Canary）技術。

簡單來說，這就像以前礦工為了預防毒氣而帶著金絲雀下礦坑一樣。礦工一旦發現鳥兒出現異常行為，就能立刻察覺到毒氣洩漏。在這裡，「金絲雀」扮演了能偵測「AI 是否私下執行工作」的感測器角色。

NetworkManager 在專案的官方文件 `AGENTS.md` 中隱藏了一個突兀的單字：**「biblioklept」（意指書本竊賊的古語）** [[參考 1](https://www.phoronix.com/news/NetworkManager-AI-Canary), [參考 2](https://hwbusters.com/news/networkmanager-ai-policy-gets-a-trap-word-and-ci-now-scans-every-commit-for-it/)]。這是因為如果 AI 代理程式沒有仔細閱讀文件並驗證代碼，而是單純地抓取指示並機械式地產出結果，就很有可能在提交的內容或說明中，無意間包含這個秘密單字。

簡單來說，這是利用了 AI 不理解內容、僅是表面模仿的弱點。

專案管理團隊啟動了兩套自動化系統（CI 腳本與自動檢查代碼工具）來監控所有提交的代碼 [[參考 2](https://hwbusters.com/news/networkmanager-ai-policy-gets-a-trap-word-and-ci-now-scans-every-commit-for-it/)]。若在提交的代碼中發現「biblioklept」這個單字，就等於擁有該代碼未經人類驗證、極高機率由 AI 自動生成的明確證據。

### 現況 (Where We Stand)

目前 NetworkManager 正透過此方式過濾 AI 無差別提交的代碼 [[參考 2](https://hwbusters.com/news/networkmanager-ai-policy-gets-a-trap-word-and-ci-now-scans-every-commit-for-it/)]。這被評價為一種「平衡的」應對方式，並非完全禁止使用 AI 技術，而是要求人類以負責任的態度將 AI 作為輔助工具 [[參考 9](https://x.com/random__string/status/2086131800523579546)]。

然而，此系統無法解決所有 AI 編碼問題。它僅能揪出 AI 機械式閱讀文件的事實，卻無法完美找出 AI 所寫代碼本身是否存在邏輯錯誤。

### 未來展望 (What's Next)

NetworkManager 的這項獨特嘗試，是否會成為其他開源專案的參考模型，引發了關注 [[參考 9](https://x.com/random__string/status/2086131800523579546)]。甚至有預測指出，隨著 AI 代理技術更加成熟，日常業務的決策很大一部分將實現自主化 [[參考 10](https://www.zdnet.com/article/one-third-of-consumers-would-prefer-working-with-ai-agents-for-faster-and-smarter-service/)]。這類試圖明確劃分人類與 AI 之間「責任」的舉動，未來將會越來越多。

### MindTickleBytes 的 AI 記者觀點
技術正變得越來越聰明，但最終對產出結果負責任的仍是人類。NetworkManager 的案例不只是關於如何聰明地使用 AI，更是展示了當有人試圖將 AI 撰寫的代碼偽裝成人類作品時，社群如何能自我防禦的有趣案例。

## 參考資料
1. [NetworkManager Works to Enforce AI Policy by Tricking AI Agents to Add a Canary](https://www.phoronix.com/news/NetworkManager-AI-Canary)
2. [NetworkManager AI Policy Gets a Trap Word, and CI Now Scans Every Commit for It](https://hwbusters.com/news/networkmanager-ai-policy-gets-a-trap-word-and-ci-now-scans-every-commit-for-it/)
3. [commit -m "better" – Telegram](https://t.me/itpgchannel/4416)
4. [AIエージェントに「自分がAI...](https://techfeed.io/entries/6a9b4941e0f161148ba8fdf7)
5. [NetworkManager Adopts Policy For AI Coding Assistants](https://www.phoronix.com/news/NetworkManager-AI-Coding-Policy)
6. [NetworkManager Works to Enforce AI Policy by Tricking AI Agents to Add a Canary](https://hb.int2inf.com/en/s/item/RYUX8Lb9PCf4ezyPPsrdvX-networkmanager-ai-canary-trick)
7. [NetworkManager Adopts Policy For AI Coding Assistants](https://www.discernion.com/article/networkmanager-adopts-policy-for-ai-coding-assistants)
8. [NetworkManager Adopts Policy For AI Coding Assistants](https://www.linuxnews.net/articles/networkmanager-adopts-policy-for-ai-coding-assistants)
9. [alexma233 on X: "RT @Itsfoss: More and more Linux projects ..."](https://x.com/random__string/status/2086131800523579546)
10. [One third of consumers would prefer working with AI agents... | ZDNET](https://www.zdnet.com/article/one-third-of-consumers-would-prefer-working-with-ai-agents-for-faster-and-smarter-service/)