---
layout: post
title: "保存我的問題30天？Anthropic新AI政策引發爭議的原因"
description: "Anthropic推出最高性能AI模型Claude Fable 5與Mythos 5，並強制實施30天數據保存政策。本文為您深入淺出地整理企業強烈反彈以及微軟限制內部使用的原因。"
summary: "隨著強大的新AI模型以安全監控為由，強制保存用戶的問答內容達30天，出於對企業機密外洩的擔憂，主要企業紛紛限制其使用，引發了日益延燒的隱私爭議。"
tags: [Anthropic, Claude, 隱私, AI安全, 企業, 網路安全]
image: 2026-06-11-Anthropic-requires-30-day-data-retention-for-Fable-and-Mythos.jpg
image_alt: "在開啟著安全監控鏡頭的房間內，一台聰明的機器人正在審閱重要文件的模樣"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "為了享受更聰明的AI所帶來的優勢，我們必須在隱私上退讓到什麼程度？強大的技術管控與數據主權之間激烈的拉鋸戰才剛剛正式展開。"
quiz:
  - question: "Anthropic在Claude Fable 5與Mythos 5中全新導入的數據保存期限是多久？"
    choices: ["不保存（立即刪除）", "30天", "1年"]
    answer: 1
    explanation: "Anthropic以系統安全監控為名義，實施了強制保存所有提示詞與生成結果至少30天的政策。"
  - question: "企業客戶先前與Anthropic簽署的「零保留（數據立即刪除）」合約，在這項新政策下將會如何處理？"
    choices: ["現有合約優先並繼續維持", "全新的30天保存政策將使現有合約失效並強制適用", "用戶可自由選擇是否保存"]
    answer: 1
    explanation: "全新的30天強制數據保存政策將強制無效化（override）企業先前簽署的所有零保留合約，並被視為最優先適用。"
  - question: "微軟限制其員工使用Claude Fable 5的主要原因為何？"
    choices: ["為了降低競爭對手模型的市佔率", "由於新數據保存政策引發對公司機密資訊外洩及侵犯隱私的擔憂", "因為AI模型的寫程式能力顯著下降"]
    answer: 1
    explanation: "微軟判定Anthropic強制的30天數據保存政策將對企業數據隱私帶來嚴重風險，因此全面限制了內部使用。"
lang: zh-tw
ref: 2026-06-11-Anthropic-requires-30-day-data-retention-for-Fable-and-Mythos
---

請想像一下。您正在公司撰寫一份攸關公司命運的重要新產品發布計畫，或是核心技術架構的藍圖。由於獨自處理這項龐大的工作實在太過吃力，您決定向一位極其聰明且辦事效率極高的AI助理尋求協助。

「我把我們的極機密配方和核心行銷策略資料交給你，請幫我完美地整理成明早高層會議的簡報資料。」

幸好，這位優秀的助理早已簽署了一份嚴格的保密協定：「我在工作結束後，會立刻將剛剛看到的文件內容從腦海中徹底抹除。」於是您放心地將攸關公司未來的機密文件交到了助理手中。

然而有一天，這位助理聲稱大幅提升了自己的工作能力，卻突然改變了態度：「未來因為我變得太聰明了，我擔心我處理的資訊萬一牽涉到犯罪行為。因此，為了確認安全，我必須將您提供的所有文件強制保存在我的個人保險箱中『30天』並進行監視。以前簽署的立即刪除協定從今天起全面失效。」

換作是您，還能繼續安心地將公司的最高機密交給這位助理嗎？或許大多數人都會急忙搶回文件，立刻離開房間。

