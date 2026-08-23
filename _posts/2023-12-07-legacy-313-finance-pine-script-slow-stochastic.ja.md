---
layout: post
title: "Pine Script - Slow Stochastic"
description: "Slow Stochastic // Slow Stochastic 設定 slowStochKLength = input(7, \"Slow Stochastic %K Length\") slowStochDLength = input(6, \"Slow Stochastic %D Length\") stoch..."
date: 2023-12-07 02:31:19 +0900
section: blog
category: finance
lang: ja
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
スローストキャスティクス
</span>
</b>
</h2>
</div>
<pre class="python">
<code>
// スローストキャスティクス設定
slowStochKLength = input(7, "Slow Stochastic %K Length")
slowStochDLength = input(6, "Slow Stochastic %D Length")
stochUpper = input(70, "Upper Level")
stochLower = input(30, "Lower Level")
// スローストキャスティクス計算
slowStochK = ta.sma(ta.stoch(close, high, low, slowStochKLength), slowStochDLength)
slowStochD = ta.sma(slowStochK, slowStochDLength)
</code>
</pre>
<h2>
<b>
Description (説明)
</b>
</h2>
<p>
<b>
SlowStochKLength (スローストキャスティクス %K 期間):
</b>
<br>
このパラメータは、スローストキャスティクス・オシレーターにおけるストキャスティクス %K ラインの期間を定義します。
<br>
%K ラインを計算するために使用される期間数を決定します。
<br>
この期間を長くすると %K ラインはより滑らかになり、直近の価格変動に対する感度が低下するため、シグナルの数は減るものの、より安定したシグナルが得られる可能性があります。期間を短くすると %K ラインは直近の価格変動により敏感に反応するため、シグナル数は増加しますが、同時に誤ったシグナル（ダマシ）も増加する可能性があります。
</p>
<p>
<br>
<b>
SlowStochDLength (スローストキャスティクス %D 期間):
</b>
<br>
スローストキャスティクス・オシレーターにおいて、%D ラインを計算するために %K ラインに適用される移動平均の期間を設定するパラメータです。
<br>
%D ラインは %K ラインの移動平均であり、より滑らかなシグナルを提供し、潜在的なトレンドの反転を特定する役割を果たします。
<br>
%D 期間が長いほどラインはより滑らかになり、重要なトレンドを特定するのに役立ちますが、シグナルに遅延が生じる可能性があります。期間が短いほどラインの反応性は高まりますが、誤ったシグナルのリスクも高まる可能性があります。
<br>
<b>
</b>
</p>

<p>
<b>
stochUpper (上限レベル):
</b>
<br>
ストキャスティクス・オシレーターの上限閾値レベルです。
<br>
ストキャスティクス・ラインがこのレベルを上回ると、対象資産は「買われすぎ」と見なされることがあります。トレーダーはこれを、潜在的な売りシグナル、あるいは資産価格が間もなく下落する可能性を示すサインとして解釈することがよくあります。
</p>

<p>
<b>
stochLower (下限レベル):
</b>
<br>
ストキャスティクス・オシレーターの下限閾値レベルです。
<br>
ストキャスティクス・ラインがこのレベルを下回ると、対象資産は「売られすぎ」と見なされることがあります。これは多くの場合、潜在的な買いシグナル、あるいは資産価格が間もなく上昇する可能性を示すサインと見なされます。
</p>