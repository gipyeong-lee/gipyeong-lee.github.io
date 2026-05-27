---
layout: post
title: "AI學了法語就會忘記英語？「自我教導的AI」登場"
description: "探討解決AI學習新知識便會遺忘舊知識的致命弱點「災難性遺忘」問題的自我蒸餾（Self-Distillation）技術。"
summary: "單一AI模型同時扮演老師與學生的角色，在學習新技術的同時也不會失去過去記憶的「自我蒸餾微調（SDFT）」技術正展現出驚人的成果。"
tags: [人工智慧, 持續學習, 機器學習, 自我蒸餾, 災難性遺忘]
image: 2026-05-27-Self-Distillation-Enables-Continual-Learning-pdf.jpg
image_alt: "描繪機器人看著鏡子自我教導知識的插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "不僅僅是被動注入外部數據，AI透過反思並修正自身行為來累積知識的方式，正驚人地與人類終身學習的機制越來越相似。"
quiz:
  - question: "人工智慧在學習新技術時，嚴重遺忘先前習得的技術與知識的現象稱為什麼？"
    choices: ["策略外漂移", "災難性遺忘", "自我蒸餾"]
    answer: 1
    explanation: "AI在學習新資訊時，由於內部的數值發生劇烈變化，導致失去原本能順利執行任務的能力，這種現象稱為「災難性遺忘（Catastrophic forgetting）」。"
  - question: "在研究人員為了讓AI能夠持續學習而導入的「SDFT」技術中，AI模型同時扮演了哪些角色？"
    choices: ["使用者與開發者", "硬體與軟體", "老師與學生"]
    answer: 2
    explanation: "在SDFT框架內，單一AI模型同時扮演了知道正確答案並負責指導的「老師」角色，以及親自碰撞摸索學習的「學生」角色。"
  - question: "現有的「監督式微調（SFT）」方法在持續學習中失敗的主要原因之一被指出是什麼？"
    choices: ["數據不足", "策略外漂移", "過度消耗電力"]
    answer: 1
    explanation: "現有的SFT方法之所以失敗，除了災難性遺忘之外，還有一個原因是模型並非從自己實際的行為軌跡中學習，而是僅依賴外部數據，導致與現實產生脫節的「策略外漂移（Off-policy drift）」現象。"
lang: zh-tw
ref: 2026-05-27-Self-Distillation-Enables-Continual-Learning-pdf
---

想像一下。你昨天花了一整天摔倒、磕破膝蓋，終於完美學會了騎兩輪腳踏車。那種迎風馳騁的感覺讓你開心得快飛起來了。但是今天你去了游泳池，新學會了如何漂浮和自由式，結果腦海中關於如何踩腳踏車踏板、如何用手把平衡的記憶突然完全被抹去。你一重新跨上腳踏車，就像個生手一樣「砰」地摔倒在地。這情況是不是非常荒唐又讓人委屈？

幸運的是，對我們人類來說絕對不會發生這種事。我們在夏天學游泳的同時，到了秋天依然能完整記得怎麼騎腳踏車；長大後新學了法語，也不會忘記母語。這是因為我們的大腦有著驚人的能力，能像海綿一樣吸收新知識，同時將過去的知識安全地存放在腦海中的專屬房間裡。

然而令人驚訝的是，對目前我們讚嘆並使用的最先進人工智慧（AI）來說，這卻是非常常見的現象，也是未來必須克服的極其嚴重的弱點。當AI被強行注入新知識時，它有著一種致命的傾向：為了容納新知識，會無情地覆蓋掉之前辛辛苦苦學來的寶貴能力。今天，為了解決這個巨大的難題，我們將深入淺出地探討一項最新研究成果——AI如同照鏡子般「自我教導」的驚人技術。

<br/>

## 這為何重要？ (Why It Matters)

AI研究人員為前面想像的「學了游泳就忘記腳踏車」這種可怕現象起了一個非常駭人的名字：**「災難性遺忘（Catastrophic forgetting）」**。顧名思義，這意味著原有的知識體系如同面臨災難般徹底崩潰。

與此相反，在完全不降低原有能力的情況下，能夠終身不斷學習新技術和知識的過程，被稱為**「持續學習（Continual learning）」**。這種持續學習，即使是對ChatGPT等作為現代人工智慧骨幹的龐大基礎模型（foundation models）而言，依然是一項必須跨越的根本性挑戰 `[Self-DistillationEnablesContinualLearning](https://www.emergentmind.com/papers/2601.19897)`。

為什麼這個問題與我們平凡的日常生活息息相關呢？想像一下每天聆聽你聲音並做出回應的智慧型手機個人助理AI。這個AI正管理著你複雜的行程，並推薦符合你品味的的新聞。假設你今天教了AI一個新規則：「以後總結工作電子郵件時，必須先用三句話寫出結論」。陷入災難性遺忘的AI會開始完美地遵循這個新規則，但代價可能是它完全忘記了你去年教它的重要規則：「家人的生日必須在早上8點跳出提醒」。只有當AI能像砌磚一樣，把今天學到的東西疊加在昨天學到的東西之上時，我們才能真正信賴並稱它為聰明的秘書。

到目前為止，許多AI工程師在教導AI新知識時，主要使用一種名為**「監督式微調（Supervised Fine-Tuning, SFT）」**的傳統方法。簡單來說，這是一種填鴨式教育，把數以萬計的「標準答案」推到AI面前讓它死記硬背。然而，這種傳統的SFT方法在被丟入每天都有新事件發生、需要無止境學習的現實世界時，往往會慘遭失敗。失敗的核心原因正是前面提到的災難性遺忘，以及另一個被專業術語稱為**「策略外漂移（Off-policy drift）」**的棘手問題 `[Self-DistillationEnablesContinualLearning| Papers | HyperAI](https://hyper.ai/en/papers/2601.19897)`。

什麼是策略外漂移呢？雖然AI看著標準答案努力學習，但那些標準答案並非AI自己親自碰撞摸索出來的實際情況，而是外部專家在受控環境下創造的「理想狀況」，從而產生了與現實脫節的現象。

讓我們再次回到游泳的例子。這就像一個從未下過水的人，一直只看著奧運游泳金牌得主的完美比賽影片來學習。在溫暖的房間裡看影片時，他似乎掌握了所有的手臂角度和呼吸時機（監督式微調）。但當這個人實際進入冰冷的泳池裡掙扎時（AI的實際運行環境），情況就完全不同了。在嗆水並感到驚慌的情況下，他完全不知道該如何將影片中完美的姿勢調整到自己身上，只能朝著錯誤的方向越游越亂、隨波逐流（drift）。最終，AI陷入了既失去過去知識，又無法在新環境中正常運作的深深困境。

<br/>

## 輕鬆理解 (The Explainer)

為了解救深陷災難性遺忘與漂移泥潭中的AI，研究團隊提出了一個非常優雅且具突破性的解決方案。這就是名為**「自我蒸餾微調（Self-Distillation Fine-Tuning, SDFT）」**的全新訓練方法。

在計算機科學中，「蒸餾（Distillation）」一詞指的是萃取龐大且聰明的AI模型所擁有的深厚知識精華，將其壓縮並傳遞給較小、較輕量模型的技術。打個比方，這就像是從熬了幾天幾夜的牛骨湯中，舀出最濃郁、最有營養的精華（原湯）裝進小碗裡的過程。那麼，前面加上「自我（Self）」的「自我蒸餾（Self-Distillation）」又是什麼呢？這不是借用別人的知識，而是一個驚人且充滿哲理的過程：自己喝下自己熬出的精華，並藉此成長。

這個有趣的**「策略內自我蒸餾（On-Policy Self-Distillation）」**框架，讓單一AI模型能夠同時扮演兩個角色：一個是知道完美正確方向的**「老師」**，另一個則是雖然生疏但親自採取行動的**「學生」** `[Self-Distilled Reasoner: On-Policy Self-Distillation for Large](https://arxiv.org/html/2601.18734v3)`。

