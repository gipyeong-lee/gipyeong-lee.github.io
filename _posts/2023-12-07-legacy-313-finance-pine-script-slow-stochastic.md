---
layout: post
title: "Pine Script - Slow Stochastic"
description: "Slow Stochastic // Slow Stochastic 설정 slowStochKLength = input(7, \"Slow Stochastic %K Length\") slowStochDLength = input(6, \"Slow Stochastic %D Length\") stoch..."
date: 2023-12-07 02:31:19 +0900
section: blog
category: finance
lang: ko
ref: 2023-12-07-legacy-313-finance-pine-script-slow-stochastic
tags:
  - "tradingview"
  - "Slow"
  - "auto"
  - "pine"
  - "Pine Script Tutorial"
  - "finance"
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
// Slow Stochastic 설정
slowStochKLength = input(7, "Slow Stochastic %K Length")
slowStochDLength = input(6, "Slow Stochastic %D Length")
stochUpper = input(70, "Upper Level")
stochLower = input(30, "Lower Level")
// Slow Stochastic 계산
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
SlowStochKLength(느린 확률론적 %K 길이):
</b>
<br>
이 매개변수는 느린 스토캐스틱 오실레이터에 대한 스토캐스틱 %K 라인의 길이를 정의합니다.
<br>
%K 라인을 계산하는 데 사용되는 기간 수를 결정합니다.
<br>
이 길이를 늘리면 %K 선이 더 부드러워지고 최근 가격 변화에 덜 민감해지며 잠재적으로 더 적은 수이지만 잠재적으로 더 안정적인 신호로 이어질 수 있습니다. 길이를 줄이면 %K 라인이 최근 가격 변화에 더 잘 반응하게 되어 신호 수가 증가하지만 잘못된 신호 수도 증가할 수 있습니다.
</p>
<p>
<br>
<b>
SlowStochDLength(느린 확률적 %D 길이):
</b>
<br>
슬로우 스토캐스틱 오실레이터에서 %D 라인을 계산하기 위해 %K 라인에 적용되는 이동평균의 길이를 설정하는 파라미터입니다.
<br>
%D 선은 %K 선의 이동 평균이며 평탄한 신호를 제공하고 잠재적인 추세 반전을 식별하는 역할을 합니다.
<br>
%D 길이가 길수록 더 부드러운 선이 제공되어 더 중요한 추세를 식별하는 데 도움이 될 수 있지만 신호가 지연될 수도 있습니다. 길이가 짧을수록 라인의 반응성이 높아지지만 잘못된 신호의 위험이 높아질 수 있습니다.
<br>
<b>
</b>
</p>

<p>
<b>
stochUpper (상위 레벨):
</b>
<br>
이는 스토캐스틱 오실레이터의 상위 임계값 레벨입니다.
<br>
스토캐스틱 선이 이 수준 이상으로 상승하면 해당 자산은 과매수된 것으로 간주될 수 있습니다. 거래자들은 이를 잠재적인 매도 신호나 자산 가격이 곧 하락할 수 있다는 신호로 해석하는 경우가 많습니다.
</p>

<p>
<b>
stochLower (하위 레벨):
</b>
<br>
이는 스토캐스틱 오실레이터의 하한 임계값 레벨입니다.
<br>
스토캐스틱 선이 이 수준 아래로 떨어지면 해당 자산은 과매도된 것으로 간주될 수 있습니다. 이는 종종 잠재적인 매수 신호 또는 자산 가격이 곧 상승할 수 있다는 표시로 간주됩니다.
</p>
