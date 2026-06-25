---
layout: post
title: "AI 竟能直接操控網站？「Persona.js」開啟代理人時代"
description: "這是一篇關於 Persona.js 和 WebMCP 技術的簡易指南，這些技術為能與網站對話並自主處理事務的 AI 代理人提供了 UI 支援。"
summary: "Persona.js 是一個開源函式庫，協助網站與 AI 代理人直接溝通；透過新標準 WebMCP，大幅提升了 AI 的工作效率與準確度。"
tags: [AI, 網頁開發, Persona.js, WebMCP, AI代理人]
image: 2026-06-26-Show-HN-Personajs-a-vanilla-JS-agent-UI-library-with-native-WebMCP-MIT.jpg
image_alt: "一幅簡潔的插圖，象徵著 AI 代理人在螢幕上點擊網站按鈕並輸入數據的場景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "與其費力解析複雜的瀏覽器畫面，不如讓網站直接將自己的工具告知 AI，這是 AI 代理人時代的必然進化。Persona.js 將成為開發者引入這種未來的絕佳橋樑。"
quiz:
  - question: "Persona.js 的最大特色為何？"
    choices: ["它是 React 專用的函式庫", "它是以純 JavaScript 編寫的 WebMCP 原生 UI 框架", "它是付費服務專用工具"]
    answer: 1
    explanation: "Persona.js 是以純 JavaScript (Vanilla JS) 編寫，是一款具備 WebMCP 支援功能的開源框架，專為 AI 代理人設計。"
  - question: "相比傳統螢幕截圖方式，WebMCP 技術有何優勢？"
    choices: ["能美化網站設計", "能減少 AI 理解所需的 Token 成本並提高準確度", "能提升網路速度"]
    answer: 1
    explanation: "WebMCP 直接進行數據傳輸，而非對整個畫面進行截圖分析，因此能大幅降低 AI 的 Token 使用量，並將準確度提升至約 98%。"
  - question: "WebMCP 是由誰主導開發的標準？"
    choices: ["Google 與 Microsoft", "OpenAI 與 Meta", "Apple 與 Samsung"]
    answer: 0
    explanation: "WebMCP 是由 Google 與 Microsoft 主導開發的瀏覽器原生代理人協議。"
lang: zh-tw
ref: 2026-06-26-Show-HN-Personajs-a-vanilla-JS-agent-UI-library-with-native-WebMCP-MIT
---

想像一下：早晨醒來，你對手機或電腦上的 AI 助理說：「幫我把今天下午三點的會議資料上傳到網站，並發信通知相關人員。」以前的 AI 就像人眼看螢幕一樣，必須透過「螢幕截圖」來分析網站，過程緩慢且笨拙。但現在，一個 AI 能直接理解網站「內部構造」並將其作為工具來運用的新時代已經來臨。

近期在開發者間引起關注的 **Persona.js** 與 **WebMCP**，正是這場變革的核心。

### 為什麼這項技術如此重要？

過去，為了代勞處理瑣事而存在的「AI 代理人」在操作網站時，必須經過非常低效的過程。因為 AI 必須將網站畫面逐一截圖，分析按鈕在哪裡、輸入框在哪裡。這對人類而言，就像蒙著眼睛、摸索著鍵盤打字一樣。

