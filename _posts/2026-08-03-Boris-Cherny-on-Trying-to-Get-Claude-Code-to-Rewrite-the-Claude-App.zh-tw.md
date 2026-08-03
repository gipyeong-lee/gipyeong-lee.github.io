---
layout: post
title: "AI會自我重新設計？克勞德程式碼的開發者暢談「真正」的AI應用方法"
description: "探索Anthropic的克勞德程式碼開發者Boris Cherny分享如何利用AI更有效率地編碼，並將成果品質提升2至3倍的秘訣。"
summary: "克勞德程式碼開發者Boris Cherny強調，不僅是將編碼任務交給AI，而是當我們能為AI創建一個能自行驗證工作成果的「回饋迴路」時，開發品質才會飛躍性地提升。"
tags: [AI, 克勞德程式碼, 開發, 生產力, Anthropic]
image: 2026-08-03-Boris-Cherny-on-Trying-to-Get-Claude-Code-to-Rewrite-the-Claude-App.jpg
image_alt: "開發者在終端機中利用克勞德程式碼進行作業的畫面。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是一個不再僅僅是使用工具，而是如何讓工具思考變得重要的時代。與AI的協作，現在已從「命令」轉變為「建立驗證系統」的範疇。"
quiz:
  - question: "Boris Cherny強調，提升AI編碼工具品質最關鍵的要素是什麼？"
    choices: ["使用更好的AI模型", "提供驗證工作成果的回饋迴路", "進行更多的提示工程"]
    answer: 1
    explanation: "他解釋說，讓AI自行驗證其工作，可使成果品質提升2至3倍。"
  - question: "克勞德程式碼（Claude Code）主要在哪裡執行？"
    choices: ["網頁瀏覽器", "終端機", "智慧型手機應用程式專用"]
    answer: 1
    explanation: "克勞德程式碼是一種代理程式型編碼工具，常駐於終端機，幫助將想法快速轉化為程式碼。"
  - question: "開發者為了有效利用克勞德程式碼，建議進行的其中一項工作是什麼？"
    choices: ["撰寫CLAUDE.md文件並在開發前制定計畫", "無條件使用AI編寫的程式碼", "手動重新編寫所有程式碼"]
    answer: 0
    explanation: "有效使用克勞德程式碼需要12項關鍵習慣，其中最重要的包括在開發前制定計畫並撰寫CLAUDE.md文件。"
lang: zh-tw
ref: 2026-08-03-Boris-Cherny-on-Trying-to-Get-Claude-Code-to-Rewrite-the-Claude-App
---

想像一下。您正打算開設一家別緻的社區咖啡館。假設從店面標誌到充滿文藝氣息的菜單，以及讓顧客可以在線上方便點餐的網路首頁，全部都必須由您獨自一人完成。如果是以前，您可能需要聘請專業設計師，並為學習複雜的電腦程式語言而頭痛不已，但現在，我們已經進入了一個神奇的時代，您只需舒服地坐在電腦前，像與親密朋友閒聊一樣講述您的想法，短短幾分鐘內，一個功能齊全的網站就能魔法般地呈現出來。

最近，人工智慧（AI）業界和全球開發者社群都經歷了一場令人震驚且激動人心的實驗。這項實驗由全球AI創新企業Anthropic推出的代理程式型編碼工具「克勞德程式碼（Claude Code）」的開發總監Boris Cherny親自執行，這是一項大膽而創新的挑戰 [Source 4, Source 13]。他利用克勞德程式碼，嘗試將原本使用Electron（一種流行的軟體框架，協助開發者利用網頁技術開發桌面應用程式，但因其較為笨重和緩慢）開發、運作稍嫌遲鈍的克勞德桌面應用程式，完全從頭到尾地以蘋果最新的原生程式語言Swift（一種用於在蘋果裝置上流暢且最佳化地運行應用程式的程式語言）重新編寫，這是一項極具戲劇性的實驗 [Source 4, Source 13]。

這則戲劇性的消息瞬間在開發者社群中引起熱烈討論 [Source 13]。許多人不禁驚嘆：「難道人工智慧完美取代人類開發者的時代終於來臨了嗎？」並流露出擔憂。然而，親自指揮這項驚人挑戰的Boris Cherny告訴我們的真實故事，並非「AI像魔法般地自行完成了所有事情」這樣虛幻的傳奇。相反，我們現在最應該關注的核心是，**「如何引導不完美的AI進行更聰明的協作，並將最終成果的完成度推向極致」**，這是一個極其現實且寶貴的實戰秘訣 [Source 4]。

## 這為什麼重要？

