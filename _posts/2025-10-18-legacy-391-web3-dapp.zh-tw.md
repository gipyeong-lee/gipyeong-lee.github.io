---
layout: post
title: "我完成了生平第一個 Dapp。"
description: "你好？我是 Slow Thinking。我進行了大約一個月的開發。如果沒有 AI，我可能無法完成。我這個懶人選擇的方法如下。在 Visual Studio Code 的左右面板分別設置 Codex 和 Claude Code。當遇到 Token 限制時，就輪流切換使用。以下是我對這兩個工具的比較表，請參考。"
date: 2025-10-18 20:57:34 +0900
section: blog
category: web3
lang: zh-tw
ref: 2025-10-18-legacy-391-web3-dapp
tags:
  - "Ai"
  - "Claude"
  - "Codex"
  - "DAPP"
  - "Project"
  - "Projects"
translation_source_hash: 80e0e93d306232af16e6f6d408598d3b9b8be3d0a9bae18b179452ac9bae1aa4
---

<p>
你好？我是 Slow Thinking。
</p>
<p>
我進行了大約一個月的開發。
</p>
<p>
如果沒有 AI，我可能無法完成。
</p>
<p>
我這個懶人選擇的方法如下。
</p>

<p>
在 Visual Studio Code 的左右面板分別設置 Codex 和 Claude Code。
</p>
<p>
當遇到 Token 限制時，就輪流切換使用。以下是我對這兩個工具的比較表，請參考。
</p>

<table>
<tbody>
<tr>
<td>
<b>
項目
</b>
</td>
<td>
<b>
Codex CLI ( OpenAI )
</b>
</td>
<td>
<b>
Claude Code CLI (Anthropic)
</b>
</td>
</tr>
<tr>
<td>
<b>
方案名稱
</b>
</td>
<td>
包含在 ChatGPT Plus (每月 $20) 內
</td>
<td>
Claude Pro (每月 $20)
</td>
</tr>
<tr>
<td>
<b>
會話限制方式
</b>
</td>
<td>
約
<b>
5 小時滾動視窗
</b>
(每 5 小時重置使用量)
</td>
<td>
約
<b>
5 小時滾動視窗
</b>
(每 5 小時重置)
</td>
</tr>
<tr>
<td>
<b>
會話額度 (概略)
</b>
</td>
<td>
30 ~ 150 條本地訊息或 5 ~ 40 個雲端任務
</td>
<td>
約 45 條訊息或 10 ~ 40 個提示等級
</td>
</tr>
<tr>
<td>
<b>
每週累計額度
</b>
</td>
<td>
存在
<b>
共享每週配額 (weekly quota)
</b>
(官方數據未公開)
</td>
<td>
存在約
<b>
每 7 天
</b>
重置的每週額度
</td>
</tr>
<tr>
<td>
<b>
重置時間點 (會話)
</b>
</td>
<td>
首次請求後 5 小時自動重置
</td>
<td>
首次提示後 5 小時自動重置
</td>
</tr>
<tr>
<td>
<b>
重置時間點 (每週)
</b>
</td>
<td>
約以
<b>
一週
</b>
為週期重置 (精確時間未公開)
</td>
<td>
約
<b>
7 天
</b>
後重置 (依帳號時間有所不同)
</td>
</tr>
<tr>
<td>
<b>
Token 上下文窗口
</b>
</td>
<td>
約
<b>
192,000 Token
</b>
(估計為輸入 + 輸出 + 歷史記錄總和)
</td>
<td>
約
<b>
200,000 Token
</b>
(Pro 標準) 最高 500,000 (Enterprise)
</td>
</tr>
<tr>
<td>
<b>
基礎模型
</b>
</td>
<td>
GPT-4 Turbo (程式碼解讀模式)
</td>
<td>
Claude 3 Sonnet (程式碼編寫模式)
</td>
</tr>
<tr>
<td>
<b>
超額時訊息
</b>
</td>
<td>
“Usage limit reached. Try again in X hours.”
</td>
<td>
“You’ve hit your limit. Resets in ~X hours.”
</td>
</tr>
<tr>
<td>
<b>
重置方式
</b>
</td>
<td>
自動滾動重置 (無法手動初始化)
</td>
<td>
自動滾動重置 (5 小時後會話更新)
</td>
</tr>
<tr>
<td>
<b>
額外特徵
</b>
</td>
<td>
- 區分本地 vs 雲端任務 - 包含程式碼執行功能
</td>
<td>
- 可透過 /clear, /compact 指令縮減上下文 - 支援以 Sonnet 4 為核心的模型
</td>
</tr>
<tr>
<td>
<b>
官方來源範例
</b>
</td>
<td>
<a href="https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan">
help.openai.com
</a>
</td>
<td>
<a href="https://claudelog.com/faqs/claude-code-usage/">
claudelog.com
</a>
/
<a href="https://portkey.ai/blog/claude-code-limits/">
portkey.ai
</a>
</td>
</tr>
</tbody>
</table>

<p>
以下是關於這次 Project L 的資訊。
</p>


<table>
<tbody>
<tr>
<td>
<b>
專案名稱
</b>
</td>
<td>
Project L
</td>
</tr>
<tr>
<td>
<b>
開發語言
</b>
</td>
<td>
Rust (鏈上程式) + TypeScript (客戶端 / 前端)
</td>
</tr>
<tr>
<td>
<b>
平台
</b>
</td>
<td>
Solana Blockchain (Anchor Framework)
</td>
</tr>
<tr>
<td>
<b>
開發期間
</b>
</td>
<td>
2025.09.29 ~ 2025.10.18 (共 19 天，38 小時)
</td>
</tr>
<tr>
<td>
<b>
主要目標
</b>
</td>
<td>
完成 Solana 網路上的智能合約部署及客戶端連動
</td>
</tr>
<tr>
<td>
<b>
依賴關係圖
</b>
</td>
<td>
共 2,130 個依賴項 (包含套件、模組、建置依賴)
</td>
</tr>
</tbody>
</table>

<p>
開發已經完成，目前正在進行自我 QA (品質保證)。
</p>
<p>
之後預計進行發布。
</p>

<hr>

<blockquote>
<s>
devnet QA - 已完成
</s>
<br>
testnet QA -
<b>
進行中
</b>
<br>
Deploy on mainnet  - 待辦
</blockquote>