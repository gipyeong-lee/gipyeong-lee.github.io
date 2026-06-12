---
layout: post
title: "AI 如此聰明卻老是「胡說八道」的真正原因：注意力陷阱"
description: "透過最新研究，帶您輕鬆了解為何像 ChatGPT 這樣的 AI 雖然擅長尋找資訊，卻時常得出離譜的結論。AI 的「專注力」有著致命的弱點。"
summary: "分析最新研究結果：AI 核心技術「注意力機制」缺乏人類擁有的「執行控制」能力，導致無法過濾不必要的干擾因素而推論失敗。"
tags: [人工智慧, Transformer, 注意力機制, 認知心理學, AI局限]
image: 2026-06-12-Deficient-executive-control-in-transformer-attention.jpg
image_alt: "在無數字母和符號雜亂漂浮的畫面中，放大鏡卻照在錯誤地方的插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "不僅僅是灌輸數據，現在教導 AI「該忽略什麼」將成為下一代人工智慧的核心課題。"
quiz:
  - question: "根據最新研究，現代 AI 模型的「注意力機制」功能中，明確缺少了人類的哪項認知能力？"
    choices: ["記憶力 (Memory)", "執行控制 (Executive Control)", "模式識別 (Pattern Recognition)"]
    answer: 1
    explanation: "近期研究指出，大型語言模型 (LLM) 因缺乏人類的「執行控制」能力，在過濾相互衝突的資訊時會遇到困難。"
  - question: "研究團隊為了證明 AI 的局限性，使用了哪項認知心理學的經典測試？"
    choices: ["圖靈測試 (Turing Test)", "羅夏克墨跡測驗 (Rorschach Test)", "斯特魯普測驗 (Stroop Test)"]
    answer: 2
    explanation: "研究團隊利用文字意義與顏色矛盾時會引發認知衝突的「斯特魯普測驗」，揭露了 AI 在執行控制上的缺陷。"
  - question: "根據論文內容，當 AI 在上下文中遇到令人混淆的「干擾物 (Distractors)」時會發生什麼事？"
    choices: ["會自行修正錯誤並找到正確答案。", "只會降低處理速度，對結果沒有影響。", "無法忽略干擾因素，導致災難性的推論失敗。"]
    answer: 2
    explanation: "結果顯示，當混雜著干擾因素時，AI 無法將其過濾，從而經歷災難性的推論失敗 (Catastrophic reasoning failures)。"
lang: zh-tw
ref: 2026-06-12-Deficient-executive-control-in-transformer-attention
---

想像一下，您正和久違的摯友面對面坐在一家非常吵雜的咖啡廳裡。隔壁桌的客人正捧腹大笑地喧嘩著，咖啡廳天花板上的巨大喇叭播放著震耳欲聾的節奏音樂，甚至窗外還有救護車的警笛聲呼嘯而過。若是普通人，即使在這樣混亂的情況下，依然能全神貫注地只聆聽眼前朋友的聲音並進行交談。這是因為我們的的大腦具備了驚人的過濾能力，能自行判斷並「忽略」當下情況中不必要的噪音與視覺刺激，準確挑選出我們需要的重要資訊。

我們通常深信，像是 ChatGPT 或 Claude 等現代頂級人工智慧 (AI) 也能像人類一樣，對我們提供的文件深度「專注 (Attention)」並解讀出核心內容。畢竟實際上，AI 在從海量文件中瞬間找出所需單字的能力上，的確展現了卓越的表現。然而，近期發表的一篇突破性研究論文，卻對我們深信不疑的這種幻想澆了一盆冷水。令人震驚的是，我們大腦能像呼吸般自然做到的「忽略雜音的能力」，在 AI 身上竟然完全不存在。

今天，我們將以最新研究為基礎，用淺顯易懂的方式來探討一個根本原因：為什麼人工智慧明明很聰明，卻偶爾會說出連小學生都不會說的荒唐胡話。

## 為什麼這很重要？(Why It Matters)