Persona.js 與 WebMCP 技術讓 AI 不再只是「看著」螢幕，而是能直接讀取網站的「藍圖」並進行精確操作。這意味著 AI 助理不再只是單純的聊天工具，而是能真正成為代你處理業務的「實務工作者」。 [Persona：純 JavaScript 編寫的開源代理人 UI 函式庫](https://www.persona-chat.dev/)

### 簡而言之：AI 的「標準出入口」

將 **WebMCP** 比喻為網站安裝的「AI 專用出入口」再貼切不過了。 [WebMCP 解讀：Google 與 Microsoft 的瀏覽器原生代理人協議](https://particula.tech/blog/webmcp-explained-browser-agent-protocol) 過去，AI 若想進入網站，往往無法通過正門，只能破窗而入（螢幕截圖方式）或是翻牆。但導入 WebMCP 的網站，當 AI 代理人提出「我想按這個按鈕」、「我想在這裡輸入文字」的需求時，網站會主動開啟出入口，禮貌地讓其執行功能。 [WebMCP：將網頁轉化為 AI 代理人的工具](https://nearform.com/digital-community/webmcp-turning-web-pages-into-tools-for-ai-agents/)

而 **Persona.js** 可以視為安裝這扇門的「室內裝修套件」。 [Persona：純 JavaScript 編寫的開源代理人 UI 函式庫](https://www.persona-chat.dev/) 開發者只需在網站上安裝這個套件，就能輕易擁有輔助 AI 代理人理解網站的 UI 與工具。特別是 Persona.js 是該領域中首個預設支援 WebMCP 的函式庫。 [支援 WebMCP 的 Persona AI 代理人 UI 框架 | LinkedIn](https://www.linkedin.com/posts/nathan-booker_persona-open-source-ai-ui-library-in-vanillajs-activity-7470559829275779072-BQvC)

### 我們現在的進度：效率如何？

導入 WebMCP 的成效有數據為證。傳統基於截圖的方式，每次分析畫面都會消耗超過 2,000 個「Token」（AI 處理語言的單位）。使用 WebMCP 則僅需 20 到 100 個 Token，且 AI 的處理準確度大幅提升至約 98%。 [WebMCP：Google 的新網頁代理人協議如何改變 AI...](https://niteagent.com/blog/2026-05-22-webmcp-google-web-agent-protocol/)

目前的網頁生態系正迅速擁抱由 Google 與 Microsoft 主導的 WebMCP 標準。開發者們開始在網站中加入如 `window.AICommands` 等標準 JavaScript 指令，為 AI 直接控制網頁做好技術準備。 [WebMCP：Google 的新網頁代理人協議如何改變 AI...](https://niteagent.com/blog/2026-05-22-webmcp-google-web-agent-protocol/) [代理人網頁 AI | Chrome AI | Chrome 開發者](https://developer.chrome.com/docs/ai/agents?hl=de)

### 未來展望：網站將如何改變？

在不久的將來，你所使用的幾乎每個網站都會擁有一個為 AI 代理人準備的「專屬對話視窗」。使用者無須再費力尋找複雜的選單，只需開口告知 AI 即可。代理人將透過以 Persona.js 等函式庫構建的 UI，代你順利完成網站上的各項操作。

此外，開發者無須再為了實現這些功能而費力打造龐大且複雜的機器人。只要熟悉標準 JavaScript，任何人都能將自己的網站轉變為「AI 代理人能高效工作的辦公室」，這樣的時代即將到來。 [如何使用 WebMCP 讓你的網站做好代理人準備](https://www.ivanturkovic.com/2026/02/23/webmcp-tutorial-make-website-agent-ready/)

## 參考資料

1. [Persona: Open-source Agent UI Library in VanillaJS](https://www.persona-chat.dev/)
2. [GitHub - runtypelabs/persona](https://github.com/runtypelabs/persona)
3. [AI-native Web Interfaces With WebMCP](https://darekdari.com/ai-native-web-interfaces-with-webmcp-2025/)
4. [How to Make Your Website Agent-Ready With WebMCP](https://www.ivanturkovic.com/2026/02/23/webmcp-tutorial-make-website-agent-ready/)
5. [GitHub - hmsk/persona-js](https://github.com/hmsk/persona-js)
6. [WebMCP Explained: Google and Microsoft's Browser-Native Agent Protocol](https://particula.tech/blog/webmcp-explained-browser-agent-protocol)
7. [GitHub - jack-e-hobbs/webmcp-native-skill](https://github.com/jack-e-hobbs/webmcp-native-skill)
8. [Google’s WebMCP: Making the Web “AI-Agent-Ready”](https://javascript.plainenglish.io/googles-webmcp-making-the-web-ai-agent-ready-8ca4e60850d6)
9. [Persona AI Agent UI Framework with WebMCP Support | LinkedIn](https://www.linkedin.com/posts/nathan-booker_persona-open-source-ai-ui-library-in-vanillajs-activity-7470559829275779072-BQvC)
10. [21st: Infrastructure and UI building blocks for the agentic internet](https://21st.dev/mcp)
11. [WebMCP: Google's New Web Agent Protocol Changes How AI...](https://niteagent.com/blog/2026-05-22-webmcp-google-web-agent-protocol/)
12. [Agentische Web-KI | AI on Chrome | Chrome for Developers](https://developer.chrome.com/docs/ai/agents?hl=de)
13. [JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
14. [WebMCP: Turning webpages into tools for AI agents](https://nearform.com/digital-community/webmcp-turning-web-pages-into-tools-for-ai-agents/)
15. [webmcp-bridge: A stable local bridge that... | AgentIndex - Top AI Tools](https://agentindex.app/tool/holon-run-webmcp-bridge/)
16. [auto-webmcp v0.3.0: React support, richer schemas... - DEV Community](https://dev.to/prasannagyde/auto-webmcp-v030-react-support-richer-schemas-and-webmcp-spec-compliance-2eo9)
17. [WebMCP: So machen Sie Ihre Website AI-Agent-Ready (Praxis-Guide...)](https://studiomeyer.io/de/blog/webmcp-website-ai-agent-ready)