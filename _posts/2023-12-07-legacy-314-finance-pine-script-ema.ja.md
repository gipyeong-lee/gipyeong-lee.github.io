---
layout: post
title: "Pine Script - EMA"
description: "EMA // EMA設定 shortEmaLength = input(5, \"Short EMA Length\") longEmaLength = input(20, \"Long EMA Length\") // EMA計算 shortEma = ta.ema(close, shortEmaLength) l..."
date: 2023-12-07 02:45:21 +0900
section: blog
category: finance
lang: ja
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
// EMA設定
shortEmaLength = input(5, "Short EMA Length")
longEmaLength = input(20, "Long EMA Length")

// EMA計算
shortEma = ta.ema(close, shortEmaLength)
longEma = ta.ema(close, longEmaLength)
</code>
</pre>

<h2>
<b>
Description (説明)
</b>
</h2>

<p>
<b>
shortEmaLength（短期EMAの期間）:
</b>
<br>
この行は、ユーザーが短いEMAの期間を指定するための入力項目を作成します。
<br>
期間は、input(10, "Short EMA Length")に示されているように、デフォルトで10期間に設定されています。
<br>
「短期」EMAは期間が短いため、「長期」EMAよりも価格変動に対して素早く反応します。
</p>
<p>
<br>
<b>
longEmaLength（長期EMAの期間）:
</b>
<br>
同様に、この行はユーザーが長いEMAの期間を指定するための入力項目を作成します。
<br>
このEMAのデフォルト期間は5期間(input(5, "Long EMA Length"))に設定されています。
<br>
期間が長い「長期」EMAは、「短期」EMAに比べて価格変動に対してゆっくりと反応します。これにより、長期間にわたるトレンドをより滑らかに表現できます。
<br>
EMA計算:
<br>
<br>
<b>
shortEma = ta.ema(close, shortEmaLength):
</b>
この行は、資産の終値（close）とshortEmaLengthで指定された期間に基づいてEMAを計算します。
</p>
<p>
<br>
<b>
longEma = ta.ema(close, longEmaLength):
</b>
この行は、終値とlongEmaLengthで指定された期間に基づいてEMAを計算します。
<br>
ただし、重要な注意点があります。命名規則が逆になっているようです。一般的に「短期」EMAは短い期間（日数）を持つため、直近の価格変動に敏感に反応します。逆に、「長期」EMAは期間が長いため、反応速度が遅くなり滑らかになります。このスクリプトでは、短期EMAが長期EMA(5)よりも長い期間(10)で設定されており、一般的なルールに反しています。明確にするために、これらの値を入れ替えるか、名前を変更することができます。
<br>
<br>
「短期」EMAは通常、小さい数字（例：5）を持ち、直近の価格変化に対して敏感になります。
<br>
「長期」EMAは大きい数字（例：10）を持つべきであり、これにより滑らかになり、短期的な変動の影響を受けにくくなります。
</p>
<p>
<br>
これらのEMAは、潜在的なトレンドの方向や市場の転換点を識別するために併用されることがよくあります。例えば、一般的な取引戦略には、これら2つのEMAのクロスを観察することが含まれます。短期EMAが長期EMAを上抜けると強気シグナル、下抜けると弱気シグナルと見なすことができます。
</p>