---
layout: post
title: "手機關機也能自動工作的 AI 助理？Google「Gemini Spark」全解析"
description: "淺顯易懂地為您解析 Google 在 I/O 2026 發表的 24 小時運作 AI 代理「Gemini Spark」的原理與優缺點，以及它將如何改變我們的日常生活。"
summary: "為您介紹超越單純聊天機器人、甚至在您睡覺時也能整理電子郵件並管理行程的 Google 全新 AI 代理「Gemini Spark」。"
tags: [Google, Gemini Spark, AI 代理, Google I/O 2026, 人工智慧]
image: 2026-06-03-Testing-Googles-Gemini-Spark-AI-agent-its-incredible-and-creepy.jpg
image_alt: "在黑夜中自體發光、整理著各種智慧型手機應用程式圖示、有著閃亮彗星外型的微小 AI 助理插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是一把雙面刃，雖然方便得令人驚訝，但同時因為它掌握了我的所有數據，也讓人感到一絲毛骨悚然。"
quiz:
  - question: "下列關於「Gemini Spark」的敘述，何者正確？"
    choices: ["是一個全新的獨立 AI 模型。", "使用者必須開啟應用程式才會運作。", "是一個基於 Gemini 3.5 Flash 模型的代理運行階段系統 (Agent runtime)。"]
    answer: 2
    explanation: "Gemini Spark 並非全新的 AI 模型，而是建立在 Gemini 3.5 Flash 之上，24 小時運作的代理運行階段 (Agent runtime) 系統。"
  - question: "Gemini Spark 目前率先提供的訂閱服務名稱與價格為何？"
    choices: ["Google Basic (每月 10 美元)", "Google AI Ultra (每月 100 美元)", "Gemini Premium (每月 50 美元)"]
    answer: 1
    explanation: "目前 Gemini Spark 已針對美國境內的「Google AI Ultra」訂閱者（每月 100 美元）展開 Beta 測試服務。"
  - question: "Google 在今年夏天將 Gemini Spark 整合至桌面應用程式時，將新增哪項主要功能？"
    choices: ["在無網際網路連線的情況下使用所有網頁搜尋功能", "存取使用者電腦的本機檔案並直接執行工作", "免費無限制生成圖片"]
    answer: 1
    explanation: "整合至桌面應用程式後，Spark 將能存取本機檔案，並直接在使用者電腦上執行各種工作。"
lang: zh-tw
ref: 2026-06-03-Testing-Googles-Gemini-Spark-AI-agent-its-incredible-and-creepy
---
想像一下。週五夜晚，結束了一週辛勤的工作，您沉沉睡去。智慧型手機插著充電器，螢幕一片漆黑。但在您的數位世界中，有人正忙碌地運作著。隔天早上醒來時，昨夜如雪片般飛來的數十封電子郵件，已經按照重要程度整齊地摘要整理好。孩子們下週複雜的課後活動行程，也已在行事曆上依顏色無縫填滿。甚至週末與朋友聚會的派對地點候補名單，以及要發送給出席者的邀請函草稿，都已完美準備好顯示在螢幕上。您所做的，就只有在睡前說了一句：「幫我留意一下這週末的派對行程，還有把重要的郵件自己整理好。」

