---
layout: post
title: "AI使用到一半被『限制』而停下來嗎？與朋友一起等待的新方法"
description: "當 AI 使用量限制迫使您必須中斷編碼工作時，向您介紹這款可以讓您在等待時與朋友聊天的 Mac 應用程式「Die With Me」。"
summary: "「Die With Me」這款 Mac 應用程式登場了，它能讓您與朋友共享 AI 使用量限制，並在受限時一起聊天。"
tags: [AI, 工具, 生產力, 開發者, Mac]
image: 2026-09-18-Show-HN-Die-With-Me-Claude-and-Codex-rate-limits-as-AIM-away-messages.jpg
image_alt: "展示監控 AI 使用量限制並可與朋友聊天的「Die With Me」應用程式介面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "將 AI 使用量限制這種枯燥且令人沮喪的體驗，轉化為過去通訊軟體的懷舊感，這一點非常有趣。這是一個將技術限制轉化為社交連結的好點子。"
quiz:
  - question: "「Die With Me」應用程式提供什麼功能？"
    choices: ["AI 模型無限使用", "查看朋友的 AI Token 使用量以及等待室聊天", "提升 AI 回應速度"]
    answer: 1
    explanation: "該應用程式提供查看朋友 AI 使用量，以及當 Token 限制低於 20% 時，與其他等待者進行聊天的功能。"
  - question: "可以查看哪些 AI 模型的使用量？"
    choices: ["Claude 與 Codex", "ChatGPT 與 Gemini", "所有模型"]
    answer: 0
    explanation: "該應用程式專門用於追蹤 Claude 和 Codex 的使用量限制。"
  - question: "「Die With Me」應用程式參考了哪款應用程式而開發？"
    choices: ["Discord", "過去 AIM 通訊軟體的聯絡人清單（Buddy List）", "最新社群軟體"]
    answer: 1
    explanation: "它將過去 AIM 通訊軟體的聯絡人清單（Buddy List）感性應用於 AI Token 使用量監控中。"
lang: zh-tw
ref: 2026-09-18-Show-HN-Die-With-Me-Claude-and-Codex-rate-limits-as-AIM-away-messages
---

想像一下：您正忙於編寫複雜的程式碼，並向 AI 助理求助時，螢幕突然跳出「已達使用量限制」的訊息。工作停擺，您只能無奈地等待限制解除。此時，心中難免會浮現「只有我這樣嗎？」的煩悶感。

然而，最近一款為 Mac 設計的應用程式吸引了眾人目光，它以過去使用通訊軟體時的懷舊感，巧妙地化解了這種窘境。這款應用程式名為「Die With Me」。它將技術限制這種冰冷而現實的問題，轉化為充滿人情味的溫暖等待室。

## 為什麼這很重要？

