---
layout: post
title: "Pine Script - RSI"
description: "RSI / RSI Settings rsiLength = input(5, \"RSI Length\") rsiOverbought = input(80, \"RSI Overbought Level\") rsiOversold = input(20, \"RSI Oversold Level\") rsi = ta.rsi(..."
date: 2023-12-07 13:44:23 +0900
section: blog
category: finance
lang: en
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
// RSI Settings
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
rsiLength:
</b>
<br>
This is the RSI calculation length, set to 5 periods in the script.
<br>
It defines the number of bars (or periods) used to calculate the RSI.
<br>
A shorter length, such as 5, makes the RSI more sensitive and responsive to recent price changes, potentially resulting in more frequent overbought or oversold signals.
</p>
<p>
<br>
<b>
rsiOverbought:
</b>
<br>
Set to 80 in the script, this level represents the threshold above which an asset is considered overbought.
<br>
Traditionally, the overbought level is set to 70, but setting it to 80 makes the overbought criteria stricter. This can potentially reduce false signals, though recognition of overbought conditions may be delayed.
</p>
<p>
<br>
<b>
rsiOversold:
</b>
<br>
Set to 20, this level represents the threshold below which an asset is considered oversold.
<br>
Typically, the oversold level is set to 30, but setting it to 20 in the script, similar to the overbought condition, makes the criteria stricter. This can reduce false oversold signals, but detection of actual oversold states may be delayed.
<br>
<b>
</b>
</p>

<p>
<b>
RSI Calculation:
</b>
<br>
The RSI itself is calculated using the ta.rsi(close, rsiLength) function.
<br>
This function calculates the RSI based on the closing price for the specified length (rsiLength).
<br>
The RSI is a momentum oscillator that measures the speed and change of price movements. It oscillates between 0 and 100. Generally, an RSI above 70 indicates that an asset may be overbought (potentially overvalued), while an RSI below 30 indicates it may be oversold (potentially undervalued).
</p>

<h2>
Example
</h2>
<blockquote>
Applying the strategy to a 3-minute timeframe chart
</blockquote>

<p>
<b>
rsiLength:
</b>
<br>
Setting rsiLength to 5 means the RSI is calculated using the last 5 bars of the 3-minute chart.
<br>
Since each bar represents 3 minutes, the RSI effectively analyzes the trading data from the past 15 minutes (5 bars × 3 minutes per bar).
<br>
This relatively short lookback period makes the RSI very responsive to recent price changes, which is suitable for short-term trading decisions often made on lower timeframe charts like the 3-minute chart.
</p>
<p>
<br>
<b>
rsiOverbought:
</b>
<br>
Set to 80, if the RSI exceeds this level, the asset is considered overbought.
<br>
On a 3-minute chart, an RSI above 80 indicates strong short-term bullish momentum. However, it also suggests that the asset may be overextended and could face a decline or reversal.
</p>
<p>
<br>
<b>
rsiOversold:
</b>
<br>
Set to 20, this level indicates that the asset is considered oversold when the RSI drops below this threshold.
<br>
On a 3-minute chart, an RSI below 20 indicates strong short-term bearish momentum, suggesting the asset may be under-extended and could experience a rebound or reversal.
<br>
Using these settings (5 periods, 80/20 thresholds) on a short duration (3-minute chart) means focusing on very fast, short-term changes in price momentum. This can be useful for day traders or those looking to capitalize on small, quick price fluctuations. However, because shorter periods can be more susceptible to market "noise" and false signals, it is often recommended to use additional indicators or methods to confirm trading signals.
<br>
<br>
As with any trading strategy, it is important to thoroughly backtest and validate your approach using historical data to understand its potential efficiency and to be aware of the risks associated with trading over short durations.
</p>