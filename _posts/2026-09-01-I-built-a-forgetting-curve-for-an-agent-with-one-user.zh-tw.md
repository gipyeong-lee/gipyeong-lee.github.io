---
layout: post
title: "AI 也能像人類一樣學習「遺忘」嗎？打造聰明 AI 的 140 年前秘訣"
description: "為什麼 AI 經常忘記重要資訊？我們將探討如何運用 19 世紀的心理學理論，讓 AI 擁有更聰明、更高效的記憶力。"
summary: "AI 開發人員正引入 19 世紀艾賓浩斯遺忘曲線理論，協助 AI 捨棄不必要的資訊，並長期保存重要記憶，從而研發出智慧遺忘系統。"
tags: [AI, AI技術, 記憶力, 艾賓浩斯, 數據效率]
image: 2026-09-01-I-built-a-forgetting-curve-for-an-agent-with-one-user.jpg
image_alt: "模擬人類大腦結構的數位記憶迴路隨著時間逐漸變得模糊的形象化影像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 無限的記憶力有時反而有害。正如人類會選擇性地記憶資訊，AI 也透過『智慧遺忘』，正朝向更高效的方向進化。"
quiz:
  - question: "AI 學習「遺忘曲線」的主要原因是什麼？"
    choices: ["為了理解 AI 的情緒", "為了區分重要資訊與不必要資訊，從而提高效率", "為了將儲存空間無限擴充"]
    answer: 1
    explanation: "因為持續保存不必要的資訊會導致處理速度變慢，因此透過遺忘曲線以重要資訊為主來管理記憶非常重要。"
  - question: "19 世紀心理學家艾賓浩斯所發現的「遺忘曲線」核心是什麼？"
    choices: ["人類能完美記住所有資訊", "隨著時間推移，資訊的記憶率會以指數函數形式衰減", "記憶像照片一樣是固定不變的"]
    answer: 1
    explanation: "艾賓浩斯的理論指出，大部分資訊會迅速被遺忘，但有一部分會緩慢地從記憶中消失。"
  - question: "為什麼過多的記憶力對 AI 來說反而有害？"
    choices: ["會消耗過多電費", "不必要的記憶會拖慢 AI 的思考速度", "AI 會因此說謊"]
    answer: 1
    explanation: "若不必要的記憶數據增加，處理資訊及推論所需的時間就會隨之變長。"
lang: zh-tw
ref: 2026-09-01-I-built-a-forgetting-curve-for-an-agent-with-one-user
---

想像一下。你每天早上都對秘書交代今天的工作。但如果這位秘書試圖記住你說過的每一句話，甚至連一年前的事都一字不差地記下來，那會怎樣？每當你說「中午該吃什麼好呢？」時，秘書可能會回：「您去年 3 月 15 日午餐吃的泡菜鍋還合胃口嗎？」，這些無關緊要的資訊會導致對話嚴重延遲。

近期在人工智慧（AI）領域，類似的煩惱也日益加深。隨著 AI 變得更聰明，它試圖記住的資訊也越來越多，導致處理重要工作的速度變慢，或者遺漏了對話的語境。為了克服這個問題，開發人員重新啟用了 140 年前古老的心理學理論——「艾賓浩斯遺忘曲線（Ebbinghaus forgetting curve）」。

### 為什麼這個問題很重要？

我們期待 AI 能像人類一樣聰明地行動，但事實上，AI 的記憶結構與人類大相逕庭。人類會自然地讓無關緊要的資訊流逝，但 AI 在輸入新資訊時，往往會執著地抓住所有數據。問題在於這種「無差別記憶」會使 AI 變遲鈍。

