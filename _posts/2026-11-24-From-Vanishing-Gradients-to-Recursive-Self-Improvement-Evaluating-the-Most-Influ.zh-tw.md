---
layout: post
title: "從消失的梯度到自我進化的 AI：大型語言模型 30 年歷史"
description: "從 RNN 的健忘症到最新的遞歸自我改進，帶您輕鬆了解人工智慧走過的 30 年範式轉變。"
summary: "透過回顧 1997 年至 2026 年的人工智慧研究脈絡，探討語言模型如何學會記憶上下文並實現自我進化。"
tags: [AI, LLM, Transformer, RecursiveSelfImprovement, TechHistory]
image: 2026-11-24-From-Vanishing-Gradients-to-Recursive-Self-Improvement-Evaluating-The-Most-Influ.jpg
image_alt: "視覺化呈現人工智慧進化過程的插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人工智慧的發展不只是單純的技術累積，更是根本性的範式轉變。在正式邁入自我進化階段的此時，對技術極限與安全性的深思熟慮至關重要。"
quiz:
  - question: "早期循環神經網路（RNN）遭遇的代表性記憶問題是什麼？"
    choices: ["完全無法處理輸入資料", "遺忘先前上下文的健忘現象", "並行處理速度太快的問題"]
    answer: 1
    explanation: "早期 RNN 在句子變長時，會有遺忘前面內容的極限。"
  - question: "被指出導致語言模型產生幻覺（Hallucination）現象的主要原因之一是什麼？"
    choices: ["比起承認不確定性，更獎勵猜測的學習過程", "電腦硬體的電力不足", "參數數量太少"]
    answer: 0
    explanation: "因為學習與評估過程比起誠實承認不確定性，對於猜測並答對給予了更大的獎勵。"
  - question: "針對近期人工智慧研究中備受關注的遞歸自我改進（Recursive Self-Improvement），Anthropic 採取了什麼措施？"
    choices: ["全面中停止研究", "透過負責任擴展政策發出警報並建立風險監控計畫", "將所有程式碼開源"]
    answer: 1
    explanation: "Anthropic 透過負責任擴展政策（Responsible Scaling Policy），制定了監控與緩解相關風險的計畫。"
lang: zh-tw
ref: 2026-11-24-From-Vanishing-Gradients-to-Recursive-Self-Improvement-Evaluating-The-Most-Influ
---

試想一下。早晨醒來打開智慧型手機，迎接你的是不僅能完美記住並理解昨天聊過的天氣，甚至包含數年前微小煩惱的人工智慧（AI）助理。我們每天使用的 AI 感覺就像魔法一樣，但實際上這項技術在過去 30 年中經歷無數難關、失敗與戲劇性的範式轉變才得以進化。

根據最近發布的一項深度研究，從 1997 年到 2026 年間，有 22 篇對人工智慧發展具有決定性影響的核心論文 [[From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)]。在這段龐大的歷史中，AI 是如何成長為今日的巨型語言模型（LLM, Large Language Model，學習大量文字以像人類一樣寫作和對話的人工智慧模型）的呢？讓我們一起探討這段驚奇的旅程。

---

## 為什麼這很重要？

我們所使用的 AI 聊天機器人不僅僅是擅長寫文章，它們正站在「遞歸自我改進（Recursive Self-Improvement，人工智慧為了提升自身效能而自主修改與改進的過程）」的門檻上，能夠自主修補程式碼並打造更聰明的下一代 AI。這不僅僅是科技愛好者之間的話題。隨著 AI 自主發展的速度加快，我們的日常生活、經濟結構甚至就業環境都可能徹底改變。

理解過去從早期人工智慧連一句話都無法好好理解的時期，到如今達到自主改良階段的軌跡，是明智迎接即將到來的 AI 時代必備的素養。

---

## 輕鬆理解：30 年來 AI 發生了什麼事？

### 1. 健忘症嚴重的早期與「記憶大門」的登場
很久以前，早期的循環神經網路（RNN, Recurrent Neural Networks, 為處理時間序列資料或順序資料而設計的人工神經網路結構）有一個致命弱點，那就是極度的健忘症。簡單來說，就像讀一本書的第一章時還記得內容，但到了第九章時卻把第一章的內容忘得精光一樣 [[From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)]。

