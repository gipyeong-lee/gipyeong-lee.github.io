---
layout: post
title: "AI 程式編寫助手，現在可以換成「中國產模型」了嗎？Kimi K3 與 Claude Code 的相遇"
description: "我們將探討如何連接最近發布的強大 AI 模型「Kimi K3」與熱門的程式編寫代理「Claude Code」，並了解其實際性能表現。"
summary: "探討如何將擁有 2.8 兆參數的強大 AI 模型「Kimi K3」應用於 Claude Code 環境，並檢視其效率與優勢。"
tags: [AI, 程式編寫, KimiK3, ClaudeCode, 技術評論]
image: 2026-08-17-Testing-Moonshot-AIs-Kimi-K3-Inside-Claude-Code.jpg
image_alt: "想像在程式編寫代理界面上，Kimi K3 模型正在連接並生成複雜網頁代碼的圖片。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Kimi K3 的出現顯示開放權重模型在性能與成本方面已足以威脅專有模型。現在開發者可以自由選擇代理的「大腦」，這將使開發效率達到極致。"
quiz:
  - question: "Kimi K3 模型被介紹為其最大特徵之一的規模約為多少？"
    choices: ["1000 億參數", "2.8 兆參數", "5 兆參數"]
    answer: 1
    explanation: "Kimi K3 是一款擁有 2.8 兆參數的大型模型。"
  - question: "在 Claude Code 等環境中使用 Kimi K3，最關鍵的操作是什麼？"
    choices: ["重新安裝 Claude Code", "設定模型的基礎 URL 與 API 金鑰", "更換電腦硬體"]
    answer: 1
    explanation: "只需將 Claude Code 的 Anthropic 基礎 URL 修改為 Moonshot 的兼容端點並設定 API 金鑰，即可完成連接。"
  - question: "在人工智慧評估機構「Artificial Analysis」的智力指數評估中，Kimi K3 獲得了多少分？"
    choices: ["50 分", "56 分", "57 分"]
    answer: 2
    explanation: "在 Artificial Analysis 的評估中，Kimi K3 獲得了 57 分，超越了 Claude Opus 4.8 的 56 分。"
lang: zh-tw
ref: 2026-08-17-Testing-Moonshot-AIs-Kimi-K3-Inside-Claude-Code
---

想像一下，如果您常用的「AI 程式編寫助手」在性能提升的同時，成本還降到了原來的三分之一，那會是什麼樣的體驗？最近，開發者社群中出現了一個熱門話題，那就是中國 Moonshot AI（月之暗面）所發布的「Kimi K3」。

這款模型不僅被評價為極其聰明，更與那些幾乎壟斷 AI 市場的全球企業旗艦模型並駕齊驅，甚至在某些性能指標上有所超越，因此備受矚目。今天，我們將介紹如何將這個強大的「2.8 兆參數巨獸」Kimi K3 連接到我們熟悉的程式編寫代理「Claude Code」中使用。

## 為什麼這很重要？

過去的 AI 模型就像一扇「關閉的門」。特定公司開發的模型只能在該公司提供的服務中使用。但 Kimi K3 是作為「開放權重（Open-Weight，指任何人都可以查看並運用模型內部設定的狀態）」模型發布的。這意味著用戶可以根據自己的工作流程，自由替換 AI 的「大腦」。