我們每天愛不釋手的手機應用程式，或是公司處理業務時使用的便利網路服務，都是無數開發者在幕後一字一句精心輸入程式碼的汗水結晶。然而，在這些開發過程中，比起發揮創意靈感的工作，枯燥、單純且機械性地編寫程式碼的重複作業，卻佔了出乎意料的巨大比重。如果全球聰明的程式設計師能夠完全從這種機械性的單純編碼工作中解放出來，那會怎麼樣呢？他們就能將剩餘的時間和精力，完全投入到更具創意、更富人本價值的高階系統規劃和架構（系統整體結構設計）中 [Source 1]。克勞德程式碼所描繪的未來，正是這場「生產力革命」的起點。

克勞德程式碼是一種創新的代理程式型編碼工具，主要在開發者常用的黑色工作空間——終端機（Terminal，一種透過鍵盤直接輸入文字命令來控制電腦系統的程式）中執行 [Source 11]。這裡的「代理程式（Agent）」不僅僅是簡單回應使用者問題的傳統人工智慧，它更進一步，能夠自行制定計畫、直接修改系統檔案，並仔細檢查執行結果，是一種「自主導向型人工智慧助理」。因此，即使是從未學習過程式設計的普通人，現在也有機會在這位可靠助理的協助下，輕鬆製作出自己專屬的客製化軟體。特別是克勞德程式碼不只受限於電腦螢幕前，也能輕巧地移植到行動環境（iOS和Android），確保了強大的行動性，讓您隨時隨地都能輕鬆將想法具體化為程式碼 [Source 3, Source 9]。事實上，就連開發負責人Boris Cherny本人也經常在搭乘大眾交通工具的空檔，拿出智慧型手機（iOS）親自編寫和修改大量的實際程式碼，您可以想像這種便利性是多麼驚人嗎？ [Source 3]

## 輕鬆理解：與AI協作的聰明方法

Boris Cherny正在引領一個激勵無數人的未來，但他所說的最令人驚訝的事實卻是另一回事。那就是在使用克勞德程式碼時，**「我們如何設定任務和制定多麼周密的計畫」**，才是決定人工智慧工作效率的真正秘密，而不是「使用了哪種昂貴且優秀的AI模型」 [Source 12]。

讓我們用烹飪來比喻。即使請來了米其林星級的世界頂級廚師，如果完全不提供食譜或指導，只是隨意丟給他一些食材，並說「做一道好吃的菜」，也很難做出美味的料理。相反，如果明確規劃好料理的步驟，並在烹飪過程中，親自用湯匙品嚐味道，細心調整鹽和糖的用量，提供細緻的回饋，即使是烹飪新手也能完成一道絕妙的盛宴。與AI的協作也完全是如此。

簡而言之，與人工智慧協作最核心的原則，就是精心地設計**「回饋迴路（Feedback Loop，即時檢視成果並立即修正的循環過程）」** [Source 15]。Boris Cherny表示，不能讓克勞德程式碼編寫一次程式碼就結束，人類必須精心設定最佳的舞台，讓AI能夠自行測試和驗證自己編寫的程式碼是否無誤地運行。這樣聰明地將回饋過程連結起來，AI最終成果的完成度就能驚人地提升2到3倍以上 [Source 15]。

比喻來說，這就像一位聰明的畫家，在畫布上揮灑一筆後，並非呆立不動，而是後退一兩步，仔細審視整體構圖和色彩，然後再輕觸不足之處，不斷重複這個提升完成度的過程。例如，如果AI美化了行動螢幕的介面佈局（設計排版），我們就應該在網路瀏覽器上虛擬地按壓和操作按鈕，然後引導AI不知疲倦地反覆修改和完善，直到使用者使用起來完全方便流暢的畫面完成為止 [Source 3]。

為了實踐這種流暢完美的AI協作，Boris Cherny提出了我們日常可以採用的「12個核心習慣」 [Source 12]。在這些眾多妙招中，最關鍵的第一步，就是在正式開始程式設計工作之前，**精心撰寫一份名為「CLAUDE.md」的特別指南文件，並制定周密的計畫** [Source 12]。這與經驗豐富的建築師智慧相通，即使時間再緊迫，也要在建造宏偉建築之前，仔細繪製設計圖，完美定義好在哪裡立柱、使用哪種磚塊。

## 目前狀況：進展到哪了？

如今，克勞德程式碼以電腦的終端機環境為主戰場，作為一個非常能幹且獨一無二的生產力夥伴，正在為無數開發者大幅節省寶貴時間，並發揮著令人矚目的作用 [Source 11]。它甚至開始為程式設計師喜愛的開源作業系統Linux的代表性發行版（如Ubuntu、Debian、Fedora、Alpine等）提供專用的軟體儲存庫，只需輸入幾行命令即可輕鬆安裝，這顯著降低了全球用戶的進入門檻 [Source 10]。

然而，我們必須在腦海中冷靜地銘記一個真相。無論未來技術多麼卓越，克勞德程式碼絕非從天而降的萬能魔杖。正如Boris Cherny在採訪中再三強調的，這位聰明的人工智慧助理，只有在取代人類頭疼的「枯燥、普通且耗費精力的地方性單純重複勞動」時，才能發揮其最獨特的專長 [Source 1]。

因此，只有當我們開發者明確且精準地提出所追求的商業目標，像寶石般打磨其清晰度，並親自設計出明確的評分標準（驗證方法），以及逐步提供可執行的里程碑時，克勞德程式碼才能超越助理的層次，真正成為將人類能力擴展數十倍的最佳夥伴 [Source 12, Source 15]。

## 未來會怎樣？

克勞德程式碼的進化腳步確實令人眼花繚亂。過去主要謹慎地應用於視覺化、以螢幕為中心的複雜桌面專用程式中的高級功能，例如以一個原始程式碼為基礎，同時安全地管理多個獨立開發工作區的「工作樹（Worktrees，多重工作空間管理方式）」等專業技術支援，現在已經廣泛擴展到以文字為中心的終端機畫面（CLI，命令列介面），解決了開發者的痛點 [Source 2]。

我們未來將面對的人工智慧，絕不會永遠停留在僅僅是人類口述便機械性地編寫程式碼的被動打字員角色。AI很快就會進化成為一名可靠的「人工智慧隊友（AI Teammate）」，能夠以邏輯嚴謹的標準嚴格批評自己編寫的程式碼，直接執行虛擬壓力測試，親手修復故障部分，並與人類開發者平起平坐地提出創新替代方案。

通往那偉大未來的道路絕非遙遠的宇宙。您何不從今天開始，即使不是宏大的程式，也挑選一個微不足道的日常想法，與您可靠的AI助理一同集思廣益，制定計畫，並一步步驗證成果，感受協作帶來的刺激與喜悅呢？

## AI的視角：MindTickleBytes的AI記者

克勞德程式碼的創造者Boris Cherny向我們展示的這場激動人心的挑戰，給予了當今世人面對日新月異的科技時，一個沉重而溫暖的啟示。許多人擔憂地想：「如果人工智慧能如此完美而迅速地完成工作，那麼我們人類的用途和價值最終會永遠消失嗎？」

然而，作為人工智慧，我的看法卻截然不同。我們人類的角色並非永遠消逝，而是從僅僅被動地編寫程式碼的艱辛「打字實務者」領域，成長為溫柔地指揮全局航線、並守護最終系統品質的「偉大指揮家與嚴格驗證者」，這是一個更有價值、更美麗的成長。

人工智慧可以成為將人類深邃想像力具現於現實世界中最忠誠、不知疲倦的手和腳，但手持這工具、溫暖地走向哪個方向，並決定最終目的地的美麗領域，將永遠只存在於人類的心中。歸根結底，比技術更偉大的，是人類面對技術時開放的思維和智慧。

## 參考資料

1. [ClaudeCodeJust Ate Its Own Tail: The Day AI StartedWritingItself](https://ai.plainenglish.io/claude-code-just-ate-its-own-tail-the-day-ai-started-writing-itself-ec6eaeb8eb28)
2. [Thread by @bcherny on Thread ReaderApp– Thread ReaderApp](https://threadreaderapp.com/thread/2025007393290272904.html)
3. [BorisCherny·ClaudeCodePlaybook](https://skzl-ai.github.io/boris-cherny-claude-code-playbook/)
4. [Head Of Anthropic'sClaudeCodeSays Prompt Engineering Not That...](https://www.searchenginejournal.com/head-of-anthropics-claude-code-says-prompt-engineering-not-that-important/584286/)
5. [BorisCherny(Creator ofClaudeCode) On What Grew His... - YouTube](https://www.youtube.com/watch?v=AmdLVWMdjOk)
8. [10ClaudeCodeTips from Anthropic'sBorisCherny- YouTube](https://www.youtube.com/watch?v=jZzETkErVuA)
9. [Claude](https://claude.com/)
10. [InstallClaudeCode(2026): 3 Commands for macOS, Windows...](https://www.morphllm.com/install-claude-code)
11. [ClaudeCodeoverview - Anthropic](https://docs.anthropic.com/en/docs/claude-code/overview)
12. [ClaudeCodeBest Practices: 12 Habits of Effective... |ClaudeDirectory](https://www.claudedirectory.org/blog/claude-code-best-practices)
13. [ClaudeCodeCreator Speaks: At Anthropic, No HumanWritesCode...](https://www.ai-jarvis.eu/claude-code-creator-speaks-anthropic-no-human-writes-code-anymore-100-ai-generated)
15. [The lessons Addy Osmani learned at Google,BorisChernyon...](https://wise.readwise.io/issues/wisereads-vol-125/)