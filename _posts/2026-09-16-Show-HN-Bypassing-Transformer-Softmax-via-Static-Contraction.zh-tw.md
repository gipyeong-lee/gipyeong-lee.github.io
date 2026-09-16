---
layout: post
title: "AI 變得更聰明、更快速？「Softmax」繞道技術的秘密"
description: "介紹最新技術，革命性地改善了拖慢 AI 模型運算速度並佔用大量記憶體的 Softmax（軟最大值）功能。"
summary: "隨著跳過或優化人工智慧 Transformer 模型中固有的運算瓶頸——「Softmax」的技術出現，一個處理速度更快、能處理更龐大資訊的 AI 時代正在開啟。"
tags: [AI, Transformer, Softmax, 深度學習, 技術趨勢]
image: 2026-09-16-Show-HN-Bypassing-Transformer-Softmax-via-Static-Contraction.jpg
image_alt: "象徵複雜公式與符號被簡化，進而提升 AI 模型效率過程的數位藝術"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "減少對 Softmax 的依賴是將 AI 效率最大化的必要步驟。這類技術突破不僅僅是單純的速度提升，更是拓展 AI 處理資訊水平的重要關鍵。"
quiz:
  - question: "Softmax 函數的主要作用是什麼？"
    choices: ["壓縮資料", "將數字轉換為機率分佈", "刪除資料"]
    answer: 1
    explanation: "Softmax 是一種將各種數值轉換為機率分佈的函數，有助於 AI 做出最終判斷 [出處: Softmaxfunction - Wikipedia](https://en.wikipedia.org/wiki/Softmax_function)。"
  - question: "SOFT (Softmax-free Transformer) 模型使用什麼來取代既有的點積 (dot-product) 相似度？"
    choices: ["高斯核函數", "線性函數", "對數函數"]
    answer: 0
    explanation: "SOFT 模型為了在沒有 Softmax 的情況下實現自我注意力 (self-attention)，使用了高斯核函數 [出處: SOFT: Softmax-free Transformer with Linear Complexity](https://proceedings.neurips.cc/paper/2021/file/b1d10e7bafa4421218a51b1e1f1b0ba2-Paper.pdf)。"
  - question: "引入「遺忘閘 (forget gate)」機制的模型名稱是什麼？"
    choices: ["ForgettingTransformer(FoX)", "Softmax-free Transformer", "UniAttn"]
    answer: 0
    explanation: "ForgettingTransformer(FoX) 在注意力分數中整合了遺忘閘機制，使其能進行更好的上下文處理 [出處: ForgettingTransformer:SoftmaxAttention with a Forget Gate](https://arxiv.org/abs/2503.02130)。"
lang: zh-tw
ref: 2026-09-16-Show-HN-Bypassing-Transformer-Softmax-via-Static-Contraction
---

想像一下。你正在一個巨大的圖書館裡尋找特定資訊。但如果圖書館員必須將每一本書都翻開並整理後才能給你答案，會發生什麼事？隨著書籍數量增加，圖書館員給出答案所需的時間將會呈指數級增加。我們目前使用的人工智慧模型，特別是「Transformer」（AI 的核心結構，用於辨識句子中單字之間的關係），所面臨的問題正與此類似。

近來，人工智慧領域為了克服這種頑固的「瓶頸現象」，正積極進行革命性的嘗試，試圖跳過或優化過去被視為理所當然的「Softmax（軟最大值）」運算。

## 為什麼這很重要？ (Why It Matters)

