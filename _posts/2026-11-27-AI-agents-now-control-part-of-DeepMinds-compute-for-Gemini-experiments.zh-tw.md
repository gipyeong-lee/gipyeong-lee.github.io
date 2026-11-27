---
layout: post
title: "AI自主實驗時代：Google DeepMind將Gemini運算資源交給AI代理"
description: "Google DeepMind 為了開發下一代 Gemini 模型，已將部分運算資源控制權交給 AI 代理。本文將探討 AI 自主進行科學實驗的時代意義與安全機制。"
summary: "Google DeepMind 為了進行下一代 Gemini 模型實驗，已將部分自有運算資源委託給 AI 代理。不過，完全的自我改進尚有一段距離，為了人類監督，團隊也保留了不對內部思考歷程（Chain of Thought）進行獎勵的安全機制。"
tags: [AI, GoogleDeepMind, Gemini, AI代理, 技術趨勢]
image: 2026-11-27-AI-agents-now-control-part-of-DeepMinds-compute-for-Gemini-experiments.jpg
image_alt: "具象化 AI 系統在實驗室電腦螢幕前自主分析運算資料的插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 自主設計並執行實驗，是從工具轉變為同伴的巨大轉變。只要維持透明思考歷程驗證這項安全機制，科學發現的速度將快得超乎想像。"
quiz:
  - question: "Google DeepMind 交給 AI 代理的是什麼？"
    choices: ["公司人事招聘權限", "用於下一代 Gemini 實驗的部分運算資源", "Google 搜尋引擎原始碼修改權限"]
    answer: 1
    explanation: "Google DeepMind 為了開發下一代 Gemini 模型的實驗，允許 AI 代理自主控制部分自有運算資源（compute budget）。"
  - question: "DeepMind 在 AI 訓練過程中刻意不予獎勵的是什麼？"
    choices: ["程式碼編寫速度", "內部思考歷程（Chain of Thought）", "伺服器電力消耗量"]
    answer: 1
    explanation: "DeepMind 在訓練期間不對 AI 的內部思考歷程（Chain of Thought）進行獎勵，藉此確保 AI 的意圖以自然語言狀態毫無過濾地保留下來，讓人類在執行前得以審查，從而建立安全機制。"
  - question: "DeepMind 研究負責人 Koray Kavukcuoglu 強調目前的 AI 狀態是什麼？"
    choices: ["完全的遞迴自我改進（Recursive Self-Improvement）尚屬遙遠", "AI 已經完全取代了人類研究員", "完全不需要人類介入的自主研究時代已經開啟"]
    answer: 0
    explanation: "研究副總裁 Koray Kavukcuoglu 強調，儘管 AI 開始控制實驗運算，但能將自身無限升級的遞迴自我改進（RSI）階段仍是遙遠的未來。"
lang: zh-tw
ref: 2026-11-27-AI-agents-now-control-part-of-DeepMinds-compute-for-Gemini-experiments
---

想像一下，你是一間龐大研究所的總負責人，在某個深夜將實驗室超級電腦的部分使用權限交給了人工智慧助理。早晨上班時，你發現那個人工智慧竟然提出了連人類研究員都意想不到的新穎假設，並在夜裡進行了數千次虛擬實驗，甚至把有意義的結果整理得井然有序。聽起來像小說情節嗎？然而，在 Google DeepMind 的實驗室裡，類似的事情正真實上演著。

## AI 親自掌握實驗室鑰匙

