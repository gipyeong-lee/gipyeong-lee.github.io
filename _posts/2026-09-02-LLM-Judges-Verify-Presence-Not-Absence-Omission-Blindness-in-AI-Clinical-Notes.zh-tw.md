---
layout: post
title: "AI 醫師寫的病歷，真的能信嗎？AI 無法察覺「缺失資訊」的盲點"
description: "探討為何評估 AI 病歷準確度的「AI 裁判」難以發現資訊遺漏的事實，並深入分析其背後的原因與局限。"
summary: "AI 病歷助理所撰寫的文件中，經常出現關鍵資訊遺漏的「缺失（Omission）」錯誤，然而負責評估這些紀錄的 AI 裁判往往只能確認「已存在資訊」，在發現「缺失資訊」方面存在顯著限制。"
tags: [AI, 醫療AI, 病歷, LLM, 技術分析]
image: 2026-09-02-LLM-Judges-Verify-Presence-Not-Absence-Omission-Blindness-in-AI-Clinical-Notes.jpg
image_alt: "透過放大鏡審視 AI 撰寫的病歷文件，象徵性地呈現 AI 的評估能力。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "盲目迷信 AI 的評估能力是非常危險的。必須認知到，區分「存在」與「不存在」是完全不同維度的智能。"
quiz:
  - question: "根據研究結果，AI 裁判最擅長發現的錯誤類型是什麼？"
    choices: ["資訊缺失 (Omission)", "幻覺 (Hallucination)", "確認已存在的資訊"]
    answer: 2
    explanation: "AI 裁判雖然擅長確認紀錄中已包含資訊的「存在」判斷，但在找出缺漏資訊的「缺失」判斷上卻面臨困難。"
  - question: "病歷助理 AI 所撰寫的文件中，最常見的錯誤是什麼？"
    choices: ["資訊缺失 (Omission)", "幻覺 (Hallucination)", "錯別字"]
    answer: 0
    explanation: "在環境 AI (Ambient AI) 撰寫的病歷中，最主要的錯誤類型是關鍵資訊未被記錄的「缺失錯誤」。"
  - question: "當 AI 裁判 (LLM-as-a-judge) 偵測資訊缺失時，其性能表現如何？"
    choices: ["達到人類水準", "非常卓越", "與隨機機率相近 (Chance levels)"]
    answer: 2
    explanation: "研究指出，在偵測資訊缺失時，AI 裁判的表現與隨機猜測的程度相近。"
lang: zh-tw
ref: 2026-09-02-LLM-Judges-Verify-Presence-Not-Absence-Omission-Blindness-in-AI-Clinical-Notes
---

試想一下：您前往醫院與醫師進行了詳盡的諮詢。診療結束後，AI 助理替您撰寫了病歷。細讀之下，發現醫師所言大抵被整理得井井有條，讓您感到放心。但如果其中遺漏了關鍵資訊（例如「從昨天開始的胸痛」），那會怎麼樣呢？若根據這份不完整的紀錄進行處方，真的安全嗎？