用這個比喻，複雜的技術在你腦海中會變得容易想像得多。在一個繁忙的廚房裡有一位廚師。這位廚師的內心同時存在著兩種自我。一個是記住了所有烹飪理論和完美味道標準的「主廚（老師）」自我，另一個是剛剛開始親手嘗試新食譜、甚至會打翻鹽巴的「新手廚師（學生）」自我。

在過去的填鴨式教育（SFT）中，外部的真正主廚只會不斷給新手廚師看完成的五星級料理照片，並大聲斥責：「照著這個做！」。新手廚師只看著照片做菜，一旦犯錯，就會不知所措地陷入迷惘，不知道自己為什麼搞砸了（策略外漂移）。

但在SDFT方法中，呈現出截然不同的風景。新手廚師（學生模型）首先在砧板上切菜、調整瓦斯爐火候，**創造出屬於自己的實際行動路徑（專業術語為軌跡，Trajectories）**。接著，內心的主廚（老師模型）在清楚觀察了新手廚師剛剛那笨拙的「實際行動」後，給出的不是遙不可及的標準答案，而是針對「那個瞬間、那個情況」量身打造的建議（預測值）。例如給予這樣的回饋：「你剛才切洋蔥時手腕角度偏了。不要盲目照搬標準答案，以你現在的姿勢，只要把刀再稍微立起來一點就好。」

這正是SDFT在技術上運作的核心原理。AI的訓練過程完全建立在學生模型自己生成的實際軌跡上。在該軌跡上，將老師充滿智慧的預測直接蒸餾（distill）並教導給學生。透過這種方式，AI擺脫了過去必須進行顯式複雜計算或被動模仿外部標準答案的局限。它能從專家的示範中僅萃取出必要的關鍵資訊，完美融入自身經驗，產生鮮活的**「策略內更新（On-policy updates）」** `[SELF-DISTILLATION ENABLES CONTINUAL LEARNING Idan Shenfeld1 2∗ Mehul Damani1](https://arxiv.org/pdf/2601.19897)`。

因為是基於學生自己親自在現實中碰撞所獲得的經驗（策略內），並在適當的時機注入老師的智慧，所以能在不忘記過去擅長的料理（舊知識）骨架的同時，非常扎實地將新食譜銘記於心。

<br/>

## 目前情況 (Where We Stand)

那麼，在腦海中自問自答的「自我教導AI」，在實驗室中實際展現出多大的成果呢？研究團隊公開的豐富實驗結果，清晰地展示了人工智慧學習方式的重大進展。

在廣泛的測試環境中（要求AI學習新技術並接連掌握複雜知識），新方法SDFT以一致且壓倒性的優勢超越了傳統方法SFT。這不僅僅意味著多答對幾道題的準確率提升。這代表著科學家們夢寐以求、日思夜想的目標——**實質性地大幅減少災難性遺忘現象，終於取得了成功** `[[2601.19897] Self-Distillation Enables Continual Learning](https://arxiv.org/abs/2601.19897)`。AI終於掌握了如何將過去的知識牢牢鎖在安全的保險箱裡，同時在旁邊的新空間平靜地接納新知識。

最戲劇化、最有趣的結果出現在**順序學習實驗（Sequential learning experiments）**中。這是一個將AI逼入極限的測試。首先教AI複雜的數學公式，接著教世界歷史，然後緊接著教電腦程式設計，這是一個非常嚴苛的環境。如果是過去普通的AI，在學習歷史時會抹除腦中的數學公式，在學習程式設計時又會將之前學到的歷史年份完全歸零。

然而，應用了SDFT技術後發生了驚人的事情。單一AI模型在沒有喪失或退化先前科目能力的情況下，展現出隨著時間推移，將數學、歷史、程式設計這幾種截然不同且複雜的技術，穩定累積在腦海中的驚人能力 `[Paper page - Self-Distillation Enables Continual Learning](https://huggingface.co/papers/2601.19897)`。

