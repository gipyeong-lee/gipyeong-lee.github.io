---
layout: post
title: "Pine Script - EMA"
description: "EMA // EMA Settings shortEmaLength = input(5, \"Short EMA Length\") longEmaLength = input(20, \"Long EMA Length\") // EMA Calculation shortEma = ta.ema(close, shortEmaLength) l..."
date: 2023-12-07 02:45:21 +0900
section: blog
category: finance
lang: en
ref: 2023-12-07-legacy-314-finance-pine-script-ema
tags:
  - "Pine Script Tutorial"
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
// EMA Settings
shortEmaLength = input(5, "Short EMA Length")
longEmaLength = input(20, "Long EMA Length")

// EMA Calculation
shortEma = ta.ema(close, shortEmaLength)
longEma = ta.ema(close, longEmaLength)
</code>
</pre>

<h2>
<b>
Description
</b>
</h2>

<p>
<b>
shortEmaLength:
</b>
<br>
This line creates an input that allows the user to specify the length of the shorter EMA.
<br>
The length is set to a default of 10 periods, as indicated in input(10, "Short EMA Length").
<br>
Because of its shorter length, the 'short' EMA reacts faster to price changes than the 'long' EMA.
</p>
<p>
<br>
<b>
longEmaLength:
</b>
<br>
Similarly, this line creates an input that allows the user to specify the length of the longer EMA.
<br>
The default length for this EMA is set to 5 periods (input(5, "Long EMA Length")).
<br>
The 'long' EMA, with its longer period, reacts more slowly to price changes compared to the 'short' EMA. This results in a smoother representation of the trend over a longer timeframe.
<br>
EMA Calculation:
<br>
<br>
<b>
shortEma = ta.ema(close, shortEmaLength):
</b>
This line calculates the short EMA based on the asset's closing price and the length specified in shortEmaLength.
</p>
<p>
<br>
<b>
longEma = ta.ema(close, longEmaLength):
</b>
This line calculates the long EMA based on the closing price and the length specified in longEmaLength.
<br>
However, there is an important point to note: the naming convention appears to be reversed. Generally, a "short" EMA has a shorter period (number of days), making it more sensitive to recent price fluctuations. Conversely, a "long" EMA has a longer period, resulting in a slower and smoother reaction. In the script, the short EMA is set with a longer period (10) than the long EMA (5), which goes against standard rules. For clarity, you may want to swap these values or rename them.
<br>
<br>
A "short" EMA typically has a smaller number (e.g., 5), making it more sensitive to recent price changes.
<br>
A "long" EMA should have a larger number (e.g., 10), making it smoother and less sensitive to short-term fluctuations.
</p>
<p>
<br>
These EMAs are often used together to identify potential trend directions or market turning points. For example, common trading strategies involve observing the crossover of these two EMAs. When the short EMA crosses above the long EMA, it can be considered a bullish signal, and when it crosses below, it can be considered a bearish signal.
</p>