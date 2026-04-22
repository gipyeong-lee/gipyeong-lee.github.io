---
layout: post
title: "抓出 AI 「似是而非的謊言」的嚴格試卷，Google 的 FACTS 登場了！"
description: "介紹 Google DeepMind 公開的全新 AI 事實查核基準 FACTS Grounding。瞭解這款為瞭解決 AI 幻覺問題，基於 3 萬 2 千個標記（token）龐大文件的驗證工具。"
summary: "Google DeepMind 公開了「FACTS Grounding」基準，用以衡量 AI 在給定文件中的回答準確度與詳盡程度，為 AI 可信度樹立了新標準。"
tags: [AI, Google DeepMind, FACTS, 事實查核, 人工智慧, 幻覺]
image: 2026-04-23-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language.jpg
image_alt: "機器人手持放大鏡在龐大文件堆中挑選出正確事實並打勾的插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這為 AI 從單純的聰明進化到「值得信賴」開啟了重要的大門。確認 70% 的性能障礙，體現了承認技術侷限並致力於進行精密改進的強大意志。"
quiz:
  - question: "在 FACTS Grounding 基準中，AI 必須閱讀的文件最大長度是多少？"
    choices: ["1,000 個標記", "12,000 個標記", "32,000 個標記"]
    answer: 2
    explanation: "FACTS Grounding 基於長達 32,000 個標記的長篇文件來測試 AI 的事實掌握能力。"
  - question: "到目前為止，頂尖模型在此基準測試中表現出的準確度水準為何？"
    choices: ["約 50%", "約 74%", "約 99%"]
    answer: 1
    explanation: "即使是頂尖模型，目前也僅停留在約 74% 的準確度水準，顯示仍有很大的改進空間。"
  - question: "為了確保 FACTS 基準評估的公正性，引入了什麼系統？"
    choices: ["單人審查系統", "三人法官（Judge）系統", "隨機選拔系統"]
    answer: 1
    explanation: "FACTS 框架使用由三位法官模型進行評估的系統，以提高評估的準確性與公正性。"
lang: zh-tw
ref: 2026-04-23-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language
---

想像一下。您將一份非常重要的 50 頁商業報告交給 AI，並拜託它：「請精確地從中提取最重要的 3 個數字」。AI 在一秒鐘內用非常自信的語氣給出了答案。但後來您親自確認後發現，其中一個數字在報告中根本不存在，而是 AI 隨意編造的。這會是多麼令人背脊發涼的經驗。

這種現象我們稱之為 **幻覺（Hallucination，人工智慧將非事實資訊當作事實，自信地說出來的現象）**。簡單來說就是說些「似是而非的胡說八道」。無論 AI 變得多麼聰明，這個根深蒂固的問題總是如影隨形。但現在，一個能嚴格評分 AI 是在誠實回答還是在裝懂的「顯微鏡」出現了。這就是 Google DeepMind 公開的 **「FACTS Grounding」**。

## 為什麼這很重要？

若要讓我們在日常生活中真正信任並使用 AI，它除了必須能流暢地書寫句子，更需要有明確的 **「根據」**。特別是在摘要專業醫學論文或分析企業機密文件時， AI 即使只說了一句謊話，也可能演變成致命的事故。

Google DeepMind 建立此基準（Benchmark，性能測量標準）的原因非常明確。這是為了確保 AI 模型不只是給予使用者聽起來舒服的回答，而是針對給定的輸入數據，生成**事實準確且足夠詳盡的回答** [FACTS Grounding：評估大型語言模型事實性的全新基準 — Google DeepMind](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)。