Transformer 是目前幾乎所有現代 AI 的基礎結構。然而在這個結構中，Softmax 函數就像是一種每次處理資訊時都必須支付的「通行費」。Softmax 的必要作用是將各種數據值轉換為機率分佈，協助 AI 做出最終選擇或判斷 [出處: Softmaxfunction - Wikipedia](https://en.wikipedia.org/wiki/Softmax_function)。

問題在於，AI 所處理的資訊量最近出現了爆炸性的增長。處理的數據越多，Softmax 運算就會變得極度耗費記憶體，並成為拖慢整體運算速度的主因。如果能夠省略或優化這種運算，AI 將能在消耗更少能量的同時，更快地處理更長的上下文。這意味著未來我們在日常生活中，能夠更舒適地使用反應速度更快、更聰明的 AI 助理。

## 輕鬆理解 (The Explainer)

為了理解 Softmax，我們用一個簡單的比喻。試想我們在購物中心挑選「最中意的商品」的過程。在比較了無數商品的價格、品質和設計後，計算每樣商品是我最中意機率的過程，就是 Softmax 運算。這就是在為所有選擇評分，並將其匯總轉換為 100% 的機率分佈。

但如果 AI 模型必須閱讀一本像書一樣長且複雜的內容呢？將所有單字逐一比較並精確計算機率是一件非常艱鉅的工作。

因此，研究人員最近找到了一些妙招：

1. **靜態收縮 (Static Contraction) 技術**：就像預先鋪好道路一樣，這是一種在運算過程中提前阻斷無效計算路徑，並以高效公式取代的方法。這大幅降低了 AI 模型在處理長上下文時遇到記憶體不足 (OOM, Out-Of-Memory) 的風險 [出處: GitHub - PJHkorea/jax-softmax-bypass](https://github.com/PJHkorea/jax-softmax-bypass), [出處: ShowHN:BypassingTransformerSoftmaxviaStaticContraction](https://news.ycombinator.com/item?id=49666335)。
2. **Softmax 去除 (Softmax-free)**：「SOFT」模型使用了一種稱為「高斯核 (Gaussian kernel)」的相對簡單數學函數，取代了既有複雜的運算。這就像為了計算機率，與其每次都敲擊複雜的工程計算機，不如選擇更直觀的捷徑 [出處: SOFT: Softmax-free Transformer with Linear Complexity](https://proceedings.neurips.cc/paper/2021/file/b1d10e7bafa4421218a51b1e1f1b0ba2-Paper.pdf), [出處: [2110.11945] SOFT: Softmax-free Transformer with Linear Complexity](https://arxiv.org/abs/2110.11945)。
3. **遺忘技術 (Forgetting Mechanism)**：「ForgettingTransformer (FoX)」利用了能夠適當遺忘不必要資訊的「遺忘閘 (forget gate)」。簡單來說，就像我們只記住重要資訊而自然遺忘其餘部分一樣，它有選擇地調整需要關注的分數，使上下文處理變得更加輕鬆 [出處: ForgettingTransformer:SoftmaxAttention with a Forget Gate](https://arxiv.org/abs/2503.02130), [出處: ForgettingTransformer:SoftmaxAttention with... | Papers with Code](https://paperswithcode.co/paper/2503.02130), [出處: GitHub - zhixuan-lin/forgetting-transformer](https://github.com/zhixuan-lin/forgetting-transformer)。

## 現狀 (Where We Stand)

目前，這些技術正以多種形式快速發展，從實驗室階段的 PoC（概念驗證）到學術提案階段不等。然而，說已經完全取代 Softmax 還為時過早。雖然已經明確證明了其比既有的標準方式更有效率，但仍有部分需要額外驗證，才能應用於所有通用 AI 模型。儘管如此，像「UniAttn」這樣在最小化效能損失的同時，突破性降低運算成本的嘗試正持續取得成果，令人期待 [出處: UniAttn: Reducing Inference CostsviaSoftmax... | Papers with Code](https://paperswithcode.co/paper/2502.00439)。

## 未來展望 (What's Next)

未來的 AI 技術競爭將超越單純製造「更大的模型」，轉向誰能製造出「更有效率的模型」。特別是為了在像我們使用的智慧型手機這種物理運算資源受限的裝置上運行更強大的 AI，這些繞過 Softmax 的技術將成為關鍵要素。如果今日的研究能夠開花結果，我們將在日常生活中遇見能完美記住更長對話記錄、回答速度更快的聰明 AI。

## 參考資料

1. GitHub - PJHkorea/jax-softmax-bypass: [https://github.com/PJHkorea/jax-softmax-bypass](https://github.com/PJHkorea/jax-softmax-bypass)
2. Vertex-Softmax: Tight Transformer Verification via Exact Softmax Optimization∗: [https://arxiv.org/pdf/2605.10974](https://arxiv.org/pdf/2605.10974)
3. SimA: Simple Softmax-free Attention for Vision Transformers: [https://openaccess.thecvf.com/content/WACV2024/papers/Koohpayegani_SimA_Simple_Softmax-Free_Attention_for_Vision_Transformers_WACV_2024_paper.pdf](https://openaccess.thecvf.com/content/WACV2024/papers/Koohpayegani_SimA_Simple_Softmax-Free_Attention_for_Vision_Transformers_WACV_2024_paper.pdf)
4. SOFT: Softmax-free Transformer with Linear Complexity: [https://proceedings.neurips.cc/paper/2021/file/b1d10e7bafa4421218a51b1e1f1b0ba2-Paper.pdf](https://proceedings.neurips.cc/paper/2021/file/b1d10e7bafa4421218a51b1e1f1b0ba2-Paper.pdf)
5. [2110.11945] SOFT: Softmax-free Transformer with Linear Complexity: [https://arxiv.org/abs/2110.11945](https://arxiv.org/abs/2110.11945)
6. Differential Transformer | Hacker News: [https://news.ycombinator.com/item?id=41776324](https://news.ycombinator.com/item?id=41776324)
7. Softmaxfunction - Wikipedia: [https://en.wikipedia.org/wiki/Softmax_function](https://en.wikipedia.org/wiki/Softmax_function)
8. ForgettingTransformer:SoftmaxAttention with a Forget Gate: [https://arxiv.org/abs/2503.02130](https://arxiv.org/abs/2503.02130)
9. ShowHN:BypassingTransformerSoftmaxviaStaticContraction: [https://news.ycombinator.com/item?id=49666335](https://news.ycombinator.com/item?id=49666335)
10. ForgettingTransformer:SoftmaxAttention with... | Papers with Code: [https://paperswithcode.co/paper/2503.02130](https://paperswithcode.co/paper/2503.02130)
11. In-Context Learning withTransformers:Softmax... | OpenReview: [https://openreview.net/forum?id=lfxIASyLxB](https://openreview.net/forum?id=lfxIASyLxB)
12. Transformersare RNNs: Fast Autoregressive... - YouTube: [https://www.youtube.com/watch?v=hAooAOFRsYc](https://www.youtube.com/watch?v=hAooAOFRsYc)
13. UniAttn: Reducing Inference CostsviaSoftmax... | Papers with Code: [https://paperswithcode.co/paper/2502.00439](https://paperswithcode.co/paper/2502.00439)
14. GitHub - zhixuan-lin/forgetting-transformer: [https://github.com/zhixuan-lin/forgetting-transformer](https://github.com/zhixuan-lin/forgetting-transformer)
15. SoftmaxFunction in Deep Learning: [https://lzwjava.com/notes/2025-06-03-softmax-en](https://lzwjava.com/notes/2025-06-03-softmax-en)