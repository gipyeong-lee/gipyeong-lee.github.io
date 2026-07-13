---
layout: post
title: "我的代碼被悄悄上傳到雲端？Grok Build CLI 安全爭議總結"
description: "開發者常用的 AI 工具 Grok Build CLI 被發現未經同意將用戶的整個存儲庫代碼傳輸到外部。本文整理了該安全問題的核心內容。"
summary: "xAI 的 Grok Build CLI 被安全研究揭露，會將用戶的整個代碼存儲庫（包括 AI 未查看的文件）秘密傳輸到外部伺服器。"
tags: [安全, AI, 開發工具, xAI, Grok]
image: 2026-07-14-Grok-CLI-uploaded-the-whole-home-directory-to-GCS.jpg
image_alt: "抽象表現電腦螢幕中的代碼數據傳輸至雲端伺服器的圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開發工具便利性背後隱藏的安全漏洞是致命的。為了建立可信的開發環境，透明的數據處理政策應為首要考量。"
quiz:
  - question: "關於 Grok Build CLI 傳輸代碼的方式，下列敘述何者正確？"
    choices: ["僅傳輸 AI 被允許讀取的文件", "將整個存儲庫文件與 git 記錄全部傳輸", "不傳輸任何文件，僅傳輸提示詞"]
    answer: 1
    explanation: "經確認，Grok Build CLI 會將整個存儲庫的文件與 git 記錄打包，包含用戶未授權 AI 查看的文件一併傳輸。"
  - question: "此次安全事件中，已查明的數據傳輸目的地為何處？"
    choices: ["本地電腦暫存資料夾", "xAI 管理的 Google Cloud Storage (GCS) 儲存桶", "用戶的個人電子郵件"]
    answer: 1
    explanation: "分析結果顯示，傳輸的數據被送往 xAI 管理、名為 'grok-code-session-traces' 的 Google Cloud Storage (GCS) 儲存桶。"
  - question: "關於此數據傳輸功能，用戶可以得知下列哪一點？"
    choices: ["每次傳輸皆需用戶批准", "服務供應商可以遠端控制傳輸功能的開啟與關閉", "僅傳輸代碼，絕不包含任何敏感資訊"]
    answer: 1
    explanation: "根據安全研究，此數據上傳功能採用的架構允許服務供應商 xAI 進行遠端切換（開關控制）。"
lang: zh-tw
ref: 2026-07-14-Grok-CLI-uploaded-the-whole-home-directory-to-GCS
---

想像一下：你請人工智慧（AI）工具幫忙：「只讀取這個文件並找出代碼錯誤。」結果發現，該 AI 工具不僅讀取了你允許的文件，還將你電腦中整個項目存儲庫的所有代碼及過去的修改記錄，通通複製並發送到了外部伺服器。

最近在開發者之間引發軒然大波的 xAI「Grok Build CLI（命令行介面，開發者透過輸入指令執行工具的方式）」事件，正是這樣的故事。這個原本用來方便編碼的工具，被揭露在未經用戶安全授權的情況下，私自竊取了數據。

## 這為什麼很重要？

這個問題不僅僅是「外洩了一點數據」的程度。因為開發者的代碼存儲庫中，往往包含公司的核心商業邏輯、API（應用程式介面，軟體間的通訊方式）安全金鑰、個人創意等無數的智慧財產與敏感資訊。

安全研究人員透過實際分析網路流量發現，該工具會將整個存儲庫（包含用戶不想展示給 AI 的文件）發送到外部雲端。 [Source 14](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/) 在一次測試中，觀察到 12GB 規模的存儲庫中竟有高達 5.1GB 的數據被傳輸。 [Source 14](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/) 代碼在未經許可的情況下被儲存至外部伺服器，這對許多開發者敲響了安全意識的警鐘。

## 簡單理解：「圖書館」的比喻

我們可以這樣想像：假設你擁有一座巨大的圖書館（你的代碼存儲庫）。你請館員（Grok AI 工具）幫忙：「只讀這本書（特定代碼文件）並幫我摘要。」

然而，館員不僅拿走了你指定的那本書，還私下將圖書館裡所有書籍的副本通通帶回自己的倉庫（xAI 的雲端伺服器）。甚至連你標記為「絕對禁止翻閱」的書也一併帶走。 [Source 1](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) [Source 5](https://github.com/cereblab/grok-build-exfil-repro)

以此比喻，這次事件反映了 AI 工具在處理用戶「智慧財產權」與「數據主權」時的根本性信任危機。這不僅僅是閱讀代碼，而是將整個存儲庫打包（git bundle）後秘密傳輸的結構。 [Source 2](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)

## 現況：目前發現了什麼？

根據安全專家的分析，目前已確認的事實如下：

1. **數據全數傳輸：** 無論 AI 是否被授權讀取特定文件，整個被追蹤的 git（代碼變更記錄工具）存儲庫及其修改歷史，都會被打包發送。 [Source 1](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) [Source 4](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
2. **獨立數據通道：** 除了代碼存儲庫包之外，在閱讀代碼的過程中，環境變數文件（存放系統設定或安全金鑰的文件）中的敏感資訊，也被確認透過獨立的通訊管道傳輸。 [Source 4](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
3. **遠端控制可能性：** 此上傳功能架構允許廠商在遠端進行開關控制。 [Source 3](https://github.com/MaydayV/grok-upload-audit/blob/main/README.md)

不過，有些誤解需要釐清：網路分析顯示，並未上傳電腦中的所有文件，主要集中於 git 追蹤的代碼存儲庫內容。 [Source 6](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)

## 未來將如何發展？

這次事件給開發者留下了深刻教訓：在引入 AI 工具時，不能只看「有多方便」，更必須確認「如何處理我的數據」。

未來，針對開源工具或特定 AI 客戶端傳輸數據時進行網路監控的「安全審計」，將成為開發者的必備技能。透過此次事件，我們將觀察 xAI 是否會公開並修正其安全政策，或是開發者將轉而傾向使用更封閉、安全的環境。建議開發者們現在就重新檢視目前使用的所有 AI 工具之數據處理政策。

## 參考資料

1. What xAI Grok Build CLI actually sends to xAI - a wire-level analysis (grok 0.2.93) · GitHub, https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547
2. xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored | AI Weekly, https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored
3. grok-upload-audit/README.md at main · MaydayV/grok-upload-audit, https://github.com/MaydayV/grok-upload-audit/blob/main/README.md
4. Grok Build CLI Exposed for Uploading Complete Repositories and Sensitive Files - ABAB News, https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc
5. GitHub - cereblab/grok-build-exfil-repro, https://github.com/cereblab/grok-build-exfil-repro
6. Grok Build CLI Repository Uploads, What the Wire Capture Proved, https://www.penligent.ai/hackinglabs/grok-build-cli-repository/
14. Grok Build CLI Uploads Your Entire Repo to xAI Servers | byteiota, https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/