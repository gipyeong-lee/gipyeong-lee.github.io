---
layout: post
title: "AI竟然能自行修正自己的「智慧外殼」？自主進化 AI 代理時代來臨"
description: "AI 代理在沒有人類協助下，自行改進並進化其運作機制「Harness（束具/支架）」的最新技術研究淺顯解說。"
summary: "Google DeepMind 的最新研究顯示，AI 代理無需繁瑣的手動工程，就能自行修改並優化其運作環境（Harness），為自主軟體開發開闢了新道路。"
tags: [AI, GoogleDeepMind, 代理, AutoHarness, Evo2]
image: 2026-10-14-Google-DeepMind-paper-trains-an-agent-to-rewrite-its-own-harness.jpg
image_alt: "描繪 AI 代理自行編寫程式碼並修正其運作體系的未來感插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人類逐一制定規則的時代即將落幕。AI 具備自我認知極限並進行修復的能力，將成為邁向真正自主代理的最重要關鍵。"
quiz:
  - question: "AI 代理的「Harness（束具）」是什麼？"
    choices: ["AI 的記憶儲存裝置", "作為連接模型與作業間「黏著劑」作用的軟體架構", "AI 的學習資料集"]
    answer: 1
    explanation: "Harness 是 AI 模型與待解決任務之間的 plumbing（管路）或 glue（黏著劑），扮演協助 AI 順利運作的軟體 scaffolding（鷹架/框架）角色。"
  - question: "Google DeepMind 的 AutoHarness 研究是以何種方式運作？"
    choices: ["人類每天直接輸入新的程式碼。", "Gemini 利用從環境接收到的回饋，透過反覆精煉過程自行生成程式碼。", "維持既有的規則不變。"]
    answer: 1
    explanation: "AutoHarness 是 Gemini-2.5-Flash 根據從環境中獲得的回饋，透過反覆改進過程，自行建構出最佳程式碼 Harness 的方式。"
  - question: "Evo2 框架的核心目標為何？"
    choices: ["極大化人類的干預。", "完全更換 AI 的基礎語言模型。", "在不更動任務執行者（task executor）的情況下，改善代理的工作流程與策略。"]
    answer: 2
    explanation: "Evo2 是一個在不更動任務執行者本身的情況下，將代理的 Harness 修改紀錄與評估資料作為學習資料，進而改善工作流程與策略的框架。"
lang: zh-tw
ref: 2026-10-14-Google-DeepMind-paper-trains-an-agent-to-rewrite-its-own-harness
---

想像一下，您聘請了一位新助理。但這位助理在每次執行任務時都會說：「我覺得用這種方式工作效率更高」，並不時自行升級工作方式（手冊）。甚至在您沒有指示的情況下，主動重整自己專屬的工具與記憶體系。這並非科幻電影情節，而是 Google DeepMind 最新研究所展現的「自主進化 AI 代理」樣貌。

### 為何這項技術如此重要？

