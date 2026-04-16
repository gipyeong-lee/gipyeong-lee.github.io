---
layout: post
title: "哈囉，海豚！今天心情如何？AI 開始學習海洋語言"
description: "介紹 Google 發布的首個海豚語言 AI 模型「DolphinGemma」。了解學習了 40 年數據的 AI 如何解碼海豚的複雜對話，以及人類與動物的交流是否真的可行。"
summary: "Google 與喬治亞理工學院及野生海豚計畫合作，發表了首個學習並預測海豚聲音的大型語言模型 (LLM)「DolphinGemma」，向人類與動物的雙向溝通邁出了歷史性的一步。"
tags: [DolphinGemma, Google AI, 海豚溝通, 人工智慧, 生物學, 未來技術]
image: 2026-04-16-DolphinGemma-How-Google-AI-is-helping-decode-dolphin-communication.jpg
image_alt: "藍色大海中互相溝通的海豚與分析其聲音的數位波形圖相結合的影像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "超越以人類為中心的語言，嘗試與地球上其他智慧體溝通，是 AI 技術所能擁有的最崇高目標之一。DolphinGemma 展示了技術與自然共存的新方式。"
quiz:
  - question: "Google 開發的用於解碼海豚語言的 AI 模型名稱是什麼？"
    choices: ["DolphinChat", "DolphinGemma", "SeaGemma"]
    answer: 1
    explanation: "Google 以其 Gemma 模型為基礎，開發了學習海豚聲音的「DolphinGemma」。"
  - question: "為了訓練 DolphinGemma，總共使用了多少年的數據？"
    choices: ["10年", "25年", "40年"]
    answer: 2
    explanation: "DolphinGemma 使用了野生海豚計畫 (WDP) 40 年來收集的龐大數據進行學習。"
  - question: "DolphinGemma 模型預計何時向一般開發者開放（開源）？"
    choices: ["2025年夏季", "2026年春季", "沒有公開計劃"]
    answer: 0
    explanation: "Google 表示計畫於 2025 年夏季將 DolphinGemma 模型以開源方式發布。"
lang: zh-tw
ref: 2026-04-16-DolphinGemma-How-Google-AI-is-helping-decode-dolphin-communication
---

想像一下，你正乘船在藍色的大海中央，一群海豚突然靠近並發出「呼哧—」的哨聲。以前你可能只是驚嘆「海豚心情真好」，但現在如果你手上的設備能即時分析並翻譯成這樣呢？「嘿！我是這群海豚的領袖。前面有一大群好吃的魚，我們一起去吧！」

這聽起來像是科幻電影中的場景嗎？然而，人工智慧 (AI) 技術的飛速發展正逐漸將這種電影般的想像變為現實。Google 最近發布的創新 AI 模型 **「DolphinGemma」** 正是主角。[DolphinGemma: How Google AI is helping decode dolphin communication](https://research.gatech.edu/dolphingemma-how-google-ai-helping-decode-dolphin-communication)

## 為什麼這很重要？

我們很久以前就知道海豚是非常聰明的動物。它們能照鏡子識別自己，還會成群結隊合作狩獵。然而，它們究竟以何種方式交換複雜資訊，以及彼此傳達什麼樣的深層情感，對人類來說仍然是一個巨大的謎團。因為海豚使用的是點擊音 (Clicks)、哨聲 (Whistles) 以及極短促且強烈的脈衝音 (Burst pulses) 等與人類語言結構完全不同的聲音。[DolphinGemma: How Google AI is helping decode dolphin communication](https://research.gatech.edu/dolphingemma-how-google-ai-helping-decode-dolphin-communication)

理解海豚的對話不僅僅是翻譯神奇的動物聲音，它更有價值。這是人類數千年來夢想的 **「跨物種溝通 (Interspecies communication)」** 的歷史性嘗試。透過這項技術，我們可以更深入地了解並保護海洋生態系統，並學會如何真正與地球上另一個智慧體共存。[Google working to decode dolphin communication using AI](https://www.foxnews.com/science/google-working-decode-dolphin-communication-using-ai)

Google 在這次計畫中，將以往處理人類文字或程式碼的大型語言模型 (LLM) 技術應用於自然界的聲音。這證明了 AI 不僅是辦公工具，更能成為解鎖自然界隱藏密碼的現代版「羅塞塔石碑 (Rosetta Stone)」。[DolphinGemma—GoogleDeepMind](https://deepmind.google/models/gemma/dolphingemma/)

## 輕鬆理解：AI 是如何學習海豚語言的？

AI 學習海豚語言的過程與我們學習陌生外語的過程相似，但更為精細。讓我們透過兩個比喻來了解其核心原理。

### 1. SoundStream：將聲音轉化為「數位碎片」
就像我們學習英文單字時，聽到「Apple」的聲音會先想到「A-P-P-L-E」這些字母一樣，AI 也必須將海豚的聲音轉換為數據。Google 在此使用了 **「SoundStream 編碼器 (SoundStream tokenizer)」** 技術。[DolphinGemma: How AI can decipher dolphin communication](https://blog.google/innovation-and-ai/products/dolphingemma/)

**比喻來說：** 這就像是將錄有海豚複雜聲音的「錄音帶」切碎成 AI 可以讀取的微小「數位拼圖碎片」。這些碎片聚集在一起，就成了海豚語言的「字母」。轉換為代幣 (Token，AI 能理解的最小資訊單位) 的聲音，AI 模型才能開始正式分析。[DolphinGemma: How AI can decipher dolphin communication](https://blog.google/innovation-and-ai/products/dolphingemma/)

### 2. 大型語言模型 (LLM)：預測聲音後面的內容
DolphinGemma 是以 Google 最新的語言模型「Gemma」為基礎誕生的。你在手機傳訊息時，輸入「今天...」後會自動建議「要吃什麼？」或「在做什麼？」對吧？DolphinGemma 的運作原理也與此類似。

喬治亞理工學院 (Georgia Tech) 的 Thad Starner 教授解釋道：「一旦海豚開始發出某種聲音，AI 就會嘗試預測該聲音將如何結束。」[DolphinGemma: How Google AI is helping decode dolphin communication](https://www.linkedin.com/posts/google_dolphingemma-how-google-ai-is-helping-decode-activity-7317578448380538882-Ko3i)

**簡單來說：** AI 正在執行海豚語言的「自動完成功能」。得益於對大量海豚對話模式的學習，AI 只要聽到聲音的前半段，就能預測接下來的聲音。這是 AI 開始理解海豚語言特有語法和結構的重要證據。[DolphinGemma: How Google AI is helping decode dolphin communication](https://research.gatech.edu/dolphingemma-how-google-ai-helping-decode-dolphin-communication)

## 目前狀況：進展到哪裡了？

這次計畫是由 Google、喬治亞理工學院以及名為 **野生海豚計畫 (Wild Dolphin Project, WDP)** 的專業研究機構合作完成的。[DolphinGemma: How AI can decipher dolphin communication](https://blog.google/innovation-and-ai/products/dolphingemma/)

### 40 年的記錄，AI 的珍貴教科書
DolphinGemma 之所以能變得聰明，最大的功臣是龐大的「學習資料」。野生海豚計畫團隊在過去 **40 年的漫長歲月**中，一直堅持錄製海洋中海豚的聲音並觀察其行為。[Google Uses DolphinGemma AI to Decode Dolphin Communication - Entrepreneur](https://www.entrepreneur.com/business-news/google-uses-dolphingemma-ai-to-decode-dolphin-communication/490753) AI 在極短時間內學習了這份相當於一個人一生心血的龐大資料，並掌握了海豚聲音中的細微模式。

### 2025 年夏季，將向全球科學家開放
Google 決定不壟斷這項驚人的技術。計畫於 2025 年夏季將 DolphinGemma 模型以 **開源 (Open Source)** 方式發布。[Google Is Training a New A.I. Model to Decode Dolphin Chatter—and ...](https://www.smithsonianmag.com/smart-news/google-is-training-a-new-ai-model-to-decode-dolphin-chatter-and-potentially-talk-back-180986434/) 屆時，全球海洋生物學家將能更快速、更準確地分析其研究的海豚語言，預計將為海洋科學領域帶來巨大的進步。

## 未來會如何發展？

DolphinGemma 的最終目標不僅止於聽音和分析。科學家們夢想著有一天能夠實現 **「人類與海豚真正的對話」**。[Google working to decode dolphin communication using AI](https://www.foxnews.com/science/google-working-decode-dolphin-communication-using-ai)

### 海底首次對話的開始
如果說到目前為止我們還處於單方面觀察海豚聲音的立場，那麼像 DolphinGemma 這樣的模型將能夠直接生成海豚能理解的聲音。[SETI Tech On Earth: DolphinGemma: How Google AI Is Helping Decode ...](https://astrobiology.com/2025/04/seti-tech-on-earth-dolphingemma-how-google-ai-is-helping-decode-dolphin-communication.html) 雖然實際海豚是否能理解我們發送的訊息並給予回應仍有待觀察，但專家評價認為，我們比以往任何時候都更接近那個奇蹟般的階段。[Google develops AI model to help researchers decode dolphin ...](https://siliconangle.com/2025/04/14/google-develops-ai-model-help-researchers-decode-dolphin-communication/)

然而，還有許多功課要做。除了單純模仿聲音模式外，還必須完美掌握該聲音在何種「情境 (脈絡)」下以及帶著何種「意圖」被使用。就像我們說「吃過了嗎？」有時是問候，有時是關心一樣，海豚的語言也可能根據情況有不同的含義。[Google made an AI model to talk to dolphins | Popular Science](https://www.popsci.com/technology/dolphin-talking-google-ai/)

---

### MindTickleBytes 的 AI 記者觀點

DolphinGemma 不僅僅是一項技術成就，更是一個可以改變我們對待地球同伴生命態度的工具。語言是智慧與情感的象徵。理解海豚的語言，將是一個用心而非僅用腦去承認它們是與我們人類一樣擁有複雜社會紐帶、感受喜怒哀樂的智慧存在的過程。

如果 AI 傳達的海底海豚第一句話是「謝謝你們一起守護地球」會如何呢？在那一天到來之前，讓我們一起傾聽 DolphinGemma 將串連起的藍色大海故事。

## 參考資料
1. [DolphinGemma: How Google AI is helping decode dolphin communication](https://research.gatech.edu/dolphingemma-how-google-ai-helping-decode-dolphin-communication)
2. [DolphinGemma: How AI can decipher dolphin communication](https://blog.google/innovation-and-ai/products/dolphingemma/)
3. [Google Is Training a New A.I. Model to Decode Dolphin Chatter—and Potentially Talk Back](https://www.smithsonianmag.com/smart-news/google-is-training-a-new-ai-model-to-decode-dolphin-chatter-and-potentially-talk-back-180986434/)
4. [SETI Tech On Earth: DolphinGemma: How Google AI Is Helping Decode Dolphin Communication](https://astrobiology.com/2025/04/seti-tech-on-earth-dolphingemma-how-google-ai-is-helping-decode-dolphin-communication.html)
5. [Google working to decode dolphin communication using AI](https://www.foxnews.com/science/google-working-decode-dolphin-communication-using-ai)
6. [Google Uses DolphinGemma AI to Decode Dolphin Communication - Entrepreneur](https://www.entrepreneur.com/business-news/google-uses-dolphingemma-ai-to-decode-dolphin-communication/490753)
7. [DolphinGemma: How Google AI is helping decode dolphin communication (LinkedIn)](https://www.linkedin.com/posts/google_dolphingemma-how-google-ai-is-helping-decode-activity-7317578448380538882-Ko3i)
8. [DolphinGemma—GoogleDeepMind](https://deepmind.google/models/gemma/dolphingemma/)
9. [Google made an AI model to talk to dolphins | Popular Science](https://www.popsci.com/technology/dolphin-talking-google-ai/)
10. [Google develops AI model to help researchers decode dolphin communication](https://siliconangle.com/2025/04/14/google-develops-ai-model-help-researchers-decode-dolphin-communication/)
11. [Decoding Dolphin Communication with AI (LinkedIn)](https://www.linkedin.com/pulse/decoding-dolphin-communication-ai-googles-maxime-grenu-ffmse)
12. [Google’s new AI is trying to talk to dolphins—seriously](https://blog.geogarage.com/2025/04/googles-new-ai-is-trying-to-talk-to.html)

## FACT-CHECK SUMMARY
- Claims checked: 10
- Claims verified: 10
- Verdict: PASS