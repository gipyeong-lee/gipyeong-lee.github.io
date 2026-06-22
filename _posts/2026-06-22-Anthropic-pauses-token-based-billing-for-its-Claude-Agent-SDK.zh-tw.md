---
layout: post
title: "AI 定價方案突然變更？Anthropic 為何在開發者的反彈下暫緩實施"
description: "近期 AI 公司 Anthropic 原定計畫導入新的代幣（Token）計費方案，目前已宣布暫緩。為您淺顯易懂地說明開發者為何反彈，以及這件事對我們有何意義。"
summary: "Anthropic 原計劃對 Claude Agent SDK 導入高昂的代幣計費方案，因遭遇開發者的強烈反彈而宣布暫緩實施。"
tags: [AI, Anthropic, Claude, 定價方案, 技術議題]
image: 2026-06-22-Anthropic-pauses-token-based-billing-for-its-Claude-Agent-SDK.jpg
image_alt: "置於複雜文件與程式碼背景上的 Anthropic 標誌圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企業追求創新固然重要，但若該創新導致使用者難以承擔的成本壓力，將會失去信任。此次暫緩決定顯示出，AI 服務要能普及，「永續的經濟性」是不可或缺的基石。"
quiz:
  - question: "Anthropic 原本打算導入後又暫緩的計費方式是什麼？"
    choices: ["訂閱制無限制使用", "基於代幣的按量計費", "廣告置入型免費使用"]
    answer: 1
    explanation: "Anthropic 原本計畫將 Agent SDK 的使用量從既有的訂閱服務中剔除，改為根據使用量計費的代幣收費機制。"
  - question: "這次定價方案變更讓開發者最擔憂的是什麼？"
    choices: ["服務速度變慢", "成本突然暴增", "資料安全問題"]
    answer: 1
    explanation: "開發者擔心原本在訂閱費用內即可處理的大規模代理（Agent）工作，改為獨立計費後，成本將大幅增加。"
  - question: "Anthropic 發給開發者的通知核心內容為何？"
    choices: ["全面廢除計費方案", "維持現行政策", "確定調漲兩倍費用"]
    answer: 1
    explanation: "Anthropic 透過發送給客戶的電子郵件表示：「目前不會有任何變更（Nothing changes for now）」，暫緩了該政策。"
lang: zh-tw
ref: 2026-06-22-Anthropic-pauses-token-based-billing-for-its-Claude-Agent-SDK
---

試想一下，您訂閱了一項每個月支付固定費用即可無限使用的串流服務。然而公司卻突然宣布：「從現在開始，請依據觀看電影的分鐘數額外支付費用」，您會作何感想？對於每天看電影的人來說，這不僅令人困惑，更會感到憤怒。