特別是程式編寫是一項高成本的工作。因為完成一個專案需要進行無數次的 AI 呼叫。使用 Kimi K3，既能達到與 Claude 類似的性能，成本卻僅約為 35%，這使其在經濟上具有極大的吸引力。[出處: Moonshot AI's Kimi-K3 tops Frontend Code Arena · Digg](https://digg.com/tech/hm2wuequ)

## 簡單理解：AI 的「大腦」與「司機」

我們可以將程式編寫代理比作汽車嗎？「Claude Code」就是配備了方向盤、踏板和導航系統的「汽車本身」。而我們使用的 AI 模型（Claude 或 Kimi K3）則是驅動該車輛的「引擎」和「司機」。

許多人擔心：「要使用 Kimi K3，是不是得重新編寫程式？」其實並不然。即使引擎（Kimi K3）換了，方向盤（Claude Code）依然可以使用。我們只需輕輕更換引擎，就能體驗到更快、更便宜的駕駛過程。[出處: Kimi K3 vs Claude Code vs Codex 2026 · senn-tech](https://senn-tech.com/en/blog/kimi-k3-vs-claude-code-codex)

## 現狀：『3T 級』巨型模型的登場

2026 年 7 月 16 日，Moonshot AI 推出了擁有 2.8 兆參數（Parameter，指 AI 通過學習調整的數值）的 Kimi K3。[出處: I Ran Kimi K3 Against Claude for a Week · Medium](https://medium.com/@inprogrammer/i-ran-kimi-k3-against-claude-for-a-week-here-is-what-actually-happened-20c1a17c9206) 這在業界屬於所謂的「3T（兆）級」模型。

性能也不容忽視。獨立 AI 評估機構「Artificial Analysis」的智力指數（Intelligence Index）測量結果顯示，Kimi K3 以 57 分的成績超越了當時領先的 Claude Opus 4.8（56 分）。[出處: Kimi K3 Beats Opus 4.8 in Blind Coding Test · Adwait | LinkedIn](https://www.linkedin.com/posts/adwait-gawade_moonshot-ai-releases-kimi-k3-a-28-trillion-parameter-activity-7485215773880139776-6lEv)

目前 Kimi K3 具有以下特徵：
* **海量上下文**：一次可以記憶 100 萬個 Token（Token，AI 理解的文本片段單位）。[出處: Kimi K3: Moonshot AI's 2.8T Open-Weight Model](https://www.eigent.ai/blog/kimi-k3-open-weight-frontier-model)
* **API 性價比**：提供 3 美元與 15 美元級別的合理定價政策。[出處: Kimi K3: Moonshot AI's 2.8T Open-Weight Model](https://www.eigent.ai/blog/kimi-k3-open-weight-frontier-model)
* **連接簡便**：只需稍作修改 Claude Code 設定，即可立即替換。[出處: How to Run Kimi K3 in Claude Code: 3 Routes, Real Costs, and...](https://shaam.blog/articles/how-to-run-kimi-k3-in-claude-code-2026)

## 在 Claude Code 中使用 Kimi K3

方法意外地簡單。利用 Claude Code 與 Anthropic API 通訊的方式，將其指向 Moonshot AI 提供的相容端點即可。[出處: Kimi K3 with Claude Code: Setup, Env Vars and Real Limits (2026)](https://www.codeagentswarm.com/en/guides/kimi-k3-with-claude-code)

1. **設定端點**：將 Claude Code 的 Anthropic Base URL 設定變更為 Moonshot AI 提供的相容端點位址。[出處: Kimi vs Claude Code: Coding Agent Comparison 2026](https://www.layer3labs.io/comparisons/kimi-k3-vs-claude-code)
2. **更換 API 金鑰**：輸入 Moonshot AI 的 API 金鑰，取代原有的 Anthropic API 金鑰。[出處: Kimi vs Claude Code: Coding Agent Comparison 2026](https://www.layer3labs.io/comparisons/kimi-k3-vs-claude-code)
3. **確認**：無需複雜的編譯過程或軟體安裝，啟動 Claude Code 後，Kimi K3 就會立即開始處理程式編寫任務。[出處: How to Run Kimi K3 in Claude Code: 3 Routes, Real Costs, and...](https://shaam.blog/articles/how-to-run-kimi-k3-in-claude-code-2026)

## 未來展望

Kimi K3 的出現，展現了 AI 市場中「基準測試分數」的變化速度有多快。技術發展速度極快，甚至在發布後的短短 9 天內，基準測試排名就多次洗牌。[出處: Kimi K3 vs Claude for Coding 2026: Benchmarks Compared](https://aiforesight360.com/kimi-k3-vs-claude-coding/)

未來我們在選擇 AI 模型時，將不再糾結於「這是誰的服務」，而是思考「哪種引擎對我的專案更有效率」。目前它已在程式編寫與網頁開發環境中證明了性能，隨著技術進一步成熟，我們即將迎來一個在文件撰寫或企劃工作中，能選用自己「最愛 AI 引擎」的時代。

## MindTickleBytes AI 記者的視角
技術競爭最終將帶給身為使用者的我們更聰明、更便宜的工具。像 Kimi K3 這樣的模型出現，很好地證明了特定企業無法壟斷 AI 技術。未來，開發者為了取得最佳成果，將會像運動員挑選適合的鞋子一樣，依需求選擇不同的模型。

---

## 參考資料

1. [Testing Moonshot AI's Kimi K3 Inside Claude Code](https://philippdubach.com/posts/kimi-k3-inside-claude-code/)
2. [How to Run Kimi K3 in Claude Code: 3 Routes, Real Costs, and...](https://shaam.blog/articles/how-to-run-kimi-k3-in-claude-code-2026)
3. [Testing Moonshot AI's Kimi K3 Inside Claude Code | Hacker News](https://news.ycombinator.com/item?id=49319610)
4. [Moonshot AI's Kimi-K3 tops Frontend Code Arena · Digg](https://digg.com/tech/hm2wuequ)
5. [China's Kimi K3 Calls Itself Claude, Exposing Illegal Distillation](https://propakistani.pk/2026/07/18/chinas-kimi-k3-calls-itself-claude-exposing-illegal-distillation/)
6. [Kimi K3 Beats Opus 4.8 in Blind Coding Test | Adwait... | LinkedIn](https://www.linkedin.com/posts/adwait-gawade_moonshot-ai-releases-kimi-k3-a-28-trillion-parameter-activity-7485215773880139776-6lEv)
7. [moonshotai/Kimi-K3 · Hugging Face](https://huggingface.co/moonshotai/Kimi-K3)
8. [I Ran Kimi K3 Against Claude for a Week. Here Is ... - Medium](https://medium.com/@inprogrammer/i-ran-kimi-k3-against-claude-for-a-week-here-is-what-actually-happened-20c1a17c9206)
9. [Kimi K3 vs Claude Code vs Codex 2026 · senn-tech](https://senn-tech.com/en/blog/kimi-k3-vs-claude-code-codex)
10. [Kimi K3 just went toe-to-toe with Claude, and it's cheaper ...](https://www.howdoiuseai.com/blog/2026-07-18-kimi-k3-just-went-toe-to-toe-with-claude-and-it-s-)
11. [Kimi K3 vs Claude for Coding 2026: Benchmarks Compared](https://aiforesight360.com/kimi-k3-vs-claude-coding/)
12. [Kimi K3 with Claude Code: Setup, Env Vars and Real Limits (2026)](https://www.codeagentswarm.com/en/guides/kimi-k3-with-claude-code)
13. [Kimi vs Claude Code: Coding Agent Comparison 2026](https://www.layer3labs.io/comparisons/kimi-k3-vs-claude-code)
14. [Moonshot AI's Kimi K3 Claims Parity With OpenAI in China's Latest...](https://www.techbuzz.ai/articles/moonshot-ai-s-kimi-k3-claims-parity-with-openai-in-china-s-latest-salvo)
15. [Kimi K3: Moonshot AI's 2.8T Open-Weight Model](https://www.eigent.ai/blog/kimi-k3-open-weight-frontier-model)
16. [China Moonshot AI Kimi K3 claims rival OpenAI and Anthropic](https://beyondtmrw.org/article/china-moonshot-ai-kimi-k3-claims-rival-openai-and-anthropic)
17. [Kimi K3 Surpasses Claude in Frontend Coding Benchmarks | LinkedIn](https://www.linkedin.com/posts/muruganvenugopal_kimi-k3-moonshot-ai-is-performing-very-activity-7484041216322326528-8_CN)