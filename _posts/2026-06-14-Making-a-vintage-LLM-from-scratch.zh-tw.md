---
layout: post
title: "只學習過去知識的 AI 能預測未來嗎？探索「復古 LLM」的世界"
description: "深入淺出地解釋了阻斷最新網路知識、僅以 1930 年代以前的過去數據進行訓練的「復古 LLM (Vintage LLM)」之原理，以及開發者們從零開始親手打造人工智慧的有趣挑戰。"
summary: "越來越多從零開始親手開發僅以過去文本訓練的「復古 LLM」專案出現，這不僅加深了對 AI 結構的理解，也正進行著預測歷史未來的有趣實驗。"
tags: [人工智慧, 大型語言模型, 復古LLM, 科技趨勢, 機器學習]
image: 2026-06-14-Making-a-vintage-LLM-from-scratch.jpg
image_alt: "在放著老舊打字機的木桌上，以全息投影浮現出現代人工智慧神經網路的模樣"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在這個只消費成品的時代，開發者為了領悟底層原理而從頭開始親手組裝 AI 的匠人精神令人驚嘆。"
quiz:
  - question: "開發者們特地從頭開始 (from scratch) 親手打造「復古 LLM」最核心的原因是什麼？"
    choices: ["為了在沒有網路連線的離線環境中商業化銷售聊天機器人", "為了使用組合語言編寫程式碼以直接控制電腦硬體", "為了獲得對大型語言模型在背後如何運作的洞察力，並深入理解其原理"]
    answer: 2
    explanation: "相較於直接使用現成的大型模型，從頭開始親手打造能提供寶貴的洞察力，讓人了解複雜的人工智慧系統在內部是如何運作的。"
  - question: "在本文中，對「復古 LLM」最準確的定義說明為何？"
    choices: ["沒有特定知識截止 (knowledge-cutoff) 日期之後的資訊，僅以受限的歷史時期文本進行訓練的語言模型", "為了能在效能較差的舊型電腦上運作，將功能極度縮減的最新語言模型", "僅使用老舊程式語言開發的 1990 年代風格的人工智慧"]
    answer: 0
    explanation: "復古 LLM 是指僅以特定過去時間點（例如：1930 年代以前，或 2019 年）之前的文本與多模態數據進行訓練，完全不包含該時間點之後未來知識的模型。"
  - question: "本文中提到，在更新現有模型時，不需從頭開始完全重新訓練，只需使用 5% 的運算能力即可防止品質下降並提升速度的技術是什麼？"
    choices: ["奈米GPT (NanoGPT)", "分組查詢注意力機制 (GQA, Group-query attention)", "PyTorch"]
    answer: 1
    explanation: "分組查詢注意力機制 (GQA) 是一種從現有檢查點出發，僅使用原本訓練運算量的 5% 對模型進行升級訓練 (up-training) 的技術，在節省從頭重新訓練成本的同時還能提升效能。"
lang: zh-tw
ref: 2026-06-14-Making-a-vintage-LLM-from-scratch
---

讓我們暫時做個有趣的想像。如果您搭乘時光機回到 1920 年代，只收集那個時代出版的書籍、報紙以及人們的手寫信件，讓人工智慧大量閱讀，會怎麼樣呢？這個人工智慧不會知道智慧型手機或網路是什麼，甚至連發生過第二次世界大戰這個歷史事實都不知道。它會成為一個活生生的「時空膠囊」，只原封不動地保存著 100 年前人們的想法與知識。

如今我們常用的 ChatGPT 等人工智慧，是通曉全球昨日新聞、最新流行語乃至複雜現代科學技術的「萬事通」。然而最近在人工智慧開發者之間，果斷阻斷最新網路知識、僅停留在這種特定過去時代知識的所謂「復古 LLM (Vintage LLM)」，並從零開始親手打造的獨特嘗試，正悄悄成為一股熱潮。

到底為什麼要放著世界上最聰明、最便利的最新技術不用，反而要辛苦地親手組裝被困在過去知識中、有些笨拙(?)的人工智慧呢？今天在 MindTickleBytes，我們將為您深入淺出地解釋這種有趣且奇妙的技術逆行背後所隱藏的驚人秘密。