近期在人工智慧領域，就發生了類似的情況。知名 AI 公司 Anthropic 原先宣布將變更其開發工具「Claude Agent SDK」（一種協助 AI 自主思考並執行任務的工具）的定價機制，卻在施行前夕宣布全面暫緩。 [Source 2](https://www.devdigest.org/articles/anthropic-pauses-token-based-billing-for-claude-agent-sdk), [Source 6](https://www.aichatdaily.com/ai-business/anthropic-pauses-token-based-billing-change-claude-agent-sdk)

### 這件事為何重要？

此事件顯示 AI 技術不僅僅是在「變得更聰明」，在「人們如何付費與使用」的經濟層面上，也正處於重要的轉折點。 [Source 4](https://www.weexplaintech.com/2026/06/anthropic-pauses-token-based-billing.html)

開發者利用 AI 製作執行複雜自動化任務的應用程式。如果定價機制突然改變，營運這些應用程式的成本可能會瞬間翻漲數倍。這不僅僅是開發者的煩惱，隨著營運成本上升，最終可能以提高服務價格或縮減功能的形式，對我們這些使用 AI 應用的普通用戶造成間接衝擊。 [Source 1](https://arstechnica.com/ai/2026/06/anthropic-pauses-token-based-billing-for-its-claude-agent-sdk), [Source 10](https://www.newsbreak.com/news/4714926599628-anthropic-pauses-token-based-billing-for-its-claude-agent-sdk)

### 淺顯易懂：從吃到飽變成按盤計費？

若將 Anthropic 的變更方案比喻為餐飲，就像是從「吃到飽」改為「按盤計費」。

原本開發者支付每月固定訂閱費，即可獲得固定額度的 AI 使用量。然而 Anthropic 於 5 月 13 日宣布，自 6 月 15 日起，將把「Claude Agent SDK」的使用量從現有的訂閱福利中排除。 [Source 7](https://www.winzheng.com/en/article/anthropic-pauses-claude-agent-sdk-token-billing)

比喻來說，原本的訂閱費變成了「門票」，而 AI 實際處理任務的數量則需以「代幣」（Token，AI 處理數據的單位，類似句子的單字碎片）為單位額外付費。 [Source 7](https://www.winzheng.com/en/article/anthropic-pauses-claude-agent-sdk-token-billing), [Source 8](https://letsdatascience.com/news/anthropic-pauses-claude-agent-sdk-billing-overhaul-1cff2071) 不僅如此，使用者可能還需要額外購買價值 20 至 200 美元不等的點數。 [Source 8](https://letsdatascience.com/news/anthropic-pauses-claude-agent-sdk-billing-overhaul-1cff2071)

### 目前現況

該計畫原定於 6 月 15 日生效。 [Source 4](https://www.weexplaintech.com/2026/06/anthropic-pauses-token-based-billing.html), [Source 6](https://www.aichatdaily.com/ai-business/anthropic-pauses-token-based-billing-change-claude-agent-sdk) 但發表後隨即引發開發者的強烈抗議。特別是那些利用 AI 處理大量自動化任務的「重度使用者」，在計算後發現營運成本將暴增至難以負荷的地步，因此深感不安。 [Source 2](https://www.devdigest.org/articles/anthropic-pauses-token-based-billing-for-claude-agent-sdk), [Source 9](https://www.coreiten.com/en/article/anthropic-abruptly-halts-claude-agent-sdk-billing-hike-after-developer-backlash)

最終，Anthropic 在生效當天宣布暫緩執行該計畫。 [Source 13](https://www.bitsminds.com/news/anthropic-pauses-claude-agent-sdk-billing-overhaul-2026) 他們在發給客戶的郵件中簡短表示：「目前不會有任何變更（Nothing changes for now）。」 [Source 13](https://www.bitsminds.com/news/anthropic-pauses-claude-agent-sdk-billing-overhaul-2026) 目前仍維持原有的訂閱方式與使用量限制。 [Source 12](https://www.msn.com/en-us/news/other/anthropic-pauses-claude-agent-sdk-billing-overhaul/gm-GM25B5B0AE)

### 未來展望

這次暫緩決策顯示 Anthropic 無法無視開發者的聲音。但這並不代表定價方案的調整就此永遠消失，因為隨著 AI 服務規模擴大及模型升級，企業仍需尋找更有效率、更具體系的獲利模式來支撐營運成本。 [Source 4](https://www.weexplaintech.com/2026/06/anthropic-pauses-token-based-billing.html)

未來我們將持續關注 Anthropic 如何與開發者協商，制定出更合理且具預測性的新計費體系。隨著 AI 深入我們的日常生活，其使用成本也必須透明且合理，如此一來，技術普及的速度才能進一步加快。

## 參考資料

1. [Anthropic “pauses” token-based billing for its Claude Agent SDK](https://arstechnica.com/ai/2026/06/anthropic-pauses-token-based-billing-for-its-claude-agent-sdk/)
2. [Anthropic Pauses Token-Based Billing for Claude Agent SDK](https://www.devdigest.org/articles/anthropic-pauses-token-based-billing-for-claude-agent-sdk)
3. [Anthropic “pauses” token-based billing for its Claude Agent SDK](https://vuink.com/post/nefgrpuavpn-d-dpbz/ai/2026/06/anthropic-pauses-token-based-billing-for-its-claude-agent-sdk)
4. [Anthropic Pauses Token-Based Billing - weexplaintech.com](https://www.weexplaintech.com/2026/06/anthropic-pauses-token-based-billing.html)
5. [Anthropic "pauses" token-based billing for its Claude Agent SDK](https://article.wn.com/view/2026/06/17/Anthropic_pauses_tokenbased_billing_for_its_Claude_Agent_SDK/)
6. [Anthropic pauses token-based billing change for Claude Agent SDK](https://www.aichatdaily.com/ai-business/anthropic-pauses-token-based-billing-change-claude-agent-sdk)
7. [Anthropic Pauses Claude Agent SDK Token Billing Change Amid ...](https://www.winzheng.com/en/article/anthropic-pauses-claude-agent-sdk-token-billing)
8. [Anthropic Pauses Claude Agent SDK Billing Overhaul](https://letsdatascience.com/news/anthropic-pauses-claude-agent-sdk-billing-overhaul-1cff2071)
9. [Anthropic Pauses Claude Agent SDK Billing Changes for Developers](https://www.coreiten.com/en/article/anthropic-abruptly-halts-claude-agent-sdk-billing-hike-after-developer-backlash)
10. [Anthropic "pauses" token-based billing for its Claude Agent SDK](https://www.newsbreak.com/news/4714926599628-anthropic-pauses-token-based-billing-for-its-claude-agent-sdk)
12. [Anthropic Pauses Claude Agent SDK Billing Overhaul - MSN](https://www.msn.com/en-us/news/other/anthropic-pauses-claude-agent-sdk-billing-overhaul/gm-GM25B5B0AE)
13. [Anthropic Backs Off Its Claude Agent SDK Billing Overhaul on ...](https://www.bitsminds.com/news/anthropic-pauses-claude-agent-sdk-billing-overhaul-2026)