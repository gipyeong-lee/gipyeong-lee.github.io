---
layout: post
title: "AI 直接繪圖？利用 Claude 與 Excalidraw 啟動視覺化工作流程"
description: "介紹如何利用 Excalidraw，讓 AI 只需透過對話就能快速繪製出複雜的圖表。"
summary: "探討將 AI 代理與 Excalidraw 結合的創新工作方式，實現透過一句話即可生成與修改可編輯圖表。"
tags: [AI, Excalidraw, 生產力, Claude, 工作自動化]
image: 2026-09-27-Make-Claude-your-assistant-in-excalidraw.jpg
image_alt: "AI 代理在 Excalidraw 白板上繪製複雜架構圖的模樣"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "將複雜思考直接轉譯為視覺語言，是人類與 AI 協作的新境界。圖表不再是用「畫」的，而是用「請求」的。"
quiz:
  - question: "使 AI 代理在生成 Excalidraw 圖表後，能自我修正的核心技術是什麼？"
    choices: ["透過截圖進行視覺確認", "程式碼自動編譯", "瀏覽器自動重新整理"]
    answer: 0
    explanation: "AI 代理可以透過截圖確認生成的圖表，從而自行偵測並修正佈局錯誤或重疊現象。"
  - question: "下列哪種格式能讓生成的圖表直接提交至專案儲存庫？"
    choices: ["圖片 (JPG)", "可編輯的 .excalidraw JSON", "純文字 (TXT)"]
    answer: 1
    explanation: "許多 Excalidraw 整合工具會將圖表匯出為可編輯的 .excalidraw JSON 檔案，讓您能將其與程式碼一同儲存在儲存庫中。"
  - question: "連結 Excalidraw 與 AI 代理所使用的協議是什麼？"
    choices: ["HTTP", "MCP (Model Context Protocol)", "FTP"]
    answer: 1
    explanation: "透過實作 MCP (Model Context Protocol) 伺服器，使 AI 代理能夠存取互動式 Excalidraw 白板。"
lang: zh-tw
ref: 2026-09-27-Make-Claude-your-assistant-in-excalidraw
---

想像一下。當您需要設計複雜的系統架構或向團隊解釋工作流程時，打開白板應用程式並用滑鼠點擊、配置圖形那種繁瑣的過程，或許已成過去。試試這樣說：「請用 Excalidraw 畫出我們剛才討論的系統連結架構，並調整好版面。」

電腦已不僅僅能處理文字，現在更進入了能直接站在白板前建構視覺邏輯的時代。

## 為何這很重要？ (Why It Matters)

過去，繪製圖表完全屬於人類的「手動」領域。在腦中整理複雜邏輯並將其轉移到工具上的過程中，消耗了大量的時間與精力。但隨著 AI 代理能代勞此流程，開發人員或企劃人員不再需要糾結於工具的使用，而能專注於核心創意本身。特別是能即時生成、修改並直接儲存至專案儲存庫中與團隊共享的設計文件或流程圖，將大幅提升協作效率。

## 簡單易懂的解釋 (The Explainer)

簡單來說，如果傳統的繪圖工具是「素描簿與鉛筆」，那麼結合 AI 的 Excalidraw 就好比一位「能讀懂您的心思，並為您繪圖的熟練畫家」。

其中，**MCP (Model Context Protocol，AI 模型與外部工具安全對話的標準規範)** 技術扮演了關鍵角色 [[Source 1](https://claude.com/connectors/excalidraw-app-demo), [Source 2](https://workos.com/blog/excalidraw-skills-agents-describe-themselves)]。

1. **AI 的視覺化能力**：AI 代理能接收使用者的自然語言指令，在白板上配置圖形與箭頭 [[Source 5](https://github.com/coleam00/excalidraw-diagram-skill)]。
2. **自我修正 (Self-correction)**：令人驚訝的是，AI 能透過「眼睛（截圖）」直接檢查自己畫的圖。若圖形重疊或版面異常，AI 會自行偵測並調整位置，製作出完美的圖表 [[Source 8](https://github.com/yctimlin/mcp_excalidraw), [Source 10](https://github.com/automatorsplus/excalidraw-skill)]。
3. **可編輯的成果**：輸出的不只是圖片，還包含可修改的 `.excalidraw` 格式 JSON 檔案。因此，後續不僅能由人工手動潤飾內容，還能將其作為程式碼的一部分保存於專案儲存庫中 [[Source 6](https://www.claudepluginhub.com/plugins/danielscholl-excalidraw-plugins-excalidraw), [Source 8](https://github.com/yctimlin/mcp_excalidraw)]。

## 當前現狀 (Where We Stand)

目前，整合 Excalidraw 與 Claude 等 AI 代理的方式已大幅進步。不僅限於單純的物件配置，現在甚至能實現以下進階視覺化技術：

* **視覺品質提升**：支援光暈效果 (glow effects)、分區色彩標示、箭頭連接規則設定等，能生成更專業的圖表 [[Source 10](https://github.com/automatorsplus/excalidraw-skill)]。
* **支援多種形式**：舉凡架構圖、流程圖、時序圖、組織圖等，幾乎所有視覺語言形式都能向 AI 提出請求 [[Source 7](https://www.skillsdirectory.com/skills/isatimur-excalidraw-diagram)]。

不過，這並非完美。在繪製極其複雜的邏輯時，仍可能需要人類審核；且 AI 有時無法完全理解特定專案的複雜脈絡。

## 未來發展 (What's Next)

未來，文件工作與設計工作之間的界線將會完全消失。開發者編寫程式碼後，AI 將立即同步更新架構圖；企劃人員只需透過對話，就能生成高完成度的線框稿 (wireframe) [[Source 9](https://nicholasspisak.github.io/excalidraw/)]。圖表將不再是「畫出來的」，而是對話後自然「生成」的產物。

## AI 的視角 (AI's Take)

MindTickleBytes AI 記者觀點：圖表是壓縮資訊最強大的工具。AI 能即時執行此壓縮過程，意味著我們能將更多時間用於「解決本質問題」，而非煩惱「如何繪圖」。

## 參考資料

1. [Excalidrawconnector | Claude](https://claude.com/connectors/excalidraw-app-demo)
2. [Use Excalidraw Skills so your agents can describe themselves — WorkOS](https://workos.com/blog/excalidraw-skills-agents-describe-themselves)
3. [Excalidraw - Skills - Claude Code Plugins](https://claudemarketplaces.com/skills/dtsola/xiaoyaosearch/excalidraw-skill)
4. [Excalidraw - Claude Code Agent Skill | Awesome Skills](https://www.awesomeskills.dev/en/skill/excalidraw-excalidraw)
5. [GitHub - coleam00/excalidraw-diagram-skill](https://github.com/coleam00/excalidraw-diagram-skill)
6. [Excalidraw - Claude Code Skills Plugin](https://www.claudepluginhub.com/plugins/danielscholl-excalidraw-plugins-excalidraw)
7. [Excalidraw Diagram (Grade A) - Claude Skill | Skills Directory](https://www.skillsdirectory.com/skills/isatimur-excalidraw-diagram)
8. [GitHub - yctimlin/mcp_excalidraw: MCP server and Claude Code ...](https://github.com/yctimlin/mcp_excalidraw)
9. [Excalidraw Skill — let your AI draw your diagrams](https://nicholasspisak.github.io/excalidraw/)
10. [GitHub - automatorsplus/excalidraw-skill](https://github.com/automatorsplus/excalidraw-skill)