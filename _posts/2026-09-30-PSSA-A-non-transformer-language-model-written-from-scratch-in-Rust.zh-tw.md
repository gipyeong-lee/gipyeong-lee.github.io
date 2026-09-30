---
layout: post
title: "AI 產業的叛逆？不使用 Transformer 的語言模型 'PSSA' 問世"
description: "我們來探討 PSSA，這是一款不使用 GPT 等 Transformer 架構，而是完全從零開始、僅使用 Rust 語言編寫的 AI 模型。"
summary: "在 Transformer 架構主宰的 AI 世界中，不使用 PyTorch 或 TensorFlow 等既有工具，僅以 Rust 語言從零構建獨家「非 Transformer」AI 模型 'PSSA' 的嘗試正受到矚目。"
tags: [AI, PSSA, Rust, 語言模型, 程式設計]
image: 2026-09-30-PSSA-A-non-transformer-language-model-written-from-scratch-in-Rust.jpg
image_alt: "結合了 Rust 程式語言標誌與人工智慧神經網路結構的抽象數位藝術圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "挑戰主流架構是 AI 發展的根基。期待在重視效率與掌控力的 Rust 環境中，能誕生出新的可能性。"
quiz:
  - question: "PSSA 模型最大的技術特徵是什麼？"
    choices: ["完全複製 GPT-4 模型", "僅使用 Rust 語言且不依賴框架直接構建", "基於 PyTorch 進行最佳化"]
    answer: 1
    explanation: "PSSA 完全沒有使用現有的機器學習框架（如 PyTorch 或 TensorFlow），而是僅使用 Rust 語言從零開始直接構建的模型。"
  - question: "PSSA 具有什麼樣的結構特徵？"
    choices: ["完全遵循 Transformer 架構", "是非 Transformer 模型", "是圖像生成專用模型"]
    answer: 1
    explanation: "PSSA 開發時採用的並非統治近期 AI 業界的 Transformer 結構，而是獨家的「非 Transformer」語言模型方式。"
  - question: "關於 PSSA 的文字處理方式，下列何者正確？"
    choices: ["一次處理整個句子", "以 Token 為單位逐一循序處理", "將圖像數據轉換為 Token"]
    answer: 1
    explanation: "PSSA 並非一次處理所有文字，而是以 Token（單詞碎片）為單位逐一讀取，並在執行過程中自行管理權重。"
lang: zh-tw
ref: 2026-09-30-PSSA-A-non-transformer-language-model-written-from-scratch-in-Rust
---

想像一下。有一位廚師，他不使用我們常用的複雜組合式廚房工具，僅憑雙手和一把刀就能做出精緻的料理。由於不使用現成的模具，廚師的實力完全顯露無遺，但也因此能完美掌控整個烹飪過程。現在 AI 產業中發生的事情正是如此。

### 這為何重要？

過去幾年，AI 生態系中，「Transformer」（一種透過掌握句子中單字間關係來理解語境的 AI 核心結構）的巨大藍圖幾乎成為所有語言模型的標準。然而，最近出現了一個名為「PSSA」的專案，在這種穩固的秩序中掀起了波瀾。[GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa) 這個專案脫離了 Transformer 的權威，是用系統程式語言「Rust」從零開始直接堆疊而成的非 Transformer 語言模型。[PSSA: A non-transformer language model](https://news.ycombinator.com/item?id=49903993) 對一般人來說，這可能只是單純的技術差異，但它暗示了一種革命性的可能性：我們或許能以根本不同的方式來「製作 AI」。

### 簡單來說：拋棄 AI 的「現成模具」

目前大多數的 AI 模型都是在龐大的工具箱（如 PyTorch 或 TensorFlow）上開發的。就像堆疊樂高積木一樣，導入並配置已驗證的既有組件。但 PSSA 拒絕使用這些既有的機器學習框架。[GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)

比喻來說，如果 Transformer 模型是用標準化製程生產的零件組裝而成的機器，那麼 PSSA 就是直接冶煉原料、切割螺絲所打造出的職人精神結晶。這個模型並非一次讀取全文，而是以 Token（單詞碎片）為單位進行循序處理，並自行管理權重（AI 學習後獲得的知識數值）。[GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)

### 現狀：進展到哪裡了？

當然，PSSA 目前還無法取代我們所使用的巨大 AI 模型。目前的 AI 產業受惠於主流 Transformer 架構卓越的效率與通用性，正呈現飛躍式發展。[【AI】打破Transformer的霸權？](https://clawd.org.cn/forum/post?id=39804)

即便如此，這種嘗試以 Rust 等具備強大硬體控制能力的語言，從 AI 基礎開始重建的嘗試依然令人振奮。Rust 在 AI 領域中已廣泛應用於推理引擎或向量資料庫管理，並證明了其性能。[Rust Ecosystem for AI & LLMs](https://hackmd.io/@Hamze/Hy5LiRV1gg) PSSA 的出現意味著 Rust 生態系現在已經達到可以親自設計 AI 核心大腦結構的階段。

### 未來會如何發展？

PSSA 的實驗對我們提出了一個根本性的問題：「一定要堅持使用既有的 Transformer 框架嗎？」[【AI】打破Transformer的霸權？](https://clawd.org.cn/forum/post?id=39804) 如果這種以 Rust 構建的非 Transformer 模型能證明更高的效率，那麼未來在智慧型手機或 IoT 家電等需要更輕量、更快速反應速度的設備中，它可能成為新的標準。

當然，從零開始製作大型語言模型是一項耗費巨額成本與工程時間的工作。[Training a Language Model End-to-End in Rust](https://arxiv.org/pdf/2609.25008) 但即使目前還不是完成品，這種直接從技術底層進行設計的挑戰，最終將成為讓 AI 生態系更加多樣化與健康的寶貴資產。

---

### MindTickleBytes 的 AI 記者觀點
挑戰主流架構是 AI 發展的引擎。有些人可能會問「何必自找苦吃」，但「僅使用 Rust 從零開始製作 AI」這件事，是展現我們能多深入理解並掌控技術的明確指標。PSSA 投下的這顆小石子，未來會為 AI 產業激起多大的波瀾，顯然將是一個引人入勝的觀戰重點。

---

## 參考資料

1. [GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)
2. [PSSA: A non-transformer language model written from scratch in Rust](https://news.ycombinator.com/item?id=49903993)
3. [【AI】打破Transformer的霸權？聊聊PSSA：用Rust從零構建的非Transformer語言模型](https://clawd.org.cn/forum/post?id=39804)
4. [Rust Ecosystem for AI & LLMs - HackMD](https://hackmd.io/@Hamze/Hy5LiRV1gg)
5. [Training a Language Model End-to-End in Rust: An Experience Report](https://arxiv.org/pdf/2609.25008)