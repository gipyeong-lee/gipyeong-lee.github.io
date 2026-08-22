---
layout: post
title: "Pine Script - RSI"
description: "RSI / RSI 설정 rsiLength = input(5, \"RSI Length\") rsiOverbought = input(80, \"RSI Overbought Level\") rsiOversold = input(20, \"RSI Oversold Level\") rsi = ta.rsi(..."
date: 2023-12-07 13:44:23 +0900
section: blog
category: finance
lang: ko
ref: 2023-12-07-legacy-315-finance-pine-script-rsi
tags:
  - "Pine Script Tutorial"
  - "finance"
---

<h2>
RSI
</h2>
<pre class="python">
<code>
/ RSI 설정
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
rsi길이(RSI 길이):
</b>
<br>
이는 스크립트에서 5개 기간으로 설정된 RSI 계산 길이입니다.
<br>
RSI를 계산하는 데 사용되는 막대(또는 기간) 수를 정의합니다.
<br>
5와 같이 길이가 짧을수록 RSI가 최근 가격 변화에 더 민감하고 반응하게 되어 잠재적으로 과매수 또는 과매도 신호가 더 자주 발생하게 됩니다.
</p>
<p>
<br>
<b>
rsiOverbought(RSI 과매수 수준):
</b>
<br>
스크립트에서 80으로 설정하면 이 수준은 자산이 과매수된 것으로 간주되는 임계값을 나타냅니다.
<br>
전통적으로 과매수 수준은 70으로 설정되어 있지만, 80으로 설정하면 과매수 기준이 더 엄격해지며 잠재적으로 잘못된 신호를 줄일 수 있지만 과매수 조건 인식이 지연될 수도 있습니다.
</p>
<p>
<br>
<b>
rsiOversold(RSI 과매도 수준):
</b>
<br>
20으로 설정하면 이 수준은 자산이 과매도된 것으로 간주되는 임계값을 나타냅니다.
<br>
일반적으로 과매도 수준은 30으로 설정되지만 스크립트에서 20으로 설정하면 과매수 조건과 유사하게 기준이 더 엄격해집니다. 이렇게 하면 잘못된 과매도 신호를 줄일 수 있지만 실제 과매도 상태 감지가 지연될 수 있습니다.
<br>
<b>
</b>
</p>

<p>
<b>
RSI 계산:
</b>
<br>
RSI 자체는 ta.rsi(close, rsiLength) 함수를 사용하여 계산됩니다.
<br>
이 함수는 지정된 길이(rsiLength)에 대한 종가(종가)를 기반으로 RSI를 계산합니다.
<br>
RSI는 가격 움직임의 속도와 변화를 측정하는 모멘텀 오실레이터입니다. 0과 100 사이에서 진동합니다. 일반적으로 RSI가 70보다 크면 자산이 과매수(과대평가될 가능성이 있음)될 수 있음을 나타내고, 30보다 작으면 과매도(저평가될 가능성이 있음)될 수 있음을 나타냅니다.
</p>

<h2>
Example
</h2>
<blockquote>
3분 봉 차트에 전략 적용시
</blockquote>

<p>
<b>
rsi길이(RSI 길이):
</b>
<br>
rsiLength를 5로 설정하면 RSI는 3분 차트의 마지막 5개 막대를 사용하여 계산됩니다.
<br>
각 막대는 3분을 나타내므로 RSI는 지난 15분간의 거래 데이터(5막대 × 막대당 3분)를 효과적으로 분석합니다.
<br>
이렇게 상대적으로 짧은 되돌아보기 기간은 RSI가 최근 가격 변화에 매우 잘 반응하도록 하며, 이는 3분 차트와 같은 낮은 시간대 차트에서 종종 이루어지는 단기 거래 결정에 적합합니다.
</p>
<p>
<br>
<b>
rsiOverbought(RSI 과매수 수준):
</b>
<br>
80으로 설정하면 RSI가 이 수준을 초과하면 자산이 과매수된 것으로 간주됩니다.
<br>
3분 차트에서 RSI가 80을 넘으면 단기적으로 강한 강세 모멘텀을 나타냅니다. 그러나 이는 또한 자산이 과도하게 확장되어 하락 또는 반전에 직면할 수 있음을 시사합니다.
</p>
<p>
<br>
<b>
rsiOversold(RSI 과매도 수준):
</b>
<br>
20으로 설정된 이 수준은 RSI가 이 임계값 아래로 떨어질 때 자산이 과매도된 것으로 간주됨을 나타냅니다.
<br>
3분 차트에서 RSI가 20 미만이면 단기적으로 강한 약세 모멘텀을 나타내며 자산이 과소 확장되어 반등 또는 반전을 경험할 수 있음을 나타냅니다.
<br>
이러한 설정(5개 기간, 80/20 임계값)을 사용하여 짧은 기간(3분 차트)에서 RSI를 사용한다는 것은 가격 모멘텀의 매우 빠르고 단기적인 변화에 초점을 맞추고 있음을 의미합니다. 이는 데이 트레이더나 작고 빠른 가격 변동을 활용하려는 사람들에게 유용할 수 있습니다. 그러나 기간이 짧을수록 시장의 "잡음"과 잘못된 신호에 더 취약할 수 있으므로 거래 신호를 확인하기 위해 추가 지표나 방법을 사용하는 것이 종종 권장됩니다.
<br>
<br>
모든 거래 전략과 마찬가지로 과거 데이터를 사용하여 접근 방식을 철저히 백테스트하고 검증하여 잠재적인 효율성을 이해하고 짧은 기간 동안의 거래와 관련된 위험을 인식하는 것이 중요합니다.
</p>
