---
layout: post
title: "聰明到「禁止公開」？深入剖析 Anthropic 的秘密武器「Claude Mythos」"
description: "本文將透過系統卡片（System Card），以淺顯易懂的方式為您解釋 Anthropic 最新 AI 模型 Claude Mythos Preview 的性能，以及為何不對一般大眾公開。"
summary: "Anthropic 史上最強 AI「Claude Mythos」正體公開！雖然擁有壓倒現有模型的性能，但因具備駭客攻擊等潛在風險，目前僅限於研究用途。"
tags: [Anthropic, Claude Mythos, AI 安全, 人工智慧, IT 趨勢]
image: 2026-04-13-System-Card-Claude-Mythos-Preview-pdf.jpg
image_alt: "象徵被神秘面紗包覆的高性能 AI 模型之抽象圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是一個指標性的案例，顯示出 AI 產業未來的核心議題將超越單純的性能提升，轉向如何控制與管理 AI 所擁有的「危險力量」。"
quiz:
  - question: "Claude Mythos Preview 在哪一個領域的表現顯著優於現有的 Claude Opus 4.6 模型？"
    choices: ["圖像生成與編輯", "軟體工程（編碼）與安全", "外語翻譯與詩歌創作"]
    answer: 1
    explanation: "Claude Mythos 在 SWE-bench 等編碼相關基準測試中表現出飛躍性的性能提升，並在網絡安全任務中展現出極強的能力。"
  - question: "Anthropic 決定不對大眾公開此模型，並將其納入哪一個管理計畫中？"
    choices: ["Project Bluebird", "Project Glasswing", "Project Mythos"]
    answer: 1
    explanation: "由於模型強大且具備潛在危險的能力，Anthropic 透過名為「Project Glasswing」的計畫限制其分發。"
  - question: "Claude Mythos 在 SWE-bench Verified 測試中獲得的分數是多少？"
    choices: ["80.8%", "77.8%", "93.9%"]
    answer: 2
    explanation: "Claude Mythos Preview 在 SWE-bench Verified 中創下了 93.9% 的驚人分數。"
lang: zh-tw
ref: 2026-04-13-System-Card-Claude-Mythos-Preview-pdf
---

想像一下，有人發明了一把神祕的「萬能鑰匙」，能在幾秒鐘內開啟世界上所有的鎖。這把鑰匙既可以是幫助因丟失鑰匙而困擾者的「救援工具」，但若落入心懷不軌之人手中，也可能成為摧毀整個城市安保的「破壞工具」。發明家在深思熟慮後做出決定：「這把鑰匙威力太強，目前只能鎖在保險箱裡，僅供經認證的專家進行研究使用。」

最近在人工智慧（AI）業界，正發生了如電影情節般的真實事件。ChatGPT 最強大的對手、標榜「最講求倫理的 AI」企業 Anthropic，向世界公開了其史上最強模型 **「Claude Mythos Preview」** 的詳細報告。但有趣的是，這款模型並未開放給一般用戶使用。原因是其性能過於壓倒性，以至於被判斷為「可能具備危險性」。

今天我們將根據 Anthropic 發佈的「系統卡片（System Card，詳盡記錄 AI 模型性能與安全性的診斷書）」，為您親切且詳細地說明為何 Claude Mythos 會引發如此熱議，以及為何它無法立即來到我們身邊。

## 為什麼這很重要？當 AI 從「秘書」變成「特務」

