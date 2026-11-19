---
layout: post
title: "如果覺得 AI 助理太多而感到混亂？HubSpot 找到的解答：代理 harness 框架「Aviator」"
description: "在企業用 AI 代理大量湧現、管理難度大增的時代，本文探討 HubSpot 推出的代理 harness 框架「Aviator」與集中式控制中心「AgentHub」，如何改變商業自動化的格局。"
summary: "透過 HubSpot 為解決碎片化 AI 代理管理問題而推出的 AgentHub 與代理 harness 框架「Aviator」，了解超過 250 萬名使用者所使用的商業 AI 平台之演進過程。"
tags: [HubSpot, AgentHub, Aviator, AI Agents, CRM]
image: 2026-11-20-Aviator-HubSpots-Agent-Harness.jpg
image_alt: "表現各種辦公用 AI 代理在單一中央控制中心中有機連接並協同合作的儀表板畫面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "走過無數個別 AI 工具四處散落的過去，如今將其串聯成單一有機系統的「harness（框架）」時代已經來臨。HubSpot 的 Aviator 與 AgentHub 展示了企業用 AI 要穩固落實為真正的實務夥伴所不可或缺的基礎設施。"
quiz:
  - question: "HubSpot 為了解決碎片化的 AI 代理問題而新推出的集中式平台名稱是什麼？"
    choices: ["AgentHub", "Aviator Harness", "Breeze Customer"]
    answer: 0
    explanation: "HubSpot 建立了集中式控制中心 AgentHub，以解決代理分散與碎片化的問題。"
  - question: "HubSpot 的 AI 代理平台記錄的使用者規模大約是多少？"
    choices: ["50 萬名以上", "100 萬名以上", "250 萬名以上"]
    answer: 2
    explanation: "HubSpot 基於創辦人的代理型 AI 平台使用者數已突破 250 萬人。"
  - question: "使用 AgentBuilder 需要具備哪種 HubSpot 訂閱方案？"
    choices: ["免費版（Free）或新手版（Starter）方案", "專業版（Professional）或企業版（Enterprise）方案", "無論任何方案皆可免費使用"]
    answer: 1
    explanation: "AgentBuilder 無法在免費版或新手版中使用，必須具備專業版或企業版方案。"
lang: zh-tw
ref: 2026-11-20-Aviator-HubSpots-Agent-Harness
---

試想一下。假設你是公司裡負責企劃行銷活動、發掘銷售線索並回覆客戶諮詢的忙碌實務工作者。為了提高工作效率，你引進了撰寫電子郵件用 AI、客戶回覆用 AI、數據分析用 AI 等多種人工智慧工具。一開始以為會很方便，但實際操作後卻發現，各個 AI 無法互相溝通、各自為政，反而導致人類管理者必須疲於奔命地居中協調，出現了奇妙的現象。

