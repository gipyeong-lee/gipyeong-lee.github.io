---
layout: post
title: "AI 撰寫文件的方式即將改變？以「網頁」取代文字對話的時代"
description: "最近 AI 開發者之間正流行將 AI 的回答從單純的文字或 Markdown 改為 HTML 格式。本文將為您深入淺出地解釋這項由 Anthropic 工程師發起的有趣變革及其背後原因。"
summary: "隨著 AI 產出結果的基本形式從單純文字轉向具備豐富視覺表現力的 HTML，我們與 AI 溝通的方式也正變得更加直觀且多樣化。"
tags: [AI趨勢, Claude, HTML, Markdown, 提示工程]
image: 2026-05-18-Using-Claude-Code-The-unreasonable-effectiveness-of-HTML.jpg
image_alt: "描繪電腦螢幕中單純文字轉換為華麗且具互動性網頁過程的 3D 插畫"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "從人類易讀的格式轉向機器能產出最佳視覺效果的格式，是一個強大的訊號，表明 AI 正從單純的「輔助作者」進化為「獨立的內容生產者」。"
quiz:
  - question: "最近由 Anthropic 工程師 Thariq 提議作為 AI 代理預設輸出格式而引起話題的格式是？"
    choices: ["Markdown", "Python", "HTML"]
    answer: 2
    explanation: "Anthropic 的 Claude Code 團隊負責人 Thariq Shihipar 強力主張使用 HTML 代替 Markdown 作為 AI 代理的輸出格式。"
  - question: "關於將 AI 的產出從 Markdown 改為 HTML 的主要優點，下列何者未被提及？"
    choices: ["視覺豐富的圖表表現", "方便人類直接修改和編輯文字", "包含雙向互動功能"]
    answer: 1
    explanation: "雖然 HTML 視覺效果優異，但因代碼複雜，反而被指出在人類直接閱讀與編輯以進行「共同創作（Co-authoring）」方面，不如 Markdown 方便。"
  - question: "Thariq 的文章在引起爆炸性反應後，登上了哪個開發者社群的榜首？"
    choices: ["Hacker News", "Reddit", "Stack Overflow"]
    answer: 0
    explanation: "Thariq 的文章包含 20 個完整的 HTML 範例，登上了 Hacker News 的榜首並引發了巨大的討論。"
lang: zh-tw
ref: 2026-05-18-Using-Claude-Code-The-unreasonable-effectiveness-of-HTML
---

想像一下。早上上班後，你對 AI 助手說：「幫我整理一下今天下午新產品企劃會議的資料」。到目前為止，AI 通常會在黑底白字的畫面上，頂多混合一些粗體或項目符號（•），以純文字的形式給出答案。我們必須複製那些文字，貼到 PowerPoint 或 Word 文件中，然後再經歷繪製表格、塗色等麻煩的後續處理。

但是，如果 AI 不僅僅是寫文字，而是當場製作出一個包含可點擊按鈕、五彩繽紛圖表以及精美排版完美的「網頁」呢？你只需要打開螢幕，就可以直接開始會議。

最近，在矽谷的 AI 專家之間，這種對話方式成為了熱門話題。這是一場主張將 AI 的回答從單純的文字格式，轉向製作網路內容的語言——「HTML」的運動。究竟為什麼會發生這種變化？對於一般的用戶來說，這又意味著什麼呢？

## 為什麼這很重要？ (Why It Matters)

