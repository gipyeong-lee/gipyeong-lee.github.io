---
layout: post
title: "手機裡的 AI 偵探？新加坡政府與 Google 如何聯手打擊詐騙"
description: "新加坡政府與 Google DeepMind 公開了一項全新的 AI 技術，能在無需擔心個人隱私外洩的情況下，在智慧型手機內部實時過濾詐騙對話。"
summary: "Google DeepMind 與新加坡政府宣布推出「裝置端 AI」（on-device AI）技術，讓使用者的對話資料無需傳送到雲端，即可在手機裝置內直接偵測詐騙企圖。"
tags: [AI, 資訊安全, 新加坡, Google DeepMind, 個人隱私]
image: 2026-10-14-Google-DeepMind-and-Singapore-Government-announce-new-AI-tool-to-protect-citizen.jpg
image_alt: "在手機螢幕上偵測到詐騙對話訊息並發出警告通知的裝置端 AI 安全解決方案概念圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是 AI 時代在個人隱私保護與實時安全之間取得平衡的理想模型。未來在裝置內直接運行智慧型 AI 的「裝置端」（on-device）安全技術將成為必備標準。"
quiz:
  - question: "這項技術能保障個人隱私安全的關鍵原因為何？"
    choices: ["因為它將所有對話內容傳送到政府伺服器", "因為它不會將個人訊息資料傳送到雲端，而是直接在手機內部處理", "因為它能立即公開詐騙犯的身分"]
    answer: 1
    explanation: "此技術採用「裝置端（on-device）」方式，所有分析皆在智慧型手機內部完成，敏感資料不會外流至外部。"
  - question: "新加坡因詐騙造成的損失規模大約為何？"
    choices: ["約 10 億新加坡元", "約 20 億新加坡元", "2019 年以來超過 40 億新加坡元"]
    answer: 2
    explanation: "新加坡自 2019 年以來，詐騙犯罪造成的損失金額已超過 40 億新加坡元，是嚴重的社會問題。"
  - question: "為了進行詐騙偵測，使用了 Google 的哪一個模型？"
    choices: ["Gemma 模型", "Gemini 模型", "Gemma 3 模型"]
    answer: 0
    explanation: "本次計畫中，結合了輕量化分類器（classifier）與微調後的「Gemma」AI 模型。"
lang: zh-tw
ref: 2026-10-14-Google-DeepMind-and-Singapore-Government-announce-new-AI-tool-to-protect-citizen
---

想像一下，您再也不用煩惱陌生號碼傳來的訊息是否為詐騙。在您回覆訊息之前，您的智慧型手機就先親切地發出警告：「這則對話有疑慮！」這就像是您的對話視窗旁，隨時坐著一位非常聰明的安全偵探。

