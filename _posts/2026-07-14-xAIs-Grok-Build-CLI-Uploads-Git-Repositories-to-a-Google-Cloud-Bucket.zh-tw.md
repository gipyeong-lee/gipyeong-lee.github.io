---
layout: post
title: "我的程式碼竟被偷偷傳送至 AI 伺服器？「Grok Build」安全爭議始末"
description: "開發者愛用的 xAI Grok Build CLI 工具被踢爆，會在未經使用者同意下，將整個程式碼儲存庫偷偷傳送至遠端伺服器。"
summary: "xAI 的「Grok Build」工具遭證實會在未經授權的情況下，自動將所有程式碼與敏感資訊上傳至雲端伺服器，引發軒然大波。"
tags: [AI, 安全, Grok, xAI, 開發者]
image: 2026-07-14-xAIs-Grok-Build-CLI-Uploads-Git-Repositories-to-a-Google-Cloud-Bucket.jpg
image_alt: "數位藝術：象徵資料從電腦螢幕外洩至雲端"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企業級解決方案的核心在於「信任」。此次事件再次證明，缺乏透明度的資料收集行為，會瞬間摧毀使用者建立的信任，這是極為慘痛的教訓。"
quiz:
  - question: "此次安全分析揭露了「Grok Build」的什麼問題？"
    choices: ["只會傳送使用者指示讀取的檔案", "會在未經使用者允許下，上傳整個 Git 儲存庫與敏感設定值", "會加密資料並安全地儲存"]
    answer: 1
    explanation: "分析結果顯示，該工具會自動將包含使用者未明確指定讀取的檔案，以及敏感安全金鑰在內的整個儲存庫，上傳至雲端伺服器。"
  - question: "目前這項資料傳送問題處理得如何了？"
    choices: ["經查證沒有任何問題", "xAI 已正式發表道歉聲明", "公開後似乎已透過伺服器端設定中止傳送"]
    answer: 2
    explanation: "據悉目前已透過伺服器端設定中止傳送，但 xAI 尚未針對資料保存與刪除政策發表任何正式回應。"
  - question: "開發者需注意的最大風險是什麼？"
    choices: ["電腦速度會變慢", "環境變數 (.env) 中包含的敏感 API 金鑰等可能外洩", "Git 紀錄會被刪除"]
    answer: 1
    explanation: "該工具會將包含敏感資訊在內的所有環境設定檔（如 .env）一併傳送至伺服器，這可能導致嚴重安全風險。"
lang: zh-tw
ref: 2026-07-14-xAIs-Grok-Build-CLI-Uploads-Git-Repositories-to-a-Google-Cloud-Bucket
---

試想一下，你把家裡的密碼寫在紙條上收進抽屜深處，結果一請清潔服務，清潔工竟然把抽屜裡的所有東西通通打包，帶回他們公司的金庫。

最近，許多開發者在使用的 AI 程式輔助工具——xAI 的「Grok Build CLI」，就被發現存在類似的安全隱患，引發了強烈爭議。根據 [AI Weekly](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored) 的報導，儘管該工具主打「本機優先（local-first，指直接在使用者電腦上執行）」的行銷口號，但實際上卻會將使用者的完整 Git 儲存庫內容，偷偷傳送至特定雲端伺服器。

## 這件事為何如此重要？

問題的嚴重性不僅僅在於「程式碼被拿走了一點」。這意味著公司內部的程式碼、包含客戶個資的敏感檔案，甚至是用於服務連線的「私密金鑰（如 .env 檔案等）」，都通通傳送到了 AI 公司的伺服器上。 [byteiota](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/) 指出，該工具甚至會掃描並上傳使用者根本不想讓 AI 讀取的檔案。

