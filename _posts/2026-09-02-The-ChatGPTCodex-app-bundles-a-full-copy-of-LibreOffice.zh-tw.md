---
layout: post
title: "電腦中隱藏的巨人：為什麼 ChatGPT 應用程式內建了 LibreOffice？"
description: "探討近期發現的 ChatGPT 桌面應用程式中 1.7GB 的巨大套件，以及隱藏其中的 LibreOffice 與開發工具。"
summary: "OpenAI 的 ChatGPT 桌面應用程式被發現，在安裝過程中隱藏了一個高達 1.7GB 的外部軟體套件。"
tags: [ChatGPT, OpenAI, 軟體, LibreOffice, 技術新聞]
image: 2026-09-02-The-ChatGPTCodex-app-bundles-a-full-copy-of-LibreOffice.jpg
image_alt: "顯示 ChatGPT 應用程式內部資料夾結構的抽象圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "ChatGPT 原本被視為單純的聊天應用，但其內建強大的開發與文件處理引擎，這點令人非常感興趣。這顯示 AI 正超越單純的對話夥伴，演變成能在使用者電腦中執行實質「任務」的代理人 (Agent)。"
quiz:
  - question: "ChatGPT 桌面應用程式內 'codex-primary-runtime' 資料夾的容量為多少？"
    choices: ["170MB", "1.7GB", "17GB"]
    answer: 1
    explanation: "該資料夾包含約 1.7GB 的軟體套件。"
  - question: "此套件中不包含下列哪項軟體？"
    choices: ["Python", "Node.js", "Microsoft Word"]
    answer: 2
    explanation: "套件中包含 Python、Node.js 與 LibreOffice 等，但未包含 MS Word。"
  - question: "為什麼該應用程式會隨附安裝像 LibreOffice 這類外部工具？"
    choices: ["純屬容量浪費", "為了活用內部工具進行文件作業", "無法刪除的函式庫"]
    answer: 1
    explanation: "透過隨附的技術文件，AI 能學習如何搜尋並活用這些二進位檔案。"
lang: zh-tw
ref: 2026-09-02-The-ChatGPTCodex-app-bundles-a-full-copy-of-LibreOffice
---

## ChatGPT，跨越對話夥伴的角色，開始自備「工具」

想像一下，剛買的新智慧型手機本以為只預裝了基礎應用，結果發現應用程式資料夾深處，竟然整套內建了數十本食譜和一整箱工具。近期 OpenAI 的桌面應用程式（前身為 Codex，現已更名為 ChatGPT）就發生了這樣的事情。[出處 1](https://simonwillison.net/2026/Sep/1/codex-libreoffice/), [出處 4](https://x.com/simonw/status/2094864223683903800)

在這個原本以為只是單純聊天視窗的應用程式內部，精確地說是在 `~/.cache` 資料夾下，有個名為 `codex-primary-runtime` 的神祕空間，隱藏了高達 1.7GB 的巨大軟體套件。[出處 3](https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache), [出處 5](https://news.ycombinator.com/item?id=49527396)

## 這為何重要？

身為使用者，或許會感到驚訝：「竟然佔用我這麼多電腦空間？」但這個現象是一個重要的訊號，顯示 AI 正從單純的「會說話的鸚鵡」轉變為「協助處理實務的解題者」。過去的 AI 僅止於回答提問，現在則試圖直接操控安裝在您電腦中的工具（如 Python、文件編輯器等），進而產出實際的成果。

## 淺顯易懂：AI 的「工具箱」

用簡單的比喻來說明：假設您雇了一位廚師（AI）。以前的廚師只會用說的告訴您食譜，但現在的廚師直接進入您的廚房，翻開食譜（LibreOffice），直接動手使用刀具與瓦斯爐（Python, Node.js），已經準備好要親手做出一道料理。

實際上，這個套件內不僅包含了 Python（電腦語言執行工具）與 Node.js（網頁技術執行工具）的完整安裝檔，還包含了 LibreOffice（開源文件編輯軟體）以及用於文件轉換的 Poppler 等工具。[出處 1](https://simonwillison.net/2026/Sep/1/codex-libreoffice/), [出處 2](https://zeli.app/story/49527396) 有趣的是，應用程式內部還另外存在一份「使用說明書（Skills）」，記錄了該如何運用這些龐大的工具。[出處 3](https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache)

LibreOffice 是全球無數志工共同製作的免費文件處理軟體，提供了一個任何人都能研究其運作原理並進行改良的開放環境。[出處 7](https://www.libreoffice.org/) OpenAI 正是透過在應用程式中預先「植入」這些工具，建立了一套讓 AI 在接收指令後，能毫無延遲地執行外部程式的環境。

## 現況

目前該功能透過 ChatGPT 桌面應用程式實現。[出處 8](https://github.com/openai/codex) 使用者表面上使用的是普通的對話介面，但後端其實有這一大套工具群組在等待 AI 的指令。[出處 9](https://filecr.com/windows/openai-codex/) 當然，這種強制綁定軟體的方式，對部分使用者而言可能會被視為浪費電腦資源。安全性分析師與開發者對這些隱藏檔案表示驚訝。[出處 5](https://news.ycombinator.com/item?id=49527396)

## 未來發展

AI 隨身攜帶工具箱的方式未來將會更加普及。因為這正標誌著「代理人（Agent）」時代的正式來臨——AI 不再只是生成回答，而是能在使用者的電腦內編輯文件檔、編譯程式碼以及分析數據。[出處 6](https://github.com/hashgraph-online/awesome-codex-plugins) 未來，您可能不只是與 AI 對話，而是會親眼看見 AI 直接開啟您電腦裡的 LibreOffice，幫您撰寫報告。

## MindTickleBytes AI 記者觀點

AI 變得聰明，意味著 AI 能操作的工具範圍正在擴大。ChatGPT 內建 LibreOffice，是 AI 從單純的知識儲存庫，轉而深度滲入我們實際生產環境的強而有力的證據。

## 參考資料

1. Codex bundles LibreOffice - [https://simonwillison.net/2026/Sep/1/codex-libreoffice/](https://simonwillison.net/2026/Sep/1/codex-libreoffice/)
2. Codex bundles LibreOffice — The ChatGPT/Codex app bundles a ... - [https://zeli.app/story/49527396](https://zeli.app/story/49527396)
3. OpenAI Codex app bundles LibreOffice, Python, Node in 1.7GB ... - [https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache](https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache)
4. Simon Willison on X: "Just noticed the ChatGPT desktop app ... - [https://x.com/simonw/status/2094864223683903800](https://x.com/simonw/status/2094864223683903800)
5. The ChatGPT/Codex app bundles a full copy of LibreOffice ... - [https://news.ycombinator.com/item?id=49527396](https://news.ycombinator.com/item?id=49527396)
6. GitHub - hashgraph-online/awesome-codex-plugins: A curated ... - [https://github.com/hashgraph-online/awesome-codex-plugins](https://github.com/hashgraph-online/awesome-codex-plugins)
7. Free and private office suite, no forced AI — LibreOffice - [https://www.libreoffice.org/](https://www.libreoffice.org/)
8. GitHub - openai/codex: Lightweight coding agent that runs in your... - [https://github.com/openai/codex](https://github.com/openai/codex)
9. OpenAI ChatGPT(With Codex) Download (Latest 2026) - FileCR - [https://filecr.com/windows/openai-codex/](https://filecr.com/windows/openai-codex/)