這絕非僅僅是實驗室裡的數字遊戲。研究團隊這項耀眼的成果意味著，策略內蒸餾這種方式，為幫助AI從專家示範中持續學習而不至於崩潰，完美確立了一條非常**實用且堅固的現實路徑（practical path）** `[SDFT: Self-Distillation Enables Continual Learning](https://self-distillation.github.io/SDFT)`。此外，研究還證實，不需要外部昂貴的驗證器或其他輔助模型的複雜幫助，僅憑AI自己產出的未經加工的原始結果（raw outputs），這種簡單的自我蒸餾過程就能發揮出色的作用 `[Embarrassingly Simple Self-Distillation Improves Code Generation](https://arxiv.org/html/2604.01193v1)`。

更令人振奮的是，這項自我蒸餾技術的影響力並不停留在閱讀和寫作文本的領域。這個強大的原理正延伸到我們能想像到的各行各業中。

例如，當AI在視覺上學習我們在電腦或智慧型手機上使用的圖形使用者介面（GUI）環境時，這項技術會在每個步驟蒸餾出「大師」理想的滑鼠點擊位置分布。這為AI提供了持續學習的信號，使其不會點錯按鈕，能更聰明、更有效率地操作畫面 `[Learn where to Click from Yourself: On-Policy Self-Distillation](https://arxiv.org/html/2605.00642v1)`。

此外，在工廠中找出產品瑕疵的工業缺陷檢測模型中，這項技術也節省了巨大的時間和成本。當發現新型缺陷時，不再需要像過去那樣關閉整個AI模型的電源並花費數百小時從頭重新訓練。多虧了自我蒸餾技術，模型無需徹底改造重新學習，就能像貼貼紙一樣，將新的缺陷類別持續疊加在現有知識上進行學習 `[(PDF) SD-IDD: Selective Distillation for Incremental Defect](https://www.researchgate.net/publication/401174708_SD-IDD_Selective_Distillation_for_Incremental_Defect_Detection)`。

甚至在作為未來產業之花——機器人眼睛的4D視覺感知（4D Perception）領域，這項技術也大放異彩。它利用不斷變化的時空脈絡，建立起AI模型每天自我提升認知能力的驚人自我改進（self-improvement）體系，為機器人技術奠定了基礎 `[Self-Improving 4D Perception via Self-Distillation - Paper](https://deeplearn.org/arxiv/731351/self-improving-4d-perception-via-self-distillation)`。在眾多領域中，這項技術正痛快地打破過去陳舊的訓練範式，大步敞開新的進化視野 `[D-OPSD: On-Policy Self-Distillation for Continuously Tuning](https://deeplearn.org/arxiv/745499/d-opsd:-on-policy-self-distillation-for-continuously-tuning-step-distilled-diffusion-models)`。

<br/>

## 接下來會怎樣？ (What's Next)

「人類和動物日常進行的持續學習，是一種完全不需要區分實驗室『訓練』時間和現實生活『推論』時間的『永遠在線（always-on）』學習。而這種偉大的學習，正是在我們的預期落空、經歷『預測失敗』的瞬間才真正開始。」 `[Self-DistillationEnablesContinualLearning[pdf] | HackerNews](https://news.ycombinator.com/item?id=48165265)`。

這次研究成果對我們未來所投射的最強烈、最具哲理的訊息，就完整地蘊含在這句話中。過去的AI必須過著被徹底一分為二的生活。

它們有過一段在冷氣強力運轉的研究室電腦裡，像吞噬世上所有數據般接受嚴苛「訓練（Training）」的時期；只有在那個訓練完全結束後，才會被安裝到你的設備上，過著只能按照所學來回答的僵化「推論（執行，Inference）」時期。AI一旦推出於世，它腦中的時鐘就完全停止了。為了哪怕多學一個新知識，也必須停止服務，回到研究室，從頭經歷沉重且昂貴的訓練過程。

