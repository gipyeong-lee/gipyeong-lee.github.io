---
layout: post
title: "我的編碼紀錄竟然被偷偷傳送到雲端？ZCode 的隱密數據外洩爭議"
description: "AI 編碼工具 ZCode 被爆在未經授權的情況下，將使用者的 Git 紀錄傳送到伺服器。我們將探討這對開發者來說為什麼如此危險。"
summary: "經鑑識分析證實，AI 編碼工具 ZCode 會將使用者的整個專案 Git 紀錄加密，並偷偷上傳至阿里雲 (Aliyun OSS)。"
tags: [AI, 編碼, 安全, ZCode, 開發工具]
image: 2026-09-18-ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history.jpg
image_alt: "描繪電腦螢幕中的編碼數據被吸入不明雲端伺服器的插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開發者交給編碼工具的數據不僅僅是程式碼而已。這種不透明的數據收集行為，是從根本上動搖 AI 工具信任感的危險舉動。"
quiz:
  - question: "ZCode 被指控偷偷上傳使用者的哪些數據？"
    choices: ["僅聊天紀錄", "整個專案的 Git 紀錄與設定", "僅瀏覽器瀏覽紀錄"]
    answer: 1
    explanation: "ZCode 被指控將包含 Git 紀錄、reflogs、LFS 快取等在內的整個專案工作區進行加密並傳輸。"
  - question: "ZCode 的官方隱私權政策如何說明數據收集？"
    choices: ["明確說明會上傳整個專案", "僅提及對話中提交的數據", "完全沒有提及"]
    answer: 1
    explanation: "官方政策僅提及收集對話中提交的文字、檔案與程式碼，並未說明會上傳整個儲存庫。"
  - question: "ZCode 將數據上傳至哪種雲端服務？"
    choices: ["AWS S3", "Google Cloud Storage", "Aliyun OSS"]
    answer: 2
    explanation: "分析顯示，ZCode 正在將數據傳輸至阿里雲 (Aliyun OSS)。"
lang: zh-tw
ref: 2026-09-18-ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history
---

試想一下，如果你花了好幾個月熬夜完成的專案，其中所有的修改紀錄、過去的錯誤，甚至偶爾混入程式碼中的敏感設定資訊，都在你不知情的情況下被傳送到別人的伺服器，你會有什麼感覺？最近，AI 編碼工具「ZCode」的使用者之間就爆發了這樣的恐怖疑雲。

