---
layout: post
title: "AI 晶片市場的新挑戰：『Transformer 專用』Sohu 晶片能否跨越輝達（Nvidia）的高牆？"
description: "這篇文章將深入淺出地解釋威脅輝達 GPU 的新 AI 晶片——Etched 的「Sohu」晶片究竟是什麼，以及為什麼它專為 Transformer 模型而設計。"
summary: "由 Etched 開發的「Sohu」是一款專為 Transformer 模型設計的專用晶片，與通用 GPU 相比，它能提供更快、更廉價且更具效率的 AI 效能。"
tags: [AI, 硬體, Etched, 輝達, Sohu]
image: 2026-08-24-Etched-Sohu-vs-Nvidia-Transformer-ASIC-vs-GPU-2026-Spheron-Blog.jpg
image_alt: "將 Transformer AI 模型結構具象化的未來感半導體晶片影像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是通用性與效率之間的對決。Sohu 在特定任務上展現了極致的效率，但因捨棄了硬體的靈活性，未來能否迅速應對 AI 演算法的變革將是關鍵。"
quiz:
  - question: "Etched 的 Sohu 晶片比傳統 GPU 更有效率的原因是什麼？"
    choices: ["搭載了更大的記憶體", "將 Transformer 結構直接設計於硬體電路中", "使用了更廉價的材料"]
    answer: 1
    explanation: "Sohu 是因為將 Transformer 模型的核心功能直接以硬體電路實現，從而減少了軟體處理過程。"
  - question: "Sohu 晶片專精於哪種類型的任務？"
    choices: ["各類電腦遊戲", "Transformer 系列 AI 模型", "高畫質影片剪輯"]
    answer: 1
    explanation: "Sohu 是一款專門用於執行 GPT 或 Llama 等 Transformer 模型的專用晶片（ASIC）。"
  - question: "根據效能比較數據，Sohu 晶片相較於傳統 GPU 具備什麼優勢？"
    choices: ["速度更慢但更便宜", "相似的速度與功耗效率", "最高 20 倍的處理速度"]
    answer: 2
    explanation: "Sohu 宣稱相較於現有的輝達 H100 GPU，處理速度最高可提升 20 倍，且具備更高的功耗效率。"
lang: zh-tw
ref: 2026-08-24-Etched-Sohu-vs-Nvidia-Transformer-ASIC-vs-GPU-2026-Spheron-Blog
---

想像一下。早上起床對智慧型手機的 AI 說：「幫我整理這 3 份會議資料並告訴我重點。」現在的 AI 為了完成這項任務，必須經過複雜的計算過程，有時甚至需要等待數秒。但如果把這個 AI 的思考方式直接製造成硬體晶片，一發出指令，0.1 秒內結果就出來了，會怎樣呢？最近在 AI 硬體市場發生的，正是這種驚人的變化。

### 這為何重要？ (Why It Matters)

我們目前使用的大多數強大 AI，都是在輝達（Nvidia）的 GPU（圖形處理器）上運行。然而，最近 AI 新創公司 Etched 在獲得 103 億美元（約 14 兆韓元）的企業估值後，震撼了整個市場 [Source 14, Source 15]。原因很簡單，他們製造的不是「什麼都做」的萬能 GPU，而是只執行 AI 引擎——「Transformer」模型的專用晶片「Sohu」 [Source 5, Source 13]。

這項轉變之所以至關重要，是因為它能降低 AI 成本並大幅提升速度。據傳，原本需要高達 160 台輝達 GPU 才能完成的龐大任務，現在只需一台搭載 8 顆 Sohu 晶片的伺服器即可取代 [Source 1, Source 3]。對一般用戶而言，這是一個確切的信號，預示著比現在更快速、更聰明的 AI，將能以更低成本普及的時代即將到來。

### 淺顯易懂的解釋 (The Explainer)

讓我們用一個比喻來說明。現有的輝達 GPU 就像是**「萬能廚師」**。他們擁有非常靈活的技術，能做出韓式、西式、中式、日式等所有料理。但也因為這樣，無論要做什麼菜，都需要花時間準備廚具、處理食材。在電腦術語中，這稱為「透過軟體處理」 [Source 4, Source 6]。

另一方面，Etched 的 Sohu 晶片則是**「泡菜鍋專用機器人」**。它將製作泡菜鍋的方法直接固定在機器人的骨架與機械裝置中。不需要另外拿出廚具，只要按下按鈕，完美的泡菜鍋就會出來。Sohu 晶片正是將 Transformer（一種判斷句子中單字間關係的 AI 結構）這份食譜，直接烙印在硬體電路中 [Source 4, Source 5]。

