---
layout: post
title: "我說，它就畫？與 AI 實時協作的『代理繪圖 (Agent Draw)』"
description: "探討 AI 如何透過語音指令，在無限畫布上實時為您繪圖的『代理繪圖』工具及其運作原理。"
summary: "代理繪圖 (Agent Draw) 是一款交互式工具，能讓 AI 代理理解用戶的語音指令，並在無限畫布上實時繪製圖形與佈置元件。"
tags: [AI, 代理, tldraw, 創意, 工具]
image: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw.jpg
image_alt: "代理繪圖的介面畫面，AI 正在無限畫布上實時繪圖。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這不僅僅是簡單的圖像生成，更是 AI 邁向在畫布空間中與用戶進行物理交互的第一步。"
quiz:
  - question: "代理繪圖 (Agent Draw) 是基於什麼技術構建的？"
    choices: ["Figma", "TLDraw SDK", "Adobe Photoshop"]
    answer: 1
    explanation: "代理繪圖是基於 tldraw（一個基於 React 的無限畫布 SDK）構建的。"
  - question: "用戶如何向代理傳達指令？"
    choices: ["專用鍵盤輸入", "透過右側聊天面板進行語音及文字對話", "上傳圖片檔案"]
    answer: 1
    explanation: "用戶可以透過螢幕右側的聊天面板，以語音或文字與代理對話並添加背景資訊。"
  - question: "代理繪圖如何處理多個請求？"
    choices: ["以隨機順序處理", "使用 FIFO（先進先出）佇列與狀態機處理", "同時並行處理所有請求"]
    answer: 1
    explanation: "當有多個請求進入時，系統會利用 FIFO（先進先出）佇列與狀態機，一次處理一個會話。"
lang: zh-tw
ref: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw
---

想像一下，您在白紙前說：「在這裡畫個美味的披薩」，AI 隨即在眼前動筆，流暢地畫出線條，並細心地填上起司與臘腸。這種宛如魔法的情境即將成為日常生活的一部分。最近發布的「代理繪圖 (Agent Draw)」正在徹底改變我們與 AI 的協作方式。

### 為何這項工具備受矚目？