最近，Google DeepMind 為了下一代 Gemini（能夠同時理解文字、圖像、音訊等多種形式資料的 Google 核心大型語言模型系列 [來源：維基百科](https://en.wikipedia.org/wiki/Gemini_(language_model))）模型的實驗，允許**AI 代理（AI Agent，能自主判斷並執行目標的自主型人工智慧程式）**自主控制實驗室的核心資源——部分運算預算（compute budget）（[AI 代理現在控制部分 DeepMind 的 Gemini 實驗運算資源](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/)）。 

這項消息是透過 Google DeepMind 研究副總裁（VP of Research）兼 Gemini 開發總負責人 Koray Kavukcuoglu 在官方 Podcast《Google DeepMind: The Podcast》第 35 集親自透露後才公諸於世（[DeepMind 代理控制部分 Gemini 訓練運算](https://explainx.ai/blog/google-deepmind-gemini-agents-training-compute-koray-kavukcuoglu-november-2026)）。從「單純回答問題」到「AI 直接晉升為規劃實驗與分配運算的主體」，這項轉變吸引了技術界的目光。

---

## 這為什麼重要？

這則新聞對我們一般人的日常生活有什麼意義？核心在於**「研究與技術發展的速度開始脫離人類的時間表」**。 

過去，在建立新的 AI 模型或發掘新材料時，人類科學家必須親自建立假設、在電腦中輸入指令並等待結果。這個過程是消耗大量時間與成本的乏味重複作業。然而，當 AI 代理直接掌控運算資源並主導實驗時，人類發現新知識與創新技術的速度可能會快到超乎想像。

事實上，Google DeepMind 透過此類自主代理系統（例如 Co-Scientist 系統）已經取得了巨大成果。從新材料合成到醫療用 AI 架構的自主開發，他們已在多個科學領域成功得出經實驗驗證的成果（[Google Deepmind 的 AI 科學共同研究員現在可以規劃實驗、執行...](https://the-decoder.com/google-deepminds-ai-co-scientist-now-plans-experiments-runs-lab-equipment-and-writes-scientific-papers/)）。甚至在人類研究員的監督下，AI 代理還發現了能以比傳統方式快上 1,600 倍的速度找出舊版 RSA 加密演算法漏洞的技術（[Google DeepMind 發現快 1,600 倍的方法來暴露加密漏洞](https://interestingengineering.com/ai-robotics/google-deepmind-agents-expose-older-encryption-flaws)）。 

也就是說，這項舉措意味著此類實驗性成功並非曇花一現，而是已經深入納入 Google 核心 AI 模型 Gemini 開發流程整體的標準營運方式中。

---

## 輕鬆理解：就像給了「超級實習生」公司信用卡

為了讓人們輕鬆理解這個複雜狀況，我們舉個日常生活的比喻。 

想像一下，你招募了一位能力非常優秀但還不是正式員工的「超級實習生」。到目前為止，這位實習生只執行前輩交辦的簡單文書處理或資料調查。但高層做出了決定，將權限交給這位實習生：**「我分給你一部分公司信用卡額度，你自己在夜裡放手去跑你認為有必要的市場調查專案吧。」**

實習生（AI 代理）在給定的預算（運算資源）範圍內自行決定要掌握的主題，熬夜運算分析資料後，在早晨提交報告。這正是 DeepMind 這次在 Gemini 實驗中嘗試的做法。

然而，這裡產生了一個重要的疑問：「當實習生開始自主行使權限時，會不會脫離控制而恣意妄為呢？」

DeepMind 研究團隊看透了這一點，並設立了一道非常獨特的防護機制。他們決定在訓練過程中，刻意不對人工智慧的內部思考過程——亦即**「思維鏈（Chain of Thought，AI 在得出答案前於腦海中進行分階段推論的內部思考歷程）」**進行獎勵（reward）（[AI 代理現在控制部分 DeepMind 的 Gemini 實驗運算資源...](https://www.topai-tools.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but)）。 

這是什麼意思？簡單來說，就是讓 AI 為什麼要進行該實驗的**內部意圖與動機以自然語言（人類看得懂的語言）毫無過濾地透明保留**，好讓人類管理者在付諸行動前進行徹底審查（[AI 代理現在控制部分 DeepMind 的 Gemini 實驗運算資源...](https://www.topai-tools.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but)）。這等於不是把腦海遮得漆黑一片，而是造了一扇能透明窺探實習生心裡在想什麼的玻璃窗。

---

## 現狀：進展到哪裡，限制又在哪裡？

媒體經常以聳動的標題報導「AI 正在自我修正，像魔鬼終結者一樣進化」。然而，現場的聲音要冷靜且現實得多。

Google DeepMind 研究副總裁 Koray Kavukcuoglu 在 Podcast 訪談中承認，此舉是實驗室內部巨大策略轉型（strategic shift）的一部分，但也劃清界線表示，科幻電影中常見的**「遞迴自我改進（Recursive Self-Improvement，AI 自行修改程式碼並無限變聰明的迴圈）」**離實現還有一段長路（[AI 代理現在控制部分 DeepMind 的 Gemini 實驗運算資源，但遞迴自我改進仍然遙遠](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/)）。

換句話說，目前的 AI 代理說到底，也只是在人類設計的框架與安全機制內，利用指定的運算預算來「代行」實驗。這並不意味著它處於自主設定目標並完全改造自身架構的階段。AI 雖然已經進化為非常強大的「實驗助手」與「協調者（Orchestrator）」，但最終的指揮棒仍然握在人類研究員手中。

---

## 未來將如何發展？

透過這次發表，我們可以一窺 AI 發展的下一個階段會是什麼模樣。 

跨越了只會寫好文章、畫出漂亮圖片的生成式 AI 時代，我們正快速進入**執行科學發現與技術開發本身的「自主代理 AI（Agentic AI）」時代**。Google DeepMind 的最終目標是建構出涵蓋整體科學的統一通用演算法（[DeepMind 的 Gemini 實驗現由 AI 代理協調](https://best-ai.org/ai-news/deepminds-gemini-experiments-now-orchestrated-by-ai-agents-5o695i)）。

我們未來需要關注的是，AI 代理在受控的運算資源中能產出多麼精密的假設，以及在此過程中與人類的協作治理（Governance，管理體系）能維持多高的安全性。隨著技術越發精進，DeepMind 試圖透明監控人工智慧「內部思考歷程」的理念，預計將成為全球 AI 產業的重要標準安全指南。

---

## 參考資料

1. The Decoder, *AI agents now control part of Deepmind's compute for Gemini experiments, but recursive self-improvement remains distant*, https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/
2. AI Weekly, *DeepMind Agents Now Run Part of Gemini Experiment Compute*, https://aiweekly.co/alerts/deepmind-agents-now-run-part-of-gemini-experiment-compute
3. TopAI Tools, *AI agents now control part of Deepmind's compute for Gemini experiments, but*, https://www.topai-tools.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but
4. ExplainX AI, *DeepMind Agents Control Part of Gemini Training Compute — Koray Kavukcuoglu*, https://explainx.ai/blog/google-deepmind-gemini-agents-training-compute-koray-kavukcuoglu-november-2026
5. Emergent SH, *DeepMind AI Agents Now Control Gemini Experiment Compute*, https://emergent.sh/news/deepmind-ai-agents-now-control-gemini
6. Best AI, *DeepMind's Gemini Experiments Now Orchestrated by AI Agents*, https://best-ai.org/ai-news/deepminds-gemini-experiments-now-orchestrated-by-ai-agents-5o695i
7. AI Future, *AI agents now control part of Deepmind's compute for Gemini experiments, but recursive self-improvement*, https://aifuture.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but-recu-21077
8. The Decoder, *Google Deepmind's AI Co-Scientist now plans experiments, runs lab equipment and writes scientific papers*, https://the-decoder.com/google-deepminds-ai-co-scientist-now-plans-experiments-runs-lab-equipment-and-writes-scientific-papers/
9. Wikipedia, *Gemini (language model)*, https://en.wikipedia.org/wiki/Gemini_(language_model)
10. Interesting Engineering, *Google DeepMind finds 1,600x faster way to expose encryption flaws*, https://interestingengineering.com/ai-robotics/google-deepmind-agents-expose-older-encryption-flaws