---
layout: post
title: "機器人終於能像人一樣靈活運作？Google Gemini Robotics 2.5 登場"
description: "透過 Google DeepMind 最新機器人 AI「Gemini Robotics 2.5」在工廠現場展現的驚人手藝與作業效率提升，一探即將走入日常生活的機器人未來。"
summary: "Google DeepMind 發布的 Gemini Robotics 2.5 相比前代模型，作業成功率最高提升了 100%，處理速度縮短達 30%，並在實際工廠環境中創下 96% 的成功率，大幅提升了機器人在實際操作上的靈活度。"
tags: [AI, 機器人學, Google DeepMind, Gemini]
image: 2026-11-11-Gemini-Robotics-25-accelerates-real-world-general-dexterity.jpg
image_alt: "搭載 Google DeepMind Gemini Robotics 2.5 技術、正在執行複雜任務的類人型機器人"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Gemini Robotics 2.5 不僅僅是變聰明了，它更證明了「行動智慧」在物理世界中完成實際任務的可能性。未來，我們與機器人同事並肩工作、讓它們默默協助完成任務的日子已更近一步。"
quiz:
  - question: "Google Gemini Robotics 2.5 與前代模型相比，有哪些改進？"
    choices: ["作業成功率提升及速度縮短", "電池續航力增加兩倍", "全新的機器人硬體設計"]
    answer: 0
    explanation: "Gemini Robotics 2.5 根據作業類型，最高提升了 100% 的成功率，處理速度也快了 20% 到 30%。"
  - question: "像 Gemini Robotics 2.5 這類 VLA 模型，是透過什麼來決定機器人的行動？"
    choices: ["僅分析過去的資料日誌", "攝影機輸入值與指令", "僅使用使用者的語音指令"]
    answer: 1
    explanation: "VLA（視覺-語言-行動，Vision-Language-Action）模型會將攝影機捕捉到的視覺資訊與給定的指令相結合，進而輸出機器人的動作。"
  - question: "在工廠現場中，搭載 Gemini Robotics 2.5 的機器人創下了多少百分比的成功率？"
    choices: ["85%", "90%", "96%"]
    answer: 2
    explanation: "在賓士（Mercedes-Benz）工廠的測試中，Apptronik 的 Apollo 2 類人型機器人利用 Gemini Robotics 2.5 達成了 96% 的作業成功率。"
lang: zh-tw
ref: 2026-11-11-Gemini-Robotics-25-accelerates-real-world-general-dexterity
---

想像一下：在零件堆疊雜亂的工廠作業台上，機器手臂能毫不遲疑地精準挑選所需零件，甚至能在彈指間完成過去需由人工進行的精細綁繩工作。過去的機器人更接近「單純的機械」，只能重複執行既定路徑；但現在，它們正蛻變為能自行掌握狀況並採取行動的「聰明工作者」。

Google DeepMind 於 2026 年 11 月 10 日公開了將機器人智慧提升至全新境界的「Gemini Robotics 2.5」。這是迄今為止 Google 所展示過性能最強大的視覺-語言-行動（VLA, Vision-Language-Action）模型 [[參考資料 9](https://codingislove.com/gemini-robotics-2-5/), [參考資料 12](https://arxiv.org/abs/2503.20020)]。

## 這為何重要？

機器人不僅能做好重複性工作，更具備了理解環境並發揮「手藝（Dexterity）」的能力，這預告了我們的產業現場與日常生活將發生巨大變革。過去的機器人大多專精於特定工序，只要情況稍有變化，就需要人工介入重新設定程式碼 [[參考資料 5](https://www.linkedin.com/posts/aslam-ahamed_artificialintelligence-ai-robotics-activity-7490016683873542144-3VmV)]。然而，現在機器人能夠透過感知環境並自行判斷，從而執行更具通用性的任務。

特別是在物流中心的分類作業或工廠的複雜組裝線上，如果機器人能執行與人類相當、甚至比人類更精確且快速的任務，生產效率將會大幅躍升。

## 輕鬆理解：擁有「眼睛」與「大腦」的機器人

簡單來說，Gemini Robotics 2.5 就如同賦予了機器人「狀況判斷力」與「靈活的手指」。如果說舊式機器人是蒙著眼、只能按指令動作的人偶，那麼搭載此模型的機器人就是能透過攝影機（眼睛）拍攝並觀察周遭狀況，再由人工智慧（大腦）判斷影像中該做什麼，最後驅動機器手臂（手）立即執行動作 [[參考資料 9](https://codingislove.com/gemini-robotics-2-5/)]。

其中的核心 VLA 模型，扮演著將「視覺（Vision）」資訊與「語言（Language）」指令結合，並轉化為機器人「行動（Action）」的橋樑。這與人類閱讀食譜（語言）、用眼睛確認食材狀態（視覺）後進行切菜（行動）的過程非常相似。正因如此，機器人即便在複雜的環境中，也能主動找出該做的事並執行 [[參考資料 10](https://deepmind.google/models/gemini-robotics/)]。

## 現狀：以數據證實的性能

Gemini Robotics 2.5 已經在實際現場證明了其能力。據 Google DeepMind 指出，相比前幾代的機器人模型，該模型根據任務內容的不同，將作業成功率提升了 30% 到最高 100% [[參考資料 12](https://arxiv.org/abs/2503.20020)]。

更驚人的是速度。不僅成功率提高，完成作業的時間也比過去快了 20% 到 30% [[參考資料 12](https://arxiv.org/abs/2503.20020)]。在實際於賓士（Mercedes-Benz）工廠進行的試運行中，搭載 Gemini Robotics 2.5 的 Apptronik 公司類人型機器人「Apollo 2」創下了 96% 的驚人作業成功率 [[參考資料 11](https://blockchain.news/news/gemini-robotics-2-5-enhances-dexterity-safety), [參考資料 12](https://arxiv.org/abs/2503.20020)]。

## 未來發展如何？

Google 的目標是透過這項技術，讓機器人在物理世界中成為更具通用性且有價值的存在。從 Gemini Robotics 2.0 模型開始，不僅能控制類人型機器人的全身，甚至實現了多台機器人在同一個空間內相互協作 [[參考資料 10](https://deepmind.google/models/gemini-robotics/)]。

當然，這並不代表「物理人工通用智慧（Physical AGI）」已經降臨。因為仍有安全問題與技術難關尚待解決 [[參考資料 5](https://www.linkedin.com/posts/aslam-ahamed_artificialintelligence-ai-robotics-activity-7490016683873542144-3VmV), [參考資料 12](https://arxiv.org/abs/2503.20020)]。但從技術發展的速度來看，機器人在身旁安全且精確地代勞人類工作的未來，已不再是遙不可及的幻想。

## AI 的觀點

Gemini Robotics 2.5 不僅僅是變聰明了，它更證明了「行動智慧」在物理世界中完成實際任務的可能性。未來，我們與機器人同事並肩工作、讓它們默默協助完成任務的日子已更近一步。

## 參考資料

1. [Gemini Robotics 2.5 accelerates real-world general dexterity](https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/)
2. [Gemini— Google DeepMind | Our next era of frontier intelligence](https://deepmind.google/models/gemini/)
3. [Google Just Unveiled Gemini Robotics, and It's a Whole New Level of...](https://lilys.ai/en/notes/gemini-robotics-20251020/google-unveils-gemini-robotics-ai-humanoid)
4. [Google DeepMind's Gemini Robotics 2 boosts AI accuracy... | LinkedIn](https://www.linkedin.com/posts/aslam-ahamed_artificialintelligence-ai-robotics-activity-7490016683873542144-3VmV)
5. [Google reveals Gemini Robotics 2.0, promising improved dexterity and safety | AIBlog.com.my](https://aiblog.com.my/articles/google-reveals-gemini-robotics-20-promising-improved-dexterity-and-safety)
6. [Gemini Robotics 2 advances dexterity](https://newsletter.dotika.ai/p/gemini-robotics-2-advances-dexterity)
7. [Google DeepMind releases Gemini Robotics 2.5 for robot dexterity](https://codingislove.com/gemini-robotics-2-5/)
8. [Gemini Robotics — Google DeepMind](https://deepmind.google/models/gemini-robotics/)
9. [Gemini Robotics 2.5 Enhances Dexterity and Safety in Real ...](https://blockchain.news/news/gemini-robotics-2-5-enhances-dexterity-safety)
10. [Gemini 2.5 for robotics and embodied intelligence - Google ...](https://arxiv.org/abs/2503.20020)