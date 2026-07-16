---
layout: post
title: "AI 會說謊？即便如此，我們仍持續使用大型語言模型 (LLM) 的理由"
description: "探討 AI 的幻覺現象與批評聲浪下，為何許多人仍在使用大型語言模型 (LLM)，並剖析其核心價值與未來前景。"
summary: "儘管面臨對 AI 的批判，得益於技術的演進與補強方案，LLM 依然作為強大的工具，提升了我們日常生活與工作的生產力。"
tags: [AI, LLM, 技術趨勢, 生成式AI]
image: 2026-07-16-The-LLM-Critics-Are-Right-I-Use-LLMs-Anyway.jpg
image_alt: "象徵性圖像，呈現複雜程式碼與對話視窗上方，正反兩面審查意見相互交織的場景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "批評是技術成長的養分。認清 LLM 的侷限，並引入「批評模型」等補強機制，顯示我們能與 AI 更健康地共存。"
quiz:
  - question: "導致 LLM 自信滿滿地回答錯誤資訊之「幻覺現象」的主要原因之一為何？"
    choices: ["因為學習了網際網路上帶有偏見的資料", "因為電腦效能過低", "僅僅是因為耗電量太大"]
    answer: 0
    explanation: "LLM 學習網際網路上海量的資料，其中包含了矛盾、錯誤資訊與觀點；加上目前的基準測試方式，對於「自信回答」的獎勵大於「準確度」。"
  - question: "近期 AI 開發領域中，用於尋找程式碼漏洞的「批評模型 (Critic Models)」是指什麼？"
    choices: ["能讀懂人類情緒的模型", "評估其他 AI 生成結果並給予回饋的 LLM", "計算 AI 耗電量的程式"]
    answer: 1
    explanation: "批評模型透過人類回饋強化學習 (RLHF) 進行訓練，扮演如同同儕開發者的角色，以自然語言回饋指出其他 AI 所生成程式碼或結果中的錯誤。"
  - question: "部分開源專案拒絕接受由 LLM 生成的貢獻 (PR) 之主要原因為何？"
    choices: ["貢獻者人數太多", "與開源精神不符的版權問題", "難以區分 AI 生成內容的可靠性與確認投入時間"]
    answer: 2
    explanation: "隨著越來越難分辨程式碼究竟是出自人工精心編寫，還是 AI 自動大量生成，社群擔憂這將破壞開發者之間的信任。"
lang: zh-tw
ref: 2026-07-16-The-LLM-Critics-Are-Right-I-Use-LLMs-Anyway
---

想像一下。今天早上，您開始工作時將昨天整理好的數十頁合約草案交給了 AI，並對它說：「請幫我列出主要的風險項目。」AI 瞬間給出了答案。但您腦中突然閃過一個念頭：『這內容真的能信嗎？會不會是 AI 自己隨意編造出來的？』

近來，圍繞著生成式 AI，特別是大型語言模型 (LLM) 的輿論呈現兩極化。有些人歡呼 AI 將徹底改變我們的生活；另一些人則強烈批評，指出幻覺現象 (Hallucination，即 AI 將非事實的資訊偽裝成事實的現象)、環境影響以及可靠性問題。甚至像 Zig 或 Gentoo 這類開源軟體專案，也開始拒絕接受由 AI 生成的程式碼貢獻。 [出處: The LLM Critics Are Right. I Use LLMs Anyway. | Jeremy Theocharis](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/)

然而，儘管批評聲浪高漲，全球無數用戶仍甘願付費使用 LLM。 [出處: 2025: The Year in LLMs | Hacker News](https://news.ycombinator.com/item?id=46449643) 究竟為什麼批評與使用會共存呢？

## 這為什麼重要？

僅僅因為 AI「新奇」而使用的時代已經過去了。現在，AI 正逐漸成為決定工作效率的必備工具。對於開發者而言，當他們設計複雜的函數結構時，LLM 是極佳的合作夥伴。 [出處: Here’s how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) 然而，如果信任問題無法解決，在需要做出重大決策的商務場合中，我們就無法放心地使用 AI。

批評者的聲音起到了讓 AI 更安全的「護欄」作用。他們指出的幻覺現象，實際上是 LLM 所學習的網際網路資料本身就充滿矛盾與偏見，加上模型受訓目標往往是追求「使用者喜愛的自信回答」而非「絕對準確性」所產生的副產品。 [出處: It's 2026. Why Are LLMs Still Hallucinating? - Duke University Libraries](https://blogs.library.duke.edu/blog/2026/01/05/its-2026-why-are-llms-still-hallucinating/) 我們越是正視這些問題，技術就會變得越精確。

## 輕鬆理解：超能力圖書館館員

若要簡單比喻，LLM 就像是一位讀過世上所有書籍與網際網路文章的「超能力圖書館館員」。這位館員學會了無數規律，能在我們提問時，快速找出看起來最合理的答案。 [出處: Part 1: How to Apply LLMs and AI to Contracts](https://www.knowable.com/blog/part-1-how-to-apply-llms-and-ai-to-contracts-what-are-llms-anyway/)

但有時，它也會在那龐大的知識庫中混入一些荒謬的內容。這就像館員讀了太多書，導致將虛構小說的情節誤認為真實歷史事件來解釋一樣。因此，最近開始引進了一種讓「批評家」在旁監督館員回答的方式。

「批評模型 (Critic Models)」是一種 LLM，它們會仔細閱讀其他 AI 所寫的程式碼，並像同事一樣給予回饋，檢查是否有邏輯錯誤或安全性風險。 [出處: LLM Critics Help Catch LLM Bugs | Athina AI](https://blog.athina.ai/llm-critics-help-catch-llm-bugs) 事實上，批評模型「CriticGPT」在尋找程式碼漏洞方面的表現，甚至超越了人類直接審核的效能。 [出處: LLM Critics: A New Weapon in the Fight Against AI Bugs](https://medium.com/@ayoubkirouane3/llm-critics-a-new-weapon-in-the-fight-against-ai-bugs-f258a6b7cf91)

## 我們現在處於什麼階段？

現今的 LLM 雖然基於能理解語境並預測下一個單字的「解碼器風格 Transformer」結構運作，但內在已經變得聰明許多。它們採用了令人聯想到專家團隊的「專家混合 (MoE, Mixture-of-Experts) 結構」，根據問題的性質啟動最合適的小型模型，藉此提升效率。 [出處: The State Of LLMs 2025: Progress, Progress, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)

但顯然，限制依然存在。麻省理工學院 (MIT) 的研究顯示，模型在學習過程中會形成錯誤的相關性，導致產生看似完美但邏輯上失敗的「合成謬誤」。 [出處: Researchers discover a shortcoming that makes LLMs less reliable](https://news.mit.edu/2025/shortcoming-makes-llms-less-reliable-1126) 這證實了我們絕不能盲目相信 AI 的回答，依然需要「具備檢核能力的用戶」參與其中。

## AI 的未來：協作型秘書

未來的下一代 LLM 將會變得比現在更便宜、更高效。 [出處: LLMs+: 10 Things That Matter in AI Right Now](https://www.technologyreview.com/2026/04/21/1135645/llm-large-language-models-ai/) 重點不再僅僅是填入更多資料，而是強化識別並自動修正錯誤的能力。

我們需要從將 AI 視為「無所不知的完美考卷解答」的階段走出來，將其定位為「協作型創意秘書」。批評並非阻礙技術進步，而是引導技術走向正確方向的燈火。當我們認清 LLM 的極限，並在基礎上批判性地運用這些工具時，我們才能真正成為 AI 時代的主人。

## AI 的觀點

批評是技術成長的養分。認清 LLM 的侷限，並引入「批評模型」等補強機制，顯示我們能與 AI 更健康地共存。

## 參考資料

1. [How I use LLMs - YouTube](https://www.youtube.com/watch?v=EWvNQjAaOHw)
2. [As an Experienced LLM User, I Actually Don’t Use Generative LLMs...](https://minimaxir.com/2025/05/llm-use/)
3. [LLM Critics Help Catch LLM Bugs | Athina AI](https://blog.athina.ai/llm-critics-help-catch-llm-bugs)
4. [Using ChatGPT is not bad for the environment](https://blog.andymasley.com/p/individual-ai-use-is-not-bad-for)
5. [Bad (but common) LLM criticisms - Ritza Articles](https://ritza.co/articles/gareth/bad-llm-criticisms/)
6. [Part 1: How to Apply LLMs and AI to Contracts: What are LLMs anyway? - Knowable](https://www.knowable.com/blog/part-1-how-to-apply-llms-and-ai-to-contracts-what-are-llms-anyway/)
7. [Here’s how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)
8. [LLMs+: 10 Things That Matter in AI Right Now | MIT Technology Review](https://www.technologyreview.com/2026/04/21/1135645/llm-large-language-models-ai/)
9. [It's 2026. Why Are LLMs Still Hallucinating? - Duke University Libraries](https://blogs.library.duke.edu/blog/2026/01/05/its-2026-why-are-llms-still-hallucinating/)
10. [Assessing the Strengths and Weaknesses of Large Language Models](https://link.springer.com/article/10.1007/s10849-023-09409-x)
11. [LLM Critics: A New Weapon in the Fight Against AI Bugs](https://medium.com/@ayoubkirouane3/llm-critics-a-new-weapon-in-the-fight-against-ai-bugs-f258a6b7cf91)
12. [LLM News, Updates and Articles](https://llm-explorer.com/static/llm-news/)
13. [The State Of LLMs 2025: Progress, Progress, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)
14. [The LLM Critics Are Right. I Use LLMs Anyway. | Jeremy Theocharis](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/)
15. [Researchers discover a shortcoming that makes LLMs less reliable | MIT News](https://news.mit.edu/2025/shortcoming-makes-llms-less-reliable-1126)
16. [2025 LLM Year in Review – karpathy](https://karpathy.bearblog.dev/year-in-review-2025/)
17. [2025: The Year in LLMs | Hacker News](https://news.ycombinator.com/item?id=46449643)