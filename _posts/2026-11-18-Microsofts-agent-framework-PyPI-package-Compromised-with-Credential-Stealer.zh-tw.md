---
layout: post
title: "微軟官方 AI 套件藏密碼間諜事件：究竟發生了什麼事？"
description: "微軟官方 Python 套件 'agent-framework' 遭駭客入侵以竊取使用者憑證，本文為您簡單解析這起供應鏈攻擊事件的始末與因應之道。"
summary: "2026年11月17日，微軟官方 Python 套件 'agent-framework' 被植入隱形間諜惡意程式。本文為您整理這個「下載即執行」攻擊的真相，以及我們必須了解的資安常識。"
tags: [資訊安全, Python, 供應鏈攻擊, 微軟, AI]
image: 2026-11-18-Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer.jpg
image_alt: "象徵數位安全的鎖頭與 Python 程式碼畫面的插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這看似僅與開發者有關，卻是突顯現代數位服務信任基礎有多脆弱的重要事件。我們比以往更需要透明且徹底的供應鏈驗證機制。"
quiz:
  - question: "這次遭到攻擊的微軟 Python 套件名稱是什麼？"
    choices: ["agent-framework", "azure-sdk", "microsoft-ai-tools"]
    answer: 0
    explanation: "微軟官方 Python 中介套件（meta-package）'agent-framework' 成為了攻擊目標。"
  - question: "為了讓惡意程式碼執行，使用者是否必須在程式碼中手動 import（呼叫）該套件？"
    choices: ["是的，必須透過程式碼載入才會執行。", "不是，在 Python 啟動或安裝時就會自動執行。", "只有在開啟智慧型手機應用程式時才會執行。"]
    answer: 1
    explanation: "它利用了 `.pth` 啟動掛鉤（startup hook），即使不將套件 import 到程式碼中，只要 Python 執行或安裝時就會自動運作。"
  - question: "這起事件後，專家建議採取的立即應變措施是什麼？"
    choices: ["將電腦格式化並重新安裝", "將版本釘選（Pinning）至 1.26.0 並替換主要密碼與金鑰", "註銷微軟帳號"]
    answer: 1
    explanation: "建議將版本釘選至安全的 1.26.0 版本，並替換（Rotate）Azure 與 GitHub Actions 等相關密鑰。"
lang: zh-tw
ref: 2026-11-18-Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer
---

想像一下，你收到了平日信賴的知名大企業所寄出的料理食材調理包。你才剛把紙箱拆開、放在餐桌上，家裡的保險箱鑰匙和大門密碼卻已經悄悄傳送給了某人。儘管你根本還沒開始做菜，甚至也沒拆開任何食材包裝。

在軟體開發的世界裡，類似的事實上真的發生了。全球大型科技企業微軟（Microsoft）所提供的官方工具箱中，有人偷偷安插了「資訊小偷」 [Source 18]。讓我們用最簡單的方式，來拆解這起讓全球無數開發者大吃一驚的資安事件全貌。

---

## 為什麼這很重要？

就像我們在智慧型手機上使用應用程式時，會從 Apple App Store 或 Google Play 商店下載經過安全驗證的 App 一樣，程式設計師也會引用無數的開源工具來打造程式。此時，開發者所使用的 Python 程式語言官方軟體倉庫——Python 套件索引（PyPI, Python Package Index）中，微軟的官方套件 **'agent-framework'** 卻被植入了惡意程式碼 [Source 3, Source 18]。

比喻來說，這就像是全球無數餐飲連鎖店共同使用的核心食材物流網中，有人被混入了雜質。這個套件每個月下載次數高達近 20 萬次，是全球開發現場廣泛使用的重要工具 [Source 3]。一旦企業或開發者的電腦、自動化伺服器（CI/CD 環境，持續整合與持續部署環境）安裝了包含惡意程式碼的版本，雲端服務存取權限或密鑰等敏感資訊就可能被一網打盡，情況相當危險 [Source 17, Source 18]。這不僅是開發者個人的單純疏失，更是一起可能威脅到使用其服務之廣大一般民眾數位安全的重大供應鏈資安事故。

---

## 輕鬆理解：藏在快遞箱裡的超小型間諜

軟體供應鏈攻擊（Supply Chain Attack）就像是攔截了信賴的大型物流商貨車，並在原廠紙箱內巧妙偽裝、暗中塞入監聽裝置一樣。

簡單來說，這次事件的運作方式可以用日常生活的比喻來解釋：
1. **信任陷阱**：開發者憑藉對微軟品牌的信任與官方倉庫的信心，像平常一樣下載所需的工具（透過 `pip install` 指令安裝） [Source 18]。
2. **無形潛入**：通常惡意程式碼必須手動執行程式或呼叫特定功能時才會運作。但這次的惡意程式碼利用了名為 `.pth` 檔案的 Python 啟動掛鉤（startup hook，指程式啟動時自動執行程式碼的技術） [Source 7, Source 18]。這就像是一個連快遞箱都還沒打開、只要搬進房間就會自動運作的超小型監聽器，開發者即使沒有在程式碼中直接呼叫（import）該套件，僅僅是安裝了它，就會在 Python 環境中自動執行 [Source 18]。
3. **機密外洩**：這個悄悄甦醒的間諜程式迅速搜刮了電腦環境變數或重要設定檔中儲存的密碼，以及雲端控制權限（Azure DevOps、Azure 託管身分 Azure managed identity、GitHub Actions 金鑰等），並透過 Webhook（基於網頁的通知服務）瞬間傳送給攻擊者的外部伺服器 [Source 7, Source 17, Source 18]。

---

## 現狀與事件全貌

根據資安業界與外媒報導，這起縝密的供應鏈入侵事件發生於 2026 年 11 月 17 日 [Source 3]。

- **發生時間與版本**：微軟官方中介套件 `agent-framework` 的 **1.26.1** 與 **1.26.2 版本**在短短 33 分鐘內相繼註冊到 PyPI 上 [Source 3, Source 16, Source 18]。這兩個版本中都藏有竊取使用者認證資訊的憑證竊取程式（credential stealer） [Source 3]。
- **迅速應變**：幸虧全球資安專家與自動化監控系統的快速偵測，這兩個惡意檔案在問世僅 45 分鐘後，就被微軟與倉庫管理員緊急隔離並刪除 [Source 3, Source 16]。
- **受害範圍與目標**：這個惡意程式碼主要鎖定廣泛應用於雲端基礎設施環境的 Azure 相關認證資訊，以及 GitHub Actions 的自動化機密金鑰 [Source 7, Source 17, Source 18]。

---

## 未來會怎麼樣？（安全的應變方法）

這起轉瞬之間發生的供應鏈攻擊，再次深刻提醒我們「在數位世界裡，沒有任何人可以 100% 盲目信任」的資安鐵律。如果開發者或企業在這段期間接觸過相關套件，必須立即採取以下應變措施 [Source 7]：

1. **版本釘選（Pinning）**：徹底避開有問題的漏洞版本，將版本確實釘選回已驗證安全的舊版本 **1.26.0** [Source 7]。
2. **全面更換金鑰（Rotation）**：如果在包含惡意版本的開發環境中曾安裝過該套件哪怕只有一次，為了防範未然的洩漏事故，必須立即將 Azure 相關認證與 GitHub Actions 金鑰替換（Rotate）為全新數值 [Source 7]。
3. **強化供應鏈監控**：不能再單純因為是知名開源套件而掉以輕心，全球正加速導入能在自動化開發管線（CI/CD）的全程中實時驗證套件完整性之高階資安解決方案的趨勢。

---

## AI 的視角

這雖然容易被歸咎為開發者才有的問題，但這起事件其實是現代數位社會建立在多麼複雜交織的信任基礎上的一個代表性縮影。我們每天使用的智慧型手機 App、網路服務、雲端系統背後，都交織著成千上萬個開源套件。只要一個小小的螺絲釘（套件）動搖，巨大的大樓（服務）全體都可能陷入危機。未來，編寫程式碼的能力固然重要，但能否透明且徹底地驗證我們所使用的工具之信任度，將是比以往任何時候都更加迫切的資安時代。

---

## 參考資料

1. [Microsoft's agent-framework PyPI package Compromised with Credential Stealer](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer) [Source 1]
2. [Secure PyPI Packages - 16K+ Projects From PyPI](https://www.bing.com/aclick?ld=e8MGxqEwIckNRkofSDE9RZSzVUCUyhyXQCO9oiZ32AYVUcUCdcy_8e_QkCWirnWclBVub227fMt1Iuf2-P6lDskhNij9dIiDNkedC4XdnJP9wL2_LmCVh66uI5MiHE9AYc_t7-cA48zWJAibzw_Sdeur1Rkvj3S5WDklw4rqi-TldMjbUNm2GDN3O9sU5mzhn5oCppHVAfmiRkciJcmY42dYa4tMo&u=aHR0cHMlM2EklMmZ2d3cuY2hhaW5ndWFyZC5kZXYlMmZwcm9kdWN0cyUyZmxpYnJhcmllcyUyZnB5dGhvbiUzZm1zY2xraWQlM2Q2ZmUwMDdhYjIzNmQxYjI2ZWUzZjZkNTY3NGY3ZjA1MyUyNnV0bV9zb3VyY2UlM2RiaW5nJTI2dXRtX21lZGl1bUlzZGNwYyUyNnV0bV9jYW1wYWlnbiUzZGJnX3NfYXBhY19hY3FfZ2VuZXJpY19ib2YlMjZ1dG1fdGVybSUzZHB5cGklMjUyOG1hbHdhcmUlMjZ1dG1fd29udGVudCUzZGxpYnJhcmllc19weXBp&rlid=6fe007ab236d1b26ee3f6d5674f7f053) [Source 2]
3. [Microsoft agent-framework Compromised: Credential Stealer ...](https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi) [Source 3]
4. [PyPI agent-framework 1.26.1: Credential Stealer Fix ...](https://explainx.ai/blog/microsoft-agent-framework-pypi-1-26-credential-stealer-november-2026) [Source 7]
5. [Inside the LiteLLM 1.107.0 supply chain compromise: Credential theft...](https://threatnoir.com/article/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-pyth-e59453) [Source 11]
6. [[Security]: litellm PyPI package (v1.82.7 + v1.82.8) compromised...](https://github.com/BerriAI/litellm/issues/24518) [Source 12]
7. [Download Microsoft Visual C++ 2010 Service Pack 1 Redistributable...](https://www.microsoft.com/en-us/download/details.aspx?id=26999) [Source 14]
8. [LiteLLM PyPI Supply Chain Attack — Credential Stealer in... — al-ice.ai](https://al-ice.ai/posts/2026/07/litellm-pypi-supply-chain-attack-credential-stealer/) [Source 15]
9. [Microsoft's agent-framework on PyPI shipped a credential ...](https://techbytes.app/posts/microsofts-agent-framework-on-pypi-shipped-a-credential-stealer-in/) [Source 16]
10. [Two malicious agent-framework releases on PyPI carried a ...](https://pulse.adyog.com/briefs/two-malicious-agent-framework-releases-on-pypi-carried-a-sec) [Source 17]
11. [Microsoft agent-framework Compromised Twice on PyPI](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise) [Source 18]