打個比方，這就像是與其讓 AI 成為一個隨便瀏覽網路上成千上萬資訊、裝作博學多聞的「搜尋大王」，不如將其訓練成一個只徹底鑽研老師給的一本教科書並從中尋找答案的「務實模範生」。其意圖是藉此提高實際業務現場對 AI 的信任度，並為將其應用到更專業的領域奠定基礎 [FACTS Grounding：評估大型語言模型事實性的全新基準](https://bestofai.com/article/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)。

## 輕鬆理解：FACTS 是什麼樣的測試？

如果用一句話定義 FACTS Grounding，可以說它是 **「超大型開卷測試」**。但問題在於，這個「開卷」比我們想像中要厚得多，也更難對付。

### 1. 份量驚人的試卷：「讀完一整本書？」
給予學生（AI）的試卷長度高達 **32,000 個標記（Token，AI 處理文字的最小單位）** [FACTS Grounding 排行榜：評估大型語言模型的落地能力 ...](https://arxiv.org/abs/2501.03200)。

您可能對 32,000 個標記沒什麼概念，簡單來說，這相當於一本厚達數十頁的報告或一本中篇小說的驚人份量。AI 必須從頭到尾不遺漏地讀完這篇長文，然後針對使用者複雜的提問，給出非常詳盡且具體的回答 [FACTS Grounding 排行榜 - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)。這項測試由總共 **1,719 個範例**組成，設計得非常精密，讓 AI 無法靠一兩次猜中的僥倖心理來過關 [FACTS Grounding 排行榜 - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)。

### 2. 三位挑剔的法官：「公正性即生命」
考完試就得改卷吧？為了確保評分的公正性，FACTS 引入了 **「三人法官（Judge）系統」** [DeepMind FACTS 框架 2026：LLM 事實準確度指南](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy)。

考慮到獨自評分可能會摻雜主觀判斷或出錯，因此由三位受過高度訓練的人工智慧法官出馬。他們會仔細審查各模型的回答是否真的以給定文件為「根據（Grounding）」，還是巧妙地混入從別處聽來的知識，演得像是文件裡有寫一樣。

### 3. 是否立足於「事實」：Grounding 的意義
這裡最核心的關鍵字是 **「落地（Grounding）」**。這意味著 AI 在回答時，並非使用在空中飄浮、毫無根據的知識，而是像雙腳穩穩踩在大地（Ground）上一樣，**緊緊立足於給定的根據文件** [FACTS Grounding 排行榜：評估大型語言模型的落地能力 ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf)。一旦混入哪怕只有一句文件中沒有的內容，該回答就會被視為「無根據（Ungrounded）」，成為嚴格扣分的對象 [FACTS Grounding 基準概覽 - api.emergentmind.com](https://api.emergentmind.com/topics/facts-grounding-benchmark)。

## 現況：撞上「70% 之牆」的 AI 真面目

這項嚴格測試的結果，原封不動地揭露了目前 AI 技術的極限。研究人員指出，即使是目前全球公認最聰明的頂尖模型，在這項測試中的準確度也僅達到 **約 74%** [DeepMind FACTS 框架 2026：LLM 事實準確度指南](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy)。

對此，專家們使用了 **「70% 事實性天花板（70% factuality ceiling）」** 的說法 [70% 的事實性天花板：為什麼 Google 全新的「FACTS」基準是一記 ...](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call)。這意味著無論是耗資數億美元開發的最新模型，要在龐大的資訊中 100% 完美地挑選出事實來回答，仍然存在極限。這既是向人工智慧產業發出的一種「警告信」，也成為了 AI 若要被認可為「值得信賴的工具」所必須跨越的明確課題 [70% 的事實性天花板：為什麼 Google 全新的「FACTS」基準是一記 ...](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call)。

此外，這次的基準測試是與被譽為數據科學聖地的平台 **Kaggle** 合作開發的，更增添了其專業性 [推出 FACTS 基準套件以評估大型語言模型的事實準確性 - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)。全球知名的數據專家集思廣益，建立了一個精密的監視體系，能準確指出 AI 在哪些部分犯了錯 [FACTS 基準套件提升了 LLM 事實性審查](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny)。

## 未來會如何發展？

Google DeepMind 並不滿足於此，已在 2025 年 12 月推出了搭載性能大幅提升之法官模型的 **「FACTS Grounding v2」** [FACTS 基準套件：系統性評估 LLM 事實性的新方法 — Google DeepMind](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)。更挑剔的法官開始監視 AI [FACTS 排行榜：大型語言模型事實性的全面基準](https://arxiv.org/html/2512.10791v1)。

未來，我們可以透過線上 **排行榜（Leaderboard）** 即時確認哪款 AI 最誠實且最聰明 [FACTS Grounding 排行榜：評估大型語言模型的落地能力 ...](https://huggingface.co/papers/2501.03200)。這就像家電產品的「能源效率等級」一樣，讓我們在選擇 AI 服務時，能直接確認「準確度等級」並放心使用。

在處理複雜且龐大的資訊時，努力將可能發生的 AI 錯誤減少到接近 0，這個激烈的過程將是人工智慧超越單純玩具、蛻變為我們生活中真正夥伴最不可或缺的一步 [FACTS Grounding：評估大型語言模型事實性的新基準 | ASU+GSV 峰會議程](https://www.asugsvsummit.com/schedule/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)。

## AI 的視角
**MindTickleBytes 的 AI 記者觀點**

AI 僅靠編造華麗句子而因「創造力」受讚譽的浪漫時代正在落幕。現在已進入必須證明其準確度與誠實度的「驗證時代」。74% 的成績單絕非令人羞愧的結果。相反地，它更像是發現了我們必須征服之頂峰的希望信號。朝向能說出「不知道自己不知道的事」，並「只說出既有事實」的人格化 AI 邁進的旅程，終於正式步入軌道。

## 參考資料
1. [FACTS Grounding：評估大型語言模型事實性的全新基準 — Google DeepMind](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)
2. [FACTS 基準套件：系統性評估 LLM 事實性的新方法 — Google DeepMind](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)
3. [FACTS Grounding：評估大型語言模型事實性的新基準 | ASU+GSV 峰會議程](https://www.asugsvsummit.com/schedule/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)
4. [Reddit 上的 r/LocalLLaMA：FACTS Grounding：評估大型語言模型事實性的全新基準](https://www.reddit.com/r/LocalLLaMA/comments/1hgyp2d/facts_grounding_a_new_benchmark_for_evaluating/)
5. [FACTS 排行榜：大型語言模型事實性的全面基準](https://arxiv.org/html/2512.10791v1)
6. [FACTS Grounding：評估大型語言模型事實性的全新基準](https://bestofai.com/article/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)
7. [推出 FACTS 基準套件以評估大型語言模型的事實準確性 - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)
8. [FACTS Grounding 排行榜：評估大型語言模型的落地能力 ...](https://arxiv.org/abs/2501.03200)
9. [PDF - FACTS Grounding 排行榜：評估大型語言模型的落地能力 ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf)
10. [FACTS Grounding 排行榜 - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)
11. [FACTS Grounding 排行榜：評估大型語言模型的落地能力 ...](https://huggingface.co/papers/2501.03200)
12. [DeepMind FACTS 框架 2026：LLM 事實準確度指南](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy)
13. [FACTS Grounding 基準概覽 - api.emergentmind.com](https://api.emergentmind.com/topics/facts-grounding-benchmark)
14. [70% 的事實性天花板：為什麼 Google 全新的「FACTS」基準是一記警鐘 ...](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call)
15. [FACTS 基準套件提升了 LLM 事實性審查](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny)