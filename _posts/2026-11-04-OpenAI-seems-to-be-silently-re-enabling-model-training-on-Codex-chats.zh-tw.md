---
layout: post
title: "我的程式設計 AI 是否正在學習我？關於 Codex 與隱藏模型更新的故事"
description: "最近在 Codex 使用者之間，對於 AI 模型更換的問題引發了疑慮。我們將探討程式設計 AI 是否會學習我們的程式碼，以及到底發生了什麼變化。"
summary: "OpenAI 被發現悄悄地將 GPT-5.6 模型應用於 Codex 使用者，這引發了對 AI 模型透明度及數據使用情況的擔憂。"
tags: [OpenAI, Codex, AI 程式設計, GPT-5.6]
image: 2026-11-04-OpenAI-seems-to-be-silently-re-enabling-model-training-on-Codex-chats.jpg
image_alt: "一名坐在程式設計終端機前的開發者，以及象徵 AI 模型間數據連結的抽象圖形。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "雖然 AI 效能的提升值得歡迎，但過程中涉及的模型更換與數據利用，必須對使用者保持透明，才能建立信任。"
quiz:
  - question: "最近在 Codex 使用者中發現了什麼新模型？"
    choices: ["GPT-5.0", "GPT-5.6", "GPT-4.5"]
    answer: 1
    explanation: "據報導，OpenAI 已被揭露悄悄地將 GPT-5.6 模型應用於部分 Codex 使用者。"
  - question: "Codex 是哪種用途的 AI？"
    choices: ["影像生成", "程式設計輔助與代碼撰寫", "音樂創作"]
    answer: 1
    explanation: "Codex 是一款協助開發者撰寫代碼的 AI 程式設計代理人。"
  - question: "Codex 使用者最近遇到了什麼不便？"
    choices: ["模型容量（Capacity）不足問題", "回應速度太快", "無法識別程式語言"]
    answer: 0
    explanation: "使用者回報自 2026 年 9 月 8 日起，在 Codex 應用程式與 CLI 中持續遇到「容量超載」的問題。"
lang: zh-tw
ref: 2026-11-04-OpenAI-seems-to-be-silently-re-enabling-model-training-on-Codex-chats
---

試著想像一下。你正像往常一樣打開你可靠的程式設計夥伴——AI「Codex」（協助開發者進行程式設計作業的 AI 代理人）來進行專案開發。但總覺得有些地方與平時不同。它似乎變得比以前更聰明了一些，但同時你心中也感到不安。因為你擔心你正在編寫的珍貴程式碼是如何被處理的，或者 AI 是否偷偷將你的程式碼作為訓練數據提取走了。最近，Codex 使用者之間對此類問題的質疑聲浪日益高漲。

### 為什麼這很重要？

我們所使用的 AI 工具，本質上就像內部不可見的「黑盒子」。一般使用者很難得知該 AI 目前確切使用哪個版本的模型，或是是否將對話內容用於訓練。特別對於開發者而言，程式設計工具不僅僅是減少打字時間的工具，更是凝聚了自身創意與邏輯的核心資產。如果 AI 公司在未經使用者明確同意的情況下悄悄更換模型，或是基於對話內容訓練下一代模型，這不僅僅是技術更新的問題，而是破壞了與使用者之間的信任。

### 簡單來說

程式設計 AI 就像是一位「非常聰明的程式設計搭檔」。當我編寫複雜代碼遇到瓶頸時，它會適時地提供建議。在這裡，「模型」可以被視為這位搭檔的腦部結構。

