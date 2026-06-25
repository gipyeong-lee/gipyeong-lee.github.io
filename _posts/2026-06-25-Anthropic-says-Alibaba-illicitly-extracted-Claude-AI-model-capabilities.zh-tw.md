---
layout: post
title: "我的AI被複製了嗎？『Claude』捲入大規模技術竊取事件"
description: "Anthropic 指控包括阿里巴巴在內的中國企業未經許可擅自複製（蒸餾）旗下 AI 模型 Claude 的智慧，本文將帶您輕鬆了解此次事件。"
summary: "AI 公司 Anthropic 指控包括阿里巴巴在內的中國 AI 企業不當竊取其模型「Claude」的智慧，並已請求美國政府介入調查。"
tags: [AI, 技術, Anthropic, Claude, 阿里巴巴]
image: 2026-06-25-Anthropic-says-Alibaba-illicitly-extracted-Claude-AI-model-capabilities.jpg
image_alt: "象徵複雜交織的數位數據節點與其間資訊流動的抽象影像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "此事件為我們如何保護 AI 模型的「智慧」提出了全新的法律與倫理挑戰。鑑於技術發展迅速，建立國際間保護模型知識產權的準則已刻不容緩。"
quiz:
  - question: "在此事件中，Anthropic 所指控的「蒸餾 (Distillation) 攻擊」核心為何？"
    choices: ["直接刪除 AI 的數據", "以強大 AI 的回答作為學習數據來複製其效能", "物理上入侵 AI 伺服器"]
    answer: 1
    explanation: "Anthropic 指控競爭模型透過大規模蒐集其旗下模型「Claude」的回答數據，並以此訓練自家的 AI，從而不正當地提升效能。"
  - question: "根據 Anthropic 的調查，此次攻擊中疑似被動用的假帳號數量約為多少？"
    choices: ["約 250 個", "約 2,500 個", "約 25,000 個"]
    answer: 2
    explanation: "根據 Anthropic 的公布，對方動用了約 25,000 個假帳號，發送了高達 2,880 萬次提問。"
  - question: "此次被 Anthropic 公開點名的企業所屬國家為何？"
    choices: ["美國", "中國", "韓國"]
    answer: 1
    explanation: "Anthropic 指名了包括阿里巴巴，以及深度求索 (DeepSeek)、月之暗面 (Moonshot AI)、面壁智能 (MiniMax) 等總部位於中國的 AI 開發商。"
lang: zh-tw
ref: 2026-06-25-Anthropic-says-Alibaba-illicitly-extracted-Claude-AI-model-capabilities
---

想像一下。您花了好幾年時間不眠不休地打造了一位非常聰明且具備創意的私人補習老師。然而某天，有人偷偷錄下這位老師的所有授課內容並進行整理，接著製作出一模一樣的「山寨老師」，並以廉價費用開始提供課程，您會作何感想？

