---
layout: post
title: "若數萬名 AI 同時寫程式會怎樣？OpenAI 的新挑戰：『Pando』"
description: "探討 OpenAI 為應對 AI 代理人爆發式的編碼速度，所開發的新型 Git 後端「Pando」。"
summary: "OpenAI 開發了全新的後端「Pando」，克服了既有 Git 基礎設施的限制，以支援數萬個 AI 代理人同時撰寫與修改程式碼的環境。"
tags: [OpenAI, Git, AI, Codex, Pando]
image: 2026-11-03-Scaling-Git-at-OpenAI.jpg
image_alt: "抽象的數位網路影像，顯示龐大的資料流與無數個複雜連接的 AI 代理人"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在人類開發者與 AI 代理人共存的時代，基礎設施的根本重構至關重要。Pando 不僅是單純的技術升級，更為 AI 與人類共同建構軟體的「代理人時代」樹立了標準。"
quiz:
  - question: "OpenAI 開發的新型 Git 後端名稱為何？"
    choices: ["Codex", "Pando", "GitAI"]
    answer: 1
    explanation: "OpenAI 為支援「代理人規模的開發」，開發了全新的 Git 相容後端「Pando」。"
  - question: "導入 Pando 後，預期主要的效能改善為何？"
    choices: ["資料儲存容量增加 80%", "中間推送延遲時間減少約 80%", "解除 AI 代理人數量限制"]
    answer: 1
    explanation: "相比現有的 Git 基礎設施，Pando 將中間推送延遲（Git push latency）改善了約 80%。"
  - question: "「代理人規模開發（Agent-scale development）」最大的特徵為何？"
    choices: ["僅由人類開發者撰寫程式碼", "由 AI 代理人單獨進行所有開發", "AI 與人類在同一個儲存庫中進行高速並行作業"]
    answer: 2
    explanation: "代理人規模的開發是指 AI 代理人與人類開發者在同一個儲存庫中，同時高速撰寫並提交程式碼的環境。"
lang: zh-tw
ref: 2026-11-03-Scaling-Git-at-OpenAI
---

想像一下，數萬名程式設計師正同時撰寫同一本巨著。然而，這些程式設計師並非人類，而是每秒能撰寫數百行程式碼的 AI 代理人。他們不斷地儲存（提交）修改內容，並持續交換資料以確保彼此的工作互不衝突。既有的軟體開發基礎設施，真的能承受這樣的速度嗎？

