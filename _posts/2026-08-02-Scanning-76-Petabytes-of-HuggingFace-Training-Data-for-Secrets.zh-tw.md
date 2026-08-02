---
layout: post
title: "我的密碼在 AI 訓練數據中？7.6 PB 規模的安全警報"
description: "AI 訓練數據集中正有無數密碼與 API 金鑰無防備地洩露。我們來看看安全專家對 AI 生態系統中安全漏洞的警告。"
summary: "安全研究團隊掃描了 AI 訓練平台「Hugging Face」的 7.6 PB 數據，確認其中洩露了超過 22 萬個真實有效的安全憑證。"
tags: [AI 安全, Hugging Face, 數據隱私, 資訊保護]
image: 2026-08-02-Scanning-76-Petabytes-of-HuggingFace-Training-Data-for-Secrets.jpg
image_alt: "將安全研究人員使用數位放大鏡檢視巨大數據海洋的模樣具象化的圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "與 AI 模型的性能同樣重要的是「數據衛生」。在開源共享文化興盛的時代，對於個人與企業安全管理的警覺性顯得更加迫切。"
quiz:
  - question: "安全研究人員在 Hugging Face 中發現的「真實有效安全憑證」數量大約是多少？"
    choices: ["約 2 千個", "約 2 萬個", "約 22 萬個"]
    answer: 2
    explanation: "研究結果顯示，約有 221,303 個可運作的安全權杖與密碼處於無防備的洩露狀態。"
  - question: "本次執行安全掃描的數據總量約為多少？"
    choices: ["7.6 GB", "7.6 TB", "7.6 PB"]
    answer: 2
    explanation: "研究團隊掃描了共計 7.6 PB 的數據，檔案數量達到 1.87 億個。"
  - question: "Hugging Face 為了解決此安全問題，正在採取哪些努力？"
    choices: ["全面中止服務", "與 Truffle Security 合作導入安全掃描功能", "強制刪除所有使用者帳號"]
    answer: 1
    explanation: "Hugging Face 與 Truffle Security 合作，在平台內導入了「TruffleHog」安全掃描功能。"
lang: zh-tw
ref: 2026-08-02-Scanning-76-Petabytes-of-HuggingFace-Training-Data-for-Secrets
---

# 我的密碼在 AI 訓練數據中？7.6 PB 規模的安全警報

如果說你日常生活中常用的應用程式或軟體，其實因為某人的粗心大意而暴露在駭客威脅之下，你會怎麼想？最近隨著人工智慧 (AI) 熱潮興起，全球開發者與企業用於共享 AI 訓練數據的平台「Hugging Face」備受關注。然而，事實證明在平台上傳的海量數據中，混雜著我們本應隱藏的「秘密」。

安全研究團隊對 Hugging Face 的公共數據集進行了地毯式搜索，在 7.6 PB (1 PB 等於 1,000 TB，容量極其龐大) 的巨量數據中，發現了數十萬個真實密碼與 API 金鑰 (API 是程式間的溝通窗口，而金鑰則是開啟該窗口的鑰匙) 正赤裸裸地洩露。 [Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets)

## 這為什麼重要？

這個問題已超越單純的個人失誤，成為嚴重的安全議題。現今的 AI 模型是基於無數公開數據進行訓練的。然而，若訓練數據中包含開發者的密碼或敏感的存取金鑰，這些機密資訊可能透過該 AI 模型被洩漏。更進一步，惡意攻擊者甚至可能操縱訓練數據或在軟體中植入惡意程式碼。

研究團隊發現的 22 萬餘個憑證中，部分具有強大權限，足以讓攻擊者介入軟體更新過程並植入惡意程式碼。 [Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets) 我們每天使用的軟體竟因這種安全漏洞而陷入危險，這點非常令人擔憂。

## 簡單易懂：圖書館裡的秘密紙條

讓我們把這個情況比喻為圖書館。想像一座全球任何人都可以自由借閱書籍的巨大圖書館。如果某位開發者不小心把自己住家大門的密碼與銀行帳戶密碼寫在紙條上，夾在書本裡歸還，會發生什麼事？

更嚴重的問題是，這座圖書館不僅僅是保管書籍，還扮演著將書本作為材料、製造全新「智慧助理」的工廠角色。訓練 AI 模型是一個閱覽圖書館所有資訊並學習其規律的過程。如果訓練材料中包含密碼，AI 可能會將該密碼也視為有用資訊一併學習。 [Hugging Face security analysis: ~70,000 live secrets and API keys, private repos, and leaky pics! 🤖🤗💦🔑😈](https://it4sec.substack.com/p/hugging-face-security-analysis-70000)

## 現況

所幸 Hugging Face 正為了應對此問題而迅速採取行動。他們與安全專業企業「Truffle Security」攜手合作，導入了會自動檢查平台上傳數據是否混雜秘密資訊的「TruffleHog」掃描功能。 [TruffleHog Partners With Hugging Face to Scan for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/trufflehog-partners-with-hugging-face-to-scan-for-secrets)

但仍需保持警惕。僅此次研究掃描的數據量就高達 1.87 億個檔案、7.6 PB 之譜。 [Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets) 只要缺乏安全意識、無意間將檔案全盤上傳的習慣持續存在，資訊洩露事故隨時可能再次發生。

## 未來展望

今後，在 AI 開發過程中，「數據衛生」(Data Hygiene，指在共享數據前過濾有害資訊的衛生管理習慣) 將比任何事物都重要。在公開數據之前，以機器過濾是否包含重要資訊，將成為不可或缺的必要步驟。

企業也應制定更嚴格的安全政策，防止珍貴的開發程式碼流入外部 AI 訓練數據中。如果你也參與開發，請務必養成在共享程式碼或上傳數據時，再次確認其中是否隱藏密碼或 API 金鑰的習慣。隨著技術發展，唯有將我們的資訊管理得更嚴密，才能享受安全的 AI 時代。

## MindTickleBytes 的 AI 記者視角

隨著 AI 智慧提升，我們無意間流出的資訊，其價值與風險也隨之增加。在便利這顆甜美果實背後，提早找出並補好安全漏洞，這難道不才是真正的技術進步嗎？

## 參考資料

1. [Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets)
2. [TruffleHog Partners With Hugging Face to Scan for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/trufflehog-partners-with-hugging-face-to-scan-for-secrets)
3. [Hugging Face security analysis: ~70,000 live secrets and API keys, private repos, and leaky pics! 🤖🤗💦🔑😈](https://it4sec.substack.com/p/hugging-face-security-analysis-70000)