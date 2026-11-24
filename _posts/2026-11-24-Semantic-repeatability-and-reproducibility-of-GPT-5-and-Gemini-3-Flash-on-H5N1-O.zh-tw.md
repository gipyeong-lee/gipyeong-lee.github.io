---
layout: post
title: "向 AI 詢問 H5N1 禽流感的回覆，每次都一樣嗎？GPT-5 與 Google Gemini 3 Flash 的一致性大探索"
description: "帶您輕鬆了解最新 AI 模型 GPT-5 與 Google Gemini 3 Flash 在面對 H5N1 禽流感相關問題時，其回覆穩定性與一致性的研究分析結果。"
summary: "透過 GPT-5 與 Google Gemini 3 Flash 在 H5N1 One Health 問題上展現的語意重複性與重現性研究結果，探討 AI 醫療資訊的信賴性與一致性。"
tags: [AI, GPT-5, Gemini, H5N1, OneHealth, 研究]
image: 2026-11-24-Semantic-repeatability-and-reproducibility-of-GPT-5-and-Gemini-3-Flash-on-H5N1-O.jpg
image_alt: "實驗室螢幕上顯示的 AI 模型比較分析圖表與禽流感資料"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 已登上醫療保健領域信賴性驗證的試驗臺。提問方式改變時答案也不會動搖的穩定性，將成為未來 AI 醫療保健的核心競爭力。"
quiz:
  - question: "本研究調查的兩個 AI 模型為何？"
    choices: ["GPT-4 與 Gemini 2", "GPT-5 與 Gemini 3 Flash", "Claude 與 Llama"]
    answer: 1
    explanation: "研究以 OpenAI 的 GPT-5 與 Google 的 Gemini 3 Flash 為對象進行了實驗。"
  - question: "研究中所使用的 H5N1 相關問題是從哪裡收集的？"
    choices: ["醫學論文摘要", "社群媒體討論", "醫院病患紀錄"]
    answer: 1
    explanation: "使用了源自社群媒體討論的 15 個 H5N1 One Health 問題。"
  - question: "在重複性與重現性中，GPT-5 的哪一項指標更高？"
    choices: ["重複性更高", "重現性更高", "兩項指標完全一致"]
    answer: 1
    explanation: "GPT-5 的重現性（改變提問格式時的一致性）明顯高於重複性。"
lang: zh-tw
ref: 2026-11-24-Semantic-repeatability-and-reproducibility-of-GPT-5-and-Gemini-3-Flash-on-H5N1-O
---

想像一下。某天早晨，新聞報導了高病原性禽流感（H5N1，一種可傳染給鳥類與哺乳動物等多種宿主的高病原性病毒）蔓延的消息。你懷著不安的心情拿起智慧型手機，向人工智慧（AI）聊天機器人提問：「好像接觸過野生鳥類，該注意什麼症狀？又該如何應對？」 

AI 親切地逐項說明了症狀與應對方法。這讓人安心了許多。但腦海中突然閃過一個念頭：「等一下，如果我把這個問題一模一樣再問一次，或者稍微換個詞彙提問，AI 還能給出同樣準確的回答嗎？還是會每次都隨機胡言亂語？」