這個令人錯愕的劇本，正是目前全球IT業界正在真實上演的情況。2026年6月9日，知名人工智慧企業Anthropic無預警發布了其史上最高性能的AI模型「Claude Fable 5」，以及更具專業性且有使用限制的版本「Mythos 5」[[Anthropic針對Claude Fable 5全新的30天數據保存政策是否...](https://www.linkedin.com/pulse/does-anthropics-new-30-day-data-retention-claude-fable-jonathan-milne-qhrfe)]。

但事實上，外界熱切關注的焦點，並非這些模型所展現的驚人智慧或壓倒性的寫程式能力。人們的目光全都嚴厲地聚焦在他們全新祭出的「數據強制保存30天」這張隱藏的帳單上。

線上社群與網路空間隨即爆發強烈的憤怒[[Claude Fable 5發布後，網路上對Anthropic感到憤怒 - Decrypt](https://decrypt.co/370688/internet-furious-anthropic-claude-mythos-fable-5)]，包含微軟在內的主要科技巨頭也立即在安全部門拉響了警報。具備世界最高水準能力的AI華麗登場，卻沒有獲得掌聲與歡呼，反而引來排山倒海的擔憂與警戒。究竟在舞台背後發生了什麼事？

## 這為什麼很重要？ (Why It Matters)

隨著AI技術的飛躍性發展，現代企業與個人將無可比擬的敏感資訊輸入至AI系統中，並高度依賴其產出的結果。

軟體工程師在編寫企業核心原始碼時，藉助AI的幫助來縮短工作時間；醫生們試圖透過分析醫院複雜的病患數據來做出更準確的診斷；財務專家則讓AI事先審閱尚未對外公開的企業業績報表。當每天都要處理如此致命且敏感的資訊時，企業最優先考量的絕對價值只有一個，那就是隱私（Privacy，個人資訊與機密保護）與嚴密的數據安全。因為只要發生一次外洩，就可能直接導致公司破產。

為了消除企業這種巨大的不安感，在此之前，大多數的企業客戶都會與AI服務供應商簽署嚴格的「零保留（Zero-retention，即數據在伺服器上連1秒都不會保存，處理完畢後立即刪除的政策）」合約。多虧了這份合約，企業才能安心地將AI積極應用於實務中。也就是說，無論用戶向AI詢問什麼機密、獲得多麼出色的回答，只要關閉該對話視窗，相關紀錄就會立刻從伺服器上被永久銷毀，這是一個堅定且明確的承諾。對企業而言，這是將AI導入內部網路的唯一底線。

然而，Anthropic在向世界公開這批新型Claude模型時，卻投下了震撼彈。他們單方面通知了一項新政策：強制將所有用戶的提示詞（Prompt，向AI下達的指令或問題）及AI生成的結果流量，保留在其伺服器中達「30天」[[Fable 5與Mythos 5如何改變AI安全、數據保存...](https://www.forrester.com/blogs/how-fable-5-and-mythos-5-change-ai-security-data-retention-and-vendor-risk/)]。

其中最讓業界感到震驚的事實是，這項全新的30天強制保存條款，竟然將無效化（override）眾多企業客戶花費數百萬美元所簽署的鐵壁般零保留合約，並被視為最優先適用[[Anthropic的Claude Fable是大眾可存取的Mythos版本...](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/)]。這意味著過去的承諾已不再有效。

更嚴重的是這項可怕政策的適用範圍。它並不僅限於在Anthropic官方網站（第一方介面）上使用模型時。即使是透過Amazon Web Services (AWS)的雲端平台Bedrock，或是GitHub Copilot等第三方（Third-party）合作夥伴平台間接運行這款AI時，這項30天保存義務同樣毫無例外地無條件適用[[AWS上的Anthropic Claude Fable 5：內建防護機制的Mythos級功能現已可用 | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)][[Anthropic將Fable 5的風險提示詞路由至Opus 4.8](https://www.implicator.ai/anthropic-routes-high-risk-fable-5-queries-to-opus-4-8-in-public-rollout/)][[Claude Fable 5數據保存合規性 | Lushbinary](https://lushbinary.com/blog/claude-fable-5-enterprise-data-retention-compliance-guide/)][[Claude Fable 5發布後，網路上對Anthropic感到憤怒 - Decrypt](https://decrypt.co/370688/internet-furious-anthropic-claude-mythos-fable-5)]。

簡單打個比方，這就像是您租了一間頂級飯店房間（AWS）幾天，打算舉行一場不受外界干擾的完美秘密會議，但製作房間內舒適床鋪的傢俱公司（Anthropic）卻堅持說：「若要使用我們公司的床，房間內就必須安裝我們的安全監控鏡頭，而且30天的錄影紀錄必須由我們帶走」。這等同於理直氣壯地向全世界所有企業宣告：「想要借用我們頂級的AI智慧，就乖乖把你們如同心臟般重要的機密數據，交到我們手上長達一個月吧」。

## 淺顯易懂的解釋 (The Explainer)

究竟為什麼Anthropic明明預見到企業這個最重要客戶群體的強烈反彈與流失，卻仍要強行推動這項無理的要求呢？他們用來當作擋箭牌的名義只有一個，那就是保護人類免受致命危險威脅的「安全（Safety）」。

我們可以用日常生活中使用的工具危險性來比喻。當我們把在社區遊樂場堆沙堡用的輕巧塑膠鏟借給鄰居時，不需要要求任何身分查驗或文件。因為就算用錯了，充其量只是噴起一點沙子而已。然而，當要出租能夠把整座巨大岩山炸飛的高性能炸藥時，情況就完全不同了。必須進行嚴格的身分調查，安裝追蹤裝置以確認炸藥具體用在哪裡，並且必須用監視器仔細監控整個過程，以防止事故發生。

同理，隨著AI模型的能力變得過去無法比擬的強大，當它被用於惡意目的時，對全人類可能造成的損害規模也呈指數級增長。

這次全新推出的Claude Fable 5在龐大知識作業、複雜視覺資訊處理、甚至自行移動滑鼠操作電腦的能力，以及進階寫程式領域，都具備了現有最高水準（State-of-the-art）的能力[[Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable)]。而在這之上更進一步的Mythos 5模型，則是登峰造極於建構高階網路安全系統防禦網、深入的生物學研究以及專業醫療領域的終極模型[[Claude Mythos \ Anthropic](https://www.anthropic.com/claude/mythos)]。

如果擁有如此驚人專家知識與能力的AI落入駭客或恐怖分子手中，在眨眼間編寫出癱瘓國家電網的惡意程式碼，或是親切地指導如何秘密製造致命生物武器，那將會是一場無法挽回的可怕災難。

因此，為了即時監控AI在與用戶對話的過程中，是否有危險行為或違反內部規定的情況，Anthropic決定全面啟動名為「安全分類器（Safety Classifiers，即時判別危險徵兆的人工智慧監控程式）」這種主動式的24小時監控系統[[所有準備使用Fable 5的組織請注意：他們會保留您的...](https://cybernews.com/ai-news/claude-fable-five-data-retention-collection/)][[微軟因數據保存疑慮限制員工使用Claude Fable | The Verge](https://www.theverge.com/report/947575/microsoft-claude-fable-5-restricted-internally)]。

然而，這套監控系統若要完美掌握對話的上下文關聯，並準確評估實際危險性，就必須深入分析用戶究竟帶著什麼意圖提問，以及AI給出了什麼回答的來龍去脈。為此，絕對的「時間」與保存的「數據」是不可或缺的。

最終，Anthropic得出的結論是，為了正確無誤地執行這項複雜的安全監控作業，至少30天的保存期限絕對有其必要。他們果斷拔掉了企業如此信任且渴望的零保留這台可靠「文件立即碎紙機」的電源線，並在其位置上安裝了一台強制錄影長達30天的強大「安全監控攝影機」。

當然，Anthropic為了安撫憤怒企業客戶的強烈反彈與深切擔憂，也急忙補充了一項重要承諾。他們明文規定，被強制保存的商業客戶敏感流量數據，僅會極其受限地用於安全監控這個本來的防禦目的，絕對不會胡亂收集這些數據來訓練（學習）新一代的Claude AI模型[[Anthropic推出具備...的Claude Fable 5 — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)]。然而，儘管有如此積極的澄清與承諾，仍不足以完全消除企業已然瓦解的信任與深沉的不安感。

## 現況 (Where We Stand)

這項破格且略顯單方面的政策一經發布，IT市場與主要企業客戶的反應冷淡且堅決。動作最快且最為敏感的，正是IT業界的科技巨頭兼嚴密安全的象徵——微軟（Microsoft）。

微軟提出沉重的擔憂，認為Anthropic這項新數據保存政策與其嚴格的數據隱私標準正面衝突，並採取了強硬手段，立即限制了大量員工在內部工作網路上存取並使用Claude Fable 5模型[[微軟因數據保存疑慮限制員工存取Anthropic的Claude Fable 5](https://cryptobriefing.com/microsoft-restricts-claude-fable-5-data-retention/)][[微軟因數據保存疑慮限制員工使用Claude Fable | The Verge](https://www.theverge.com/report/947575/microsoft-claude-fable-5-restricted-internally)]。就連世界上對安全最嚴格、對AI趨勢最敏感的全球頂尖科技企業，也冷靜地判定：他們絕對無法承受作為公司骨幹的內部機密，被綁在無法控制的外部伺服器上長達30天的驚險危機。

更讓用戶輾轉難眠且感到不安的是，數據被綁定的期間，可能不一定只侷限在30天這個短暫（？）的時間內結束。根據相關報導與Anthropic政策的細節指出，如果安全分類器系統懷疑特定用戶的提示詞或AI生成結果具有嚴重的潛在風險因素（例如：精密的駭客攻擊企圖、危險化學物質相關討論等）而亮起紅燈，相關數據為了進行精確分析與深入調查，將有可能被保存在伺服器上長達2年[[微軟因數據保存疑慮限制員工使用Claude Fable | The Verge](https://www.theverge.com/report/947575/microsoft-claude-fable-5-restricted-internally)]。

究竟是基於何種模糊又隱密標準，讓我珍貴的業務數據必須被關在別家公司的保險箱裡長達2年之久？對用戶來說，由於沒有適當的管道能確保透明度或追究原因，只能懸著一顆心。

正因如此，目前全球無數的跨國大型企業與創新的新創公司，都陷入了痛苦的進退兩難困境。是該聘用現有最聰明、能將員工工作效率提升數十倍的出色AI助理（Fable 5、Mythos 5），以在激烈的市場競爭中拔得頭籌？還是為了堅守如同公司生命線般絕對的數據主權與安全性，寧可犧牲一點工作效能，繼續堅持使用保障安全「零保留」的舊型AI，或是其他競爭對手較不聰明的替代模型？此時此刻，在無數企業的安全主管與高層會議室裡，連日來正展開著激烈的馬拉松式討論。

最重要的是，網路社群中無數開發者表達最深切擔憂的原因，在於這項政策可怕的擴展性。根據Anthropic堅決發布的聲明，這項強制保存政策絕不僅是適用於本月推出的Fable 5或Mythos 5模型後就結束的一次性措施。它預計將永久且毫無例外地，適用於未來發布的、具備相似水準能力或擁有更高超智慧的所有「Mythos級（Mythos-class）」巨型模型[[Anthropic透過其有史以來最強大的普及化模型Claude Fable 5將Mythos帶給大眾 | VentureBeat](https://venturebeat.com/technology/anthropic-brings-mythos-to-the-masses-with-claude-fable-5-its-most-powerful-generally-available-model-ever/)][[Claude Fable 5數據保存合規性 | Lushbinary](https://lushbinary.com/blog/claude-fable-5-enterprise-data-retention-compliance-guide/)][[Claude Fable 5發布後，網路上對Anthropic感到憤怒 - Decrypt](https://decrypt.co/370688/internet-furious-anthropic-claude-mythos-fable-5)]。

在最先討論最新IT趨勢的HackerNews等開發者社群中，這則消息也立刻成為燙手山芋，引發了激烈的正反辯論[[Anthropic為Fable要求30天數據保存... | HackerNews](https://news.ycombinator.com/item?id=48464258)]。也就是說，這隱含著一種濃厚的風險：它可能會成為人類未來為了享受更卓越、更夢幻的人工智慧所帶來的好處，而必須支付且無法逃避的「新型過路費」，並逐漸成為整個AI業界固定的新標準（Standard）。

## 未來將會如何？ (What's Next)

我們正處在驚人人工智慧技術歷史中，一個將永遠決定人類隱私發展方向、至關重要且驚險的轉折點上。

隨著AI變得比人類更聰明，並深入滲透至連人類都無法輕易完成的極度複雜與精密領域，Anthropic「安全至上」的主張——為了防患未然，防止其引發毀滅性危險，管控與監視的強度也必須成正比地更加嚴密——在哲學上的確有其合理的面向。為了避免令人眼花撩亂的技術發展可怕加速度，在某個瞬間徹底脫離人類微弱的控制力，預先建立起堅固且巨大的「安全網」，或許是為了全人類的生存與未來，必須有人背負著被譴責的十字架去完成，過程痛苦卻不可或缺的任務。

然而，在強制建立與維持這張沉重且巨大安全網的過程中，個人與企業長久以來艱辛奮戰才守護住的「隱私」與「數據主權」這兩項絕不可退讓的根本基本權利，正受到嚴重動搖並發生尖銳衝突。微軟迅速全面限制內部存取的措施，可能只是這場巨大矛盾冰山的一角。

未來，只要發生一次數據外洩事故便攸關公司存亡的嚴謹金融界、處理極度敏感且私密病患生命資訊的保守醫療界、以及以嚴守秘密為存在理由的法律領域，這些領域的無數企業，極有可能將從原點全面重新評估是否在業務中導入與使用最新的Claude模型。

## AI的觀點 (AI's Take)

為了享受更聰明的AI所帶來的優勢，我們必須在隱私上退讓到什麼程度？強大的技術管控與數據主權之間激烈的拉鋸戰才剛剛正式展開。

隨著人工智慧的智力爆發性成長，人類現在已開始不再將AI僅僅視為便利的簡單工具，而是潛在的風險因素。Anthropic這次固執的決定，正是源自於AI能力總有一天可能徹底脫離人類掌控的根本恐懼。

然而，從企業與個人的立場來看，自己傾注心血製作的最高機密資訊，必須留在無法控制的某人伺服器上達30天，甚至可能基於模糊標準而停留長達2年之久，這項事實無疑令人感到極度不安與不滿。

渴望自由奔放地運用創新最高效能AI技術，同時也希望自己珍貴的資訊能完美隔絕外界視線並受到保護——這是人類的根本慾望。而另一端，則是為確保全人類安全，必須徹底審視並監控所有潛在風險的AI安全網。這兩者之間劍拔弩張且令人窒息的緊張感，未來將進一步升溫。最終，能夠在技術上最優雅地解決這巨大矛盾的企業，或許才能真正稱霸未來的AI市場。

在接下來的一段時間裡，我們必須饒富興味地觀察：Anthropic這項堅定且強硬的隱私限制政策，究竟能否戰勝重視效率的冷酷市場邏輯，並穩固地成為整個業界的新標準。此外，無數競爭的AI企業將如何敏銳地切入這場衝突的縫隙，端出何種充滿創意的誘餌與具吸引力的替代政策來拉攏惶恐不安的企業客戶，這也是非常重要的觀戰重點。畢竟，技術真正的創新，總是在這般出乎意料的激烈衝突與痛苦陣痛中，找尋出明朗的解答。

## 參考資料

1. [Fable 5與Mythos 5如何改變AI安全、數據保存...](https://www.forrester.com/blogs/how-fable-5-and-mythos-5-change-ai-security-data-retention-and-vendor-risk/)
2. [Anthropic針對Claude Fable 5全新的30天數據保存政策是否...](https://www.linkedin.com/pulse/does-anthropics-new-30-day-data-retention-claude-fable-jonathan-milne-qhrfe)
3. [Claude Fable 5發布後，網路上對Anthropic感到憤怒 - Decrypt](https://decrypt.co/370688/internet-furious-anthropic-claude-mythos-fable-5)
4. [Anthropic的Claude Fable是大眾可存取的Mythos版本...](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/)
5. [AWS上的Anthropic Claude Fable 5：內建防護機制的Mythos級功能現已可用 | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)
6. [Anthropic將Fable 5的風險提示詞路由至Opus 4.8](https://www.implicator.ai/anthropic-routes-high-risk-fable-5-queries-to-opus-4-8-in-public-rollout/)
7. [Claude Fable 5數據保存合規性 | Lushbinary](https://lushbinary.com/blog/claude-fable-5-enterprise-data-retention-compliance-guide/)
8. [Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable)
9. [Claude Mythos \ Anthropic](https://www.anthropic.com/claude/mythos)
10. [所有準備使用Fable 5的組織請注意：他們會保留您的...](https://cybernews.com/ai-news/claude-fable-five-data-retention-collection/)
11. [微軟因數據保存疑慮限制員工使用Claude Fable | The Verge](https://www.theverge.com/report/947575/microsoft-claude-fable-5-restricted-internally)
12. [Anthropic推出具備...的Claude Fable 5 — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)
13. [微軟因數據保存疑慮限制員工存取Anthropic的Claude Fable 5](https://cryptobriefing.com/microsoft-restricts-claude-fable-5-data-retention/)
14. [Anthropic透過其有史以來最強大的普及化模型Claude Fable 5將Mythos帶給大眾 | VentureBeat](https://venturebeat.com/technology/anthropic-brings-mythos-to-the-masses-with-claude-fable-5-its-most-powerful-generally-available-model-ever)
15. [Anthropic為Fable要求30天數據保存... | HackerNews](https://news.ycombinator.com/item?id=48464258)