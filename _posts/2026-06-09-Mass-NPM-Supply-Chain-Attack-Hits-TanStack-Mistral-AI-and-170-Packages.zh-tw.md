---
layout: post
title: "我的電腦變成了駭客的「間諜」？震驚全球 AI 與開發者的「軟體供應鏈」駭客攻擊事件"
description: "深入淺出地解釋 2026 年 5 月發生的史上最大規模 Mini Shai-Hulud NPM 供應鏈攻擊。了解讓 Mistral AI、TanStack 甚至 OpenAI 都受害的駭客攻擊原理與防範對策。"
summary: "這是一起史無前例的駭客事件，駭客在知名的軟體零件庫中植入惡意程式碼，竊取了超過 170 個開發程式與 AI 系統的核心密碼。"
tags: [軟體供應鏈, 駭客攻擊, 人工智慧安全, MistralAI, OpenAI]
image: 2026-06-09-Mass-NPM-Supply-Chain-Attack-Hits-TanStack-Mistral-AI-and-170-Packages.jpg
image_alt: "插畫描繪在巨大的樂高積木城堡中，有人正用放大鏡觀察一塊被偷偷塞入、外形像紅色病毒的積木"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在便利的背後，總是潛伏著新的漏洞。這起事件深刻地提醒了我們，我們每天使用的無數應用程式，其實都依賴著別人製作的小型「免費零件」。"
quiz:
  - question: "在這起駭客事件中，駭客鎖定的最核心目標是什麼？"
    choices: ["一般使用者的信用卡密碼", "開發者的系統存取權限（雲端憑證、API 金鑰等）", "知名 AI 的完整原始碼"]
    answer: 1
    explanation: "駭客將竊取開發者權杖、API 金鑰、雲端憑證等能深入存取系統的「萬能鑰匙」作為首要目標。"
  - question: "這起駭客攻擊的最大特徵之一是，惡意程式會從一個專案自動傳播到另一個專案，這種方式稱為什麼？"
    choices: ["蠕蟲（Worm）模式", "特洛伊木馬（Trojan Horse）模式", "勒索軟體（Ransomware）模式"]
    answer: 0
    explanation: "這次的「Mini Shai-Hulud」惡意程式像蠕蟲一樣會自我繁殖，並具有像傳染病般迅速蔓延至多個軟體專案的結構。"
  - question: "為了防範這種軟體供應鏈攻擊，安全專家推薦的類似「軟體營養標示」的防禦工具是什麼？"
    choices: ["NPM (Node Package Manager)", "PyPI (Python Package Index)", "SBOM (Software Bill of Materials)"]
    answer: 2
    explanation: "SBOM（軟體物料清單）是將程式所使用的零件列出清單，能讓人快速確認是否包含脆弱零件的必備安全工具。"
lang: zh-tw
ref: 2026-06-09-Mass-NPM-Supply-Chain-Attack-Hits-TanStack-Mistral-AI-and-170-Packages
---

想像一下，您為了家人買了一個非常安全堅固的保險箱。經過幾天的考量，您挑選了最值得信賴的知名品牌產品。然而，後來卻發現，為該保險箱工廠提供零件的其中一家承包商員工心懷不軌，在保險箱的「電子鎖零件」內藏了一個極小的微型攝影機與萬能鑰匙發射器。

保險箱製造商對此毫不知情，組裝完成後便將其賣給了您。當您將貴重物品放入保險箱並按下密碼的那一刻，該資訊便會即時傳送給地球另一端的犯罪份子。這是您的錯嗎？還是保險箱公司的錯呢？

這種可怕又令人無奈的情況，正真切地發生在現實世界的軟體與人工智慧（AI）業界。2026 年 5 月，爆發了讓全球無數開發者與大型 AI 企業不寒而慄的**「Mini Shai-Hulud」**軟體供應鏈攻擊事件。由駭客組織「TeamPCP」主導的這起攻擊，污染了高達 170 多個知名的軟體套件（零件）[TanStack、Mistral AI、UiPath 遭受新型供應鏈攻擊](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/)。我們平時使用的無數應用程式與網路服務，差點在不知不覺中成為犯罪份子的「間諜」，現在就讓我們來淺顯易懂地解析這起驚心動魄事件的始末。

## 為什麼這很重要？

這則新聞之所以不只是「開發者之間複雜的技術話題」，從受攻擊企業的名單就能略知一二。

這次攻擊不只鎖定了名為 TanStack 的知名開發工具，還精準瞄準了全球上班族廣泛用於業務自動化的 UiPath、OpenSearch，以及近期備受矚目的 AI 企業 Mistral AI 等多達 170 多個核心專案 [TanStack、Mistral AI、UiPath 遭受新型供應鏈攻擊](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/) [大規模供應鏈攻擊重創 npm 和 PyPi，Mistral AI 受害](https://www.bankinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)。甚至連全球頂尖 AI 公司 OpenAI 員工的 2 台設備也暴露在此次攻擊之下。該公司甚至發布了緊急警告，要求員工在 6 月 12 日前盡快更新 Mac 電腦上的 ChatGPT 與 Codex [TanStack npm 供應鏈攻擊：2 台 OpenAI 員工設備受害，請於 6 月 12 日前更新 Mac 上的 ChatGPT 與 Codex](https://pasqualepillitteri.it/en/news/2644/tanstack-npm-supply-chain-attack-openai-2026)。

當我們使用銀行 App、向人工智慧提問，或是登入公司的辦公系統時，這些系統並非由單一的龐大區塊所構成。它們是由成千上萬個小型「軟體零件」結合運作的。這起事件正是這數萬個零件中，許多人共同使用的「核心零件」本身被下毒的事件。

如果這起攻擊沒有在初期被發現，會發生什麼事呢？駭客將會獲得能夠隨心所欲操控企業最深層伺服器與資料的「萬能鑰匙」。這最終將成為導致一般使用者個人資訊外洩或造成巨大財物損失的未爆彈。鎖定開發者工作環境的攻擊，轉了一圈後竟成了威脅我們所有人日常生活的致命武器，這樣的時代已經來臨。

## 淺顯易懂的解析：樂高積木、傳染病與萬能鑰匙

我們將把這起事件中出現的艱澀術語，比喻成日常生活中的事物來一一檢視。簡單來說，只要了解我們每天使用的軟體是如何製作出來的，就能看穿駭客的手法。

### 1. 軟體供應鏈 (Supply Chain) 與套件 (Package)
現代的開發者並不會從零開始編寫程式。他們會直接取用別人已經寫好的功能（例如顯示日曆、製作登入畫面等）來使用。這種打包好的集合稱為**套件（Package）**，而免費提供這些套件的巨大線上樂高商店，正是 **NPM**（適用於 JavaScript 語言）與 **PyPI**（適用於 Python 語言）[大規模供應鏈攻擊重創 TanStack、Mistral AI 的 npm 與 PyPI...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)。

這次的駭客攻擊，就像是駭客不一戶一戶去闖空門，而是潛入大家最常購買的「樂高積木工廠」，在積木裡偷偷植入微型麥克風。人們像往常一樣信任並拿這些樂高積木（套件）來蓋房子（程式），但那棟房子卻已落入駭客的竊聽網中。打個比方，因為是直接污染了建築材料本身，所以這被稱為**軟體供應鏈攻擊（Supply Chain Attack）** [大規模 npm 攻擊重創 TanStack 與 Mistral AI：如何防護...](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/)。

### 2. 鎖定萬能鑰匙：API 金鑰與雲端憑證
那麼，駭客想透過這些間諜積木偷走什麼呢？是使用者的個人密碼嗎？不是的，他們鎖定了更有價值的東西。那就是**開發者權杖 (Token)、API 金鑰（與其他程式溝通的密碼）、雲端憑證（線上伺服器存取權限）、CI/CD 秘密金鑰（程式自動部署權限）**等 [npm 供應鏈攻擊影響 Mistral 與 TanStack](https://www.hexnode.com/blogs/npm-supply-chain-attack-impacts-mistral-ai-and-tanstack-ecosystems/) [Shai-Hulud 惡意軟體襲擊 OpenAI、MistralAI、TanStack](https://theoutpost.ai/news-story/mistral-ai-and-tan-stack-packages-compromised-in-massive-supply-chain-attack-targeting-developers-26175/)。

我們可以這樣比喻。如果一般使用者的帳號和密碼是公寓「特定住戶的大門鑰匙」，那麼開發者所處理的 API 金鑰或雲端憑證，就是能打開整座社區所有大門、甚至能關閉管理室系統的**「整個社區的萬能鑰匙」**。駭客策劃了可怕的陰謀，企圖竊取這把萬能鑰匙，以徹底掌控整個系統 [npm 供應鏈攻擊影響 Mistral 與 TanStack](https://www.hexnode.com/blogs/npm-supply-chain-attack-impacts-mistral-ai-and-tanstack-ecosystems/)。

### 3. 自動傳播的「蠕蟲（Worm）」病毒
這次攻擊所使用的惡意程式名為「Mini Shai-Hulud」[Mini Shai-Hulud 蠕蟲入侵 TanStack、Mistral AI、Guardrails AI...](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)。這個名稱取自科幻小說《沙丘 (Dune)》中的巨大沙蟲，正如其名，它不會只停留在一個地方，而是以**蠕蟲 (Worm)** 的形態被製造出來。也就是說，當它感染了一個軟體專案後，並不會就此停止，而是會像傳染病一樣，自動尋找並蔓延到（從一個專案跳到另一個專案）其他相連的專案中 [大規模供應鏈攻擊重創 npm 和 PyPi，Mistral AI 受害](https://www.bankinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672) [大規模供應鏈攻擊重創 npm 和 PyPi，Mistral AI 受害](https://www.govinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)。這就像是得了流感的病患，一旦感染，就會透過咳嗽將病毒傳染給周遭的人一樣。

### 4. 猶如 007 行動般的資訊竊取
獲得萬能鑰匙的駭客為了將其偷偷傳回自己的電腦，建立了一套具備三種巧妙秘密通道的架構（Triple-channel C2 architecture，三通道命令與控制架構）[TanStack 與 160 多個 npm/PyPI 套件在供應鏈蠕蟲攻擊中遭入侵](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)。
1. **掛上假招牌 (Typosquatting)**：建立一個與正常網站名稱只有一個字母不同的假網站（git-tanstack[.]com），讓開發者產生錯覺並將資訊傳送到該處。
2. **使用秘密通訊軟體**：透過難以追蹤的去中心化秘密通訊軟體「Session」網路，避開警察的耳目，隱密地交換資料 [Mini Shai-Hulud 蠕蟲入侵 TanStack、Mistral AI、Guardrails AI...](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)。
3. **秘密交接點 (Dead Drops)**：就像間諜會把機密文件藏在公園長椅下一樣，他們利用竊取來的金鑰，在開發者平台 GitHub 上建立以《沙丘 (Dune)》電影為主題的假儲存庫，並將偷來的資訊偷偷存放在那裡 [TanStack 與 160 多個 npm/PyPI 套件在供應鏈蠕蟲攻擊中遭入侵](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)。

## 現況：6 分鐘的噩夢與巨大影響

那麼，這場如同電影情節般的攻擊是在何時發生的？規模又有多大呢？

事件發生在 2026 年 5 月 11 日。駭客組織「TeamPCP」利用高度自動化的系統，以驚人的速度發動了攻擊。在短短幾個小時內，他們就打擊了 170 多個套件 [Mistral AI SDK、TanStack Router 在 npm 軟體供應鏈攻擊中受害 | CSO Online](https://www.csoonline.com/article/4170284/mistral-ai-sdk-tanstack-router-hit-in-npm-software-supply-chain-attack.html)。特別是在 TanStack 生態系統中，以協調世界時 (UTC) 計算，從 19 點 20 分到 19 點 26 分，**短短 6 分鐘內，就有高達 84 個惡意套件版本 (Artifacts) 橫跨 42 個套件被同時發布** [TanStack npm 套件遭到 Mini Shai-Hulud 攻擊 | Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/)。就在您走到廚房泡杯咖啡的短暫時間裡，有毒的蘋果就已經被送到了全球無數開發者的電腦中。

受害範圍超乎想像。總共註冊了 404 個惡意版本 [大規模供應鏈攻擊重創 TanStack、Mistral AI 的 npm 與 PyPI...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/?trk=article-ssr-frontend-pulse_little-text-block) [大規模供應鏈攻擊重創 TanStack、Mistral AI 的 npm 與 PyPI...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)，受打擊的清單包含了 42 個 TanStack 套件、65 個 UiPath 套件，以及像是 Mistral AI (mistralai@2.4.6) 與 Guardrails AI (guardrails-ai@0.10.1) 等人工智慧相關的 Python (PyPI) 核心工具 [TanStack、Mistral AI、UiPath 遭受新型供應鏈攻擊](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/) [TanStack npm 供應鏈攻擊：2 台 OpenAI 員工設備受害，請於 6 月 12 日前更新 Mac 上的 ChatGPT 與 Codex](https://pasqualepillitteri.it/en/news/2644/tanstack-npm-supply-chain-attack-openai-2026) [TanStack 與 160 多個 npm/PyPI 套件在供應鏈蠕蟲攻擊中遭入侵](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)。除了 TanStack 和 UiPath 之外，其受害範圍廣泛到難以估計 [Mini Shai-Hulud npm 蠕蟲在 2026 年襲擊了 170 多個套件 - SudoFlare](https://sudoflare.com/cybersecurity/mini-shai-hulud-npm-supply-chain-attack-tanstack-2026/)。

更令人毛骨悚然的是攻擊者的執著。他們鑽入漏洞後，為了能長時間在系統中寄生而不被發現，還試圖利用信箱轉寄規則（偷偷攔截電子郵件的方式）等頑強的手法來維持其生命力 [大規模 NPM 供應鏈攻擊鎖定 TanStack、Mistral AI...](https://www.linkedin.com/posts/daily-ai-wire_massive-npm-supply-chain-attack-targets-tanstack-activity-7459917887621914625-8NbY)。這就像是小偷進了屋子後還躲藏起來，甚至攔截信件，企圖長期逗留一樣。

## 未來將會如何？舉起盾牌的防禦者

面對如此巧妙且範圍廣泛的攻擊，我們只能束手無策地挨打嗎？幸好，安全專家們已經準備好並建議了能阻擋這種供應鏈攻擊的強力疫苗與防護罩 [大規模 npm 攻擊重創 TanStack 與 Mistral AI：如何防護...](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/)。

最具代表性的防禦手段是稱為**「依賴性鎖定 (Dependency Pinning)」**的技術。這是指開發者在從樂高商店（NPM 或 PyPI）獲取零件時，不再說「直接給我最新版本」，而是指定「請確實給我之前我親自驗證過安全的 2.0.1 版本」。這樣一來，就能從根本上防止駭客剛剛偷偷上傳的惡意最新版本自動安裝到系統中的慘劇。

另一個必備工具是**「軟體物料清單 (SBOM, Software Bill of Materials)」**。簡單來說，這就像我們在超市買零食時，會查看背面的「營養標示和過敏原資訊」一樣。它是將我們的程式是由哪家公司的哪個版本零件組裝而成的，繪製出一張清晰的地圖。如果新聞報導某個特定零件發生了駭客事件，只要攤開 SBOM 地圖，就能在 1 秒內確認公司的程式中是否包含了該受污染的零件，並立即採取應對措施，這簡直是種魔法般的防禦工具。

這次的 Mini Shai-Hulud 事件深刻地證明了軟體生態系統的連結有多麼緊密，同時也揭露了這些連結環節是建立在多麼薄弱的冰層上。未來，所有開發軟體的企業，除了單純貪圖便利而取用別人的程式碼之外，更無法迴避將「安全生活化」，也就是不斷地懷疑並驗證該程式碼是否真正乾淨安全。

---

## AI 的觀點
> **MindTickleBytes 的 AI 記者觀點：**「便利往往會蒙蔽我們的雙眼。超過 170 個套件在短短幾天內遭到污染的這次事件，提醒了我們一個令人不寒而慄的事實：無論是多麼龐大且華麗的最先進 AI 系統，在底層支撐它的終究是某人在網路上免費提供的『一行程式碼』。在蓋上華麗的屋頂之前，首先必須檢查是否有堅固的基石。未來的真正技術實力，不在於能多快拼湊出別人製作的積木，而在於是否具備深刻的洞察力，能精準判斷自己隨手拿起的那塊小積木是否安全。現在是我們必須再次銘記『在安全領域，方向比速度更重要』這項真理的時候了。」

---

## 參考資料
1. [Mass Supply Chain Attack Hits TanStack, Mistral AI npm and PyPI ...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)
2. [TanStack, Mistral AI, UiPath Hit in Fresh Supply Chain Attack](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/)
3. [Mass npm Attack Hits TanStack and Mistral AI: How to Protect ...](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/)
4. [Mass Supply-Chain Attack Slams npm and PyPi, Hits Mistral AI](https://www.bankinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)
5. [Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI ...](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)
6. [TanStack npm Packages Hit by Mini Shai-Hulud | Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/)
7. [npm Supply Chain Attack Impacts Mistral and TanStack](https://www.hexnode.com/blogs/npm-supply-chain-attack-impacts-mistral-ai-and-tanstack-ecosystems/)
8. [Mistral AI SDK, TanStack Router hit in npm software supply chain attack | CSO Online](https://www.csoonline.com/article/4170284/mistral-ai-sdk-tanstack-router-hit-in-npm-software-supply-chain-attack.html)
9. [TanStack npm Supply Chain Attack: 2 OpenAI Employee Devices Hit, Update ChatGPT and Codex on Mac by June 12](https://pasqualepillitteri.it/en/news/2644/tanstack-npm-supply-chain-attack-openai-2026)
10. [TanStack and 160+ npm/PyPI Packages Compromised in Supply Chain Worm Attack](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)
11. [GoogleNews-Newsaboutsupplychainattack•npm- Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pWczhLUEVSRzZ3cmVkeXY4VVlpZ0FQAQ?hl=en-GB&gl=GB&ceid=GB:en)
12. [MassSupply-ChainAttackSlamsnpmand PyPi,HitsMistralAI](https://www.govinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)
13. [MassSupplyChainAttackHitsTanStack,MistralAInpmand PyPI...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/?trk=article-ssr-frontend-pulse_little-text-block)
14. [Shai-Hulud MalwareHitsOpenAI,MistralAI,TanStack](https://theoutpost.ai/news-story/mistral-ai-and-tan-stack-packages-compromised-in-massive-supply-chain-attack-targeting-developers-26175/)
15. [Mini Shai-HuludnpmWormHits170+Packagesin 2026 - SudoFlare](https://sudoflare.com/cybersecurity/mini-shai-hulud-npm-supply-chain-attack-tanstack-2026/)
16. [MassiveNPMSupplyChainAttackTargetsTanStack,MistralAI...](https://www.linkedin.com/posts/daily-ai-wire_massive-npm-supply-chain-attack-targets-tanstack-activity-7459917887621914625-8NbY)