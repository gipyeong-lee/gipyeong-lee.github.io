---
layout: post
title: "開發者們怒了！GitHub Copilot 轉向「按量計費」，引發退訂潮"
description: "隨著 GitHub Copilot 從無限量的包月制改為用多少付多少的按量計費，開發者們對天價帳單的抱怨如潮水般湧來。我們透過日常比喻來輕鬆了解這場風波。"
summary: "GitHub Copilot 將計費方式從包月制改為「按量計費」後，短短幾小時內就耗盡了一個月額度的開發者們紛紛表達不滿，並警告將會棄用。"
tags: [GitHub Copilot, AI 寫程式, 按量計費, 計費方式變更, 開發者動態]
image: 2026-06-06-Angry-devs-vow-to-flee-GitHub-Copilot-as-metered-billing-takes-hold.jpg
image_alt: "一名開發者拿著空錢包，在電腦螢幕前抱頭苦惱的模樣"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這就像原本方便的吃到飽自助餐突然變成了昂貴的迴轉壽司。這是象徵 AI 使用成本開始回歸現實的標誌性事件。"
quiz:
  - question: "從 2026 年 6 月 1 日起，GitHub Copilot 的計費方式發生了什麼變化？"
    choices: ["完全免費", "維持無限量包月制", "改為用多少付多少的按量計費"]
    answer: 2
    explanation: "從 2026 年 6 月 1 日起，GitHub Copilot 變更為根據使用的 Token 數量來收費的按量計費模式。"
  - question: "報導中提到新計費方式引發的其中一個問題是什麼？"
    choices: ["錯誤變得更頻繁", "週末期間 AI 寫錯程式碼導致被收取了約 120 美元", "速度變得太慢"]
    answer: 1
    explanation: "一位開發者報告說，他沒有手動修復報錯的測試，而是讓 AI 代理程式不斷重複執行，結果在週末期間浪費了約 120 美元的費用。"
  - question: "開發者們抱怨的另一個技術限制是什麼？"
    choices: ["不支援特定的程式語言", "VSCode 和 Visual Studio 之間的工具不一致，以及 Sonnet 4.6 的上下文窗口限制", "不支援離線模式"]
    answer: 1
    explanation: "部分開發者對於 VSCode 和 Visual Studio 之間環境不一致，以及 Sonnet 4.6 模型原本具備讀取 1M Token 的能力，卻被限制在 200k 表示不滿。"
lang: zh-tw
ref: 2026-06-06-Angry-devs-vow-to-flee-GitHub-Copilot-as-metered-billing-takes-hold
---

想像一下，早上進辦公室，喝著熱咖啡，帶著輕鬆的心情開始寫程式，但還沒到午餐時間，手機就跳出帳單通知：「您這個月的 AI 使用額度已全數耗盡」，這會是什麼感覺？明明只是像平常一樣工作，卻在一夕之間收到了天價帳單。