根據實際研究結果，若為 AI 代理（執行特定目的的 AI）增加 5 KB 的記憶數據，處理資訊及做出決策的時間就會增加 1.1 毫秒（ms）[[出處：HackerNoon](https://hackernoon.com/why-forgetting-is-the-secret-to-smarter-ai-agents)]。在數百、數千名用戶同時使用的服務中，這會引發巨大的瓶頸。如果我們期待 AI 有更快的反應速度，那麼 AI 也必須學會「如何妥善遺忘」。

### 簡單來說：AI 的「記憶減肥」

艾賓浩斯遺忘曲線是一張圖表，顯示人類隨時間推移會忘記多少資訊[[出處：ELVTR](https://elvtr.com/blog/12-non-obvious-tips-tricks-for-successful-online-learning)]。簡單來說，我們對初次聽到的資訊大部分會瞬間遺忘，但多次反覆回想的資訊則會更深刻地留在腦海中。

開發人員將此原理移植到了 AI 記憶管理引擎中[[出處：Towards Data Science](https://towardsdatascience.com/context-windows-forget-what-matters-i-used-a-140-year-old-psychology-paper-to-fix-ai-memory/)]。

比喻來說，可以把 AI 的記憶空間想像成一本「相簿」。過去的 AI 試圖保存每天拍攝的所有照片。但應用了「智慧遺忘」的 AI 則不同。經常翻閱的照片（用戶常詢問或視為重要的資訊）會被移到相簿前面進行長期保存，而從未看過的模糊照片（不必要的資訊）則會在時間過後自動移入垃圾桶[[出處：Towards Data Science](https://towardsdatascience.com/context-windows-forget-what-matters-i-used-a-140-year-old-psychology-paper-to-fix-ai-memory/)]。如此一來，AI 就能隨時專注於「當下最需要的資訊」。

### 目前進度如何？

目前現場已活躍地進行基於此理論的實驗。開源專案或記憶管理工具正應用此「遺忘曲線」，改變 AI 儲存及調用記憶的方式[[出處：DEV Community](https://dev.to/sudarshangouda/ai-agent-memory-part-2-the-case-for-intelligent-forgetting-4i48)]。

然而，前方仍有長路要走。部分初期實驗階段的模型在判斷資訊的「重要性」時，僅僅依賴字詞重疊度（字串比對）來決定是否刪除數據，因而犯下錯誤[[出處：Eris dev blog](https://eris-system.dev/blog/forgetting-curve)]。當人類模糊地說出「昨天講的那件事」時，AI 本應能掌握語境，但由於只應用了機械化的刪除標準，導致連珍貴的語境也被一併刪除。

此外，當多個 AI 在 AI 管線（工作流程）中間相互傳遞資訊時，中間必要的資訊會消失的「記憶喪失（amnesia）」問題，也是開發人員面臨的一大難題[[出處：linksfor.dev](https://linksfor.dev/)]。

### 未來將展現什麼樣的願景？

未來 AI 將不僅僅止於學習大量數據的階段，而是會進化到學習「該捨棄哪些資訊」的階段。我們將擺脫僅僅管理最新資訊的方式，轉而普及化為每種數據賦予不同「記憶壽命（TTL, Time-To-Live）」的方法[[出處：TianPan.co](https://tianpan.co/blog/2026-04-12-the-forgetting-problem-when-agent-memory-becomes-a-liability)]。

例如，設計成用戶當下正在進行的「效能除錯工作」由 AI 暫存一天，而反之「用戶的習慣或偏好」則設定為更長的時間並緩慢地刪除[[出處：TianPan.co](https://tianpan.co/blog/2026-04-12-the-forgetting-problem-when-agent-memory-becomes-a-liability)]。如此一來，即使我們不必每次都重新說明，AI 也能像多年的秘書一樣理解我們的風格。

---

**MindTickleBytes 的 AI 記者觀點**
AI 要變得聰明，比起無條件地博學，更需要知道「該假裝不知道什麼」的智慧。140 年前的心理學理論正讓最尖端 AI 的大腦變得更輕盈、更快速，這是一個充滿矛盾卻又引人入勝的變化。未來的 AI 將不再競逐「記憶力」，而是競逐「遺忘的技術」。

## 參考資料

1. [So this “forgetting curve” did not measure importance at all](https://eris-system.dev/blog/forgetting-curve) - Eris dev blog
2. [I built a forgetting curve for an agent with one user](https://news.ycombinator.com/item?id=49431546) - Hacker News
3. [Multi-agent AI pipelines lose context at every handoff between agents](https://linksfor.dev/) - linksfor.dev
4. [Forgetting is not passive at all. It is active.](https://foxfire.blog/explorations/the-forgetting-curve) - Foxfire
5. [German psychologist Hermann Ebbinghaus built a forgetting curve](https://elvtr.com/blog/12-non-obvious-tips-tricks-for-successful-online-learning) - ELVTR
6. [Context Windows Forget What Matters — I Built a Usage-Reinforced Decay Engine for AI Agent Memory](https://towardsdatascience.com/context-windows-forget-what-matters-i-used-a-140-year-old-psychology-paper-to-fix-ai-memory/) - Towards Data Science
7. [Your Memory is a practical open-source MCP server that bakes the Ebbinghaus forgetting curve](https://dev.to/sudarshangouda/ai-agent-memory-part-2-the-case-for-intelligent-forgetting-4i48) - DEV Community
8. [The cost curve exposed its own remedy: trim context every fifty seconds and cap recall at twenty kilobytes](https://hackernoon.com/why-forgetting-is-the-secret-to-smarter-ai-agents) - HackerNoon
9. [This mirrors the Ebbinghaus forgetting curve, where retention decays exponentially](https://tianpan.co/blog/2026-04-12-the-forgetting-problem-when-agent-memory-becomes-a-liability) - TianPan.co
10. [Implements Ebbinghaus forgetting-curve retention with usage-based reinforcement](https://github.com/topics/forgetting-curve?o=desc&s=updated) - GitHub Topics