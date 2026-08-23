---
layout: post
title: "Pine Script - EMA"
description: "EMA // EMA 設定 shortEmaLength = input(5, \"Short EMA Length\") longEmaLength = input(20, \"Long EMA Length\") // EMA 計算 shortEma = ta.ema(close, shortEmaLength) l..."
date: 2023-12-07 02:45:21 +0900
section: blog
category: finance
lang: zh-tw
ref: 2023-12-07-legacy-314-finance-pine-script-ema
tags:
  - "Pine Script 教學"
  - "finance"
translation_source_hash: 386ca2039fb55706e7b1113d3af430ad066162c721df2abb58d9c67feeab31ea
---

<h2>
<b>
EMA
</b>
</h2>
<pre class="python">
<code>
// EMA 設定
shortEmaLength = input(5, "Short EMA Length")
longEmaLength = input(20, "Long EMA Length")

// EMA 計算
shortEma = ta.ema(close, shortEmaLength)
longEma = ta.ema(close, longEmaLength)
</code>
</pre>

<h2>
<b>
說明 (Description)
</b>
</h2>

<p>
<b>
shortEmaLength (短週期 EMA 長度)：
</b>
<br>
此行代碼為使用者建立一個輸入欄位，用來指定較短 EMA 的長度。
<br>
根據 `input(10, "Short EMA Length")` 所示，長度預設為 10 個週期。
<br>
由於「短」EMA 的週期較短，它對價格變化的反應比「長」EMA 更快。
</p>
<p>
<br>
<b>
longEmaLength (長週期 EMA 長度)：
</b>
<br>
同樣地，此行代碼為使用者建立一個輸入欄位，用來指定較長 EMA 的長度。
<br>
此 EMA 的預設長度設為 5 個週期 (`input(5, "Long EMA Length")`)。
<br>
週期較長的「長」EMA 與「短」EMA 相比，對價格變化的反應較慢，這能更平滑地呈現長期趨勢。
<br>
EMA 計算：
<br>
<br>
<b>
shortEma = ta.ema(close, shortEmaLength)：
</b>
此行根據資產的收盤價（close）以及 shortEmaLength 指定的長度來計算賣出 EMA。
</p>
<p>
<br>
<b>
longEma = ta.ema(close, longEmaLength)：
</b>
此行根據收盤價以及 longEmaLength 指定的長度來計算買入 EMA。
<br>
但有一點需要注意：命名規則似乎顛倒了。通常「短」EMA 會有較短的週期（天數），因此對近期價格波動較敏感；反之，「長」EMA 因為週期長，反應速度會變慢且更平滑。在該腳本中，短 EMA 被設定為比長 EMA（5）更長的週期（10），這與一般規則不符。為了清晰起見，可以交換這些數值或重新命名。
<br>
<br>
「短」EMA 通常應採用較小的數字（例如：5），以便對近期價格變化更敏感。
<br>
「長」EMA 應採用較大的數字（例如：10），這能使其更平滑，並降低對短期波動的敏感度。
</p>
<p>
<br>
這些 EMA 經常被同時使用，以識別潛在的趨勢方向或市場轉折點。例如，常見的交易策略包含觀察這兩條 EMA 的交叉。當短 EMA 上穿長 EMA 時，可視為看漲訊號；當下穿時，則視為看跌訊號。
</p>