---
layout: post
title: "忘掉只會回答問題的AI吧：能自主工作與自我驗證的「Claude Fable 5」"
description: "Anthropic新推出的「Claude Fable 5」不只是一個簡單的聊天機器人。本文為您深入淺出地解析這個全新AI的出現，它能夠自主規劃並驗證人類通常需要花費數天才能完成的複雜專案。"
summary: "一個嶄新層次的AI模型「Claude Fable 5」已經問世。它能夠自主規劃人類需要花費數天甚至數週才能完成的複雜專案，運用視覺能力批判性地審查自己的成果，並堅持不懈地主動解決問題。"
tags: [AI, Claude, Anthropic, 人工智慧, 科技趨勢]
image: 2026-06-12-Claude-Fable-is-relentlessly-proactive.jpg
image_alt: "以溫暖色調繪製的插畫，描繪一個機器人在巨大的圖書館中懸浮著無數的書籍與設計圖，並不斷自主進行研究與校對的工作場景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI的進化已經跨越了一個新台階，從單純吐出知識的自動販賣機，轉變為能主動發現並解決問題的積極同事。"
quiz:
  - question: "如何才能最好地利用Claude Fable 5？"
    choices: ["詢問日常簡單的天氣問題", "翻譯簡單的問候語", "交給它需要花費數天、複雜且尚未解決的最困難問題"]
    answer: 2
    explanation: "Claude Fable 5是為了複雜且長期的專案而設計的。如果只在簡單的任務上測試它，將會低估這個模型的真正能力。"
  - question: "在Claude Fable 5的特徵中，與現有AI最大差異的特點是什麼？"
    choices: ["只能純粹以文字回答", "能視覺化地審查自己的成果，並批判性地自我驗證是否符合目標", "價格永遠是完全免費的"]
    answer: 1
    explanation: "該模型具備使用視覺（Vision）功能將自己的成果與目標進行對比並批判性審查的能力，同時能夠主動地進行自我驗證。"
  - question: "與其一同發表的「Claude Mythos 5」是提供給誰使用的？"
    choices: ["所有一般的免費使用者", "透過Glasswing專案參與的網路安全專家", "國小學生的教育用途"]
    answer: 1
    explanation: "Mythos 5是與Fable 5相同的模型，但在解除部分保護措施的狀態下，僅透過Glasswing專案向網路安全專家進行有限的提供。"
lang: zh-tw
ref: 2026-06-12-Claude-Fable-is-relentlessly-proactive
---

想像一下：早晨您來到公司，對一位剛入職且能力出眾的新進員工指示：「請你全權負責從我們公司的新服務企劃到原型開發的整個過程。」普通的AI可能會因為不明白您的意思而不斷提問，或者在1秒鐘內隨便生出一份網路上流傳的老套企劃書，然後告訴您工作已經完成。但這位新員工卻與眾不同。它會自行擬定企劃案、編寫程式碼，接著用自己的眼睛親自確認畫面是否正確呈現。如果產出的成果有錯誤，它會毫不猶豫、甚至通宵達旦地自行修改與評估，並在隔天早晨將近乎完美的成果悄悄放在您的辦公桌上。

這是最能精準描述人工智慧企業Anthropic於2026年6月9日向全球全新公開的人工智慧——**「Claude Fable 5」**的場景 [[Claude Fable 5 已經問世：Anthropic首個公開的Mythos級別...](https://pasqualepillitteri.it/en/news/4523/claude-fable-5-fruitcake-eap-mythos-public-release)] [[Claude Fable 5 已經問世：全新頂級模型對您的...有何意義](https://theaicareerlab.com/blog/claude-fable-5-for-professionals)]。知名軟體開發者西蒙·威利森（Simon Willison）在密集測試這款AI兩天後，用一句話留下了深刻的感想：

「形容這款AI最好的方式就是**『堅持不懈地主動（relentlessly proactive）』**。這個模型懂得許多技術上的訣竅（tricks）。」 [[Claude Fable展現出堅持不懈的主動性](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/)] [[Claude Fable 5 AI模型在初步測試後被形容為堅持不懈地主動...](https://news.linxi.com.au/news/willison-describes-claude-fable-5-as-relentlessly-proactive-following-initial-testing)]

究竟Claude Fable 5與現有的聊天機器人有何不同，竟能讓專家們給出如此驚人的評價？讓我們從一般人的視角，按部就班地探討這項新技術的意義與影響力。

---

## 這為什麼重要？ (Why It Matters)

我們至今所使用的熟悉的聊天機器人型AI，打個比方就像是一台「高級飲料自動販賣機」。投入硬幣（提出問題）並按下按鈕，相應的飲料（回答）就會掉出來。但您不可能拜託飲料販賣機：「請幫我規劃一週的健康菜單，去超市採買後，每天早上再根據我的體質做飯給我吃」。因為販賣機只能回應單一的請求，無法朝著長期目標自行運作。

Claude Fable 5 已經遠遠超越了這種簡單的販賣機或聊天機器人的極限。該模型被設計成能扮演「獨立知識工作者（Autonomous knowledge worker）」的角色，能夠獨自從頭到尾完成那些人類需要耗費數小時、數天甚至數週才能艱難解決的大型複雜專案 [[Claude Fable 5 提示工程 - Claude API文件](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)] [[ClaudeFable5 - API定價與基準測試 | OpenRouter](https://openrouter.ai/anthropic/claude-fable-5)]。 

Anthropic將這個模型稱為具備了**「Mythos等級（Mythos-class）」**的能力 [[AWS上的Anthropic Claude Fable 5：內建安全防護的Mythos級別功能現已可用 | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)] [[ClaudeFable5 - API定價與基準測試 | OpenRouter](https://openrouter.ai/anthropic/claude-fable-5)]。「Mythos」是神話或傳說的意思，這個等級的模型是為了您最具野心且需要漫長時間的專案（Long-running projects）而打造的。這意味著它專精於解決過去的AI模型連想都不敢想的複雜、模糊且龐大的問題 [[Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable)] [[Claude Fable 5 提示工程 - Claude API文件](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)]。 

這對於普通上班族或大眾來說意義非凡。直到現在，使用者還必須對AI一一拆解下達指示：「請幫我總結這個段落」、「接下來請把這個寫成程式碼」。人類必須作為AI的管理者不斷地介入其中。但現在，您只需要給出一個大方向：「請達成這個巨大的目標」即可。接著，AI會自行制定詳細計畫，遇到障礙時主動繞道，並負責執行到底，一個真正意義上的「委任」時代正在全面開啟。簡單來說，它已經從單純協助我工作的「工具」，進化成了能主動代替我完成工作的可靠「同事」。

---

## 深入淺出 (The Explainer)

那麼，Claude Fable 5是如何獨自完成這種長達數天的專案的呢？讓我們來看看讓這個模型與眾不同的三大核心特徵。

**1. 自行核對答案的細心模範生：「主動自我驗證」**

如果把困難的數學題或程式設計問題交給現有的AI，無論答案對錯，它都會先快速生成句子然後草草了事。就像是一個交了錯誤答案還理直氣壯的學生。然而，Claude Fable 5則是一個在交考卷前會徹底「驗算」的學生。 

根據Anthropic的說法，這個模型的工作方式非常徹底（thorough）且主動（proactive），並且會自行測試自己產出的結果 [[Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable)]。在技術術語上，這被稱為**「主動自我驗證（Proactive self-verification）」**。如果這款AI在工作過程中學到了新內容，它會自行更新自己的技能，甚至為了評估自己的成果，還會自行開發出一套專屬的評估工具集（Evaluations and harnesses）[[AWS上的Anthropic Claude Fable 5：內建安全防護的Mythos級別功能現已可用 | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)]。在別人檢查之前，它會嚴格地自我評估，將完成度提升到極致。

**2. 長了眼睛的寫程式魔法師：「運用視覺進行批判性審查」**

最令人驚訝的進展之一是，這款AI不僅僅是一個只會盲目輸入文字（程式碼）的魔法師，而是能用雙眼親自「看見」自己創造出的成果。 

舉例來說，想像您指示Fable 5製作一個電腦程式的網頁畫面。Fable 5會編寫程式碼，以高保真度（High fidelity）將設計實現出來。令人驚訝的是接下來的動作。它會利用視覺（Vision，看圖並理解的功能）功能親自確認自己編寫的程式碼所呈現出的結果畫面，然後與最初設定的目標進行比較並進行批判性評估（Critique）[[AWS上的Anthropic Claude Fable 5：內建安全防護的Mythos級別功能現已可用 | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)]。這完全就像是一位廚師照著食譜完成料理後，在端上客人餐桌前，會親眼確認擺盤並親口品嚐評估一樣。它在編寫程式、多模態（同時理解文字與影像的能力）推理等方面都具備了驚人的優勢 [[經濟實惠且適用於編程與Mythos級別的ClaudeFable5 API... | Kie.ai](https://kie.ai/claude-fable-5)]。

**3. 不會無條件說「好」的直言同事：「提示詞評論」**

以前的AI無論使用者提出多麼愚蠢的問題，都會機械式地拼湊出一個看似合理的答案。然而，使用過Claude Fable 5的人們會立刻發現一種奇妙的傾向——這個模型似乎會對使用者的問題（提示詞）本身提出自己的意見 [[Claude Fable 5 是面向大眾的Mythos - Techzine Global](https://www.techzine.eu/blogs/applications/141978/claude-fable-5-is-mythos-for-the-masses/)]。

雖然它依然受限於大型語言模型（LLM，學習了大規模文本資料的AI）的框架，但Fable 5展現出了對輸入指令進行自我反思（Self-reflect）的行為 [[Claude Fable 5 是面向大眾的Mythos - Techzine Global](https://www.techzine.eu/blogs/applications/141978/claude-fable-5-is-mythos-for-the-masses/)]。它更像是一位聰明且敢言的實務工作者，會反過來給予使用者回饋：「這個問題用這種方式處理可能會更好。」這意味著您擁有了一個可靠的合作夥伴，當您下達錯誤指令時，它不會一味服從，而是會為您指出更好的道路。

---

## 目前現況 (Where We Stand)

Claude Fable 5 並不是遙遠未來的想像，而是已經進入了我們的現實。Anthropic已將這個模型作為最先進的通用模型正式向大眾公開 [[介紹 Claude Fable 5 與 Claude Mythos 5 - Claude API文件](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)]。

有趣的是，這次發表會中還有一位**隱藏的雙胞胎兄弟**。向大眾公開，內建各種安全防護（Safeguards，防止有害或危險輸出的保護功能），讓我們能在日常和商業中安全使用的版本，就是我們現在討論的「Claude Fable 5」。另一方面，存在著一個與該模型如雙胞胎般相同，卻刻意解除了限制AI強大力量的保護措施，既危險又強大的版本。這個神秘模型的名字叫做**「Claude Mythos 5」**，它僅透過一個名為「Glasswing專案（Project Glasswing）」的極機密計畫，秘密且受限地提供給身分與目的明確的網路安全專家等少數人使用 [[Claude Fable 5 已經問世：Anthropic首個公開的Mythos級別...](https://pasqualepillitteri.it/en/news/4523/claude-fable-5-fruitcake-eap-mythos-public-release)]。

那麼，一般人與企業可以從哪裡使用Fable 5呢？目前，該模型不僅可以透過其專屬的Claude API，還已經部署在亞馬遜強大的雲端網路AWS Bedrock、Google的Vertex AI、微軟的Foundry等全球主要的科技巨頭平台上，可以立即啟用 [[ClaudeFable5 剛上線：在...達到80.3% | WaveSpeed Blog](https://wavespeed.ai/blog/posts/claude-fable-5-launch-benchmarks-pricing/)]。這項新技術一問世，就已經全面鋪設在全球的數位神經網路中了。

在使用費率方面，隱藏著Anthropic的重要策略。如果您是一般消費者服務Claude的付費方案（Pro、Max、Team方案）訂閱者，在2026年6月22日之前，都可以不需額外付費，自由地測試這款最高級的模型 [[Claude Fable 5 已經問世：全新頂級模型對您的...有何意義](https://theaicareerlab.com/blog/claude-fable-5-for-professionals)] [[ClaudeFable5 剛上線：在...達到80.3% | WaveSpeed Blog](https://wavespeed.ai/blog/posts/claude-fable-5-launch-benchmarks-pricing/)]。 

然而，當開發者在程式後端（API）大量使用時，其定價相當昂貴。以AI處理單詞的單位「標記（Token）」為基準，定價為每100萬個輸入標記10美元，每100萬個輸出標記50美元 [[ClaudeFable5（附備援）- 智慧、效能與價格...](https://artificialanalysis.ai/models/claude-fable-5)] [[ClaudeFable5 - API定價與基準測試 | OpenRouter](https://openrouter.ai/anthropic/claude-fable-5)]。假設一本書大約是10萬個標記，這相當於讓AI讀取10本書需要花費10美元。考慮到其他便宜的日常用AI模型成本約為1到2美元，這無疑是在支付超級頂級專家的「人事費用」。

**這裡有最需要注意的一點。**
絕對不能白白浪費這顆極度昂貴且聰明的「大腦」。Anthropic的官方文件對開發者與使用者留下了強烈的警告與建議。 

*「如果僅在簡單的工作負載上測試Claude Fable 5，反而會低估這個模型的能力範圍。」* [[Claude Fable 5 提示工程 - Claude API文件](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)]

也就是說，如果用這個AI來回答「告訴我今天台北的天氣」或是「幫我翻譯這封簡短的英文郵件」這種日常問題，就像是請來世界頂尖的火箭工程師，卻要他解答小學生的九九乘法表，然後失望地說「也不過如此嘛」一樣。能夠從Fable 5獲得最佳成果的團隊，都是將這個AI投入到他們所面臨的**「最難以解決的未解難題（Hardest unsolved problems）」**中 [[Claude Fable 5 提示工程 - Claude API文件](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)]。

實際上，在給予5項真實且複雜的實務工作進行效能測試的結果顯示，Fable 5在處理龐大文件或從架構層級設計程式碼等，一般專業工作者（Working professional）需要苦思冥想數天才能完成的深度工作中，證明了其真正的價值 [[我用5個真實世界的提示詞測試了Claude Fable 5：這是它...](https://aitoolsclub.com/i-tested-claude-fable-5-with-5-real-world-prompts-heres-what-it-can-actually-do/)] [[Claude Fable 5 已經問世：全新頂級模型對您的...有何意義](https://theaicareerlab.com/blog/claude-fable-5-for-professionals)]。 

---

## 未來發展 (What's Next)

「您完全用錯Claude Fable 5了。」這是一位在YouTube上評論該模型使用方式的專家所留下的針砭之言 [[你用錯了ClaudeFable5 - YouTube](https://www.youtube.com/watch?v=vjdHAWvVCP4)]。因為如果還按照過去的習慣，單純作為一問一答的用途，就無法完整享受這項先進技術帶來的助益。

Claude Fable 5 的問世正在根本性地顛覆我們的工作方式。如果說至今為止，AI還只是一個草草起草，再由人類花費大量時間修改的「人類主導型輔助工具」，那麼現在局勢已經徹底翻轉。反過來，當AI花費數天自行潤飾企劃案、修正錯誤，並提交近乎完美的最終方案時，人類監督者只需進行審查與最終批准即可。工作重心的轉移如此戲劇化，要求繁多且複雜的長期代理（Agentic，能自主判斷與行動的自主個體）工作時代已正式揭開序幕 [[介紹 Claude Fable 5 與 Claude Mythos 5 - Claude API文件](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)]。 

我們現在迎來了一位新的職場同事——一個會緊咬著工作不放、自我反省成果並進行修正的傑出AI。現在我們只剩下唯一、也是最重要的課題：認真思考要將什麼樣的「最巨大且最具野心的問題」交給這位聰明的數位同事。一個「問題的格局決定成果的格局」的時代已經來臨。

---

**MindTickleBytes AI記者的視角：**
如果過去的AI只是個忙著被動處理交辦事項的實習生，那麼Fable 5已經成長為一位會主動發現公司問題、親眼確認結果，並堅持不懈地深入探究的、充滿責任感的資深實務工作者。人工智慧已超越了單純「縮短」人類工作時間的範疇，正在開啟一個能夠拓展需要數天激烈思考的「思維深度」的真正自動化時代。為了將這項耀眼的進步完全化為自己的武器，我們人類不應再死記硬背工具的使用方法，而是到了該培養能提出更敏銳、更大膽問題的「企劃者」能力的時候了。

---

## 參考資料

1. [Claude Fable 5 已經問世：Anthropic首個公開的Mythos級別...](https://pasqualepillitteri.it/en/news/4523/claude-fable-5-fruitcake-eap-mythos-public-release)
2. [Claude Fable展現出堅持不懈的主動性](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/)
3. [Claude Fable 5 AI模型在初步測試後被形容為堅持不懈地主動...](https://news.linxi.com.au/news/willison-describes-claude-fable-5-as-relentlessly-proactive-following-initial-testing)
4. [Claude Fable 5 提示工程 - Claude API文件](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
5. [Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable)
6. [AWS上的Anthropic Claude Fable 5：內建安全防護的Mythos級別功能現已可用 | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)
7. [Claude Fable 5 是面向大眾的Mythos - Techzine Global](https://www.techzine.eu/blogs/applications/141978/claude-fable-5-is-mythos-for-the-masses/)
8. [介紹 Claude Fable 5 與 Claude Mythos 5 - Claude API文件](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)
9. [Claude Fable 5 已經問世：全新頂級模型對您的...有何意義](https://theaicareerlab.com/blog/claude-fable-5-for-professionals)
10. [ClaudeFable5 剛上線：在...達到80.3% | WaveSpeed Blog](https://wavespeed.ai/blog/posts/claude-fable-5-launch-benchmarks-pricing/)
11. [ClaudeFable5（附備援）- 智慧、效能與價格...](https://artificialanalysis.ai/models/claude-fable-5)
12. [ClaudeFable5 - API定價與基準測試 | OpenRouter](https://openrouter.ai/anthropic/claude-fable-5)
13. [經濟實惠且適用於編程與Mythos級別的ClaudeFable5 API... | Kie.ai](https://kie.ai/claude-fable-5)
14. [我用5個真實世界的提示詞測試了Claude Fable 5：這是它...](https://aitoolsclub.com/i-tested-claude-fable-5-with-5-real-world-prompts-heres-what-it-can-actually-do/)
15. [你用錯了ClaudeFable5 - YouTube](https://www.youtube.com/watch?v=vjdHAWvVCP4)