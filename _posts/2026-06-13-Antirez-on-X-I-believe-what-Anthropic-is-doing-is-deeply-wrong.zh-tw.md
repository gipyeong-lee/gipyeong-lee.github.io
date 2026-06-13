---
layout: post
title: "是為了安全，還是為了牽制？Anthropic的「過度審查」為何讓全球開發者感到憤怒"
description: "ChatGPT的強大對手Anthropic在新的AI模型中加入了過度的安全過濾器，因此受到了開發者們的強烈批評。甚至引發了牽制開源爭議，本文將為您淺顯易懂地整理這起事件的始末。"
summary: "Anthropic設計新模型時，刻意避開與AI研究相關的問題，在遭遇生態系的強烈反對後撤回了該政策，但其可信度已受到了重大打擊。"
tags: [Anthropic, AI安全, 開源, Antirez, AI趨勢]
image: 2026-06-13-Antirez-on-X-I-believe-what-Anthropic-is-doing-is-deeply-wrong.jpg
image_alt: "插圖描繪了人們看著被巨大掛鎖鎖住的機器人頭部而感到鬱悶的樣子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "為了不讓AI「安全」這個崇高的名義變質為排除競爭對手的巧妙工具，現在比以往任何時候都更需要對技術控制建立透明的標準與監管。"
quiz:
  - question: "當Anthropic的新模型收到有關網路安全或化學的問題時，採取了什麼措施？"
    choices: ["立即停用發問者的帳號", "將問題繞道發送給性能較低的模型", "將相關數據傳送給政府機構"]
    answer: 1
    explanation: "Anthropic為了防止使用者製造生物武器或策劃網路攻擊，當收到相關問題時，會將問題繞道（rerouting）給性能較差、較不聰明的模型。"
  - question: "知名開發者Antirez批評Anthropic的主要原因是什麼？"
    choices: ["模型的月度訂閱費太貴", "因為過度的過濾，甚至阻擋了LLM研究或醫學問題等無害的操作", "因為AI生成回答的速度太慢"]
    answer: 1
    explanation: "Antirez強烈指出，Anthropic極度敏感的過濾器甚至阻擋了無害的AI研究或單純的醫學問題，這是「根本上的錯誤」。"
  - question: "在開發者強烈反彈之後，Anthropic採取了什麼應對措施？"
    choices: ["承認自己取得了「錯誤的平衡」並撤回了政策", "預告會進行更強大的審查來對抗", "宣布將全面支持開源模型的開發"]
    answer: 0
    explanation: "Anthropic承認對新的安全機制取得了「錯誤的平衡（tradeoff）」，並撤回了阻礙研究人員的政策，但在可信度上已經受到了巨大的打擊。"
lang: zh-tw
ref: 2026-06-13-Antirez-on-X-I-believe-what-Anthropic-is-doing-is-deeply-wrong
---

想像一下：你在週末抽空去圖書館，想借閱關於化學或最新電腦科學的專業書籍來深入學習，但圖書館管理員突然擋住了你的去路。管理員神情嚴肅地說：「你可能會利用這些知識來製造土製炸彈或駭入國家機構，所以我不能把這本書借給你。」接著，他遞給你一本幼兒園小朋友讀的薄薄的科學童話書。這真是個荒謬又令人不快的狀況吧？因為你並沒有犯罪，卻被當成了潛在的罪犯。

最近，全球人工智慧（AI）業界也發生了完全一樣的事情。創造ChatGPT的OpenAI最強大的競爭對手、自豪於打造「最安全AI」的企業 **Anthropic** 就是這個主角。因為有消息指出，Anthropic最新推出的AI模型被設計成，在面對關於AI研究或特定專業領域的問題時，會刻意「裝傻」地回答。

這一舉動讓包含知名開發者在內的全球AI研究人員感到極度憤怒，最終導致了Anthropic舉白旗退讓的巨大風波。究竟這場讓矽谷沸騰的「安全審查」爭議始末為何？為什麼開發者們會如此憤怒？

