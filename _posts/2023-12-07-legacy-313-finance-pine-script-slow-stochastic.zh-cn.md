---
layout: post
title: "Pine Script - 慢速随机指标 (Slow Stochastic)"
description: "慢速随机指标 (Slow Stochastic) // 慢速随机指标设置 slowStochKLength = input(7, \"慢速随机 %K 长度\") slowStochDLength = input(6, \"慢速随机 %D 长度\") stochUpper..."
date: 2023-12-07 02:31:19 +0900
section: blog
category: finance
lang: zh-cn
ref: 2023-12-07-legacy-313-finance-pine-script-slow-stochastic
tags:
  - "tradingview"
  - "Slow"
  - "auto"
  - "pine"
  - "Pine Script 教程"
  - "finance"
translation_source_hash: 966c008257615c760ac6b53d3da1d51465841fa816088c16e32e1dd6422f5ebd
---

<div>
<h2>
<b>
<span>
慢速随机指标 (Slow Stochastic)
</span>
</b>
</h2>
</div>
<pre class="python">
<code>
// 慢速随机指标设置
slowStochKLength = input(7, "慢速随机 %K 长度")
slowStochDLength = input(6, "慢速随机 %D 长度")
stochUpper = input(70, "超买水平")
stochLower = input(30, "超卖水平")
// 慢速随机指标计算
slowStochK = ta.sma(ta.stoch(close, high, low, slowStochKLength), slowStochDLength)
slowStochD = ta.sma(slowStochK, slowStochDLength)
</code>
</pre>
<h2>
<b>
说明
</b>
</h2>
<p>
<b>
SlowStochKLength（慢速随机指标 %K 长度）：
</b>
<br>
此参数定义了慢速随机震荡指标中 %K 线长度。
<br>
它决定了用于计算 %K 线的周期数。
<br>
增加此长度会使 %K 线更加平滑，对近期价格变化的敏感度降低，从而可能导致交易信号数量减少，但信号可能更为稳定。缩短长度会使 %K 线对近期价格变化反应更灵敏，从而增加信号数量，但也可能增加错误信号的数量。
</p>
<p>
<br>
<b>
SlowStochDLength（慢速随机指标 %D 长度）：
</b>
<br>
此参数用于设置应用于 %K 线以计算慢速随机震荡指标中 %D 线的移动平均长度。
<br>
%D 线是 %K 线的移动平均线，起到平滑信号并识别潜在趋势反转的作用。
<br>
%D 长度越长，线条越平滑，有助于识别更重要的趋势，但信号可能会滞后。长度越短，线条反应越快，但出现错误信号的风险可能会增加。
<br>
<b>
</b>
</p>

<p>
<b>
stochUpper（超买水平）：
</b>
<br>
这是随机震荡指标的上限阈值。
<br>
当随机指标线升至此水平以上时，该资产可能被视为“超买”。交易者通常将其解读为潜在的卖出信号，或预示资产价格即将下跌的信号。
</p>

<p>
<b>
stochLower（超卖水平）：
</b>
<br>
这是随机震荡指标的下限阈值。
<br>
当随机指标线跌至此水平以下时，该资产可能被视为“超卖”。这通常被视为潜在的买入信号，或预示资产价格即将上涨的信号。
</p>