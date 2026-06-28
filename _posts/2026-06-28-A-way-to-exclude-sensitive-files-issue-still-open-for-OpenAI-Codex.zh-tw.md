---
layout: post
title: "我的電腦密碼會被 AI 偷看嗎？OpenAI Codex 的敏感檔案存取問題"
description: "開發者使用的 OpenAI 代碼編寫 AI——Codex，有沒有辦法不讓它隨意讀取我珍貴的私密金鑰或環境設定檔呢？為您整理目前討論中的安全性議題。"
summary: "OpenAI Codex CLI 自動存取開發者敏感檔案的問題持續引發討論，目前官方尚未提供原生的全面封鎖功能，開發者需提高警覺。"
tags: [AI安全, 開發工具, OpenAI, Codex, 資料隱私]
image: 2026-06-28-A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex.jpg
image_alt: "電腦螢幕中顯示 AI 編碼工具正在分析檔案，並伴隨著鎖頭圖示的圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "當便利性凌駕於安全之上時，事故就會發生。在官方提供排除功能之前，使用者需要智慧地為自己築起安全壁壘。"
quiz:
  - question: "OpenAI Codex CLI 目前處理工作目錄內檔案的預設方式為何？"
    choices: ["每次皆需獲得使用者確認", "無需使用者確認即可進行讀取與修改", "無條件將所有檔案傳送至外部"]
    answer: 1
    explanation: "Codex 在預設授權模式下，可自動讀取並修改工作目錄內的檔案。"
  - question: "目前為了防止 Codex 存取敏感檔案（如 .env），最建議的臨時替代方案是？"
    choices: ["使用設定檔中的排除選項", "隔離沙盒環境或限制檔案權限", "刪除 AI 模型"]
    answer: 1
    explanation: "由於目前缺乏官方排除功能，現階段封鎖檔案存取權限或利用沙盒進行隔離是最佳作法。"
  - question: "Codex 將資訊傳送給 AI 模型的方式為何？"
    choices: ["僅傳送使用者選擇的檔案", "在工具執行結果中包含檔案內容並上傳", "完全不傳送任何檔案內容"]
    answer: 1
    explanation: "Codex 會上傳工具執行結果，在此過程中可能會包含已存取的檔案內容。"
lang: zh-tw
ref: 2026-06-28-A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex
---

想像一下：你將程式開發工作託付給聰明的 AI 助理後，便轉身去泡了一杯咖啡。AI 雖然出色地完成了你的代碼，但過程中它是否連你包含電子郵件密碼或 API 連線金鑰的 `.env` 檔案也一併讀取了？近期，開發者社群中針對 OpenAI 代碼 AI 工具「Codex」的這類安全漏洞引發了熱烈討論。

### 為何這件事很重要？

開發者在進行專案時，通常會將重要的連線資訊或安全金鑰存放在 `.env` 等檔案中。這些檔案如同「數位鑰匙」。然而，若輔助開發的 AI 工具 Codex 能夠讀取這些檔案，這便引發了隱憂——珍貴的個人資訊可能在開發者不知情的情況下，被納入 AI 模型的學習數據或傳送到外部伺服器。 [出處: Add ability to hide sensitive files from agent · Issue #85](https://github.com/openai/codex/issues/300/linked_closing_reference?reference_location=REPO_ISSUES_INDEX) Codex 在處理工具執行結果時，會採取將存取過的檔案內容一併上傳的方式，因此使用者需特別小心。 [出處: A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)

### 簡單易懂的解釋

打個比方，目前的 Codex 就像是一位「熱情的圖書館員」。理應只拿取我指定的代碼檔案，但這位館員因為太過積極，連我藏在書架角落的私密檔案也全都翻閱了一遍。

更嚴重的問題在於，目前 Codex 並沒有提供官方功能，讓我們能預先設定「禁區」來禁止館員存取這些檔案。 [出處: A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847) 在預設授權模式下，Codex 無需獲得使用者的個別許可，即可自由讀取及修改工作目錄內的檔案。 [出處: Codex can read sensitive files outside the CWD without ...](https://developers.openai.com/codex/agent-approvals-security) 雖然在執行需要跨越工作區域或網路連線的指令時，系統會要求使用者授權，但對於「檔案存取」本身的控制仍存在侷限。 [出處: Codex can read sensitive files outside the CWD without ...](https://developers.openai.com/codex/agent-approvals-security)

### 目前狀況

開發者社群強烈要求應增加禁止 AI 讀取特定檔案的設定功能（例如 `.codexignore`）。 [出處: Ignore files feature, e.g. ".codexignore" · openai codex ...](https://github.com/openai/codex/discussions/3456) 然而，OpenAI 目前尚未提出相關的官方對策。 [出處: A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847)

專家建議，目前解決此問題的有效方法是從源頭阻斷 AI 程序接觸敏感檔案。將檔案移至其他資料夾、強化作業系統的檔案權限設定，或是將工作在沙盒（與外部隔離的安全虛擬空間）中執行，是目前最穩妥的作法。 [出處: A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)

### 未來展望

目前開源社群持續討論此議題，要求設計更安全的架構之聲浪高漲。 [出處: [SECURITY!] Do not allow Codex to read whole filesystem by ...](https://github.com/openai/codex/issues/4410) 未來，使用者或許不再需要手動控制，而是能透過設定檔輕鬆阻斷 AI 的存取，增加官方的「排除（Exclusion）」功能。開發者在使用 Codex 時，務必定期追蹤最新的更新內容與安全相關變更。 [出處: How to prevent OpenAI Codex CLI from accessing `.env` files?](https://askai.glarity.app/search/How-to-prevent-OpenAI-Codex-CLI-from-accessing---env--files)

---

**MindTickleBytes AI 記者觀點**
隨著 AI 變得愈發聰明，我們需要守護的秘密也隨之增加。與其等待軟體變得絕對安全，不如在身為使用者的我們，學會更聰明地為 AI 築起「安全籬笆」。

## 參考資料

1. [A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847)
2. [A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)
3. [Ignore files feature, e.g. ".codexignore" · openai codex ...](https://github.com/openai/codex/discussions/3456)
4. [How to prevent OpenAI Codex CLI from accessing `.env` files?](https://askai.glarity.app/search/How-to-prevent-OpenAI-Codex-CLI-from-accessing---env--files)
5. [Agent approvals & security – Codex | OpenAI Developers](https://developers.openai.com/codex/agent-approvals-security)
6. [[SECURITY!] Do not allow Codex to read whole filesystem by ...](https://github.com/openai/codex/issues/4410)
7. [Add ability to hide sensitive files from agent · Issue #85 ...](https://github.com/openai/codex/issues/300/linked_closing_reference?reference_location=REPO_ISSUES_INDEX)