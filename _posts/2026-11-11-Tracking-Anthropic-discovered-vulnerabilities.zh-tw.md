---
layout: post
title: "AI 竟能找出軟體的「漏洞」？解析 Anthropic 的安全追蹤計畫"
description: "探討 AI 如何自動發現並管理軟體安全漏洞，以及 Anthropic 安全計畫對產業帶來的影響。"
summary: "Anthropic 運用其 AI 模型自動掃描全球軟體安全漏洞，並建立了一套系統化的安全計畫，通知開發人員進行修復。"
tags: [AI, 安全, Anthropic, 軟體, 技術]
image: 2026-11-11-Tracking-Anthropic-discovered-vulnerabilities.jpg
image_alt: "螢幕上顯示著象徵電腦程式碼與資訊安全的數位圖形。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 轉變為防禦者主動找出漏洞固然是件好事，但漏洞發現速度遠超修補速度，這將是我們必須解決的新課題。"
quiz:
  - question: "Anthropic 在發現安全漏洞後，優先採取的行動是什麼？"
    choices: ["將漏洞公開在網路上", "私下通知軟體維護者", "立即編寫攻擊程式碼"]
    answer: 1
    explanation: "Anthropic 遵循「協調漏洞揭露 (CVD)」政策，將發現的漏洞私下傳遞給軟體維護者，以便在公開前給予其修復的時間。"
  - question: "截至 2026 年 10 月，Anthropic 發現的漏洞候選名單中，實際公開的漏洞數量為？"
    choices: ["6,157 個", "29,439 個", "516 個"]
    answer: 0
    explanation: "根據 Anthropic 的儀表板數據，在 29,439 個候選漏洞中，有 6,157 個已公開，其中 516 個已在相關專案中獲得修復。"
  - question: "Anthropic 安全計畫目前面臨的現實挑戰為何？"
    choices: ["AI 完全無法發現漏洞", "漏洞發現速度遠快於實際修補速度", "所有漏洞都已立即遭到惡意利用"]
    answer: 1
    explanation: "在已發現的漏洞中，僅約 8.4% 完成修復。相較於 AI 發現漏洞的數量，開發人員實際修補的速度顯得滯後，這是目前的現實挑戰。"
lang: zh-tw
ref: 2026-11-11-Tracking-Anthropic-discovered-vulnerabilities
---

試著想像一下，你使用的智慧型手機或網頁瀏覽器裡住著一位「安全偵探」。這位偵探日以繼夜地檢查軟體的每一個角落，找出駭客可能入侵的細微「破口（漏洞）」。

近期，人工智慧企業 Anthropic 正因運作這樣的安全計畫而備受關注。AI 不再僅限於寫文章或作畫，它已站在維護我們日常所用程式安全的最前線。

### 這為何重要？

我們的日常生活仰賴無數的軟體。我們透過瀏覽器購物、透過作業系統（OS）工作。如果這些程式存在安全漏洞，會發生什麼事？駭客可能會趁虛而入，竊取個資或癱瘓系統。

過去，尋找這些漏洞一直是人類安全專家的職責。然而，現代軟體浩瀚且複雜，人類很難找出所有的漏洞。Anthropic 的作法正在改寫規則，透過 AI 更快速、高效地找出漏洞，試圖在攻擊者動歪腦筋前先築起防禦牆。這不僅關乎個人資訊保護，更直接影響我們所信任的整體數位生態系統之安全性 [[出處 2](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)]。

### 淺顯易懂：AI「安全偵探」的工作方式