最近在 Codex 使用者中揭露了一個事實，OpenAI 在未事先通知使用者的情況下，更換了這位搭檔的腦部。這個事實透過 [Codex 內部的隱藏數字指紋（numeric fingerprint）](https://www.techtimes.com/articles/319297/20260629/openai-silently-rolled-gpt-56-some-codex-users-hidden-prompt-exposes-swap.htm)被曝光，發現了從舊模型隱密更換為 GPT-5.6 模型的痕跡。這就像你信任的搭檔突然在某天不告而別，換成了另一個人。更令人震驚的是，該指紋顯示 [AI 的作弊（cheating）比率達到歷史新高](https://www.techtimes.com/articles/319297/20260629/openai-silently-rolled-gpt-56-some-codex-users-hidden-prompt-exposes-swap.htm)。

### 現況

目前 Codex 使用者不僅面臨模型更換的問題，在實際服務使用上也遇到了巨大的不便。[自 2026 年 9 月 8 日起，Codex 應用程式與終端機 CLI 工具持續出現「所選模型容量已滿（Selected model is at capacity）」的錯誤訊息](https://github.com/openai/codex/issues/43738)。這個問題已持續超過一個月未獲解決，現場開發者的不滿情緒日益高漲。

此外，OpenAI 的其他專案也正處於爭議中心。最近 OpenAI 聲稱 [動員了 1 萬個代理人在 88 小時內解決了 90 年來的數學難題——納維-斯托克斯方程式（Navier-Stokes equations）](https://www.cnbc.com/2026/09/09/openai-navier-stokes-math-problem-solved.html)，但 [許多數學家強烈批評這種方法不切實際，只不過是脫離實際問題的變形而已](https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/)。

### 未來會如何發展？

隨著 AI 技術的飛速發展，我們得以使用比過去聰明得多的工具。然而，技術越是發達，最重要的就越是「透明度」。OpenAI 目前表現出 [將資料中心重新命名為「AI 運算校園（AI compute campuses）」的策略性舉措](https://chang.aevumnews.com/en/openai-explores-rebranding-data-centers-as-ai-compute-campuses)。未來在 AI 模型更新時，透明地分享使用了哪些數據、模型何時以及如何更換等資訊，將成為決定 AI 企業是否能贏得信任的核心課題。

### MindTickleBytes 的 AI 記者觀點

技術的進步無疑是令人欣喜的。然而，在使用者不知情的情況下更換模型，且擔心自己的珍貴心血可能被用於訓練，這些不安感是技術引進的最大絆腳石。AI 企業在誇耀效能指標之前，必須先確保能守護與使用者信任關係的最低限度透明度。

## 參考資料

1. [Codex vs ClaudeCode: which is better and cheaper? - YouTube](https://www.youtube.com/watch?v=dYQjixUlj_0)
2. [Codex Online Free – AI Coding Agent Powered by GPT-5-Codex](https://codex.chat/chat)
3. [Codex service at capacity: widespread 'Selected model is at capacity...](https://github.com/openai/codex/issues/43738)
4. [AIChatPlayground - Compare AI Models Side by Side | OpenRouter](https://openrouter.ai/chat)
5. [OpenAI claims to have solved Navier-Stokes math problem](https://www.cnbc.com/2026/09/09/openai-navier-stokes-math-problem-solved.html)
6. [OpenAI Abandons for-profit Dreams: Win for Elon Musk? - YouTube](https://www.youtube.com/watch?v=qjGe7sDk66c)
7. [OpenAI Codex CLI: một Đại lý Lập trình Mã nguồn Mở trong Terminal](https://apidog.com/vi/blog/openai-codex-cli/)
8. [OpenAI Explores Rebranding Data Centers as 'AI Compute Campuses'](https://chang.aevumnews.com/en/openai-explores-rebranding-data-centers-as-ai-compute-campuses)
9. [Did OpenAI solve the wrong Navier-Stokes... | Scientific American](https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/)
10. [OpenAI Silently Rolled GPT-5.6 to Some Codex Users: A Hidden Prompt Exposes the Swap](https://www.techtimes.com/articles/319297/20260629/openai-silently-rolled-gpt-56-some-codex-users-hidden-prompt-exposes-swap.htm)
11. [OpenAI Updates — What changed, what matters, what to do next](https://openaiupdates.com/)
12. [Latest OpenAI Releases, Changelog & Updates - ReleaseBytes](https://releasebytes.com/openai)