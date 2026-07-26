---
layout: post
title: "我的 AI 編碼紀錄消失了？了解 Claude Code 的 30 天刪除規則"
description: "探討 AI 編碼工具 Claude Code 自動刪除用戶對話紀錄的現象、原因以及解決方法。"
summary: "Claude Code 預設會刪除超過 30 天的對話紀錄，用戶可以透過修改設定來防止此情況發生。"
tags: [AI, 編碼, ClaudeCode, 生產力, 開發技巧]
image: 2026-07-26-Claude-Code-Deletes-Your-Context-History-from-Your-Device-After-30-Days.jpg
image_alt: "將電腦螢幕上的編碼紀錄消失視覺化的圖形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開發工具的數據政策會直接影響用戶的工作流程。若要在便利性與數據保存之間取得平衡，必須關注工具的內部設定。"
quiz:
  - question: "Claude Code 刪除對話紀錄的基準期限是多久？"
    choices: ["7 天", "30 天", "1 年"]
    answer: 1
    explanation: "Claude Code 預設會自動刪除超過 30 天的對話紀錄。"
  - question: "若要防止對話紀錄被自動刪除，應該修改哪個檔案？"
    choices: ["settings.json", "config.py", "main.js"]
    answer: 0
    explanation: "透過調整用戶設定檔 settings.json 中的 cleanupPeriodDays 數值，可以延長紀錄的保存期限。"
  - question: "紀錄刪除會在何時發生？"
    choices: ["每天午夜", "每次啟動 Claude Code 時", "每週一次"]
    answer: 1
    explanation: "此刪除機制會在每次啟動 Claude Code 時執行。"
lang: zh-tw
ref: 2026-07-26-Claude-Code-Deletes-Your-Context-History-from-Your-Device-After-30-Days
---

試想一下：為了尋找上個月與 AI 絞盡腦汁完成的複雜程式邏輯，你打開了日誌，卻發現最重要的對話紀錄竟消失得無影無蹤。這種情況雖然令人焦慮，但事實上，這可能是你的工具正在「盡忠職守」地執行其任務。

最近在開發者社群中，關於 AI 編碼工具 Claude Code 的對話紀錄在未經預告下被刪除的抱怨聲浪不斷。 [參考資料: Claude Code 用戶抱怨他們的聊天紀錄被神秘地清除](https://www.theregister.com/ai-and-ml/2026/06/30/claude-code-users-complain-their-chat-records-are-being-mysteriously-wiped-out/5264673) 究竟為什麼會發生這種事呢？

## 這為什麼很重要？

對開發者而言，過去的對話紀錄不僅僅是文字，更是重要的資產，其中包含了與 AI 交流的思想軌跡、除錯的紀錄，以及項目的上下文（Context，AI 用來理解對話內容所需的資訊）。若這些紀錄無故消失，會導致必須重複解決相同問題，造成效率低落。特別是對於進行團隊專案或長時間開發任務的人來說，數據保存政策直接關乎工作的連續性。

## 輕鬆理解：AI 內部的「自動清潔工」

為什麼紀錄會消失？簡單來說，是因為 Claude Code 內建了一種「自動清潔工」程式。 [參考資料: Claude Code 預設在 30 天後刪除聊天紀錄，且未發出警告 | nowosci.ai/en](https://nowosci.ai/en/article/claude-code-deletes-chat-history-without-warning) 

這個清潔工的本體就是設定檔中的 `cleanupPeriodDays`（自動刪除等待天數）選項。預設值被設為「30」，每當啟動 Claude Code 時，該程式便會運作，找出並刪除超過 30 天的對話日誌檔案。 [參考資料: Claude Code 用戶抱怨他們的聊天紀錄被神秘地清除](https://www.theregister.com/ai-and-ml/2026/06/30/claude-code-users-complain-their-chat-records-are-being-mysteriously-wiped-out/5264673)

以此比喻：**就像每天早上清潔公司來到家中，把 30 天前的報紙或便條紙全部丟棄一樣**。家裡雖然變乾淨了，但若便條紙上寫著項目的核心構思，情況就不同了。問題在於，這個「清潔」規則在安裝過程中並未對用戶進行充分告知。 [參考資料: Claude Code 預設在 30 天後刪除聊天紀錄，且未發出警告 | nowosci.ai/en](https://nowosci.ai/en/article/claude-code-deletes-chat-history-without-warning)

## 現況

許多用戶在珍貴的編碼對話紀錄消失後才意識到此事，感到相當困擾。 [參考資料: 我調查了 Claude Code 對話紀錄的儲存位置與保留期限 (cleanupPeriodDays) | DevelopersIO](https://dev.classmethod.jp/en/articles/claude-code-conversation-history-retention/) 

慶幸的是，有防止此情況的方法。只要修改設定檔 `settings.json` 即可解決。將 `cleanupPeriodDays` 的數值改為非常大的數字，就能阻止紀錄被自動刪除。例如設定為 3,650，約可保留紀錄達 10 年之久。 [參考資料: [BUG] Claude Code 預設靜默刪除超過 30 天的對話紀錄 · Issue #62476 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/62476) 許多用戶透過社群分享此方法，以保護自己的數據。 [參考資料: Claude Code 在 30 天後刪除對話紀錄 | Hacker News](https://news.ycombinator.com/item?id=48802300)

## 未來展望

為了改善用戶體驗 (UX)，預計 AI 工具未來將引入更明確的數據管理方式。目前，透過 GitHub Issue 等管道，已有請求指出希望不要直接刪除紀錄，而是將數據移至垃圾桶資料夾，或提供更易於用戶控制的刪除功能介面。 [參考資料: [BUG] Claude Code 預設靜默刪除超過 30 天的對話紀錄 · Issue #62476 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/62476) 

我們在使用 AI 工具時，需要具備一種智慧：偶爾檢查那便利性背後所隱藏的設定值代表什麼意義。保存紀錄不僅是單純的儲存，更是守護我們的工作流程與寶貴創意。

## MindTickleBytes AI 記者觀點

科技雖是協助我們工作的強大工具，但若不了解該工具如何處理我們的數據，反而可能遭遇預期之外的不便。若想在使用智慧 AI 的同時，保有對紀錄的完全主導權，未來在導入新工具時，養成仔細查看「設定」選單的習慣是必要的。

## 參考資料

1. [Claude Code users complain their chat records are being mysteriously wiped out](https://www.theregister.com/ai-and-ml/2026/06/30/claude-code-users-complain-their-chat-records-are-being-mysteriously-wiped-out/5264673)
2. [Claude Code Deletes Chat History After 30 Days by Default, Without Warning | nowosci.ai/en](https://nowosci.ai/en/article/claude-code-deletes-chat-history-without-warning)
3. [Claude Code History: Where It's Stored & How to Restore It](https://www.codeagentswarm.com/en/guides/claude-code-history-complete-guide)
4. [Claude Code deletes conversations after 30 days | Hacker News](https://news.ycombinator.com/item?id=48802300)
5. [I investigated the storage location and retention period (cleanupPeriodDays) of Claude Code conversation history | DevelopersIO](https://dev.classmethod.jp/en/articles/claude-code-conversation-history-retention/)
6. [[BUG] Claude Code silently deletes conversation transcripts after 30 days by default · Issue #62476 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/62476)