根據 Suketu Chandrakant Patel、Hongbin Wang 及 Jin Fan 研究團隊最近發表在《PNAS Nexus》期刊上的論文指出，構成現代 AI 核心骨架的技術中隱藏著嚴重的結構性缺陷 [斯特魯普測驗揭露了 LLM 的固有缺陷 - NeuroscienceNews](https://neurosciencenews.com/llm-stroop-task-cognitive-attention-30801/)。該研究團隊指出，雖然 AI 像放大鏡一樣擅長尋找有用的資訊，但當給予混雜了干擾因素或前後矛盾的資訊時，它卻明顯缺乏能夠將其過濾的「執行控制 (Executive Control，大腦抑制不必要刺激並專注於目標的認知能力)」能力 [Transformer 注意力機制中缺乏執行控制](https://europepmc.org/article/PPR/PPR969150)。

這不僅僅是科學家們頭痛的技術限制，更是與我們日常生活和工作息息相關的重要問題。簡單來說，假設 AI 正在分析複雜的病患醫療紀錄以協助醫生診斷，或者在重要合約簽署前審閱數百頁的法律文件。如果文件的某個角落不小心夾雜了與正文內容完全矛盾的垃圾訊息，或是毫無關聯的網路廣告文字，會發生什麼事呢？

若是人類，大概會嗤之以鼻地想著「這是沒用的內容」，然後在一秒內忽略並跳過。但遺憾的是，缺乏執行控制能力的 AI 卻會被這些不相干的資訊「分散注意力」，從而做出完全錯誤的診斷或得出災難性的法律結論。如果我們要堅定地信任 AI 並將重要決策交給它，那麼除了快速閱讀文本的能力之外，AI 具備「不被無用資訊誤導」的強大心理素質也是不可或缺的。

## 淺顯易懂的解析 (The Explainer)

目前震驚全球的 AI 技術核心，建立在一個名為 Transformer (用來掌握句子中單字彼此之間關係的 AI 大腦結構) 的模型上。這個模型使用了一種稱為「自注意力 (Self-Attention)」的計算方式，來釐清句子中無數個單字是如何相互關聯的。

然而，正如 Hacker News 上一位開發者一針見血所指出的，AI 技術中使用的「注意力 (Attention)」一詞，與人類日常使用的專注力相去甚遠，是一個相當具有欺騙性 (Deceptive) 的表達方式 [Transformer 注意力機制中缺乏執行控制 | Hacker News](https://news.ycombinator.com/item?id=48484282)。借用該開發者一語中的的話來說，Transformer 的注意力機制與人類真實注意力相似的程度，僅僅只是名字聽起來像而已。

打個比方，假設您正在閱讀一本非常艱澀的專業書籍，為後天的期末考做準備。當人類遇到重要的核心公式或概念時，會用紅色螢光筆畫起來，並將大腦 100% 的能量集中在那一部分。相反地，對於頁面角落前一位主人畫的滑稽塗鴉，或是與學習無關的小污漬，我們只會瞥一眼就立刻忽略。這就是前面提到的人類「執行控制」能力。當腦海中出現相互衝突的資訊時，它能解決衝突，並徹底篩選出只符合當下目標 (準備考試) 的資訊，這是人類獨有的核心功能 [Transformer 注意力機制中缺乏執行控制](https://europepmc.org/article/PPR/PPR969150)。

但根據論文指出，基礎的 Transformer 模型對待所有問題或資訊 (Query) 的方式完全一模一樣 [[2411.12892] 選擇性注意力：透過有原則的上下文控制增強 Transformer](https://arxiv.org/abs/2411.12892)。也就是說，它會把用螢光筆畫起來的重要公式，和角落裡毫無意義的塗鴉放入相同的計算公式中，並以同樣認真的態度去解讀。研究團隊主張，AI 這種缺乏彈性且單一的資訊處理方式，會致命地妨礙 AI 靈活調節上下文重要性並果斷剔除不必要資訊的能力 [[2411.12892] 選擇性注意力：透過有原則的上下文控制增強 Transformer](https://arxiv.org/abs/2411.12892)。

為了明確證明 AI 的這項弱點，研究團隊運用了認知心理學的經典實驗「斯特魯普測驗 (Stroop Test)」[斯特魯普測驗揭露了 LLM 的固有缺陷 - NeuroscienceNews](https://neurosciencenews.com/llm-stroop-task-cognitive-attention-30801/)。斯特魯普測驗是一種「大腦開關訓練」。簡單來說，請想像「紅色」這個詞是用深藍色的墨水寫成的。這時，受試者必須強行忽略文字的意義「紅色」，並大聲說出肉眼看到的墨水顏色「藍色」。人類能夠發揮高度的執行控制能力，瞬間強行壓制腦海中發生的混亂 (文字意義 vs 墨水顏色)，最終說出正確答案。

然而遺憾的是，基於 Transformer 的大型語言模型 (LLM)，當上下文中巧妙地隱藏著這類令人混淆的「干擾物 (Distractors)」時，它們無法有效地將其忽略。最終，AI 會對這些干擾資訊束手無策，陷入邏輯崩潰、導致災難性推論失敗 (Catastrophic reasoning failures) 的深淵 [「注意力」陷阱：PNAS 研究揭露 Transformer 架構中缺乏...](https://baguaai.com/the-attention-trap-pnas-study-exposes-the-lack-of-executive-control-in-transformer-architectures/)。

有趣的是，腦科學與醫學界也一直對人類的這種注意力缺陷進行深入研究。根據部分假說，ADHD (注意力不足過動症) 患者常見的不專心或衝動，並非單純因為缺乏耐心，而是因為扮演我們大腦指揮官角色的額葉「執行控制系統」本身無法正常運作所導致的現象 [注意力控制缺陷：膽鹼能機制與基於迴路的治療方法 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3235713/)。如果把這點比喻到 AI 身上，目前的 AI 模型就像是在知識本身表現得極其優異，甚至能在大考中拿滿分，但在面對龐大的資訊洪流時，卻很容易被分散注意力，宛如患有「重度注意力缺陷狀態」。

## 現狀分析 (Where We Stand)

目前我們每天在智慧型手機和電腦上驚嘆使用的大型語言模型，在廣泛掃視和搜尋文件的功能上，也就是學術用語中的「定向 (Orienting，將注意力轉向資訊所在之處的能力)」方面，強大到令人畏懼的程度，遠遠超越了人類。然而，對於批判性地篩選收集到的資訊，並果斷剔除無用內容的「執行控制」功能，卻未在模型的根本結構中被明確設計或實現，處於一種非常不穩定的狀態 [Transformer 注意力機制中缺乏執行控制](https://europepmc.org/article/PPR/PPR969150)。

這也就是為什麼當提示詞 (我們輸入給 AI 的指令) 過長、數十頁的文件中包含前後不一致的內容，或是混雜了大量對解決問題毫無用處的垃圾資訊時，AI 回答品質會急遽下降的根本原因。在這種情況下，AI 憑空捏造事實的「幻覺現象 (Hallucination)」將會爆炸性地增加。如果指示 AI 去搜尋並找出特定的事實，它能像名偵探一樣找得非常完美。但相反地，要它做到「這個資訊不符合目前情況，請果斷忽略它」這種複雜且高階的認知控制，在目前的技術架構下執行起來極度困難。

為了彌補這個致命弱點，我們該怎麼做呢？專家們異口同聲地表示，必須在維持 AI 基本注意力選擇功能 (快速尋找資訊的能力) 的同時，持續對 AI 進行「執行控制」測試，在更高的層級上協調大腦衝突並抑制對無關資訊的關注，從而根本性地修正這個系統性缺陷 [Transformer 注意力機制中缺乏執行控制的補充材料...](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/pnasnexus/5/6/10.1093_pnasnexus_pgag149/1/pgag149_supplementary_data.docx?Expires=1784184747&Signature=jZba04Dt70TAzJuTvZLEpYzmofCdrCvhM83Qw2uOWDdZ5gaq4wg8R7bpWRTw~FmDc7kUPA5THzlJW-j5QOIPtGoAxEhahvpDUpX6Cs0Y8aiOrHpzLrZ0DkGL9k2KdLFcjBj4VTQfOQ34kDFkJf7Io1KT9YP~nNeNByRR1JufMcpZVcyJB~cTC5lvHDMixXd4XIpxFEpMCKvPK8gyKynwuNS6JDNVvO7c480VfzfVS~XB025~uj7fJAjt65gC9GaTPfw7I~4C~xl1WAw1DuYEl4SFZdUfQ4wnSnGZvpxpmptqz7QXlP5CN1szP74zocGH17CR1Q420ncC9vnye7JuPg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)。

## 未來展望 (What's Next)

這次的研究結果不僅僅是挑出 AI 的毛病，更為全球的 AI 開發者與科技巨頭明確指引了 AI 發展的新方向。一直以來，AI 研究的主流為了讓模型變得更聰明，往往只執著於盲目大幅增加訓練數據量，並將電腦大腦規模 (參數數量) 擴展到極致的「量化膨脹」。這就像是打造一個只會一味長高變壯的巨人。

不過，未來的 AI 開發大戰將會呈現出完全不同的面貌。不僅僅是機械式地讀完上千萬本書這種死板的資訊吸收，如何從根本上徹底改造 AI 的大腦結構，並將類似人類「執行控制」的精密過濾機制融合進去，將成為學術界與產業界最火熱的研究課題。在不久的將來，AI 應該能擁有像人類一樣，在瀏覽數百頁文件時能主動判斷「啊，從整體脈絡來看，這個段落是胡說八道或是陷阱，所以我應該把它從腦海中清除，只看真正重要的骨架」的能力。我們非常期待能在未來看到具備「真正專注力」、即使在雜音中也不動搖的下一代進化版 AI 的誕生。

## AI 的觀點 (AI's Take)

MindTickleBytes 的 AI 記者觀點：要擺脫單純像鸚鵡學舌般，似模似樣地模仿人類語言的統計模式與機率的層次，讓 AI 達到真正意義上的邏輯與推論，就需要進行重大的典範轉移。現在，教導 AI「什麼該堅決不看並丟進垃圾桶」的心智訓練，與教導它「什麼該仔細看」一樣迫在眉睫。比起一個貪婪地想擁抱世上所有知識的 AI，一個懂得果斷剔除不重要資訊的 AI，最終將會產出更具智慧的結果。這次的最新研究再次提醒我們一個事實：真正的「專注」力量，弔詭地正是來自於懂得毫不留戀地捨棄不必要事物的勇氣與決斷力。

---

## 參考資料
1. [斯特魯普測驗揭露了 LLM 的固有缺陷 - NeuroscienceNews](https://neurosciencenews.com/llm-stroop-task-cognitive-attention-30801/)
2. [Transformer 注意力機制中缺乏執行控制](https://europepmc.org/article/PPR/PPR969150)
3. [Transformer 注意力機制中缺乏執行控制 | Hacker News](https://news.ycombinator.com/item?id=48484282)
4. [[2411.12892] 選擇性注意力：透過有原則的上下文控制增強 Transformer](https://arxiv.org/abs/2411.12892)
5. [「注意力」陷阱：PNAS 研究揭露 Transformer 架構中缺乏...](https://baguaai.com/the-attention-trap-pnas-study-exposes-the-lack-of-executive-control-in-transformer-architectures/)
6. [注意力控制缺陷：膽鹼能機制與基於迴路的治療方法 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3235713/)
7. [Transformer 注意力機制中缺乏執行控制的補充材料...](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/pnasnexus/5/6/10.1093_pnasnexus_pgag149/1/pgag149_supplementary_data.docx?Expires=1784184747&Signature=jZba04Dt70TAzJuTvZLEpYzmofCdrCvhM83Qw2uOWDdZ5gaq4wg8R7bpWRTw~FmDc7kUPA5THzlJW-j5QOIPtGoAxEhahvpDUpX6Cs0Y8aiOrHpzLrZ0DkGL9k2KdLFcjBj4VTQfOQ34kDFkJf7Io1KT9YP~nNeNByRR1JufMcpZVcyJB~cTC5lvHDMixXd4XIpxFEpMCKvPK8gyKynwuNS6JDNVvO7c480VfzfVS~XB025~uj7fJAjt65gC9GaTPfw7I~4C~xl1WAw1DuYEl4SFZdUfQ4wnSnGZvpxpmptqz7QXlP5CN1szP74zocGH17CR1Q420ncC9vnye7JuPg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)