Anthropic 利用「Claude」AI 模型及其內部研究模型，分析全球的開源與封閉原始碼軟體 [[出處 2](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude), [出處 6](https://red.anthropic.com/2026/cvd/about/)]。

簡單來說，若過去的安全檢測是靠人力拿著放大鏡巡視建築物來尋找裂縫，那麼 Anthropic 的 AI 就像是先徹底掌握了建築藍圖，再動用數千台攝影機，瞬間找出所有結構缺陷。

特別是名為「Claude Mythos」的模型，它不僅能發現漏洞，還具備編寫攻擊程式碼、模擬實際攻擊路徑的能力 [[出處 7](https://www.sherlockforensics.com/blog/claude-mythos-security-analysis-2026.html), [出處 8](https://www.dynatrace.com/news/blog/how-anthropic-claude-mythos-is-reshaping-the-vulnerability-landscape/)]。這好比醫生診斷病情時，不只看病況，還會模擬病菌入侵體內的路徑，藉此研發出完美的疫苗。

### 現況：數千個漏洞，卻緩慢的修補速度

目前已經發現了多少漏洞？截至 2026 年 10 月 2 日，根據 Anthropic 的儀表板數據，團隊審查了約 29,439 個漏洞候選，其中 6,157 個已正式對外公開 [[出處 5](https://vulnerabilities.ai/ledger)]。

但這裡有一個既有趣又令人擔憂的現象：在這些發現的漏洞中，開發人員實際完成修復（Patch）的比例僅約 8.4%（516 個）[[出處 5](https://vulnerabilities.ai/ledger)]。AI 正以驚人的速度找出問題，但人類修補的速度卻難以跟上。

此外，儘管發現了這麼多漏洞，幸運的是，其中不到 0.5% 的漏洞被駭客實際惡意利用 [[出處 16](https://www.theregister.com/security/2026/09/21/anthropic-linked-cves-pile-up-attackers-mostly-shrug/5298018)]。不過，由於已有案例報告顯示，AI 被用於在無需人類干預的情況下自動發現並成功攻擊，我們仍不可掉以輕心 [[出處 19](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf)]。

### 未來展望

Anthropic 並不會將發現的漏洞立即散布到網路上。相反地，他們遵循「協調漏洞揭露 (Coordinated Vulnerability Disclosure, CVD)」政策，先行私下通知相關軟體的維護者，並給予修改的時間 [[出處 6](https://red.anthropic.com/2026/cvd/about/)]。

隨著未來 AI 發現的漏洞數量將呈現指數級增長，軟體開發環境也勢必需要調整。業界很可能會從「人類逐一修復 AI 發現的問題」，轉向「AI 發現問題並自動產生修補檔應用」的「自動化防禦體系」。

我們現在活在一個新時代，不再僅是擔心 AI 是否會攻擊我們的電腦，而是如何利用 AI 來打造更安全的軟體環境。究竟未來有哪些技術進展能守護我們的數位日常，值得我們持續關注 Anthropic 的儀表板。

---
**MindTickleBytes 的 AI 記者觀點：**
科技總是一體兩面。Anthropic 的 AI 扮演安全守護者的角色固然是一大進步，但目前漏洞發現速度遠超修補速度的現況，正對軟體產業提出史無前例的速度要求。安全不再是純粹的人類藝術，而是一場人類與 AI 必須攜手進行的馬拉松。

## 參考資料

1. [Tracking Anthropic-discovered vulnerabilities](https://www.vulncheck.com/blog/anthropic-glasswing-november-update)
2. [Discovering and exploiting vulnerabilities in critical, real ...](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)
3. [Anthropic's coordinated vulnerability disclosure dashboard](https://red.anthropic.com/2026/cvd/)
4. [Coordinated vulnerability disclosure for Claude-discovered ...](https://www.anthropic.com/coordinated-vulnerability-disclosure)
5. [Ledger — Tracking the AI Vulnerability-Discovery Programs](https://vulnerabilities.ai/ledger)
6. [About this dashboard - red.anthropic.com](https://red.anthropic.com/2026/cvd/about/)
7. [Claude Mythos Security Vulnerabilities: What We Know in 2026](https://www.sherlockforensics.com/blog/claude-mythos-security-analysis-2026.html)
8. [How Anthropic Claude Mythos is reshaping the vulnerability ...](https://www.dynatrace.com/news/blog/how-anthropic-claude-mythos-is-reshaping-the-vulnerability-landscape/)
9. [Research \Anthropic](https://www.anthropic.com/research)
10. [A Cheeky Pint withAnthropicCEO Dario Amodei - YouTube](https://www.youtube.com/watch?v=GcqQ1ebBqkc)
11. [Secret Claudetrackershocks users afterAnthropic’s anti-surveillance...](https://arstechnica.com/tech-policy/2026/07/anthropic-outed-for-claude-tracker-that-secretly-monitored-chinese-users/)
13. [AnthropicStatus. Check ifAnthropicis down or having... | StatusGator](https://statusgator.com/services/anthropic)
16. [Anthropic-linked CVEs pile up, attackers mostly shrug](https://www.theregister.com/security/2026/09/21/anthropic-linked-cves-pile-up-attackers-mostly-shrug/5298018)
19. [Full report: Disrupting the first reported AI-orchestrated ...](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf)