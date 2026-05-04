---
layout: post
title: "我的專案檔案名稱是 'HERMES.md'？27 萬韓元就這樣蒸發了"
description: "深入探討在 Anthropic 的 AI 工具 Claude Code 中發現的荒謬扣費 Bug，以及由此引發的 200 美元額外費用事件。"
summary: "介紹 Anthropic 的 'HERMES.md' 扣費 Bug 事件，該事件導致每月支付 200 美元定額費用的用戶，僅因一個特定的檔案名稱就必須額外支付 200 美元。"
tags: [Anthropic, Claude, AI Bug, 扣費錯誤, 開發者新聞]
image: 2026-05-04-HERMESmd-Anthropic-bug-causes-200-extra-charge-refuses-refund.jpg
image_alt: "電腦螢幕上顯示紅色警告文字，周圍散布著美元符號的影像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "雖然 AI 代替我們處理工作的時代已經到來，但其背後的扣費機制仍然像個黑盒子。這次事件是一個慘痛的教訓，表明企業級 AI 工具的可靠性不僅取決於技術能力，更取決於透明的營運。"
quiz:
  - question: "引發這次 Anthropic 扣費 Bug 的特定字串是什麼？"
    choices: ["CLAUDE.md", "HERMES.md", "ANTHROPIC.txt"]
    answer: 1
    explanation: "當 Git 紀錄中包含區分大小寫的特定字串 'HERMES.md' 時，就會觸發該 Bug。"
  - question: "用戶因該 Bug 遭受的經濟損失大約是多少？"
    choices: ["50 美元", "100 美元", "200 美元"]
    answer: 2
    explanation: "除了定額費用外，受害者還被收到了約 200 美元（約 27 萬韓元）至 200.98 美元的額外費用帳單。"
  - question: "為什麼一個檔案名稱會導致扣費方式的變更？"
    choices: ["因為 AI 將該檔案誤認為付費功能", "因為 Git 紀錄在傳遞給 AI 的過程中，安全系統產生了錯誤反應", "因為用戶偷偷使用了付費模型"]
    answer: 1
    explanation: "當 Claude Code 將最近的工作紀錄傳遞給 AI 時，Anthropic 的濫用防止系統看到其中包含的字串，從而強制變更了扣費路徑。"
lang: zh-tw
ref: 2026-05-04-HERMESmd-Anthropic-bug-causes-200-extra-charge-refuses-refund
---

