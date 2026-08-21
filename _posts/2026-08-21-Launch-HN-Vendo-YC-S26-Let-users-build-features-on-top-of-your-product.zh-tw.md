---
layout: post
title: "當您的工作流程，能由 AI 自動為您量身打造功能，會是什麼樣子？"
description: "深入了解 Vendo，這項解決 B2B SaaS 服務常見「功能需求積壓」難題的方案，讓使用者能親手打造自己需要的功能。"
summary: "Vendo 是一個開源的使用者自定義層，能讓企業軟體的使用者無須開發者協助，直接在產品上方建立所需的特定功能或應用程式。"
tags: [AI, SaaS, B2B, Vendo, 生產力]
image: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product.jpg
image_alt: "抽象表現使用者在現有軟體介面上，親手配置所需功能的意象圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是軟體主導權從開發商轉向使用者的一個重要轉捩點。Vendo 將打破產品僵化的模式，創造出一個尊重個別使用者工作方式的靈活生態系統。"
quiz:
  - question: "Vendo 的核心功能是什麼？"
    choices: ["讓使用者能直接修改軟體的原始程式碼", "讓使用者能直接在產品內建立所需的特定功能或應用程式", "能將開發者的工作效率提高兩倍"]
    answer: 1
    explanation: "Vendo 協助使用者無須仰賴開發者，即可在產品之上直接建構符合自身需求的功能或微型應用程式。"
  - question: "使用 Vendo 會修改到現有產品的原始程式碼嗎？"
    choices: ["是的，務必進行修改", "不會，它是以沙盒形式實作，不會更動原始程式碼", "僅修改部分核心功能"]
    answer: 1
    explanation: "Vendo 不會修改現有產品的原始程式碼，而是在沙盒（隔離環境）內產生與品牌風格自然融合的 UI。"
  - question: "透過 Vendo 產生的功能是如何運作的？"
    choices: ["在獨立的專用伺服器上運作", "透過產品 API 以使用者的權限進行運作", "所有功能都會在雲端強制更新"]
    answer: 1
    explanation: "產生的功能會透過該產品的 API，以當前登入使用者的權限直接運作，並根據使用者的工作流程進行個人化設定。"
lang: zh-tw
ref: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product
---

試想一下，當您盯著每天工作的軟體介面時，心裡想著：「啊，如果能直接在這裡按這個按鈕把檔案寄給我自己就好了。」然而，當您向開發團隊提出需求時，得到的回答總是：「好的，我們會評估看看。」或是：「功能積壓（backlog）太多了，今年恐怕沒辦法排程。」

最終，我們只能被迫調整自己的工作方式來適應軟體提供的功能，就像穿著一雙不合腳的鞋子走上一整天的路一樣。但如果使用者能親手在當下建立符合需求的功能，並直接掛載到系統上，那會是什麼樣子？最近，在矽谷 Y Combinator (YC) 支持下登場的 **Vendo**，正致力於解決這個問題。

## 為什麼這很重要？ (Why It Matters)

許多企業軟體 (B2B SaaS) 的使用者，總會感受到「自己需要的功能」與「產品實際提供的功能」之間的落差。每家企業的工作流程各異，但軟體往往只提供「平均化」的功能。

Vendo 打破了這種軟體的「僵化」。導入此技術的企業，其使用者無須開發者協助，即可親自建立符合自身工作需求的功能或小型應用程式（微型應用）。[出處: Vendo(YC S26) – Let your users build features on top of your product](https://www.ycombinator.com/companies/vendo)。結果就是，企業能從無止盡的功能開發需求清單（feature backlog）中解脫，而使用者也能完成屬於自己的工作流程 (Workflow)。[出處: YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii)。

## 輕鬆理解 (The Explainer)

我們可以這樣比喻：如果現有的軟體是一套「打造好的現成家具」，那麼 Vendo 就是一套可以讓您自由添購並組裝到家具上的「樂高積木組」。

簡單來說，Vendo 是植入於軟體內部的「嵌入式代理程式 (Embedded agent，指植入產品內部，能代表使用者進行作業的 AI)」。[出處: GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo)。

1. **連接**：Vendo 透過該產品提供的 API（軟體與外界溝通的通道），以類似於真實使用者操作的方式，安全地執行指令。[出處: Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)。
2. **建構**：當使用者提出功能需求時，Vendo 系統內部的客製化裝置會撰寫 React（用於建構使用者介面的 JavaScript 函式庫）元件。過程中會套用防止錯誤的準則（Guardrails）以確保安全執行呼叫。[出處: LaunchHN:Vendo(YC S26) –Letusersbuildfeaturesontopof...](https://news.ycombinator.com/item?id=49376038)。
3. **渲染**：這些產生的功能在不更動原軟體原始程式碼的前提下，在沙盒（與外部隔離的獨立安全空間）內自然地呈現在螢幕上，彷彿它們本來就是軟體的一部分。[出處: GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo)。

## 現狀 (Where We Stand)

目前 Vendo 以開源方式（任何人皆可查看程式碼並參與貢獻）提供。[出處: Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)。企業管理員只需透過 `npm install` 指令，即可在 60 秒內安裝到自己的軟體中。[出處: Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)。

Vendo 的共同創辦人尤塞夫 (Yousef) 強調，AI 代理程式正在根本性地改變大眾消費儀表板與使用者介面的方式，而其中的核心就是「個人化」。[出處: Show HN: Vendo (YC S26) – Let your users add their own ...](https://news.ycombinator.com/item?id=48926618)。目前，許多 B2B SaaS 企業正透過此解決方案，試圖逃離處理客戶個別功能需求所造成的「積壓地獄」。[出處: YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii)。

## 未來展望 (What's Next)

未來，我們所使用的幾乎所有工作工具，極大機率會從「成品」轉變為「素材」的形式。隨著像 Vendo 這類工具的普及，軟體開發企業將只需提供核心引擎，而由使用者在上方疊加自身工作方式的模式，將成為標準。

開發者無須再處理個別客戶瑣碎的需求，而是能專注於系統穩定性與核心功能的開發。一個我們所使用的應用程式，能如同樂高積木般彼此契合，且能記住我們個人工作風格的未來，正向我們走來。

## MindTickleBytes AI 記者視角

軟體定義權不再侷限於開發者手中，而是交還給最了解該軟體的使用者。Vendo 是一項大膽的嘗試，將隱藏在技術複雜性背後的「工具主權」歸還給使用者。現在，軟體不再是單方面詢問您是否能適應，而是轉化為您能將軟體進化至符合自身工作方式的自然過程。

## 參考資料

1. [Vendo: Let your users build their own features on top of your ...](https://www.ycombinator.com/companies/vendo)
2. [Vendo — YC S26 Launch on Hacker News - bestofshowhn.com](https://bestofshowhn.com/yc-s26/vendo)
3. [Show HN: Vendo (YC S26) – Let your users add their own ...](https://news.ycombinator.com/item?id=48926618)
4. [GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo)
5. [Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)
6. [Introducing Vendo: let your users edit your product - LinkedIn](https://www.linkedin.com/pulse/introducing-vendo-let-your-users-edit-product-ankit-gupta-0uu9c)
7. [Vendo lets users build custom features on top of your product ...](https://www.linkedin.com/posts/y-combinator_vendo-yc-s26-lets-your-users-build-their-activity-7485385624418439168-KuP2)
8. [LaunchHN:Vendo(YC S26) –Letusersbuildfeaturesontopof...](https://news.ycombinator.com/item?id=49376038)
9. [Vendo (YC S26) – Let your users add their lown features to ...](https://aiindigo.com/blog/vendo-yc-s26-let-your-users-add-their-lown-features-to-your-product-deep-dive-te)
10. [YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii)