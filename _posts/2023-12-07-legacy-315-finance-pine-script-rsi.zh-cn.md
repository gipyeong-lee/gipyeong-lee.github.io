---
layout: post
title: "Pine Script - RSI"
description: "RSI / RSI 设置 rsiLength = input(5, \"RSI 长度\") rsiOverbought = input(80, \"RSI 超买水平\") rsiOversold = input(20, \"RSI 超卖水平\") rsi = ta.rsi(..."
date: 2023-12-07 13:44:23 +0900
section: blog
category: finance
lang: zh-cn
ref: 2023-12-07-legacy-315-finance-pine-script-rsi
tags:
  - "Pine Script 教程"
  - "finance"
translation_source_hash: 0e2b121859cfb52077956ecfc5823b3ce8204423ae97ae4bf7482dc75fa3dd9c
---

<h2>
RSI
</h2>
<pre class="python">
<code>
/ RSI 设置
rsiLength = input(5, "RSI Length")
rsiOverbought = input(80, "RSI Overbought Level")
rsiOversold = input(20, "RSI Oversold Level")
rsi = ta.rsi(close, rsiLength)
</code>
</pre>

<h2>
描述
</h2>
<p>
<b>
rsiLength（RSI 长度）：
</b>
<br>
这是脚本中设定的 RSI 计算长度，默认为 5 个周期。
<br>
它定义了用于计算 RSI 的 K 线（或周期）数量。
<br>
长度越短（如 5），RSI 对近期价格变动就越敏感、反应越快，这可能会导致更频繁的超买或超卖信号。
</p>
<p>
<br>
<b>
rsiOverbought（RSI 超买水平）：
</b>
<br>
脚本中设定为 80，该水平代表资产被视为超买的阈值。
<br>
传统上，超买水平设定为 70，但设定为 80 会使超买标准更严格，虽然可以潜在地减少错误信号，但也可能导致对超买情况的识别出现滞后。
</p>
<p>
<br>
<b>
rsiOversold（RSI 超卖水平）：
</b>
<br>
设定为 20，该水平代表资产被视为超卖的阈值。
<br>
通常超卖水平设定为 30，但在脚本中设定为 20，与超买条件类似，标准变得更加严格。这样可以减少错误的超卖信号，但可能会延迟对实际超卖状态的检测。
<br>
<b>
</b>
</p>

<p>
<b>
RSI 计算：
</b>
<br>
RSI 本身使用 `ta.rsi(close, rsiLength)` 函数计算。
<br>
该函数基于指定长度（rsiLength）的收盘价（close）来计算 RSI。
<br>
RSI 是一种衡量价格波动速度和变化的动量振荡指标，在 0 到 100 之间波动。通常，若 RSI 大于 70，表明资产可能处于超买状态（可能被高估）；若小于 30，则表明可能处于超卖状态（可能被低估）。
</p>

<h2>
示例
</h2>
<blockquote>
在 3 分钟周期图表上应用策略时
</blockquote>

<p>
<b>
rsiLength（RSI 长度）：
</b>
<br>
将 rsiLength 设为 5 时，RSI 将使用 3 分钟图表上的最后 5 根 K 线进行计算。
<br>
由于每根 K 线代表 3 分钟，RSI 实际上分析的是过去 15 分钟的交易数据（5 根 K 线 × 每根 3 分钟）。
<br>
这种相对较短的回溯期使 RSI 对近期价格变动反应极快，非常适合在 3 分钟图表等低时间周期图表上进行的短线交易决策。
</p>
<p>
<br>
<b>
rsiOverbought（RSI 超买水平）：
</b>
<br>
设定为 80，当 RSI 超过此水平时，资产被视为超买。
<br>
在 3 分钟图表上，若 RSI 超过 80，表示短期内存在强劲的看涨动量。然而，这也暗示资产可能过度扩张，面临回调或反转的风险。
</p>
<p>
<br>
<b>
rsiOversold（RSI 超卖水平）：
</b>
<br>
设定为 20，当 RSI 低于此阈值时，资产被视为超卖。
<br>
在 3 分钟图表上，若 RSI 低于 20，表示短期内存在强劲的看跌动量，暗示资产可能超卖过度，有望反弹或反转。
<br>
使用这些设置（5 个周期，80/20 阈值）在短周期（3 分钟图表）上使用 RSI，意味着专注于价格动量非常快速和短暂的变化。这对日内交易者或试图利用微小、快速价格波动的人很有帮助。但是，时间周期越短，越容易受到市场“噪音”和错误信号的影响，因此通常建议结合其他指标或方法来确认交易信号。
<br>
<br>
与所有交易策略一样，请务必利用历史数据彻底回测并验证您的方法，以理解其潜在效果，并意识到短周期交易所涉及的风险。
</p>