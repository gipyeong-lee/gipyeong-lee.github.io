---
layout: post
title: "Pine Script - Slow Stochastic (慢速隨機指標)"
description: "Slow Stochastic // Slow Stochastic 設定 slowStochKLength = input(7, \"Slow Stochastic %K 長度\") slowStochDLength = input(6, \"Slow Stochastic %D 長度\") stoch..."
date: 2023-12-07 02:31:19 +0900
section: blog
category: finance
lang: zh-tw
ref: 2023-12-07-legacy-313-finance-pine-script-slow-stochastic
tags:
  - "tradingview"
  - "Slow"
  - "auto"
  - "pine"
  - "Pine Script 教學"
  - "finance"
translation_source_hash: 966c008257615c760ac6b53d3da1d51465841fa816088c16e32e1dd6422f5ebd
---

<div>
<h2>
<b>
<span>
Slow Stochastic (慢速隨機指標)
</span>
</b>
</h2>
</div>
<pre class="python">
<code>
// Slow Stochastic 設定
slowStochKLength = input(7, "Slow Stochastic %K 長度")
slowStochDLength = input(6, "Slow Stochastic %D 長度")
stochUpper = input(70, "超買區間 (Upper Level)")
stochLower = input(30, "超賣區間 (Lower Level)")
// Slow Stochastic 計算
slowStochK = ta.sma(ta.stoch(close, high, low, slowStochKLength), slowStochDLength)
slowStochD = ta.sma(slowStochK, slowStochDLength)
</code>
</pre>
<h2>
<b>
說明 (Description)
</b>
</h2>
<p>
<b>
SlowStochKLength (慢速隨機指標 %K 長度)：
</b>
<br>
此參數定義了慢速隨機震盪指標中 %K 線的長度。
<br>
它決定了計算 %K 線所使用的期間數量。
<br>
增加此長度會使 %K 線更平滑，對近期的價格變動較不敏感，這可能導致訊號數量減少，但相對更穩定。縮短長度則會使 %K 線對近期價格變動反應更靈敏，雖增加了訊號數量，但也可能增加誤訊號的次數。
</p>
<p>
<br>
<b>
SlowStochDLength (慢速隨機指標 %D 長度)：
</b>
<br>
此參數設定應用於 %K 線的移動平均長度，用於計算慢速隨機震盪指標中的 %D 線。
<br>
%D 線是 %K 線的移動平均，具有提供平滑訊號及識別潛在趨勢反轉的作用。
<br>
%D 長度越長，產生的線條越平滑，有助於識別更重要的趨勢，但可能會導致訊號延遲。長度越短，線條的反應性越高，但誤訊號的風險也隨之提高。
<br>
<b>
</b>
</p>

<p>
<b>
stochUpper (超買區間)：
</b>
<br>
這是隨機震盪指標的上限臨界值。
<br>
當隨機指標線升至此水平之上時，該資產可能被視為「超買」。交易者通常將其解讀為潛在的賣出訊號，或是資產價格即將下跌的預兆。
</p>

<p>
<b>
stochLower (超賣區間)：
</b>
<br>
這是隨機震盪指標的下限臨界值。
<br>
當隨機指標線跌至此水平之下時，該資產可能被視為「超賣」。這通常被視為潛在的買入訊號，或是資產價格即將上漲的指標。
</p>