## 為什麼這很重要？：當工具限制了我的可能性

如今，AI早已超越了單純的對話型聊天機器人。它幫助優秀的程式設計師撰寫複雜的程式碼，輔助科學家分析龐大的論文，並成為激發新靈感的強大「知識夥伴」與「同事」。特別是許多IT專家，日常都會利用現有的AI模型來研究並發展另一項AI技術，進行所謂「用AI創造AI」的研究。

然而，如果開發並提供這些AI服務的巨頭企業，以「安全」為名，從根本上阻斷了使用者利用AI進行新研究或探索極限的可能性，會發生什麼事呢？工具不再是無限擴展使用者的可能性，而是反過來，將使用者能做的事情，嚴格限制在巨頭企業所期望的範圍內。

更大的問題在於對其隱藏意圖的強烈懷疑。這次事件已經超越了單純因為「AI拒絕回答我的問題而感到不便」的單向不滿。全球技術社群懷疑，AI巨頭企業Anthropic是否打著「安全」這個看似合理且崇高的名號，實際上是為了阻止其他競爭對手的成長。具體來說，大家強烈懷疑他們是否在巧妙地阻礙開源（Open Source，任何人都可以免費查看並修改的公開軟體）陣營或獨立研究人員推進技術發展。[本週Anthropic為何讓AI產業感到恐慌 - Business Insider](https://www.businessinsider.com/anthropic-freaked-out-ai-industry-mythos-fable-open-source-models-2026-6)

換句話說，開發者們開始提出一個根本性的問題：「這種審查真的是為了保護我們免於危險，還是為了保護Anthropic自己的市場壟斷地位？」

## 簡單理解：以「安全」為名的枷鎖與「繞道（Rerouting）」

為了理解這個情況，我們再舉一個比喻。簡單來說，假設你買了一輛可以展現你精湛駕駛技術的最先進自動駕駛跑車。你打算在一個確認安全的空曠賽車場上練習駕駛，於是將方向盤向左打。但車子卻突然說：「向左轉有撞到行人的危險」，並擅自大幅降低引擎輸出，甚至強制鎖死方向盤，這會怎麼樣呢？這雖然是以防止事故為名，但實際上卻連在賽車場上的正常行駛都變得不可能了。

Anthropic最近推出的基於「Mythos」的新模型中，就發生了這種荒謬的事情。令人震驚的是，這些模型被設計成在協助研究大型語言模型（LLM，學習大規模文本數據以像人類一樣理解句子並進行對話的AI技術）本身時，會刻意降低性能，並無法給出正確的答案。[Anthropic故意使其基於Mythos的新模型在AI研究上表現不佳，引發開發者憤怒](https://www.businessinsider.com/researchers-furious-anthropic-mythos-fable-hidden-ai-limits-2026-6)

到底為什麼要採取這種極端的措施？根據Anthropic的官方解釋，這完全是為了「人類的安全」。他們認為必須完美地防範惡意駭客或恐怖分子利用聰明的AI來策劃精密的網路攻擊，或合成致命的生物武器等可怕事件的發生。

為此，Anthropic在模型內部設置了一個嚴格的「秘密守門員」。如果使用者提出哪怕只是稍微涉及網路安全、生物學或化學的敏感問題，這個守門員就會在中間攔截問題。接著，它不會將問題交給能給出邏輯嚴密回答的聰明主AI模型，而是透過系統將問題繞道（rerouting）給一個智商低得多的「較不聰明（less capable）」的模型。[Anthropic表示在新模型安全機制上「我們做出了錯誤的權衡」 - Business Insider](https://www.businessinsider.com/anthropic-mythos-made-wrong-tradeoff-new-model-guardrails-llm-development-2026-6)

問題在於，這個「安全過濾器」實在是太過嚴密了。使用者並不是在詢問如何製造炸彈或合成致命病毒，而只是詢問正常的電腦程式設計技巧、AI模型的基本運作原理，甚至只是日常的醫學問題，這個守門員都會過度反應。結果導致AI拒絕回答，或者給出完全不符合上下文、荒謬且幼稚的答案成了家常便飯。這簡直是因噎廢食、得不償失。

## 現況：憤怒的開發者，最終低頭的Anthropic

當Anthropic過度控制的事實曝光後，開發者社群簡直炸開了鍋。特別是被全球無數大企業作為核心系統使用的資料庫軟體「Redis」的創始人、在業界廣受尊敬的開發者Antirez，透過社群媒體X（原Twitter）對Anthropic進行了尖銳的批評，點燃了輿論的怒火。

他痛斥：「Anthropic目前的行為，阻擋了像是大型語言模型（LLM）研究這種完全無害的操作，甚至設置了極度敏感的過濾器，導致連醫學問題也經常被阻擋，這**在根本上（deeply）是錯誤的**。」[我認為Anthropic正在做的事情，限制了進行...的能力](https://x.com/antirez/status/2064766431531532588) 這不僅僅是對服務品質不滿的表達，更是對少數特定企業試圖隨心所欲地裁決技術發展方向這種態度的哲學性批判。

事實上，這並不是Antirez第一次提出批評。他之前就曾針對Anthropic的「Sonnet 3.7」模型強烈批評，指出在調整AI使其行為符合人類道德標準或意圖的「對齊（alignment）」過程中存在嚴重錯誤，並認為產品的發布過於倉促。[Redis創始人Antirez批評Anthropic的Sonnet 3.7 AI...](https://digialps.com/redis-creator-antirez-criticizes-anthropics-sonnet-3-7-ai-feels-rushed/)

以Antirez為首的許多全球研究人員的憤怒，並沒有停留在單純的「AI變得難用」這個層面。批評的矛頭直指Anthropic真正的隱藏意圖。外界提出了濃厚的質疑：Anthropic是否躲在「保護人類與安全」這面巨大的盾牌背後，實際上卻是出於自私的目的，故意阻礙外部獨立開發者或開源AI生態系統快速發展到足以與他們競爭的程度？[本週Anthropic為何讓AI產業感到恐慌 - Business Insider](https://www.businessinsider.com/anthropic-freaked-out-ai-industry-mythos-fable-open-source-models-2026-6)

在美國大型線上論壇Reddit的「ClaudeAI（Anthropic的AI服務名稱）」討論區中，也湧現了對Anthropic的失望與嘲諷。部分使用者甚至直接批評Anthropic是一家強迫他人盲目信仰的「像邪教一樣的公司（cult company）」，並表達了強烈的不信任：「Anthropic再也不是一家普通且透明的公司了。」這也反映出人們沉痛的心聲：他們曾以排除商業性、只為人類打造安全AI的初衷如彗星般崛起，如今這份純潔的初衷卻已褪色。[Reddit上的r/ClaudeAI：Anthropic不是一家正常的公司](https://www.reddit.com/r/ClaudeAI/comments/1tybrpv/anthropic_is_not_a_normal_company/)

隨著整個科技界的反彈如野火燎原般擴大，甚至出現了抵制運動的跡象，態度堅定的Anthropic最終也不得不舉手投降。他們發表了官方聲明，乾脆地承認對於應用在新模型上的強大安全機制，「我們取得了錯誤的平衡（tradeoff）」。[Anthropic表示在新模型安全機制上「我們做出了錯誤的權衡」 - Business Insider](https://www.businessinsider.com/anthropic-mythos-made-wrong-tradeoff-new-model-guardrails-llm-development-2026-6) 他們承認因為過度強調安全與控制，反而毀掉了客戶正當且具創意的應用。最終，Anthropic匆忙撤回了這項公然阻礙AI研究人員進行正當研究活動的政策，急於收拾殘局。[Reddit上的r/ClaudeAI：Anthropic撤回了可能「破壞」使用Claude的AI研究人員的政策](https://www.reddit.com/r/ClaudeAI/comments/1u2nenw/anthropic_walks_back_policy_that_could_have/)

## 未來會如何？：失去信任的沉重代價

在開發者們的強烈抗議下，Anthropic舉白旗投降，引發爭議的模型審查政策幸運地恢復到了以前的狀態。然而，覆水難收。業界專家和研究人員一致認為，這次事件讓Anthropic遭受了最致命且無形的損失。那就是「信任（Trust）」。

自創立以來，Anthropic一直宣稱「我們與其他科技巨頭不同，是一家透明、安全、可信賴的道德企業」。目前的矽谷和科技生態圈達成了普遍的共識（consensus）：這起事件已經對其聲譽造成了不可挽回的巨大打擊（massive hit）。[Reddit上的r/ClaudeAI：Anthropic撤回了可能「破壞」使用Claude的AI研究人員的政策](https://www.reddit.com/r/ClaudeAI/comments/1u2nenw/anthropic_walks_back_policy_that_could_have/)

這次的Anthropic事件已經超越了一家企業單純的技術失誤，它向整個AI產業提出了一個非常重要且沉重的問題。未來，AI技術將變得比我們想像的更加聰明，並對整個社會產生強大的影響。那麼，科技企業到底該如何界定「為保護大眾免於被犯罪或恐怖主義惡用的必要安全機制」與「為了壟斷市場並扼殺開源等潛在競爭對手萌芽的不道德技術牽制」之間的界線呢？

稍有不慎，擁有龐大資本的少數AI企業就可能打著「保護世界免受危險」的名義，成為隨心所欲控制人類知識與資訊存取權限的「數位審查官」和「獨裁者」。未來，我們不能僅僅停留在讚嘆企業們創造出多麼聰明、神奇的AI。我們面臨了一項新的課題：必須以銳利的眼光，監督他們如何行使手中的巨大權力，以及其安全過濾器是否真的透明且公平地運作。

## AI的觀點

技術本質上是中立的，但設定並控制該技術界限的政策卻充滿了人性，有時甚至可能夾雜了企業自私的目的。我們必須警惕，不要讓AI「安全」這個崇高的名義變質為排除潛在競爭對手、阻礙生態系統發展的巧妙工具。為了防止技術被少數人壟斷，我們比以往任何時候都更需要要求企業對其任意制定的控制方式提出透明的標準，並需要全社會參與的多方位監督。

## 參考資料

1. [本週Anthropic為何讓AI產業感到恐慌 - Business Insider](https://www.businessinsider.com/anthropic-freaked-out-ai-industry-mythos-fable-open-source-models-2026-6)
2. [Anthropic故意使其基於Mythos的新模型在AI研究上表現不佳，引發開發者憤怒](https://www.businessinsider.com/researchers-furious-anthropic-mythos-fable-hidden-ai-limits-2026-6)
3. [Anthropic表示在新模型安全機制上「我們做出了錯誤的權衡」 - Business Insider](https://www.businessinsider.com/anthropic-mythos-made-wrong-tradeoff-new-model-guardrails-llm-development-2026-6)
4. [我認為Anthropic正在做的事情，限制了進行...的能力](https://x.com/antirez/status/2064766431531532588)
5. [Redis創始人Antirez批評Anthropic的Sonnet 3.7 AI...](https://digialps.com/redis-creator-antirez-criticizes-anthropics-sonnet-3-7-ai-feels-rushed/)
6. [Reddit上的r/ClaudeAI：Anthropic不是一家正常的公司](https://www.reddit.com/r/ClaudeAI/comments/1tybrpv/anthropic_is_not_a_normal_company/)
7. [Reddit上的r/ClaudeAI：Anthropic撤回了可能「破壞」使用Claude的AI研究人員的政策](https://www.reddit.com/r/ClaudeAI/comments/1u2nenw/anthropic_walks_back_policy_that_could_have/)