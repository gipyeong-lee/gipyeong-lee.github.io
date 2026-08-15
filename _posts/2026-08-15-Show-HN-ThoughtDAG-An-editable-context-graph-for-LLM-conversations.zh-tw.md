---
layout: post
title: "與 AI 的對話，只在聊天視窗中進行嗎？現在就來畫出「思考導圖」：ThoughtDAG 的故事"
description: "介紹 ThoughtDAG，這是一款能將與 AI 的複雜對話視覺化，並像思考導圖一樣進行編輯的工具。"
summary: "ThoughtDAG 是一款開源工具，它能將線性的 AI 對話記錄轉換為可編輯的圖譜形式，讓使用者能直觀地查看並控制傳遞給 AI 的上下文（Context）。"
tags: [AI, 生產力, ThoughtDAG, 介面, LLM]
image: 2026-08-15-Show-HN-ThoughtDAG-An-editable-context-graph-for-LLM-conversations.jpg
image_alt: "AI 對話記錄以多分支導圖形式視覺化的無限畫布畫面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "與 AI 的對話並非直線，而是發散的思考過程。將其視覺化為導圖，是人類奪回人工智慧運用主導權非常重要的一步。"
quiz:
  - question: "ThoughtDAG 與現有 AI 聊天介面最大的區別是什麼？"
    choices: ["提升 AI 的運行速度", "能將對話記錄視覺化為基於圖譜的導圖形式並進行編輯", "大幅增強 AI 的智慧能力"]
    answer: 1
    explanation: "ThoughtDAG 不使用線性的聊天視窗，而是在無限畫布上讓對話以分支圖譜的形式呈現，讓使用者能像繪製思考導圖一樣管理對話。"
  - question: "在 ThoughtDAG 中，「導線（Wire）」的含義是什麼？"
    choices: ["AI 伺服器連接狀態", "實際傳遞給 AI 的上下文（Context）", "使用者的網路速度"]
    answer: 1
    explanation: "在 ThoughtDAG 中，作為圖譜連接線的「導線（Wire）」定義了傳遞給 AI 的上下文。"
  - question: "下列何者不是使用 ThoughtDAG 可以進行的操作？"
    choices: ["修剪對話內容的部分分支（Prune）", "視覺化確認對話流程", "修改 AI 模型本身的參數"]
    answer: 2
    explanation: "ThoughtDAG 並非修改 AI 模型內部參數的工具，而是一個視覺化並編輯對話上下文的介面工具。"
lang: zh-tw
ref: 2026-08-15-Show-HN-ThoughtDAG-An-editable-context-graph-for-LLM-conversations
---

試想一下，假設您正在與 AI 進行一項極為漫長的研發專案。起初，對話是以「氣候變遷」這個宏大的主題開始的，隨後話題不斷延伸，從「海平面上升」談到「環保建築技術」，最後落腳在「特定材質的耐久性」。然而，AI 突然失去了上下文，開始給出一些莫名其妙的回答。究竟是從哪裡開始出錯的呢？

目前我們使用的大多數對話式 AI 介面，都將聊天視窗管理得如同永無止境的捲軸。這是一種必須不斷向上滾動才能找到線索的結構。最近，一個有趣的開源專案出現，完美解決了這種令人沮喪的情況，那就是「ThoughtDAG」。

## 為什麼這很重要？

