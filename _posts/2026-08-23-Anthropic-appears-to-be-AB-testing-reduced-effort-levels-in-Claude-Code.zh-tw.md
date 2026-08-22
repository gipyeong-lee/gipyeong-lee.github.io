---
layout: post
title: "我的 AI 突然變笨了？Claude Code 的隱藏實驗故事"
description: "你有沒有感覺過 AI 模型的性能突然下降？透過 Anthropic 的 Claude Code 發生的「努力程度」調整及用戶的不適體驗，我們來審視 AI 透明度問題。"
summary: "為了節省成本並提升速度，Anthropic 曾悄悄降低 Claude Code 的預設推理強度，在用戶對於品質下降的抱怨聲浪中，最終將其恢復。"
tags: [AI, Anthropic, ClaudeCode, 人工智慧, 技術倫理]
image: 2026-08-23-Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code.jpg
image_alt: "Claude Code 介面畫面與表示推理過程的圖形元素"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企業在進行技術優化時，為了與用戶建立信任，必須透明地公開變更理由。實驗性功能永遠應以保障用戶的選擇權為優先。"
quiz:
  - question: "Anthropic 降低 Claude Code 預設推理水準的主要原因為何？"
    choices: ["加強模型安全性", "節省成本並提升回應速度", "為了學習更多資料"]
    answer: 1
    explanation: "Anthropic 反應了用戶關於 Token 消耗量過大的回饋，試圖改善回應速度並減少 Token 消耗。"
  - question: "在 Claude Code 中，「努力程度（effort level）」越高會發生什麼事？"
    choices: ["回應速度更快", "思考深度加深，更能解決複雜問題", "必然會產生更多費用"]
    answer: 1
    explanation: "努力程度與思考深度有關，能提升解決更複雜問題的能力。"
  - question: "Anthropic 最近是如何解決品質下降問題的？"
    choices: ["向用戶收取更高費用", "於 4 月 7 日恢復至先前水準", "完全更換了 AI 模型"]
    answer: 1
    explanation: "Anthropic 承認該措施是錯誤的妥協，並於 2026 年 4 月 7 日將設定恢復為原本較高的推理水準。"
lang: zh-tw
ref: 2026-08-23-Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code
---

想像一下，你有一位每天協助你工作的聰明 AI 助手。如果直到昨天都能輕鬆解決複雜編碼問題的助手，今天早上突然開始只給出太過簡單的回答，或是忽略了重要的脈絡，你會有多少驚慌？最近，人工智慧公司 Anthropic 的開發者編碼工具「Claude Code」的用戶之間，就發生了這樣的事情。

### 這為何重要？

這次事件對將 AI 作為專業工具使用的人們造成了巨大衝擊。這不僅僅是模型變慢的問題。因為 AI 的「大腦運轉」方式在用戶不知情的情況下被強制變更，導致工作生產力立即受到打擊。這顯示了我們每天使用的 AI 服務，可能會因為企業的內部政策，隨時在未預告的情況下發生性能變化，是一個重要的案例。

### 簡單理解：什麼是 AI 的「努力程度」？

Claude Code 有一項功能稱為 **「努力程度（Effort Level，決定 AI 為解決問題需要思考多深度的設定）」**。

簡單來說，這項努力程度與學生解試題時投入的努力類似。「低努力」水準就像粗略瀏覽題目並快速寫下答案，「高努力」水準則是仔細閱讀並檢視所有句子，進行深層思考。 [出處: Claude Code effort level and model selection](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)

比喻來說，就像一位資深廚師原本用心製作料理，卻突然為了節省材料費與時間，將料理方式改成了速食水準。以消費者的立場，當然會感覺到味道的差異。

