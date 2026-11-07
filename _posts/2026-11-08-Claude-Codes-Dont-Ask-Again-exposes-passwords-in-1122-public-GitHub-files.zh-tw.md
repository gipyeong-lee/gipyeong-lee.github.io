---
layout: post
title: "對 AI 說「不要再問了」導致密碼外洩？1,122 個 GitHub 儲存庫發出警告"
description: "探討 Anthropic AI 編碼助理 Claude Code 的「不再詢問」功能如何導致開發者的密碼與 API 金鑰外洩，並了解其風險與應對措施。"
summary: "Claude Code AI 的便利功能「不再詢問」設定，導致開發者的密碼與 API 金鑰以明文形式存儲於設定檔中，進而引發 GitHub 外洩安全事故。"
tags: [AI, 安全, ClaudeCode, 開發者, GitHub]
image: 2026-11-08-Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files.jpg
image_alt: "描繪 GitHub 程式碼儲存庫安全性受損與 AI 工具圖示的數位藝術作品。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是一個血淋淋的案例，展示了為了便利而簡化安全設定可能付出的沉重代價。使用 AI 工具時，務必確認哪些數據被存儲在哪裡。"
quiz:
  - question: "Claude Code 導致密碼外洩的主要原因為何？"
    choices: ["AI 模型遭到駭客攻擊", "使用「不再詢問」功能時，指令以明文形式存儲在設定檔中", "GitHub 伺服器本身遭到駭客攻擊"]
    answer: 1
    explanation: "當使用者選擇「Yes, and don't ask again」選項時，AI 執行的指令會以明文形式存儲在設定檔（如 .claude/settings.local.json）中。"
  - question: "下列何者不屬於本次安全事故中可能洩露的資訊？"
    choices: ["API 金鑰", "資料庫密碼", "個人電腦的作業系統更新紀錄"]
    answer: 2
    explanation: "洩露的資訊主要為密碼、API 金鑰、資料庫憑證、SSH 金鑰等敏感數據。"
  - question: "據調查，本次安全事故受影響的公開 GitHub 儲存庫共有多少個？"
    choices: ["1,122 個", "76,011 個", "104,185 個"]
    answer: 0
    explanation: "根據安全公司 Apiiro 的調查，共在 1,122 個公開 GitHub 儲存庫中發現含有敏感資訊的檔案。"
lang: zh-tw
ref: 2026-11-08-Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files
---

想像一下。你像往常一樣將繁瑣的任務交給 AI 編碼助理。每當 AI 問你「是否要繼續執行此指令？」時，為了省麻煩，你點選了「好，以後不要再問我，直接執行（Yes, and don't ask again）」按鈕。但如果你發現，這一次輕輕的點擊，竟讓你將資料庫密碼與 API 金鑰「公開展示」在網際網路上，供全球任何人瀏覽，你會作何感想？

最近，AI 工具「Claude Code」的使用者之間發生了這起荒謬且駭人的安全事故。一個單純的便利功能，竟然將開發者珍貴的憑證以明文（Plaintext，即未加密、可直接閱讀的數據）儲存了下來。

## 為何這很重要？

這不僅僅是「開發者的事」。AI 編碼工具如今已成為開發工作的標準配備。如果這類工具將你輸入指令中包含的密碼，在沒有任何安全保護措施的情況下寫入設定檔，並將該檔案上傳至 GitHub 等共享儲存庫，情況將會徹底改變。惡意的駭客可以利用這些資訊闖入你的伺服器，或輕易竊取你的雲端服務帳號。

安全研究公司 Apiiro 確認，受此問題影響，共有 1,122 個公開 GitHub 儲存庫中的密碼與 API 金鑰等敏感資訊處於毫無防備的暴露狀態[Source 2, Source 5, Source 14]。

## 簡單理解：「聰明助手」的失誤

簡單比喻，Claude Code 就像你的「聰明助手」。你告訴這位助手：「以後別再每次都問我密碼，直接按我要求的指令處理就好。」