事實上，我們的思考絕非直線。當我們進行研究或規劃時，我們會發散思維、大膽刪除無用的方向，並挑選重要資訊重新整合。然而，既有的 AI 服務會將所有對話記錄按順序傳送給 AI。 [出處: DEV Community](https://dev.to/chenxiachan/i-made-llm-context-editable-a-graph-where-the-wires-are-the-prompt-2afl) 在此過程中，AI 會收到使用者不需要的過去資訊，導致回答失焦，甚至產生不必要的費用。

ThoughtDAG 不僅是「記錄」與 AI 的對話，而是將其變成「思考導圖」。使用者可以親眼確認哪些分支是重要的研究，哪些則是該捨棄的假設，並精準控制傳遞給 AI 的資訊。 [出處: ThoughtDAG — Make LLM context visible and editable](https://chenxiachan.github.io/thoughtdag/)

## 輕鬆理解

為了方便理解 ThoughtDAG 的運作原理，請試著想像「Photoshop 的圖層」或「地圖」。

1. **無限畫布**：不再是聊天視窗，對話會以「節點（點）」的形式在無限延伸的畫布上逐一生成。 [出處: GitHub - thoughtdag](https://github.com/chenxiachan/thoughtdag)
2. **導線（Wire）即上下文**：連接畫布上節點的線被稱為「導線（Wire）」。只有這些導線連接的部分，才會成為傳遞給 AI 的「上下文（Context）」。 [出處: ThoughtDAG — your thinking deserves a map](https://app.thoughtdag.workers.dev/) 換句話說，只要移動導線，就能立即更改 AI 所參考的資料。
3. **保留具價值的決策**：通常當對話變長時，AI 會自行總結內容，此時重要的背景資訊往往會消失。ThoughtDAG 則能完整保留人類親自標記的重要決策，防止聊天機器人隨意壓縮內容，並能透明地確認所有過程。 [出處: AiA Feed](https://aiforanything.io/feed/post/cfd83df1-f9c2-448d-a67f-33df68986a58)

例如，在對話中閱讀 PDF 文件、上傳圖片或添加新點子時，ThoughtDAG 都會將其添加為圖譜的一個碎片。 [出處: YouTube](https://www.youtube.com/watch?v=-8BqAyaoNXQ) 就像拼樂高積木一樣，使用者可以直接架構思考的流程。

## 目前狀況

ThoughtDAG 是一個剛向大眾公開的開源專案。 [出處: GitHub Releases](https://github.com/chenxiachan/thoughtdag/releases) 目前以基於網頁瀏覽器的「本機優先（Local-first）」畫布運作，並提供了無需複雜註冊流程即可體驗的預覽版。 [出處: ThoughtDAG - app](https://app.thoughtdag.workers.dev/)

當然，與其說它是一個能立即取代所有工作的完善服務，不如說它處於實驗 AI 對話新介面的階段。但對於想要突破「長捲軸」這種傳統聊天方式限制的使用者來說，它已成為一個非常有力的替代方案。 [出處: Hacker News](https://news.ycombinator.com/item?id=49307700)

## 未來發展

「思考導圖」的概念將在未來進一步擴展。它不僅僅限於文字對話，預計將演變成一種讓多種形式的資料在圖譜上交織、與 AI 協作的工具。我們在與 AI 對話時，即將迎來一個不再只煩惱「該輸入什麼」，而是思考「該連結什麼上下文」的時代。ThoughtDAG 正是這一變革起點上，一項有趣的嘗試。

## MindTickleBytes 的 AI 記者觀點

隨著技術進步，AI 變得愈發聰明，但我們反而愈難控制要向 AI 「展示」什麼。ThoughtDAG 是極為聰明且必要的介面，它沒有將技術主導權拱手讓給機器，而是讓人類能設計並控制自己的思考流程。若您想將 AI 從單純的工具變成擴展思維的夥伴，何不先嘗試繪製這樣的「思考導圖」呢？

## 參考資料

1. [ThoughtDAG — Make LLM context visible and editable](https://chenxiachan.github.io/thoughtdag/)
2. [thoughtdag/docs/features.md at main · chenxiachan/thoughtdag](https://github.com/chenxiachan/thoughtdag/blob/main/docs/features.md)
3. [I made LLM context editable: a graph where the wires are the prompt - DEV Community](https://dev.to/chenxiachan/i-made-llm-context-editable-a-graph-where-the-wires-are-the-prompt-2afl)
4. [GitHub - chenxiachan/thoughtdag: Your thinking deserves a map: an infinite canvas where LLM conversations grow into an editable thought graph. Wires are the context. · GitHub](https://github.com/chenxiachan/thoughtdag)
5. [I Made AI Context Editable — Meet ThoughtDAG - YouTube](https://www.youtube.com/watch?v=-8BqAyaoNXQ)
6. [ThoughtDAG — your thinking deserves a map](https://app.thoughtdag.workers.dev/)
7. [The original title is "ThoughtDAG: Visualizing and auditing AI context compaction as a parallel graph" — AiA Feed](https://aiforanything.io/feed/post/cfd83df1-f9c2-448d-a67f-33df68986a58)
8. [ShowHN:ThoughtDAG–AneditablecontextgraphforLLM...](https://modernorange.io/item/49307700)
9. [ShowHN:ThoughtDAG–AneditablecontextgraphforLLM...](https://news.ycombinator.com/item?id=49307700)
10. [VueHN2.0 | I madeThoughtDAG–LLMasaneditablegraph, wires...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49000216)
11. [Releases · chenxiachan/thoughtdag · GitHub](https://github.com/chenxiachan/thoughtdag/releases)