最近，OpenAI 針對這個問題給出了答案，推出了名為「Pando」的新基礎設施。[OpenAI 發布 Pando：面向 AI 規模開發的 Git 後端](https://emergent.sh/news/openai-launches-pando-git-backend-ai-scale)。如果說過去的軟體開發模式是以人類為中心，那麼現在則需要一條符合數萬名 AI 主導的「代理人時代」的全新道路。

### 為何這件事很重要？

軟體開發的核心是「協作」。我們所使用的所有應用程式與服務，都是透過無數開發者修改與合併程式碼的過程所完成。在此過程中，「Git」一直是核心工具。然而，OpenAI 所追求的「代理人規模開發（Agent-scale development）」會導致現有模式難以承受的過載。[GitHub 正為 AI 代理人規模的開發重構 Git 基礎設施](https://lumienai.com/news/github-git-infrastructure-agent-scale-development)

代理人規模的開發，是指無數 AI 代理人與人類開發者並行作業，並以高速提交程式碼的方式。[OpenAI 發布 Pando：面向 AI 規模開發的 Git 後端](https://emergent.sh/news/openai-launches-pando-git-backend-ai-scale)。若基礎設施跟不上這個速度，開發就會停滯，AI 的生產力也將付諸流水。OpenAI 的這次變革暗示著：AI 不僅僅是在寫程式，更是在親自鋪設整個軟體開發生態系的「高速公路」。

### 淺顯易懂：Pando 的作用是什麼？

Git 可以簡單地被稱為「程式碼的時光機與圖書館」。它紀錄了誰在何時修改了什麼，並將多人撰寫的程式碼匯集成一體。

為了方便理解，我們打個比方：如果現有的 Git 是兩線道公路，那麼 OpenAI 的 Pando 就像是能容納數千輛車（AI 代理人）同時行駛的 16 線道高速公路。

為了建立其編碼代理人「Codex」能夠運作的基礎，OpenAI 在僅僅 10 週的短時間內就自行開發了 Pando。[OpenAI 的 Pando Git 後端將 Monorepo 的 Git 推送延遲減少了約 80%](https://cryptobriefing.com/openai-pando-git-backend-push-latency/)。在這個過程中，Codex 代理人也直接參與了基礎設施的建構。Pando 不僅與現有的 Git 相容，還被設計為能處理每日接近 1 PB（約 100 萬 GB）的龐大程式碼資料量。[OpenAI 也打造了自己的全新 Git 後端](https://thenewstack.io/openai-pando-git-backend/)。

### 現狀：速度提升了多少？

Pando 的導入帶來了實質的開發速度提升。根據 OpenAI 的資料，與現有模式相比，Git 的中間推送延遲（push latency）減少了約 80%，也就是縮短了將近 5 倍的時間。[OpenAI 也打造了自己的全新 Git 後端](https://thenewstack.io/openai-pando-git-backend/)。

這不僅僅是稍微變快而已。過去，當無數代理人同時湧入時，基礎設施就會陷入癱瘓；而現在，這些任務皆能被舒適地處理。基於這樣的基礎設施，OpenAI 正協助其編碼代理人在無需人類介入的情況下，解決更高度、更複雜的問題。例如，OpenAI 最近為了破解數學難題「納維-斯托克斯方程式（Navier-Stokes equations）」，同時投入了約 1 萬個 AI 代理人，並在 88 小時內找到了解答。[OpenAI 聲稱已解決困擾人類數十年的數學問題](https://www.theguardian.com/science/2026/sep/08/openai-claims-to-have-solved-maths-problem-that-stumped-humans-for-decades)。

### 未來會如何？

OpenAI 的這次行動預示著軟體的開發方式將會徹底改變。過去是人類逐行敲擊鍵盤撰寫程式碼，而現在，一個 AI 代理人能在巨大的協作工具（如 Pando 這類的基礎設施）上，不眠不休地演進軟體的時代即將來臨。

未來，我們將頻繁見證 AI 製作的服務與應用程式以比以往更快的速度更新，以及複雜的技術門檻被 AI 瞬間突破的景象。當然，在此過程中，也伴隨著精密的監控系統，以確保 AI 的行為不會偏離預期方向。[OpenAI 擴大監控範圍，以檢測開拓者模型的不一致行為](https://www.unite.ai/openai-expands-monitoring-to-detect-frontier-model-misalignment/)。

Pando 為 AI 增強了能更快速、更強大地編寫程式碼的「肌肉」。下一次當您使用的應用程式變得明顯更聰明時，在那背後，說不定就有數萬個 AI 代理人正跑在名為 Pando 的高速公路上，日以繼夜地努力著。

## 參考資料

1. [OpenAI 發布 Pando：面向 AI 規模開發的 Git 後端](https://emergent.sh/news/openai-launches-pando-git-backend-ai-scale)
2. [OpenAI 也打造了自己的全新 Git 後端](https://thenewstack.io/openai-pando-git-backend/)
3. [OpenAI 的 Pando Git 後端將 Monorepo 的 Git 推送延遲減少了約 80%](https://cryptobriefing.com/openai-pando-git-backend-push-latency/)
4. [GitHub 正為 AI 代理人規模的開發重構 Git 基礎設施](https://lumienai.com/news/github-git-infrastructure-agent-scale-development)
5. [OpenAI 聲稱已解決困擾人類數十年的數學問題](https://www.theguardian.com/science/2026/sep/08/openai-claims-to-have-solved-maths-problem-that-stumped-humans-for-decades)
6. [OpenAI 擴大監控範圍，以檢測開拓者模型的不一致行為](https://www.unite.ai/openai-expands-monitoring-to-detect-frontier-model-misalignment/)