近期，人工智慧 (AI) 業界就傳出了類似的指控。開發 AI 模型「Claude」的 Anthropic 公司聲稱，包括阿里巴巴在內的數家中國 AI 企業，未經許可擅自竊取了其模型的智慧。[參考資料 1](https://www.channelnewsasia.com/business/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-6207956)

### 這件事為什麼很重要？

此事件不單是企業間的爭端，更對深深融入我們日常生活的「AI 智慧」究竟是如何誕生及保護的，提出了重要疑問。事實上，開發單一 AI 模型需要投入天文數字的成本與無數研究人員的心血。[參考資料 9](https://claude.com/) 如果有人能以極低成本複製這龐大的努力，將嚴重挫傷企業開發新 AI 的意願。這最終可能導致技術發展遲緩，並破壞市場的公平競爭環境。[參考資料 8](https://techgolly.com/news/alibaba-illicit-ai-model-accusations-cause-shares-to-drop-as-anthropic-warns-white-house)

### 輕鬆了解：「蒸餾」之名的竊取行為

Anthropic 將此次事件稱為「蒸餾 (Distillation) 攻擊」。[參考資料 17](https://finance.yahoo.com/technology/ai/articles/anthropic-says-alibaba-illicitly-extracted-203048734.html) 蒸餾是 AI 業界常用的學習方法，簡單來說，就像是偷偷抄襲「聰明老師的重點筆記」。

原本的蒸餾（即較小的模型透過模仿大型模型的回答來進行學習的技術）是一種透過參考效能優異的「老師 AI」之回答，使效能較低的「學生 AI」變得更聰明的正當學習手法。[參考資料 6](https://www.jpost.com/business-and-innovation/article-887718) 然而，Anthropic 質疑的是此過程是在「未經授權」的情況下大規模進行的。

這好比廚師為了探究秘製醬汁的製作方式，偷偷潛入廚房並試圖嘗試醬汁配方多達 2,880 萬次。[參考資料 8](https://techgolly.com/news/alibaba-illicit-ai-model-extraction-accusations-cause-shares-to-drop-as-anthropic-warns-white-house) Anthropic 主張，阿里巴巴的特定研究團隊創建了多達 2 萬 5 千個假帳號，向 Claude 發動提問攻勢，試圖竊取這份秘方。[參考資料 8](https://techgolly.com/news/alibaba-illicit-ai-model-extraction-accusations-cause-shares-to-drop-as-anthropic-warns-white-house), [參考資料 13](https://stocktwits.com/news-articles/markets/equity/anthropic-writes-to-white-house-accusing-alibaba-of-illicitly-accessing-claude-ai-models/cZKyprTR7Qd)

### 目前處境：Anthropic 的反擊

Anthropic 對此事嚴陣以待。除了單純表達抗議，他們已正式致函美國國會議員及白宮官員，告知此一事態。[參考資料 2](https://www.zerohedge.com/political/anthropic-accuses-alibaba-running-major-adversarial-distillation-campaign-extract-claude)

此次被點名的企業不只阿里巴巴。Anthropic 指出，深度求索 (DeepSeek)、月之暗面 (Moonshot AI)、面壁智能 (MiniMax) 等總計 3 家中國 AI 開發商，皆以類似手法未經許可提取其技術，用以提升自家模型的效能。[參考資料 3](https://www.linkedin.com/posts/vaibhav-pandya_anthropic-says-chinese-ai-firms-used-16-million-activity-7432708525300031488-uasc), [參考資料 5](https://gizmodo.com/anthropic-says-chinese-ai-companies-made-models-by-illicitly-copying-its-capabilities-2000725717) 目前此問題已與國際間的 AI 技術霸權競爭掛鉤，成為熱門話題。[參考資料 16](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)

### 接下來會發生什麼？

此事件極有可能在未來引發關於「AI 智慧版權」的全新法律辯論。過去我們多聚焦於軟體或內容的著作權，如今如何保護 AI 模型所習得的「智慧精華」將成為核心課題。

對使用者而言，需要關注的是，這些事件是否會促使 AI 開發商加強安全政策，進而營造出更安全的 AI 環境，亦或是會導致服務受限等不便。可以確定的是，隨著 AI 變得越聰明，試圖竊取與致力守護之間的緊張感，將會變得愈發強烈。

## 參考資料

1. [Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://www.channelnewsasia.com/business/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-6207956)
2. [Anthropic Accuses Alibaba Of Running Major Adversarial Distillation Campaign](https://www.zerohedge.com/political/anthropic-accuses-alibaba-running-major-adversarial-distillation-campaign-extract-claude)
3. [China's AI Companies Illicitly Extract Claude Capabilities](https://www.linkedin.com/posts/vaibhav-pandya_anthropic-says-chinese-ai-firms-used-16-million-activity-7432708525300031488-uasc)
4. [Anthropic accuses Chinese AI firms of siphoning Claude via distillation](https://biz.chosun.com/en/en-it/2026/02/24/7QIXKECJTBBLTA5VZQ42SBM7LY/)
5. [Anthropic Says Chinese AI Companies Improved Models By 'Illicitly Copying'](https://gizmodo.com/anthropic-says-chinese-ai-companies-made-models-by-illicitly-copying-its-capabilities-2000725717)
6. [Anthropic accuses Chinese labs of stealing Claude's data](https://www.jpost.com/business-and-innovation/article-887718)
7. [Anthropic alleges large-scale distillation campaigns targeting Claude](https://www.computerworld.com/article/4136474/anthropic-alleges-large-scale-distillation-campaigns-targeting-claude-2.html)
8. [Alibaba Illicit AI Model Extraction Accusations Cause Shares to Drop](https://techgolly.com/news/alibaba-illicit-ai-model-extraction-accusations-cause-shares-to-drop-as-anthropic-warns-white-house)
9. [Claude](https://claude.com/)
10. [Anthropic Accuses Chinese AI Firms of Illicit Model “Distillation”](https://techgrid.media/news/anthropic-accuses-chinese-ai-firms-of-illicit-model-distillation-in-claude-copying-dispute/)
13. [Anthropic Writes To White House Accusing Alibaba Of “Illicitly” Accessing Claude AI](https://stocktwits.com/news-articles/markets/equity/anthropic-writes-to-white-house-accusing-alibaba-of-illicitly-accessing-claude-ai-models/cZKyprTR7Qd)
16. [Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)
17. [Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://finance.yahoo.com/technology/ai/articles/anthropic-says-alibaba-illicitly-extracted-203048734.html)
18. [Anthropic Accuses Alibaba of Distilling Claude AI Model Capabilities](https://www.globalbankingandfinance.com/anthropic-alibaba-illicitly-extracted-claude-ai-model/)