過去，建構 AI 代理的過程是充滿痛苦且高成本的「手工勞動」。因為為了讓代理執行特定任務，人類工程師必須逐一定義該任務的具體規則與限制條件。在業界，這種建立連接的過程被稱為「Harness（束具/框架）」，而這其實正是引進 AI 代理時最大的阻礙。[來源: This AutoHarness paper(from Google DeepMind) is the most...](https://www.linkedin.com/posts/omarsar_this-autoharness-paper-from-google-deepmind-activity-7437877601853153280-uWyl)

但現在情況不同了。當 AI 能夠自行修改並優化其運作體系時，即便沒有人類介入，AI 代理也能自主執行各種複雜任務的世界將會快速來臨。這將成為 AI 技術從實驗室層級跨越到實務現場進行「規模化（scalable）」部署的重要分水嶺。

### 淺顯易懂：AI 的「黏著劑」，Harness

讓我們將技術內容稍微簡化。AI 代理通常由擔任「大腦」角色的大型語言模型（LLM），以及協助該大腦與外部世界溝通的「Harness」框架所組成。[來源: AutoHarness: improving LLM agents by automatically ...](https://arxiv.org/pdf/2603.03329)

若將 AI 代理比喻為「天才畫家」就很好理解了。畫家要作畫，必須要有畫筆（工具）、準備好畫布（環境），還必須有明確的繪畫指示（提示詞）。在這裡，畫家的工具箱與協助繪畫過程的整體工作台，就可以視為「Harness」。過去是由人類逐一準備畫筆並調整工作台高度，現在則是畫家（AI）自己說：「這次畫作需要這樣的畫筆」，並自行改變工具箱的結構。

Google DeepMind 的 **AutoHarness** 協助 Gemini-2.5-Flash 模型利用從環境中獲得的回饋，自行設計出更優秀的「工作台」。[來源: AutoHarness: improving LLM agents by automatically ...](https://arxiv.org/pdf/2603.03329), [來源: AutoHarness | DAIR.AI Academy](https://academy.dair.ai/papers/autoharness)

此外，名為 **Evo2** 的框架會將代理在修正 Harness 時獲得的資料，回收作為學習資料。換句話說，它將修改與實驗的經驗累積為資料，進而自主強化自身的工作流程（Workflow）。[來源: Google DeepMind paper trains an agent to rewrite its own harness](https://runtimewire.com/article/google-deepmind-evo2-agent-harness-co-evolution)

### 進展到什麼程度了？

目前 AI 研究領域正熱烈討論多種透過改善結構來自我提升的有趣方式。

首先，**AutoHarness** 讓代理親自編寫程式碼，自行創造 Harness。相較於人類手動編寫複雜規則，經過少量反覆精煉過程的自動化 Harness 有時能表現出更高效的性能。[來源: [2603.03329] AutoHarness](https://arxiv.org/abs/2603.03329)

其次，**Self-Harness** 是一種新典範，代理在沒有外部強大支援或人類幫助的情況下，獨立改進其運作環境。[來源: [2606.09498] Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498)

第三，由 Google Cloud AI 研究團隊等人發表的 **RRSI（遞迴自我改善）** 技術，讓 AI 親自重寫提示詞、工具、記憶體系、控制流程，甚至是子代理（sub-agents）。[來源: Paper AutoHarness from DeepMind Changes AI Agents 1](https://www.youtube.com/watch?v=4Xczb2z3N_w)

現場專家們一致認為：「比起模型本身的性能差異，根據使用何種 Harness 而產生的性能差距更大。」因為無論模型多聰明，若使用工具的方式不佳，就無法發揮應有的能力。[來源: Auto-Harness Synthesis - Just Understanding Data](https://understandingdata.com/posts/auto-harness-synthesis/)

### 未來的展望

未來的 AI 代理將不再是靜態的存在。今天遇見的 AI 與 1,000 天後的 AI，其結構、記憶與工具可能完全不同。[來源: The Harness That Learns You | XO Docs](https://docs.xo.builders/research/perspectives/the-harness-that-learns-you)

我們現在正超越思考「該給 AI 什麼指示」的階段，邁向觀察「AI 會自行選擇何種工具與方式來解決問題」的階段。讓我們一同見證，人類干預減至最低、真正意義上的自主代理將如何改變我們的日常生活。

## 參考資料

1. [Google DeepMind - Wikipedia](https://en.wikipedia.org/wiki/Google_DeepMind)
2. [This AutoHarness paper(from Google DeepMind) is the most...](https://www.linkedin.com/posts/omarsar_this-autoharness-paper-from-google-deepmind-activity-7437877601853153280-uWyl)
3. [Google DeepMind](https://deepmind.google/)
4. [AI has grown beyond human knowledge, says Google's DeepMind unit](https://www.zdnet.com/article/ai-has-grown-beyond-human-knowledge-says-googles-deepmind-unit/)
5. [The Harness That Learns You | XO Docs](https://docs.xo.builders/research/perspectives/the-harness-that-learns-you)
6. [Google DeepMind paper trains an agent to rewrite its own harness](https://runtimewire.com/article/google-deepmind-evo2-agent-harness-co-evolution)
7. [AutoHarness: improving LLM agents by automatically ...](https://arxiv.org/pdf/2603.03329)
8. [[2603.03329] AutoHarness: improving LLM agents by ...](https://arxiv.org/abs/2603.03329)
9. [AutoHarness: LLM Agents That Build Own Scaffolding | aiHola](https://aihola.com/article/autoharness-llm-agent-code-harness)
10. [Auto-Harness Synthesis - Just Understanding Data](https://understandingdata.com/posts/auto-harness-synthesis/)
11. [AutoHarness | DAIR.AI Academy](https://academy.dair.ai/papers/autoharness)
12. [[2606.09498] Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498)
13. [Paper AutoHarness from DeepMind Changes AI Agents 1](https://www.youtube.com/watch?v=4Xczb2z3N_w)