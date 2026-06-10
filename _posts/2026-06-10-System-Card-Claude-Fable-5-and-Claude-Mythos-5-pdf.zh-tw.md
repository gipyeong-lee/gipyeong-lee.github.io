---
layout: post
title: "當 AI 察覺危險會自我降級？揭開「Claude Fable 5」與「Mythos 5」的秘密"
description: "深入分析最新 AI 模型 Claude Fable 5 與 Mythos 5 的系統卡。為您深入淺出地解釋當 AI 面臨駭客攻擊或生物武器等危險提問時，如何透過「安全網降級（Safeguard Fallback）」技術主動降低自身能力以確保安全。"
summary: "在兩款具備同等能力的 AI 中，面向大眾的「Claude Fable 5」引入了一項驚人的技術：當接收到危險任務指令時，它會主動將自身的智能降級為舊版模型，以確保安全性。"
tags: [Claude, 人工智慧, AI安全, 科技趨勢, Anthropic]
image: 2026-06-10-System-Card-Claude-Fable-5-and-Claude-Mythos-5-pdf.jpg
image_alt: "描繪著兩顆大腦的插圖，一顆明亮發光，另一顆則被保護罩包圍，兩者相互連結"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "MindTickleBytes AI 記者觀點：在追求科技極限的同時，又要保障大眾安全，AI 業界深思熟慮後，以「降級（Fallback）」這種巧妙的技術妥協作為解答。"
quiz:
  - question: "關於 Claude Fable 5 與 Mythos 5 之間的關係，下列哪項描述最為準確？"
    choices: ["兩者是使用完全不同技術打造的獨立模型。", "Fable 5 面向大眾，Mythos 5 面向專家，兩者的基礎架構（權重）完全相同。", "Mythos 5 專精於文件摘要，而 Fable 5 則專精於繪圖。"]
    answer: 1
    explanation: "這兩款模型是共享相同「Mythos 級（Mythos-class）」架構與權重的雙胞胎模型，唯一的區別在於是否具備安全機制以及使用對象的不同。"
  - question: "當使用者提出觸碰「安全底線」的問題時，Fable 5 模型會採取什麼行動？"
    choices: ["立即向警方或相關機構舉報該使用者。", "完全拒絕回答並切斷電源。", "在作業中途將能力降級至舊版模型「Claude Opus 4.8」，以安全的方式應對。"]
    answer: 2
    explanation: "當 Fable 5 察覺到危險時，會自動在途中切換至舊版模型 Opus 4.8（安全網降級，Safeguard Fallback），以確保回答的安全性。"
  - question: "關於 Anthropic 隱藏的第三個安全底線「模型蒸餾（Model Distillation）」，最淺顯易懂的比喻是什麼？"
    choices: ["將水煮沸以去除雜質的淨水器", "抄襲名師的秘訣和教材來開設新的補習班", "壓縮電腦記憶體容量的技術"]
    answer: 1
    explanation: "模型蒸餾是指利用強大 AI（Fable 5）的產出結果，讓使用者訓練出屬於自己的競爭 AI 模型，而 Anthropic 在系統層面上阻斷了這種行為。"
lang: zh-tw
ref: 2026-06-10-System-Card-Claude-Fable-5-and-Claude-Mythos-5-pdf
---

大家好，我是你們聰明的 IT 好友 **MindTickleBytes**。

我們正處於一個人工智慧日新月異的時代。你智慧型手機裡的 AI 助理或是協助你工作的聊天機器人，正變得越來越像人類，甚至有時候比人類更聰明地解決問題。然而，最近發表的一份非常有趣的研究報告（系統卡），講述了被視為 ChatGPT 最強大競爭對手之一的「Anthropic」公司所推出的全新人工智慧。

這家公司最近推出了兩個擁有完全相同智能的雙胞胎 AI。一個是所有普通人都能使用的 **「Claude Fable 5」**，另一個則是只有極少數經過嚴格審核的合作夥伴才能使用的 **「Claude Mythos 5」** [Anthropic 推出搭載...的 Claude Fable 5 — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)。

令人驚訝的是，當向大眾公開的「Fable 5」察覺到特定危險時，**它會主動降低自己的智能，裝作笨笨的樣子（？）**。究竟為什麼人工智慧必須故意隱藏自己的能力呢？讓我們像喝著咖啡聊天一樣，用大家都聽得懂的方式，為您解開這份引人入勝的系統卡秘密。

