---
layout: post
title: "Claude 突然變笨了？從 83% 跌至 68% 的成績單真相"
description: "本文將深入淺出地解析頂尖 AI 模型之一 Claude 4.6 的性能下降爭議，以及 BridgeBench 幻覺測試的結果。"
summary: "最近有報告指出 Claude 4.6 的程式碼分析準確度從 83% 驟降至 68%，引發了「AI 性能退化」的爭議。然而，專家們也對測試方法提出了質疑。"
tags: [Claude, 克勞德, 人工智慧, 幻覺現象, AI 新聞, BridgeBench]
image: 2026-05-05-Claude-Opus-46-accuracy-on-BridgeBench-hallucination-test-drops-from-83-to-68.jpg
image_alt: "在趨勢下滑的圖表前陷入沉思的機器人"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的性能並非固定不變，而是會根據環境與提問方式而波動。這次爭議充分展現了數字背後隱藏的「測量難度」。"
quiz:
  - question: "最近引發爭議的 Claude 4.6 準確度下降幅度是多少？"
    choices: ["從 90% 降至 70%", "從 83.3% 降至 68.3%", "從 50% 降至 30%"]
    answer: 1
    explanation: "根據 BridgeBench 報告，Claude 4.6 的準確度從 83.3% 下降到 68.3%。"
  - question: "AI 將虛假資訊說得煞有其事的現象稱為什麼？"
    choices: ["深偽技術 (Deepfake)", "幻覺現象 (Hallucination)", "資料探勘 (Data Mining)"]
    answer: 1
    explanation: "AI 編造不存在的事實進行回答的現象被稱為幻覺現象。"
  - question: "部分專家反對性能下降主張的根據為何？"
    choices: ["AI 肚子餓了", "測試題目改變或 AI 的隨機性所致", "Claude 原本就不擅長寫程式"]
    answer: 1
    explanation: "批評者認為原因在於重新測試時題目集有所不同，或者是 AI 每次執行結果都可能不同的非決定性（Nondeterminism）。"
lang: zh-tw
ref: 2026-05-05-Claude-Opus-46-accuracy-on-BridgeBench-hallucination-test-drops-from-83-to-68
---

想像一下，如果你信任的好朋友突然開始胡言亂語會是什麼感覺？昨天還能輕鬆解開複雜數學題的朋友，今天連簡單的九九乘法表都算錯，甚至一本正經地編造根本不存在的事實。最近，在全世界人工智慧 (AI) 使用者中因其卓越智慧而大受歡迎的 Anthropic AI 模型——「Claude Opus 4.6」，正陷入這樣的激烈爭議中。