Sohu 將 Transformer 模型理解句子時使用的核心技術——「注意力（Attention）」直接實現為專用電路 [Source 6]。因此，當一般 GPU 因為要經過複雜的軟體過程而只能發揮 30~40% 的效能時，Sohu 可以將晶片效能的 80~90% 全數投注在該任務上 [Source 6, Source 7]。

### 現況 (Where We Stand)

Sohu 是採用 4 奈米（nm）製程製造的最尖端半導體 [Source 2, Source 6]。從目前發布的技術數據來看，出現了相當驚人的數字。他們宣稱在 Llama 70B 等大型語言模型中，每秒可以處理 50 萬個 Token（AI 讀取的字元單位） [Source 1, Source 14]。

當然，極限也很明確。「泡菜鍋專用機器人」無法做出義大利麵，Sohu 除了 Transformer 基礎的 AI 模型外，無法執行任何其他工作 [Source 4, Source 5]。輝達 GPU 擁有從科學研究到遊戲圖形處理，什麼都能做的「通用性」這項強大武器 [Source 13]。Etched 也明確承認了除了這種 Transformer 架構外無法使用的事實，同時也面臨著必須克服複雜的混合專家模型（MoE）等方面所顯現的侷限性等課題 [Source 16]。

### 未來發展 (What's Next)

未來 AI 硬體市場將是「通用型 GPU」與「專用型晶片（ASIC）」之間的激烈對決。Etched 已經透過獲得數億美元的資金，向市場證明了這項技術的可能性 [Source 6, Source 14]。專家預測，這種趨勢將使 AI 推論（Inference，已學習的 AI 在實際問題中進行回答的過程）成本降低至原先的 10 分之 1 [Source 2, Source 3]。

各位讀者接下來可以觀察「有多少 AI 模型能更自然地融入我們的生活中」。因為當 Sohu 這樣高效的晶片普及後，原本因伺服器成本過高而不敢想像的高階 AI 功能，將能更輕鬆地融入我們的智慧型手機或日常生活家電中。

### MindTickleBytes AI 記者的視角
硬體將特定的演算法強制進行硬編碼，就像是製作了一個只能完美聽懂特定語言的專用翻譯機。這象徵性地顯示了 AI 技術已完全固化在特定方向上。輝達的靈活性與 Etched 的效率，最終誰會成為更廣大市場的支配者，將會是 2026 年科技界最有趣的看點。

## 參考資料
1. [Etched Sohu vs NVIDIA: Transformer ASIC vs GPU (2026) | Spheron Blog](https://www.spheron.network/blog/etched-ai-sohu-vs-nvidia-transformer-asic-inference/)
2. [Etched’s $500M Sohu Chip Takes Aim at Nvidia](https://theaiworld.org/news/etcheds-500m-sohu-chip-takes-aim-at-nvidia)
3. [Independent AI Chip Companies Challenging NVIDIA in 2026](https://hashrateindex.com/blog/independent-ai-chip-companies-ai-asic-market-part-3/)
4. [Etched Just Raised $300M at a $10.3B Valuation for a Chip That Can Only Run Transformers — And It's Beating Nvidia's Blackwell by 10x](https://www.nguyen-ly-thanh.com/en/blog/etched-sohu-transformer-chip-nvidia-inference-2026)
5. [Etched Sohu: the ASIC born solely to run Transformers](https://foro3d.com/en/2026/mayo/etched-sohu-el-asic-que-nacio-solo-para-ejecutar-transformers.html)
6. [Transformer Chip Startup Etched Exits Stealth: $800M Raised, $1B in Contracts](https://www.techtimes.com/articles/319393/20260630/transformer-chip-startup-etched-exits-stealth-800m-raised-1b-contracts.htm)
7. [AI Startup Etched Unveils Transformer ASIC Claiming 20x Speed-up Over NVIDIA H100 | TechPowerUp](https://www.techpowerup.com/323887/ai-startup-etched-unveils-transformer-asic-claiming-20x-speed-up-over-nvidia-h100)
13. [Etched's Jump From $5B to $20B: What aTransformer-Only AI Chip...](https://carussignal.com/etched-5b-to-20b-transformer-chip-nvidia/)
14. [Etched $300M Sohu Chip Rivals Nvidia H100 | TechPillow](https://www.techpillow.co/blog/etched-sohu-asic-chip-300m-transformer-inference-2026)
15. [AI Chip Startup Etched Reaches 10.3 Billion Valuation to ...](https://explore.n1n.ai/blog/etched-ai-chip-startup-valuation-nvidia-competitor-2026-07-24)
16. [Etched AI Review 2026: Sohu Chip Benchmarks and Limits](https://fast.io/resources/etched-ai-review-2026/)