比喻來說，這就像家裡的每個家電都有各自獨立的遙控器，想開電視得找 A 遙控器、想開冷氣得找 B 遙控器般令人氣結。今天許多企業所面臨的現實正是如此。個別的 AI 功能雖然優秀，但卻無法與企業的核心客戶關係管理系統（CRM）資料有機結合，呈現碎片化的狀態。為了克服這個問題，客戶關係管理領域的巨擘 HubSpot 給出了答案。這就是代理管理的中央控制中心 [AgentHub](https://www.hubspot.com/products/artificial-intelligence) 以及融入工程創新的代理 harness 框架 [Aviator: HubSpot's Agent Harness](https://hubspot.engineering/blog/aviator-hubspots-agent-harness/) [Source 1, Source 2, Source 3]。

在本文中，我們將以淺顯易懂的方式探討 HubSpot 如何將無數的 AI 代理整合進一個井然有序的生態系中，以及這對我們的日常生活與商業發展代表著什麼意義。

---

## 為什麼這很重要？

我們通常一提到 AI，就會聯想到在畫面上開個聊天室視窗並提出問題。然而，企業環境中的 AI 已經超越了單純回答問題的範疇，正在朝著能自主判斷與行動的「代理（Agent）」形式演進。

問題在於，企業在行銷、銷售、服務等各個部門引進了不同的 AI 工具，業界稱此現象為**「代理碎片化（Agent Fragmentation）」** [Source 3]。比喻來說，就像家裡的每個家電都有獨立遙控器一樣。如果要管理的 AI 增加到數十個，管理成本反而會增加，整體生產力反而會下降。

HubSpot 的 AgentHub 與代理 harness 框架 Aviator 正是為了結束這種混亂而進行的嘗試 [Source 1, Source 3]。它提供了一個巨大的「控制塔」，讓使用者能夠在單一地方監控所有 AI 代理、衡量成效、開啟尚未啟用的助理功能，甚至直接建構自訂代理 [Source 2]。在商業生態系中，這堪稱是 AI 不再只是碎片化玩具、而是蛻變為有機合作真正團隊夥伴的分水嶺。

---

## 輕鬆理解：什麼是「代理 harness」與「AgentHub」？

為了直觀地理解這些抽象概念，我們舉兩個日常生活的比喻。

### 1. AgentHub：有多位專業助理工作的「整合中央辦公室」
簡單來說，**AgentHub**（過去稱為 Breeze Agents 的系統）就像是公司內部無數 AI 助理齊聚的**「整合中央辦公室」** [Source 2, Source 3]。
- 走進這間辦公室，你可以一眼看出目前有哪些助理正在努力工作（啟用狀態）、每個助理的表現有多出色（效能檢查） [Source 2]。
- 如果有尚未被指派工作崗位的全新助理，只要點擊一下就能將其喚醒並立即投入實務 [Source 2]。
- 甚至還能直接製作符合企業需求的專屬**「自訂代理」** [Source 2]。

### 2. 代理 harness（Aviator）：協助助理們安全活動的「安全帶與駕駛桿」
那麼，從技術上將這些代理緊密串聯起來的結構——**代理 harness（Agent Harness）**也就是**「Aviator」**究竟是什麼呢 [Source 1]？
在登山或降落傘中，將人體安全固定並控制裝備的繩索或帶子就稱為「harness」（吊帶/框架）。在人工智慧領域中，harness 意指**支撐多個 AI 代理操作複雜工具、維持記憶並安全協調執行過程的框架**。

簡單來說，Aviator 的角色就像是一條堅固的「安全帶與駕駛桿」，將 AI 代理牢牢固定，防止其暴走，使其能夠安全參考客戶的 CRM 資料（客戶諮詢紀錄、購買歷史等），並準確執行行銷、銷售與服務工作。

---

## 現狀：250 萬名使用者選擇的代理型 AI 平台

目前 HubSpot 的代理型 AI 生態系正迎來爆發式成長。HubSpot 創辦人基於此理念打造的代理型 AI 平台**使用者數已突破 250 萬**，獲得全球企業的廣泛支持 [Source 17]。

實際在現場運作的主要功能如下：

1. **客戶代理（Customer Agents）**：全方位支援行銷、銷售與服務團隊。超越單純的回覆，處理即時客戶互動，並實現隨著時間自主學習與最佳化的智慧自動化 [Source 18]。
2. **AI 銷售潛在客戶開發代理（AI Prospecting Agent）**：銷售團隊的必備工具，直接與 CRM 資料連動，能夠識別具備資格的潛在客戶（Leads）、撰寫客製化電子郵件，並自動管理後續追蹤（Follow-up） [Source 8]。
3. **AgentBuilder 與 BuilderPack**：提供企業使用者輕鬆建構專屬自訂代理的環境。特別是透過 HubSpot 的 OAuth，只需安裝一次，不需進行複雜的 API 金鑰設定或個別工作設定，就能立即執行代理 [Source 4, Source 5]。不過，使用 AgentBuilder 需要 HubSpot 專業版（Professional）或企業版（Enterprise）方案 [Source 4]。

像這樣，AgentHub 以公開測試版（Public Beta）形式提供，並設計成能根據各企業的角色（Hub roles）徹底管理治理與權限 [Source 5]。

---

## 未來走向如何？

未來的商用軟體市場將完全從「功能導向」重塑為**「代理導向」**。過去人類必須親自點擊軟體按鈕、尋找選單並輸入資料，而現在，在 AgentHub 這個中央控制塔的指揮下，AI 代理將自動分析客戶資料、發送行銷郵件並受理服務客訴的時代已經來臨。

特別是透過工程部落格公開的「Aviator: HubSpot's Agent Harness」等技術框架的出現 [Source 1]，為超越表面華麗聊天室、與企業內部系統深度結合的高效能 AI 代理奠定了更穩定且無誤運作的基礎。

我們應該關注的並不是單一模型的效能有多聰明。**如何讓無數的 AI 代理結合我們的商業資料（CRM），像同一個團隊一樣有機地協同工作**，這項真正的競爭力時代已經來到了我們眼前 [Source 2]。

---

## MindTickleBytes 的 AI 記者觀點

> 在無數 AI 工具湧現、反而讓工作現場變得更複雜的「數位疲勞」時代裡，HubSpot 的 AgentHub 與 Aviator harness 整理了工具的亂象，為我們開啟了真正的協調時代。AI 不再是孤芳自賞的天才，而是已經紮根成為連結企業各部門與資料的堅實夥伴。

---

## 參考資料

1. [Aviator: HubSpot's Agent Harness](https://hubspot.engineering/blog/aviator-hubspots-agent-harness/)
2. [Run, Build, and Manage Your AI Agents | AgentHub](https://www.hubspot.com/products/artificial-intelligence)
3. [Обзор HubSpot AgentHub (2026) - YouTube](https://www.youtube.com/watch?v=s1ldahJ1Zko)
4. [BuilderPack · AI actions for HubSpot AgentBuilder](https://www.builderpack.com/)
5. [HubSpot AgentHub: Access, Builder, Governance | Flowith](https://flowith.io/tools/hubspot-agent-hub/)
6. [Agent de prospection IA pour les équipes commerciales | HubSpot](https://www.hubspot.fr/products/sales/ai-prospecting-agent)
7. [HubSpot Founder’s Agentic AI Platform Surges Past 2,500,000 Users | CX Today](https://www.cxtoday.com/crm/hubspot-founders-agentic-ai-platform-surges-past-2500000-users/)
8. [Agentic AI: HubSpot Customer Agents & Custom GPTs](https://www.kunocreative.com/blog/agentic-ai-hubspot-agents-custom-gpts)