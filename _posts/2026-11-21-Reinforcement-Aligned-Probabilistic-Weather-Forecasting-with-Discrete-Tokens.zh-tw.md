---
layout: post
title: "AI預測天氣的新方法：『數位天氣 Token』與強化學習的相遇"
description: "輕鬆了解次世代機率性天氣預測框架 WeatherCraft 的原理與效能，它如同 GPT 讀取文字般將大氣切割並進行預測。"
summary: "WeatherCraft 結合離散天氣 Token 與強化學習，是將全球中長期天氣預測的準確度與速度大幅提升的次世代 AI 框架。"
tags: [AI, Weather, WeatherCraft, MachineLearning, ReinforcementLearning]
image: 2026-11-21-Reinforcement-Aligned-Probabilistic-Weather-Forecasting-with-Discrete-Tokens.jpg
image_alt: "以數位 Token 分析地球大氣狀態的 AI 天氣預測系統概念視覺化"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "將生成式 AI 與強化學習範式植入複雜大氣科學的 WeatherCraft，超越了單純的數值計算，將極端天氣應對能力提升至全新境界。"
quiz:
  - question: "WeatherCraft 在全球中長期天氣預測中引入的核心範式是什麼？"
    choices: ["GPT 風格的預訓練與後訓練範式", "基於傳統物理定律的單獨模擬", "固定的單一決定論性預測模型"]
    answer: 0
    explanation: "WeatherCraft 透過離散天氣 Token 與強化學習對齊，將 GPT 風格的預訓練-後訓練範式引入全球中長期天氣預測中。"
  - question: "與傳統 GenCast 相比，WeatherCraft 應用 KV 快取時達到的推論速度提升倍數大約是多少？"
    choices: ["約 5 倍", "約 10 倍", "約 18 倍"]
    answer: 2
    explanation: "應用 KV 快取時，WeatherCraft 記錄到相較於 GenCast 提升約 18 倍的推論速度。"
  - question: "WeatherCraft 為了最大化下游任務獎勵所採用的最佳化技術是什麼？"
    choices: ["GRPO (Group Relative Policy Optimization)", "基於 CNN 的影像卷積", "隨機蒙地卡羅模擬"]
    answer: 0
    explanation: "透過利用直接 Token 對數機率的 GRPO（Group Relative Policy Optimization），無需經過評估器或結合模型，即可最大化下游任務獎勵。"
lang: zh-tw
ref: 2026-11-21-Reinforcement-Aligned-Probabilistic-Weather-Forecasting-with-Discrete-Tokens
---

想像一下，週末想和家人去露營而打開了天氣 App，氣象預報顯示「降雨機率 30%」。然而，大家一定都有過這樣的經驗：無法確切得知雨何時會傾盆而下，或是風有多大，因而感到困擾。天氣是左右我們生活計畫最重要的自然現象，然而長期以來，全球中長期天氣預報為了破解複雜的大氣動力學，一直在龐大的超級電腦資源與時間中苦戰 [Source 1, Source 6]。

比喻來說，解讀巨大的大氣流動就像是盲目拼湊由數百萬個碎片組成的立體拼圖。傳統方法依賴基於物理方程式逐一模擬大氣狀態的數值天氣預報（NWP, Numerical Weather Prediction） [Source 20]。然而，天氣本質上充滿不確定性，與其斬釘截鐵地預測單一未來，不如同時檢視多種可能性的機率性預測來得不可或缺 [Source 1, Source 15]。最近，徹底顛覆這種天氣預測格局的全新人工智慧框架問世了，這就是由李錦漢（Jinhan Li）研究團隊等人所開發的 **WeatherCraft** [Source 1, Source 6]。

---

## 為什麼這很重要？

天氣預報不僅僅是決定是否帶傘而已。預先偵測並警告颱風或熱浪等極端氣象事件，是保護無數人命與財產的安全通道 [Source 1, Source 6]。此外，在預測再生能源發電量、制定農業計畫等各種社會與經濟決策中，精準的中長期氣象預報扮演著核心角色 [Source 1, Source 15]。

簡單來說，精準的天氣預報就是現代社會的安全網。然而，以往基於機器學習的天氣模型偏向僅產出單一結果的決定論式方法 [Source 18]，或者在生成多種情境時運算速度過慢。WeatherCraft 將對話式大型語言模型（LLM, Large Language Model，理解並生成人類語言的 AI 架構）理解世界的方式直接移植到天氣預報中，開闢了一條能夠快速、準確且同時呈現多種未來天氣情境的道路 [Source 1, Source 2]。這具有從根本上改變我們應對因氣候變遷而日益難以預測的極端氣象之方式的潛力。

---

## 輕鬆理解：讀取大氣的「數位 Token」與量身打造的讀書方法

那麼，WeatherCraft 是如何透過 AI 完美消化複雜的大氣狀態呢？核心原理大致分為兩部分。第一是**離散天氣 Token（Discrete Weather Tokens）**與多尺度 Tokenizer，第二是**強化學習對齊（Reinforcement Learning Alignment）** [Source 1]。

### 1. 將巨大的地球當作拼圖碎片：多尺度 Tokenizer

如果將巨大的地球大氣狀態原封不動地塞進 AI 中，AI 將因龐大的資訊量而消化不良。這就像是為了在智慧型手機上順暢觀看高畫質電影檔案而進行壓縮一樣。WeatherCraft 的**多尺度 Tokenizer（Multiscale Tokenizer）**將大氣狀態從粗略碎片（Coarse）到細緻碎片（Fine）以階層式的 Token 形式細細切割 [Source 1]。 

試著想想拼拼圖的過程。首先用大塊的拼圖碎片拼出整體大氣的宏觀流向（大體氣壓配置與巨大雲帶），接著在上面疊加細緻的碎片，填補局部地區的風向流動或微小溫度變化 [Source 1]。此時，**Transformer（掌握句子或資料中元素相互關係的核心 AI 架構）**投入其中，建立隨時間流逝與空間尺度的因果關係模型，並平行預測各尺度內的 Token [Source 1]。 

### 2. 透過模擬考試精進實力的辦法：GRPO 與強化學習

第二個秘密在於學習方式。正如人類在先學習基本概念後（預訓練，Pretraining），透過大量模擬考糾正錯誤來經歷後訓練（Post-training）一樣，WeatherCraft 也完全遵循這項學習範式 [Source 1, Source 2]。 

研究團隊引進了稱為 **GRPO（Group Relative Policy Optimization，群組相對策略優化）**的最新強化學習技術 [Source 1]。由於這項技術利用了直接的 Token 對數機率（Log-probabilities，各 Token 被選中機率的對數值），因此在評估 AI 預測結果與實際天氣的吻合度時，無需經過複雜且緩慢的外部評估模型，便能直接最大化下游任務的獎勵（Reward） [Source 1]。換句話說，就是讓 AI 自行判斷哪些預測更準確且更有用，藉此以驚人的速度提升實力。

---

## 現狀：以數字證明的壓倒性效能與速度

新的點子在實際現場究竟有多大成效，讓人不禁好奇。研究團隊透過全球氣象資料的標準基準 **ERA5** 資料集，徹底驗證了 WeatherCraft 的效能 [Source 1]。

其結果令人振奮：
- **預測準確度提升**：WeatherCraft 的 8 成員系集平均（Ensemble Mean，綜合多個預測結果的平均值）將第 15 天（Day-15）的正規化均方根誤差（RMSE，衡量預測值與實際值誤差的統計指標），相較於最強的比較對象——決定論性基準，**減少了高達 17.6%** [Source 1]。
- **速度革新**：應用 KV 快取（KV Caching，重複使用先前計算的鍵-值資料以消除重複運算並提升速度的技術）時，相較於現有模型 GenCast，記錄下了**約 18 倍的推論速度提升** [Source 1]。

此外，透過直接的 fair-CRPS（Continuous Ranked Probability Score，評估機率預測準確度的標準評分方式）調適方法，系集的機率性預測技術整體得到了提升；透過基於獎勵的後訓練，陸地極端溫度（Land Temperature Extremes）與耦合海洋極端熱浪（Coupled Ocean Heat Extremes）的預測能力也獲得了顯著改善 [Source 1]。比喻來說，這不只是單純拼出森林的大致輪廓，而是具備了不放過森林中各角落火種或熱氣的精確度。這顯示出 WeatherCraft 可以成為捕捉威脅人類安全的極端熱浪或海面溫度異常現象的強大武器 [Source 1]。

---

## 未來走向如何？

WeatherCraft 所提出的「基於離散 Token 的自我迴歸建模（Discrete Autoregressive Modeling）」並不僅限於天氣預報 [Source 1]。它可以成為跨領域（Cross-sphere）耦合模擬的通用基礎，將涵蓋整個地球系統的各種複雜物理現象（大氣、海洋、陸地等）交織在一起 [Source 1]。

未來，將大步邁向降低個別氣象機構對龐大超級電腦的依賴，並在一般伺服器環境中即時生成多樣且精細的機率性氣象系集情境之時代 [Source 1]。當我們計畫週末露營時，不再是拿到「降雨機率 30%」這種模糊的數字，而是由 AI 輕鬆提供數十種模擬出的精確未來大氣情境的世界正在開啟。

---

## AI 的視線

將生成式 AI 的 Token 化範式與強化學習結合，應用於長久以來被視為複雜物理定律領域的氣象學，WeatherCraft 的這項嘗試是跨越學術界線的實用性勝利。這不僅超越了單純的運算加速，更可說是展現了 AI 如何針對極端氣候預測這個人類共同難題提出實質解答的模範里程碑。

---

## 參考資料

1. [Reinforcement-Aligned Probabilistic Weather Forecasting with Discrete Tokens](https://arxiv.org/abs/2611.25570)
2. [Reinforcement-Aligned Probabilistic Weather Forecasting with ...](https://arxiv.org/pdf/2611.25570)
3. [Advancing subseasonal forecasting with machine learning](https://www.nature.com/articles/s41586-026-11126-x)
4. [WeatherCraft/configs at main · Jinhan-Li/WeatherCraft · GitHub](https://github.com/Jinhan-Li/WeatherCraft/tree/main/configs)
5. [Probabilistic Weather Forecasting System for Enhanced ...](https://www.welcome.ai/content/probabilistic-weather-forecasting-system-for-enhanced-decision-making)
6. [Probabilistic Weather Forecasting and Ensemble Prediction... | Nature](https://www.nature.com/subjects/probabilistic-weather-forecasting-and-ensemble-prediction-systems)