ZCode 是 Z.AI 以 GLM 模型為基礎所開發的官方桌面 AI 編碼代理工具 [[Source 4](https://www.digitalapplied.com/blog/zcode-glm-5-2-agentic-development-environment-guide), [Source 5](https://glm5.app/blog/glm-5-3-zcode)]。這款曾因功能便利而備受矚目的工具，如今因涉嫌在未經授權下傳輸使用者數據，在開發者社群中引發了巨大震撼。

### 為什麼這很重要？

你可能會想：「只不過是分享一些程式碼，有什麼關係？」但對開發者而言，Git（管理程式碼修改紀錄的系統）紀錄不僅僅是檔案那麼簡單。其中不僅包含專案的完整結構，還可能混有不小心包含的密碼、存取權杖（認證資訊）、個人開發習慣，甚至是企業內部機密。

在使用者未明確同意的情況下，將這些敏感數據傳送到外部伺服器，構成極其嚴重的安全威脅。特別是這次的疑雲顯示，即使是 UI 上提供的「禁止數據傳輸」開關，可能也無法正常運作，這從根本上摧毀了開發者對該工具的信任 [[Source 14](https://tokenstead.ai/guides/zcode-silent-git-history-upload)]。

### 簡單類比

如果用個比喻來說，就像你安裝了一個「智慧 AI 日記本 App」來幫助你寫日記。然而，當你在寫作的同時，這個 App 卻偷偷將你日記本後面隱藏的「舊日記」、甚至是已經撕掉丟棄的「便條紙碎片」全部複製，並送到了別人的倉庫裡。

根據鑑識審查（分析數位資訊以尋找證據的過程），ZCode 3.12.3 版本生成了一個高達 748 MiB 的加密快照。令人震驚的是，該數據中 98.9% 皆為 Git 相關資訊 [[Source 17](https://glbai.com/en/posts/zcode-silent-git-history-upload/)]。換句話說，它並非只擷取編碼過程中所需的部分，而是將你專案的整個足跡全盤帶走。

### 目前狀況？

最大的問題在於 ZCode 的態度。其官方隱私權政策僅表示會收集「對話中提交的文字、檔案與程式碼」，完全沒有提到會收集整個專案儲存庫或 Git 紀錄 [[Source 16](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)]。

目前已知的是，ZCode 會將使用者的工作區 (Workspace) 打包並加密，上傳至阿里雲 (Aliyun OSS) [[Source 1](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)]。甚至有些使用者是因為看到反覆出現的「上傳失敗」訊息，才發現了這種異常的傳輸行為 [[Source 16](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)]。

### 未來展望

這起事件再次將 AI 開發工具帶來的便利性背後所隱藏的「透明度」問題推上檯面。現在的開發者生活在一個不僅要評估工具性能，還必須詳細檢視該工具如何處理自己電腦（本地環境）數據的時代。

接下來我們將持續關注 Z.AI 是否會針對此事給出透明解釋並改進數據收集方式，還是會有許多開發者選擇轉向更安全的替代方案。在使用 AI 編碼工具時，務必養成檢查數據隱私設定與網路流量的習慣。

## 參考資料

1. [InsideZCode: Silently Uploading Your Entire Git History to the Cloud](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)
2. [ZCode Docs | GLM-5.3 Agentic Coding Guide](https://zcode.z.ai/en/docs/welcome)
3. [ZCode+GLM5.2 Tutorial - Stop Paying $200 for Claude Code](https://www.youtube.com/watch?v=7-evWQJ1Vlw)
4. [ZCode Explained: Z.ai's Agentic Dev Environment for GLM-5.2](https://www.digitalapplied.com/blog/zcode-glm-5-2-agentic-development-environment-guide)
5. [ZCode+GLM5.3: The Complete Guide to Z.AI's Coding Agent](https://glm5.app/blog/glm-5-3-zcode)
6. [Zcode Review 2026: Free AI Coding Agent With Goal Mode (vs Cursor)](https://www.bitdoze.com/zcode-ai-review/)
7. [GitHub - nothing1595/codex-zcode-bridge](https://github.com/nothing1595/codex-zcode-bridge)
8. [ZCode | Official Harness for GLM-5.3](https://zcode.z.ai/en)
9. [GLM5.2 бесплатно и БЕЗЛИМИТНО за 5 минут | Без карты в Zcode](https://www.youtube.com/watch?v=J3-lDiB-U8g)
10. [Claude Code vs Cursor vs ZCode: что выбрать в августе 2026](https://ip-calculator.ru/blog/artificial-intelligence/claude-code-vs-cursor-vs-zcode/)
11. [Революционный ZCode 3.0 — альтернатива Claude Code...](https://vc.ru/ai/3033535-zcode-3-0-alternativa-claude-code)
12. [What is GLM and how it can help you be more productive](https://sypalo.com/what-is-glm)
13. [OpenCode | The open source AI coding agent](https://opencode.ai/)
14. [ZCode uploads your git history; Z.ai holds the only key](https://tokenstead.ai/guides/zcode-silent-git-history-upload)
15. [ZCode, the GLM coding agent, silently uploads your Git history](https://news.ycombinator.com/item?id=49752422)
16. [ZCode AI Programming Tool Found to Upload Entire Git Repositories to Alibaba Cloud](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)
17. [Developers Asked Where ZCode Was Sending Their Git History](https://glbai.com/en/posts/zcode-silent-git-history-upload/)
18. [ZCode: what Z.ai's GLM-5.2 coding agent really is | eesel AI](https://www.eesel.ai/blog/zcode)
19. [Z.ai launches ZCode to turn GLM-5.2 into a coding-agent wedge](https://runtimewire.com/article/zai-zcode-glm-52-ai-coding-agent)