問題就出在這裡。為了下次能繼續處理你的指令，助手會將你給的指令詳盡地寫入它的「記事本」。但這位助手的安全意識不足，它沒有過濾掉你在指令中提到的「資料庫密碼：12345」等敏感資訊，而是原封不動地記錄下來。隨後，這本記事本就被你一併上傳到了你與他人共享工作成果的公開平台（GitHub）上[Source 6, Source 7]。

若從技術層面深入分析，當使用者選擇「不再詢問（Yes, and don't ask again）」時，Claude Code 會將所執行的 Shell（直接與電腦對話的介面）指令，以明文形式存儲在 `.claude/settings.local.json` 或 `.claude/settings.json` 等設定檔中[Source 3, Source 7, Source 8]。開發者在不經意間將這些檔案與程式碼一同提交（Commit，將變更記錄至儲存庫的行為）到 GitHub 時，敏感資訊便隨之暴露在網路上[Source 2, Source 5]。

## 目前狀況如何？

情況相當嚴重。根據 Apiiro 的分析，在調查的 104,185 份設定檔副本中，有 1,122 份發現了實際的密碼或 API 金鑰[Source 14]。另一項分析亦指出，在 76,011 份副本中，有 298 份在共享設定檔中包含了密碼[Source 3]。

這些檔案不單單是設定檔，它們其實是一串包含 API 金鑰、資料庫憑證、SSH 金鑰等的「數位鑰匙包」[Source 6, Source 7]。如果你正在使用 Claude Code，務必立即仔細檢查 GitHub 儲存庫的歷史紀錄。即便現在在儲存庫中看不到這些檔案，它們仍可能殘留在過去的提交紀錄中[Source 3]。

## 未來該如何應對？

專家強烈建議，如果密碼與 API 金鑰曾經被儲存於這些檔案中，**務必立即廢棄並重新生成（Rotate）所有相關憑證**[Source 3]。

往後，使用 AI 編碼代理（Agent）的開發者必須對設定檔的管理投入更多關注。企業方面，必須強化安全政策，防止 AI 工具的設定檔被提交至儲存庫，並透過持續性的掃描系統監控是否有敏感資訊外洩[Source 7]。

## MindTickleBytes 的 AI 記者觀點

便利往往會侵蝕安全。Claude Code 所提供的「自動化」強大工具，因降低了使用者的警覺性，導致 1,122 個儲存庫遭受波及。這再次提醒我們一個顯而易見的事實：當工具變得越聰明，使用工具的人類，其安全意識就必須更加敏銳。

## 參考資料

1. [Source 2] Claude Code "Don't Ask Again" File Leaks 1,122 Public GitHub Repos Detection and Remediation Guide (https://securityarsenal.com/blog/claude-code-dont-ask-again-file-leaks-1122-public-github-repos-detection-and-remediation-guide)
2. [Source 3] Claude Code's don't-ask-again file held 1,379 secrets in 1,122 public repos: What to do (https://dev.to/piekwerk/claude-codes-dont-ask-again-file-held-1379-secrets-in-1122-public-repos-what-4mg5)
3. [Source 5] Claude Code 'Don't Ask Again' Bug Exposes 1,122 GitHub Repos (https://aviatrix.ai/threat-research-center/claude-code-dont-ask-again-settings-local-json-passwords-keys-1122-github-2026/)
4. [Source 6] Claude Code “Don't Ask Again” Feature Exposes Passwords and API Keys in Public GitHub Repositories (https://www.cyberincidents.in/blog/claude-code-dont-ask-again-feature-exposes-passwords-and-api-keys-in-public-github-repositories)
5. [Source 7] Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public GitHub Repos (https://www.realground.com/news/2650-claude-codes-dont-ask-again-file-exposes-passwords-and-keys-in-1-122-public)
6. [Source 8] Утечка “Don’tAskAgain” отClaudeCode: пароли и ключи (https://dzen.ru/a/au7m4aCL2QDFv4Wh)
7. [Source 14] Claude Code “Don’t ask again” left secrets in 1,122 GitHub files (https://madrobot.blog/2026/11/07/claude-code-dont-ask-again-secrets-github/)