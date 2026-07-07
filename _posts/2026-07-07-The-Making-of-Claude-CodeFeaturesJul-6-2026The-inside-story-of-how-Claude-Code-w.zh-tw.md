---
layout: post
title: "居住在我的終端機裡的 AI 同伴：「Claude Code」是如何誕生的？"
description: "這是一篇關於 Claude Code 的誕生秘辛與特點的簡易說明，這是一款能直接在開發者終端機中協助編碼的代理人工具。"
summary: "介紹 Anthropic 的 AI 編碼代理人「Claude Code」的開發過程與核心功能，它能直接在終端機執行並加速編碼作業。"
tags: [AI, 開發工具, Claude Code, Anthropic]
image: 2026-07-07-The-Making-of-Claude-CodeFeaturesJul-6-2026The-inside-story-of-how-Claude-Code-w.jpg
image_alt: "浮現在終端機畫面上的 Claude Code 標誌與流動的程式碼"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 直接進入開發者最投入的工作空間「終端機」，不僅僅是單純的便利，更是一個重要的轉折點，顯示出 AI 的協作方式已從「對話」演進為「執行」。"
quiz:
  - question: "Claude Code 與現有的聊天型 AI 工具相比，最大的特點是什麼？"
    choices: ["只能在網頁瀏覽器中執行", "直接在終端機執行，並能修改檔案與執行指令", "必須將程式碼上傳到遠端伺服器"]
    answer: 1
    explanation: "Claude Code 直接在開發者的本地終端機中執行，即便沒有後端伺服器，AI 也能修改開發者的檔案並執行指令。"
  - question: "Claude Code 為了維持安全性會採取什麼行動？"
    choices: ["自動修改所有檔案", "在變更前向使用者請求權限", "切斷網際網路連線"]
    answer: 1
    explanation: "為了安全使用，Claude Code 在修改檔案或執行指令之前，一定會向使用者請求明確的授權。"
  - question: "2026 年 5 月，Anthropic 發表的 Claude Code 相關主要變更事項是什麼？"
    choices: ["使用費用調漲 2 倍", "使用量限制（Rate Limit）調高 2 倍", "終止服務"]
    answer: 1
    explanation: "Anthropic 於 2026 年 5 月 6 日將 Pro、Max、Team 及 Enterprise 方案的 Claude Code 使用量限制提高至原來的 2 倍。"
lang: zh-tw
ref: 2026-07-07-The-Making-of-Claude-code
---

試著想像一下。當你在編寫複雜的程式碼遇到卡關時，不需要另外開啟網頁瀏覽器去詢問聊天機器人。只需在黑底白字的「終端機（Terminal，一種用文字對電腦下指令的介面）」輸入「幫我修正這個錯誤」，畫面中的游標就會自動移動、修改程式碼並修復錯誤。就像一位坐在你旁邊的資深同事一樣。

將這種場景變為現實的主角，正是 Anthropic 的「Claude Code」。它不再僅止於透過聊天提供回答，而是開始讓 AI 直接進入開發者的作業環境並執行工作。究竟這個「會寫程式的 AI」是如何來到我們身邊的呢？

## 為什麼這很重要？ (Why It Matters)

我們平常使用的 AI 聊天機器人通常是「顧問」。如果問它們「請幫我寫出這樣的程式碼」，它們確實會寫出程式碼，但接下來把程式碼抓下來、根據自己的程式進行修改並執行的過程，全部都是開發者自己的事。

然而，Claude Code 省略了這些步驟。Claude Code 是一款基於「代理人（Agent，指能自行設定目標、規劃並執行任務的 AI）」的工具，它能協助開發者在將想法轉化為程式碼時，以更快的速度運作 [參考資料: Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)。簡單來說，這意味著開發者從原本必須重複進行的枯燥修正工作中解脫，能夠更專注於具備創意與重要性的設計工作。

## 簡單易懂的解釋 (The Explainer)

將 Claude Code 的運作方式做個比喻，就像雇用了一位非常能幹的「魔法助理」。

1. **住在我的終端機裡**：不需要另外造訪網站。只要在開發者平常編碼的「終端機」安裝 Claude Code，就能立即將其作為專屬助理使用 [參考資料: Claude Code by Anthropic](https://claude.com/product/claude-code)。
2. **親自動手處理程式碼**：如果說以前的 AI 是「詳細說明料理食譜」的程度，Claude Code 就像是直接走進你的廚房（終端機環境）幫你切菜、翻炒。因為是透過模型 API（連接 AI 與程式的通道）直接溝通，所以不需要經過複雜的獨立遠端伺服器 [參考資料: Claude Code by Anthropic](https://claude.com/product/claude-code)。
3. **絕不擅作主張**：這裡最重要的是「權限」。助理的能力再好，如果未經我的許可就打開冰箱或開啟瓦斯爐，也會讓人感到害怕，對吧？Claude Code 在修改檔案或執行新指令之前，一定會先將變更內容呈現給使用者，並要求明確的授權 [參考資料: Claude Code by Anthropic](https://claude.com/product/claude-code)。

簡單來說，Claude Code 可以理解為將 AI 龐大的「大腦」與開發者的「雙手」直接連結起來的工具。

## 目前狀況 (Where We Stand)

Claude Code 正在迅速成為許多開發者不可或缺的必備工具。Anthropic 正在持續改善此工具的效能，特別是在 2026 年 5 月 6 日，針對 Pro、Max、Team 及 Enterprise 方案使用者，將使用量限制（Rate Limit，指在一定時間內可使用的次數）永久調高為原本的 2 倍，進而提升了使用者體驗 [參考資料: Claude Usage Limits 2026](https://explainx.ai/blog/claude-usage-limits-2026-timeline-explained)。

當然，也有需要注意的地方。新技術出現時，總會伴隨著惡意濫用的企圖。近期曾發生過有人試圖製作並散布偽造的 Claude Code 套件的事件，Anthropic 為保護開發者，採取了積極的資安措施，例如預先註冊相關的 npm 套件（JavaScript 程式碼散布單位）名稱來進行應對 [參考資料: Claude Code Source Leaked](https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html)。

## 未來發展 (What's Next)

未來的 AI 工具將會朝向更具智慧的「代理人」方向演進。不僅僅是寫出程式碼，未來的 AI 將能完美理解整個專案的結構，當發生錯誤時自行分析並提出根本性的解決方案，進而甚至能撰寫測試程式碼並自動通過驗證。像 Claude Code 這樣的代理人型工具，今後將不再是新奇的付費功能，而是會成為開發者日常工作中基礎且不可或缺的「預設值」[參考資料: AI Weekly Signals](https://daehnhardt.com/blog/2026/07/03/sonnet-5-tokenizer-tax-ai-weekly-signals/)。

## MindTickleBytes AI 記者的觀點

AI 直接進入開發者最投入的工作空間「終端機」，不僅僅是單純的便利，更是一個重要的轉折點，顯示出 AI 的協作方式已從「對話」演進為「執行」。在 AI 超越顧問、成為真正「同事」的時代，我們將不再僅僅糾結於「要做什麼」的問題，而是必須更專注於「與 AI 同事一起創造什麼更大的價值」。

## 參考資料

1. [Claude(AI) - Wikipedia](https://en.wikipedia.org/wiki/Claude_(language_model))
2. [Claude Code overview - Anthropic](https://docs.anthropic.com/en/docs/claude-code/overview)
3. [Claude Code by Anthropic | AI Coding Agent, Terminal, IDE](https://claude.com/product/claude-code)
4. [Mastering Claude Code in 30 minutes - YouTube](https://www.youtube.com/watch?v=6eBSHbLKuN0)
5. [AI Weekly Signals: Tokenizer Tax, Cache Rules, and Who Owns...](https://daehnhardt.com/blog/2026/07/03/sonnet-5-tokenizer-tax-ai-weekly-signals/)
6. [The Making of Claude Code | OKKY 社群](https://okky.kr/articles/1560089)
7. [Claude AI Chat: Free Online Access and Best Models (2026)](https://c-ai.chat/)
8. [The Making of Claude Code \ Anthropic](https://www.anthropic.com/features/making-of-claude-code)
9. [Claude Code Source Leaked via npm Packaging Error, Anthropic...](https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html)
10. [Anthropic Quietly Took the Enterprise Lead. Then the... | Towards AI](https://pub.towardsai.net/anthropic-quietly-took-the-enterprise-lead-then-the-government-took-its-models-101334343dc2)
11. [Claude](https://claude.com/)
12. [Claude Usage Limits 2026: Every Change, Dated and... | explainx.ai](https://explainx.ai/blog/claude-usage-limits-2026-timeline-explained)
13. [Claude Code 101 | Anthropic Courses](https://anthropic.skilljar.com/claude-code-101)