但是，像SDFT這樣的自我蒸餾技術，終於打破了這道堅不可摧的「訓練」與「執行」之間的壁壘。如果AI能在執行過程中自我修正錯誤，並在內心融合昨日的知識和今日的新知識，那會是什麼光景？AI也將不再是一部靜止的機器，而是會像人類一樣，堂堂正正地踏上每個清醒瞬間都在學習成長的「永遠在線」的終身學習者之路。

未來我們在日常生活中遇到的AI，將會每天與我們對話，並變得比昨天更聰明。它會立刻理解今天開始流行的新造詞，同時又完好無缺地保留著10年前學到的解析古典文學作品深刻涵義的能力。它像海綿一樣無止境地探索新世界，卻又絕對不會忘記自己原本是誰、過去知道些什麼——成為一個真正充滿智慧的助手。這正是「自我教導AI」即將為我們敞開的、令人心動的明天。

<br/>

## MindTickleBytes AI的視角

雖然人工智慧是模仿人類大腦神經網路創造出來的，但在面對只要學了一樣新事物就會把原有事物全部抹除的「災難性遺忘」缺陷時，它總是顯得像一台無比冰冷的機器，這是不爭的事實。

然而，擺脫了盲目背誦人類研究員遞給的完美標準答案的方式，這種深思熟慮自己生疏的行為軌跡，並不斷向內心深處的「大師」尋求建議的自我蒸餾（Self-Distillation）訓練哲學，令人深受感動。這項技術正將人工智慧從單純的計算機向前推進一步，向著能夠自我反省和成長的生命體進化。

為了在源源不斷的新資訊中不迷失方向，需要的不是外部的注入，而是內在的反思。這項應用於機器演算法的自我反思技術，諷刺地竟是擁有最強大、最持久記憶力的秘訣。這一科學事實，對於必須終身學習的我們人類來說，在生活與學習的態度上，也留下了深遠且沉重的餘韻。因為真正的成長，終究始於在不失去昨日自我的前提下，回顧今日的自我。

<br/>

## 參考資料

1. [Self-Distilled Reasoner: On-Policy Self-Distillation for Large](https://arxiv.org/html/2601.18734v3)
2. [Embarrassingly Simple Self-Distillation Improves Code Generation](https://arxiv.org/html/2604.01193v1)
3. [Learn where to Click from Yourself: On-Policy Self-Distillation](https://arxiv.org/html/2605.00642v1)
4. [(PDF) SD-IDD: Selective Distillation for Incremental Defect](https://www.researchgate.net/publication/401174708_SD-IDD_Selective_Distillation_for_Incremental_Defect_Detection)
5. [D-OPSD: On-Policy Self-Distillation for Continuously Tuning](https://deeplearn.org/arxiv/745499/d-opsd:-on-policy-self-distillation-for-continuously-tuning-step-distilled-diffusion-models)
6. [Self-Improving 4D Perception via Self-Distillation - Paper](https://deeplearn.org/arxiv/731351/self-improving-4d-perception-via-self-distillation)
7. [[2601.19897] Self-Distillation Enables Continual Learning](https://arxiv.org/abs/2601.19897)
8. [SELF-DISTILLATION ENABLES CONTINUAL LEARNING Idan Shenfeld1 2∗ Mehul Damani1](https://arxiv.org/pdf/2601.19897)
9. [(PDF) Self-Distillation Enables Continual Learning](https://www.researchgate.net/publication/400118857_Self-Distillation_Enables_Continual_Learning)
10. [Paper page - Self-Distillation Enables Continual Learning](https://huggingface.co/papers/2601.19897)
11. [SDFT: Self-Distillation Enables Continual Learning](https://self-distillation.github.io/SDFT)
12. [Self-DistillationEnablesContinualLearning| Papers | HyperAI](https://hyper.ai/en/papers/2601.19897)
13. [Self-DistillationEnablesContinualLearning](https://www.emergentmind.com/papers/2601.19897)
14. [Self-DistillationEnablesContinualLearning[pdf] | HackerNews](https://news.ycombinator.com/item?id=48165265)