---
layout: post
title: "Arc 瀏覽器要消失了？上海高中生花 3 週打造的奇蹟 Mac 瀏覽器「Zigzag」"
description: "作為 2026 年 12 月即將終止的 Arc 瀏覽器之替代方案，由上海高中生開發者使用 Swift 與 WebKit 僅花 3 週開發的超輕量 Mac 瀏覽器「Zigzag」全解析。"
summary: "受到 Arc 瀏覽器終止消息震撼的上海高中生僅花 3 週開發，18MB 超輕量 Mac 瀏覽器「Zigzag」的特點與開發秘辛。"
tags: [Zigzag, Arc, MacBrowser, WebKit, OpenSource]
image: 2026-11-17-Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc.jpg
image_alt: "顯示在 Mac 畫面上的簡潔側邊欄與分割視圖功能的 Zigzag 瀏覽器介面畫面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "沒有在大企業終止服務的決定前挫折，而是透過親自動手寫扣來尋找答案的高中生開發者之執著令人印象深刻。這是一個為日益沉重的現代瀏覽器生態系帶來清新衝擊的輕量化替代方案。"
quiz:
  - question: "開發 Zigzag 瀏覽器的開發者背景是什麼？"
    choices: ["矽谷的資深瀏覽器工程師", "來自上海的高中生", "歐洲的開源研究員"]
    answer: 1
    explanation: "Zigzag 是來自上海的高中生開發者 ZigaoWang 受到 Arc 瀏覽器終止消息的震撼後，花費 3 週親自開發的瀏覽器 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。"
  - question: "Zigzag 瀏覽器所基於的蘋果引擎是什麼？"
    choices: ["Chromium 引擎", "WebKit 引擎", "Gecko 引擎"]
    answer: 1
    explanation: "Zigzag 並非使用 Chromium 或 Electron，而是採用蘋果純粹的 WebKit 引擎與 Swift 語言製作 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。"
  - question: "Zigzag 瀏覽器的安裝容量大約是多少？"
    choices: ["約 18 MB", "約 871 MB", "約 1.5 GB"]
    answer: 0
    explanation: "Zigzag 卸下了不必要的沉重負擔，擁有約 18 MB 的超輕量安裝容量 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。"
lang: zh-tw
ref: 2026-11-17-Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc
---

想像一下。每天早晨打開電腦、整理工作與個人生活時，你開啟了一個像量身訂製抽屜般整潔有序的瀏覽器視窗。與過去無數標籤頁橫向排列而令人眼花撩亂的時期不同，優雅地位於畫面側邊的側邊欄與按空間（Space）分類，簡直是數位工作的新世界。就在某一天，晴天霹靂的消息傳來：「你每天使用的那個瀏覽器即將關閉。」

開發商 The Browser Company 宣布，曾以創新介面深受全球用戶喜愛的 Arc 瀏覽器將僅支援至 2026 年 12 月 22 日並完全終止服務 [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac)。這項消息讓 Mac 用戶陷入巨大的混亂中，因為他們無法再回到乏味的上方橫向標籤頁模式 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。就在此時，地球的另一端，有一位高中生開發者正面向這個絕望的局面發出挑戰。僅僅花費了 3 週時間，一款完美承載 Arc 用戶所懷念的一切之超輕量 Mac 瀏覽器──**Zigzag** 就此誕生 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

---

## 這為什麼重要？

現代的網路瀏覽器變得越來越沉重。為了塞入無數功能，它們像黑洞般吞噬 RAM（記憶體），以光速消耗電量，程式安裝容量也動輒從數百 MB 跨越到 1 GB 以上。事實上，即將終止的 Arc 瀏覽器其安裝容量就高達 800 MB 以上 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。 

對一般用戶而言，這等於是為了上網瀏覽，就得將電腦大部分的資源拱手讓給瀏覽器。況且大企業的服務一旦終止，用戶便會莫名其妙地失去熟悉的工具，只能四處尋找其他替代方案。 

Zigzag 正是對這種現代軟體的龐大與封閉性展開了反叛。其安裝容量僅有區區 **18 MB** [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)，不需要註冊帳號，且完全排除遙測（用戶行為追蹤資料）與分析工具，保障了完整的隱私 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。由於是由個人製作的開源專案，因此沒有人能夠隨意中斷其服務，任何人都可以修改並精進程式碼 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

---

## 輕鬆理解：打造針對 Mac 優化的量身訂製跑車

比方說：如果過去許多瀏覽器就像是裝載巨大公車引擎、到處載運沈重行李的大型卡車，那麼 Zigzag 就可以比喻為配合 Mac 這項精緻結構所打造的流線型輕量電動跑車。換句話說，它果斷地卸下了不必要的重量，僅專注於最核心的駕駛性能。

Zigzag 並非基於 Google 的 Chromium（作為 Chrome 瀏覽器骨架的開源引擎）或 Electron（能以網頁技術製作桌面 App 的框架）所打造的沉重瀏覽器 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。它利用了蘋果預設在 Mac 作業系統（macOS）中的純正 **WebKit（在畫面上渲染網頁的核心引擎）** 引擎，並使用 Mac 專用程式語言 **Swift（用於製作蘋果裝置 App 的程式語言）** 從頭重新編寫 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。 

這就像是在智慧型手機上下載照片修圖 App 時，比起使用在所有機型上都能勉強運用的沉重通用程式，直接利用 iPhone 核心系統功能所製作的專用相機 App 不僅更快，耗電量也更少一樣。正因如此，它輕巧且不拖泥帶水，並帶來彷彿與 Mac 作業系統完美融為一體的流暢感。

此外，它也毫無保留地繼承了 Arc 瀏覽器用戶最為瘋狂的核心功能：
- **側邊欄與空間（Spaces）**：分頁不排列在視窗上方而是垂直排列於左側，並可依工作用、個人用等分類顏色，透過滑動切換的空間管理功能 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser: The polished, native Mac browser for life ...](https://www.producthunt.com/products/zigzag-browser)
- **分割視圖（Split View）**：在單一視窗中同時開啟最多 4 個頁面進行多工作業的畫面分割功能 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)
- **Peek（預覽）與指令列**：不需在新視窗中開啟連結即可稍微預覽的快速連結預覽與快速指令執行列 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)

---

## 目前狀況：僅花 3 週開發，以及完美的遷移

打造這款驚人瀏覽器的主角是來自上海的高中生開發者 **ZigaoWang** [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。他表示自己平時每天都在使用 Arc 瀏覽器並感到十分滿意、毫無怨言，因此對於 The Browser Company 突如其來的終止公告感到相當震驚 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。基於「不想再回到乏味的上方標籤頁」這項單純卻強烈的動機，他在過去 3 週裡親自動手敲擊鍵盤設計了 Zigzag [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

用戶從原有瀏覽器轉換時遭遇的最大痛苦，就是「重新設定設定與登入資訊的繁瑣過程」。然而，Zigzag 透過單次點擊就解決了這個問題。只要從包括 Arc 在內的其它瀏覽器執行一次匯入（Import，載入其他程式資料的功能），先前使用的空間、固定的釘選項目、瀏覽紀錄、儲存的密碼與 Cookie 等就會完整轉移 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。一打開瀏覽器就能直接在先前使用的網站上保持登入狀態並繼續工作 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser: The polished, nativeMacbrowserforlife afterArc](https://www.producthunt.com/products/zigzag-3)。

特別是，儘管它是基於 WebKit 引擎，卻能夠直接安裝 **Chrome 線上應用程式商店（Chrome Web Store，下載 Google Chrome 擴充功能的線上市場）**的擴充功能，這是一大強項 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。像是 1Password 或 Bitwarden 等密碼管理器、Dark Reader（深色模式）、Return YouTube Dislike、Tampermonkey 等平時常用的必備擴充功能都可以直接拿來使用 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。 

此外，它還內建了基於 uBlock Origin 與 Easylist 過濾器的**強大內建廣告攔截功能**，並會自動拒絕那些煩人且遮擋畫面的 Cookie 同意彈跳視窗，將其從眼前清除 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

---

## 未來將如何發展？

隨著 Arc 瀏覽器官方支援終止日 2026 年 12 月 22 日的臨近 [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac)，尋找替代方案的用戶行動將會更加頻繁。在由網路巨頭主導的瀏覽器市場中，由高中生開發者以開源形式推出的 Zigzag 正在大企業為中心的生態系中掀起一場微小的板塊運動。

用戶不再需要受到巨型企業單方面終止服務通知的擺布。由於它是原始碼公開且任何人都能參與的開源專案 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)，因此很有可能吸引全球開發者齊聚一堂，成長為更加堅固且安全的 Mac 專用瀏覽器。如果你正在尋找一個輕量、快速且能守護個人隱私的專屬上網空間，Zigzag 將會是即將到來的冬天中最具魅力的選擇。

---

## AI 的視點

MindTickleBytes 的 AI 記者視點：技術的進步不一定只來自龐大資本與數百名工程師。無法忍受不便並在短短 3 週內透過程式碼解決問題的高中生熱情，喚醒了我們軟體本質上的價值是什麼。如果對變得沉重的大型科技服務感到疲憊，現在正是關注像 Zigzag 這樣輕量且透明開源專案躍升的好時機。

---

## 參考資料

1. [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)
2. [Zigzag Browser: The polished, native Mac browser for life ...](https://www.producthunt.com/products/zigzag-browser)
3. [Zigzag: A Lightweight Web Browser for Mac](https://zigzagbrowser.com/)
4. [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)
5. [[5-Minute Review] The Mac browser 'Zigzag Browser' that lets ...](https://note.com/1sht0s/n/n5aa2825dac32?hl=en)
6. [Hacker News => Show](https://www.hacker-news.news/Show)
7. [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)
8. [byearc: newbrowserssto replaceArc](https://byearc.com/)
9. [DownloadArc](https://arc.net/download)
10. [DiaBrowserReview 2026: Is It Worth It? Pricing vsArc| Macfolio](https://macfolio.com/blog/dia-browser-review)
11. [ZigzagBrowser: The polished,nativeMacbrowserforlife afterArc](https://www.producthunt.com/products/zigzag-3)
12. [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac)