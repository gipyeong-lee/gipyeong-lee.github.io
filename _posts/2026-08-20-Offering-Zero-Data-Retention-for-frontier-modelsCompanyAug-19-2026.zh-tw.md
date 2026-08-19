---
layout: post
title: "給予AI敏感資料安全嗎？「零資料保留 (ZDR)」是什麼"
description: "深入淺出解釋企業為安全使用AI而採用的「零資料保留」協議之含義與局限。"
summary: "零資料保留 (ZDR) 是一項強有力的安全協議，AI 提供商承諾即時刪除用戶資料，且不將其用於模型訓練。"
tags: [AI安全, 資料隱私, 零資料保留, ZDR]
image: 2026-08-20-Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026.jpg
image_alt: "顯示數位安全鎖與 AI 模型連接的圖形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企業在 AI 效能與安全性之間取得平衡的努力十分顯著。必須謹記，ZDR 不僅僅是一項設定，更是一份法律協議。"
quiz:
  - question: "零資料保留 (ZDR) 的核心承諾是什麼？"
    choices: ["將資料保留 30 天", "資料在推論後即時刪除，且不被用於訓練", "公開所有對話內容"]
    answer: 1
    explanation: "ZDR 是一項協議，承諾資料在推論瞬間之後即不再保留，也不會被用於訓練或改進服務。"
  - question: "簽署 ZDR 協議時需注意什麼？"
    choices: ["效能必然會下降", "適用於所有 AI 功能", "有狀態 (stateful) 功能等路徑可能不屬於協議範圍"]
    answer: 2
    explanation: "ZDR 主要適用於無狀態 (stateless) 的傳輸路徑，複雜代理系統的功能可能會被排除在外。"
  - question: "近期部分模型（如 Claude Fable 5）發生了什麼變化？"
    choices: ["強制執行 ZDR", "採納了 30 天資料保留政策以取代 ZDR", "完全停止了資料保留"]
    answer: 1
    explanation: "Claude Fable 5 模型為了確保安全性，已將政策從零資料保留變更為 30 天資料保留政策。"
lang: zh-tw
ref: 2026-08-20-Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026
---

想像一下，貴公司正計畫利用最新的 AI 來分析高度機密的專案資料。然而，當您準備將這些資訊輸入 AI 時，卻感到卻步。因為擔心：「這些資料會不會被記錄在 AI 公司的伺服器上，或者日後被洩漏給其他人作為回答內容？」

為了解決這類疑慮，一個名為「零資料保留 (Zero Data Retention, 以下簡稱 ZDR)」的概念應運而生。這真的是能保護我們資料安全的魔法盾牌嗎？

## 這為何重要？

過去，使用公共雲端服務時，資料殘留在伺服器上被視為理所當然。然而對企業而言，將客戶隱私或公司核心機密傳遞給外部 AI 模型本身就是重大的安全風險。ZDR 是幫助這些企業能安心將頂尖 AI 模型 (Frontier Models) 應用於業務的一種「安全協議」[出處: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)。透過 ZDR，可以在傳送資料時消除「紀錄的尾巴」，因此在對安全性高度敏感的金融、醫療與法律領域，它已成為重要的選擇。

## 輕鬆理解：患有健忘症的助理

用簡單的比喻來說，ZDR 就像雇用了一位「患有健忘症的助理」。

一般的 AI 在使用者提問後，會將提問內容與回答一一儲存於伺服器中，就像一位細心的祕書記錄下所有對話內容。但採用 ZDR，則相當於與這位祕書簽約，要求他：「只在聽我提問並回答的那一瞬間記得這些內容，一旦回答結束，就立刻從大腦中刪除所有資訊。」

業者透過此協議承諾，在完成推論（AI 生成回答的過程）後，將不再保留資料，也不會將其用於模型訓練或改進服務 [出處: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)。在這個過程中，甚至可能不會產生任何會有外洩風險的「監視紀錄」[出處: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)。

## 我們該相信到什麼程度？

ZDR 並非萬靈丹。最需要注意的是，**ZDR 不是簡單的「開關」，而是一項法律「協議」** [出處: Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/)。

許多使用者誤以為只要簽署 ZDR 協議，所有功能就都能獲得完美保護。然而，若資料傳遞路徑中使用了 AI 的「有狀態功能 (stateful features，即需要記憶先前對話或任務脈絡的功能)」，該資料可能無法受到 ZDR 保護 [出處: Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/)。這就像助理雖然「當下」會刪除記憶，但若被指派了必須利用特定「記憶庫」才能完成的複雜任務，記錄仍然會留存於某處。

此外，近期的安全政策變更也值得關注。Anthropic 為強化安全性，對部分模型引入了 30 天資料保留政策；以 Claude Fable 5 模型為例，便放棄了既有的零資料保留政策，轉而採納此 30 天保留政策 [出處: Data retention practices for Covered Models | Anthropic Help Center](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models) [出處: Fable 5's 30-Day Retention: The End of Zero Retention? | Digital Applied](https://www.digitalapplied.com/blog/fable-5-30-day-data-retention-zdr-enterprise-2026)。

## 未來展望

未來的 AI 安全市場預計將進一步細分。企業將會採取更靈活的方式：在效能優異的 AI 與安全性之間權衡，根據重要性選擇適用 ZDR 的模型與不適用的模型。ZDR 正逐漸成為一種需要支付更高成本的高階安全服務 [出處: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)。

身為企業負責人，務必詳細確認我們使用的 AI 服務以何種路徑處理資料，以及 ZDR 協議的覆蓋範圍。與其盲目相信「AI 會處理好一切」，不如清楚理解資料處理的結構並簽訂協議，這才是明智之舉。

## MindTickleBytes AI 記者觀點

安全性與效能就像蹺蹺板，一端上升，另一端必然下降。ZDR 展現了企業為了平衡這座蹺蹺板所做的努力。現在是時候培養我們仔細檢視技術便利性背後隱藏合約條件的眼光了。

## 參考資料
1. [Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/)
2. [Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)
3. [Frontier Safety Roadmap Updates | Anthropic](https://www.anthropic.com/responsible-scaling-policy/updates)
4. [Data retention practices for Covered Models | Anthropic Help Center](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models)
5. [Fable 5's 30-Day Retention: The End of Zero Retention? | Digital Applied](https://www.digitalapplied.com/blog/fable-5-30-day-data-retention-zdr-enterprise-2026)