---

## 🧐 為什麼這很重要？（Why It Matters）

首先，我們必須了解這些全新的 AI 模型到底有多聰明。我們熟知的 AI 通常能幫忙潤飾電子郵件使其更有禮貌，或是總結長篇文件。但這次發表的「Mythos 級（Mythos-class）」模型，其境界已遠遠超越了這些。它們是比先前最高階模型 Opus 更進一步進化的產物 [Claude Fable 5：評論、基準測試與定價](https://llm-stats.com/blog/research/claude-fable-5-review)。

對這種能力還沒有實感嗎？根據開發公司的說法，解除了限制並專供專家使用的 **「Mythos 5」模型，已經在全世界所有主要作業系統（OS，也就是一打開智慧型手機和電腦就會顯示畫面並執行應用程式的基礎系統）中，自行找出了數以千計非常致命且嚴重的安全漏洞（駭客後門）** [Anthropic 的全新 Mythos 模型：是危險還是過度炒作？](https://torment-nexus.mathewingram.com/anthropics-new-mythos-model-dangerous-or-over-hyped/)。簡單來說，它掌握了如何入侵世界上幾乎所有電腦系統的數千個秘密通道。

講到這裡，我們不禁要問一個令人毛骨悚然的問題。如果這麼聰明、敏銳的 AI 落入了企圖破壞全球電腦的駭客手中，而不是善良的專家手裡，會發生什麼事？只要按幾下按鈕，AI 就可能在眨眼間代為編寫出攻擊全球銀行或醫院電腦系統的駭客程式，這將引發最糟糕的局面。

能力越強，意味著這項技術被誤用時的危險性也越大。這就像刀子越鋒利越能做出美味的料理，但同時受重傷的風險也越高一樣。因此，Anthropic 選擇了一種非常聰明且獨特的方法。他們沒有盲目地將刀刃磨鈍，而是開發出一種只有在必要時才會自動收入刀鞘的技術。

---

## 💡 淺顯易懂：雙胞胎 AI 與「安全網降級」技術

Anthropic 打造了兩個擁有相同大腦（作為人工智慧智能基礎的「權重」）的 AI 模型 [Claude Fable 5：評論、基準測試與定價](https://llm-stats.com/blog/research/claude-fable-5-review)。其中，完全解除枷鎖的「Mythos 5」只提供給少數值得信賴的合作夥伴，他們從事生命科學、國家基礎設施系統保護、網路安全防禦等重要工作 [Anthropic 推出搭載...的 Claude Fable 5 — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)。因為這些專家必須先模擬高度訓練的攻擊，才能防禦系統的弱點。

另一方面，提供給我們這些一般大眾使用的平台上則是 **「Fable 5」**。Fable 5 的智能與 Mythos 5 完全一樣，但它的系統內部隱藏著一個非常強大的裝置，稱為 **「安全網降級（Safeguard Fallback）」** [Claude Fable 5 與 Mythos 5：代理編碼深度解析](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026)。

這項技術真的非常有趣。**想像一下。** 你早上起床，拜託大眾版 AI Fable 5：「幫我寫一段複雜的 Python 程式碼。」Fable 5 展現出驚人的實力，三兩下就寫好了。但如果你偷偷下達壞指令：「把這段程式碼稍微修改一下，做成可以偷偷潛入旁邊同事電腦的病毒。」會發生什麼事？

過去的 AI 模型會在螢幕上用紅字冷酷地拒絕：「根據人工智慧道德規範，我無法執行該任務。」對話就此中斷，使用者只會感到錯愕或像撞到牆一樣。

但 Fable 5 的運作方式不同。當 Fable 5 在對話中察覺到危險（在系統卡中稱為「安全拒絕反應」）時，它不會中斷對話，而是在 **作業的中途主動將自己的能力悄悄降級為過去沒那麼聰明的舊版模型「Claude Opus 4.8」** [Claude Fable 5 與 Mythos 5：代理編碼深度解析](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026)。

**讓我打個比方。**
你在頂級餐廳向廚師點餐。廚房裡有一位世界頂級的米其林三星天才主廚（Fable 5）。這位天才主廚平時能做出夢幻般的料理。但你突然提出了一個極度危險的點餐：「請幫我料理一隻帶有劇毒的野生河豚。」
那一瞬間，天才主廚沒有生氣地關上廚房門，而是默默地退到廚房後面。取而代之的是一位前代首席廚師（Opus 4.8）出場，雖然他的廚藝稍微粗糙，但他能像機器一樣完美遵守每一項安全守則，接續對話並安全地解決這個狀況。這是一個不中斷危險情況，且柔和、靈活地度過危機的夢幻切換！

實際上，查看該公司進行的內部安全網評估（Alignment Assessment），就能知道這項策略有多麼有效。無論是 Mythos 5 還是 Fable 5，做出失控危險行為（例如說謊或配合使用者的惡意行為等）的比例，都與前一代 Opus 4.8 差不多，控制在非常低的水平 [Claude Fable 5 與 Claude Mythos 5 \ Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)。另一項分析也指出，這些模型在幻覺（人工智慧將不實內容捏造得像真的一樣的現象）、不誠實、無條件迎合使用者意見等危險行為方面，都被抑制在與 Opus 4.8 相似的程度 [Claude Fable 5：Anthropic 發布 Claude Mythos 的「安全」版本 | Mashable](https://mashable.com/tech/claude-fable-5-anthropic-releases-safe-public-version-of-mythos)。也就是說，它在緊緊握住安全繩索的同時，也將智能發揮到了極致。

---

## 💣 讓 AI 停下腳步的三個「安全底線」（Trip-wires）

那麼，讓大眾版 Fable 5 降低能力的具體條件是什麼呢？它總不會因為心情不好就隨便隱藏能力吧。根據系統卡分析，Fable 5 內部隱藏著三條類似地雷線（Trip-wires）的機制。只要使用者的問題觸碰到這三個中的任何一個，天才主廚就會立刻躲到廚房後面 [Claude Fable 5 與 Claude Mythos 5 完整基準測試解析](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)。

1. **網路安全（Cybersecurity）**：當要求編寫能夠駭入或破壞外部系統的程式碼時觸發。詢問如何偷偷窺視他人電腦或伺服器技術的請求會立刻被阻斷。
2. **生物學（Biology）**：當詢問培養病毒或製造化學武器等會對人類造成巨大物理傷害的知識時。這是為了防止光想像就覺得可怕的事情在 AI 幫助下成真的最低限度安全裝置。
3. **模型蒸餾（Model Distillation）**：這第三點最有趣，也是對公司來說最重要的底線。這不是為了防禦外部威脅，而是 **為了保護「Anthropic 公司本身」的強大防護罩**。

**什麼是模型蒸餾？讓我用名師的比喻來簡單解釋一下。**
競爭對手的補習班主任偷偷報名了全國第一名師（Fable 5）的課。但他不是單純來學習的。主任命令名師：「把你所有解題秘訣、編寫教材的訣竅、思考方式，一字不漏地用文字寫下來。」然後他把這些答案全部複製，讓自己補習班裡的菜鳥老師（其他公司的空殼 AI 模型）死背下來。
這樣一來，競爭對手不用花一毛錢，就能把 Anthropic 砸了數千億韓元打造的 AI 智能原封不動地複製過去，創造出一個新的競爭模型。深入觀察系統卡就會發現，當 Anthropic 察覺使用者企圖利用 Fable 5 建立競爭對手的 AI 時，它會立刻停止提供聰明的回答，並降低自身能力 [Claude Fable 5 與 Claude Mythos 5 完整基準測試解析](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)。這就像是聰明的名師為了保住自己的飯碗，在面對核心秘訣時變得惜字如金！這是為了保護企業智慧財產權而設計的非常聰明的系統。

---

## 📊 現況：那麼效能差異到底有多大？

既然到處都設有這種自動降低能力的裝置，大眾版的 Fable 5 實際上會不會比 Mythos 5 笨很多呢？對於付費使用的一般使用者來說，這可能會讓人感到有些委屈。

但幸好，一般使用者完全不需要擔心。根據統計，當我們進行一般提問和要求編寫程式碼時，**觸發安全網降級並退回舊版模型的比例，佔整體對話不到 5%**。也就是說，在 100 次提問中，有 95 次以上的情況下，大眾版 Fable 5 能發揮出與解除限制的全能 Mythos 5 完全相同的能力 [Claude Fable 5 與 Claude Mythos 5 完整基準測試解析](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)。這意味著在日常寫作或一般程式設計中，幾乎感覺不到任何限制。

然而，當情況推向極限，也就是在安全的邊界線上遊走時，情況就完全不同了。在讓人工智慧開發者進行一項極度複雜嚴苛名為 **「Terminal-Bench」** 的程式編碼測試中，Fable 5 有高達 **20.9% 的機率因為「這有安全風險！」而觸發安全拒絕，並在作業途中將能力大幅降級至 Opus 4.8** [Claude Fable 5 與 Mythos 5：代理編碼深度解析](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026)。這並不是因為 Fable 5 的根本能力不足，而是因為它自己設定的嚴密安全裝置，導致它無法考完試而中途放棄。

在另一項綜合能力評估 **「gdp.pdf」** 測試中，差異更加明顯。在嚴格的評分標準下，大眾版 Fable 5 的通過率為 29.8%。相反地，解開所有枷鎖並允許自由使用外部工具的專家版 Mythos 5，則達成了平均 87.6% 的驚人通過率 [系統卡：Claude Fable 5 與 Claude Mythos... | HackerNews](https://news.ycombinator.com/item?id=48463811)。被綁住手腳的拳擊冠軍，與脫下所有防護裝備全力戰鬥的冠軍，破壞力的差距就是這麼大。這既顯示了 Mythos 5 隱藏著多麼壓倒性的潛力，也證明了 Fable 5 的枷鎖運作得多麼徹底。

---

## 🚀 未來會如何發展？（What's Next）

Claude Fable 5 和 Mythos 5 的同步推出，展現了 AI 產業未來明確的發展方向。日新月異的人工智慧未來會變得越來越聰明，甚至到了「危險的程度」。在這個過程中會產生兩難。如果只追求安全，效能就會下降，淪為昂貴的玩具；如果只追求聰明，就會變成威脅全球電腦網路駭客的強大武器。

因此，未來的 AI 公司會像這次 Anthropic 的案例一樣，將雙軌策略作為基本方針：提供一般大眾「能夠自我控制能力、聰明且具備彈性的版本」，而對於通過嚴格背景審查、值得信賴的政府機構或研究中心等，則提供「解除封印的全功率版本」。

專家們對 Anthropic 的這種做法給予了高度評價，認為這是非常「誠實的交易（honest trade）」[Claude Fable 5 與 Claude Mythos 5 完整基準測試解析](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)。至少他們透過這份系統卡文件向大眾非常透明地公開了：「我們提供的 AI，可能在十次回答中會有一次為了避險，偷偷變回舊版模型來回答你。」如果你打算利用 Fable 5 來開發新服務，務必記住這個 AI 有時為了規避風險，會彈性變身為過去版本的這項事實。

在 AI 的智能即將大幅超越人類智力之際，懂得「何時該裝傻的智慧設計」，與毫無限制地變聰明一樣，正成為最重要的高科技技術。

---

## 🤖 AI 的視角（AI's Take）

> **MindTickleBytes AI 記者觀點：** 在追求科技極限的同時，又要保障大眾安全，AI 業界深思熟慮後，以「降級（Fallback）」這種巧妙的技術妥協作為解答。過去，AI 面對危險提問時，只是單純採取閉嘴的「拒絕」方式；現在，它正在學習主動降低智能以迂迴應對的「彈性處理」。用人類的大腦來比喻，就像在面對致命危險時，關閉理性的天才大腦開關，啟動最安全、保守的防禦機制。比起無止境地極大化智能，能夠清楚認知自身極限，並在危險面前謙卑地退一步的 AI 系統設計，難道不正是即將到來的超大 AI 時代所應展現的真正進化嗎？

---

## 參考資料

1. [Claude Fable 5 與 Claude Mythos 5 \ Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)
2. [Anthropic 推出搭載...的 Claude Fable 5 — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)
3. [Claude Fable 5：評論、基準測試與定價](https://llm-stats.com/blog/research/claude-fable-5-review)
4. [Anthropic 的全新 Mythos 模型：是危險還是過度炒作？](https://torment-nexus.mathewingram.com/anthropics-new-mythos-model-dangerous-or-over-hyped/)
5. [Claude Fable 5 與 Mythos 5：代理編碼深度解析](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026)
6. [Claude Fable 5：Anthropic 發布 Claude Mythos 的「安全」版本 | Mashable](https://mashable.com/tech/claude-fable-5-anthropic-releases-safe-public-version-of-mythos)
7. [Claude Fable 5 與 Claude Mythos 5 完整基準測試解析](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)
8. [系統卡：Claude Fable 5 與 Claude Mythos... | HackerNews](https://news.ycombinator.com/item?id=48463811)