近年來，醫院現場引入「環境 AI（Ambient AI，診療現場紀錄助理）」的趨勢日益增長，這類工具能監聽醫病對話並自動生成病歷草稿。雖然其便利性極高，但紀錄中重要資訊被意外省略的「缺失（Omission）」錯誤，仍是一項亟待解決的難題。[출처 12](https://arxiv.org/abs/2608.31016) 今天，我們將深入淺出地探討為何為了應對此問題而引入的「AI 裁判」表現不如預期，以及其背後的原因與局限。

## 為什麼這很重要？

在醫療現場，病歷是守護患者健康最基本且核心的數據。一旦紀錄中遺漏了重要症狀，醫師便可能做出誤診，或導致處方偏差的風險。為了防止此類情況，業界開始採用「AI 裁判（LLM-as-a-Judge）」來取代人力進行紀錄審查。[출처 10](https://www.linkedin.com/posts/catherine-chen-5851a6a0_continual-monitoring-of-note-quality-at-scale-activity-7496283957693448192-ksR_)

然而，如果連這位「AI 裁判」都無法正確找出遺漏的資訊，會發生什麼事呢？這意味著醫療事故的風險依然存在，而我們所使用的 AI 助理實際上正在製造「漏洞百出的紀錄」，甚至連審查系統都無法發現這些漏洞，這將陷入極其嚴重的處境。

## 易懂的比喻：沒有「標準答案」的考試評分

為什麼 AI 裁判無法找出缺失資訊？讓我們用「考試評分」的狀況來比喻。

請將 AI 裁判想像成一位「手握標準答案，對學生的答題卷進行評分的教師」。

*   **存在確認 (Presence)：** 確認學生是否在答題卷上寫下「第 1 題的答案是 A」非常簡單。因為「A」這個字在卷面上清晰可見。AI 在確認特定關鍵字是否包含在紀錄中這類任務上，表現非常優異。[출처 2](https://arxiv.org/pdf/2608.31016)
*   **缺失確認 (Absence)：** 相反地，教師要確認「這位學生是否漏寫了該寫的內容？」，這屬於不同維度的挑戰。若要找出學生未寫出的內容，教師必須將標準答案完全內化，並與答題卷上的每一行進行對比。

根據近期發表的「OmissionBench」專案研究顯示，AI 裁判雖然能強力確認紀錄中「包含什麼」，但在找出「缺少什麼」時，其性能表現僅與隨機猜測（chance levels）相當。[출처 3](https://github.com/composo-ai/omission-bench), [출처 13](https://arxiv.org/html/2608.31016v1) 換言之，AI 只能看見紀錄所承載的「結果」，卻顯著缺乏感知紀錄中未被填補的「空白空間」的能力。學術界將此現象稱為「缺失盲點 (Omission Blindness)」。

## 目前狀況如何？

許多醫療 AI 系統已開始利用 AI 裁判來評估病歷品質。[출처 10](https://www.linkedin.com/posts/catherine-chen-5851a6a0_continual-monitoring-of-note-quality-at-scale-activity-7496283957693448192-ksR_) 然而，現實性能表現卻相當冷酷。研究結果指出，實際由 AI 撰寫的病歷中，約有 3.45% 包含資訊缺失錯誤（幻覺錯誤則為 1.47%）。[출처 18](https://www.nature.com/articles/s41746-025-01670-7)

問題在於，理應過濾這些缺失的 AI 裁判，卻只看得見「存在」而看不見「缺失」。[출처 2](https://arxiv.org/pdf/2608.31016) 甚至由於負責評估的 AI，與產出該紀錄的 AI 擁有類似的思考邏輯，導致它們容易重複同樣的錯誤，或對錯誤視而不見。[출처 4](https://www.youtube.com/watch?v=BPXFDC7WHSk)

## 未來將如何發展？

隨著 AI 裁判的局限性變得顯著，產業界正透過多種面向進行突破：

1.  **引入確定性驗證工具：** 不再僅依賴 AI 的判斷，而是結合簡單且明確的程式規則，例如關鍵字檢核清單來進行雙重驗證。[출처 4](https://www.youtube.com/watch?v=BPXFDC7WHSk)
2.  **多重評估體系：** 不只依靠單一 AI 裁判，而是利用多個模型或多重代理人系統（Multi-agent system）來進行資訊的交叉驗證。[출처 14](https://www.nature.com/articles/s41746-025-02005-2)
3.  **人類參與：** 在安全性至上的醫療領域，最終核心仍是「以人為中心的評估」——即由身為專家的醫師對 AI 的審查結果進行最終把關，而非讓 AI 全權評估。[출처 17](https://arxiv.org/html/2607.18828)

我們現在已來到必須審慎評估 AI 不僅是「能完成什麼」，更要審視它「錯過了什麼」的時代。

## MindTickleBytes AI 記者的觀點

將 AI 立為裁判固然便利，但區分「存在」與「缺失」是智能的另一個維度。對於無法解讀紀錄中「沈默」的 AI，若要完全託付我們的健康，顯然還有很長一段路要走。

## 參考資料
1. [2608.31016] LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes and What Recovers It (https://arxiv.org/abs/2608.31016)
2. LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes and What Recovers It (https://arxiv.org/pdf/2608.31016)
3. GitHub - composo-ai/omission-bench: OmissionBench harness: code (https://github.com/composo-ai/omission-bench)
4. Replace Your LLM Judge With 10 Lines of pytest - YouTube (https://www.youtube.com/watch?v=BPXFDC7WHSk)
5. LLM-as-a-judge: a complete guide to using LLMs for evaluations (https://www.evidentlyai.com/llm-guide/llm-as-a-judge)
7. LLM-as-a-Judge Simply Explained: The Complete Guide (https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)
8. Position Bias in LLM Judges: Measurement and Mitigation (https://mbrenndoerfer.com/writing/position-bias-in-llm-judges)
9. LLMs bow to pressure, changing answers when challenged (https://www.computerworld.com/article/4023989/llms-bow-to-pressure-changing-answers-when-challenged-deepmind-study.html)
10. Continual Monitoring of Note Quality At Scale (https://www.linkedin.com/posts/catherine-chen-5851a6a0_continual-monitoring-of-note-quality-at-scale-activity-7496283957693448192-ksR_)
11. LLM Judges Are Unreliable (https://www.cip.org/blog/llm-judges-are-unreliable)
12. LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes (https://arxiv.org/abs/2608.31016v1)
13. LLM Judges Verify Presence, Not Absence (https://arxiv.org/html/2608.31016v1)
14. Evaluating clinical AI summaries with large language models as judges (https://www.nature.com/articles/s41746-025-02005-2)
17. Evaluating medical AI under missing information (https://arxiv.org/html/2607.18828)
18. A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation (https://www.nature.com/articles/s41746-025-01670-7)