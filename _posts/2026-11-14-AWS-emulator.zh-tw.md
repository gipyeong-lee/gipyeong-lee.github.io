---
layout: post
title: "AI 代理直接打造的 AWS 模擬器：如何在沒有雲端的情況下在我的電腦上執行 AWS"
description: "無需 AWS 帳戶或雲端部署，即可在本地電腦上以毫秒級測試幾乎所有 AWS 服務的開源工具「AWS Emulator」全解析"
summary: "透過由 AI 代理全面開發與測試的開源工具「AWS Emulator」，了解開發者與 AI 編碼代理如何在本地環境中高速測試 AWS API，省去雲端費用與等待時間。"
tags: [AWS, Emulator, AI, Rust, Cloud, TechNews]
image: 2026-11-14-AWS-emulator.jpg
image_alt: "描繪在本地電腦上測試雲端服務的插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "據報導，由 AI 代理而非人類工程師親自編寫程式碼並驗證完成的 AWS Emulator，被視為一個具有里程碑意義的代表性案例，展示了軟體開發範式正從以人類為中心轉向以代理為中心的協作。這將成為未來全面引爆軟體生態系統生產力的起點。"
quiz:
  - question: "負責開發與測試 AWS Emulator 的主體是誰？"
    choices: ["全球開源貢獻志願者", "全部由 AI 代理", "AWS 內部特定的雲端基礎設施團隊"]
    answer: 1
    explanation: "AWS Emulator 的所有程式碼都是由 AI 代理編寫和測試的。"
  - question: "使用 AWS Emulator 的必要條件是什麼？"
    choices: ["付費 AWS 帳戶與雲端部署", "高效能雲端伺服器執行個體", "無需 AWS 帳戶及雲端部署"]
    answer: 2
    explanation: "AWS Emulator 無需 AWS 帳戶或雲端部署，即可在本地電腦上免費執行。"
  - question: "AWS Emulator 是用哪種程式語言編寫的？"
    choices: ["Rust", "Python", "Go"]
    answer: 0
    explanation: "AWS Emulator 是一個以高效能與安全性著稱的 Rust 語言編寫的開源本地模擬器。"
lang: zh-tw
ref: 2026-11-14-AWS-emulator
---

想像一下，你正在開發一款新的智慧型手機應用程式。當應用程式拍照並上傳到伺服器時，它會被儲存在雲端儲存空間中，然後人工智慧 (AI) 會分析照片並返回結果。過去如果要測試這個功能，該怎麼做呢？你必須在亞馬遜網路服務 (AWS) 建立付費帳戶，將程式碼逐一上傳到雲端伺服器，然後等待幾秒鐘到幾分鐘才能得到結果。每次測試都會產生費用，如果在操作過程中網路中斷，工作就會直接停擺，這種不便過去只能理所當然地承受。

然而，如今技術生態系統的格局正在發生翻天覆地的變化。最近，亞馬遜發布了一款具有劃時代意義的工具，讓開發人員無需連接遠端雲端，就能在自己的電腦（本地）上幾乎完美地還原並測試 AWS 服務。這就是 **AWS Emulator（模擬器）** [[Test your applications against AWS locally with AWS Emulator](https://aws.amazon.com/blogs/aws/test-your-applications-against-aws-locally-with-aws-emulator/), [What is AWS Emulator?](https://docs.aws.amazon.com/emulator/latest/userguide/what-is-service.html)]。更令人驚訝的是，據報導，該程式的所有程式碼都不是由人類編寫的，而是由 **AI 代理**從頭到尾編寫並驗證的 [[AWSEmulator and the engineer's job when... | All Things Distributed](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineer-job-when-agents-write-the-code.html)]。在沒有人類介入的情況下，AI 透過協同合作完成了龐大的雲端模擬系統。

---

## 為什麼這很重要？

在軟體開發過程中，最枯燥、最浪費時間的時刻是什麼？那就是修改了一行程式碼後，將其部署到雲端，然後坐在螢幕前發呆等待其正常運作的等待時間。開發人員每天要重複數十、數百次這個沉悶的過程。

**AWS Emulator** 將這個令人沮喪的等待時間大幅縮短至毫秒（ms，1秒的千分之一）級別 [[Local AWS emulator for testing and CI | AWS Emulator](https://aws.amazon.com/products/developer-tools/emulator/)]。 

簡單比喻的話，這就像是在設計新車時，不需要每次都把車開上真正的高速公路行駛數十公里，而是能在超高精度的室內駕駛模擬器中於 1 秒內檢查性能。由於不需要實際開上道路，因此一滴燃料（雲端費用）都不用花，道路上發生事故的風險（部署錯誤與故障）也能從根本上被阻絕。 

特別是對於近年來大行其道的 AI 編碼代理（代替人類執行開發工作的 AI 程式）而言，這項工具無疑是如虎添翼。在人類看來，AI 代理能在眨眼間修改數十行程式碼，但如果在雲端部署和遠端測試過程中出現等待時間，整個工作流程就會突然中斷。如果模擬器能在你的電腦內以毫秒級的光速響應，AI 代理就能以比人類快數十倍的速度驗證程式碼並自行修復錯誤 [[Local AWS emulator for testing and CI | AWS Emulator](https://aws.amazon.com/products/developer-tools/emulator/), [AWSEmulator and the engineer's job when... | All Things Distributed](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineer-job-when-agents-write-the-code.html)]。

---

## 輕鬆理解：什麼是 AWS Emulator？

**AWS Emulator**（AWS 模擬器，在我的電腦中精確模仿並執行雲端服務行為的軟體程式）簡而言之就是**「住在筆記型電腦裡面的迷你雲端」**。

我們平時經常使用的 AWS SDK（軟體開發套件，幫助程式與 AWS 溝通的工具集合）或 CLI（命令列介面，在黑畫面上輸入文字指令的工具）指令可以原封不動地使用，只不過訊號不是飛到遠在太平洋彼岸的 AWS 資料中心，而是直接在筆記型電腦內立即處理的架構 [[Test your applications against AWS locally with AWS Emulator](https://aws.amazon.com/blogs/aws/test-your-applications-against-aws-locally-with-aws-emulator/), [Getting started with AWS Emulator](https://docs.aws.amazon.com/emulator/latest/userguide/getting-started.html)].

支撐這種高速處理的技術背景是嚴謹的模擬設計。這個工具使用 **Rust**（具備極高效能與電腦記憶體安全性的次世代程式語言）編寫，幾乎不佔用電腦資源，同時具備壓倒性的執行速度 [[Test your applications against AWS locally with AWS Emulator](https://aws.amazon.com/blogs/aws/test-your-applications-against-aws-locally-with-aws-emulator/)]. 

它精確建模了 400 多個複雜的雲端 API（應用程式介面，程式彼此對話的規則），完美支援 200 多種不同的 AWS 服務 [[AWSEmulator and the engineer's job when... | All Things Distributed](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineer-job-when-agents-write-the-code.html)]. 由於透過精確測量實際 AWS 的運作方式，將模擬器的忠實度（fidelity）發揮到極致，因此在本地電腦環境中完美執行的程式碼，在實際的雲端生產環境中也無需任何修改就能直接順暢運行 [[Test your applications against AWS locally with AWS Emulator](https://aws.amazon.com/blogs/aws/test-your-applications-against-aws-locally-with-aws-emulator/)].

---

## 現狀：誰製作的？目前進展到哪裡？

這個專案作為開源專案向全球公開，任何人都可以免費取用 [[Test your applications against AWS locally with AWS Emulator](https://aws.amazon.com/blogs/aws/test-your-applications-against-aws-locally-with-aws-emulator/)]. 相關原始碼與更新紀錄可以在官方儲存庫 [AWS emulator](https://github.com/aws/aws-emulator) 中即時查看 [[AWS emulator](https://github.com/aws/aws-emulator)].

如前所述，這個龐大的模擬器專案的程式碼並不是由人類工程師坐在書桌前敲擊鍵盤打造出來的 [[AWSEmulator and the engineer's job when... | All Things Distributed](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineer-job-when-agents-write-the-code.html)]. 高度進化的 AI 代理團隊投入其中，親自編寫了涵蓋 400 多個 API 模型與 200 多種 AWS 服務的龐大程式碼 [[AWSEmulator and the engineer's job when... | All Things Distributed](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineer-job-when-agents-write-the-code.html)]. 

據相關人員透露，AI 代理不僅僅是自己編寫程式碼，還經歷了一個自主循環過程：與實際 AWS 環境不斷進行對比並進行嚴格測試，自主識別並修正執行過程中發現的微小差異（落差） [[AWSEmulator and the engineer's job when... | All Things Distributed](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineer-job-when-agents-write-the-code.html)]. 這被視為一個歷史性的轉折點，表明 AI 已超越了單純的文字生成器或輔助工具，具備了從頭到尾自主設計與實現複雜系統軟體的真正工程能力 [[AWSEmulator and the engineer's job when... | All Things Distributed](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineer-job-when-agents-write-the-code.html)].

開發人員將其應用於實際工作中的方法也非常直觀且簡單。只需將程式安裝並執行在自己的電腦上，然後將平時使用的 AWS SDK 所指向的連線位址稍微更改為本地模擬器的位址即可 [[Getting started with AWS Emulator](https://docs.aws.amazon.com/emulator/latest/userguide/getting-started.html)]. 完全不需要複雜的 AWS 帳戶，即使在網路連線不穩定的環境下也能順利運行，當然也完全不需要支付任何雲端使用費用 [[Local AWS emulator for testing and CI | AWS Emulator](https://aws.amazon.com/products/developer-tools/emulator/), [Test your applications against AWS locally with AWS Emulator](https://aws.amazon.com/blogs/aws/test-your-applications-against-aws-locally-with-aws-emulator/), [AWSEmulator and the engineer's job when... | All Things Distributed](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineer-job-when-agents-write-the-code.html)].

---

## 未來將會如何？

以這次 AWS Emulator 的出現為起點，雲端運算產業正迎來巨大的範式轉變。過去所有的雲端測試都必須透過遠端伺服器進行，但展望未來，「本地優先 (Local-First)」測試環境預計將迅速在開發人員之間確立為新的標準。

1. **開發生產力的飛躍性提升**：開發人員現在即使在飛機上或網路連線不佳的偏遠地區，也能自由開發並徹底測試基於 AWS 的應用程式。
2. **AI 代理生態系統的加速**：由於 AI 編碼代理可以在本地環境中毫無成本負擔地進行數百、數千次測試，軟體開發的速度與品質將躍升至截然不同的層次。
3. **開源與 AI 結合模型的確立**：超越了以往由人類主導的模式，成功提出了由 AI 主導實現與驗證全過程的新型開源專案標準模型。

當然，模擬器可能無法 100% 完美取代實際雲端環境所具有的微小網路延遲或全球規模的不可預測變數。然而，在佔據開發週期大部分的初期開發、功能實現以及單元測試階段，這個工具將成為大幅節省開發人員時間與企業成本的最強大武器。

---

## MindTickleBytes 的 AI 記者視角

據報導，由非人類工程師逐行編寫的程式碼所組成的軟體被採納為官方開源項目，並完美模擬了數百個雲端服務，這一案例直觀地表明我們已經進入了以 AI 為中心的新時代。今後，技術的演進速度與開發組織的效率，將不再取決於人類開發人員有多優秀，而是取決於能否為 AI 代理提供完美且快速的本地測試環境。

---

## 參考資料

1. [AWS emulator](https://github.com/aws/aws-emulator)
2. [Local AWS emulator for testing and CI | AWS Emulator](https://aws.amazon.com/products/developer-tools/emulator/)
3. [Test your applications against AWS locally with AWS Emulator](https://aws.amazon.com/blogs/aws/test-your-applications-against-aws-locally-with-aws-emulator/)
4. [What is AWS Emulator?](https://docs.aws.amazon.com/emulator/latest/userguide/what-is-service.html)
5. [Getting started with AWS Emulator](https://docs.aws.amazon.com/emulator/latest/userguide/getting-started.html)
6. [Releases · aws/aws-emulator · GitHub](https://github.com/aws/aws-emulator/releases)
7. [AWSEmulator and the engineer's job when... | All Things Distributed](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineer-job-when-agents-write-the-code.html)