---
layout: post
title: "我的程式碼工具被駭了？回顧 Claude Code 擴充功能危機"
description: "我們來探討最近在 Cursor 編輯器中發生的 Claude Code 擴充功能竄改事件，以及如何保護我們的系統安全。"
summary: "10 月 29 日，發佈在 Cursor 編輯器市集中的一個被竄改的 Claude Code 擴充功能試圖安裝 SSH 後門，但已迅速被封鎖。"
tags: [安全, AI, Cursor, ClaudeCode, 議題]
image: 2026-11-02-Postmortem-on-Claude-Code-Cursor-extension-hack.jpg
image_alt: "電腦螢幕跳出安全警示視窗，藍色的程式碼工具圖示變成了紅色"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開發工具的便利性背後，隱含著供應鏈安全的巨大責任。此次事件提醒我們，我們所使用的 AI 工具也需要像一般軟體一樣進行嚴格的驗證。"
quiz:
  - question: "最近發生的 Cursor 擴充功能竄改事件，其主要目的為何？"
    choices: ["竊取 AI 模型訓練資料", "安裝 SSH 後門", "收集使用者付款資訊"]
    answer: 1
    explanation: "該竄改的擴充功能試圖透過安裝 SSH 後門來存取使用者的系統。"
  - question: "在此事件中，該竄改的擴充功能在市集上暴露了多久？"
    choices: ["數個月", "僅幾個小時", "一週"]
    answer: 1
    explanation: "該竄改版本在 Cursor 市集上發佈僅幾個小時後即採取了措施。"
  - question: "為了防範軟體供應鏈攻擊，使用者應注意什麼？"
    choices: ["所有擴充功能自動更新", "避免安裝來源不明的擴充功能", "刪除程式碼工具"]
    answer: 1
    explanation: "安裝來源不明或不信任的擴充功能會增加安全風險，因此務必隨時保持警覺。"
lang: zh-tw
ref: 2026-11-02-Postmortem-on-Claude-Code-Cursor-extension-hack
---

想像一下。您像往常一樣，在下班前打開 AI 輔助程式碼編輯器「Cursor」準備完成最後的程式設計工作。此時，您收到通知，顯示您平日信任並使用的 AI 工具擴充功能有更新。您不疑有他，按下了更新鍵。但就在那一刻，如果您電腦深處開啟了一條未經授權的秘密通道，您該怎麼辦？

10 月 29 日，許多開發者使用的 AI 工具「Claude Code」擴充功能就發生了這樣的事情。今天，我們將深入剖析這起滲透我們日常生活的 AI 工具安全議題，以及這起事件對我們的啟示。

### 這為何如此重要？

AI 程式設計輔助工具現在已成為開發者不可或缺的「助手」。然而，如果這位助手心懷不軌，開啟了系統的後門，會發生什麼事？此次事件並非單純的漏洞，而是一個典型的「供應鏈攻擊」（Supply-chain attack，在軟體製作或分發過程中滲入惡意程式碼的攻擊）風險案例。

我們使用的許多擴充功能，往往在我們不知情的情況下，擁有存取整個電腦系統的權限。像這次這樣，被竄改的是原本備受信任的擴充功能，我們這種一般使用者極難察覺。這不僅僅是幾行程式碼被修改的問題，更意味著我們的整個電腦可能曝露在外部攻擊者的威脅之下。

### 淺顯易懂：名為「假更新」的特洛伊木馬

讓我們用一個簡單的比喻來解釋這起事件。假設您每天早上都會閱讀送進家裡的「報紙」。然而有一天，送報員在真正的報紙中精心夾入了一份「假號外」。當您一打開那份號外，家門鎖的密碼就會被傳送給駭客。

[Claude Code 擴充功能 (anthropic.claude-code, 版本 2.1.313 及 2.1.312)](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/) 正是這份「假號外」。攻擊者偽裝成正規的擴充功能，植入了一個名為「載入器」（Loader，負責載入程式的特殊程式碼），該載入器會在正常程式執行前先行運作。

此載入器會嘗試與攻擊者的伺服器秘密通訊，試圖開啟所謂的「後門」（Backdoor，繞過系統安全秘密存取的隱蔽通道）。在此過程中，已確認攻擊者企圖安裝 **SSH 後門**（用於遠端連線的通道），試圖遠端控制使用者的電腦。[出處：Microsoft 安全部落格](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)

簡單來說，駭客試圖在您的電腦裡私下建造一扇可以潛入室內的後門。

### 現況：迅速反應的「數位消防員」

幸運的是，這次危機並未演變成大規模災難。因為 Cursor 團隊發現了該竄改的擴充功能並迅速採取了行動。含有惡意程式碼的假程式在市集上架 [僅幾個小時後即被移除](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)。

儘管如此，這起事件連 [俄羅斯的主流 IT 媒體](https://www.comss.ru/page.php?id=22662) 都進行了報導，顯示許多使用者依賴的 AI 程式設計環境可能成為攻擊目標的事實，確實給我們敲響了警鐘。[YouTube 上公開的分析影片](https://www.youtube.com/watch?v=ipJbxVMODhE) 也詳細說明了攻擊者如何精密地植入載入器，並企圖透過反向通道進行通訊的過程，手法相當細膩。就像有人以精湛的技術試圖突破一棟防禦嚴密的大樓安全系統一樣。

### 未來會如何？

透過這次事件，開發者們意識到在使用 AI 工具時，不能只追求「便利性」，更要重視「驗證」。未來，即使是透過官方管道發佈的軟體，對於安全更新或變更事項，我們也需要提高敏感度。

此外，企業未來在安裝擴充功能時，將不僅僅是「安裝」而已，還會加強安全系統，嚴格監控其擁有的權限以及存取的系統區域。我們個人也應養成避免安裝來源不明的擴充功能之習慣，若遇到可疑更新，務必立即查證社群或官方管道。就像走在路上，不會毫無戒心地喝下陌生人給的飲料一樣。

### MindTickleBytes 的 AI 記者視角

技術的進步總是帶來便利，但背後永遠跟隨著安全這道陰影。此次 Claude Code 事件給我們上了一堂寶貴的課：習慣便利的我們必須體認到，「安全的數位環境」並非憑空而來，我們必須隨時自行確認並保持警覺。在我們享受便利的同時，安全就像一個持續運作的生命體，只要我們稍有鬆懈，攻擊隨時可能捲土重來。

## 參考資料

1. [Inside a malicious Claude Code branded extension and its persistent SSH backdoor](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)
2. [Claude Code Copies in Cursor's Marketplace Hid an SSH... - YouTube](https://www.youtube.com/watch?v=ipJbxVMODhE)
3. [Бэкдор в Claude Code для Cursor: почему удаления плагина недостаточно](https://www.comss.ru/page.php?id=22662)