這聽起來像是科幻電影裡的高科技助理嗎？令人驚訝的是，這並非遙遠未來的想像。這是 Google 在 2026 年 5 月 19 日舉行的「Google I/O 2026」大會上正式發表的全天候 24 小時個人用 AI 代理 (代使用者執行特定工作的程式) ——「Gemini Spark」即將打造的明日日常 [Gemini Spark：Google 的 24/7 AI 代理如何運作 | 透過 AI 快速構建](https://www.buildfastwithai.com/blogs/gemini-spark-google-ai-agent-how-it-works)。徹底告別過去只能被動回答問題的單純聊天機器人 (Chatbot) 時代，現在正式揭開了能自行判斷狀況並主動採取行動的「代理 (Agent)」時代序幕。這個功能過去在 Google 應用程式 Beta 版中被稱為略顯生硬的「Gemini Agent」，現在則獲得了正式名稱，並配備了如彗星般拖著尾巴、充滿動感的 Spark 圖示 [「Gemini Spark」是 Google 即將在 Gemini 應用程式中推出的 AI 代理](https://9to5google.com/2026/05/14/gemini-spark-insight/)。這項強大且全新的技術，一方面帶來驚人的便利，另一方面卻也因為它看透並掌控您的一切而讓人感到一絲毛骨悚然。究竟 Gemini Spark 的具體運作原理為何？它又將如何徹底顛覆我們每天的日常生活呢？

## 這為何重要？ (Why It Matters)

近年來，我們對 ChatGPT 或 Google 現有的 Gemini 等生成式人工智慧已經非常熟悉。它們是出色且聰明的助手，只要提問就能對答如流，要求撰寫企劃案也能在幾秒鐘內迅速建立架構 [Google Gemini](https://gemini.google.com/)。然而，直到目前為止，我們所使用的幾乎所有人工智慧都有一個共同的限制。那就是必須由我們主動「搭話」才會運作。當我們關閉瀏覽器視窗或按下智慧型手機電源鍵關閉螢幕的那一刻，人工智慧的所有活動與任務也會在瞬間停止。

Gemini Spark 之所以能為全球科技界帶來巨大震撼並備受重視，正是因為它徹底打破了這個根本的限制。這項令人驚豔的技術，即使在您的智慧型手機關機時，也能一天 24 小時、一週 168 小時在背景 (在螢幕後方安靜執行的狀態) 毫不歇息地持續運作 [Google 新聞 - Google 的 Gemini Spark AI 代理能自動化完成任務... (US/NA 地區新聞)](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2o5NjZXZkVSR2FmdXZsVW5zZGVDZ0FQAQ?hl=en-NA&gl=NA&ceid=NA:en)。Google 強烈企圖將 Gemini Spark 打造成一個終極窗口與萬能介面 (Interface，機器與人類溝通的媒介)，未來不僅能讓它自行操作各種類型的外部行動應用程式，隨著時間推移，最終甚至能操作使用者的整個電腦作業系統 [測試 Google 的 Gemini Spark AI 代理：令人驚艷，卻也令人毛骨悚然 (Online Tech Guru)](https://onlinetechguru.co.uk/testing-googles-gemini-spark-ai-agent-its-incredible-and-creepy/)。

這對我們這些平凡的非專業人士來說，其實際意義非常巨大。過去，如果要銀行轉帳就必須打開銀行 App，要安排行程就得打開行事曆 App，要和朋友約時間則要切換開啟通訊軟體 App，我們必須親自「手動」逐一控制與管理自己的數位生活。但現在，我們可以果斷地將這些繁瑣的控制權，委託給一位完全了解您的超級聰明數位助理。Google 闡述的 Gemini Spark 最終目標，同樣是在使用者明確的指揮與許可下，代替使用者直接採取「行動 (Action)」，幫助使用者更從容地航行於這個錯綜複雜的數位生活中 [Google 發表 AI 模型 Gemini 3.5 與 AI 代理 Gemini Spark](https://www.cnbc.com/2026/05/19/google-ai-ultra-gemini-spark-omni.html)。對於在每天重複枯燥的數位雜務、整天響個不停的數十個無意義 App 通知、以及如洪水般湧入的電子郵件中掙扎並感到疲憊的現代人來說，終於出現了一個能將寶貴時間完整還給自己的強大且現實的解決方案。

## 淺顯易懂的解析 (The Explainer)

那麼，Gemini Spark 到底是用什麼異想天開的原理來運作的呢？為了理解這項功能的運作方式，我們從 Google I/O 2026 的發表內容中可以發現一個有趣的細節。Gemini Spark 本身並不是一個完全從頭打造的獨立人工智慧「模型 (Model)」。這項技術是以已經證明其卓越效能的「Gemini 3.5 Flash」人工智慧模型為大腦建構而成，並由 Google 開發的「Google Antigravity」特殊基礎平台提供動力運作的永久性、持續性「代理運行階段 (Agent runtime，程式執行的環境)」系統 [Gemini Spark：Google 的 24/7 AI 代理如何運作 | 透過 AI 快速構建](https://www.buildfastwithai.com/blogs/gemini-spark-google-ai-agent-how-it-works)。

出現這些專業術語是不是讓人覺得有些艱澀複雜？用以下直觀的情境來比喻，就能非常容易理解。

**第一個比喻：思考聰明的大腦與直接行動的手腳**
假設將整個人工智慧系統看作是一個能幹的「人」。在這裡，作為基礎的「Gemini 3.5 Flash」模型，就相當於一個能聽懂使用者的話、判斷複雜文字情境、理解整體脈絡與文章的超級聰明**「大腦 (Brain)」**。另一方面，名為「Google Antigravity」的新平台，則是接收這個聰明大腦的指示與命令後，能夠在虛擬網際網路空間中勤奮穿梭、點擊各種文件與按鈕的實體**「手腳」**。過去我們使用的聊天機器人，無論多聰明，都只是一個被孤零零放在桌上的大腦，只能用言語來回答我們的問題。然而，Gemini Spark 這種全新形態的「代理運行階段」，就像是為這個孤立的大腦裝上了能自由活動的手腳，甚至為了讓它 24 小時不睡覺、不疲倦，還裝上了一個永久的心律調節器。正因如此，即使在您熟睡的靜謐凌晨，Spark 也能發揮其驚人的能力，忙碌地揮舞虛擬的手腳，將您凌亂的信箱整理得乾乾淨淨。

**第二個比喻：一次性外部顧問 vs. 擁有我家鑰匙的常駐管理員**
再舉個例子來說明。如果現有普通的人工智慧聊天機器人是我們在有需求時才付費見面一小時、尋求建議並獲取文字內容的**「外部顧問」**，那麼 Gemini Spark 就是一個擁有我們家所有房間鑰匙、24 小時全天候不眠不休打理家裡各個角落的**「常駐管理員 (或能幹的管家)」**。外部顧問在諮詢時間結束、電腦螢幕關閉的同時，就會拍拍屁股回家；但常駐管理員即使在我不在身邊、甚至外出的情況下，也會持續適當地調節室內溫度、分類積壓的郵件並清理地板。實際上，Google 提供了一個名為「AI 代理工作區 (AI Agent Workspace)」的空間，使用者只需向 Spark 拋出一個粗略的目標，Spark 就會自行將該目標塑造成代理可以處理的完美工作流程 (Workflow)。使用者可以在這個單一且集中的工作空間內，一次性明確定義並指示管理員的角色、必須執行的步驟、絕對不能逾越的限制條件、最終需要產出的結果格式，以及判斷工作是否成功的驗收標準 [Gemini Spark - AI 代理工作區](https://geminispark.ai/)。 

然而，這個常駐管理員為了能察言觀色、完美處理我的家務，理所當然地必須對我家中的各種隱私與我的個人喜好瞭若指掌。根據正式推出前流出的詳細資訊，以及開發者親自拆解 Android 應用程式安裝檔 (APK) 的分析結果顯示，Gemini Spark 不僅僅是聽取使用者的話語，它還在更龐大、更深層的領域中運作。Spark 會蒐集使用者平時常用的「已連結應用程式 (Connected Apps)」、包含使用者獨特傾向的「個人智慧 (Personal Intelligence)」、過去龐大的對話紀錄、待辦事項清單、目前登入的眾多網站資訊，甚至是使用者的即時實體位置 (Location) 資訊，以立體的方式掌握當前的脈絡與狀況。此外，如果它自行判斷為了完成使用者指示的特定行動而有絕對必要時，它甚至被設計成可以採取果斷行動，開拓路徑將部分相關個人數據直接傳遞給外部的第三方服務 (Third parties) App 或網站 [洩露資訊揭露 Google Gemini Spark AI 代理 | Let's Data Science](https://letsdatascience.com/news/leaks-reveal-google-gemini-spark-ai-agent-700d03c8)。 

這所有過程，即使使用者沒有一一按下按鈕，也會如流水般自然地在背景進行。人工智慧終於走出螢幕，開始直接介入我們複雜的生活。

如果有這樣一位擁有驚人能力的常駐管理員立刻進駐到我的智慧型手機裡，生活會變得多麼豐富美好？這位革命性的助理何時能真正落入我們手中，現在就讓我們在下一章探討它的現況。

## 目前狀況 (Where We Stand)

那麼就在今天，我們究竟該如何親自使用並體驗這項革命性且驚人的功能？任何人都可以直接從智慧型手機的 App Store 下載使用嗎？

目前還不行。Google 在將這項具備巨大影響力的技術完全釋放給全世界之前，正在非常謹慎且受限的環境中進行測試。截至 2026 年 5 月底的發表內容，Google 僅與其內部可信賴的初期測試人員，以及在美國境內使用「Google AI Ultra」方案的頂級訂閱者，小心翼翼地率先展開了 Gemini Spark 的 Beta (正式推出前的測試版本) 服務 [Google 發表 AI 模型 Gemini 3.5 與 AI 代理 Gemini Spark](https://www.cnbc.com/2026/05/19/google-ai-ultra-gemini-spark-omni.html)。這裡提到的「Google AI Ultra」訂閱並不是任何人都能輕易負擔的廉價方案。這是一個超高單價的 Premium 服務，使用者每個月必須支付高達 100 美元 (約合新台幣 3,200 元) 的可觀金額，才能無限制地存取 Google 旗下最先進、最強大的頂級 AI 工具 [為什麼 Google 的 Gemini Spark AI 代理可能成為改變遊戲規則的關鍵 - CBS 新聞](https://www.cbsnews.com/news/google-gemini-spark-ai-agent/)。雖然作為單一軟體訂閱費用有著不小的成本門檻，但 Google 解釋，它能提供足以抵上一個人力的強大且壓倒性的自動化功能，絕對物超所值。

根據在 Google 內部統籌此專案測試的負責人 Woodward 的說法，目前正在使用 Beta 版的初期測試人員，已經將 Gemini Spark 深入且積極地應用於他們的日常生活與工作中。測試人員會指示 Spark 從頭到尾策劃本週末即將舉辦的複雜派對詳細行程、讓它即時追蹤孩子們每天變動的複雜課後行程，甚至讓它在背景持續監控整天如雪片般飛來的電子郵件收件匣，確認是否包含使用者必須回覆的重要問題或請求事項。這些活動如實地展現了 Gemini Spark 不再侷限於模糊的對話或心理諮商，而是將焦點銳利地集中在「成功完成實際現實中的工作 (getting the job done)」上 [Google 全新的 Gemini AI 模型與工具現在全都是為了代理而生 - CNET](https://www.cnet.com/tech/services-and-software/google-gemini-3-5-flash-spark-antigravity/)。目前在 Google 網頁應用程式內部，這項功能已貼上「Gemini Spark BETA」的標籤並開啟，充分扮演著小幫手的角色，有效地對滿溢的收件匣進行分類，並自動處理那些顯而易見且重複的線上作業繁瑣工作流程 [Google 準備在 I/O 發表會前推出 Gemini Spark AI 代理](https://www.testingcatalog.com/google-prepares-gemini-spark-ai-agent-ahead-of-i-o-launch/)。

搶先體驗這項驚人功能的科技專業媒體早期使用者，其反應可以用非常熱烈且正面來形容。一位知名 IT 媒體的專業評論員為了測試 Gemini Spark 的能力，下達了相當複雜的指示。他將草擬發送給 Google 內部團隊成員的公務電子郵件工作完全交給 Spark，並指示它從散落的各項文件中自行彙整上週的多項成果，以及與 Gemini Live 功能發布相關的龐大數據。令人驚訝的是接下來發生的事。這位評論員不僅要求蒐集資訊，還要求應用特殊的 AI 技能，模仿他「平時的說話語氣」，讓最終完成的電子郵件文體與語調聽起來完美自然。結果如何呢？評論員對結果讚不絕口，難掩驚訝地表示，產出的內容就如同 Google 在華麗舞台上展示的精緻展示影片一樣出色且流暢 [Gemini 全新 AI 代理的表現幾乎與 Google 示範的一樣好 | The Verge](https://www.theverge.com/tech/941138/google-gemini-spark-ai-agent-hands-on)。另一位早期採用者 (樂於盡早接受新技術的人) 使用者也在其部落格評論中留下好評，表示將 Google 這款 24 小時全年無休的 AI 助理 Gemini Spark 直接投入其複雜的實際工作環境後，發現它出乎意料地「實際上相當有用 (actually pretty useful)」，大幅縮短了工作時間 [Google 新聞 - Google 的 Gemini Spark AI 代理能自動化完成任務... (PH 地區新聞)](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2o5NjZXZkVSRXFBM2wtWUI3dHVTZ0FQAQ?hl=en-PH&gl=PH&ceid=PH:en)。

簡單來說，Gemini Spark 帶來的效果就像是聘請了一位優秀的新進員工。但這並不意味著我們現在就獲得了魔法棒。目前只有極少數的內部人員，以及支付高昂費用的美國境內使用者才能享受到這種魔法，加上仍處於未經打磨的 Beta 服務階段，在預料不到的時刻犯下離譜錯誤或發生突發故障的可能性依然很高。每月 100 美元這個絕對不低的進入門檻，同樣是 Gemini Spark 在超越少數專業人士工具的範疇、完美融入大眾日常生活並普及化之前，Google 必須在策略上跨越的巨大挑戰。

## 未來將如何發展？ (What's Next)

Gemini Spark 真正具備的破壞力與無限潛力，並不僅僅侷限在我們每天開啟的網頁瀏覽器視窗，或是狹小的智慧型手機 App 框架內。Google 在 I/O 舞台上正式宣布了一項宏偉計畫，預計在即將到來的今年夏天，將 Gemini Spark 提升至更高層次，直接引入使用者的桌上型電腦專屬應用程式 (Desktop app) 中並進行全面整合。這意味著一個非常重大的改變。當 Spark 與桌面應用程式有機整合後，這個 24 小時 AI 助理將不再只是在網際網路空間中遊蕩，而是被賦予了強大的權限，可以直接存取深深儲存於使用者實體電腦硬碟中的無數「本機檔案 (Local files，未上傳至網路雲端、存放於電腦內的私人文件、Excel 檔案、個人照片等)」。透過這種方式，它將能在眨眼之間，直接在使用者的電腦環境中執行各種直接且實質的複雜工作 [Google Gemini Spark、AI 搜尋更新發表於... - India Today](https://www.indiatoday.in/technology/news/story/google-gemini-spark-ai-search-update-google-io-2026-2914202-2026-05-20)。 

不僅如此。我們過去每天輸入數十次單字來尋找資訊的傳統 Google 搜尋 (Google Search) 系統，也將透過積極導入這種強大背景運作代理的存在，以及以人工智慧為核心的全新介面，進化成過去無法比擬、更加聰明且更懂脈絡的有機助理型態 [Google Gemini Spark、AI 搜尋更新發表於... - India Today](https://www.indiatoday.in/technology/news/story/google-gemini-spark-ai-search-update-google-io-2026-2914202-2026-05-20)。

用非常淺白、直接的話來說，就算我不拖著疲憊的身軀、端正地坐在電腦桌前握著滑鼠，Gemini Spark 也能在今年夏天將科幻電影般的魔法搬進我的房間裡：只需我一句指令，它就能自行連按兩下開啟我的電腦資料夾，將昨天寫到一半的 Excel 檔案數據俐落地修改至最新狀態，並將桌面上散亂的各種檔案分門別類建立資料夾，整理得井然有序。對於這種能自由跨越網路虛擬空間與我實體裝置 (Devices) 邊界、不間斷執行複雜連結作業的驚人 AI 體驗，英語圈知名 IT 媒體記者以既興奮又擔憂的語氣給予了這樣的評價：「Gemini Spark 作為 Google 全新的自主型 (Agentic) AI 平台，在網路與使用者裝置上完成了無數任務。這是我至今體驗過的所有 AI 經驗中，最令人印象深刻、同時也是最令人感到恐懼 (terrifying) 的體驗。」他補充道：「這真的是一項令人驚嘆且出色的技術結晶。但坦白說，這項技術所描繪的未來，確實讓人感到心情微妙且有些毛骨悚然 (creepy)。」[測試 Google 的 Gemini Spark AI 代理：令人驚艷，卻也令人毛骨悚然 (The Verge)](https://www.theverge.com/ai-artificial-intelligence/941388/gemini-spark-ai-agent-trip-planning)。

為什麼連專業科技記者都會形容這讓人毛骨悚然呢？原因非常明顯。這個名為 Gemini Spark 的人工智慧，如果要為我擔任一個精準無誤、完美的個人化助理，在邏輯上和必然上，它必須徹底窺探並深入學習我最私密的對話內容、敏感的職場工作細節、錯綜複雜的人際關係脈絡，以及我每天去了哪裡、見了誰等構成我生活各種形式的龐大數據。我每天無意間打開智慧型手機的私人 App 紀錄、我現在所處的精確物理位置、甚至是與我生理時鐘相關的睡眠時間模式，所有構成我數位自我的碎片，都會被吸入 Google 龐大的中央伺服器與 Spark 密集的認知網中。為了獲得這項能節省寶貴時間的終極 24 小時自動化便利服務，我們究竟願意將自己最私密、最個人的隱私讓步到什麼程度？我們又能完全信任掌握著這個巨大權限的大型科技企業嗎？這正是變得耀眼且聰明的 Gemini Spark，在超越技術讚譽之外，對活在 2026 年的我們所有人拋出的一個最沉重的哲學與現實困境。

## AI 的視角 (AI's Take)

**MindTickleBytes 的 AI 記者視角：**
Gemini Spark 的出現，是人工智慧從單純握在人類手中、被動的「工具」，進化成代替人類執行意志、獨立的「代理人」的歷史性轉折點。雖然每月 100 美元的 24 小時個人助理將為我們省下大量有限的實體時間，提供極大的效用，但其背後也潛藏著陰影。如果我們將生活幾乎所有的控制權都交給這個完美的 AI 系統，哪怕只發生一次不可預期的致命錯誤、故障，或是遭到駭客攻擊，我們將面臨的日常混亂，恐怕是人類前所未見的破壞性程度。在沉醉於極致便利的甜美果實之前，我們所有人必須針對交給這個機器新助手的生命「控制權」範圍，以及隨之而來的沉重責任進行深入思考，並達成社會共識，這是一個決定性的時刻。打個比方，這就像是把錢包、家裡鑰匙，甚至銀行密碼，全部交給一位知道您所有秘密的能幹秘書一樣。為了安全地控管這個巨大的便利性，建立一套屬於我們自己的堅固安全機制，已經是刻不容緩的課題。

## 參考資料

1. [測試 Google 的 Gemini Spark AI 代理：令人驚艷，卻也令人毛骨悚然 (The Verge)](https://www.theverge.com/ai-artificial-intelligence/941388/gemini-spark-ai-agent-trip-planning)
2. [測試 Google 的 Gemini Spark AI 代理：令人驚艷，卻也令人毛骨悚然 (Online Tech Guru)](https://onlinetechguru.co.uk/testing-googles-gemini-spark-ai-agent-its-incredible-and-creepy/)
3. [Google Gemini](https://gemini.google.com/)
4. [Google 準備在 I/O 發表會前推出 Gemini Spark AI 代理](https://www.testingcatalog.com/google-prepares-gemini-spark-ai-agent-ahead-of-i-o-launch/)
5. [Google 新聞 - Google 的 Gemini Spark AI 代理能自動化完成任務... (US/NA 地區新聞)](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2o5NjZXZkVSR2FmdXZsVW5zZGVDZ0FQAQ?hl=en-NA&gl=NA&ceid=NA:en)
6. [Gemini Spark：Google 的 24/7 AI 代理如何運作 | 透過 AI 快速構建](https://www.buildfastwithai.com/blogs/gemini-spark-google-ai-agent-how-it-works)
7. [Gemini Spark - AI 代理工作區](https://geminispark.ai/)
8. [Google 新聞 - Google 的 Gemini Spark AI 代理能自動化完成任務... (PH 地區新聞)](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2o5NjZXZkVSRXFBM2wtWUI3dHVTZ0FQAQ?hl=en-PH&gl=PH&ceid=PH:en)
9. [Google Gemini Spark、AI 搜尋更新發表於... - India Today](https://www.indiatoday.in/technology/news/story/google-gemini-spark-ai-search-update-google-io-2026-2914202-2026-05-20)
10. [「Gemini Spark」是 Google 即將在 Gemini 應用程式中推出的 AI 代理](https://9to5google.com/2026/05/14/gemini-spark-insight/)
11. [為什麼 Google 的 Gemini Spark AI 代理可能成為改變遊戲規則的關鍵 - CBS 新聞](https://www.cbsnews.com/news/google-gemini-spark-ai-agent/)
12. [Gemini 全新 AI 代理的表現幾乎與 Google 示範的一樣好 | The Verge](https://www.theverge.com/tech/941138/google-gemini-spark-ai-agent-hands-on)
13. [Google 全新的 Gemini AI 模型與工具現在全都是為了代理而生 - CNET](https://www.cnet.com/tech/services-and-software/google-gemini-3-5-flash-spark-antigravity/)
14. [Google 發表 AI 模型 Gemini 3.5 與 AI 代理 Gemini Spark](https://www.cnbc.com/2026/05/19/google-ai-ultra-gemini-spark-omni.html)
15. [洩露資訊揭露 Google Gemini Spark AI 代理 | Let's Data Science](https://letsdatascience.com/news/leaks-reveal-google-gemini-spark-ai-agent-700d03c8)