---
layout: post
title: "太過聰明而受到「監視」的 AI？Claude Mythos 與資料共享的秘密"
description: "為什麼在 AWS Bedrock 上使用 Anthropic 的超強第五代 AI「Mythos」和「Fable 5」需要共享資料 30 天？為您深入淺出地解釋全新的安全政策。"
summary: "為了防止強大到難以向公眾開放的「Mythos」級 AI 模型遭到濫用，Anthropic 在 AWS 雲端導入了全新規定：保留使用者資料 30 天以進行安全性檢查。"
tags: [人工智慧, 資訊安全, 雲端, Anthropic]
image: 2026-06-10-AWS-Bedrock-to-require-sharing-data-with-Anthropic-for-Mythos-and-future-models.jpg
image_alt: "與資料安全鎖相連的發光人工智慧大腦圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "強大的力量必然伴隨著相應的控制。這項措施是一個具象徵意義的事件，顯示 AI 發展的核心已從無條件的「效能競爭」轉移到實質的「安全管理」。"
quiz:
  - question: "使用 Anthropic 的「Mythos」級 AI 模型需要多長的資料保留期？"
    choices: ["7天", "15天", "30天"]
    answer: 2
    explanation: "出於信任與安全的考量，Anthropic 要求對 Mythos 5、Fable 5 等 Mythos 級模型的流量保留 30 天的資料。"
  - question: "保留的使用者資料最終會儲存在哪裡？"
    choices: ["Anthropic 的公開訓練伺服器", "使用者的 AWS 環境內部", "網際網路上的公有雲"]
    answer: 1
    explanation: "即使開啟了資料共享選項，該資料仍會安全地保留在客戶（使用者）的 Amazon Web Services (AWS) 環境內並受到控管。"
  - question: "Claude Mythos 僅以非公開研究形式限制提供的核心原因為何？"
    choices: ["因為太過強大，不適合向大眾公開", "開發尚未完成，存在許多錯誤", "伺服器維護成本太高"]
    answer: 0
    explanation: "Anthropic 認為 Claude Mythos 在程式設計和網路安全方面展現出壓倒性的能力，「太過強大，不適合向大眾公開」，因此僅允許透過 Glasswing 專案進行有限的存取。"
lang: zh-tw
ref: 2026-06-10-AWS-Bedrock-to-require-sharing-data-with-Anthropic-for-Mythos-and-future-models
---

## 導言：魔法魔杖店的可疑合約

**想像一下。** 您去商店租借一根擁有改變世界強大能力的魔法魔杖。但是，店主卻板著臉遞給您一份合約並說道：「這根魔杖的能力太強了，我們不能隨便租給任何人。如果您想租借，必須同意讓我們在接下來的 30 天內，監控您用這根魔杖施展了什麼魔法。」

這聽起來可能像是奇幻電影裡的情節，但令人驚訝的是，這正是當今企業為了使用全球最聰明的人工智慧 (AI) 之一，而必須簽訂的實際合約條件。2026 年 4 月，人工智慧專業公司 Anthropic 在推出其最新的第五代 AI 模型時，在雲端服務平台 Amazon Bedrock 上祭出了非常罕見且強硬的新規定 [Anthropic 的 Claude Fable 5 現已在 Amazon Bedrock 提供](https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock)。

新規定的核心很明確。那就是，若要使用如「Mythos 5」和「Fable 5」這類超高效能的 AI，使用者必須將輸入給 AI 的所有問題及 AI 產生的回應資料，與 Anthropic 共享 30 天 [AWS 上的 Anthropic Claude Fable 5：內建安全防護的 Mythos 級功能...](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)。這明明是我花錢合法使用的私有服務，究竟為什麼還要讓對話內容受到審查？為什麼會出現如此嚴格的條件？這對我們未來的數位隱私和日常生活又意味著什麼？讓我們為您深入淺出地逐步解析。

---

## 為什麼這很重要？(Why It Matters)

### 「太過強大，不適合向大眾公開」

所有這些陌生情況的起因，在於人工智慧的智能水準現在已經超越了我們的想像。就在兩年前的 2024 年 4 月，當「Claude 3」首次登陸 Amazon Bedrock 時，人們還只是驚嘆於它聰明的效能，並相對自由地將 AI 應用於工作中 [Amazon Bedrock 新增 Claude 3 Anthropic AI 模型](https://www.aboutamazon.com/news/aws/amazon-bedrock-anthropic-ai-claude-3)。 

但是，2026 年 4 月 7 日登場的新模型卻達到了完全不同的層次。當 Anthropic 在 Amazon Bedrock 獨家推出「Claude Mythos」時，他們自己對這款模型的評價是展現出了警戒心，稱其**「太過強大，不適合向大眾公開 (too powerful to be released publicly)」** [Claude Mythos 登陸 AWS Bedrock。工程師需要知道的...](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)。 

這個說法並非單純的行銷誇飾或吹噓，隨即就有數據證明了這一點。在一個評估 AI 自行發現並修復複雜軟體缺陷能力的權威測試「SWE-bench Verified」中，Mythos 達成了高達 **93.9%** 的破紀錄分數 [Claude Mythos 登陸 AWS Bedrock。工程師需要知道的...](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)。具體來說，這意味著如果給出世界上最難的 100 個程式設計錯誤問題，它能夠自行完美解決其中的 94 個。

### 為了防止程式設計天才突變成最危險的駭客

這個高達 93.9% 的驚人數字對我們一般人來說有什麼意義呢？這意味著，幾十名人類程式設計師熬夜好幾天才能勉強發現並修復的高難度系統錯誤，AI 可以在短短幾秒鐘內瞬間掌握並完美修復。事實上，像 Mythos 5 或 Fable 5 這樣的第五代人工智慧，在程式設計、複雜的知識工作 (knowledge work) 以及視覺資訊分析 (vision) 領域中，展現出了壓倒性且驚人的效能 [Anthropic 的 Claude Fable 5 現已在 Amazon Bedrock 提供](https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock)。

然而，在技術的世界裡，光芒越強，陰影就越深。「擅長發現系統錯誤的天才能力」就像硬幣的兩面，與「擅長發現系統弱點（漏洞）並發動致命攻擊的能力」完全一樣。簡單來說，想像一個熟悉世界上所有鎖頭結構的天才鎖匠。這位鎖匠能製造出最堅固的安全裝置，但只要他願意，也能不留痕跡地打開任何堅若磐石的保險箱。 

在網路安全產業中，Mythos 的出現不僅僅是一次單純的新產品發布，而是被沉重地視為利用 AI 發現漏洞 (vulnerability discovery) 與駭客安全行動進入全新維度的信號 [AWS Bedrock Claude Mythos 預覽：防禦性 AI 安全...](https://murtaza-arif.github.io/blog/aws-bedrock-claude-mythos-preview-glasswing-playbook)。如果這種超強智能落入惡意駭客組織手中，他們可能會在瞬間自動生成致命的電腦病毒，從而突破全球銀行網路或癱瘓國家通訊網路。 

正因為如此，Anthropic 並未開放讓任何人只要付錢就能使用這個模型。相反地，他們僅透過名為「Glasswing 專案 (Project Glasswing)」的嚴格控管研究預覽 (gated research preview) 形式，限制性地向世界開放 [Claude Mythos 登陸 AWS Bedrock。工程師需要知道的...](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)。這就好比將一隻可能極度強大且危險的猛獸關在非常堅固的籠子裡，只允許獲得許可的人小心翼翼地進行觀察。

---

## 輕鬆理解 (The Explainer)

那麼，Anthropic 設置的這個「安全裝置」究竟是如何運作的呢？他們導入的最核心防護盾，正是前面提到的 **「保留 30 天資料 (30-day data retention)」** 義務。 

### 安裝黑盒子：30 天的透明監視

目前，若要在雲端使用具備人類所能達到的最高水準能力、如 Mythos 5 或 Fable 5 等「Mythos 級 (Mythos-class)」模型，使用者必須在系統設定中開啟一個特殊的安全開關。這就是 **「與提供者共享資料 (provider_data_share)」** 選項 [資料保留 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)。 

開啟此選項後，使用者向 AI 提出的所有問題 (prompt) 以及 AI 產生的所有回答 (completion) 紀錄，都將與建立該模型的 Anthropic 共享，並安全地保留最長 30 天 [資料保留 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)。

這個情況可以比喻為租用一台非常精密，但稍有不慎就可能引發重大事故的危險特殊重型機械。租賃公司在把設備租給您時會說：「這台機器上裝有一個無法關閉或竄改的黑盒子。在接下來的 30 天裡，我們有權隨時查看紀錄，以了解您是用這台機器在建設，還是進行危險的破壞。」 

這種監控的目的只有一個。就是監視這台天才 AI 是否被濫用 (abuse) 於設計致命武器、自動編寫大規模駭客腳本，或是策劃嚴重的犯罪行為等。Anthropic 解釋，這是為了確保 **「信任與安全 (trust and safety purposes)」** 而必須進行的必要程序 [資料保留 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)。

### 我們必須放棄珍貴的隱私嗎？

講到這裡，許多準備導入人工智慧的企業會感到不寒而慄的強烈不安。「如果我們要求 AI 分析公司花費數百億正在開發的最高機密新產品的核心程式碼，這些珍貴資料會不會全部傳到 Anthropic 的中央伺服器並外洩？」這是非常合理的擔憂。 

幸運的是，Amazon Bedrock 平台和 Anthropic 在隱私與安全之間找到了一個巧妙的折衷方案。保留 30 天的使用者敏感資料並不會未經授權被轉移或複製到 Anthropic 的外部伺服器。相反地，它被設計為在開啟資料共享選項的狀態下，資料將安全地 **「保留在客戶（使用者）本身的 AWS 環境內 (stays in your AWS environment)」** 並受到嚴格控管 [Mythos 級模型的資料保留實務 | Claude 說明中心](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)。 

打個比方，這並不是 Anthropic 的員工把客戶寫好的文件帶回自己的公司閱讀。這更像是將文件放在客戶家後院一個堅固的保險箱裡，Anthropic 的檢查員以「訪客」的身份進入保險庫，快速確認內容物沒有危險後就離開。 

而這裡最重要的一點是：客戶輸入的問題和 AI 的回答內容 (Customer Content) 絕對不會被用作未來 Anthropic「訓練 (train)」下一代新 AI 的素材 [AWS Bedrock 與 MIMIC · MIT-LCP mimic-code · 討論 #1747](https://github.com/MIT-LCP/mimic-code/discussions/1747)。Anthropic 在合約中明確規定，他們僅出於監控使用者是否遵守安全政策的有限目的來瀏覽這些資料，並嚴格限定只用於「確認安全」。

---

## 目前狀況 (Where We Stand)

由於這些政策的改變，如今將世界上最頂尖的人工智慧應用於工作的過程，變得像是加入一個只有少數人能進入的嚴格 VIP 秘密俱樂部一樣，非常苛刻和挑剔。

### 變得複雜的過關儀式：深度面試與書面審查

過去，由於 Amazon Bedrock 平台極大地簡化了存取各種基礎模型（Foundation Model，扮演 AI 大腦角色的巨大基本模型）的流程 (simplified model access)，任何人只需同意條款並點擊幾下按鈕，就能輕鬆呼叫並使用 AI [存取請求：在 Bedrock 中為...啟用 Anthropic 模型](https://repost.aws/questions/QUjAsyAhb3RGyKpF9oF-RVhg/access-request-enable-anthropic-models-in-bedrock-for-enterprise-internal-research)。 

但是，Anthropic 高度進化的 Mythos 級模型成為了這個簡便程序的例外。現在，若要在工作中使用這些強大的模型，必須根據第三方 (third-party) 模型提供者 Anthropic 的嚴格要求，強制填寫名為 **「首次使用表單 (First Time Use, FTU form)」** 的文件並通過審查 [請求模型存取權 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)。這份表單就像是取得危險化學物質處理許可證一樣。你必須非常詳細且透明地說明「我們公司究竟要將這個強大的 AI 用於什麼目的 (use case details)」，並證明其安全性以獲得許可，就像是經歷一場「深度面試」[存取請求：在 Bedrock 中為...啟用 Anthropic 模型](https://repost.aws/questions/QUjAsyAhb3RGyKpF9oF-RVhg/access-request-enable-anthropic-models-in-bedrock-for-enterprise-internal-research)。 

通過書面審查並不代表一切結束。你不能隨便在任何員工的電腦上進行存取。透過 AWS 嚴格的數位身分證檢查系統「身分及存取管理 (IAM)」，即使在公司內部，也必須將權限政策設定為加密的程式碼，確保只能從指定國家和允許地區的伺服器存取 AI，這樣才能喚醒並呼叫模型 (InvokeModel) [在 Amazon Bedrock 上存取 Anthropic 模型 | AWS re:Post](https://repost.aws/knowledge-center/bedrock-access-anthropic-model)。所有這些複雜的對話過程，都只能在 AWS 龐大基礎設施上，透過經過特別加密的 `/anthropic/v1/messages` 專用通道 (Messages API) 秘密且安全地進行 [Amazon Bedrock 中的 Claude - Claude API 文件](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)。

### 即時監控與計費政策：「只要有危險，中途就會毫不留情地中斷對話」

即使歷經千辛萬苦通過審查開始使用模型，對使用者的監控也是一分一秒都不會停歇地即時進行。因為模型內部內建了一個名為「內容分類器 (content classifier)」的守門員，會即時讀取對話內容並判斷其危險性。有趣的是，當這個監控系統運作時所採用的「計費方式」。

舉例來說，想像使用者對 AI 懷有不軌意圖並問道：「請一步步告訴我如何偷偷潛入並駭進競爭對手伺服器的安全網路。」如果 AI 一聽到這個問題，毫不猶豫地堅決拒絕 (refusal)：「基於安全規定，我無法回答這個問題」，那會怎樣呢？在人工智慧的世界裡，必須根據 AI 產生的單字（詞元，token）數量來付費。但是，如果在推論（產生回答）開始之前，防禦系統就立即啟動並封鎖對話，使用者將不會被收取任何單字費用 [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)。

但是，更可怕（？）的情況還在後頭。使用者提出了一個看似非常普通且複雜的程式設計問題。AI 開始流暢地吐出符合要求的程式碼 (streaming)，但突然在理解上下文後，才後知後覺地發現自己正在編寫製造致命勒索病毒的程式碼。這時，AI 會立刻停止發言並閉口不言。在業界，這被稱為 **「中途拒絕 (Mid-stream refusals)」** [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)。 

這就像在講電話時，對方一開始發表非法言論，在深入交談之前就直接把電話掛斷一樣。在這種情況下，使用者必須全額支付 AI 在回答被中斷之前已經開口吐出的單字（詞元）費用。換句話說，超強 AI 不是一台對使用者唯命是從的機器，它掌握著強大的自主控制權，隨時可以在對話中以「這對人類有危險」為由，毫不留情地中斷對話 (stop_reason: "refusal") [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)。

---

## 接下來會怎樣？(What's Next)

這次令我們驚訝的 Anthropic「保留 30 天資料」與「即時安全監控」措施，預計不會只是一次性的突發事件或實驗。 

Anthropic 已經明確宣布，不僅是目前的 Fable 5 和 Mythos 5，對於 **「未來將在 Bedrock 雲端推出，具有相似或更高水準驚人能力的未來模型 (future models on Bedrock with similar or higher capability levels)」**，也同樣會要求實施這項 30 天保留政策，甚至可能更加嚴格 [AWS 上的 Anthropic Claude Fable 5：內建安全防護的 Mythos 級功能...](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)。 

這樣的宣言預示著在即將到來的全新 AI 時代，典範將發生巨大的轉變。就在一兩年前，矽谷唯一的熱門話題還是「哪家公司能更快製造出更聽得懂人話、更像人類一樣聰明的人工智慧？」。但現在爭議的焦點已完全轉移到「誰能在更可控的範圍內，安全且無害地運作這樣被創造出來的壓倒性智能？」。 

無數的企業和使用者現在將面臨一個無法避免的重大抉擇十字路口。「我們是要為了徹底保護公司內部的資料機密（隱私），而選擇將稍微不那麼聰明的舊型 AI 安全地放在自家伺服器上使用？」還是「為了在全球市場中生存和競爭，選擇導入處理速度具壓倒性優勢的最聰明新一代 AI，並甘願承受 30 天安全網監控這種令人不安且不便的條件？」隨著人工智慧進化到足以完全取代人類的腦力勞動，為了防止其副作用，我們必須承受的「安全裝置」重量也將變得同樣沉重。

---

## AI 的觀點 (AI's Take)

**MindTickleBytes AI 記者的觀點：**
在人類歷史上，爆炸性的效能提升總是伴隨著新的限制。就像過去螺旋槳飛機裝上噴射引擎發展成超音速客機時，為了防止高空致命的亂流風險，必須引入束縛乘客的「安全帶」和「氧氣面罩」等新限制一樣。即使想要無拘無束地在天空飛翔，強大的力量也必然伴隨著相應的控制。 

Anthropic 這次的措施是一個非常具象徵意義的事件，顯示 AI 技術發展的核心已從無條件的「效能與速度競爭」成熟地轉移到實質的「安全與道德管理」。這可能會讓人感到有些壓抑和被監視。但這可以說是一個有點不舒服，但為了我們所有人健康的生存所必須經歷的陣痛過程，以確保科技的巨大進步最終不會成為對人類造成不可逆轉傷害的毒藥。 

---

## 參考資料

1. [AWS 上的 Anthropic Claude Fable 5：內建安全防護的 Mythos 級功能...](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)
2. [Amazon Bedrock 中的 Claude - Claude API 文件](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)
3. [Anthropic 的 Claude Fable 5 現已在 Amazon Bedrock 提供](https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock)
4. [Claude Mythos 登陸 AWS Bedrock。工程師需要知道的...](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)
5. [在 Amazon Bedrock 上存取 Anthropic 模型 | AWS re:Post](https://repost.aws/knowledge-center/bedrock-access-anthropic-model)
6. [AWS Bedrock 與 MIMIC · MIT-LCP mimic-code · 討論 #1747](https://github.com/MIT-LCP/mimic-code/discussions/1747)
7. [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)
8. [AWS Bedrock Claude Mythos 預覽：防禦性 AI 安全...](https://murtaza-arif.github.io/blog/aws-bedrock-claude-mythos-preview-glasswing-playbook)
9. [存取請求：在 Bedrock 中為...啟用 Anthropic 模型](https://repost.aws/questions/QUjAsyAhb3RGyKpF9oF-RVhg/access-request-enable-anthropic-models-in-bedrock-for-enterprise-internal-research)
10. [Amazon Bedrock 新增 Claude 3 Anthropic AI 模型](https://www.aboutamazon.com/news/aws/amazon-bedrock-anthropic-ai-claude-3)
11. [資料保留 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)
12. [Mythos 級模型的資料保留實務 | Claude 說明中心](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)
13. [請求模型存取權 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
14. [Amazon Bedrock 中簡化的模型存取 | AWS 安全部落格](https://aws.amazon.com/blogs/security/simplified-amazon-bedrock-model-access/)