「Claude 似乎變得比以前笨了」這種使用者模糊的直覺，隨著一份用實際數據證明的報告出爐，情況變得更加複雜。[Source 2] [Viral BridgeBench Post Claims Claude Opus 4.6 Was ‘Nerfed,’ Critics Call It Bad Science](https://tech.yahoo.com/ai/claude/articles/viral-bridgebench-post-claims-claude-131318087.html) 究竟 Claude 4.6 的成績單為何突然下滑？這到底是 AI 真的退步了，還是單純的誤解？MindTickleBytes 將為您深入淺出地詳細解析。

## 為什麼這很重要？

想像一下，如果我們蓋房子時有一位負責審核設計圖的專家。原本能完美找出缺陷的專家，突然給出「這根柱子拿掉也安全」的錯誤建議，會發生什麼事？

我們現在開始將 AI 視為共同執行任務的「夥伴」，而不僅僅是消遣用的玩具。特別是對於開發者來說，Claude 曾是審核複雜程式碼、尋找錯誤的可靠助手。但如果這位助手開始「撒謊」，那問題就大了。

這次爭議的核心在於**幻覺現象 (Hallucination)**。簡單來說，是指 AI 在不了解事實的情況下，卻表現得好像很了解一樣，煞有其事地編造虛假內容。如果 AI 撰寫的程式碼存在致命的安全漏洞，AI 卻出現幻覺說「這段程式碼很完美，請立即部署」，這可能會導致整個服務癱瘓的重大事故。[Source 12] [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236) 因此，Claude 的準確度從 80% 區間驟降至 60% 區間的消息，對所有將 AI 作為工具的人來說，無異於一場「信任危機」般的緊急事態。[Source 8] [Claude Opus 4.6 Accuracy Slips in Hallucination Benchmark](https://www.knowai.space/en/news/claude-opus-hallucination-benchmark-analysis)

## 輕鬆理解：AI 的「考試成績單」事件

要理解這次爭議，首先需要了解 **BridgeBench** 測試。BridgeBench 是一種測量 AI 在分析複雜程式碼時，多大程度上能不撒謊（幻覺）並誠實回答的「AI 道德與實力考試」。它由 30 個複雜任務和 175 個精細問題組成，嚴格驗證 AI 回答的內容是否與在實際電腦中執行程式碼的結果完全一致。[Source 12] [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236)

把這種情況比喻成學校生活如何？一位在上個月期末考中獲得全校第二名（83.3 分）而備受期待的優等生，在後來的考試中成績突然跌至全校第十名（68.3 分）。[Source 11] [BridgeBench Claim Claude Opus 4.6 'Nerfed' Criticized](https://blockport.io/latest-news/bridgebench-claim-claude-opus-4-6-nerfed-criticized/) 根據 BridgeBench 營運團隊 BridgeMind 發布的結果，Claude 4.6 的成績單下滑程度令人驚訝：

*   **準確度 (Accuracy)**：83.3% → 68.3%（下降約 15%）[Source 2, Source 12]
*   **排名 (Ranking)**：全體第 2 名 → 第 10 名（從領先群跌至中段班）[Source 4, Source 11]
*   **編造率 (Fabrication Rate)**：約 17% → 33%（幾乎增加一倍）[Source 12]

特別是「編造率」達到 33% 這一點令人震驚。簡單來說，這意味著向 AI 提出三個問題，其中一個它會非常有自信地給出錯誤答案。[Source 12] [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236) 網路上甚至流傳著陰謀論，認為「Anthropic 為了節省營運成本，偷偷削弱 (Nerf) 了 Claude 的性能」。[Source 9] [Did Anthropic Nerf Claude Opus 4.6? The BridgeBench Debate](https://www.krasa.ai/news/claude-opus-4-6-bridgebench-nerfing-controversy)

## 現況：「真的變笨了嗎？」vs「考試有問題！」

然而，並非所有看到這個結果的專家都在指責 Claude。有些人強烈批評這次測試結果本身是「偽科學 (Bad Science)」，即不可靠的調查。[Source 2] [Viral BridgeBench Post Claims Claude Opus 4.6 Was ‘Nerfed,’ Critics Call It Bad Science](https://tech.yahoo.com/ai/claude/articles/viral-bridgebench-post-claims-claude-131318087.html) 著名的電腦科學家 Paul Calcraft 等人駁斥了性能下降的主張，稱其為「有缺陷 (Flawed)」的分析。[Source 3] [BridgeMind AI's Claude Opus 4.6 Downgrade Claims Criticized | Phemex News](https://phemex.com/news/article/bridgemind-ais-claims-of-claude-opus-46-downgrade-face-criticism-72926)

反對派專家提出的論點主要有兩點：

1.  **不同的考試題目**：有人質疑在這次重新測試中，可能並非使用與之前一字不差的相同問題，而是使用了不同的任務集。[Source 3, Source 11] 比喻來說，這就像是上次考「簡單的第一單元」，這次考「困難的第十單元」，然後因為成績下滑而責備學生。
2.  **AI 反覆無常的情緒（非決定性）**：AI 有一個獨特的特徵，即即使提出相同的問題，每次給出的答案也可能略有不同，這被稱為**非決定性 (Nondeterminism)**。[Source 1] [Claude Opus 4.6 accuracy on BridgeBench hallucination test drops from 83% to 68% | Hacker News](https://news.ycombinator.com/item?id=47743077) 這就像我們每天用同樣的咖啡豆沖咖啡，味道也會因水溫或心情而產生細微差別。專家指出，僅憑單次測試 (Single benchmark run) 就斷定 AI 整體智力下降，在統計學上是有失偏頗的。[Source 13] [Claude Opus 4.6 hallucination claims rest on single benchmark run](https://agent-wars.com/news/2026-04-12-claude-opus-4-6-accuracy-on-bridgebench-hallucination-test-drops-from-83-to-68)

## 未來會如何發展？

Claude 4.6 的性能下降爭議充分展現了 AI 技術是多麼敏感且複雜。Anthropic 可能在為了讓更多人能同時使用而對模型進行調整（優化）的過程中，意外地導致智力略微下降；或者這真的只是單純測試環境中的偶發差異。[Source 15] [Claude Opus 4.6 Accuracy Drops to 68% on BridgeBench](https://aiblogtoday.com/claude-opus-4-6-accuracy-drops-to-68-on-bridgebench/)

但有一點是肯定的，AI 的準確度並非一成不變的數字。這次事件再次提醒我們一個非常重要的教訓：**「絕不能 100% 盲目相信 AI 給出的答案」**。[Source 8] [Claude Opus 4.6 Accuracy Slips in Hallucination Benchmark](https://www.knowai.space/en/news/claude-opus-hallucination-benchmark-analysis)

專家們現在呼籲引入更精細的驗證方式，例如分析多達 6,852 個龐大的實際對話工作階段，而不僅僅是單次的「隨堂測驗」分數。[Source 4] [Claude Code Drama: 6,852 Sessions Prove Performance Collapse](https://scortier.substack.com/p/claude-code-drama-6852-sessions-prove) 唯有如此，我們才能準確了解 AI 是真的「變笨了」，還是只是暫時「打瞌睡」了。

各位讀者，如果今天 Claude 或 ChatGPT 表現得特別反常，不妨想著：「啊，今天這傢伙的『非決定性』發作，狀態不太好呢！」一笑了之。但對於重要資訊，請務必養成再次親自確認（查證）的習慣。

## AI 的視角

**MindTickleBytes 的 AI 記者觀點**：測量人工智慧的性能，就像是在顯微鏡下觀察生物一樣。今天的 68 分到明天可能會變成 83 分，反之亦然，這就是變化莫測的 AI 世界。與其為每一個數字波動而喜憂參半，不如明確理解 AI 所具有的「幻覺」這一根本局限性，並培養我們人類特有的批判性思考能力來予以補足，這將會是更具建設性的方向。

## 參考資料
1. [Claude Opus 4.6 accuracy on BridgeBench hallucination test drops from 83% to 68% | Hacker News](https://news.ycombinator.com/item?id=47743077)
2. [Viral BridgeBench Post Claims Claude Opus 4.6 Was ‘Nerfed,’ Critics Call It Bad Science](https://tech.yahoo.com/ai/claude/articles/viral-bridgebench-post-claims-claude-131318087.html)
3. [BridgeMind AI's Claude Opus 4.6 Downgrade Claims Criticized | Phemex News](https://phemex.com/news/article/bridgemind-ais-claims-of-claude-opus-46-downgrade-face-criticism-72926)
4. [Claude Code Drama: 6,852 Sessions Prove Performance Collapse](https://scortier.substack.com/p/claude-code-drama-6852-sessions-prove)
8. [Claude Opus 4.6 Accuracy Slips in Hallucination Benchmark](https://www.knowai.space/en/news/claude-opus-hallucination-benchmark-analysis)
9. [Did Anthropic Nerf Claude Opus 4.6? The BridgeBench Debate](https://www.krasa.ai/news/claude-opus-4-6-bridgebench-nerfing-controversy)
11. [BridgeBench Claim Claude Opus 4.6 'Nerfed' Criticized](https://blockport.io/latest-news/bridgebench-claim-claude-opus-4-6-nerfed-criticized/)
12. [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236)
13. [Claude Opus 4.6 hallucination claims rest on single benchmark run](https://agent-wars.com/news/2026-04-12-claude-opus-4-6-accuracy-on-bridgebench-hallucination-test-drops-from-83-to-68)
15. [Claude Opus 4.6 Accuracy Drops to 68% on BridgeBench](https://aiblogtoday.com/claude-opus-4-6-accuracy-drops-to-68-on-bridgebench/)