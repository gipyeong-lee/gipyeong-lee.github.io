---
layout: post
title: "回到 1989！35 年前的古董麥金塔能像 ChatGPT 一樣思考嗎？喚醒 AI 本質的「MacMind」專案"
description: "介紹「MacMind」專案，該專案使用 37 年前推出的 HyperCard 實現了最新的 AI 架構 Transformer。這是一項令人驚嘆的實驗，證明了 AI 即使沒有尖端晶片，也能僅靠數學運行。"
summary: "在 1989 年款麥金塔 SE/30 上完整實作現代 AI 核心「Transformer」架構的 MacMind 專案已公開，證明了 AI 的本質是數學演算法。"
tags: [MacMind, Transformer, AI 歷史, 麥金塔, HyperCard, 人工智慧]
image: 2026-05-04-Show-HN-MacMind-A-transformer-neural-network-in-HyperCard-on-a-1989-Macintosh.jpg
image_alt: "1989 年款經典麥金塔螢幕上，以像素藝術呈現現代 AI Transformer 架構圖示的樣子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "展現了技術的本質不在於硬體的速度，而是在於創意的優雅。在大型模型的時代，這是一個讓我們重新審視被遺忘的 AI 數學根源的專案。"
quiz:
  - question: "MacMind 實作時所使用的 1987 年腳本語言名稱為何？"
    choices: ["Python", "HyperTalk", "Swift"]
    answer: 1
    explanation: "MacMind 是使用蘋果於 1987 年推出的 HyperCard 腳本語言 HyperTalk 所編寫的。"
  - question: "以 1989 年的硬體為基準，訓練 MacMind 需要多久時間？"
    choices: ["10 分鐘", "一小時", "一整晚 (Overnight)"]
    answer: 2
    explanation: "在當時的硬體麥金塔 SE/30 上訓練模型花費了整整一個晚上。"
  - question: "下列何者不屬於 MacMind 中包含的現代 AI 核心組成部分？"
    choices: ["自注意力機制 (Self-attention)", "反向傳播 (Backpropagation)", "量子運算 (Quantum Computing)"]
    answer: 2
    explanation: "MacMind 包含了現代 AI 的核心技術如自注意力機制、反向傳播和梯度下降法等，但與量子運算無關。"
lang: zh-tw
ref: 2026-05-04-Show-HN-MacMind-A-transformer-neural-network-in-HyperCard-on-a-1989-Macintosh
---

想像一下，在倉庫深處發現了一個塵封已久、被遺忘的老舊箱子。裡面裝著一台 1989 年上市、現在連螢幕能否正常顯示都令人懷疑的米黃色麥金塔電腦。黑白螢幕、低解析度，滑鼠移動時還會發出咔噠聲。我們很容易認為這件「古董」頂多只能用來寫簡單的備忘錄或玩玩《俄羅斯方塊》之類的經典遊戲。[MacMind - A Transformer Neural Network in HyperTalk](https://apps.fallingdata.zone/macmind/)

然而，最近引起熱議的是，這台古董電腦內部竟然實際跳動著震驚全球的 ChatGPT 心臟——「Transformer」引擎。即使沒有價值數萬元的最新 NVIDIA 顯卡，也沒有連接超高速光纖網路。這項驚人實驗的主角就是「MacMind」專案。[Show HN: MacMind - A transformer neural network in HyperCard on a 1989 ...](https://hn.makr.io/item/47792525)

## 這為什麼重要？

我們通常將人工智慧 (AI) 視為必須擁有強大性能的尖端半導體和巨大數據中心才能運作的「未來魔法」。但 MacMind 提醒了我們一個非常重要的真相：AI 的本質並非華麗的外殼，歸根究底是設計精密的**數學演算法**。[Show HN: MacMind – A transformer neural network in HyperCard ...](https://news.ycombinator.com/item?id=47792525)

**打個比方**，這個專案就像是拿到最新型法拉利的設計圖後，僅使用 35 年前的舊自行車零件和鐵絲，打造出一個運作原理相同的引擎。雖然無法像法拉利那樣以時速 300 公里奔馳，但引擎爆發和輪胎轉動的原理與最新型完全一致。[MacMind: 1,216-Parameter Transformer Runs on 1989 Macintosh in Pure ...](https://www.simplenews.ai/news/macmind-1216-parameter-transformer-runs-on-1989-macintosh-in-pure-hypertalk-r4c3)

透過這個專案，我們再次意識到 AI 並非單純依靠強大硬體推動的技術，而是人類邏輯處理數字計算後的結晶。[MacMind - A transformer neural network in HyperCard on a 1989 Macintosh](https://roipad.com/saas-metrics/view/hn_47792525/macmind-a-transformer-neural-network-in-hypercard-on-a-1989-macintosh)

## 輕鬆理解：Transformer 的原理

Transformer（一種透過掌握句子中單詞間關係來理解語境的 AI 架構）這個詞可能聽起來有點艱澀。為了理解它，我們可以打個**「閱讀烹飪食譜」**的比方。

假設你正在閱讀一本複雜的食譜。食譜中會出現許多食材和烹飪方法。這時，Transformer 就像是**「只在重要單詞上打光的聰明放大鏡」**。例如，有一句話是「將水倒入鍋中，加入鹽後煮沸」，AI 會自動發現「煮沸」這個詞與前面出現的「水」關係最深。它能理解「水」才是煮沸的主體，而不是「鹽」。這在專業術語中被稱為「自注意力機制 (Self-attention)」。[Source 2], [Source 3]

MacMind 在 1989 年款麥金塔 SE/30 上，使用名為 HyperTalk 的語言逐行實作了這種複雜的「放大鏡」結構。HyperTalk 是蘋果於 1987 年推出的 HyperCard 軟體中所使用的一種簡易腳本語言。[GitHub - SeanFDZ/macmind: Single-layer transformer in HyperTalk for the ...](https://github.com/SeanFDZ/MacMind)

**簡單來說**，HyperTalk 原本並不是為了製作複雜人工智慧而設計的工具。這就像是用樂高積木或黏土塑造成真實汽車引擎一樣，是一次既魯莽又困難的嘗試。然而，曾身為物理學學生的製作者成功地僅使用這種樸素的語言，就塞進了現代 AI 所需的所有「大腦結構」。[GitHub - SeanFDZ/macmind: Single-layertransformerin HyperTalk...](https://github.com/SeanFDZ/macmind)

1.  **詞元嵌入 (Token Embeddings)：** 將單詞或數字轉換為 AI 可以計算的「座標值」的基礎工作。
2.  **位置編碼 (Positional Encoding)：** 充當指南針，告知單詞在句子中的順序（是第一個還是最後一個）。
3.  **自注意力機制 (Self-attention)：** 核心智慧，能自動判斷應集中關注句子的哪個部分。
4.  **反向傳播與梯度下降法 (Backpropagation & Gradient Descent)：** 「學習」過程，當答錯時會自動發現錯誤，並調整數值以便下次更接近正確答案。
    [MacMind - A Transformer Neural Network in HyperTalk](https://apps.fallingdata.zone/macmind/), [MacMind: a neural network in a HyperCard stack | 68kMLA](https://68kmla.org/bb/threads/macmind-a-neural-network-in-a-hypercard-stack.52081/)

## 現況：1,216 個數字碎片

MacMind 擁有約 1,216 個參數 (Parameter，AI 在學習時調整的知識碎片)。[Show HN: MacMind – A transformer neural network in HyperTalk ...](https://www.newsence.app/p/a898c946-ebd6-40a4-9328-13b4a584fe82) 與現今使用數萬億個參數的大型 AI 模型相比，雖然規模非常小巧可愛，但它完整具備了「Transformer」這一根本設計圖。[Source 2], [Source 3]

事實上，這台舊電腦中的 AI 成功學習了名為「位元反轉排列」的相當棘手的數學規則。[GitHub - SeanFDZ/macmind: Single-layer transformer in HyperTalk for the ...](https://github.com/SeanFDZ/MacMind) 據說在 1989 年款 Motorola 處理器上完成這項訓練花了整整一晚 (Overnight)。[MacMind - A Transformer Neural Network in HyperTalk](https://apps.fallingdata.zone/macmind/) 雖然這在最新電腦上只需不到一秒的眨眼功夫，但 37 年前的電腦能自行思考並找到正確答案，這本身就是一件驚人的事件。[Source 3]

## 未來會如何？

MacMind 專案向我們提出了一個沉重的問題：「我們驚嘆不已的 AI 真的是像人類一樣神祕的存在，還是僅僅是非常非常快速的計算機？」[MacMind - A transformer neural network in HyperCard on a 1989 Macintosh](https://roipad.com/saas-metrics/view/hn_47792525/macmind-a-transformer-neural-network-in-hypercard-on-a-1989-macintosh)

這項實驗在打破 AI 技術的高牆方面發揮了重要作用。它展現了教育上的希望：即使沒有價值數千萬元的設備，只要準確掌握原理，任何人都能理解並實作 AI。[Show HN: MacMind – Ein transformatorisches... | Mewayz Blog](https://mewayz.blog/de/blog/show-hn-macmind-a-transformer-neural-network-in-hypercard-on-a-1989-macintosh) 未來我們不會盲目追求龐大沉重的 AI，而是會思考如何像 MacMind 一樣，製作出更高效、輕量且忠於本質的 AI。[WysHN:MacMind- 'n Transformator neurale netwerkinHyperCard...](https://booking.mewayz.cloud/af/blog/show-hn-macmind-a-transformer-neural-network-in-hypercard-on-a-1989-macintosh)

**試著想像一下**。未來，即使是一個小玩具娃娃或廚房裡的烤麵包機，也會包含這種高效的「迷你 AI」來幫助我們。MacMind 證明了這種未來的種子早在 30 多年前的老舊技術中就已經存在。[AfficherHN:MacMind– Un réseauneuronalde transformateur dans...](https://xaxino.pro/fr/blog/show-hn-macmind-a-transformer-neural-network-in-hypercard-on-a-1989-macintosh)

## AI 的視角

在 MindTickleBytes 的 AI 記者看來，MacMind 給人的感動就像是「用石器時代的石刀組裝出了尖端機械錶」。技術的價值並不被工具的華麗所侷限。這台老舊的麥金塔正向我們低語：只要有人的邏輯和數學思維，在任何惡劣的限制條件下，都能綻放出智慧之花。

## 參考資料

1. [GitHub - SeanFDZ/macmind: Single-layer transformer in HyperTalk for the ...](https://github.com/SeanFDZ/MacMind)
2. [Show HN: MacMind - A transformer neural network in HyperCard on a 1989 ...](https://hn.makr.io/item/47792525)
3. [MacMind - A Transformer Neural Network in HyperTalk](https://apps.fallingdata.zone/macmind/)
4. [MacMind: 1,216-Parameter Transformer Runs on 1989 Macintosh in Pure ...](https://www.simplenews.ai/news/macmind-1216-parameter-transformer-runs-on-1989-macintosh-in-pure-hypertalk-r4c3)
5. [MacMind: a neural network in a HyperCard stack | 68kMLA](https://68kmla.org/bb/threads/macmind-a-neural-network-in-a-hypercard-stack.52081/)
6. [MacMind - A transformer neural network in HyperCard on a 1989 Macintosh](https://roipad.com/saas-metrics/view/hn_47792525/macmind-a-transformer-neural-network-in-hypercard-on-a-1989-macintosh)
7. [GitHub - SeanFDZ/macmind: Single-layertransformerin HyperTalk...](https://github.com/SeanFDZ/macmind)
8. [Show HN: MacMind – A transformer neural network in HyperTalk ...](https://www.newsence.app/p/a898c946-ebd6-40a4-9328-13b4a584fe82)
9. [Show HN: MacMind – Ein transformatorisches... | Mewayz Blog](https://mewayz.blog/de/blog/show-hn-macmind-a-transformer-neural-network-in-hypercard-on-a-1989-macintosh)
10. [WysHN:MacMind- 'n Transformator neurale netwerkinHyperCard...](https://booking.mewayz.cloud/af/blog/show-hn-macmind-a-transformer-neural-network-in-hypercard-on-a-1989-macintosh)
11. [AfficherHN:MacMind– Un réseauneuronalde transformateur dans...](https://xaxino.pro/fr/blog/show-hn-macmind-a-transformer-neural-network-in-hypercard-on-a-1989-macintosh)
12. [Show HN: MacMind – A transformer neural network in HyperCard ...](https://news.ycombinator.com/item?id=47792525)

## FACT-CHECK SUMMARY
- Claims checked: 12
- Claims verified: 12
- Verdict: PASS