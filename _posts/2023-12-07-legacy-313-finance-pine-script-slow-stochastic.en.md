---
layout: post
title: "Pine Script - Slow Stochastic"
description: "Slow Stochastic // Slow Stochastic settings slowStochKLength = input(7, \"Slow Stochastic %K Length\") slowStochDLength = input(6, \"Slow Stochastic %D Length\") stoch..."
date: 2023-12-07 02:31:19 +0900
section: blog
category: finance
lang: en
ref: 2023-12-07-legacy-313-finance-pine-script-slow-stochastic
tags:
  - "tradingview"
  - "Slow"
  - "auto"
  - "pine"
  - "Pine Script Tutorial"
  - "finance"
translation_source_hash: 966c008257615c760ac6b53d3da1d51465841fa816088c16e32e1dd6422f5ebd
---

<div>
<h2>
<b>
<span>
Slow Stochastic
</span>
</b>
</h2>
</div>
<pre class="python">
<code>
// Slow Stochastic settings
slowStochKLength = input(7, "Slow Stochastic %K Length")
slowStochDLength = input(6, "Slow Stochastic %D Length")
stochUpper = input(70, "Upper Level")
stochLower = input(30, "Lower Level")
// Slow Stochastic calculation
slowStochK = ta.sma(ta.stoch(close, high, low, slowStochKLength), slowStochDLength)
slowStochD = ta.sma(slowStochK, slowStochDLength)
</code>
</pre>
<h2>
<b>
Description
</b>
</h2>
<p>
<b>
SlowStochKLength:
</b>
<br>
This parameter defines the length of the Stochastic %K line for the Slow Stochastic oscillator.
<br>
It determines the number of periods used to calculate the %K line.
<br>
Increasing this length makes the %K line smoother and less sensitive to recent price changes, potentially leading to fewer but potentially more reliable signals. Decreasing the length makes the %K line more responsive to recent price changes, increasing the number of signals but also potentially increasing the number of false signals.
</p>
<p>
<br>
<b>
SlowStochDLength:
</b>
<br>
This parameter sets the length of the moving average applied to the %K line to calculate the %D line in the Slow Stochastic oscillator.
<br>
The %D line is a moving average of the %K line, which serves to provide a smoothed signal and identify potential trend reversals.
<br>
A longer %D length provides a smoother line, which can help in identifying more significant trends but may result in signal lag. A shorter length increases the line's responsiveness but may increase the risk of false signals.
<br>
<b>
</b>
</p>

<p>
<b>
stochUpper:
</b>
<br>
This is the upper threshold level for the Stochastic oscillator.
<br>
If the Stochastic line rises above this level, the asset may be considered overbought. Traders often interpret this as a potential sell signal or an indication that the asset price may soon decline.
</p>

<p>
<b>
stochLower:
</b>
<br>
This is the lower threshold level for the Stochastic oscillator.
<br>
If the Stochastic line falls below this level, the asset may be considered oversold. This is often seen as a potential buy signal or an indication that the asset price may soon rise.
</p>