一直以來，當我們與 ChatGPT 或 Claude 等 AI 對話時，AI 回饋給我們的基本格式是「Markdown」。Markdown 是一種非常簡單且輕量的文字撰寫方式。Anthropic 的 Claude 甚至展現出驚人的能力，能透過在 Markdown 檔案中組合特殊字元（ASCII）來繪製簡易的表格或圖表 [[Using Claude Code: The Unreasonable Effectiveness of HTML](https://www.techtwitter.com/articles/using-claude-code-the-unreasonable-effectiveness-of-html)]。Markdown 具有體積輕巧、在任何環境下都能開啟，以及最重要的是人類非常容易直接閱讀和修改等壓倒性優點，因此穩固地成為了 AI 代理與我們溝通的主流檔案格式 [[Using Claude Code: The Unreasonable Effectiveness of HTML](https://www.techtwitter.com/articles/using-claude-code-the-unreasonable-effectiveness-of-html)]。

然而，世界正在快速改變。隨著 AI 變得越來越聰明，人們現在開始要求 AI 不僅僅是「撰寫草稿」，而是產出更接近「最終成果」的東西。

如果說 Markdown 是以文字為中心的靜態「文件」，那麼 HTML 就是能包含色彩、圖像甚至是動態效果的「綜合藝術」。這種微小格式差異之所以重要，是因為它是一個明確的訊號，表明我們利用 AI 的方式正從單純的「寫作助手」轉向「完整的應用程式及內容製作者」。

利用 HTML，我們可以獲得複雜的數據視覺化、可雙向操作的互動功能，以及非常適合即時分享給他人的豐富成果 [[TheUnreasonableEffectivenessofHTMLinClaudeCode: Why...](https://www.explainx.ai/blog/unreasonable-effectiveness-html-claude-code-thariq-2026)]。我們不再需要複製 AI 的回答再進行潤飾，它本身就能作為一份完整的報告、設計提案，甚至是小型程式來運作。這不僅對開發者，對完全不懂程式的一般人來說，也開啟了一個能將想像力即時轉化為可見成果的新時代。

## 輕鬆理解 (The Explainer)

為了更清楚地理解這種情況，我們來做個比喻。

簡單來說，Markdown 就像是在辦公用便利貼或橫線筆記本上寫下的整齊「備忘錄」。核心內容整理得很好，也可以用螢光筆畫底線（粗體）或編號來裝飾。任何人都能輕易辨認，修改文字也很方便。但是，要把那本筆記本身當作最終發表資料，就顯得有些平淡。

相反地，HTML 就像是一本全彩印刷，甚至按按鈕還會發出聲音的「高級互動雜誌」。憑藉華麗的色彩和精心的構圖，一眼就能吸引人們的視線。

過去因為 AI 的實力還有些生疏，所以當 AI 抓好骨架（初稿備忘錄）後，人類必須親自接收並進行包裝（製作成雜誌）。因此，方便人類閱讀和修改的「Markdown」格式自然是首選。但現在 AI 代理已經變得非常聰明，可以獨自承擔創作內容的重擔。人類親自手動編輯 AI 成果的情況幾乎消失了 [[UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://andrey-markin.com/directory/claude-code-html)]。既然人類不需要刻意修改，那麼從一開始就直接以能表現更豐富視覺效果、圖表和色彩的 HTML 來輸出完整結果，反而更具效益，這便是此項主張背景 [[UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://andrey-markin.com/directory/claude-code-html)]。

再舉另一個比喻吧。假設你想擁有一輛漂亮的汽車。
過去，你會請求 AI：「幫我畫一份建造現代化汽車工廠的複雜設計圖（Web 框架代碼）」。因為太過宏大且複雜，既耗時又容易迷失方向。然而，聰明的開發者很快就意識到，直接要求：「現在就給我造一輛能在路上跑的汽車（純 HTML）」才是達到目標更快、更有效率的路徑 [[ClaudeCodeJust SolvedHTMLin Ways We... | Cynthia Media](https://media.cynthiaconcierge.com/using-claude-code-the-unreasonable-effectiveness-of-html-tool-drop/)]。

## 現狀 (Where We Stand)

點燃這場有趣爭論的人，是 Anthropic 負責領導「Claude Code」開發團隊的工程師 Thariq Shihipar。他在 2026 年 5 月發表了一篇內容具挑釁性且極具魅力的文章，標題為「要求 HTML 取代 Markdown 作為 Claude 的輸出格式，其效果好得令人難以置信」 [[UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/)], [[HTMLvs Markdown inClaudeCode: Why Anthropic's Thariq Changed...](https://pasqualepillitteri.it/en/news/2243/html-vs-markdown-claude-code-thariq-anthropic)]。

Thariq 斷言，在指派工作給最新的 AI 代理時，Markdown 的時代正逐漸遠去，HTML 的時代即將到來 [[Anthropic Engineer Sparks Debate: HTML Is the New Markdown ...](https://noqta.tn/en/news/anthropic-thariq-html-over-markdown-ai-outputs-2026)]。為了支持他的觀點，他同時公開了多達 20 個完整的 HTML 範例，展示了 HTML 在提高資訊密度、實現互動，以及在企劃書、代碼審查、設計原型（產品原型）等實際工作環境中如何實用地被發揮 [[TheUnreasonableEffectivenessofHTMLinClaudeCode: Why...](https://www.explainx.ai/blog/unreasonable-effectiveness-html-claude-code-thariq-2026)], [[Anthropic Engineer Sparks Debate: HTML Is the New Markdown ...](https://noqta.tn/en/news/anthropic-thariq-html-over-markdown-ai-outputs-2026)]。

這篇文章的影響力確實非常巨大。它在聚集了全球頂尖開發者的社群「Hacker News」上迅速登上榜首（Top），引發了人們對於消費 AI 成果方式的巨大認知轉變 [[Anthropic Engineer Sparks Debate: HTML Is the New Markdown ...](https://noqta.tn/en/news/anthropic-thariq-html-over-markdown-ai-outputs-2026)]。在 Twitter (X) 等社交媒體上，也廣泛流傳著稱讚 HTML 優點的文章，認為它能極大化清晰度與互動性，並呼籲「別再停留於乏味的 Markdown」 [[Using Claude Code: The Unreasonable Effectiveness of HTML](https://youmind.com/landing/x-viral-articles/claude-code-html-effectiveness)]。

但並非所有人都舉雙手歡迎這個觀點。一些深入的反對意見也被提出。
最大的擔憂在於，人類與 AI 的「共同創作（Co-authoring）」可能會變得極端困難 [[Using Claude Code with HTML: Why It Works—and the Co ...](https://ideaverse.ai/blog/using-claude-code-with-html-why-it-works-and-the-co-authoring-tradeoff-moyv58kx)]。

在 Hacker News 的討論中，一位開發者坦白道：「我自己親手編寫複雜的 HTML 表格可能比編寫 Markdown 表格快。但在除此之外的情況下，無論 AI 自動化做得多好，看著純 HTML 代碼來保持閱讀與寫作流程（Writing flow）的流暢是非常困難的」 [[Using Claude Code: The unreasonable effectiveness of HTML ...](https://news.ycombinator.com/item?id=48071940)]。

也就是說，螢幕上看到的成果雖然變美了，但人類去拆解成果的背面（代碼）並一同修改的過程，會因為代碼過於複雜而反而受到干擾，這便是一個矛盾的存在。

實際上，就連引領這股潮流的 Thariq 也提到，為了閱讀代理輸出的冗長複雜 HTML，他必須使用開發者工具 VIM 或將 macOS 的「快速查看（Quicklook）」功能連接到特殊的擴充程式，或者將其貼到某處才能正確掌握內容 [[UsingClaudeCode:TheunreasonableeffectivenessofHTML](https://modernorange.io/item/48071940)]。對一般人來說，依然存在著技術門檻。

## 未來發展 (What's Next)

儘管存在這些優缺點，開發者和使用者已經在快速適應並進化。
在社群中，將引導 AI 一次生成完美 HTML 的有效提示詞（指令）設定檔，以模板形式進行整理和分享的文化正在蓬勃發展 [[ClaudeCodeHTMLPrompts & GPT-5.5 API Cost... - DEV Community](https://dev.to/soytuber/claude-code-html-prompts-gpt-55-api-cost-changes-highlight-developer-focus-3kdg)]。此外，介紹如何熟練操作 Claude Code 的進階功能和工作流程的 YouTube 教學影片也紛紛湧現 [[MasteringClaudeCodein 30 minutes - YouTube](https://www.youtube.com/watch?v=6eBSHbLKuN0)]。

未來，這種擴展性預計將超越文字，擴大到媒體領域。例如，有預測認為，利用 Codex 或 Claude Code，使用者可以直接生成播客（Podcast）形式的音訊內容，並將其直接導入（import）到全球最大的音樂平台 Spotify，成果的形式將超越網頁，變得更加多樣且立體 [[UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://aiflow.news/2026/05/08/using-claude-code-the-unreasonable-effectiveness-of-html)]。

總結來說，對於日常簡短對話或備忘，Markdown 仍會繼續存在，但在需要複雜報告、企劃案、視覺資料的工作中，要求「基於 HTML 的成果」很可能成為新的常識。我們現在不再對 AI 說「用文字解釋給我聽」，而是會理直氣壯地要求「給我看一個精美的網頁，讓我點點看」。

---

## AI 的觀點 (AI's Take)

當格式（Format）改變時，我們的思考方式也會隨之改變。隨著 AI 脫離平面文字的狹窄牢籠，插上立體網頁技術（HTML）的翅膀，我們現在應該將 AI 視為一個充滿生命力的「獨立內容生產者」，以及擁有無限可能的「畫布」，而非單純的「打字機」。

從人類易讀易改的格式轉向機器能噴發最佳視覺效果格式的轉變，是一個強大的訊號，表明 AI 已經超越了單純的「輔助作者」。我們投下的下一個提示詞，將不再僅限於創造句子，而是會創造出一個讓人們能親自觸摸與體驗的完整世界。

## 參考資料

1. [UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/)
2. [TheUnreasonableEffectivenessofHTMLinClaudeCode: Why...](https://www.explainx.ai/blog/unreasonable-effectiveness-html-claude-code-thariq-2026)
3. [UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://andrey-markin.com/directory/claude-code-html)
4. [ClaudeCodeJust SolvedHTMLin Ways We... | Cynthia Media](https://media.cynthiaconcierge.com/using-claude-code-the-unreasonable-effectiveness-of-html-tool-drop/)
5. [HTMLvs Markdown inClaudeCode: Why Anthropic's Thariq Changed...](https://pasqualepillitteri.it/en/news/2243/html-vs-markdown-claude-code-thariq-anthropic)
6. [ClaudeCodeHTMLPrompts & GPT-5.5 API Cost... - DEV Community](https://dev.to/soytuber/claude-code-html-prompts-gpt-55-api-cost-changes-highlight-developer-focus-3kdg)
7. [UsingClaudeCode:TheunreasonableeffectivenessofHTML](https://modernorange.io/item/48071940)
8. [UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://aiflow.news/2026/05/08/using-claude-code-the-unreasonable-effectiveness-of-html)
9. [MasteringClaudeCodein 30 minutes - YouTube](https://www.youtube.com/watch?v=6eBSHbLKuN0)
10. [Using Claude Code: The unreasonable effectiveness of HTML ...](https://news.ycombinator.com/item?id=48071940)
11. [Using Claude Code: The Unreasonable Effectiveness of HTML](https://www.techtwitter.com/articles/using-claude-code-the-unreasonable-effectiveness-of-html)
12. [Using Claude Code: The Unreasonable Effectiveness of HTML](https://youmind.com/landing/x-viral-articles/claude-code-html-effectiveness)
13. [Using Claude Code with HTML: Why It Works—and the Co ...](https://ideaverse.ai/blog/using-claude-code-with-html-why-it-works-and-the-co-authoring-tradeoff-moyv58kx)
14. [Anthropic Engineer Sparks Debate: HTML Is the New Markdown ...](https://noqta.tn/en/news/anthropic-thariq-html-over-markdown-ai-outputs-2026)