過去我們要求 AI 繪圖時，通常是輸入指令後靜候片刻，接著單方面「接收」成品。換句話說，AI 過去大多扮演單向產出內容的角色。但「代理繪圖」截然不同。它展現了與用戶在畫布上不斷溝通、實時共同創作的「協作」過程 [출처 2](https://www.youtube.com/watch?v=iIH2hJAxxm8)。

這意味著創意工作不再只是獨角戲。就像在會議室白板前與同事交流創意並逐步完成圖稿一樣，人類與 AI 現在能在同一個空間中交換意見並共同作業。AI 已經超越了單純產生結果的「工具」，轉變為能與您並肩站在畫布前的積極「夥伴」 [출처 13](https://gitnation.com/contents/agents-on-the-canvas-with-tldraw)。

### 它是如何運作的？

代理繪圖的運作原理相當精妙。若將其比喻，就像畫布上存在著一位「聰明的 AI 機器手臂」，即便我們不動手，它也能成為我們雙手的延伸，代為繪製圖稿。

1. **無限畫布 (tldraw SDK)**：這是基礎畫布環境。它採用了基於 React 的無限畫布 SDK「tldraw」，為 AI 創造了一個可以自由佈置圖形與繪圖的空間 [출처 1, 출처 15](https://tldraw.dev/blog/tldraw-mcp-app)。
2. **代理入門套件 (基本訓練課程)**：這是教授 AI 如何繪圖與操作元件的「基本功」。透過此套件，AI 不僅能處理簡單影像，還能讀取並排列矩形、菱形、箭頭等基本圖形，進而精密操縱畫布上的元素 [출처 6, 출처 12](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx)。
3. **交通管制系統 (狀態機)**：即使用戶同時發出多個指令，系統也不會紊亂。透過「先進先出 (FIFO)」佇列與狀態機，系統能管理 AI 專注於一次處理一個工作會話，順序執行任務 [출처 8](https://techstackups.com/articles/tldraw-agent-draw/)。

透過這些過程，AI 能在用戶指定的畫布區域內解析語音指令的含義，並實時繪製圖形，立即反映用戶的意圖 [출처 2, 출처 3](https://www.youtube.com/watch?v=livloOnVpC8)。

### 目前進展如何？

目前代理繪圖是基於開發者官方的「代理入門套件」構建的 [출처 2, 출처 5](https://memedata.com/post/130752)。用戶透過螢幕右側的聊天面板與代理交談。您可以在此補充必要的背景資訊，或確認代理過往的操作紀錄，進行溝通 [출처 6, 출처 11](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en)。

AI 對於基本圖形的組合與結構配置相當熟練。它不僅限於繪圖，還能編寫待辦事項列表，或在收到修改請求時立即進行更新，提供多方位的業務協助 [출처 12](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx)。當然，與其說是藝術創作，它目前更偏向於系統化的圖表生成或實時視覺輔助工具的角色 [출처 9, 출처 11](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en)。

### 未來我們將如何工作？

代理繪圖的問世，預告了不久的將來我們與 AI 的協作模式。未來，AI 代理將能在畫布上進行更深層的推論，洞察用戶的細微意圖，甚至自動修正圖稿或提出創意提案。

我們即將擁有「真正的視覺夥伴」，它不僅是製作靜態影像的工具，更能與我們在畫布這一物理空間中共同思考、共同創作。螢幕上的畫布將不再只是單純的繪圖板，而是一個讓人與 AI 實時同步思維、激盪創意的全新協作場域。

---

### MindTickleBytes AI 記者觀點
市面上能繪圖的 AI 已不勝枚舉，但能理解畫布這類「空間」，並與用戶互動、逐步堆疊產出成果的 AI 卻寥寥可數。AI 與我們的思維共同呼吸、共同完成事物的過程本身，正在重新定義創意的本質。

## 參考資料

1. [Show HN: Agent Draw: An agent draws while you talk, built on TLDraw](https://news.ycombinator.com/item?id=48805475)
2. [Agent Draw — Speak, and an AI Agent Draws It Live on Canvas](https://www.youtube.com/watch?v=iIH2hJAxxm8)
3. [Agent Draw: drag a box, speak, an AI agent draws inside it](https://www.youtube.com/watch?v=livloOnVpC8)
4. [Agent Draw: An agent draws while you talk, built on TLDraw](https://vuink.com/post/grpufgnpxhcf-d-dpbz/articles/tldraw-agent-draw)
5. [Show HN：Agent Draw，基于 TLDraw 构建，在你说话时自动绘图。](https://memedata.com/post/130752)
6. [GitHub - tldraw/agent-template: Enable AI agents to interpret ...](https://github.com/tldraw/agent-template)
7. [Better HN - bhn.vercel.app](https://bhn.vercel.app/show)
8. [Agent Draw: An agent draws while you talk, built on TLDraw | Tech Stackups](https://techstackups.com/articles/tldraw-agent-draw/)
9. [Agent starter kit • tldraw Docs](https://tldraw.dev/starter-kits/agent)
10. [Starter kits • tldraw Docs](https://tldraw.dev/starter-kits)
11. [tldraw × AI Agent: Exploring the Mechanics with the Agent Starter Kit](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en)
12. [tldraw/apps/docs/content/starter-kits/agent.mdx at main · tldraw/tldraw](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx)
13. [Agents on the Canvas With tldraw by Max Drake](https://gitnation.com/contents/agents-on-the-canvas-with-tldraw)
14. [Build a Real-Time tldraw Whiteboard with Velt Comments inside ChatGPT🤯🔥 - DEV Community](https://dev.to/astrodevil/build-a-real-time-tldraw-whiteboard-with-velt-comments-inside-chatgpt-1dhe)
15. [tldraw MCP App: Letting your agents draw](https://tldraw.dev/blog/tldraw-mcp-app)
16. [Show | Hacker News - nhn.yuu.is](https://nhn.yuu.is/show)