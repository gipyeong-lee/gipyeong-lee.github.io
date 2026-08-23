---
layout: post
title: "Pine Script - RSI"
description: "RSI / RSI 設定 rsiLength = input(5, \"RSI Length\") rsiOverbought = input(80, \"RSI Overbought Level\") rsiOversold = input(20, \"RSI Oversold Level\") rsi = ta.rsi(..."
date: 2023-12-07 13:44:23 +0900
section: blog
category: finance
lang: zh-tw
ref: 2023-12-07-legacy-315-finance-pine-script-rsi
tags:
  - "Pine Script Tutorial"
  - "finance"
translation_source_hash: 0e2b121859cfb52077956ecfc5823b3ce8204423ae97ae4bf7482dc75fa3dd9c
---

<h2>
RSI
</h2>
<pre class="python">
<code>
/ RSI 設定
rsiLength = input(5, "RSI Length")
rsiOverbought = input(80, "RSI Overbought Level")
rsiOversold = input(20, "RSI Oversold Level")
rsi = ta.rsi(close, rsiLength)
</code>
</pre>

<h2>
Description
</h2>
<p>
<b>
rsiLength (RSI 長度)：
</b>
<br>
這是腳本中設定為 5 個週期的 RSI 計算長度。
<br>
定義了用於計算 RSI 的 K 線（或週期）數量。
<br>
長度越短（如 5），RSI 對近期價格變化就越敏感且反應越快，潛在的超買或超賣訊號會更頻繁地出現。
</p>
<p>
<br>
<b>
rsiOverbought (RSI 超買水準)：
</b>
<br>
在腳本中設定為 80，該數值代表資產被視為超買的閾值。
<br>
傳統上超買水準設定為 70，但設定為 80 會使超買標準更加嚴格，潛在優點是能減少錯誤訊號，但缺點是識別超買條件可能會延遲。
</p>
<p>
<br>
<b>
rsiOversold (RSI 超賣水準)：
</b>
<br>
設定為 20，該數值代表資產被視為超賣的閾值。
<br>
通常超賣水準設定為 30，但在腳本中設定為 20 會使標準變得更嚴格（類似於超買條件）。這樣可以減少錯誤的超賣訊號，但也可能導致實際超賣狀態的偵測延遲。
<br>
<b>
</b>
</p>

<p>
<b>
RSI 計算：
</b>
<br>
RSI 本身使用 ta.rsi(close, rsiLength) 函數進行計算。
<br>
該函數基於指定長度 (rsiLength) 的收盤價 (close) 來計算 RSI。
<br>
RSI 是一種用來衡量價格變動速度與變化的動能指標，在 0 到 100 之間震盪。一般來說，當 RSI 大於 70 時，表示資產可能超買（可能被高估）；當 RSI 小於 30 時，表示資產可能超賣（可能被低估）。
</p>

<h2>
Example
</h2>
<blockquote>
將策略應用於 3 分鐘 K 線圖時
</blockquote>

<p>
<b>
rsiLength (RSI 長度)：
</b>
<br>
將 rsiLength 設定為 5，RSI 將使用 3 分鐘圖表上的最後 5 根 K 線進行計算。
<br>
由於每根 K 線代表 3 分鐘，RSI 實際上分析了過去 15 分鐘的交易數據（5 根 K 線 × 每根 K 線 3 分鐘）。
<br>
這種相對較短的回顧週期使 RSI 對近期的價格變動反應極其靈敏，這對於在低時間週期的圖表（如 3 分鐘圖）上進行的短期交易決策非常適用。
</p>
<p>
<br>
<b>
rsiOverbought (RSI 超買水準)：
</b>
<br>
設定為 80，當 RSI 超過此水準時，資產即被視為超買。
<br>
在 3 分鐘圖上，若 RSI 超過 80，表示短期內有強勁的看漲動能。然而，這也暗示資產可能過度延伸，隨時可能面臨下跌或反轉。
</p>
<p>
<br>
<b>
rsiOversold (RSI 超賣水準)：
</b>
<br>
設定為 20，此水準表示當 RSI 低於該閾值時，資產被視為超賣。
<br>
在 3 分鐘圖上，若 RSI 低於 20，表示短期內有強勁的看跌動能，暗示資產可能被過度拋售，隨時可能出現反彈或反轉。
<br>
使用這些設定（5 個週期，80/20 閾值）在短週期（3 分鐘圖）使用 RSI，意味著專注於價格動能極快且短期的變化。這對於當沖交易者或試圖利用小型、快速價格波動的人來說可能很有用。然而，由於週期越短，市場的「雜訊」與錯誤訊號越多，因此通常建議搭配其他指標或方法來確認交易訊號。
<br>
<br>
與所有交易策略一樣，務必使用歷史數據對方法進行徹底的回測與驗證，以了解其潛在效率，並意識到短週期交易所帶來的相關風險。
</p>