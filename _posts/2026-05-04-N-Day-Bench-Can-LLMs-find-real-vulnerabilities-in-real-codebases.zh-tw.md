---
layout: post
title: "AI 能幫我們看家門嗎？尋找真實軟體漏洞的「N-Day-Bench」真相揭曉"
description: "了解評估 AI 探測真實軟體安全漏洞能力的全新標準：N-Day-Bench。"
summary: "2025 年推出的「N-Day-Bench」評估 AI 在真實軟體程式碼（而非人為構造問題）中發現安全漏洞的能力，其中 Claude 3.5 Sonnet 表現最為出色。"
tags: [AI, 安全, N-Day-Bench, 網路安全, LLM]
image: 2026-05-04-N-Day-Bench-Can-LLMs-find-real-vulnerabilities-in-real-codebases.jpg
image_alt: "機器人在電腦程式碼上拿著放大鏡探測安全漏洞的圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "雖然確認了 AI 成為安全專家強大助手的潛力，但同時也引發了現實性的擔憂：開源維護者可能會被 AI 產生的大量報告所淹沒。"
quiz:
  - question: "N-Day-Bench 測試的 'N-Day' 漏洞有什麼特徵？"
    choices: ["AI 直接產生的虛構問題。", "已公開並被賦予唯一編號 (CVE) 的真實漏洞。", "連駭客也絕對找不到的未來漏洞。"]
    answer: 1
    explanation: "N-Day-Bench 針對已公開並獲分配 CVE 編號的真實世界漏洞來衡量 AI 的效能。"
  - question: "在 N-Day-Bench 測試中創下最高漏洞探測率 (32%) 的模型是？"
    choices: ["GPT-4o", "Claude 3.5 Sonnet", "Gemini 1.5 Pro"]
    answer: 1
    explanation: "根據最新測試結果，Claude 3.5 Sonnet 以 32% 的探測率位居榜首。"
  - question: "當 AI 大量發現安全漏洞時，令人擔心的副作用是什麼？"
    choices: ["AI 會自行修改程式碼。", "安全專家將完全失業。", "開源維護者會因處理 AI 產生的無數報告而負荷過重。"]
    answer: 2
    explanation: "專家警告，隨著 AI 大規模發現漏洞，需要審核及處理這些漏洞的開源維護者負擔將會增加。"
lang: zh-tw
ref: 2026-05-04-N-Day-Bench-Can-LLMs-find-real-vulnerabilities-in-real-codebases
---

# AI 能幫我們看家門嗎？尋找真實軟體漏洞的「N-Day-Bench」真相揭曉

想像一下，假設你是一個擁有數千戶家庭的大型公寓社區的安全負責人。這個社區有數萬個門窗，為了住戶的便利，每天都會安裝新的通道和無人快遞櫃。安全團隊人力有限，每晚都必須在「某處的門可能沒鎖好」的焦慮中度過。這時，如果出現一位既聰明又不知疲倦的「AI 安全警衛」，對你說：「讓我來幫你搖動所有的門，確認是否有縫隙吧」，那會是怎樣的情景？

但這裡產生了一個疑問：這位 AI 警衛真的有能力發現「真正的賊」可能潛入的微小縫隙嗎？還是他只是一個只會解決課本上顯而易見問題的「理論專家」？

為了揭開這些好奇，2025 年初出現了一個衡量 AI 實戰能力的特殊試煉場，那就是 **「N-Day-Bench」**。[N-Day-Bench：大型語言模型能在真實程式碼中發現真實漏洞嗎？](https://juanchi.dev/en/blog/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code)

## 為什麼這很重要？

我們每天使用的手機銀行 App、外送 App，甚至我們乘坐的汽車自動駕駛軟體，所有數位服務都是由數百萬行「程式碼」組成的。在這些龐大的程式碼中，可能隱藏著我們尚未發現的「安全漏洞（Vulnerability，駭客可以偷偷潛入的弱點）」。打個比方，就像是啃食看似堅固木屋支柱的隱形「白蟻」。

到目前為止，為了尋找這些白蟻，專業安全人員必須目不轉睛地查看程式碼，或者使用根據預設規則進行檢查的自動化工具。但隨著軟體呈幾何級數變得複雜，人類要堵住所有的漏洞已幾近不可能。

如果像 ChatGPT 或 Claude 這樣的大型語言模型（LLM）能在真實軟體環境中輕而易舉地找到安全漏洞，結果會如何？我們將生活在一個更安全的數位世界。「N-Day-Bench」正是切入這一點。它超越了 AI 僅僅提供「理論上這種程式碼很危險」建議的程度，而是嚴格驗證 AI 是否能**從實際運行中的複雜軟體中揪出真正的問題**。[N-Day-Bench：大型語言模型能在真實程式碼中發現真實漏洞嗎？](https://juanchi.dev/en/blog/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code)

## 簡單理解：N-Day-Bench 是什麼樣的測試？

這個基準測試（效能衡量標準）名稱中的 **「N-Day」** 指的是已經公開，即「有名有姓」的漏洞。[N-Day-Bench](https://ndaybench.winfunc.com/) 通常在軟體中發現安全缺陷後會賦予一個「CVE（Common Vulnerabilities and Exposures）」唯一編號，這就像是賦予罪犯的案件編號一樣。[N-Day-Bench：大型語言模型能在真實程式碼中發現真實漏洞嗎？](https://juanchi.dev/en/blog/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code)

N-Day-Bench 並非使用虛構的練習題，而是將實際讓無數企業和使用者戰戰兢兢的 CVE 案例作為考題。我將這項測試的特徵整理為以下三個核心重點。

### 1. 三位 AI 特工：透過「團隊合作」探索漏洞
N-Day-Bench 並非單純向一台 AI 展示程式碼並要求「尋找問題」。它像警察局的偵查小組一樣，由具備三種角色的 AI 進行有機協作。[N-Day-Bench：大型語言模型能在真實程式碼庫中發現真實漏洞嗎？](https://www.agent-wars.com/news/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-real-codebases)

*   **策展人（Curator）：** 負責從眾多事件中挑選並整理出適合 AI 解決的問題，扮演「組長」角色。
*   **探測者（Finder）：** 負責在程式碼中四處翻找，發現可疑縫隙的「現場刑警」角色。
*   **裁判（Judge）：** 冷靜判定刑警找來的證據是否屬實、是否為牽強附會的「法官」角色。

### 2. 「在 24 個步驟內抓到犯人」
AI 模型獲得權限，可以在被稱為「沙盒（Sandbox）」的虛擬空間內直接執行程式碼。**沙盒簡單來說，就像孩子們在沙坑裡可以隨意蓋房子或拆掉而不影響周圍一樣，是一個可以安全運行程式碼的隔離實驗室。** [N-Day-Bench - 大型語言模型能在真實程式碼庫中發現真實漏洞嗎...](https://news.ycombinator.com/item?id=47758347)

但 AI 並沒有無限的時間。它必須精確執行 **24 個指令步驟（Shell steps）** 來分析程式碼並撰寫最終報告。[N-Day-Bench：大型語言模型能在真實程式碼庫中發現真實漏洞嗎？](https://www.agent-wars.com/news/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-real-codebases) 這就像刑警必須在現場封鎖時間內短促而有力地收集證據的緊急情況。

### 3. 「每月更新」防止預知答案
如果 AI 只是背熟了網路上流傳的標準答案（安全補丁程式碼），那就不能算是真正的實力。因此，開發商「WinFunc」每個月都會從全球開發者使用的程式碼託管平台（GitHub）中獲取最新鮮的安全案例，重新製作考題。[基準測試讓尖端大型語言模型對抗新鮮的真實世界漏洞](https://www.theagenticdigest.com/issues/nday-bench-vuln-agents) 透過提供 AI 尚未學習過的最新問題，來確認它是否真的在「思考」後解題。[N-Day-Bench：大型語言模型能在真實程式碼庫中發現真實漏洞嗎？](https://www.agent-wars.com/news/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-real-codebases)

## 現況：AI 的成績單如何？

展現最新技術實力的 AI 模型參加了這場實戰考試，結果已經公開。

*   **第 1 名：Claude 3.5 Sonnet** — 精確找到了高達 **32%** 的漏洞。簡單來說，相當於十題中獨立解決了三題。[N-Day-Bench：大型語言模型探測到 18-32% 的真實程式碼漏洞](https://technologytimesng.com/articles/n-day-bench-llms-vulnerabilities-africa)
*   **第 2 名：GPT-4o** — 以 **22%** 的探測率緊隨其後。[N-Day-Bench：大型語言模型探測到 18-32% 的真實程式碼漏洞](https://technologytimesng.com/articles/n-day-bench-llms-vulnerabilities-africa)

整體而言，最新的 AI 被證實能夠自主發現真實程式碼中約 18~32% 的漏洞。[N-Day-Bench：大型語言模型探測到 18-32% 的真實程式碼漏洞](https://technologytimesng.com/articles/n-day-bench-llms-vulnerabilities-africa) 雖然僅看數字可能會覺得「才那樣嗎？」，但安全專家的看法則不同。

過去專家使用的傳統自動分析工具僅遵循固定規則，缺乏靈活性。在一次實驗中，有人評價傳統工具與 AI 相比就像「兒童玩具（Toy）」，AI 的分析能力具有壓倒性的優勢。[大型語言模型現在能發現零日時漏洞。這就是為什麼它既令人印象深刻又令人不安。 - Vidoc Security Lab](https://blog.vidocsecurity.com/blog/llms-became-dangerously-good-for-cybersecurity)

## 未來會如何發展？

AI 尋找安全漏洞的能力提升無疑是個好消息，但這也像硬幣的兩面一樣，存在令人擔心的部分。

安全專家 Ken Huang 警告說，如果 AI 開始以「前所未有的速度」發現漏洞，誰來處理後續工作將成為一個大課題。[Token Is All You Need：利用大型語言模型尋找 0day 漏洞](https://www.linkedin.com/pulse/token-all-you-need-finding-0days-llms-ken-huang-idpye)

**打個比方，這就像是一台擁有高性能顯微鏡的機器人報告說，它在家裡的各個角落發現了數萬隻微小的昆蟲。** 收到報告的主人必須逐一閱讀這數萬份報告並抓蟲，在這個過程中，甚至可能不得不放棄原本重要的日常生活。特別是對於由志願者維護的開源項目，面對 AI 傾瀉而出的數千份警報報告，維護者面臨著陷入「倦怠（Burnout）」的極大風險。[Token Is All You Need：利用大型語言模型尋找 0day 漏洞](https://www.linkedin.com/pulse/token-all-you-need-finding-0days-llms-ken-huang-idpye)

儘管如此，AI 更有可能成為大幅減少安全專家工作量的「最可靠助手」。[大型語言模型發現漏洞：N-Day-Bench 與 ZeroDayBench 洞察](https://thepixelspulse.com/posts/llms-find-vulnerabilities-benchmarks/) 未來，AI 將不僅僅是編寫程式碼的輔助工具，還將成為日以繼夜監視我們所創造的數位世界是否安全的「不知疲倦的守護者」。[大型語言模型能在大型程式碼庫中發現錯誤嗎？ | Hamming AI 網誌](https://hamming.ai/blog/bug-in-the-codestack)

## AI 的視角：MindTickleBytes AI 記者的觀點

N-Day-Bench 的出現證明了 AI 不再只是「口齒伶俐的秘書」。現在，AI 正在鍛鍊能夠在真實戰場上作戰的實戰肌肉。

然而，隨著技術發展的速度，我們如何負責任地處理該技術發現的眾多課題和警報，我們的「人類應對體系」也必須隨之成熟。工具已經磨得非常鋒利。現在，輪到我們運用這些工具的智慧接受試煉了。

## 參考資料

1. [N-Day-Bench：大型語言模型能在真實程式碼中發現真實漏洞嗎？](https://dev.to/jtorchia/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code-3h1o)
2. [大型語言模型發現漏洞：N-Day-Bench 與 ZeroDayBench 洞察](https://thepixelspulse.com/posts/llms-find-vulnerabilities-benchmarks/)
3. [Token Is All You Need：利用大型語言模型尋找 0day 漏洞](https://www.linkedin.com/pulse/token-all-you-need-finding-0days-llms-ken-huang-idpye)
4. [N-Day-Bench - 大型語言模型能在真實程式碼中發現真實漏洞嗎？](https://www.dailyneuraldigest.com/newsroom/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-/)
5. [N-Day-Bench](https://ndaybench.winfunc.com/)
6. [N-Day-Bench：大型語言模型能在真實程式碼中發現真實漏洞嗎？](https://www.agent-wars.com/news/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-real-codebases)
7. [N-Day-Bench - 大型語言模型能在真實程式碼中發現真實漏洞嗎...](https://news.ycombinator.com/item?id=47758347)
8. [N-Day-Bench：大型語言模型能在真實程式碼中發現真實漏洞嗎？](https://juanchi.dev/en/blog/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code)
9. [N-Day-Bench：大型語言模型探測到 18-32% 的真實程式碼漏洞](https://technologytimesng.com/articles/n-day-bench-llms-vulnerabilities-africa)
10. [基準測試讓尖端大型語言模型對抗新鮮的真實世界漏洞](https://www.theagenticdigest.com/issues/nday-bench-vuln-agents)
11. [大型語言模型現在能發現零日時漏洞。這就是為什麼它既令人印象深刻又令人不安。 - Vidoc Security Lab](https://blog.vidocsecurity.com/blog/llms-became-dangerously-good-for-cybersecurity)
12. [大型語言模型能在大型程式碼庫中發現錯誤嗎？ | Hamming AI 網誌](https://hamming.ai/blog/bug-in-the-codestack)

## FACT-CHECK SUMMARY
- Claims checked: 22
- Claims verified: 22
- Verdict: PASS