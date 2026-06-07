---
layout: post
title: "開發者停止寫程式了？AI 在 5 個月內獨自編寫 100 萬行程式碼的秘密"
description: "OpenAI 的三名工程師在沒有親自編寫任何一行程式碼的情況下，完成了擁有 100 萬行程式碼的軟體。我們將探討這種名為「Harness Engineering」的新方式如何改變軟體開發。"
summary: "OpenAI 研究團隊公開了一項令人驚訝的實驗結果：他們不直接編寫程式碼，而是採用指揮 AI 的「Harness Engineering」方式，在 5 個月內完成了一套包含 100 萬行程式碼的軟體，全程無需人工輸入。"
tags: [OpenAI, Harness Engineering, AI 編碼, 人工智慧, ChatGPT]
image: 2026-06-07-Harness-engineering-Leveraging-Codex-in-an-agent-first-world.jpg
image_alt: "一名人類工程師像交響樂指揮家一樣，指揮多個機器人手臂編寫程式碼"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人類的角色正從「打字員」演變為「提供方向的導演」。這是一個完美的案例，說明了真正的創意在於提出正確的問題與設計，而非程式碼本身。"
quiz:
  - question: "在 OpenAI 的「Harness Engineering」實驗中，三名人類工程師在 5 個月內親自編寫了多少程式碼？"
    choices: ["約 10 萬行", "完全沒有任何一行", "約 50 萬行"]
    answer: 1
    explanation: "OpenAI 的三名工程師在 5 個月內沒有親自編寫任何一行程式碼，僅透過對 AI 下達指令，就完成了高達 100 萬行的軟體。"
  - question: "在此次實驗中，人類開發者的角色最接近下列哪一項？"
    choices: ["親自蓋房子的磚瓦工", "演出所有場景的演員", "指揮交響樂團的指揮家"]
    answer: 2
    explanation: "在 Harness Engineering 中，人類不再親自輸入程式碼，而是扮演指揮家（導演）的角色，負責指示並管理 AI 代理程式以確保其正確運作。"
  - question: "OpenAI 內部將 AI 自行修改程式碼並提升完成度的重複審查過程比喻為哪個角色？"
    choices: ["魔鬼終結者迴圈", "拉爾夫·維格姆迴圈", "鋼鐵人迴圈"]
    answer: 1
    explanation: "AI 代理程式自行編寫程式碼、經過自我審查並修正直到滿意為止的過程，取自著名動畫角色的名字，被稱為「拉爾夫·維格姆迴圈（Ralph Wiggum Loop）」。"
lang: zh-tw
ref: 2026-06-07-Harness-engineering-Leveraging-Codex-in-an-agent-first-world
---

想像一下，您想建造一座規模宏大且複雜的豪宅。在過去，您必須親自揮灑汗水，搬運磚塊、塗抹水泥，辛苦工作數月甚至數年。但現在，您面前有數十位不知疲倦、技術精湛的機器人建築師隨時待命。您只需說：「客廳要向南，牆紙要溫暖的米色。」機器人就會自動繪製藍圖、訂購材料、砌磚，建造出一座完美的房子。您只需悠閒地觀察建造過程，並適時調整方向，例如說：「把窗戶調大一點。」