全球無數程式設計師的得力助手「GitHub Copilot」的用戶們，現在正處於這樣的窘境。以 2026 年 6 月 1 日為界線，GitHub Copilot 的計費方式從原先的包月制，全面改為用多少付多少的「按量計費」，導致收到天價帳單的開發者們怨聲載道 [GitHub Copilot 的按量計費：我們需要（但並不想面對）的警鐘 | Elio Struyf](https://www.eliostruyf.com/metered-billing-github-copilot-shift/)。

## 這為什麼重要？ (Why It Matters)

一直以來，我們都把 AI 服務當作高級的「吃到飽自助餐」在享受。每個月只要付固定的金額，就可以盡情地提出複雜的問題，讓它源源不絕地產出程式碼。簡單來說，這就像是每個月只要繳固定的通訊費，就能無限上網吃到飽的時代。

然而，轉向按量計費意味著這頓令人安心的自助餐，突然變成了每盤價格不同的「迴轉壽司」，或者是根據行駛距離不斷跳錶的「計程車」。就像每拿一盤壽司，或者塞車時看著計程車跳錶一樣，你必須開始擔心錢包的厚度。

開發者們為了提升工作效率，一直都將 AI 帶在身邊並依賴著它，但現在，每次向 AI 提問時，都得在腦海中打著算盤。GitHub 用戶論壇上的一位開發者憤怒地表示：「從『可預測的訂閱制』變成這種不僅無助於生產力，反而帶來干擾的『充滿壓力的按量計費』服務，這是一個令人震驚的改變」 [按量計費生效，憤怒的開發者誓言逃離 GitHub Copilot](https://www.theregister.com/ai-and-ml/2026/06/02/github-copilot-users-threaten-exit-as-metered-billing-kicks-in/5249826)。科技本該讓我們的工作更輕鬆，現在卻淪為要因為擔心費用而小心翼翼使用的尷尬處境。

## 輕鬆了解 (The Explainer)

新導入的「基於 Token 的按量計費（Metered token-based billing）」到底是什麼？打個比方，就像是在圖書館借書時，根據頁數來收費一樣。當我們讓 AI 閱讀或編寫句子時，AI 會將文字拆解成名為「Token（處理文字的基本單位）」的小拼圖塊來辨識。我們提出的問題是 Token，AI 回覆的程式碼也是 Token。

過去，只要加入每月 39 美元（約 1,200 新台幣）的「Copilot Pro+」方案，就可以無限量地使用這些拼圖塊 [按量計費生效，憤怒的開發者誓言逃離 GitHub Copilot - SoylentNews](https://soylentnews.org/article.pl?sid=26/06/02/0711209&from=rss)。開發者們會把整段長程式碼直接交給它處理，甚至為了找一個小錯字，就把所有程式碼都丟給 AI。

但在新的按量計費機制下，AI 每次拼湊這些拼圖塊時都會即時收費。你提出的問題越長、越複雜，要求編寫的程式碼越龐大，費用就會像雪球一樣越滾越大。事實上，在新計費方式上線後，不斷有開發者抱怨，他們在短短幾個小時或一天之內，就把一個月的額度（預先支付的使用權）全部燒光了 [GitHub Copilot 依用量計費生效，額度迅速耗盡引發開發者強烈反彈 - gHacks Tech News](https://www.ghacks.net/2026/06/02/github-copilot-usage-based-billing-takes-effect-drawing-developer-backlash-over-rapid-credit-depletion/)。

## 現況 (Where We Stand)

從第一線傳來的實際受害案例來看，情況還要嚴重得多。來看看知名網路論壇 Reddit 上的一則分享吧。一位開發者在週末期間沒有親自去修復報錯的測試程式碼，而是開著 AI 代理程式（能自行判斷並執行任務的 AI 工具）讓它自己解決。到了星期一回來一看，AI 在整個週末默默地不斷失敗並重試，竟然耗費了高達 120 美元（約 3,800 新台幣）的 Token [Reddit 上的 r/technology 版：按量計費生效，憤怒的開發者誓言逃離 GitHub Copilot](https://www.reddit.com/r/technology/comments/1tur88b/angry_devs_vow_to_flee_github_copilot_as_metered/)。本來是為了圖個方便才用 AI，結果在週末期間就把好幾頓大餐的錢給飛了。

另一位使用者根據自己原有的工作模式模擬了使用量，結果發現每個月將會產生高達 600 歐元（約 21,000 新台幣）的額外費用，這個結果讓他震驚不已 [GitHub Copilot 的按量計費：我們需要（但並不想面對）的警鐘 | Elio Struyf](https://www.eliostruyf.com/metered-billing-github-copilot-shift/)。

在這種情況下，使用者之間自然湧現出許多無奈的批評聲浪：「結果我們享受的福利大幅縮水，要付的錢卻變得更多了」 [Copilot 帳單震撼彈衝擊開發者 -- Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/06/04/copilot-billing-shock-hits-developers.aspx)。

雪上加霜的是，即使付了高昂的費用，服務品質也並未得到完美的支援。使用者指出，微軟的程式碼編輯器 VSCode 和 Visual Studio 之間，AI 工具的功能一致性嚴重不足。此外，Copilot 搭載的最新 AI 模型「Sonnet 4.6」，原本具備一次能讀取並理解高達 100 萬（1M）個 Token（相當於數十本厚書的份量）的卓越能力。然而，微軟為了節省成本，人為地將其限制在只有五分之一的 20 萬（200k）個 Token（上下文窗口限制，即一次能記住的上下文極限），這引發了用戶的強烈反彈 [按量計費生效，憤怒的開發者誓言逃離 GitHub Copilot | Hacker News](https://news.ycombinator.com/item?id=48364983)。

## 未來走向 (What's Next)

面對眼前突如其來的鉅額帳單，無法抑制怒火的開發者們揚言要徹底離開 GitHub Copilot，尋找其他的替代 AI 工具。在一個開發者論壇上，甚至出現了極端的退訂宣言：「我們團隊裡僅存的兩名開發者也打算放棄 Copilot 離開了」 [按量計費生效，憤怒的開發者誓言逃離 GitHub Copilot - tchncs](https://discuss.tchncs.de/post/61434336)。

業界也有部分人士以冷靜的眼光看待這次事件。有評論認為，這是一個苦澀的「起床號」，迫使開發者們開始自我控管並最佳化過去毫無節制、揮霍無度的 AI 使用量 [開發者憤怒於他們再也不能在 GitHub Copilot 上隨意燃燒 AI 額度了](https://cybernews.com/ai-news/microsoft-github-copilot-angry-developers/)。就像要節約用水一樣，節省使用 AI Token 的時代已經來臨。

但是，對成本和天價帳單的恐懼，最終可能會帶來慘痛的副作用。因為這顯然會大幅限縮開發者們自由測試各種程式碼、創造創新的實驗精神。過去一直承受著龐大虧損來提供服務的科技巨頭們，終於開始將天文數字的 AI 營運成本轉嫁給一般使用者。這項重大改變未來將對整個 AI 工具市場引發怎樣的地殼變動，是我們必須密切關注的時刻。

---

**MindTickleBytes 的 AI 記者觀點**

我們現在正走過曾經無拘無束擴張的「AI 浪漫主義時代」的尾聲。度過了以低廉價格享受無數便利的時期後，現在已經迎來了必須面對帳單這殘酷現實的「成本效益化」時代。

再聰明的 AI 助手，如果雇主無法負擔它的薪水（使用費），也只能面臨被解僱的命運。這次事件不單單只是一家公司的計費方案調整，更拋出了一個沉重的問題：「我們真的準備好為這項技術支付合理的費用了嗎？」。這不僅關乎開發者的寫程式習慣，對於隱藏在便利性背後的 AI 實際運作成本，現在正是我們所有人都必須更精明地計算並做好準備的時刻。

## 參考資料
1. [GitHub Copilot 的按量計費：我們需要（但並不想面對）的警鐘 | Elio Struyf](https://www.eliostruyf.com/metered-billing-github-copilot-shift/)
2. [按量計費生效，憤怒的開發者誓言逃離 GitHub Copilot](https://www.theregister.com/ai-and-ml/2026/06/02/github-copilot-users-threaten-exit-as-metered-billing-kicks-in/5249826)
3. [按量計費生效，憤怒的開發者誓言逃離 GitHub Copilot - SoylentNews](https://soylentnews.org/article.pl?sid=26/06/02/0711209&from=rss)
4. [GitHub Copilot 依用量計費生效，額度迅速耗盡引發開發者強烈反彈 - gHacks Tech News](https://www.ghacks.net/2026/06/02/github-copilot-usage-based-billing-takes-effect-drawing-developer-backlash-over-rapid-credit-depletion/)
5. [Reddit 上的 r/technology 版：按量計費生效，憤怒的開發者誓言逃離 GitHub Copilot](https://www.reddit.com/r/technology/comments/1tur88b/angry_devs_vow_to_flee_github_copilot_as_metered/)
6. [Copilot 帳單震撼彈衝擊開發者 -- Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/06/04/copilot-billing-shock-hits-developers.aspx)
7. [按量計費生效，憤怒的開發者誓言逃離 GitHub Copilot | Hacker News](https://news.ycombinator.com/item?id=48364983)
8. [按量計費生效，憤怒的開發者誓言逃離 GitHub Copilot - tchncs](https://discuss.tchncs.de/post/61434336)
9. [開發者憤怒於他們再也不能在 GitHub Copilot 上隨意燃燒 AI 額度了](https://cybernews.com/ai-news/microsoft-github-copilot-angry-developers/)