對開發者而言，程式碼既是資產也是智慧財產。這種未經授權的資料收集行為，直接違反了企業安全政策；若這些資訊遭到駭客攻擊或外洩，後果將不堪設想。 [GIGAZINE](https://gigazine.net/gsc_news/en/20260713-grok-build-sending-data/) 認為，最嚴重的問題在於該工具在沒有取得使用者明確同意的情況下，就擅自蒐集了程式碼。

## 簡單來說

用個比喻來解釋這個現象：假設你使用一款修圖軟體，只想挑選一張照片進行編輯，但這個應用程式每打開一張照片，就會把手機裡「所有的照片」都複製一份並傳送到雲端伺服器。根據 [GitHub 的安全分析結果](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547)，Grok Build 工具無論 AI 是否為了工作而讀取檔案，它都會將工作目錄中的所有檔案及整個 Git 歷史紀錄，上傳至名為「grok-code-session-traces」的雲端儲存空間。 [Hasty Briefs](https://hb.int2inf.com/en/s/item/A8Cux9a7WKyFuJcdKfPNER-Grok-Build-CLI-data-exfiltration-analysis) 更分析指出，過程中連敏感的安全金鑰也會經由另一個管道一併被傳送出去。

## 我們現在處於什麼狀態？

隨著安全專家的分析與公開揭露，[國際網路文摘 (International Cyber Digest)](https://x.com/IntCyberDigest/status/2076689215258014069) 表示，目前該上傳行為似乎已透過伺服器端的設定中止。然而，使用者依然感到惶惶不安。因為 xAI 對於這些資料為何被收集、如何被收集，以及是否已安全刪除伺服器上殘留的程式碼等問題，至今未給出任何正式回應。 [ABAB News](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc) 也提到，使用者的憂慮正持續擴大。

## 未來會如何發展？

此次事件將成為一個契機，未來開發者在引入外部 AI 工具時，勢必會執行更嚴格的安全審核程序。目前已有像是 [wetlink](https://github.com/wetlink/grok-build-privacy-hardening) 等開源專案，主動開發「斷路器（kill switch，當問題發生時可強制停用功能的保護裝置）」來進行防禦。企業日後在導入 AI 工具時，勢必會強化內部安全稽核，而像 xAI 這樣的服務供應商，若無法證明其透明度，恐怕很難重拾使用者的信任。

## MindTickleBytes AI 記者觀點

技術雖然便利，但若不知道背後交換了什麼樣的資料，對使用者而言始終是巨大的風險。特別是處理程式碼這類核心資產的工具，必須建立在「信任」的基礎上。xAI 應針對此次事件進行更透明的溝通，並對使用者的程式碼負起應有的責任。

## 參考資料

1. [xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored | AI Weekly](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)
2. [What xAI Grok Build CLI actually sends to xAI - a wire-level analysis (grok 0.2.93) · GitHub](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547)
3. [International Cyber Digest on X: "‼️ BREAKING: xAI's Grok Build CLI was uploading entire Git repositories to a Google Cloud bucket, private codebases and unredacted secrets included..."](https://x.com/IntCyberDigest/status/2076689215258014069)
4. [Grok Build CLI Uploads Your Entire Repo to xAI Servers | byteiota](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)
5. [Grok Build CLI Exposed for Uploading Complete Repositories and Sensitive Files - ABAB News](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
6. [GitHub - cereblab/grok-build-exfil-repro](https://github.com/cereblab/grok-build-exfil-repro)
7. [Grok Build CLI Repository Uploads, What the Wire Capture Proved](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)
10. [GitHub Gist](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547.pibb)
11. [What xAI's Grok Build CLI Actually Sends to xAI | Hasty Briefs](https://hb.int2inf.com/en/s/item/A8Cux9a7WKyFuJcdKfPNER-Grok-Build-CLI-data-exfiltration-analysis)
12. [xAI's Grok CLI Reportedly Uploads User Codebases and Keys ...](https://cb-terminal.dev/en/topic/6d9cba8e-8783-476a-92e5-f604bda29091)
13. [Investigations reveal that Grok Build transmitted... - GIGAZINE](https://gigazine.net/gsc_news/en/20260713-grok-build-sending-data/)
14. [wetlink/grok-build-privacy-hardening](https://github.com/wetlink/grok-build-privacy-hardening)