---
layout: post
title: "Pine Script - EMA"
description: "EMA // EMA 설정 shortEmaLength = input(5, \"Short EMA Length\") longEmaLength = input(20, \"Long EMA Length\") // EMA 계산 shortEma = ta.ema(close, shortEmaLength) l..."
date: 2023-12-07 02:45:21 +0900
section: blog
category: finance
lang: ko
ref: 2023-12-07-legacy-314-finance-pine-script-ema
tags:
  - "Pine Script Tutorial"
  - "finance"
---

<h2>
<b>
EMA
</b>
</h2>
<pre class="python">
<code>
// EMA 설정
shortEmaLength = input(5, "Short EMA Length")
longEmaLength = input(20, "Long EMA Length")

// EMA 계산
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
shortEmaLength(짧은 EMA 길이):
</b>
<br>
이 줄은 사용자가 더 짧은 EMA의 길이를 지정하는 입력을 생성합니다.
<br>
길이는 입력(10, "Short EMA Length")에 표시된 대로 기본적으로 10개 기간으로 설정됩니다.
<br>
'짧은' EMA는 길이가 짧기 때문에 '긴' EMA보다 가격 변화에 더 빠르게 반응합니다.
</p>
<p>
<br>
<b>
longEmaLength(긴 EMA 길이):
</b>
<br>
마찬가지로 이 줄은 사용자가 더 긴 EMA의 길이를 지정하는 입력을 생성합니다.
<br>
이 EMA의 기본 길이는 5개 기간(input(5, "Long EMA Length"))으로 설정됩니다.
<br>
기간이 긴 '긴' EMA는 '짧은' EMA에 비해 가격 변화에 더 느리게 반응합니다. 이는 장기간에 걸친 추세를 보다 매끄럽게 표현합니다.
<br>
EMA 계산:
<br>
<br>
<b>
shortEma = ta.ema(close, shortEmaLength):
</b>
이 라인은 자산의 종가(종가)와 shortEmaLength에 지정된 길이를 기반으로 매도 EMA를 계산합니다.
</p>
<p>
<br>
<b>
longEma = ta.ema(close, longEmaLength):
</b>
이 줄은 종가와 longEmaLength에 지정된 길이를 기반으로 매수 EMA를 계산합니다.
<br>
그러나 주목해야 할 중요한 점이 있습니다. 명명 규칙이 반전된 것 같습니다. 일반적으로 "짧은" EMA는 더 짧은 기간(일수)을 가지므로 최근 가격 변동에 더 민감하게 반응합니다. 반대로, "긴" EMA는 주기가 길어서 반응 속도가 느려지고 부드러워집니다. 스크립트에서 짧은 EMA는 긴 EMA(5)보다 긴 기간(10)으로 설정되어 있으며 이는 일반적인 규칙에 어긋납니다. 명확성을 위해 이러한 값을 전환하거나 이름을 바꿀 수 있습니다.
<br>
<br>
"짧은" EMA는 일반적으로 더 작은 숫자(예: 5)를 가지므로 최근 가격 변화에 더 민감합니다.
<br>
"긴" EMA는 더 큰 숫자(예: 10)를 가져야 하며, 이는 더 매끄럽고 단기 변동에 덜 민감하게 만듭니다.
</p>
<p>
<br>
이러한 EMA는 잠재적인 추세 방향이나 시장의 전환점을 식별하기 위해 종종 함께 사용됩니다. 예를 들어, 일반적인 거래 전략에는 이 두 EMA의 교차를 관찰하는 것이 포함됩니다. 짧은 EMA가 긴 EMA 위로 교차하면 강세 신호로 간주될 수 있고 아래로 교차하면 약세 신호로 간주될 수 있습니다.
</p>