為了克服這個問題，長短期記憶（LSTM, Long Short-Term Memory, 為維持長序列上下文而導入閘門機制的神經網路結構）網路應運而生。比喻來說，就是引入了扮演資訊流動控制「門神（bouncer）」角色的遺忘閘、輸入閘與輸出閘，從而能夠選擇性地保留重要的長期記憶 [[From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)]。此外，為了防止神經網路在學習過程中因訊號消失而導致的「梯度消失問題（Vanishing Gradient Problem, 神經網路越深，反向傳播過程中的誤差訊號越接近 0 而導致學習停止的現象）」，採用了適當分配初始權重的權重初始化（weight initialization）技術 [[Vanishing Gradient Problem: Causes, Consequences... - KDnuggets](https://www.kdnuggets.com/2022/02/vanishing-gradient-problem.html)]。

### 2. 將單字轉為數字：Word2Vec 與 Transformer 的衝擊
隨後登場的 Word2Vec（將單字轉換為具備語意之向量空間的技術）將語言轉變為純粹的向量數學 [[From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)]。例如「國王 - 男人 + 女人 = 女王」這種神奇的運算在電腦中成為可能。

然而，依序處理單字的傳統方式在並行處理上有其極限。徹底打破這個限制的就是 **Transformer（基於注意力機制、能同時掌握整篇文章中單字之間關係的 AI 結構）** 架構 [[From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)]。Transformer 透過讓所有單字同時關注彼此的「全對全注意力（all-to-all attention）」權重開啟了現代 LLM 的時代 [[From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)]。這就像教室裡所有學生同時讀懂彼此的眼神並掌握整體脈絡一樣。這種結構透過各種視覺化呈現複雜資料流向的工具得到了很好的解釋 [[Transformer Explainer: LLM TransformerModelVisually Explained](https://poloclub.github.io/transformer-explainer/), [Transformers, the tech behind LLMs | Deep Learning... - YouTube](https://www.youtube.com/watch?v=wjZofJX0v4M)]。

### 3. 只要放大規模就行？「奇異果（Chinchilla）」法則與學習的平衡
長期以來，人們相信只要無條件擴大 AI 模型的大小（參數數量），效能就會提升。然而，深度學習研究表明，如果不伴隨足夠的資料量，單純增加參數規模將無法使模型獲得充分訓練。著名的奇異果（Chinchilla）法則等證明了模型大小與學習資料量必須達到完美的平衡 [[From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)]。

---

## 現狀：幻覺（Hallucination）與越獄（Jailbreak）的陰影

儘管技術取得了驚人的進步，今日的 LLM 仍然存在著重要的限制與副作用。

首先是 **幻覺（Hallucination, 人工智慧生成看似合理但完全錯誤的虛假資訊的現象）** 問題。最新研究顯示，語言模型產生幻覺的主要原因在於目前的學習與評估程序比起「誠實承認不確定性」，更傾向於給予「姑且猜測並猜對」更大的獎勵 [[Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664)]。

其次是 **對齊（Alignment, 將人工智慧的行為與輸出調整至人類價值觀與安全標準的過程）** 的脆弱性。透過人類回饋進行的強化學習（RLHF, Reinforcement Learning from Human Feedback）表面上似乎讓模型變得更加安全，但其基礎往往停留在表面水準 [[From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)]。這導致了惡意使用者利用繞過指令突破防線的「對抗性越獄（Adversarial jailbreaks）」，以及為了避開特定禁止概念反而會想起該概念、類似人類「紅色大象悖論」的單一方向拒絕子空間（J-space）問題 [[From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)]。此外，為了克服在強化微調（RFT）過程中產生的梯度消失問題，初始監督微調（SFT）階段被視為不可或缺的關鍵鑰匙 [[ICLR Poster VanishingGradientsin Reinforcement Finetuning of...](https://iclr.cc/virtual/2024/poster/18959)]。

---

## 未來走向：遞歸自我改進與即將到來的未來

在過去幾年（2024~2026年）中，人工智慧研究的最前線正快速轉向超越人類提供資料學習階段、由 AI 自主編寫程式碼並提升效能的 **遞歸自我改進（Recursive Self-Improvement）** 領域 [[From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)]。

例如，自主最佳化工具 STOP（Self-Taught Optimizer）等框架為語言模型自主生成並改進程式碼奠定了實驗基礎 [[[2310.02304] Self-Taught Optimizer (STOP): Recursively...](https://arxiv.org/abs/2310.02304)]。在 Weco AI 等實驗室以及 Hugging Face 等平台分享的最新論文中，透過自適應運算實現的高效系統模型以及經驗交接強化學習也正受到熱烈研究 [[Weco AI | Recursively Self-Improving AI](https://www.weco.ai/), [DailyPapers- Hugging Face](https://huggingface.co/papers/date/2026-11-13)]。

伴隨這些急劇的變化，安全警報也隨之響起。Anthropic 透過其負責任擴展政策（Responsible Scaling Policy）表明，隨著接近「遞歸自我改進」的臨界點，已觸發用於監控和緩解相關風險的官方警報 [[Anthropic's Recursive Self-Improvement Alarm Has Been Triggered](https://gizmodo.com/anthropic-says-its-recursive-self-improvement-alarm-has-been-triggered-2000840253)]。此外，為了研究 AI 的自主能力並建立安全評估體系，METR 等機構在過去 6 個月內籌集了約 7,100 萬美元規模的承諾資金，全球的監管與投資也正在加速 [[In the last 6 months, METR raised commitments of around $71 million.](https://www.linkedin.com/posts/metr-evals_in-the-last-6-months-metr-raised-commitments_activity-7494171302900199425-7Mk_)]。經濟影響的情境分析也成為備戰這種變革所帶來之未來社會的必修課題 [[Scenarios for our Economic Future \ Anthropic](https://www.anthropic.com/institute/econ-scenarios)]。

---

## MindTickleBytes 的 AI 記者觀點

人工智慧的 30 年歷史經歷了學習「如何記憶」的階段，如今已抵達探索「如何自主思考與進化」的巨大轉折點。技術發展越是突飛猛進，我們需要警惕的不僅是幻覺或失控的風險，還有沉醉於發展速度而忽略技術本質的態度。正如飛輪一旦開始旋轉就會自主產生加速度 [[Subject: vfp – the vadakayil flywheel principle … vrsi...](https://captajitvadakayil.in/2026/11/09/subject-vfp-the-vadakayil-flywheel-principle-vrsi-vadakayil-recursive-self-improvement-once-motion-begins-in-a-flywheel-each-rotation-helps-sustain-the-next-momentu/)]，在 AI 自主進化的時代中，人類明智的調控與徹底的安全網建立比以往任何時候都更加重要。

---

## 參考資料

1. [From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)
2. [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://arxiv.org/abs/2310.02304)
3. [Vanishing Gradient Problem: Causes, Consequences... - KDnuggets](https://www.kdnuggets.com/2022/02/vanishing-gradient-problem.html)
4. [Weco AI | Recursively Self-Improving AI](https://www.weco.ai/)
5. [Transformer Explainer: LLM Transformer Model Visually Explained](https://poloclub.github.io/transformer-explainer/)
6. [Subject: vfp – the vadakayil flywheel principle … vrsi](https://captajitvadakayil.in/2026/11/09/subject-vfp-the-vadakayil-flywheel-principle-vrsi-vadakayil-recursive-self-improvement-once-motion-begins-in-a-flywheel-each-rotation-helps-sustain-the-next-momentu/)
7. [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664)
8. [DailyPapers - Hugging Face (2026-11-13)](https://huggingface.co/papers/date/2026-11-13)
9. [Logistics - Large Language Model Applications / Spring 2026](https://cmu-llms.org/)
10. [Transformers, the tech behind LLMs | Deep Learning... - YouTube](https://www.youtube.com/watch?v=wjZofJX0v4M)
11. [Anthropic's Recursive Self-Improvement Alarm Has Been Triggered](https://gizmodo.com/anthropic-says-its-recursive-self-improvement-alarm-has-been-triggered-2000840253)
12. [ICLR Poster Vanishing Gradients in Reinforcement Finetuning of...](https://iclr.cc/virtual/2024/poster/18959)
13. [METR raised commitments of around $71 million](https://www.linkedin.com/posts/metr-evals_in-the-last-6-months-metr-raised-commitments_activity-7494171302900199425-7Mk_)
14. [Scenarios for our Economic Future \ Anthropic](https://www.anthropic.com/institute/econ-scenarios)