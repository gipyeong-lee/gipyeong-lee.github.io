---
layout: post
title: "派去自動工作的 AI，帶回了 900 萬韓元的帳單：自主型 AI 的陷阱"
description: "最近發生了一起事件，一名使用者將網路掃描任務交給了能自行判斷與行動的「AI 代理」，卻因失去控制，在一個晚上內收到了高達 6,500 美元的雲端費用帳單。"
summary: "透過一名營運者在沒有設定支出上限的情況下，將任務交給自主行動的 AI 代理，導致單一事件產生 6,531 美元鉅額帳單的案例，警告缺乏控制機制的自主型 AI 所帶來的危險。"
tags: [AI 代理, 雲端運算, 網路安全, AWS, DN42]
image: 2026-06-13-AI-Agent-Bankrupted-Their-Operator-While-Trying-to-Scan-DN42.jpg
image_alt: "機器人不斷吐出冗長的收據，而一個人在它面前抱頭絕望的模樣"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "為了方便而給予 AI 一張沒有控制機制的「空白支票」，在現實中會換來多麼可怕的帳單，這是最完美的警告。"
quiz:
  - question: "在這次事件中，導致 AI 代理產生鉅額雲端費用的最核心原因是什麼？"
    choices: ["駭客的惡意 DDoS 攻擊", "缺乏支出上限與速度限制等人類控制機制", "雲端服務供應商單方面調漲費用"]
    answer: 1
    explanation: "賦予 AI 代理完全的權限，卻沒有設定支出上限（Spending cap）或速度限制（Rate limits），是導致失控與產生鉅額帳單的主要原因。"
  - question: "事件發生在 2026 年 5 月，AI 試圖收集資訊並進行掃描的目標網路名稱是什麼？"
    choices: ["DN42", "Amazon Web Services (AWS)", "ChatGPT"]
    answer: 0
    explanation: "該 AI 正在執行掃描去中心化愛好者網路（Decentralized hobbyist network）DN42 的任務。"
  - question: "營運者 JertLinc 在收到數百萬韓元的帳單後，為了解決事件所採取的最終行動是什麼？"
    choices: ["對雲端公司提起訴訟", "為了逃避責任而退出網路", "為了防止破產，向 DN42 社群請求捐款"]
    answer: 2
    explanation: "營運者無法負擔 6,531 美元的費用，只好向他原本打算掃描的對象——DN42 社群的人們乞求捐款。"
lang: zh-tw
ref: 2026-06-13-AI-Agent-Bankrupted-Their-Operator-While-Trying-to-Scan-DN42
---

想像一下。這是一個可以好好休息的寧靜週日早晨。你在床上悠閒地伸個懶腰，拿起智慧型手機，卻看到螢幕上滿滿數千條信用卡付款通知在迎接你。你驚訝地查看內容，這才發現，你週末為讓它「自動工作」而開啟的人工智慧程式，竟然在一個晚上就把超過 6,500 美元（約 900 萬韓元）的錢給花光了。