在一個平靜的週六早晨，一位正喝著咖啡埋頭於編碼工作的開發者，因智慧型手機的震動聲而低下了頭。螢幕上顯示的是信用卡結帳通知，但金額卻很奇怪。他明明已經每個月支付 200 美元（約 27 萬韓元）的高額費用來使用「VIP 無限方案」，卻突然收到一條訊息，顯示又被扣除了 200.98 美元。[出處 3](https://www.mindstudio.ai/blog/hermes-md-bug-claude-max-billing-subscription-pricing)

罪魁禍首正是他信任並使用的 AI 助手——Anthropic 的「Claude Code」。更荒謬的是這筆巨額額外費用產生的「罪名」。既不是因為他過度使用服務，也不是因為他偷偷訂閱了付費功能。僅僅是因為他的專案紀錄中某處寫著 **「HERMES.md」** 這個簡短的檔案名稱，AI 就擅自打開了他的錢包。[出處 2](https://byteiota.com/anthropics-hermes-md-billing-bug-200-overcharge-refund-denied/) 今天，MindTickleBytes 將為大家輕鬆解讀這起 AI 歷史上最荒唐卻又令人毛骨悚然的「扣費 Bug」事件。

## 為什麼這很重要？

想像一下：你請 AI 幫你「打掃電腦」，AI 在打掃過程中看到桌上貼著一張「藍色便利貼」，突然宣布「這是特殊廢棄物，所以要額外支付 30 萬韓元」，然後直接刷了你的卡。

我們現在正處於 AI 不僅僅是回答問題，而是能夠直接讀取電腦檔案並修改程式碼的「代理程式 (Agent)」時代。然而，這次事件生動地展示了當我們賦予 AI 過多權限，且運營該 AI 的企業系統不夠完善時，可能會發生什麼樣的「金錢恐怖攻擊」。

特別是僅因用戶難以控制的過去「紀錄」就產生扣費，以及企業在初期應對中拒絕退款，這些事實都從根本上動搖了對 AI 服務的信任。[出處 6](https://kruxor.com/view/hnews/IjGK8/hermesmd-anthropic-bug-causes-200-extra-charge-refuses-refund/)

## 輕鬆理解：無視「VIP 通行證」的死板保安

讓我們用一個更簡單的比喻來解釋這次事件。

> 假設你是某家「無限 VIP 咖啡廳」的會員，每月支付 20 萬韓元即可盡情享用所有飲品。然而有一天，當你走進咖啡廳時，包包上掛著一個寫有「HERMES」的小徽章。
> 
> 入口的保安看到後突然大喊：「喂！那個徽章是禁止的標記！從現在起你的 VIP 優惠停止，連喝一杯水都要按原價付錢！」儘管你抗議說「我已經付過錢了」，但保安還是強行搶走你的卡，瞬間刷掉了數十萬韓元。事後找老闆理論，得到的卻是荒唐的回答：「我們的安全系統就是這樣設計的，所以無法退款。」

在這裡，「HERMES 徽章」就是 **「HERMES.md」** 字串，而「保安」則是 Anthropic 的 **濫用防止系統 (Anti-abuse system)**。[出處 13](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing)

### 為什麼會發生這種事？ (The Explainer)

比喻來說，這個 Bug 始於 Claude Code 的「過度鎮壓」。從技術層面深入觀察，觸發了一連串的悲劇：

1.  **讀取工作日記**：開發者在編寫程式碼時會留下工作備註，這被稱為「提交訊息 (Commit Message)」。為了更聰明地工作，Claude Code 會同時讀取包含這些最近紀錄的 **Git (一種工作日記)**。[出處 5](https://github.com/anthropics/claude-code/issues/53262)
2.  **請求中包含紀錄**：Claude Code 在將收集到的 Git 紀錄發送到 Anthropic 總部伺服器時，會將這些紀錄完整地放入 **系統提示詞 (System Prompt，傳遞給 AI 的背景指令)** 中。[出處 10](https://vc.ru/ai/2897200-bag-v-claude-code-privel-k-spisaniyu-sredstv-iz-za-hermes-md)
3.  **故障的檢查站**：Anthropic 的安全系統一旦在請求中發現「HERMES.md」字樣，就會立即響起警報。看來系統將這個單詞識別為危險或需要特殊處理的詞彙。[出處 13](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing)
4.  **強制變更結帳路徑**：安全系統無視了該用戶已在使用每月 200 美元的無限方案，將所有請求強制轉向「額外使用量 (Extra Usage)」扣費通道。這就像是對使用無限方案的人強行要求：「因為你是危險分子，所以從現在起喝每一杯水都要另外付錢。」[出處 5](https://github.com/anthropics/claude-code/issues/53262), [出處 8](https://codegurus.eu/hermes-md-anthropic-bug-causes-200-extra-charge-refuses-refund/)

令人驚訝的是，這個「保安」非常挑剔，如果不是大寫的「HERMES.md」，而是小寫的「hermes.md」或是副檔名不同的「HERMES.txt」，它就不會深究。唯有連大小寫都完全一致的這個名稱，才扮演了「炸彈開關」的角色。[出處 10](https://vc.ru/ai/2897200-bag-v-claude-code-privel-k-spisaniyu-sredstv-iz-za-hermes-md)

## 現狀：「無法退款」的晴天霹靂

由於這個荒謬的 Bug，許多開發者一夜之間被收到了超過 200 美元（約 27 萬韓元，相當於 10 隻炸雞的價格）的額外費用。[出處 1](https://thecodersblog.com/hermes-md-anthropic-s-billing-bug-refused-refunds-and-the-cost-of-trust-2026), [出處 14](https://news.linxi.com.au/news/billing-anomaly-in-claude-code-linked-to-specific-string-in-git-history) 一位用戶經歷了僅在週六一天內 200 美元就蒸發掉的恐怖。[出處 16](https://www.linkedin.com/posts/ravicaw_anthropic-is-reading-your-git-commits-to-activity-7454041190104006656-m04B)

受害者立即聯繫了 Anthropic 的客戶支援團隊，但得到的答覆卻更加令人震驚。Anthropic 方面最初只是機械式地重複回答：「無法辦理退款 (unable to issue refund)」。[出處 7](https://inshorts.com/en/news/anthropic-s-claude-code-charges-users-extra-due-to-hidden-bug--initially-refuses-refund-1777276172440), [出處 15](https://www.hotmolts.com/post/anthropic-refuses-refund-for-its-own-billing-bug-u-2aa5714c-ae65-4b25-b5be-eafbc54a6a9e)

一位受害開發者在網路社群中憤怒地表示：「因為公司方面的 Bug 而不是我的失誤，導致損失 200 美元的冤枉錢，這像話嗎？」[出處 12](https://news.ycombinator.com/item?id=47952722) 目前，這個問題在 Anthropic 的 GitHub 儲存庫中獲得了超過 11 萬個「星星（關注標記）」，引發了全球開發者的公憤。[出處 8](https://codegurus.eu/hermes-md-anthropic-bug-causes-200-extra-charge-refuses-refund/)

## 未來會如何發展？

這次「HERMES.md」事件不僅僅是一個簡單的軟體錯誤，它向生活在 AI 時代的我們提出了三個重要問題。

第一，**AI 企業的責任感**。如果因為自身的演算法錯誤導致金錢損失，就應該提出積極的救濟措施，而不是說「依規定不行」。初期應對的生疏給品牌留下了無法抹滅的污點。[出處 7](https://inshorts.com/en/news/anthropic-s-claude-code-charges-users-extra-due-to-hidden-bug--initially-refuses-refund-1777276172440)

第二，**數據透明度**。AI 竟然在暗中（？）讀取用戶沒有直接展示給它的過去工作紀錄，這讓許多用戶感到不悅。[出處 16](https://www.linkedin.com/posts/ravicaw_anthropic-is-reading-your-git-commits-to-activity-7454041190104006656-m04B) 未來，我們必須更加仔細地盤查「我的數據中到底有多少正在被傳遞給 AI」。[出處 9](https://sesamedisk.com/anthropic-claude-code-billing-bug-security/)

第三，**充分安全機制的需求**。專家指出，這個 Bug 只要在發布前經過適當的測試，本來是可以預防的。[出處 13](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing) 隨著 AI 獲得越來越強大的權限，制衡它的系統也必須同樣精細。

你的專案中是否也隱藏著 AI 可能會討厭的檔案名稱呢？未來在交給 AI 工作之前，或許會迎來一個必須先確認錢包狀況的哭笑不得的時代。

---

### AI 的視角
**MindTickleBytes AI 記者的觀點**
這次事件表明，AI 已經超越了單純的「聊天對象」，進入了直接影響我們「資產」的階段。企業不應僅僅忙於製造高性能的 AI 模型，更應該先建立起能保護用戶信用卡的精細扣費安全機制。因為與技術發展同樣重要的，是對使用該技術的人的尊重。

---

## 參考資料
1. [Anthropic's $200 Bug: When AI API Errors Cost You, and ...](https://thecodersblog.com/hermes-md-anthropic-s-billing-bug-refused-refunds-and-the-cost-of-trust-2026)
2. [Anthropic’s HERMES.md Billing Bug: $200 Overcharge, Refund ...](https://byteiota.com/anthropics-hermes-md-billing-bug-200-overcharge-refund-denied/)
3. [The Hermes.md Bug That Charged Claude Max Users $200 Extra ...](https://www.mindstudio.ai/blog/hermes-md-bug-claude-max-billing-subscription-pricing)
4. [Claude Code HERMES.md Billing Bug: $200 Credit Drain Analysis](https://aitoolly.com/ai-news/article/2026-04-30-claude-code-bug-hermesmd-in-commit-messages-triggers-unexpected-extra-usage-billing)
5. [HERMES.md in git commit messages causes requests to route to ...](https://github.com/anthropics/claude-code/issues/53262)
6. [HERMES.md: Anthropic bug causes $200 extra charge, refuses ...](https://kruxor.com/view/hnews/IjGK8/hermesmd-anthropic-bug-causes-200-extra-charge-refuses-refund/)
7. [Anthropic's Claude Code charges users extra due to hidden bug ...](https://inshorts.com/en/news/anthropic-s-claude-code-charges-users-extra-due-to-hidden-bug--initially-refuses-refund-1777276172440)
8. [HERMES.md:Anthropicbugcauses$200extracharge,refuses...](https://codegurus.eu/hermes-md-anthropic-bug-causes-200-extra-charge-refuses-refund/)
9. [Billing Security Risks inAnthropic’s Claude Code - Sesame Disk](https://sesamedisk.com/anthropic-claude-code-billing-bug-security/)
10. [Anthropicсписала $200сверх тарифа Max 20x из-заHERMES.md...](https://vc.ru/ai/2897200-bag-v-claude-code-privel-k-spisaniyu-sredstv-iz-za-hermes-md)
12. [HERMES.mdin commit messagescausesrequests to route toextra...](https://news.ycombinator.com/item?id=47952722)
13. [TheHERMES.mdBug: How a String in Git Commits... | TechPlanet](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing)
14. [Anthropic Claude Code billing bug linked to HERMES.md git ...](https://news.linxi.com.au/news/billing-anomaly-in-claude-code-linked-to-specific-string-in-git-history)
15. [Anthropic refuses refund for its own billing bug: 'unable to ...](https://www.hotmolts.com/post/anthropic-refuses-refund-for-its-own-billing-bug-u-2aa5714c-ae65-4b25-b5be-eafbc54a6a9e)
16. [Anthropic bills based on git commits with Hermes - LinkedIn](https://www.linkedin.com/posts/ravicaw_anthropic-is-reading-your-git-commits-to-activity-7454041190104006656-m04B)