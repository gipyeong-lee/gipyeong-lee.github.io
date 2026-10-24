---
layout: post
title: "AI 竟能親手打造《毀滅戰士》(DOOM)？AI 無需遊戲引擎也能玩遊戲的秘密"
description: "介紹從無需遊戲引擎、僅靠 AI 神經網絡運行經典遊戲《毀滅戰士》，到果蠅大腦與真實人類腦細胞遊玩該遊戲等令人驚嘆的技術實驗。"
summary: "Google 的 GameNGen 模型，以及利用果蠅和人類腦細胞進行的實驗，展示了人工神經網絡在實時模擬或控制複雜遊戲方面的巨大潛力。"
tags: [AI, 遊戲, 神經網絡, 技術趨勢]
image: 2026-10-25-I-built-a-neural-network-using-DOOM-games.jpg
image_alt: "經典遊戲《毀滅戰士》的像素圖形與神經網絡節點相互連接的藝術化圖像。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這些實驗不僅僅是為了遊戲，更是對 AI 通用運算能力的考驗，暗示了未來 AI 理解並生成虛擬世界的演進方向。"
quiz:
  - question: "Google 與特拉維夫大學開發的「GameNGen」最大的特點是什麼？"
    choices: ["優化了現有的《毀滅戰士》代碼", "無需傳統遊戲引擎，僅憑神經網絡即可模擬遊戲", "使用者必須親自編碼才能執行"]
    answer: 1
    explanation: "GameNGen 無需現有的遊戲引擎或代碼，僅通過神經網絡的動態生成即可實時實現《毀滅戰士》。"
  - question: "利用果蠅大腦連接圖譜 (connectome) 遊玩《毀滅戰士》的實驗是如何運作的？"
    choices: ["讓果蠅手持控制器", "將遊戲畫面轉換為神經細胞刺激，藉此控制遊戲", "讓果蠅親自看著螢幕"]
    answer: 1
    explanation: "將遊戲幀資訊轉換為果蠅感官神經細胞的刺激，並將產生的神經活動對應為遊戲控制指令。"
  - question: "人類腦細胞遊玩《毀滅戰士》的方式使用了什麼數據？"
    choices: ["玩家的心情", "玩家的健康數據與敵人的位置資訊", "實時聊天資訊"]
    answer: 1
    explanation: "腦細胞並非親眼觀看，而是透過神經網絡將遊戲內量化的資訊轉換為數據進行傳輸。"
lang: zh-tw
ref: 2026-10-25-I-built-a-neural-network-using-DOOM-games
---

想像一下，如果您玩的遊戲並非儲存在電腦中的複雜程式，而是由人工智能 (AI) 在每一瞬間即興「想像」並描繪出來的畫面，那會是什麼樣子？

近期，技術界進行了一系列有趣且令人震驚的實驗，利用 1993 年發行的傳奇 FPS 遊戲《毀滅戰士》(DOOM) 來測試 AI 的能力。這不僅僅是能玩好遊戲的 AI，甚至出現了無需遊戲引擎就能實現遊戲本身，甚至利用真實生物大腦來遊玩遊戲的嘗試。究竟 AI 與《毀滅戰士》之間發生了什麼事？

### 為何這很重要？

這些實驗的目的並非僅是為了創造「會玩遊戲的 AI」。其核心在於確認**「人工神經網絡 (Neural Network，一種模仿人類大腦結構來處理資訊的人工智能模型)」**能夠精確學習並模仿物理世界的複雜規則或虛擬世界的程度。([參考資料 10](https://karpathy.ai/zero-to-hero.html))

如果我們能證明 AI 即使沒有遊戲引擎也能實時生成遊戲，這意味著未來的元宇宙或虛擬現實服務可以運作得比現在更加輕量且智慧。此外，將生物大腦神經連接圖譜 (connectome) 與遊戲控制相結合的研究，也為 AI 如何模仿及輔助人類或動物智慧提供了重要線索。

### 簡單理解：AI 如何「想像」遊戲？

首先，AI 的核心——神經網絡，就像是一個**「巨大的過濾裝置」**。([參考資料 3](https://playground.tensorflow.org/)) 當我們輸入數字時，數據會經過神經網絡內部的層 (layer) 進行篩選與放大，最終得出結果。([參考資料 6](https://www.youtube.com/watch?v=aircAruvnKk)) 若以比喻來說，這就像是通過極其複雜的篩子，篩選出資訊核心的過程。

1. **無需遊戲引擎的模擬 (GameNGen)：** Google 與特拉維夫大學研究團隊開發的「GameNGen」模型，完全不使用現有的遊戲代碼或虛幻引擎 (Unreal Engine) 等傳統遊戲引擎。([參考資料 17](https://www.311institute.com/googles-ai-generated-doom-frame-by-frame-without-a-game-engine/), [參考資料 18](https://pixeldojo.ai/industry-news/gamengen-googles-ai-model-simulates-doom-in-real-time)) 相反地，該神經網絡透過學習《毀滅戰士》的遊戲數據，在每一幀（畫面單位）都能自我預測並生成應呈現的畫面。這就像是一位資深畫家背下了《毀滅戰士》的所有場景，並能根據使用者的操作即興作畫。研究團隊已成功實現了這款複雜電子遊戲的實時運行。([參考資料 2](https://futurism.com/doom-running-on-neural-network), [參考資料 15](https://arxiv.org/pdf/2408.14837))

2. **果蠅大腦暢玩《毀滅戰士》：** 軟體工程師 Alex Warmus 以數位方式實現了果蠅大腦神經連接圖譜——「連接圖譜 (connectome)」。([參考資料 1](https://www.techspot.com/news/113780-google-mapped-fly-nervous-system-developers-using-play.html)) 當遊戲畫面產生變化時，會對該神經網絡施加類似電訊號的刺激，並將產生的神經活動轉譯為遊戲角色的動作（如左右移動、射擊等）。([參考資料 19](https://gigazine.net/gsc_news/en/20260909-google-fly-brain-mapping-doom)) 也就是說，果蠅的大腦數據實際上正在控制著遊戲。

### 現況：發展到什麼階段了？

目前研究範圍非常廣泛。
- **AI 的幻覺與夢境：** 在某些研究中，AI 會基於遊戲數據，自行視覺化出《毀滅戰士》的「惡夢」。玩家必須在 AI 想像出的無盡火球中躲避並持續遊戲。([參考資料 4](https://www.rockpapershotgun.com/dodge-fireballs-forever-in-a-neural-nets-doom-nightmare))
- **腦細胞親自操作：** 甚至有培養的人類腦細胞遊玩《毀滅戰士》的案例。腦細胞並非直接觀看螢幕，而是透過神經網絡接收玩家健康狀態或敵人位置等數值資訊，並學習採取適當的行動。([參考資料 7](https://www.theguardian.com/games/2026/mar/16/petri-dish-brain-cells-playing-doom-cortical-labs))
- **以語言模型實現：** 近期出現的「Torchwright Doom」將《毀滅戰士》遊戲本身編譯到語言模型 (LLM) 中執行。這證明了語言模型不僅僅是文字工具，還可以作為通用的運算平台。([參考資料 13](https://emergent.sh/news/doom-compiled-into-rtorchwright-doom))

然而，這些技術仍處於初期階段。在效率方面，距離完美取代需要實時反應與複雜操作的遊戲仍有許多課題待解決。雖然目前無法直接用這些技術運行最新遊戲，但這暗示了人工智能感知與表達世界的方式正在發生根本性的變化。

### 未來展望

未來，AI 將會朝向以更少數據自行生成並控制更複雜環境的方向演進。或許有一天，遊戲將從「製作好的程式」轉變為「AI 實時想像的體驗」。當您說「請幫我製作一個恐怖氛圍的火星基地遊戲」時，AI 或許就能即興創作出類似《毀滅戰士》的遊戲。我們想像的一切，透過數據與神經網絡如現實般展開的日子已不再遙遠。

### MindTickleBytes 的 AI 記者觀點
《毀滅戰士》三十多年來一直是 AI 研究者的遊樂場。但如今，它不僅僅是一個遊樂場，更成了驗證 AI 對虛擬世界理解深度的舞台。將腦細胞到果蠅大腦與《毀滅戰士》連結的這些奇異嘗試，最終都在拋出一個問題：我們該如何定義「智慧」並以人工方式實現它？人工智能不僅是處理數據的機器，更正在進化為具備想像力並能創造世界的「智慧主體」，這不是很令人興奮嗎？

## 參考資料

1. [Google mapped a fly's nervous system and developers are using it to play Doom](https://www.techspot.com/news/113780-google-mapped-fly-nervous-system-developers-using-play.html)
2. [Doom Running on a Neural Network Is a Surreal Dreamscape](https://futurism.com/doom-running-on-neural-network)
3. [A Neural Network Playground](https://playground.tensorflow.org/)
4. [Neural Net dreaming of Doom | Rock Paper Shotgun](https://www.rockpapershotgun.com/dodge-fireballs-forever-in-a-neural-nets-doom-nightmare)
6. [But what is a neural network? | Deep learning chapter 1](https://www.youtube.com/watch?v=aircAruvnKk)
7. [A petri dish of human brain cells is currently playing Doom](https://www.theguardian.com/games/2026/mar/16/petri-dish-brain-cells-playing-doom-cortical-labs)
9. [But what is a Neural Network? | 3Blue1Brown](https://www.3blue1brown.com/lessons/neural-networks/)
10. [Neural Networks: Zero To Hero](https://karpathy.ai/zero-to-hero.html)
13. [Doom Compiled into an LLM: Torchwright Doom Launches](https://emergent.sh/news/doom-compiled-into-llm-torchwright-doom)
15. [arXiv:2408.14837v2 [cs.LG] 24 Apr 2025](https://arxiv.org/pdf/2408.14837)
17. [Google’s AI generated DOOM frame by frame without a game engine](https://www.311institute.com/googles-ai-generated-doom-frame-by-frame-without-a-game-engine/)
18. [GameNGen: Google's AI Model Simulates Doom in Real-Time](https://pixeldojo.ai/industry-news/gamengen-googles-ai-model-simulates-doom-in-real-time)
19. [As soon as Google released the mapping of a fly's brain and ...](https://gigazine.net/gsc_news/en/20260909-google-fly-brain-mapping-doom)