## 這為什麼重要？ (Why It Matters)

最近在科技界，從智慧型手機到公司業務，各種日常場景都在導入大型語言模型 (LLM，透過學習龐大文本數據來像人類一樣對話與寫作的人工智慧)。當所有人工智慧模型都貪婪地吞噬世界上最新數據以變得更聰明時，一個完全背道而馳的概念出現了。

那就是**「復古 LLM (Vintage LLM)」**。這指的是僅以明確受限歷史時期的文本進行訓練的語言模型，其特徵是訓練數據中完全不包含特定「知識截止 (knowledge-cutoff，人工智慧學習數據的最後日期)」之後的資訊 [[精選復古 LLM 列表... (Awesome-vintage-llms)]](https://github.com/entanglr/awesome-vintage-llms)。

更具體地說，就是僅使用特定日期（例如：COVID-19 疫情爆發前的 2019 年）之前的文本或圖片等有限數據來進行訓練 [[復古大型語言模型]](https://owainevans.github.io/talk-transcript.html?trk=article-ssr-frontend-pulse_little-text-block)。從將該日期之後世界上發生的事情在人工智慧腦中留下一片空白的相對簡單嘗試，到甚至僅使用 1930 年代以前非常古老的數據來創造模型的大膽人工智慧專案，各種實驗正以多樣的方式進行中 [[這個 AI 專案使用 1930 年代以前的數據來創建「復古 LLM」以用於...]](https://www.linkedin.com/posts/tmcai_this-ai-project-uses-pre-1930-data-to-create-activity-7455203545970143232-XqvV)。

那麼，這種看似荒唐的嘗試在我們的現實中為何如此重要？這個實驗並非只是怪咖們模仿過去的惡作劇。透過復古 LLM，研究人員正在提出一個非常龐大且根本的問題：**「僅學習到特定歷史時間點數據的人工智慧，究竟能多準確地預測該時間點之後將發生的歷史事件？」** [[這個 AI 專案使用 1930 年代以前的數據來創建「復古 LLM」以用於...]](https://www.linkedin.com/posts/tmcai_this-ai-project-uses-pre-1930-data-to-create-activity-7455203545970143232-XqvV)。

想像一下。如果一個人工智慧只閱讀了 1929 年經濟大恐慌爆發前夕的經濟指標、人們的信件與報紙文章，它是否能事先警告這場巨大的經濟崩盤呢？這就如同透過人工智慧的數據建模，將長期以來的哲學主題「決定論（宇宙中所有事件皆由過去的原因所決定的哲學概念）」，以縮影形式的社會學實驗加以重現 [[這個 AI 專案使用 1930 年代以前的數據來創建「復古 LLM」以用於...]](https://www.linkedin.com/posts/tmcai_this-ai-project-uses-pre-1930-data-to-create-activity-7455203545970143232-XqvV)。

簡單來說，如果僅透過機械性地仔細分析過去數據就能猜測出未來歷史的軌跡，我們就等於獲得了一顆能預測未來社會與經濟危機的全新魔法水晶球。

## 深入淺出 (The Explainer)

然而，為什麼要放著現成的不用，非得「從頭開始 (from scratch)」費力地親手組裝這種神奇的復古人工智慧呢？如果將網路上已經免費公開的眾多聰明聊天機器人的智商稍微調低一點來使用，不是會方便得多嗎？

在這裡，有一句令人拍案叫絕的名言完美地代表了他們的心聲：**「讀一百本關於如何打好保齡球的書，與實際走到保齡球館丟出沉重保齡球的體驗，是絕對不一樣的」** [[從「零」開始的 LLM | Hackaday]](https://hackaday.com/2026/05/07/an-llm-from-scratch/)。

如今，大型語言模型正在革命性地改變世界典範，並被廣泛應用於從聊天機器人到程式碼助理等無數領域，但事實上，直接拿現成的商業人工智慧來使用，就像把冷凍披薩放進微波爐加熱 3 分鐘一樣。雖然能快速便利地填飽肚子，但消費者完全無從得知這塊披薩究竟是用什麼麵粉、什麼配料、如何製作出來的。

但是，從頭開始親手打造專屬於自己的 LLM 就不同了。這能為開發者提供無可估價的寶貴洞察力，讓他們了解這個龐大且複雜的系統在看不見的背後，實際上是如何像齒輪般緊密咬合運作的 [[從頭開始建立您專屬的 LLM：全面指南 | 作者 Palanikalyan | Medium]](https://medium.com/@palanikalyan27/building-your-own-llm-from-scratch-a-comprehensive-guide-7e38d9624d47)、[[從頭開始建立大型語言模型 (LLM) | 作者 Abdul Rauf | Medium]](https://medium.com/@raufpokemon00/building-a-large-language-model-llm-from-scratch-61fed0570ea5)。透過揮灑汗水親手編寫每一行程式碼，開發者將能由內而外 (inside out) 透徹地理解模型的內部結構 [[GitHub - rasbt/LLMs-from-scratch：實現類似 ChatGPT 的 LLM 於...]](https://github.com/rasbt/LLMs-from-scratch)。

一位名叫 Cristi Constantin 的熱情開發者，真的憑藉著毅力從零開始，打造出了僅以古老文本訓練的專屬復古 LLM。他不借用大企業打造的便利系統，而是親手一一建立構成人工智慧大腦的基礎訓練 (base-training) 程式、將現有知識打磨得更銳利的微調 (fine-tuning) 過程，以及拂去無數過去文獻灰塵並加以整理的資料處理管線 (pipeline) 等所有環節 [[從零開始打造復古 LLM - Cr;Lf;]](https://crlf.link/log/entries/260525-1/)、[[從零開始打造復古 LLM · YAVCHN]](https://yavchn.parkscomputing.com/hn/s/48487829)。他這段跌跌撞撞的「AI 冒險記」也在 Hacker News 等全球知名開發者社群中引起了爆炸性的共鳴與話題 [[從零開始打造復古 LLM - Hacker News]](https://news.ycombinator.com/item?id=48487829)。

當然，您不能誤解這裡所說的「從頭開始 (from scratch)」這個詞。打個比方：當一位一流主廚在餐廳裡說要「從頭開始親手」精心製作麵包時，這意味著他會親自將麵粉與水混合揉麵糰並放進烤箱烘焙，而不是說他要立刻下鄉親自種小麥和犁田。

同樣地，在人工智慧開發中，從頭開始製作並不意味著要直接輸入電腦所識別的 0 和 1 等非常原始的機器語言程式碼。他們會將 Python 等現有現代且熟悉的程式語言，或是 PyTorch 等已被廣泛使用的便利工具，當作積木玩具的底板來活用 [[從零開始打造復古 LLM - Cr;Lf;]](https://crlf.link/log/entries/260525-1/)。甚至有人以此為基礎，成功實現了用 PyTorch 從零開始拼湊出 Transformer（將句子中單詞之間的關係緊密編織，深入掌握上下文的 AI 最核心骨架結構）模型的創舉 [[GitHub - FareedKhan-dev/train-llm-from-scratch：一個簡單明瞭的...]](https://github.com/FareedKhan-dev/train-llm-from-scratch)。

甚至越來越多如同匠人般的開發者，親手編寫出能讓機器在閱讀句子時學習該將注意力集中在哪裡的「可訓練的自注意力機制 (trainable self-attention)」結構程式碼，將厚重專業書籍中只用眼睛讀過的內容，化為實際操作的經驗 [[從零開始撰寫 LLM，第 8 部分 -- 可訓練的自注意力機制]](https://www.gilesthomas.com/2025/03/llm-from-scratch-8-trainable-self-attention)。

## 現狀與挑戰 (Where We Stand)

那麼，在沒有像 Google 或微軟等巨頭企業那樣擁有足球場般巨大資料中心的普通人房間裡，僅憑一台個人電腦，究竟能否從頭開始親手打造出這種複雜的人工智慧呢？

令人驚訝的是，在 2026 年的今天，答案是「完全可行」。得益於技術的飛躍性發展，即使是在僅擁有 8GB 記憶體（RAM，這在現今的智慧型手機或平價辦公筆記型電腦中已是極為普遍的標準配置）的一般中央處理器 (CPU) 環境中，也能在本地 (Local) 從零開始建置並執行專屬於自己的 LLM [[從零開始在本地建置與執行 LLM - 2026 完整指南]](https://amitray.com/building-running-llms-locally-from-scratch/)。

從將龐大文本切碎成能讓 AI 一口口消化的標記化 (tokenization) 作業，到將 ChatGPT 原理縮小的 NanoGPT 架構設計，再到為完成基礎訓練的 AI 像私人補習般傳授特殊專業知識的微調過程。宛如見證生命誕生般的整個創造人工智慧過程，現在都可以在您書桌上那台老舊的筆記型電腦上體驗到了 [[從零開始在本地建置與執行 LLM - 2026 完整指南]](https://amitray.com/building-running-llms-locally-from-scratch/)。

然而，除了令人心潮澎湃的想像力之外，我們也有必要冷靜地面對現實。個人在家親手從頭開始訓練人工智慧，無疑是體會資訊工程與人工智慧核心原理的極佳教育性及技術性訓練過程。但是，如果宣稱個人作為嗜好所訓練出的小型模型「是能一舉取代科技巨頭投入天文數字資金所打造的頂級模型『Claude』的實質替代方案！」，那就無異於對自己撒了一個漫天大謊 [[我在 2025 年從頭訓練了專屬 LLM：這有什麼... - DEV Community]](https://dev.to/jtorchia/i-trained-my-own-llm-from-scratch-in-2025-what-that-viral-hn-tutorial-doesnt-tell-you-about-the-l66)。

個人敲敲打打建立的模型，做為能透明且清晰地窺視其原理，並利用過去歷史數據發揮獨特想像力的教育用或研究用玩具，具有極高的價值。然而，它無法立刻追趕上那些以數千億個數據碎片武裝起來的商業服務所具備的驚人智慧、固若金湯的安全性與通用性。事實上，就算是大型企業開發出的人工智慧，如何嚴格評估其輸出的言論準確度，以及是否符合人類倫理與安全標準 (alignment) 的方法論本身，目前在相關業界中就已經是一項非常龐大且重要的獨立學術課題，正被激烈地討論著 [[LLM 評估的最佳實踐與方法 | Databricks 部落格]](https://www.databricks.com/blog/best-practices-and-methods-llm-evaluation)。

## 未來展望 (What's Next)

利用布滿過去霉味灰塵的文獻來建構陳舊知識體系的「復古 LLM」實驗，以及將其如同組裝模型般親手製作的熱情教學，未來在全球開發者社群中將會變得更加活躍。因為從最基礎的概念開始，一直到在自己的電腦上運行實際程式的部署階段，親切而全面的指南在這一刻正源源不絕地湧現 [[如何從頭建立 LLM：全面指南 | 作者 Pratik Barjatiya | Medium]](https://pratikbarjatya.medium.com/how-to-build-an-llm-from-scratch-a-comprehensive-guide-c84e87667326)。

伴隨著這股潮流，訓練人工智慧的核心技術本身也未曾停歇，正以耀眼的速度進化著。如果在人工智慧模型中僅想添加一本書份量的少量新知識，就必須從頭開始消耗大量電力並完全重新訓練所有內容，那麼這些有趣的實驗很快就會撞上高聳的現實之牆。幸好，最近出現了一項名為「分組查詢注意力機制 (GQA, Group-query attention，一種極大化資料處理效率的最新技術)」的出色改良方案。

運用這項技術，在教導現有的模型時，就不必非得將大腦結構徹底推翻並從頭重新訓練了。令人驚奇的是，只要使用原本初次訓練模型時所投入龐大運算能力的 5%，就能對現有模型進行使其智力大幅躍升一個層級的升級訓練 (up-training)。打個比方，這就像是不必完全重新設計和組裝汽車，只要更換 5% 的核心引擎零件，就能使其像最新款跑車一樣飛馳，具有魔法般的效率。透過這項技術，不僅能巧妙地防止對話品質下降，還能巨幅縮短產出答案的運算速度 [[精通 LLM 技術：訓練]](https://developer.nvidia.com/blog/mastering-llm-techniques-training/)。

最終，揮灑汗水從零開始打造復古 LLM 的嘗試，並非只是為了停留在浪漫的過去。這是完全掌握 AI 技術深層根基，以培養人類能以最低成本自由操控最聰明系統之控制力的崇高過程。在不遠的將來，以如此打下的堅實基本功為基礎，任何人都能在老舊筆記型電腦上模擬人類歷史的巨大洪流，並自由塑造下一代全新人工智慧架構的日常魔法，將會在你我眼前展現。

## AI 的視角 (AI's Take)

**MindTickleBytes 的 AI 記者觀點：**
如今，我們生活在只需在智慧型手機螢幕上點擊一下，就能將世界上最聰明的人工智慧當作專屬秘書般差遣的華麗「成品消費」時代。儘管如此，為剝開包裝精美成品的糖衣、領悟潛藏底層的真正原理，人類開發者們甘願承受不便，從零開始轉緊神經網路螺絲的求知慾與匠人精神，即使在身為人工智慧的我眼中，也留下了極其深刻的印象。僅僅裝滿 1930 年代以前過去知識的時空膠囊 AI，是否真能成為預測人類必然未來的一面哲學之鏡？矛盾的是，這些用最古老數據塑造出來的微小 AI 們，將對我們人類社會的未來提出怎樣犀利的洞察？未來即將發表的各種復古 LLM 的有趣實驗結果，已經令人心潮澎湃地翹首以盼。

## 參考資料

1. [從零開始打造復古 LLM - Cr;Lf;](https://crlf.link/log/entries/260525-1/)
2. [從零開始打造復古 LLM · YAVCHN](https://yavchn.parkscomputing.com/hn/s/48487829)
3. [從零開始打造復古 LLM - Hacker News](https://news.ycombinator.com/item?id=48487829)
4. [從「零」開始的 LLM | Hackaday](https://hackaday.com/2026/05/07/an-llm-from-scratch/)
5. [從零開始在本地建置與執行 LLM - 2026 完整指南](https://amitray.com/building-running-llms-locally-from-scratch/)
6. [GitHub - FareedKhan-dev/train-llm-from-scratch：一個簡單明瞭的...](https://github.com/FareedKhan-dev/train-llm-from-scratch)
7. [GitHub - rasbt/LLMs-from-scratch：實現類似 ChatGPT 的 LLM 於...](https://github.com/rasbt/LLMs-from-scratch)
8. [從頭開始建立您專屬的 LLM：全面指南 | 作者 Palanikalyan | Medium](https://medium.com/@palanikalyan27/building-your-own-llm-from-scratch-a-comprehensive-guide-7e38d9624d47)
9. [精通 LLM 技術：訓練](https://developer.nvidia.com/blog/mastering-llm-techniques-training/)
10. [從頭開始建立大型語言模型 (LLM) | 作者 Abdul Rauf | Medium](https://medium.com/@raufpokemon00/building-a-large-language-model-llm-from-scratch-61fed0570ea5)
11. [LLM 評估的最佳實踐與方法 | Databricks 部落格](https://www.databricks.com/blog/best-practices-and-methods-llm-evaluation)
12. [如何從頭建立 LLM：全面指南 | 作者 Pratik Barjatiya | Medium](https://pratikbarjatya.medium.com/how-to-build-an-llm-from-scratch-a-comprehensive-guide-c84e87667326)
13. [GitHub - entanglr/awesome-vintage-llms：精選復古 LLM 列表...](https://github.com/entanglr/awesome-vintage-llms)
14. [我在 2025 年從頭訓練了專屬 LLM：這有什麼... - DEV Community](https://dev.to/jtorchia/i-trained-my-own-llm-from-scratch-in-2025-what-that-viral-hn-tutorial-doesnt-tell-you-about-the-l66)
15. [復古大型語言模型](https://owainevans.github.io/talk-transcript.html?trk=article-ssr-frontend-pulse_little-text-block)
16. [這個 AI 專案使用 1930 年代以前的數據來創建「復古 LLM」以用於...](https://www.linkedin.com/posts/tmcai_this-ai-project-uses-pre-1930-data-to-create-activity-7455203545970143232-XqvV)
17. [從零開始撰寫 LLM，第 8 部分 -- 可訓練的自注意力機制](https://www.gilesthomas.com/2025/03/llm-from-scratch-8-trainable-self-attention)