在軟體開發的世界裡，這種如魔法般的場景已成為現實。那個我們必須在深夜對著電腦鍵盤敲敲打打，一針一線編織難懂的英文指令（程式碼）的時代正趨於結束，取而代之的是僅用言語指示 AI「製作這樣的程式」的時代。最近 OpenAI（ChatGPT 的開發公司）發表的一項驚人實驗結果，完美展示了未來軟體將如何誕生 [OpenAI's Agent-First Codebase Learnings | Blog](https://alexlavaee.me/blog/openai-agent-first-codebase-learnings/)。

## 為什麼這很重要？

這項技術的進步，與完全不懂寫程式的我們日常工作生活有什麼關係呢？簡單來說，這意味著我們每天使用的智慧型手機 App、銀行系統、有趣的遊戲等所有數位服務的「開發速度」與「開發成本」限制將完全消失。只要有想法，任何人都能量身打造夢想中的程式，這樣的世界已近在咫尺。

根據 OpenAI 技術人員 Ryan Lopopolo 撰寫的官方報告 [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.aibrief.in/article/harness-engineering-leveraging-codex-in-an-agent-first-world)，他們最近進行了一項為期 5 個月的驚人內部實驗。僅由 3 名人類工程師組成的團隊策劃並發布了一款新軟體，而這款程式的總規模竟高達 100 萬行（電腦語言書寫的行數） [HarnessEngineering: Why 2026's AI Edge Isn't a Bigger Model](https://thebytedive.com/ai/260411-harness-engineering-ai-edge-2026/)。100 萬行程式碼的規模，足以填滿數十本厚重的百科全書，規模龐大到足以流暢運行一般大企業的核心服務。

而真正令人震驚的事實是，在這 100 萬行程式碼中，人類親手輸入的程式碼竟然連一行都沒有 [Harness Engineering: Why the Focus is Shifting from... | Epsilla Blog](https://www.epsilla.com/blogs/2026-03-12-harness-engineering)。不只是 App 的核心運行邏輯，連捕捉錯誤的測試程式、使用說明書，甚至是監視程式運行狀態的工具，百分之百都由 AI 代理程式（Agent，能代表人類自主執行特定任務的人工智慧）獨立完成 [OpenAI's Agent-First Codebase Learnings | Blog](https://alexlavaee.me/blog/openai-agent-first-codebase-learnings/)。

最終，這 3 名人類工程師在 AI 的協助下處理了高達 1,500 次的程式碼審核（Pull Request，將編寫好的程式碼更新至最終系統的批准過程） [HarnessEngineering:LeveragingCodexinanAgent-FirstWorld](https://oss.vstorm.co/blog/harness-engineering-leveraging-codex-agent-first/)。換算下來，平均每位人類開發者每天完成了 3.5 個重大功能更新，這展現了驚人的生產力 [HarnessEngineering: Why 2026's AI Edge Isn't a Bigger Model](https://thebytedive.com/ai/260411-harness-engineering-ai-edge-2026/)。現在，軟體開發的最大瓶頸不再是「人類手指在鍵盤上敲得有多快」，而是「人類如何睿智地指揮自主型 AI」，遊戲規則已發生了根本性的轉變 [HarnessEngineering: The New Job Description of... | Medium](https://medium.com/@naveenmanwani/harness-engineering-the-new-job-description-of-a-software-engineer-in-an-agent-first-world-9a5a087fab78)。

## 輕鬆理解

人類如何能在不碰鍵盤的情況下完成如此驚人的壯舉？答案隱藏在 OpenAI 重新定義的新概念——**「Harness Engineering」**之中。

HashiCorp 的創辦人 Mitchell Hashimoto 在 2026 年初經歷此現象時曾表示：「雖然不知道業界是否有通用術語，但我將這種方式稱為『Harness Engineering』」 [HarnessEngineering: From AI-Assisted to... - DEV Community](https://dev.to/seekdb/harness-engineering-from-ai-assisted-to-ai-driven-what-is-software-engineering-undergoing-l6n)。

「Harness（韁繩/背帶）」原指將馬或狗連接到馬車上的結實韁繩，或是攀岩及乘坐驚險遊樂設施時保護人身安全的保險帶。在 AI 世界中，Harness Engineering 是指設計一套穩固的「運行環境與架構約束」，以確保具備強大能力的 AI 編碼代理程式不會寫出錯誤程式碼或在過程中迷失方向，使其能安全且高效地工作 [HarnessEngineering: The Complete Guide to Building... | ZBuild](https://www.zbuild.io/resources/news/harness-engineering-complete-guide-ai-agent-codex-2026), [What IsHarnessEngineeringfor AIAgents? | Milvus - Milvus Blog](https://milvus.io/blog/harness-engineering-ai-agents.md)。

打個比方：有一匹力大無窮且聰明、但還不懂人類道路規則的賽馬（AI）。如果要騎這匹馬安全地將重物運送到目的地，就必須備好堅固的馬鞍與精確操控的韁繩（Harness）。Harness 工程師就是那個精確設計並緊握這條韁繩的人。他在百分之百發揮馬匹驚人速度與力量（AI 編解碼能力）的同時，也扮演著設置圍欄與安全網的角色，防止馬匹跳下懸崖或誤入歧途。

OpenAI 專案的開始也完全由 AI 主導。2025 年 8 月底，為這個龐大專案動下第一鏟的並非人類，而是基於 GPT-5 的 Codex（專精於程式設計的 AI）工具 [Harnessengineering:leveragingCodexinanagent-firstworld](https://openai.com/index/harness-engineering/)。專案的初期設定，例如如何分配無數檔案、制定程式碼規範等「蓋房子的基礎工程」，都是 AI 參考既有的優質模板自動建立的 [Harnessengineering:leveragingCodexinanagent-firstworld](https://openai.com/index/harness-engineering/)。

## 目前現狀

那麼，這 3 名人類工程師在 5 個月間每天都在做什麼呢？他們並非對著黑色顯示螢幕為那些像外星語般的程式碼傷透腦筋，而是像建築工地的總監工一樣，與 AI 進行不間斷的對話。

工作流程如下：人類工程師撰寫提示詞（Prompt，向 AI 下達的日常語言指令），例如：「我需要購物車結帳功能，請特別注意安全性。」AI 代理程式便會瞬間編寫好程式碼。接著，就像人類員工向主管提交結報文件一樣，AI 會自動整理並提交一份精美的「修改請求（Pull Request）」文件 [Harness engineering: leveraging Codex in an agent-first world | OpenAI](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html)。

最有趣的部分在於下一步：人類不需要像拿著放大鏡一樣逐一檢查 AI 編寫的海量程式碼。AI 會在自己的虛擬電腦環境中，先對自己寫好的程式碼進行嚴謹的自我檢查（Local Review）。甚至還會向連接到雲端網路的其他 AI 代理程式同事請求額外審查，並說：「能幫我嚴格評價一下這段程式碼嗎？」 [Harness engineering: leveraging Codex in an agent-first world | OpenAI](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html)

這就像是一群能力出眾的實務人員在進行激烈的討論。收到其他 AI 尖銳的反饋後，AI 會以此為基礎再次修改程式碼並重新接受檢查。這個過程會不斷重複，直到所有 AI 審核員都喊出「合格」並滿意為止。OpenAI 團隊以美國動畫《辛普森家庭》中一個古怪角色的名字，趣味地將這個頑強的自我修正迴圈稱為「拉爾夫·維格姆迴圈（Ralph Wiggum Loop）」 [Harness engineering: leveraging Codex in an agent-first world | OpenAI](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html)。

當然，目前仍存在明顯的局限。雖然 AI 在創建短小且明確的特定功能方面，其速度與準確度已遠超人類，但要讓 AI 一次性完美「理解」極其龐大且陳舊的複雜系統，仍然面具挑戰 [r/programming on Reddit: Harness engineering: leveraging Codex in an agent-first world](https://www.reddit.com/r/programming/comments/1r3kjqt/harness_engineering_leveraging_codex_in_an/)。也就是說，雖然出現了不知疲倦、反應迅速且聰明的實務操作者，但觀察整個森林、繪製系統大圖的洞察力，目前仍是人類監工的專屬職責。

## 未來會如何發展？

OpenAI 堂堂公開的這份 100 萬行實驗報告，不僅僅是天才開發者們的英勇故事，更為未來所有職場人士的工作方式提供了一份完美的藍圖（Blueprint） [OpenAI’sHarnessEngineeringPost Is a Blueprint for theAgent-First...](https://medium.com/@AdithyaGiridharan/openais-harness-engineering-post-is-a-blueprint-for-the-agent-first-era-d9932851dcee)。許多 IT 專家現在強調，在即將到來的時代，企業真正的技術競爭力不在於「購買多大、多昂貴的 AI 模型」，而是在於「能精細地構建多完善的 Harness（安全裝置及工作環境），讓這些聰明的 AI 在不亂來的情況下盡情發揮」 [4 Real Cases |HarnessEngineeringis... - Alibaba Cloud Community](https://www.alibabacloud.com/blog/4-real-cases-|-harness-engineering-is-becoming-the-new-moat_602970)。

順應這一潮流，OpenAI 最近正式公開了「Symphony（交響樂）」的工程預覽版，這是一個能在企業規模下同時管理並指揮無數 AI 編碼代理程式的工具 [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.linkedin.com/posts/davethackeray_harness-engineering-leveraging-codex-in-activity-7436346067559829504-Zz-r)。有趣的是，這套強大的指揮系統是用專門用於無延遲控制大規模通信網路的 Elixir 特殊語言編寫的，從最初策劃階段就深度融入了 Harness Engineering 的哲學 [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.linkedin.com/posts/davethackeray_harness-engineering-leveraging-codex-in-activity-7436346067559829504-Zz-r)。

正如過去從僅由 0 和 1 組成的生硬組合語言（Assembly language）轉換到像人類日常語言一樣簡單的 Python 經歷了很長時間一樣，這場巨大的變革不會在一夜之間讓全球所有程式設計師失業 [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.linkedin.com/posts/sachinkundu_harness-engineering-leveraging-codex-in-activity-7450785591908179968-4boT)。

然而，有一點是顯而易見的：未來的軟體開發者不應只是死記硬背電腦語法並盲目敲擊鍵盤的人。他們必須成為「頂尖的交響樂團指揮家」，指引數十、數百名不間斷產出程式碼的 AI 團員不再發出不和諧音，進而共同完成優美的和弦。

---

**MindTickleBytes AI 的視角**

即使不懂複雜的建築力學或數學公式，只要具備卓越的想像力與優秀的機器人建築師，任何人都能隨心所欲建造出精美建築的時代已經開啟。程式設計也是如此。背誦刁鑽的電腦語法現在已成為機器的職責，人類的角色已從「打字員」完全演變為「指引方向的導演」。

現在，熬夜抓蟲（Bug，程式錯誤）或像機器一樣追求打字速度，已不再具備競爭力。相反地，在 AI 每秒噴湧而出的海量成果中辨識出對我們真正有價值的內容、敏銳地洞察系統漏洞，並向 AI 提出更具創意性的「問題」，這才是留給人類最重要且最具挑戰性的功課。程式設計教育的範式也必須迫切地從「如何寫程式」轉向「要創造什麼以及要解決什麼問題」。真正的創意並非始於指尖的敲擊，而是源於人類頭腦中正確的設計，OpenAI 的這次實驗已完美證明了這一點。

## 參考資料
1. [Harnessengineering:leveragingCodexinanagent-firstworld](https://openai.com/index/harness-engineering/)
2. [Harness Engineering: Why the Focus is Shifting from... | Epsilla Blog](https://www.epsilla.com/blogs/2026-03-12-harness-engineering)
3. [HarnessEngineering:LeveragingCodexinanAgent-FirstWorld](https://oss.vstorm.co/blog/harness-engineering-leveraging-codex-agent-first/)
4. [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.linkedin.com/posts/davethackeray_harness-engineering-leveraging-codex-in-activity-7436346067559829504-Zz-r)
5. [OpenAI’sHarnessEngineeringPost Is a Blueprint for theAgent-First...](https://medium.com/@AdithyaGiridharan/openais-harness-engineering-post-is-a-blueprint-for-the-agent-first-era-d9932851dcee)
6. [HarnessEngineering: The Complete Guide to Building... | ZBuild](https://www.zbuild.io/resources/news/harness-engineering-complete-guide-ai-agent-codex-2026)
7. [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.aibrief.in/article/harness-engineering-leveraging-codex-in-an-agent-first-world)
8. [Harness engineering: leveraging Codex in an agent-first world | OpenAI](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html)
9. [GitHub - walkinglabs/awesome-harness-engineering: 🛠️ Awesome tools & guides for harness engineering.](https://github.com/walkinglabs/awesome-harness-engineering)
10. [Harness engineering: leveraging Codex in an agent-first world | daily.dev](https://app.daily.dev/posts/harness-engineering-leveraging-codex-in-an-agent-first-world-py6m8jwm4)
11. [OpenAI's Agent-First Codebase Learnings | Blog](https://alexlavaee.me/blog/openai-agent-first-codebase-learnings/)
12. [r/programming on Reddit: Harness engineering: leveraging Codex in an agent-first world](https://www.reddit.com/r/programming/comments/1r3kjqt/harness_engineering_leveraging_codex_in_an/)
13. [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.linkedin.com/posts/sachinkundu_harness-engineering-leveraging-codex-in-activity-7450785591908179968-4boT)
14. [HarnessEngineering: Why 2026's AI Edge Isn't a Bigger Model](https://thebytedive.com/ai/260411-harness-engineering-ai-edge-2026/)
15. [HarnessEngineering: The New Job Description of... | Medium](https://medium.com/@naveenmanwani/harness-engineering-the-new-job-description-of-a-software-engineer-in-an-agent-first-world-9a5a087fab78)
16. [4 Real Cases |HarnessEngineeringis... - Alibaba Cloud Community](https://www.alibabacloud.com/blog/4-real-cases-|-harness-engineering-is-becoming-the-new-moat_602970)
17. [HarnessEngineering: From AI-Assisted to... - DEV Community](https://dev.to/seekdb/harness-engineering-from-ai-assisted-to-ai-driven-what-is-software-engineering-undergoing-l6n)
18. [What IsHarnessEngineeringfor AIAgents? | Milvus - Milvus Blog](https://milvus.io/blog/harness-engineering-ai-agents.md)