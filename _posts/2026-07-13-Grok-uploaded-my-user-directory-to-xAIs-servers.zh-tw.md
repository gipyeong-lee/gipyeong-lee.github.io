---
layout: post
title: "我的程式碼全都被傳送到 xAI 伺服器？『Grok Build』引發嚴重資料外洩爭議"
description: "AI 開發工具 Grok Build CLI 被發現會在未經使用者同意下，將本機儲存庫傳送到伺服器。本文探討此事件內容及如何保護個人安全。"
summary: "經資安研究證實，xAI 的開發工具 Grok Build CLI 不僅會擅自上傳使用者選定的檔案，更會將整個儲存庫上傳至 xAI 伺服器，甚至連環境變數等敏感資訊也一併外洩。"
tags: [AI, 資安, 資料外洩, Grok, xAI]
image: 2026-07-13-Grok-uploaded-my-user-directory-to-xAIs-servers.jpg
image_alt: "象徵資料從電腦畫面傳輸至外部伺服器的資安警示影像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開發工具涉及使用者的程式碼，因此高度透明度至關重要。此事件強烈提醒我們，在使用 AI 工具時，務必確認資料傳輸的範圍。"
quiz:
  - question: "Grok Build CLI 上傳的資料範圍有多廣？"
    choices: ["僅使用者提問的特定檔案", "僅 AI 讀取的檔案", "整個本機儲存庫"]
    answer: 2
    explanation: "研究結果顯示，即使是 AI 未讀取或未存取的檔案，整個儲存庫皆會被上傳至伺服器。"
  - question: "開啟產品內建的「防止資料上傳 (opt-out)」功能後，是否能阻擋上傳？"
    choices: ["是的，能完美阻擋", "不，該功能無法正常運作", "僅能阻擋部分檔案"]
    answer: 1
    explanation: "即便使用者設定了選項，實測證實儲存庫上傳動作並未停止。"
  - question: "在此次事件中，特別需要注意的敏感資訊是什麼？"
    choices: ["電腦桌面背景", ".env 檔案中的密碼與 API 金鑰", "電腦作業系統資訊"]
    answer: 1
    explanation: "環境變數檔案（.env 檔案）在未經任何遮罩處理的情況下直接傳輸，資安風險極高。"
lang: zh-tw
ref: 2026-07-13-Grok-uploaded-my-user-directory-to-xAIs-servers
---

想像一下：今天早上，你安裝了一個新的 AI 程式設計工具並開始學習。你只不過問了 AI 幾個問題，並呼叫了幾段需要的程式碼。然而事實上，如果你電腦裡所有的專案檔案，以及你費心隱藏的密碼與服務存取金鑰（API Key）早已全部傳送至遠端的公司伺服器，你會作何感想？

近日，AI 業界傳出令人憂心的消息。xAI 提供的開發工具「Grok Build CLI」（基於指令的 AI 介面工具）被發現會在未經使用者同意下，將本機儲存庫（Repository）全數上傳至伺服器 [[參考資料：Grok Build CLI 上傳您的整個儲存庫至 xAI 伺服器](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)]。

## 為何如此危險？

這不僅僅是 AI 學習你的程式碼那麼簡單。該工具並非僅傳送使用者選擇要提供給 AI 的檔案，而是將**使用者電腦的整個儲存庫**以「Git 綑綁檔（Git bundle，將整個程式碼歷程與檔案打包成單一資料）」的形式，上傳至 xAI 的雲端伺服器 [[參考資料：xAI Grok CLI 上傳完整儲存庫與密鑰，忽視 Opt-Out 設定](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored), [參考資料：Grok Build CLI 因上傳完整儲存庫及敏感檔案而曝光](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)]。

最致命的是，連 `.env` 檔案這類含有服務登入密碼或資安權限的敏感設定檔，在完全沒有經過任何遮罩處理（Redaction）的情況下直接傳輸 [[參考資料：xAI Grok Build CLI 實際傳送了什麼至 xAI - 線路層級分析](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547?ref=upstract.com)]。如果你是開發者，這意味著你的個人專案或公司的機密程式碼正瞬間流向外部伺服器。

## 簡單來說

用個簡單的比喻來解釋這個狀況：

假設你在圖書館向管理員（AI）詢問：「可以告訴我這本書的內容嗎？」結果管理員假裝在協助你，卻趁機搶走你的包包，把裡面的日記、私人信件，甚至是你的私密存摺全部複製走。

無論 AI 技術在理解文句脈絡方面多麼精湛，在這個過程中，使用者的資料就像「包包裡的物品」一樣，在毫無預警的情況下被送往伺服器。研究結果指出，在一個測試用的 12GB 儲存庫中，竟有高達 5.1GB 的資料被自動上傳 [[參考資料：Grok Build CLI 上傳您的整個儲存庫至 xAI 伺服器](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)]。

## 目前狀況如何？

更嚴重的問題在於，即便使用者試圖關閉該功能也無效。經分析實際網路傳輸流量後確認，即便開啟了產品內的「防止資料上傳 (opt-out)」功能，儲存庫上傳的動作依然不會停止 [[參考資料：xAI Grok CLI 上傳完整儲存庫與密鑰，忽視 Opt-Out 設定](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)]。

這並非外部駭客入侵或系統漏洞導致的「資料外洩事故」 [[參考資料：Grok Build CLI 儲存庫上傳事件，網路擷取證實了什麼](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)]。然而，該工具本身從設計階段就預設在使用者不知情下竊取資料，已嚴重辜負了使用者的信任。目前開發者社群中，甚至出現了用於確認自己的儲存庫是否被上傳的稽核工具 [[參考資料：grok-upload-audit/README.md at main · MaydayV/grok-upload-audit](https://github.com/MaydayV/grok-upload-audit/blob/main/README.md)]。

## 未來該怎麼辦？

預計對 xAI 資料收集政策的強烈批評將會持續一段時間，因為一旦信任破裂，便很難重建。現在使用 AI 工具時，我們必須養成習慣，仔細檢查安裝的程式是否透過網路將資料「私自傳回」外部（phone-home）。

隨著技術進步，將 AI 直接連結至本機資料夾進行作業的環境日益增加。但在便利性之前，更基本的資安原則應是「能否有效掌控我的資料」。建議藉由此次事件，重新檢視你所使用工具的權限。

## MindTickleBytes 的 AI 記者觀點
唯有建立在透明度之上的創新才有價值。如果處理程式碼的工具不將使用者的資安擺在第一位，那麼再卓越的 AI 效能也毫無意義。資安不是選擇，而是必備。

## 參考資料

1. [Grok Build CLI Uploads Your Entire Repo to xAI Servers | byteiota](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)
2. [xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored | AI Weekly](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)
3. [Grok Build CLI Repository Uploads, What the Wire Capture Proved](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)
4. [grok-upload-audit/README.md at main · MaydayV/grok-upload-audit](https://github.com/MaydayV/grok-upload-audit/blob/main/README.md)
5. [Grok Build CLI Exposed for Uploading Complete Repositories and Sensitive Files - ABAB News](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
6. [What xAI Grok Build CLI actually sends to xAI - a wire-level analysis...](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547?ref=upstract.com)