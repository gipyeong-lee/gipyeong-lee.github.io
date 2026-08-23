---
layout: post
title: "Pine Script - EMA"
description: "EMA // EMA 设置 shortEmaLength = input(5, \"Short EMA Length\") longEmaLength = input(20, \"Long EMA Length\") // EMA 计算 shortEma = ta.ema(close, shortEmaLength) l..."
date: 2023-12-07 02:45:21 +0900
section: blog
category: finance
lang: zh-cn
ref: 2023-12-07-legacy-314-finance-pine-script-ema
tags:
  - "Pine Script 教程"
  - "金融"
translation_source_hash: 386ca2039fb55706e7b1113d3af430ad066162c721df2abb58d9c67feeab31ea
---

<h2>
<b>
EMA
</b>
</h2>
<pre class="python">
<code>
// EMA 设置
shortEmaLength = input(5, "Short EMA Length")
longEmaLength = input(20, "Long EMA Length")

// EMA 计算
shortEma = ta.ema(close, shortEmaLength)
longEma = ta.ema(close, longEmaLength)
</code>
</pre>

<h2>
<b>
说明
</b>
</h2>

<p>
<b>
shortEmaLength (短 EMA 长度)：
</b>
<br>
此行创建了一个输入项，允许用户指定较短 EMA 的长度。
<br>
根据输入设置 (input(10, "Short EMA Length")，默认周期设置为 10。
<br>
由于“短”EMA 的长度较短，因此它对价格变化的反应比“长”EMA 更快。
</p>
<p>
<br>
<b>
longEmaLength (长 EMA 长度)：
</b>
<br>
同样，此行创建了一个输入项，允许用户指定较长 EMA 的长度。
<br>
该 EMA 的默认长度设置为 5 个周期 (input(5, "Long EMA Length"))。
<br>
与“短”EMA 相比，“长”EMA 的周期更长，因此对价格变化的反应较慢。这使得它在表现长期趋势时更加平滑。
<br>
EMA 计算：
<br>
<br>
<b>
shortEma = ta.ema(close, shortEmaLength)：
</b>
此行基于资产的收盘价 (close) 和 shortEmaLength 中指定的长度计算短 EMA。
</p>
<p>
<br>
<b>
longEma = ta.ema(close, longEmaLength)：
</b>
此行基于收盘价和 longEmaLength 中指定的长度计算长 EMA。
<br>
但需要注意一点：命名规则似乎反了。通常，“短”EMA 的周期（天数）更短，因此对近期价格波动更敏感。相反，“长”EMA 的周期更长，反应速度更慢且更平滑。在该脚本中，短 EMA 的设置周期 (10) 比长 EMA (5) 还要长，这违背了常规。为了清晰起见，可以调整这些值或重命名。
<br>
<br>
“短”EMA 通常应具有较小的数值（例如 5），因此对近期价格变化更敏感。
<br>
“长”EMA 应具有较大的数值（例如 10），这使其更平滑且对短期波动不太敏感。
</p>
<p>
<br>
这些 EMA 常被结合使用，以识别潜在的趋势方向或市场转折点。例如，一种常见的交易策略是观察这两条 EMA 的交叉：当短 EMA 上穿长 EMA 时，可视为看涨信号；当其下穿长 EMA 时，可视为看跌信号。
</p>