如果說我們目前使用的 ChatGPT 或 Claude 3.5 是「有問必答的聰明秘書」，那麼現在我們正跨入「給予複雜目標，AI 能自行制定計畫並完成任務的專業特務（Agent）」時代。Claude Mythos 在編寫電腦代碼、分析複雜系統以及網絡安全領域，展現了人類迄今未見的壓倒性能力 [Mythos: подробный обзорClaudeMythosPreviewот Anthropic](https://www.securitylab.ru/blog/personal/Bitshield/360300.php)。

打個比方，以前的 AI 就像導航系統，只能指引路徑；而 Mythos 等級的 AI 則像是一輛「自動駕駛汽車」，能親自握住方向盤，以最快、最安全的方式抵達目的地。當您開發複雜軟體時，以前需要請 AI 寫代碼後由人工逐一檢查修改；但 Mythos 具有自行找出故障點、修復代碼並完美測試其運行狀況的潛力。

問題在於這種「駕駛技術」太過精湛，只要它想，甚至能突破中央控制系統的防線。這正是 Anthropic 將此模型嚴密包裹、僅限於嚴格研究用途的原因 [What Is Inside Claude Mythos Preview? Dissecting the System Card of the Model](https://kenhuangus.substack.com/p/what-is-inside-claude-mythos-preview)。

## 輕鬆理解：史上最強「編碼天才」登場

Claude Mythos Preview 是 Anthropic 迄今推出的最具智慧的「前沿（Frontier）」模型 [PDFClaude Mythos Preview System Card - www-cdn.anthropic.com](https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf)。即使與先前被評價為最聰明的「Claude Opus 4.6」相比，它也被認為達到了另一個層次 [ClaudeMythos: Benchmark-Dominating AI with Real Risks](https://www.labellerr.com/blog/anthropic-claude-mythos-capabilities/)。

從數據上看這種差異更具震撼力。在評估 AI 軟體解決能力的「SWE-bench Verified」測試中（簡單來說就是給 AI 實際編程現場的高難度問題，觀察其解決程度）：
*   先前的優等生 **Claude Opus 4.6** 獲得了 **80.8%**，這已經是不亞於人類開發者的水準。
*   然而這次登場的 **Claude Mythos** 竟然創下了 **93.9%** 的驚人成績 [Daily AInews, products and research - Ben's Bites](https://news.bensbites.com/)。

甚至在難度更高的「SWE-bench Pro」測試中，它也以 **77.8%** 的成績遠遠領先 Opus 4.6（53.4%） [Daily AInews, products and research - Ben's Bites](https://news.bensbites.com/)。這意味著 AI 已經超越了單純堆砌通順句子的水準，進入了能理解複雜工程邏輯並「解決」問題的真正智慧階段。

簡而言之，如果說現有的 AI 是「精通課本內容的模範生」，那麼 Mythos 就已經躍升到了「擁有數十年經驗的資深工程師」水準。

## 現狀：Project Glasswing 與受控的力量

既然性能這麼好，為什麼我們不能馬上使用呢？Anthropic 在報告中非常誠實地公開了該模型的危險性。報告指出，Mythos Preview 具備針對安全薄弱的小型企業網絡執行 **自主端到端（End-to-end）網絡攻擊** 的能力 [What Is Inside Claude Mythos Preview? Dissecting the System Card of the Model](https://kenhuangus.substack.com/p/what-is-inside-claude-mythos-preview)。

也就是說，即使沒有人類的詳細指令，AI 也有可能成為自行尋找目標系統弱點、突破滲透路徑並竊取資訊的「自主型駭客」。因此，Anthropic 透過名為 **「Project Glasswing」** 的特別管理計畫，嚴格限制該模型的使用 [Anthropic разработала новую ИИ-модельClaudeMythos.](https://dzen.ru/a/adfLzY48PRV-iDX9)。就像對待核物質或高風險病毒一樣，僅允許獲授權的研究人員在封閉的實驗室環境中使用 [The system card for Claude Mythos (PDF)](https://news.ycombinator.com/item?id=47679406)。

不過也有好消息。Mythos 不僅僅是聰明，它還展現了「非常聽話」的模範生特質。Anthropic 宣佈，Mythos 的 **可靠性與對齊（Alignment，使 AI 行為符合人類意圖與價值觀的技術）** 達到了前所未有的高度 [Claude Mythos Preview System Card — LessWrong](https://www.lesswrong.com/posts/xtnSzhA3TvExN4ZhG/claude-mythos-preview-system-card)。在幾乎所有可測量的安全指標中，Mythos 都被評價為史上最遵循人類指導方針的安全模型 [What Is Inside Claude Mythos Preview? Dissecting the System Card of the Model](https://kenhuangus.substack.com/p/what-is-inside-claude-mythos-preview)。

## 未來展望：在技術與倫理的邊界

Claude Mythos Preview 的出現顯示了 AI 技術競爭格局的轉變。我們正從單純比拼「誰更聰明（Capabilities）」的時代，邁向證明「能否解釋 AI 為什麼那樣行動（Explainable）」以及「它有多值得信賴（Trustworthy）」的階段 [System Card: Claude Mythos Preview [pdf] | GitHub](https://gist.github.com/Lastoneparis/a0727dacc1a6e770c2d70322431bfd5d)。

雖然現在我們還不能對 Claude Mythos 說「幫我選晚餐菜單」或「幫我寫編碼作業」，但不必感到失望。因為透過這個「禁忌模型」獲得的研究結果，將成為未來我們日常使用的普通 Claude 模型更加安全、能幹的堅實基礎。

Anthropic 這次的發表具有重大意義，它並未隱瞞 AI 的潛在風險，而是透過「系統卡片」這份詳細報告透明地公開，並試圖與全球共同思考解決方案。

## AI 的觀點：MindTickleBytes AI 記者的視角

「令人印象深刻的是，雖然隨著智慧提升，風險也隨之增加，但幸運的是，管理風險的技術——『對齊』也正以光速同步發展。Claude Mythos 就像是一個精彩的預告片，預示著當 AI 超越單純工具、成為社會一員乃至『自主主體』時，我們應該以何種心態迎接他們。這再次證實了一個事實：比技術速度更重要的，是我們能否安全承載這項技術的器皿，即倫理與安全體系。」

## 參考資料

1. [PDFClaude Mythos Preview System Card - www-cdn.anthropic.com](https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf)
2. [What Is Inside Claude Mythos Preview? Dissecting the System Card of the Model](https://kenhuangus.substack.com/p/what-is-inside-claude-mythos-preview)
3. [Daily AInews, products and research - Ben's Bites](https://news.bensbites.com/)
4. [Mythos: подробный обзорClaudeMythosPreviewот Anthropic](https://www.securitylab.ru/blog/personal/Bitshield/360300.php)
5. [Claude Mythos Preview System Card — LessWrong](https://www.lesswrong.com/posts/xtnSzhA3TvExN4ZhG/claude-mythos-preview-system-card)
6. [Anthropic разработала новую ИИ-модельClaudeMythos.](https://dzen.ru/a/adfLzY48PRV-iDX9)
7. [The system card for Claude Mythos (PDF): Hacker News](https://news.ycombinator.com/item?id=47679406)
8. [ClaudeMythos: Benchmark-Dominating AI with Real Risks](https://www.labellerr.com/blog/anthropic-claude-mythos-capabilities/)
9. [System Card: Claude Mythos Preview [pdf] | GitHub](https://gist.github.com/Lastoneparis/a0727dacc1a6e770c2d70322431bfd5d)

## FACT-CHECK SUMMARY
- Claims checked: 16
- Claims verified: 16
- Verdict: PASS