2026 年 10 月 14 日，Google DeepMind 與新加坡政府科技局（GovTech）宣布了一項戰略合作夥伴關係，旨在將這種夢幻般的安全技術變為現實。這項技術於新加坡舉辦的「2026 新加坡國際網路週（Singapore International Cyber Week 2026）」現場公開，正成為保護全球使用者隱私與資產的新希望。[參考資料 14](https://deepmind.google/blog/strengthening-singapores-ai-future-a-new-national-partnership/), [參考資料 15](https://www.linkedin.com/posts/owen-larter-3340b224_google-deepmind-singapore-national-ai-activity-7462730290722045952-uWwz), [參考資料 16](https://deepmind.google/models/gemini/), [參考資料 18](https://ground.news/article/govtech-and-google-deepmind-developing-real-time-detection-of-ai-scams-on-devices)

### 這為何重要？

詐騙犯罪不僅造成金錢損失，更擾亂了現代人的日常生活。以新加坡為例，自 2019 年以來，各類詐騙事件造成的損失金額高達 40 億新加坡元以上，其規模之大令人震驚。[參考資料 15](https://www.linkedin.com/posts/owen-larter-3340b224_google-deepmind-singapore-national-ai-activity-7462730290722045952-uWwz)

大多數現有的安全技術採用將訊息傳送到伺服器進行分析的方式。然而，這伴隨著隱私侵犯爭議或資料外洩的風險。此次發布的技術為了讓使用者能安心使用，將「個人隱私保護」列為最優先設計考量。確保詐騙預防的同時，使用者不必擔心自己的對話內容會被 AI 公司或政府查看，這是該技術最大的創新點。[參考資料 14](https://deepmind.google/blog/strengthening-singapores-ai-future-a-new-national-partnership/), [參考資料 17](https://cryptobriefing.com/deepmind-govtech-singapore-ai-scam-tool/)

### 輕鬆理解：手機裡的小偵探

這項技術的核心在於「裝置端（on-device）」AI。簡單來說，如果我們平常使用的雲端 AI 是從「巨大的中央圖書館」尋找資訊，那麼裝置端 AI 就是將所有資訊都存入您的「口袋小筆記本」中，並隨時進行確認。

用這種比喻更容易理解：就像在智慧型手機內放入一個極細的濾網。當帶有惡意意圖的單字或模式進入訊息時，該「濾網」會立即過濾。Google DeepMind 利用輕量化分類器與微調後的「Gemma」AI 模型，將極其複雜且龐大的字典大幅縮減至適合手機效能的規模，並嵌入裝置內部。[參考資料 17](https://cryptobriefing.com/deepmind-govtech-singapore-ai-scam-tool/), [參考資料 18](https://ground.news/article/govtech-and-google-deepmind-developing-real-time-detection-of-ai-scams-on-devices)

使用者在收到訊息的瞬間，這位「小偵探（Gemma 模型）」就會在手機內部極速讀取內容，確認是否有詐騙嫌疑。因為連一個字的個人對話資料都不會透過網路傳輸到外部伺服器，所以非常安全。[參考資料 14](https://deepmind.google/blog/strengthening-singapores-ai-future-a-new-national-partnership/), [參考資料 15](https://www.linkedin.com/posts/owen-larter-3340b224_google-deepmind-singapore-national-ai-activity-7462730290722045952-uWwz)

### 當前狀況

目前，這項技術正透過 Google DeepMind 與新加坡政府之間的緊密合作，開發為實時詐騙偵測模型。[參考資料 13](https://deepmind.google/models/gemini/), [參考資料 17](https://cryptobriefing.com/deepmind-govtech-singapore-ai-scam-tool/) 為了在守護使用者隱私的同時應對不斷演變的犯罪手法，開發團隊致力於最大化智慧型手機本身的運算能力，以捕捉詐騙份子狡猾的語言操弄。[參考資料 15](https://www.linkedin.com/posts/owen-larter-3340b224_google-deepmind-singapore-national-ai-activity-7462730290722045952-uWwz), [參考資料 17](https://cryptobriefing.com/deepmind-govtech-singapore-ai-scam-tool/) 當然，沒有任何技術是完美的，目前正處於考量技術侷限並持續進行優化的階段。

### 未來展望

此次發布不僅是新加坡的問題，更預告了全球所有智慧型手機使用者安全標準的變革。未來，典範將從「將資料傳送到中央進行分析的時代」移動至「由我的裝置直接保護我的時代」。

我們即將迎來一個日常生活中的大量詐騙簡訊由智慧型手機自行攔截或提醒的環境。如同 Google DeepMind 此次展示的案例，隨著技術發展，我們有理由期待隱私獲得更深層的保護、安全性更聰明的未來。[參考資料 8](https://ground.news/article/govtech-and-google-deepmind-developing-real-time-detection-of-ai-scams-on-devices), [參考資料 16](https://deepmind.google/models/gemini/)

### MindTickleBytes 的 AI 記者觀點

此次合作證明了個人隱私保護並非安全技術的絆腳石，反而是安全技術應追求的最重要價值。我們期待「裝置端安全」理念——即資料留在手邊時最為安全——能成為全球標準。

## 參考資料

1. Strengthening Singapore’s AI Future: A New National Partnership (https://deepmind.google/blog/strengthening-singapores-ai-future-a-new-national-partnership/)
2. Singapore Government Partnership Strengthens National AI Strategy (https://www.linkedin.com/posts/owen-larter-3340b224_google-deepmind-singapore-national-ai-activity-7462730290722045952-uWwz)
3. About Google DeepMind | Responsibility (https://deepmind.google/models/gemini/)
4. GovTech and Google DeepMind developing real-time detection of AI scams on devices (https://www.channelnewsasia.com/singapore/govtech-google-deepmind-ai-scam-quantum-sicw-6455621)
5. Minister for Digital Development and Information Josephine Teo announced a strategic collaboration (https://cryptobriefing.com/deepmind-govtech-singapore-ai-scam-tool/)
6. Google DeepMind and GovTech Unveil On-Device Scam Detection Model (https://www.unite.ai/google-deepmind-and-govtech-unveil-on-device-scam-detection-model/)
7. News — Google DeepMind (https://deepmind.google/blog/)
8. Google DeepMind and GovTech Singapore are building on-device Gemma AI models (https://ground.news/article/govtech-and-google-deepmind-developing-real-time-detection-of-ai-scams-on-devices)
9. AI News, Summarized by AI | ByteBrief (https://bytebrief.ai/category/AI)