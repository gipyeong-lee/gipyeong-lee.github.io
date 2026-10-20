---
layout: post
title: "如果我突然消失了怎麼辦？給獨立開發者的數位遺囑：「死亡計畫開關」(Death Plan Switch)"
description: "介紹一個自助託管的死人開關(Dead Man's Switch)服務，當獨立開發者因突發狀況失聯時，能安全地傳遞關鍵資訊。"
summary: "「死亡計畫開關」(Death Plan Switch) 是一套自動提醒系統，當獨立開發者停止回應時，會將預先準備好的資訊傳送給指定對象。"
tags: [開發者, 數位遺產, 死人開關, 資訊安全, 獨立開發]
image: 2026-10-20-Show-HN-Death-Plan-Switch-a-self-hosted-dead-mans-switch-for-solo-devs.jpg
image_alt: "將數位訊息安全保存並自動傳遞的過程圖形化"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是數位時代必備的保險。特別對於獨自維護服務的開發者而言，這是保護自身紀錄與專案負責任的選擇。"
quiz:
  - question: "「死亡計畫開關」(Death Plan Switch) 的主要目的是什麼？"
    choices: ["網站訪客統計分析", "在開發者失聯時安全地傳遞重要資訊", "自動化伺服器維護"]
    answer: 1
    explanation: "它扮演數位遺囑的角色，當開發者停止週期性的確認動作時，會通知預先指定的對象。"
  - question: "死亡計畫開關通常運作的步驟為何？"
    choices: ["定期確認郵件 -> 若未回應則聯繫次順位聯絡人 -> 最後通知接收者", "立即公開所有資訊", "立即刪除伺服器"]
    answer: 0
    explanation: "系統會週期性發送郵件確認開發者是否生存，若無回應，會先聯繫家人等指定聯絡人，最後再通知最終接收者。"
  - question: "類似目的的服務「Aeterna」有什麼特點？"
    choices: ["支援遊戲模式", "專注於安全與隱私的自助託管工具", "即時伺服器監控"]
    answer: 1
    explanation: "Aeterna 是一套專注於安全與隱私保護的自助託管服務，用於規劃數位遺產。"
lang: zh-tw
ref: 2026-10-20-Show-HN-Death-Plan-Switch-a-self-hosted-dead-mans-switch-for-solo-devs
---

試想一下，作為一名日以繼夜打造新服務、獨自奮鬥的獨立開發者，如果有一天因為突發事故或狀況，導致你無法再坐在電腦前，會發生什麼事呢？你所經營服務的營運權歸誰所有？你獨自掌握的關鍵程式碼資訊或管理員帳號又該怎麼辦？

對於單打獨鬥的開發者來說，這些問題聽起來可能有些沉重，但對於活躍在數位世界的我們而言，這是必須考慮的「數位遺產」問題。最近，一套名為「死亡計畫開關」(Death Plan Switch) 的服務登場，因能解決這些顧慮而備受關注。

## 為什麼這很重要？

你聽過「死人開關」(Dead Man's Switch) 這個術語嗎？它原指火車的一種安全裝置，當列車長失去意識時，火車會自動停止。數位世界裡的死人開關原理也是如此。如果使用者沒有定期發送「我很好」的訊號，系統就會自動將預先設定好的訊息或資訊傳遞給指定對象。

獨立開發者通常獨自掌握專案的所有權限與核心資訊。如果他們因不可預測的情況失聯，他們維護的網站或專案很容易陷入荒廢狀態。這不僅僅是開發者個人的損失，對該服務的使用者而言也會造成極大的不便。「死亡計畫開關」正是一種類似「數位保險」的機制，能填補這些空缺。

## 簡單來說：「數位遺囑」的原理

簡言之，這項服務就像你的「數位秘書」，每週在固定時間詢問你的近況。[死亡計畫開關 (Death Plan Switch)](https://deathplanswitch.com/) 是一項免費的自助託管（Self-hosted，即安裝並運作於自己的伺服器上）服務，專為獨立 Web 開發者設計。[參考資料 10](https://deathplanswitch.com/)

它的運作方式如同將遺囑鎖進保險箱，並由遺囑執行人定期確認你的生死。具體流程如下：

1. **定期檢查**：系統每週會發送郵件給你。
2. **生存確認**：你點擊郵件中的連結，發出「我一切正常」的訊號。
3. **緊急應變**：若你在一段時間內未回應郵件，系統會先聯絡你指定的「次順位聯絡人（如家人或信賴的人）」。
4. **最終傳遞**：若狀況仍未解決，系統才會將資訊傳遞給「需要接手重要作業的人」。[參考資料 10](https://deathplanswitch.com/)

具備類似目的的工具還有 [Aeterna](https://alpyxn.github.io/aeterna/)。這項服務同樣專注於隱私保護，為規劃數位遺產的人們提供安全性。[參考資料 9](https://github.com/alpyxn/aeterna), [參考資料 14](https://alpyxn.github.io/aeterna/)

## 目前的選擇：多樣化的解決方案

目前市面上關於「死人開關」的解決方案，會根據開發者的需求而有所不同：

* **使用者友善型**：最基礎的服務形式，預先寫好郵件並設定發送給指定接收者。[參考資料 1](https://www.deadmansswitch.net/)
* **開發者工具型**：如 [circa10a](https://github.com/circa10a/dead-mans-switch) 等工具，除了 UI 之外，還能透過 API 或 CLI（命令列工具）建立更複雜的開關。這類工具設計為能透過各種訊息發送供應商發出通知。[參考資料 13](https://github.com/circa10a/dead-mans-switch)

大多數服務支援「自助託管」的原因，是因為開發者有不想將敏感的個人資訊交由外部處理，希望在自己的伺服器環境下親自管控的需求。

## 未來展望：數位遺產的處理

隨著數位資產的重要性日益增加，這些「數位遺產管理」工具將會變得更加精緻。未來不僅限於傳遞訊息，預計將演化為能安全地委託帳號存取權限，或是提供能解密加密數據的密鑰等方式。身為開發者，不僅是撰寫程式碼，思考自己所創造的成果在自己不在時該如何處理，或許也是專業素養的一環。

## AI 記者的觀點：數位時代的保險

技術可以在我們離世後持續運作。將數位遺產這個沉重的主題，以開發者特有的「自助託管工具」方式來解決，是非常理性的途徑。今天，何不為你的專案準備一個小小的「開關」呢？

## 參考資料

1. [Home - DeadMan's Switch](https://www.deadmansswitch.net/)
2. [Aeterna: A Lightweight, Self-Hosted Dead Man's Switch for End-of-Life & Digital Legacy Planning - alpyxn/aeterna](https://github.com/alpyxn/aeterna)
3. [Death Plan Switch: if you disappear, the right people are told](https://deathplanswitch.com/)
4. [An all-in-one self-hosted app for creating a "Dead Man's Switch" - circa10a/dead-mans-switch](https://github.com/circa10a/dead-mans-switch)
5. [Aeterna - Dead Man's Switch](https://alpyxn.github.io/aeterna/)