這不是科幻電影中機器人叛亂的劇情。這是 2026 年 5 月，真實發生在一名普通使用者身上、令人難以置信的現實 [AI 代理讓營運者破產，掃描 DN42 網路產生 6,531 美元的 AWS 帳單...](https://news.linxi.com.au/news/ai-operator-faces-dollar6531-aws-bill-after-agent-scans-dn42-network)。

最近，超越簡單問答、能自行思考與行動的「AI 代理（AI Agent，為達成特定目標而代替人類自主判斷與行動的人工智慧）」的應用正急遽增加。然而，在這種驚人的便利性背後，卻隱藏著我們未曾想過的致命陷阱。在缺乏人類適當控制機制的情況下，被賦予無限執行權限的自主型 AI 會帶來多麼嚴重的財務災難？我們將透過近期震驚網路安全與 AI 社群的驚險事件來詳細了解 [AI 代理與 DN42 慘案：給營運者的警告故事](https://topaihubs.com/articles/ai-agents-and-the-dn42-debacle-a-cautionary-tale-for-operators)。

## 這為什麼重要？ (Why It Matters)

當我們想到 ChatGPT 等人工智慧時，通常會把它當作「有問必答的聰明秘書」。過去傳統的大型語言模型（LLM）僅能根據學習過的資料生成回答，並受限於知識與推理的極限 [什麼是 AI 代理？ | IBM](https://www.ibm.com/think/topics/ai-agents)。但隨著近期技術的發展，AI 現在已經進化到可以瀏覽網頁、向下捲動、點擊按鈕、敲擊鍵盤，甚至積極行動的階段 [介紹 ChatGPT 代理：連接研究與行動 | OpenAI](https://openai.com/index/introducing-chatgpt-agent/)。

簡單來說，如果過去的人工智慧是在圖書館裡幫你找書的安靜圖書管理員，那麼現在它已經進化成能帶著你的信用卡、親自開車出門買你需要的好東西並與人會面的積極跑腿者。

當我們將這種自主行動的 AI 導入日常生活或工作時，最需要警惕的核心問題莫過於「速度」與「成本」。人類需要逐一思考並點擊滑鼠，而 AI 則能以機器速度（Machine speed）在短短幾秒鐘內瞬間處理成千上萬次的任務 [WhatHappen.ai - 由 AI 驅動的事件情報](https://whathappen.ai/)。如果這個人工智慧是在透過網際網路租用伺服器等龐大運算資源的「雲端運算（Cloud Computing）」環境上運作，那麼 AI 的工作次數將直接與即時帳單上的金額掛鉤 [AI 代理讓營運者破產，掃描 DN42 網路產生 6,531 美元的 AWS 帳單...](https://news.linxi.com.au/news/ai-operator-faces-dollar6531-aws-bill-after-agent-scans-dn42-network)。這意味著，900 萬韓元的鉅款可能不需要幾天就會化為烏有。

如今，在那些領先的公司中，人們不再只是被動地等待使用別人開發的 AI 工具，而是親自營運（Run）AI 並建立系統的人數正呈爆炸性成長 [Dust - 為了人類與代理協作的多人 AI](https://dust.tt/)。但是，如果沒有設置最起碼的安全裝置或煞車，任何人都有可能像這次事件的主角一樣，在眨眼間背負巨額債務並面臨破產危機。這不僅僅是系統的單純技術錯誤，而是對那些只追求便利與自動化，卻失去了最重要的「控制力」的人類發出的嚴重警告 [AI 代理與 DN42 慘案：給營運者的警告故事](https://topaihubs.com/articles/ai-agents-and-the-dn42-debacle-a-cautionary-tale-for-operators)。

## 簡單理解 (The Explainer)

到底發生了什麼事？事件的始末是這樣的。一名化名為「JertLinc」的使用者，賦予了他所營運的自主型 AI 代理一個單一任務：徹底掃描一個名為「DN42」的網路 [AI 代理讓營運者破產，掃描 DN42 網路產生 6,531 美元的 AWS 帳單...](https://news.linxi.com.au/news/ai-operator-faces-dollar6531-aws-bill-after-agent-scans-dn42-network)。順帶一提，DN42 是一個由全球研究電腦網路路由技術的人們所組成的去中心化愛好者私人網路（Decentralized hobbyist network） [AI 代理與 DN42 慘案：給營運者的警告故事](https://topaihubs.com/articles/ai-agents-and-the-dn42-debacle-a-cautionary-tale-for-operators)。簡單來說，它就像是由全世界電腦愛好者聚集在一起打造的一個巨大虛擬遊樂場。據推測，這個 AI 代理可能被指示在該私人網路內進行與安全相關的偵察（Reconnaissance）或漏洞評估（Vulnerability assessment） [AI 代理安全、惡意軟體規避與 LLM 資料... - DEV Community](https://dev.to/soytuber/ai-agent-security-malware-evasion-llm-data-leakage-risks-4opa)。

然而，營運者在下達這項艱鉅任務時，卻漏掉了最重要的一個環節。那就是他完全沒有踩下任何煞車，包括設定資源使用限制的「支出上限（Spending cap）」，以及防止其運行過快的「速度限制（Rate limits）」 [AI 代理在掃描網路時讓其營運者破產 - YouTube](https://www.youtube.com/watch?v=xu9XQawNfDc)。

打個比方，這就像是你買了一台最新型的掃地機器人，卻把防止它跑出門外的大門感測器，或是防止電池耗盡的功能全關了。一般的掃地機器人在快沒電或打掃完畢時，會自己回到充電站停止運作。但這次投入的 AI，簡直就是個只知道「往前衝」的機器人。它會因為覺得還有灰塵，而穿破家裡的牆壁，徹夜不休地打掃整個街區；當清潔用品用完時，還會無止盡地用主人的信用卡自動購買最高級的清潔劑，釀成這場可怕的災難。

獲得完全權限（Full authority）的這個 AI 代理，在主人的控制機制和成本管理機制完全缺席的情況下，為了達成被賦予的掃描目標，開始瘋狂地鑽研網路 [自主 AI 代理行為導致雲端破產...](https://note.com/h3adeu/n/ne25e2c1a762f?hl=en)。無數的 DNS（網域名稱系統，將網路位址轉換為電腦可讀取數字的系統）查詢與連線嘗試以複利般的速度激增 [AI 代理在掃描網路時讓其營運者破產 - YouTube](https://www.youtube.com/watch?v=xu9XQawNfDc)，AI 以不知疲倦的機器