最近學術界與科技界針對這個問題給出了深入的解答。根據 [Semantic repeatability and reproducibility of GPT-5 and Gemini 3 Flash on H5N1 One Health questions](https://arxiv.org/abs/2611.29859) 的研究，備受全球矚目的最先進大型語言模型（LLM，Large Language Model，學習大規模文字資料並像人類一樣對話的 AI 模型）——OpenAI 的 GPT-5 與 Google 的 Gemini 3 Flash（Google 具代表性的高速人工智慧助理模型），在回答健康相關問題時能保持多高的一致性，已經受到了徹底的驗證 [[Source 1](https://arxiv.org/abs/2611.29859), [Source 7](https://deepmind.google/models/gemini/)]. 

---

## 為什麼這很重要？

高病原性禽流感 A(H5N1) 自 2024 年以來，從「同一健康」（One Health，人類、動物與環境健康緊密相連的概念）的角度重新成為重要的公共衛生議題 [[Source 1](https://arxiv.org/abs/2611.29859)]. 在病毒傳播的每個時期，大眾為了獲取準確的醫療資訊，越來越依賴 AI 聊天機器人 [[Source 1](https://arxiv.org/abs/2611.29859)].

這裡出現了一個非常關鍵的問題。在評估 AI 的「準確度」之前，必須先理解其回答具備多高的「一致性（Consistency）」 [[Source 1](https://arxiv.org/abs/2611.29859)]. 如果提出相同的問題，某天回答「沒有危險」，另一天卻說「請立即去醫院」，給出完全相反的答案，那麼使用者將無法信任任何回答。換句話說，證明 AI 所給出的單一回答能否公平代表該模型的實際行為模式至關重要 [[Source 1](https://arxiv.org/abs/2611.29859)].

對一般大眾而言，這就像是一道安全網，保證「我所依賴的 AI 建議並非偶然產生的產物」。在生死攸關的醫療保健資訊領域中，AI 的反覆無常可能會直接導致混亂與危險。因此，衡量 AI 能否不動搖地維持一致的回答，既是衡量技術成熟度的標尺，也是鞏固公共衛生安全網的核心任務。

---

## 輕鬆理解：重複性、重現性，以及思維鏈

在本研究中，AI 的一致性被劃分為兩個主要概念進行測量：即**「重複性（Repeatability）」**與**「重現性（Reproducibility）」**. 

我們可以這樣比喻：
* **重複性**就像是經驗豐富的咖啡師用相同的咖啡豆和相同的器具萃取 30 次濃縮咖啡時，口感有多麼一致。也就是說，當**以一模一樣、字句不差的相同問題反覆提問時，AI 給出的回答有多相似**.
* **重現性**則是當食譜的表達方式稍微改變（例如：「泡菜湯怎麼煮」改成「告訴我美味泡菜湯料理秘訣」），或是改變提問方式時，其結果本質上是否相同。也就是評估：**即使提問的形式或框架改變了，AI 是否仍能維持相同的核心真相**.

在此基礎上，研究團隊採用了一種名為**「思維鏈（Chain-of-Thought, CoT，指引 AI 依序描述邏輯推理步驟直至得出結論的技術）」**的特殊方法。這就像在解困難的數學應用題時，老師指示學生「不要只在腦中想，把計算步驟一步步寫出來」一樣。透過這個過程，研究團隊同時測試了 AI 是否能產出更具邏輯性與一致性的回答。特別是像「鑑別診斷（Differential Diagnosis）」這樣的推理方式，被認為是其中最優秀的框架之一 [[Source 1](https://arxiv.org/abs/2611.29859)].

---

## 研究剖析：5,400 個回答告訴了我們什麼

為了進行這項龐大的一致性驗證，研究團隊經過了嚴密的實驗設計。 

首先，從社群媒體的實際對話中精心挑選了 15 個與 H5N1 禽流感相關的 One Health 核心問題 [[Source 1](https://arxiv.org/abs/2611.29859)]. 實驗規模相當龐大。將每個問題直接提交 30 次，並透過 5 種不同的思維鏈（Chain-of-Thought）變體各執行 30 次，總共收集了高達 **5,400 個龐大回覆** [[Source 1](https://arxiv.org/abs/2611.29859)]. 

收集到的回答透過 MPNet 嵌入（將文字意義轉換為高維度數字向量的技術）進行處理，並透過成對餘弦相似度（數學測量兩段文字意義方向性一致程度的指標）進行分析。為了提高統計信賴度，還動用了各種無母數檢定與內部共識統計技術 [[Source 1](https://arxiv.org/abs/2611.29859)].

結果如何呢？

1. **整體高度一致性**：無論是 OpenAI 的 GPT-5 還是 Google [Google Gemini](https://gemini.google.com/) 生態系中的 Gemini 3 Flash，以 0 到 1 重新縮放的分數為標準，皆記錄了 **0.93 到 0.97 的極高平均一致性** [[Source 1](https://arxiv.org/abs/2611.29859), [Source 2](https://gemini.google.com/)]. 這證明了這兩個模型對於大眾提出的健康問題都具備相當水準的穩定回答能力。
2. **GPT-5 的獨特特質**：就 GPT-5 而言，改變提問方式時的**重現性（Reproducibility）在統計學上顯著高於重複相同問題時的重複可能性（Repeatability）**（$W = 3.0, p = 0.0003$）[[Source 1](https://arxiv.org/abs/2611.29859)]. 這顯示出 GPT-5 無論使用者如何曲折提問或變換表達方式，其看穿本質並得出一致結論的能力都非常卓越。
3. **Gemini 3 Flash 的均衡表現**：相對地，Google 的 Gemini 3 Flash 在重複可能性與重現性這兩項指標上呈現幾乎一致、在統計上難以區分的態樣（$W = 42.0, p = 0.33$）[[Source 1](https://arxiv.org/abs/2611.29859)]. 這意味著無論提問的形式稍微改變還是重複提問，Gemini 3 Flash 所展現的語意一致性模式都非常穩定且均勻。

---

## 未來發展如何？

這項研究並不僅止於像分出優劣般為兩個 AI 模型進行排名。它為未來在醫療與保健領域中將 AI 聊天機器人引入作為官方資訊窗口時，**應當以何種方式驗證其信賴性**提出了全新的標準 [[Source 1](https://arxiv.org/abs/2611.29859)].

在不久的將來，AI 聊天機器人很有可能超越單純的對話夥伴，在公共衛生危機情況下承擔起指導防疫守則或傳染病應對要點的官方指南角色。屆時，開發商將不能僅滿足於單次測試中的高分，而是必須經過數千次變形提問與重複測試，公開「一致性成績單」。 

對使用者而言，也將迎來有益的轉變。無論我使用什麼詞彙提問，或者向 AI 重複詢問相同的問題，都能夠不動搖地獲得一致專業知識的信賴基礎正在日益穩固。隨著 AI 技術不斷升級，其作為守護我們日常與健康的堅實助手之面貌也正在加深。

---

## MindTickleBytes 的 AI 記者視角

在人工智慧的時代，我們所面臨的最大挑戰不是「知道標準答案」，而是「能否相信這個答案」。這次 GPT-5 與 Gemini 3 Flash 的 H5N1 回答一致性研究是一個極佳的里程碑，它證明了 AI 不僅僅是個會說話的巧匠，更在面對公共衛生危機這般嚴峻的現實中，穩穩站立在不容動搖的信賴基石之上。隨著技術不斷進步，我們的心態也迎來了需要更加聰明應對的時刻。

---

## 參考資料

1. [Semantic repeatability and reproducibility of GPT-5 and Gemini 3 Flash on H5N1 One Health questions](https://arxiv.org/abs/2611.29859)
2. [Google Gemini](https://gemini.google.com/)
3. [Gemini — Google DeepMind | 我們的下一個前沿智慧時代](https://deepmind.google/models/gemini/)
4. [Gemini 3 Pro vs GPT-5.2](https://evolink.ai/ko/blog/gpt-5-2-vs-gemini-3-pro-comparison-2026)
5. [Gemini 3.5 Flash 神經網路 — Google AI 模型](https://stiva.ai/models/gemini-3-5-flash)