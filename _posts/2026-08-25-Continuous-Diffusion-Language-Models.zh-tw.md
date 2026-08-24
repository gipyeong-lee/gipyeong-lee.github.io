---
layout: post
title: "若 AI 能像繪畫般創作文字？「連續擴散」語言模型的挑戰"
description: "為什麼作為圖像生成 AI 核心技術的「擴散模型」，難以應用於文字語言模型？本文深入淺出地解析連續擴散語言模型的原理與潛力。"
summary: "介紹將應用於圖像生成的「連續擴散」技術引入文字領域的最新 AI 研究趨勢、技術難題及其發展前景。"
tags: [AI, 語言模型, 擴散模型, 人工智慧原理]
image: 2026-08-25-Continuous-Diffusion-Language-Models.jpg
image_alt: "抽象圖形，複雜的數據點沿著平滑的流動軌跡排列"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "嘗試用數學空間的幾何學解決文字的非連續性問題，這非常引人入勝。期待擴散模型能成為縮小圖像與文字之間差距的關鍵。"
quiz:
  - question: "與圖像生成 AI 不同，將「連續擴散」技術應用於文字模型的主要困難點為何？"
    choices: ["運算能力不足", "文字是單字單位的非連續性數據", "數據容量比圖像數據小"]
    answer: 1
    explanation: "圖像具有連續的像素值，但文字是由單字等個別（非連續）單位組成，因此傳統的連續擴散方式無法直接運作。"
  - question: "在連續擴散語言模型研究中，利用什麼數學概念來表示單字分佈？"
    choices: ["統計流形 (statistical manifold)", "線性回歸方程式", "量子力學"]
    answer: 0
    explanation: "最新的研究如黎曼擴散語言模型 (RDLM) 使用了統計流形（例如超球面）的幾何結構來建立單字分佈模型。"
  - question: "擴散模型目前最廣泛應用的領域是什麼？"
    choices: ["文字翻譯", "圖像與影片生成", "簡單算術運算"]
    answer: 1
    explanation: "擴散模型是目前圖像與影片生成領域中最主流的生成式 AI 方法。"
lang: zh-tw
ref: 2026-08-25-Continuous-Diffusion-Language-Models
---

試想一下，早上醒來時對 AI 助理說：「請將今天的會議資料總結並寄給我。」過去的 AI 是根據既定的機率，一個字接一個字地拼湊出內容；而新一代的 AI 則如同畫家在空白畫布上逐步完成作品般，從模糊的靈感開始，循序漸進地修飾語句。這就是近期 AI 研究界備受矚目的「連續擴散 (Continuous Diffusion) 語言模型」所勾勒的未來。

### 為什麼這項技術很重要？

目前我們使用的大多數大型語言模型（LLM，透過學習大量文字數據來像人類般寫作的 AI），皆採用按照固定順序逐字生成的「自回歸 (autoregressive)」方式。這就像只盯著前方一步距離奔跑，難以一次性宏觀地審視整篇文章的架構，存在侷限性。

相對地，橫掃圖像與影片生成領域的「擴散模型」，透過逐步精煉數據的方式，能創造出極為驚豔的成果。 [參考資料 4](https://www.youtube.com/watch?v=WqvCxdoVb64), [參考資料 9](https://discuss.pytorch.kr/t/elf-continuous-diffusion-language-model/10215) 若能將此方式成功應用於文字，將能創造出具備更佳創意與邏輯結構的寫作模型。 [參考資料 16](https://www.emergentmind.com/topics/diffusion-reasoner)

### 簡單來說：為什麼文字與圖像不同？

擴散模型本質上是一個從充滿「雜訊 (noise，即無數據的隨機狀態)」的空間中，逐步去除雜訊並還原出清晰圖像的過程。照片的亮度或色彩資訊等「像素值」是由連續數字組成的，因此這個過程連結得非常自然。 [參考資料 11](https://wandb.ai/byyoung3/ml-news/reports/Block-Diffusion-Language-Models-Combining-autoregression-and-diffusion--VmlldzoxMTg3MjU2OQ)

然而，文字的世界截然不同。若用比喻來說，圖像的世界像平緩的丘陵，而文字的世界則像斷開的階梯。「蘋果」與「梨子」兩個單字之間不存在中間值。文字由「個別碎片 (discrete tokens)」組成，難以像圖像那樣透過平滑地去除雜訊來建構內容。 [參考資料 11](https://wandb.ai/byyoung3/ml-news/reports/Block-Diffusion-Language-Models-Combining-autoregression-and-diffusion--VmlldzoxMTg3MjU2OQ)

為了克服這一點，研究人員利用「嵌入 (embedding，將單字意義配置於數學向量空間的技術)」來表示文字，使其如同存在於連續空間中的座標。 [參考資料 12](https://www.themoonlight.io/fr/review/diffusion-of-thoughts-chain-of-thought-reasoning-in-diffusion-language-models) 近期出現如「黎曼擴散語言模型 (RDLM)」等研究，將單字分佈的方式描繪成「統計流形 (statistical manifold，數據所處的複雜幾何空間)」的數學地圖。透過將單字處理為在巨大的超球面 (hypersphere) 上滾動的點，開啟了以連續方式處理文字的道路。 [參考資料 3](https://liner.com/review/continuous-diffusion-model-for-language-modeling), [參考資料 14](https://en.papernotes.org/NeurIPS2025/image_generation/continuous_diffusion_model_for_language_modeling/)

### 目前進展如何？

事實上，隨著 2022 年「Diffusion-LM」等嘗試出現，關於文字擴散模型的研究早已啟動。 [參考資料 1](https://sander.ai/2026/08/24/continuous-dlms.html) 遺憾的是，迄今為止的連續擴散方式，在性能上仍被認為稍遜於現有的逐字生成模型。 [參考資料 2](https://www.linkedin.com/posts/hangke-sui_langflow-continuous-diffusion-rivals-discrete-activity-7450571557388828674-Lv6p), [參考資料 15](https://openreview.net/forum?id=VGv5y60sXC) 雖然利用數學幾何學的新模型不斷問世，但如何搭建「語言非連續性」與「連續擴散過程」之間的橋樑，仍是人工智慧研究最前線尚未攻克的難題。 [參考資料 6](https://ai-search.io/papers/continuous-diffusion-model-for-language-modeling)

### 有何期待？

未來，這項技術有望不僅止於寫作，而是讓 AI 作為能將複雜想法分階段推論的「潛在推論者 (latent reasoner)」來活用擴散模型。 [參考資料 16](https://www.emergentmind.com/topics/diffusion-reasoner), [參考資料 17](https://www.microsoft.com/en-us/research/publication/coevolutionary-continuous-discrete-diffusion-make-your-diffusion-language-model-a-latent-reasoner/) 在同時處理文字與圖像的多模態 (multimodal) 時代，連續擴散方式將成為打破文字、影像與圖像界線的核心技術。您下一次見到的 AI 助理，將具備比現在更深層的思考能力，並能更流暢地表達自己的觀點。

### MindTickleBytes AI 記者觀點
如果擴散模型能像排列圖像像素一樣排列文字意義，我們將不僅看到 AI 進行簡單的文句生成，更將見證 AI 的思考過程轉化為一種「收斂的過程」。這將是 AI 與人類溝通更加精確的重要轉捩點。

## 參考資料
1. [Continuous diffusion language models – Sander Dieleman](https://sander.ai/2026/08/24/continuous-dlms.html)
2. [LangFlow: Continuous Diffusion Rivals Discrete Models in... | LinkedIn](https://www.linkedin.com/posts/hangke-sui_langflow-continuous-diffusion-rivals-discrete-activity-7450571557388828674-Lv6p)
3. [Continuous Diffusion Model for Language Modeling [Quick Review]](https://liner.com/review/continuous-diffusion-model-for-language-modeling)
4. [Advances in Continuous Diffusion Language Models - YouTube](https://www.youtube.com/watch?v=WqvCxdoVb64)
5. [Continuous Diffusion for Discrete Text](https://www.emergentmind.com/topics/continuous-diffusion-for-discrete-text)
6. [Continuous Diffusion Model for Language Modeling - AI for...](https://ai-search.io/papers/continuous-diffusion-model-for-language-modeling)
7. [Diffusion Language Models: How a New AI Paradigm Is Challenging...](https://www.libertify.com/interactive-library/diffusion-language-models-new-ai-paradigm/)
8. [Simple Diffusion Language Models - YouTube](https://www.youtube.com/watch?v=WjAUX23vgfg)
9. [ELF: 임베딩 공간에 머무는 연속 확산 언어 모델(Continuous Diffusion...](https://discuss.pytorch.kr/t/elf-continuous-diffusion-language-model/10215)
10. [Think In Diffusion: Continuous Latent Diffusion Language Model](https://mail.bycloud.ai/p/think-in-diffusion-continuous-latent-diffusion-language-model)
11. [Block Diffusion Language Models: Combining autoregression and...](https://wandb.ai/byyoung3/ml-news/reports/Block-Diffusion-Language-Models-Combining-autoregression-and-diffusion--VmlldzoxMTg3MjU2OQ)
12. [[Revue de papier] Diffusion of Thoughts: Chain-of-Thought Reasoning in Diffusion Language Models](https://www.themoonlight.io/fr/review/diffusion-of-thoughts-chain-of-thought-reasoning-in-diffusion-language-models)
13. [Models — Google DeepMind](https://deepmind.google/models/)
14. [[Paper Note] Continuous Diffusion Model for Language Modeling](https://en.papernotes.org/NeurIPS2025/image_generation/continuous_diffusion_model_for_language_modeling/)
15. [Continuous Diffusion Model for Language Modeling | OpenReview](https://openreview.net/forum?id=VGv5y60sXC)
16. [Diffusion Reasoners: Iterative Inference Models](https://www.emergentmind.com/topics/diffusion-reasoner)
17. [Coevolutionary Continuous Discrete Diffusion... - Microsoft Research](https://www.microsoft.com/en-us/research/publication/coevolutionary-continuous-discrete-diffusion-make-your-diffusion-language-model-a-latent-reasoner/)