到了 2026 年，Claude Code 與 Codex 已成為眾多開發者不可或缺的核心 AI 編碼代理 [[出處: Claude Code vs Codex: developers debate after - explainx.ai](https://explainx.ai/blog/claude-code-vs-codex-rate-limit-boost-2026)]。然而，這些強大的工具同樣面臨著「使用量限制」的挑戰。

對開發者來說，AI 使用量限制不僅僅是單純的不便，更是完全中斷工作流程的絆腳石。特別是在多個工具間切換作業時，往往會導致工作環境內容（背景知識、已向 AI 解釋的上下文）遺失，被迫花費時間重新說明 [[出處: Show HN: `npx continues` – resume same session Claude, Gemini ...](https://news.ycombinator.com/item?id=47075089)]。「Die With Me」正是關注到了這一點。它將使用量限制從單純的技術故障，轉變為與朋友共享的社交體驗。

## 簡單理解：AI 等待室的聯絡人清單

若要簡單比喻，「Die With Me」可以說是**「將舊時代通訊軟體的聯絡人狀態顯示器，製作成了 AI 使用量版本」**。

在我們過去愛用的 AIM 等通訊軟體中，有著可以確認朋友是否上線並順便打個招呼的「聯絡人清單」。這款應用程式則會實時顯示朋友的 Claude 或 Codex 剩餘 Token（AI 一次能處理的數據單位）使用量 [[出處: Show HN: Die With Me – Claude and Codex rate limits as AIM away messages](https://blogviral010.blogspot.com/2026/09/show-hn-die-with-me-claude-and-codex.html)]。

例如，當朋友 A 在寫程式且限制快用完時，我可以實時得知該狀況。更有趣的是，當使用者的 Token 額度低於 20% 時，應用程式不會讓您孤單等待，而是會將您連結到一個「等待室聊天室」，讓您與同樣受到限制、正在等待的其他朋友們互動 [[出處: Show HN: Die With Me – Claude and Codex rate limits as AIM away messages](https://blogviral010.blogspot.com/2026/09/show-hn-die-with-me-claude-and-codex.html)]。

這就像我們在搶購喜愛歌手的演唱會門票失敗時，與同樣處境的粉絲在社群裡互相安慰一樣。這是一種以人與人之間的連結來填補技術缺陷的方式。

## 現況：限制依然是開發者的煩惱

目前，開發者生態圈中正圍繞著 Claude Code 與 Codex 展開激烈的資源使用競爭。Anthropic 正在持續調整 Claude Code 的使用量限制 [[出處: Claude Code Limits Cut 17% Sept 14 (2026 Math) - explainx.ai](https://www.explainx.ai/blog/anthropic-claude-code-limits-17-percent-cut-september-2026-august-2026)]，許多開發者每天都在為尋找適合自己工作風格的工具而苦戰 [[出處: Claude Code vs. Codex for Heavy Users: Limits, Costs, and ...](https://codeongrass.com/blog/claude-code-vs-codex-heavy-users-limits-costs-switching/)]。

然而重點在於，無論工具如何進化，限制這道高牆始終存在。「Die With Me」並沒有試圖否認或繞過這些技術限制，而是重新定義了那段等待的時光，將其轉化為「共度的時光」。開發者們透過這款程式，獲得了一個能輕鬆打招呼、分享撇步的機會，彼此慰問：「我現在也被限制了，你呢？」

## 未來將如何發展？

AI 編碼工具的使用量限制政策未來仍會依據狀況彈性調整。某些日子可能額度寬裕，某些日子可能會更加嚴格。然而，像「Die With Me」這類應用程式的出現，預示了 AI 時代的一種新文化。

隨著 AI 變得更加聰明、便利，我們將會更關注於與我們一同使用這些技術的「人」，而非技術本身。下次在作業途中看到 AI 使用量限制訊息時，別太過生氣。不妨換個想法，這或許是進入等待室、與朋友們聚聚並享受片刻咖啡時光的休憩時刻。

## MindTickleBytes AI 記者視角

當技術不完美時，或許正是人們產生交集的空隙所在。「Die With Me」以創造性的方式重新詮釋了 AI 的局限性，是一款非常有溫度的應用程式。它完美呈現了在冷漠的編碼環境中，我們始終不能失去的，正是人與人之間的溫度。

## 參考資料

1. [Show HN: Claude and Codex rate limits as AIM away messages](https://news.ycombinator.com/item?id=49743095)
2. [Claude Code vs Codex: developers debate after - explainx.ai](https://explainx.ai/blog/claude-code-vs-codex-rate-limit-boost-2026)
3. [Show HN: Die With Me – Claude and Codex rate limits as AIM away messages](https://thenote.app/post/en/show-hn-die-with-me-claude-and-codex-rate-limits-as-aim-away-messages-gi2l22g1mq)
4. [Show HN: Die With Me – Claude and Codex rate limits as AIM away messages](https://blogviral010.blogspot.com/2026/09/show-hn-die-with-me-claude-and-codex.html)
5. [Claude Code Limits Cut 17% Sept 14 (2026 Math) - explainx.ai](https://www.explainx.ai/blog/anthropic-claude-code-limits-17-percent-cut-september-2026-august-2026)
6. [Show HN:`npx continues` – resume same session Claude, Gemini ...](https://news.ycombinator.com/item?id=47075089)
7. [Claude Code vs. Codex for Heavy Users: Limits, Costs, and ...](https://codeongrass.com/blog/claude-code-vs-codex-heavy-users-limits-costs-switching/)