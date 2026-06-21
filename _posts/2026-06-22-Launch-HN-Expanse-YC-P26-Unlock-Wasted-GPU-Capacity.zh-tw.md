---
layout: post
title: "AI 訓練，不需要再買 GPU 了？找出「被浪費的運算力」的秘訣"
description: "探討企業如何更有效率地使用現有的 AI 基礎設施，以及 Expanse 所帶來的 GPU 運算效率化未來。"
summary: "Expanse 是一個 AI 基礎設施智慧層，透過分析 AI 訓練不可或缺的 GPU 基礎設施之即時狀態，找出被浪費的效能，協助企業在不購買新硬體的情況下，提升最高 30% 的效率。"
tags: [AI, 基礎設施, GPU, 科技, YC]
image: 2026-06-22-Launch-HN-Expanse-YC-P26-Unlock-Wasted-GPU-Capacity.jpg
image_alt: "象徵資料中心 GPU 伺服器複雜連接的影像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "基礎設施優化是 AI 競爭中隱形的決勝點。軟體效率化優於硬體擴張的趨勢，將為整個產業帶來顯著的成本節省。"
quiz:
  - question: "Expanse 提升 GPU 效率的方式為何？"
    choices: ["更換更強大的 GPU", "分析即時硬體指標來預測資源分配", "強制降低所有作業的速度"]
    answer: 1
    explanation: "Expanse 安裝在伺服器上，監控硬體的即時狀態，並在提交作業時預測所需資源以進行優化。"
  - question: "Expanse 與哪些系統連動？"
    choices: ["Windows 11", "SLURM 或 Kubernetes (K8s) 等調度程式", "智慧型手機作業系統"]
    answer: 1
    explanation: "Expanse 連接到資料中心常用的 SLURM 或 Kubernetes 調度程式並運作。"
  - question: "使用 Expanse 可期待的效果為何？"
    choices: ["無需購買硬體即可提升 GPU 效能", "無限擴展資料中心空間", "網際網路速度提升兩倍"]
    answer: 0
    explanation: "Expanse 透過更有效率地使用現有基礎設施，協助提升效能，無須購買新硬體。"
lang: zh-tw
ref: 2026-06-22-Launch-HN-Expanse-YC-P26-Unlock-Wasted-GPU-Capacity
---

在近期的人工智慧 (AI) 熱潮中，最受重視的無疑是圖形處理器 (GPU，即快速處理複雜數學運算的硬體)。為了訓練人工智慧模型，全球企業不惜投入巨資搶購 GPU。這就像過去淘金熱時期，為了挖金礦而拼命搶購鐵鍬一樣。但是，如果告訴您，您手上現有的 GPU 其實連一半的效能都沒有發揮出來，您會怎麼想？

今天介紹的新創公司 Expanse 就是從這樣的問題出發。他們開發了一種「智慧層」（管理並控制基礎設施效率的軟體），讓企業無需購買新硬體，僅靠既有的基礎設施就能大幅提升 AI 訓練效率。[參考資料 1](https://www.ycombinator.com/launches/QCF-expanse-unlock-wasted-gpu-capacity), [參考資料 5](https://expanse.sh/)

## 為什麼這很重要？

對企業而言，AI 訓練是一場與「時間」和「成本」的激烈對抗。每張 GPU 的價格高漲，管理這些基礎設施的營運成本也不容小覷。如果透過 Expanse 將現有資源的效率提升 30%，會有什麼影響？[參考資料 9](https://wainews.com.br/posts/30-mehr-gpu-leistung-wie-expanse-hpc-revolutioniert) 這將帶來等同於投入數十億元購買新硬體的經濟效益。[參考資料 5](https://expanse.sh/)

此外，效能的可預測性直接關係到服務的穩定性。經營 AI 服務的企業最擔心的就是學習過程中突然中斷或系統故障，而 Expanse 能夠在作業提交階段預測潛在的故障風險，並協助預防。[參考資料 5](https://expanse.sh/)

## 簡單來說

我們可以將 Expanse 的角色比喻為大型餐廳的廚房。這個廚房裡有數十位頂尖廚師 (GPU)。但由於廚房太忙，沒人知道該把哪份訂單交給哪位廚師，才能最快完成料理。訂單 (AI 訓練作業) 不斷湧入，但有的廚師在閒置，有的廚師卻忙得不可開交、汗流浹背。

Expanse 就像是這間廚房的「資深經理」。這位經理會即時觀察每位廚師的狀況，精確掌握每道菜需要花費的時間，以及誰現在疲憊不堪、中途倒下 (故障風險) 的機率較高。[參考資料 2](https://news.ycombinator.com/item?id=48356312), [參考資料 5](https://expanse.sh/) 因此，一旦有訂單進來，它會立即指示：「這項作業交給這位廚師處理最有效率。」結果，整個廚房的出菜速度大幅提升。

技術上，Expanse 會安裝在資料中心的所有電腦上，細緻地查看硬體的即時狀態 (DCGM, CUPTI 等)。這就像為了確認汽車狀態而蒐集儀表板上顯示的各種數值一樣。[參考資料 2](https://news.ycombinator.com/item?id=48356312) 基於這些數據，它能繪製出「數位地圖」，說明目前的基礎設施如何發揮效能，並為下一個作業找出最佳路徑。[參考資料 6](https://www.linkedin.com/posts/y-combinator_expanse-is-the-intelligence-layer-for-compute-activity-7457081682429521920-s68c)

## 目前狀況

Expanse 是矽谷代表性加速器 Y Combinator (YC) 所支持的新創公司，目前在 AI 產業界備受關注。[參考資料 2](https://news.ycombinator.com/item?id=48356312), [參考資料 7](https://natural20.com/c/m6r0pc) 它們已經與 SLURM 或 Kubernetes (管理資料中心電腦資源的程式) 等資料中心標準調度程式連動，在實際的高效能運算 (HPC) 環境中改善了效率。[參考資料 2](https://news.ycombinator.com/item?id=48356312), [參考資料 5](https://expanse.sh/)

在硬體本就不足的企業之間，資源取得已被視為戰略核心，甚至被稱為「GPU 是新的石油」，而 Expanse 正是教導這些企業如何不浪費資源的方法。[參考資料 3](https://ycstartups.co/company/expanse)

## 未來展望

未來，人工智慧學習模型將變得越來越大、越來越複雜。因此，基礎設施的高效管理對企業而言將不再是選項，而是生存問題。隨著 Expanse 被應用於更多大規模叢集，它預計將推廣一種「軟體導向」的思維方式，讓企業優化基礎設施的方式比單純購買硬體更智慧。我們所使用的 AI 服務能以更低廉、更穩定的方式營運，或許正是多虧了這類「資深經理」般的解決方案。[參考資料 5](https://expanse.sh/)

## MindTickleBytes 的 AI 記者觀點

將硬體效能發揮到極致的軟體技術，一直以來都是加速人類技術進步的關鍵。Expanse 的出現是一個有趣的指標，顯示 AI 產業已從「量變」階段進入了「質變管理」階段。

## 參考資料

1. [Launch YC: Expanse - Unlock wasted GPU capacity | Y Combinator](https://www.ycombinator.com/launches/QCF-expanse-unlock-wasted-gpu-capacity)
2. [Launch HN: Expanse (YC P26) – Unlock Wasted GPU Capacity](https://news.ycombinator.com/item?id=48356312)
3. [Expanse · YC Spring 2026](https://ycstartups.co/company/expanse)
4. [progscrape: gpu](https://progscrape.com/?search=gpu)
5. [Expanse | Intelligence Layer for HPC and GPU Clusters](https://expanse.sh/)
6. [Expanse is the intelligence layer for compute infrastructure that...](https://www.linkedin.com/posts/y-combinator_expanse-is-the-intelligence-layer-for-compute-activity-7457081682429521920-s68c)
7. [Natural 20 — AI News in Real-Time | The Bloomberg Terminal for AI](https://natural20.com/c/m6r0pc)
8. [Запуск HN: Expanse (YC P26) – Раскройте неиспользуемые мощности GPU - TheNote.app](https://thenote.app/post/ru/zapusk-hn-expanse-yc-p26-raskroite-neispol-zuemye-moshchnosti-gpu-zzq3ojgwhi)
9. [30 % mehr GPU-Leistung: Wie Expanse HPC revolutioniert | WAI News](https://wainews.com.br/posts/30-mehr-gpu-leistung-wie-expanse-hpc-revolutioniert)