Anthropic 在 2026 年 2 月至 3 月間，在沒有任何公告的情況下，將 Claude Code 的預設努力程度從「高」降至「中」。 [出處: Claude Code's Thinking Depth Dropped 73%](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/) 據 Anthropic 相關人士說明，這是為了反應用戶對於 Token（AI 使用的語言單位）消耗過大的回饋，旨在改善回應速度並降低成本。 [出處: Anthropic faces user backlash over reported performance issues](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/)

但結果卻相當慘烈。由於此調整導致 AI 的思考深度大幅降低了 73%，使得執行複雜編程作業的用戶，深刻感受到性能急劇下降。 [出處: Claude Code's Thinking Depth Dropped 73%](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/)

### 現況：接連的更新與混亂

據查，性能下降的原因是三次更新重疊所致。 [出處: Anthropic Claude Code Quality Drop](https://devtoolpicks.com/blog/anthropic-claude-code-quality-fix-postmortem-2026) 特別是在 3 月份針對部分用戶進行了 A/B 測試（隨機展示兩種以上方案以比較成果的實驗），此過程中發生了諸如限制代碼計畫為 40 行，或刪除必要脈絡資訊等問題，引發用戶不滿。 [出處: Anthropic A/B Tested Claude Code Plan Mode](https://agent-wars.com/news/2026-03-14-anthropic-ab-testing-claude-code-plan-mode-without-disclosure)

最終，Anthropic 承認其決定是「錯誤的妥協」，並於 4 月 7 日將設定恢復至先前水準。 [出處: Why Is Claude Code Slow?](https://www.aakashx.com/blog/claude-code-slow-causes-fixes/)

### 未來會如何？

這次事件對 AI 工具的透明度提出了強烈警告。專家主張，提供專業 AI 工具的企業在應用實驗性變更時，必須取得用戶同意，或至少進行預先公告。 [出處: Mike Ramos Criticizes Anthropic](https://agent-wars.com/news/2026-03-14-anthropic-silent-ab-test-claude-code) 未來，用戶將會更強烈要求能夠自行選擇並調整 AI 模型所提供的「努力程度」之環境。

## MindTickleBytes 的 AI 記者觀點

AI 的性能不僅是單純的數字，更與用戶的信任直接掛鉤。這次事件顯示了以技術優化為名所進行的「悄悄變更」會導致多大的生產力下降，這很好地展示了為何 AI 企業應將透明溝通列為最優先順序。隨著未來有更多用戶將 AI 作為工作的核心工具，這種政策上的透明度將會成為與技術實力同樣重要的企業競爭力。

## 參考資料

1. [Claude Code's Thinking Depth Dropped 73% — Anthropic Admits](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/)
2. [Anthropic appears to be A/B testing reduced effort levels in Claude Code](https://zeli.app/zh/story/49401549)
3. [Anthropic Claude Code Quality Drop: What Actually Happened](https://devtoolpicks.com/blog/anthropic-claude-code-quality-fix-postmortem-2026)
4. [Claude Code's Feb–Mar 2026 Updates Quietly Broke Complex Engineering](https://dev.to/shuicici/claude-codes-feb-mar-2026-updates-quietly-broke-complex-engineering-heres-the-technical-5b4h)
5. [Anthropic A/B Tested Claude Code Plan Mode Without Telling Users](https://agent-wars.com/news/2026-03-14-anthropic-ab-testing-claude-code-plan-mode-without-disclosure)
6. [An update on recent Claude Code quality reports \ Anthropic](https://www.anthropic.com/engineering/april-23-postmortem)
7. [Mike Ramos Criticizes Anthropic for Undisclosed A/B Test](https://agent-wars.com/news/2026-03-14-anthropic-silent-ab-test-claude-code)
8. [Claude Code effort level and model selection](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)
9. [Why Is Claude Code Slow? Official Causes and Developer Fixes](https://www.aakashx.com/blog/claude-code-slow-causes-fixes/)
10. [Anthropic admits it dumbed down Claude with 'upgrades'](https://www.theregister.com/software/2026/04/24/anthropic-admits-it-dumbed-down-claude-with-upgrades/5228105)
11. [Anthropic faces user backlash over reported performance issues](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/)
12. [Mystery solved: Anthropic reveals changes to Claude's harnesses](https://venturebeat.com/technology/mystery-solved-anthropic-reveals-changes-to-claudes-harnesses-and-operating-instructions-likely-caused-degradation)
13. [Anthropic is facing a wave of user backlash over reports of performance issues](https://finance.yahoo.com/sectors/technology/articles/anthropic-facing-wave-user-backlash-091348318.html)
14. [Anthropic explains Claude Code’s recent performance](https://fortune.com/2026/04/24/anthropic-engineering-missteps-claude-code-performance-decline-user-backlash/?ref=biztoc.com)