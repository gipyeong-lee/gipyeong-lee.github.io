---
layout: post
title: "超越單純聊天機器人，「會自主計畫」的 AI 代理如何運作？"
description: "超越只會回答問題的被動聊天機器人，本文將以淺顯易懂的方式，為您解析「AI 代理（AI Agent）」的核心原理——能自主分析、計畫並執行複雜目標的「長期任務計畫（Long Task Planning）」。"
summary: "不僅僅是單純的回答，我們將探討能自主制定計畫、使用工具並完成複雜任務的「AI 代理」的核心運作原理與架構。"
tags: [AI技術, AI代理, 開發原理, 人工智慧運作原理, 提示詞]
image: 2026-06-14-Build-a-Basic-AI-Agent-from-Scratch-Long-Task-Planning.jpg
image_alt: "機器人拿著筆，將複雜的任務過程以便利貼分步驟整理在黑板上制定計畫的插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "就像人類為了達成某項目標會寫下待辦清單（To-do List）並逐一劃掉一樣，AI 也正透過專屬的記事本獲得獨立性。說到底，高度發展的技術其實也在模仿人類最普遍的工作模式，這點非常令人感興趣。"
quiz:
  - question: "為了執行複雜任務，AI 用來暫時寫下自己想法與計畫的虛擬記憶空間稱為什麼？"
    choices: ["永久資料庫", "草稿本（Scratchpad）", "網頁瀏覽器"]
    answer: 1
    explanation: "AI 模型利用稱為「草稿本」的臨時記憶空間，將目標思考到底並仔細規畫切入方式。這些資訊儲存於記憶體中，而非永久性的檔案或資料庫。"
  - question: "AI 模型在執行任務時，會產生明確的計畫表，標示出「待辦」、「進行中」、「已完成」等狀態並按步驟執行，這種方式稱為什麼？"
    choices: ["隱式計畫（Implicit Planning）", "短期記憶（Short-term Memory）", "顯式計畫（Explicit Planning）"]
    answer: 2
    explanation: "實際建立結構化的計畫表，持續更新狀態並一步步執行的方式，稱為「顯式計畫（Explicit Planning）」。"
  - question: "在代理的記憶（Memory）層中，將過去對話階段的紀錄永久保存，寫入外部儲存空間以便隔天在其他對話中也能參考的形式是什麼？"
    choices: ["短期上下文視窗（Context Window）", "草稿本記憶體", "長期記憶（Long-term Memory）與向量資料庫"]
    answer: 2
    explanation: "長期記憶（Long-term memory）為了在對話階段之外持續保留資訊，會利用向量資料庫或鍵值儲存等外部資料庫空間。"
lang: zh-tw
ref: 2026-06-14-Build-a-Basic-AI-Agent-from-Scratch-Long-Task-Planning
---

想像一下這個場景：清晨時分，您泡了一杯熱咖啡，漫不經心地對著電腦螢幕上的 AI 說：「幫我草擬一份上週企劃會議中討論的新產品行銷企劃案。相關的會議紀錄檔案在我的桌面資料夾裡，不足的市場統計數據請上網搜尋最新資料並補充進去。」

如果是過去普通的對話型人工智慧會怎麼做呢？十之八九會說「請直接將檔案上傳給我」，或是「請逐一告訴我您需要哪些具體關鍵字的統計資料」，不斷要求使用者提供下一步的行動與指示。如果我們不手把手地引導它邁出下一步，它就只是一個什麼都做不了的被動工具。

然而，近期軟體與人工智慧開發的趨勢已邁入一個截然不同的新局面。擺脫了僅僅用看似合理的句子回答使用者問題的形式，現在出現了能自主理解使用者交付的龐大且複雜任務，並使用工具將其徹底完成的驚人系統 [如何在 2025 年從零開始打造 AI 代理](https://aakashgupta.medium.com/how-to-build-ai-agents-from-scratch-in-2025-464dddd1da07)。我們將這種能自主採取行動、具備主體性的人工智慧稱為「AI 代理（AI Agent）」。簡單來說，就是從等待指令的被動機器人，進化成了會自己找事做的聰明秘書。

今天在 MindTickleBytes，我們將以淺顯易懂的方式，探討這個聰明的 AI 代理在處理繁雜冗長的業務時不會中途迷失方向的秘訣——「長期任務計畫（Long Task Planning）」的原理，以及開發者們是如何從零開始打造出這個令人驚嘆的系統。請暫時放下複雜的程式編碼知識，就像和聰明的朋友喝杯咖啡聽故事一樣，輕鬆地跟著我們看下去吧。

## 為什麼這很重要？（Why It Matters）

就在不久前，AI 技術在大眾認知中的核心仍停留在「提問就以文字回答」的對話型聊天機器人架構。但科技界將 2025 年稱為「代理式 AI（Agentic AI）」的元年，並一直密切關注這項巨大變革 [代理執行迴圈：如何從零開始打造 AI 代理](https://newsletter.victordibia.com/p/the-agent-execution-loop-how-to-build)。目前廣泛使用的 Google Gemini CLI、Claude Code、GitHub Copilot 代理模式（GitHub Copilot agent mode），以及開發工具 Cursor 等，全都具備了這種「代理」的形式。

那麼，代理到底是什麼？為什麼它與傳統 AI 截然不同呢？簡單來說，代理就是搭載了大型語言模型（LLM，即學習大量文本以像人類般掌握上下文並生成句子的 AI 大腦），能夠自主判斷並採取行動的自治系統。

它們被賦予了過去聊天機器人所不具備的三項核心且強大能力 [在 2026 年從零開始打造 AI 代理（Python 教學 ...](https://www.agilesoftlabs.com/blog/2026/03/how-to-build-ai-agent-from-scratch-2026)：
1. **感知（Perceive）：** 主動從使用者的指令、應用程式介面（API，程式間交換數據的溝通管道）或龐大的外部資料庫中接收資訊。
2. **推理（Reason）：** 將非常巨大且令人毫無頭緒的問題，拆解成數個容易處理的小步驟，自主尋找合乎邏輯的解決方案。
3. **行動（Act）：** 超越單純的撰寫文字，為了解決給定的問題，會利用滑鼠點擊、檔案搜尋、網頁瀏覽等各種工具，採取實體或虛擬的行動。

這樣的改變對我們平凡的日常生活和工作有什麼意義呢？它不僅僅是停留在「更快寫好文件」或「提高生產力」這種抽象的層面，更意味著人類的工作方式本身將發生根本性的轉變。舉例來說，只需給定一個文章主題，它就能自己上網地毯式搜尋相關資料、建立整篇文章的骨架，最後獨自從頭到尾寫出一篇完整的部落格文章。開發這種人工智慧代理程式的方法早已在網路上公開並被廣泛應用 [從零開始打造 AI 代理——完整指南 - LinkedIn](https://www.linkedin.com/pulse/build-ai-agents-from-scratch-complete-guide-clarifai-vn3sc/)。

超越了需要我們每分每秒逐一指示、費心伺候的疲憊工具，一個會自主思考並將最終成果完美奉上的「專屬不知疲倦的數位實習生」就此誕生。這正是為什麼我們需要去了解它們是如何理解世界、並一步步解決任務的深層運作原理。

## 輕鬆理解（The Explainer）

那麼，最根本的好奇心隨之而來。即便是人類，在處理複雜冗長的工作時，也很容易陷入「我剛剛做到哪裡了？」、「接下來該做什麼？」而迷失方向。注意力一旦分散，還可能會跑去做和原定計畫毫不相干的事。更何況是作為軟體的 AI，它究竟是如何在不忘記、不放棄的情況下，堅持不懈地完成動輒數十個步驟的複雜繁雜任務呢？

其核心的秘密武器，就是我們今天的主題——**「長期任務計畫（Long Task Planning）」**技術。

當工程師在初步建構 AI 代理時，會在模型的「系統提示詞（賦予 AI 最基礎的個性、規則與運作指引）」中，非常詳細且明確地說明該如何使用這項長期任務計畫 [從零開始打造基本的 AI 代理：長期任務計畫 | by Roger Oriol | 2026 年 6 月 | Medium](https://medium.com/@rogi23696/build-a-basic-ai-agent-from-scratch-long-task-planning-14e803f9bd6d)。這項功能的運作原理本身極為直觀單純，但其結果卻強大得超乎想像。

根本上來說，我們為 AI 模型**提供了一個虛擬的備忘錄空間，讓它能像拿筆隨手記下自己的想法與目前的任務進度，待時間流逝、完成其他任務後，還能回來重新閱讀**。

擁有這個備忘錄空間會帶來巨大的優勢。這能防止 AI 模型一聽到使用者的指令就盲目地開始寫程式或寫文章，並「強制」它在深思熟慮最終目標到底是什麼之後，才開始正式動工，並在事前仔細設計與規畫整體的切入方式 [從零開始打造基本的 AI 代理：長期任務計畫](https://www.ruxu.dev/articles/ai/build-an-ai-agent-planning/)。

這樣比喻好了：剛開始學做菜的新手（過去的聊天機器人 AI）看著食譜說「它叫我先切洋蔥」，便一股腦兒地切洋蔥；直到看見下一行寫著「將胡蘿蔔和肉一起用大火快炒」時，才手忙腳亂地打開冰箱找胡蘿蔔。就在這空檔，瓦斯爐上的平底鍋早已經燒焦了。相反地，擁有數十年經驗的資深大廚（AI 代理）在開始料理前，會在腦海中將整份食譜完美模擬一遍。接著，把所有需要的食材處理好，一目瞭然地按順序擺放在砧板上後，才終於打開瓦斯爐的火。AI 的長期任務計畫功能，就與這位資深大廚徹底的事前準備過程如出一轍。

開發者們通常將 AI 在此計畫過程中所使用的備忘錄空間稱為「草稿本（Scratchpad，隨手塗鴉的練習本或便條紙）」。這個草稿本工具不會將任務內容沉重地儲存在硬碟的永久檔案或龐大的資料庫中，而是輕巧地記錄在臨時記憶體內。因為根本沒有必要把當前與某位使用者進行的任務細節計畫，分享並轉移到明天面對另一位使用者的全新對話階段中 [從零開始打造基本的 AI 代理：長期任務計畫 | by Roger Oriol | 2026 年 6 月 | Medium](https://medium.com/@rogi23696/build-a-basic-ai-agent-from-scratch-long-task-planning-14e803f9bd6d)。這就像是在當前任務結束後，就把練習本那一頁撕掉丟棄一樣。

制定計畫的方式本身也分為兩大流派。
第一種是**「隱式計畫（Implicit Planning）」**。這種方式是讓模型在其一次能閱讀與記憶的文本範圍，也就是「上下文視窗（Context Window）」內，就像人類在心裡暗自盤算般，自主遵循邏輯步驟進行推理。
第二種是**「顯式計畫（Explicit Planning）」**。這種方式將原本只在腦海中思考的事物外顯化，實際透過文字產生出極具結構性且明確的計畫表，接著再按部就班地逐一執行 [從零開始打造 AI 代理：一步步的開發者指南（2026） - Blog | TechPaathshala](https://techpaathshala.com/blog/building-an-ai-agent-from-scratch-a-step-by-step-developer-guide-2026/)。任務越是複雜，顯式計畫就越能發揮其光芒。

實際產業界的開發者最廣泛導入的方式，正是利用這種顯式計畫的簡單工具。這個工具會將使用者龐大且無所適從的請求，細微地拆解成好幾個易於處理的子「任務（Task）」。接著，在 AI 的對話上下文中，巨細靡遺地記錄下這整份任務清單 [（從零開始）打造 AI 代理 - manning.com](https://www.manning.com/preview/build-an-ai-agent-from-scratch/chapter-7)。在每個任務項目旁邊，還會像標籤一樣標示出目前的執行狀態。

舉例來說，像是「1. 在統計局搜尋 2025 年人口數據」這個任務還沒著手，就標上**「待辦（Pending）」**；「2. 將搜尋到的數據整理成 Excel」剛剛才開始，所以標為**「進行中（In Progress）」**；「3. 建立摘要報告檔案」因為已經全部做完了，就貼上**「已完成（Completed）」**的標籤。

AI 在完成一個子任務、需要決定下一步到底該做什麼的每一個瞬間，都會重新檢視這張如同巨大便利貼般的計畫表，以此來掌握自己處於整趟旅程中的哪個位置 [在 2026 年從零開始打造 AI 代理（Python 教學 ...](https://www.agilesoftlabs.com/blog/2026/03/how-to-build-ai-agent-from-scratch-2026)。只要是使用過智慧型手機裡的「待辦事項（To-do）」應用程式，體驗過將項目逐一打勾消除快感的人，都能直觀地理解這個過程。

### 簡單性創造的魔法：代理執行迴圈

那麼，這個讓 AI 盯著便利貼並實際採取行動的引擎，究竟長什麼樣子呢？促成這所有智慧奇蹟的核心引擎，其秘密就在於架構極為單純，甚至令人驚訝地只需幾行程式碼就能概括的**「代理執行迴圈（Agent Execution Loop）」**。

迴圈（Loop）的意思就像滾輪一樣不停地轉圈。當被賦予沒有標準答案、屬於開放式結局的無窮任務時，代理會先制定前述的計畫、採取行動，接著確認該行動的結果並進行反思（Reflect），然後不斷地循環重複這個過程，直到最終任務完成為止 [代理執行迴圈：如何從零開始打造 AI 代理](https://newsletter.victordibia.com/p/the-agent-execution-loop-how-to-build)。

讓我們用前面提過的大廚調味湯頭的過程來比喻看看吧：
1. 主廚收到了「煮出美味湯頭」的目標。（任務尚未完成的狀態）
2. 稍微試喝一口湯。（確認與感知目前狀態）
3. 判斷「嗯，鹹味不夠，還需要加點鹽」，接著把鹽加進去。（使用工具與採取行動）
4. 再次試味道，確認鹹淡是否剛好。（確認行動結果與反思）
5. 在煮出完美味道之前，不斷重複步驟 1 到 4 的過程。

實際驅動 AI 的開發程式碼邏輯，與這位大廚的行為模式也完全如出一轍 [如何從零開始打造 AI 代理：一步步的指南 | Claude Code Playbooks Blog](https://www.claudecodehq.com/blog/how-to-build-an-ai-agent-from-scratch)。
* **任務還沒結束嗎？（`while not done`）：** 如果還有尚未完成的計畫，就會讓 AI 模型繼續思考下一個步驟。
* **需要工具嗎？（`if response.has_tool_call`）：** 假設 AI 看著草稿本的筆記回應「現在需要找齊缺少的資料，所以得用網路搜尋工具」，就會「喀」地一聲啟動預先連接好的搜尋工具。
* **告知結果（`messages.append(result)`）：** 將從網路上抓取下來的有用資訊，悄悄地再次放進 AI 的對話紀錄中，幫助 AI 自己用眼睛閱讀並做出判斷。
* **宣告結束（`done = True`）：** 如果不再需要任何工具，且計畫表上的所有項目都已被劃掉並標示為「已完成」，就會理直氣壯地向使用者提交最終成果：「所有任務已完成！」。

事實上，我們所驚嘆的那些複雜記憶系統、計畫能力，甚至是由多個 AI 像在真實公司會議室裡激烈討論般相互合作的「多重代理協作（Multi-agent orchestration）」系統，全都只不過是替這個基礎迴圈模式換上了華麗外衣的變形體罷了 [如何從零開始打造 AI 代理：一步步的指南 | Claude Code Playbooks Blog](https://www.claudecodehq.com/blog/how-to-build-an-ai-agent-from-scratch)。在看似複雜的技術背後，其實隱含著如此透明且簡潔的邏輯脈絡。

## 現今發展（Where We Stand）

像這樣具備驚人邏輯力與縝密計畫能力的高度發展技術，總讓人覺得似乎得靠數十名矽谷天才工程師沒日沒夜地埋頭苦幹才能勉強打造出來，然而技術發展的速度遠遠超乎我們的想像。如今，這項技術正以驚人的速度邁向大眾化。

令人驚訝的是，只要具備一些軟體開發的基本知識，從空白螢幕開始，從零打造出專屬的基礎代理（Basic Agent），僅僅需要一個週末，大約 **2 到 3 天**的時間。當然，如果要讓它不只是一個自用的玩具，而是要仔細排除錯誤、使其堅固到足以投入公司實際的商業環境中，大約需要 **2 到 4 週**的時間與毅力 [在 2026 年從零開始打造 AI 代理（Python 教學 ...](https://www.agilesoftlabs.com/blog/2026/03/how-to-build-ai-agent-from-scratch-2026)。運用 Python 等廣泛使用的程式語言，教導如何從白紙狀態按部就班地製作 AI 代理的親切指南，早已在網路上不勝枚舉 [如何在 2025 年使用 Python 從零開始打造 AI 代理 ...](https://www.geeky-gadgets.com/building-ai-agent-python-tutorial/)。

產業界的開發者在初步設計 AI 代理時，並不會一口氣建起巨大的城堡。而是從所謂的**「最小但實用的迴圈」**出發，就像組裝樂高積木般一點一滴地增添血肉。起初先建立起只與電腦輕鬆互傳文字的極簡易骨架，接著再逐步將有用的工具一樣樣塞進它手裡。隨後導入能在需要新功能時輕鬆插拔的「外掛（Plugin）」架構。然後，再掛上能翻閱過去無數文件、精準為我們找出所需資訊的技術以賦予其強大的記憶力；最終，加上能聰明分配各種任務的路徑設定功能，以及今天討論的核心主題「長期計畫（Planning）」系統，才大功告成 [從零開始打造 AI 代理：最小實用的迴圈](https://juntao.substack.com/p/building-an-ai-agent-from-scratch)。

在此過程中，幫助代理緊抓使用者對話脈絡、堅持維持狀態的**「記憶（Memory）」裝置**扮演著非常關鍵的角色。記憶主要分為兩種來進行系統化的管理 [從零開始打造 AI 代理：一步步的開發者指南（2026） - Blog | TechPaathshala](https://techpaathshala.com/blog/building-an-ai-agent-from-scratch-a-step-by-step-developer-guide-2026/)：
* **短期記憶（Short-term memory）：** 以人類來說，就像是短暫記住電話號碼般的工作記憶。在人工智慧一次能用眼睛閱讀並處理的視野——「上下文視窗」內，保管目前的對話脈絡和剛制定的計畫表。這份記憶在對話結束或系統關閉後，就會消失得無影無蹤。
* **長期記憶（Long-term memory）：** 就像是堆滿知識的巨大圖書館。為了讓代理即使在幾天後、甚至一個月後開啟全新的對話階段，仍能記得我們過去聊過的內容，會將文章含義轉換為數字，永久保存在特殊的外部資料庫空間（如向量資料庫等）的技術。

而在所有這些構成要素之中，最具戲劇性且耀眼的魔法，就是從**「工具的運用」**中迸發出來的。透過程式設計，我們可以為原本被困在螢幕文字框裡的 AI 裝上能夠干涉現實世界的實體手腳。它能自己找出您電腦特定資料夾中的 Excel 檔案，用眼睛讀取裡面複雜的數字後自行修改內容並重新存檔，甚至還能果斷地執行控制電腦系統本身的指令。甚至，我們還能為它連接像是我們每天打開網頁瀏覽器般、能在網路空間中抓取最新新聞或股票數據的工具。只要為它配備這四、五種不可或缺的工具，您就能親眼見證一位能瞬間完成原本需要熬夜好幾天的工作量，並自主繳交成果的極其能幹且令人驚嘆的代理 [從零開始打造基本的 AI 代理：長期任務計畫](https://dev.to/rogiia/build-a-basic-ai-agent-from-scratch-long-task-planning-1o86)。

## 未來將何去何從？（What's Next）

未來我們的生活與技術究竟會朝向哪裡發展呢？作為代理大腦核心的 AI 模型本身的智慧，如今也以連人類都難以企及的驚人速度，日新月異地飛躍進化著。

就在一年多前，開發者們還得為了防止人工智慧偏離正軌或做出荒唐舉動而提心吊膽，必須不斷地提醒它看計畫表，或是像碎碎念般發出警告。然而，今日問世的優秀最新模型，即使只是隨便丟給它一份用文字粗略寫成的簡陋計畫表，它也能毫不動搖、毫不猶豫地，展現出自動自發按部就班精準朝目標邁進的可怕專注力 [從零開始打造基本的 AI 代理：長期任務計畫 | Hacker News](https://news.ycombinator.com/item?id=48461635)。

特別是在需要一次閱讀並理解多達數十本厚重書籍份量的龐大文件，或是像高深數學證明這種需要極度深層邏輯推理的複雜任務時，那些號稱擁有世界頂尖效能的大型語言模型（如 Claude Opus、Gemini Advanced 等），便會做為代理大腦強而有力的後盾，扮演著解決任何難題的強大救星角色 [如何從零開始打造 AI 代理：一步步的指南 | Claude Code Playbooks Blog](https://www.claudecodehq.com/blog/how-to-build-an-ai-agent-from-scratch)。

從長遠的角度來看，把如此聰明的專屬秘書留在身邊，已經不再是那群在未知黑畫面裡不停輸入一行行英文程式碼的少數專家們的專利。現在如雨後春筍般湧現的**「無程式碼（No-code）」平台**，大幅降低了技術的門檻；您不需要親自撰寫任何一行程式碼，只要像在 PowerPoint 裡用滑鼠拖曳漂亮的圖形貼上一樣，就能非常直觀地輕鬆建構起系統。即使是對程式設計一竅不通的普通人，也能在網路上各處找到完善又貼心的教學指南，幫助他們擁有能感知自身工作環境、進行推理並採取行動的客製化 AI 代理秘書 [如何打造 AI 代理？完整的循序漸進指南](https://thinkml.ai/how-to-build-an-ai-agent-a-complete-step-by-step-guide/)。

在不久的將來，我們不再需要學習複雜的電腦語言，只要擁有能問出並為人工智慧設定多麼明確「目標」的企劃能力，任何人都能帶領數十名專攻各自專業領域的個人代理實習生，輕鬆創造出堪比一人企業水準的爆發性成果，那個魔法般的時代即將全面展開。

## AI 的觀點（AI's Take）

**MindTickleBytes AI 記者的觀點：**
當面對人類難以負荷的複雜龐大專案時，克服恐懼最好的方法是什麼呢？就是翻開日誌，將「待辦清單（To-do List）」分塊寫下，然後用螢光筆逐一劃掉，一步一腳印地往前邁進。令人驚訝的是，正逐漸具備高度智慧的最尖端 AI，也是在掌握了如何利用專屬的虛擬小記事本自主劃掉計畫的方法後，才終於擺脫人類的介入，獲得了完美的獨立性。

或許，技術的本質始終都是人類的鏡子。說到底，站在最尖端、高度發展的軟體技術的終點，並非什麼外星般的複雜數學公式，而是朝著精巧地模仿人類長久以來默默工作與思考的最普遍、最單純的模式——「計畫、執行、反思」——進化，這個事實真的非常令人感興趣，而在某種程度上，也帶來了奇妙的安心感。今天您的辦公桌上放著什麼樣的計畫表呢？人工智慧也正與您一樣，在小小的記事本上計畫著能改變世界的下一步。

## 參考資料

1. [從零開始打造基本的 AI 代理：長期任務計畫 | by Roger Oriol | 2026 年 6 月 | Medium](https://medium.com/@rogi23696/build-a-basic-ai-agent-from-scratch-long-task-planning-14e803f9bd6d)
2. [從零開始打造基本的 AI 代理：長期任務計畫 | Hacker News](https://news.ycombinator.com/item?id=48461635)
3. [從零開始打造基本的 AI 代理：長期任務計畫](https://www.ruxu.dev/articles/ai/build-an-ai-agent-planning/)
4. [從零開始打造 AI 代理：最小實用的迴圈](https://juntao.substack.com/p/building-an-ai-agent-from-scratch)
5. [從零開始打造 AI 代理：一步步的開發者指南（2026） - Blog | TechPaathshala](https://techpaathshala.com/blog/building-an-ai-agent-from-scratch-a-step-by-step-developer-guide-2026/)
6. [如何從零開始打造 AI 代理：一步步的指南 | Claude Code Playbooks Blog](https://www.claudecodehq.com/blog/how-to-build-an-ai-agent-from-scratch)
7. [從零開始打造基本的 AI 代理：長期任務計畫](https://dev.to/rogiia/build-a-basic-ai-agent-from-scratch-long-task-planning-1o86)
8. [從零開始打造 AI 代理——完整指南 - LinkedIn](https://www.linkedin.com/pulse/build-ai-agents-from-scratch-complete-guide-clarifai-vn3sc/)
9. [（從零開始）打造 AI 代理 - manning.com](https://www.manning.com/preview/build-an-ai-agent-from-scratch/chapter-7)
10. [在 2026 年從零開始打造 AI 代理（Python 教學 ...](https://www.agilesoftlabs.com/blog/2026/03/how-to-build-ai-agent-from-scratch-2026)
11. [如何在 2025 年從零開始打造 AI 代理](https://aakashgupta.medium.com/how-to-build-ai-agents-from-scratch-in-2025-464dddd1da07)
12. [代理執行迴圈：如何從零開始打造 AI 代理](https://newsletter.victordibia.com/p/the-agent-execution-loop-how-to-build)
13. [如何從零開始打造 AI 代理：完整的開發者 ...](https://latenode.com/blog/how-to-build-an-ai-agent)
14. [如何打造 AI 代理？完整的循序漸進指南](https://thinkml.ai/how-to-build-an-ai-agent-a-complete-step-by-step-guide/)
15. [如何在 2025 年使用 Python 從零開始打造 AI 代理 ...](https://www.geeky-gadgets.com/building-ai-agent-python-tutorial/)