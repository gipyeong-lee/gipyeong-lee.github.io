---
layout: post
title: "[단기] 04. Feature IMAGE 추출"
description: "안녕하세요? 이번시간에는 저번시간에 하기로 했던.. URL 로부터 feature 이미지를 가져오는 기능을 구현하도록 하겠습니다. 아래는 대전 멤버쉽 남두현님의 정규식관련 자료입니다. 이번 기능 구현에 많은 도움을 주셨습니다. 더보기 Python Assignment 5 Author..."
date: 2015-02-06 02:09:08 +0900
section: blog
category: projects
lang: ko
ref: 2015-02-06-legacy-11-projects-04-feature-image
tags:
  - "TJSSM"
  - "projects"
---

<p>
안녕하세요?
</p>
<p>
이번시간에는 저번시간에 하기로 했던.. URL 로부터 feature 이미지를 가져오는 기능을 구현하도록 하겠습니다.
</p>
<p>
아래는 대전 멤버쉽 남두현님의 정규식관련 자료입니다.
</p>
<p>
이번 기능 구현에 많은 도움을 주셨습니다.
</p>

<span class="txt_fold">
더보기
</span>
<div class="moreless_content">

<div class="cell border-box-sizing text_cell rendered">
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3>
<br class="Apple-interchange-newline">
Python Assignment 5
</h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3>
Author : 2009135046, Doohyun Nam
</h3>
<h3>
</h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [1번 문제] 클래스와 모듈의 공통점과 차이점에 대해 설명하시오.
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
클래스와 모듈의 공통점은 비슷하거나 관련된 일을 하는 함수나 상수값들을 모아서 저장하는 것을 말하며, 별도의 이름공간을 가지고 있다. 이러한 이유는 재사용성과 유지보수 측면에 초점을 맞추고 있다. 차이점이라면, 모듈은 파일단위로 이름공간을 정의하고, 클래스는 클래스 공간에 이름공간을 구성한다.
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [2번 문제] 다형성에 대해 설명하고 다형성을 보여주는 자신만의 파이썬 코드 예제를 제시하시오.
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In [23]:
</div>
<div class="inner_cell">
<div class="input_area">
<div class="highlight">
<pre>
<span class="c">
# -*- coding: utf-8 -*-
</span>
<span class="k">
class
</span>
<span class="nc">
FlyBehavior
</span>
<span class="p">
:
</span>
<span class="k">
def
</span>
<span class="nf">
fly
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="k">
pass
</span>
<span class="k">
class
</span>
<span class="nc">
FlyWithWings
</span>
<span class="p">
(
</span>
<span class="n">
FlyBehavior
</span>
<span class="p">
):
</span>
<span class="k">
def
</span>
<span class="nf">
fly
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="k">
print
</span>
<span class="s">
"날아 다님"
</span>
<span class="k">
class
</span>
<span class="nc">
FlyNoWay
</span>
<span class="p">
(
</span>
<span class="n">
FlyBehavior
</span>
<span class="p">
):
</span>
<span class="k">
def
</span>
<span class="nf">
fly
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="k">
print
</span>
<span class="s">
"날수 없음"
</span>
<span class="k">
class
</span>
<span class="nc">
QuackBeHavior
</span>
<span class="p">
:
</span>
<span class="k">
def
</span>
<span class="nf">
quack
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="k">
pass
</span>
<span class="k">
class
</span>
<span class="nc">
Quack
</span>
<span class="p">
(
</span>
<span class="n">
QuackBeHavior
</span>
<span class="p">
):
</span>
<span class="k">
def
</span>
<span class="nf">
quack
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="k">
print
</span>
<span class="s">
"꽥꽥"
</span>
<span class="k">
class
</span>
<span class="nc">
Squack
</span>
<span class="p">
(
</span>
<span class="n">
QuackBeHavior
</span>
<span class="p">
):
</span>
<span class="k">
def
</span>
<span class="nf">
quack
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="k">
print
</span>
<span class="s">
"삑삑"
</span>
<span class="k">
class
</span>
<span class="nc">
MuteQuack
</span>
<span class="p">
(
</span>
<span class="n">
QuackBeHavior
</span>
<span class="p">
):
</span>
<span class="k">
def
</span>
<span class="nf">
quack
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="k">
print
</span>
<span class="s">
""
</span>
<span class="k">
class
</span>
<span class="nc">
Duck
</span>
<span class="p">
:
</span>
<span class="k">
def
</span>
<span class="nf">
__init__
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
,
</span>
<span class="n">
quack
</span>
<span class="p">
,
</span>
<span class="n">
fly
</span>
<span class="p">
):
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
quackBeHavior
</span>
<span class="o">
=
</span>
<span class="n">
quack
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
flyBehavior
</span>
<span class="o">
=
</span>
<span class="n">
fly
</span>
<span class="k">
def
</span>
<span class="nf">
quack
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
quackBeHavior
</span>
<span class="o">
.
</span>
<span class="n">
quack
</span>
<span class="p">
()
</span>
<span class="k">
def
</span>
<span class="nf">
fly
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
flyBehavior
</span>
<span class="o">
.
</span>
<span class="n">
fly
</span>
<span class="p">
()
</span>
<span class="n">
mallardDuck
</span>
<span class="o">
=
</span>
<span class="n">
Duck
</span>
<span class="p">
(
</span>
<span class="n">
Quack
</span>
<span class="p">
(),
</span>
<span class="n">
FlyWithWings
</span>
<span class="p">
())
</span>
<span class="n">
rubberDuck
</span>
<span class="o">
=
</span>
<span class="n">
Duck
</span>
<span class="p">
(
</span>
<span class="n">
Squack
</span>
<span class="p">
(),
</span>
<span class="n">
FlyNoWay
</span>
<span class="p">
())
</span>
<span class="n">
mallardDuck
</span>
<span class="o">
.
</span>
<span class="n">
fly
</span>
<span class="p">
()
</span>
<span class="n">
rubberDuck
</span>
<span class="o">
.
</span>
<span class="n">
fly
</span>
<span class="p">
()
</span>
<span class="n">
mallardDuck
</span>
<span class="o">
.
</span>
<span class="n">
quack
</span>
<span class="p">
()
</span>
<span class="n">
rubberDuck
</span>
<span class="o">
.
</span>
<span class="n">
quack
</span>
<span class="p">
()
</span>
</pre>
</div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>
날아 다님
날수 없음
꽥꽥
삑삑
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
[풀이] 상속 관계 내의 다른 클래스들의 인스턴스들이 같은 멤버 함수 호출에 대해 각각 다르게 반응하도록 하는 기능, 연산자 오버로딩도 다형성을 지원하는 중요한 기술
<br>
[예제] 디자인패턴 중 전략 패턴을 사용한 예제이다. FlyBehavior, QuackBeHavior 을 상속받은 각각의 행동에 대해 실행시간에 각 객체들은 다른 반응을 지원하고 있다. 다음의 예제는 상속된 quack나 squack보다는 이를 구성관계에 있는 duck 객체가 더욱 중요하다. duck객체가 초기화될때 어떤 객체를 가지고 있는지에 따라 다른 행동을 취할 수 있다.
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [3번 문제] 다음 각 요구사항 모두를 만족시키는 Counter 클래스를 코딩하시오 (정답을 각 요구사항별로 입력할 필요 없이 3번 문제에 대해 1개의 클래스 정의 코드를 제시하면 된다.)
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In [21]:
</div>
<div class="inner_cell">
<div class="input_area">
<div class="highlight">
<pre>
<span class="c">
# -*- coding: utf-8 -*-
</span>
<span class="k">
class
</span>
<span class="nc">
Counter
</span>
<span class="p">
(
</span>
<span class="nb">
object
</span>
<span class="p">
):
</span>
<span class="k">
def
</span>
<span class="nf">
__init__
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
,
</span>
<span class="n">
value
</span>
<span class="p">
,
</span>
<span class="n">
step
</span>
<span class="o">
=
</span>
<span class="mi">
1
</span>
<span class="p">
):
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
step
</span>
<span class="o">
=
</span>
<span class="n">
step
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
value
</span>
<span class="o">
=
</span>
<span class="n">
value
</span>
<span class="k">
def
</span>
<span class="nf">
incr
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
value
</span>
<span class="o">
+=
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
step
</span>
<span class="k">
def
</span>
<span class="nf">
__str__
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="k">
return
</span>
<span class="nb">
str
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
value
</span>
<span class="p">
)
</span>
<span class="k">
def
</span>
<span class="nf">
__call__
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
incr
</span>
<span class="p">
()
</span>
<span class="k">
def
</span>
<span class="nf">
__add__
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
,
</span>
<span class="n">
other
</span>
<span class="p">
):
</span>
<span class="k">
return
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
operatorHelper
</span>
<span class="p">
(
</span>
<span class="n">
other
</span>
<span class="p">
,
</span>
<span class="s">
"+"
</span>
<span class="p">
)
</span>
<span class="k">
def
</span>
<span class="nf">
__sub__
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
,
</span>
<span class="n">
other
</span>
<span class="p">
):
</span>
<span class="k">
return
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
operatorHelper
</span>
<span class="p">
(
</span>
<span class="n">
other
</span>
<span class="p">
,
</span>
<span class="s">
"-"
</span>
<span class="p">
)
</span>
<span class="k">
def
</span>
<span class="nf">
operatorHelper
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
,
</span>
<span class="n">
other
</span>
<span class="p">
,
</span>
<span class="n">
code
</span>
<span class="p">
):
</span>
<span class="k">
try
</span>
<span class="p">
:
</span>
<span class="k">
if
</span>
<span class="nb">
type
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
)
</span>
<span class="o">
==
</span>
<span class="nb">
type
</span>
<span class="p">
(
</span>
<span class="n">
other
</span>
<span class="p">
):
</span>
<span class="k">
exec
</span>
<span class="p">
(
</span>
<span class="nb">
compile
</span>
<span class="p">
(
</span>
<span class="s">
"self.value
</span>
<span class="si">
%s
</span>
<span class="s">
= other.value"
</span>
<span class="o">
%
</span>
<span class="n">
code
</span>
<span class="p">
,
</span>
<span class="s">
'&lt;string&gt;'
</span>
<span class="p">
,
</span>
<span class="s">
'single'
</span>
<span class="p">
))
</span>
<span class="k">
exec
</span>
<span class="p">
(
</span>
<span class="nb">
compile
</span>
<span class="p">
(
</span>
<span class="s">
"self.step
</span>
<span class="si">
%s
</span>
<span class="s">
= other.step"
</span>
<span class="o">
%
</span>
<span class="n">
code
</span>
<span class="p">
,
</span>
<span class="s">
'&lt;string&gt;'
</span>
<span class="p">
,
</span>
<span class="s">
'single'
</span>
<span class="p">
))
</span>
<span class="k">
else
</span>
<span class="p">
:
</span>
<span class="k">
exec
</span>
<span class="p">
(
</span>
<span class="nb">
compile
</span>
<span class="p">
(
</span>
<span class="s">
"self.value
</span>
<span class="si">
%s
</span>
<span class="s">
= int(other)"
</span>
<span class="o">
%
</span>
<span class="n">
code
</span>
<span class="p">
,
</span>
<span class="s">
'&lt;string&gt;'
</span>
<span class="p">
,
</span>
<span class="s">
'single'
</span>
<span class="p">
))
</span>
<span class="k">
except
</span>
<span class="p">
:
</span>
<span class="k">
pass
</span>
<span class="k">
return
</span>
<span class="bp">
self
</span>
<span class="k">
def
</span>
<span class="nf">
__cmp__
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
,
</span>
<span class="n">
other
</span>
<span class="p">
):
</span>
<span class="n">
value
</span>
<span class="o">
=
</span>
<span class="n">
other
</span>
<span class="p">
;
</span>
<span class="k">
try
</span>
<span class="p">
:
</span>
<span class="k">
if
</span>
<span class="nb">
type
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
)
</span>
<span class="o">
==
</span>
<span class="nb">
type
</span>
<span class="p">
(
</span>
<span class="n">
other
</span>
<span class="p">
):
</span>
<span class="n">
value
</span>
<span class="o">
=
</span>
<span class="n">
other
</span>
<span class="o">
.
</span>
<span class="n">
value
</span>
<span class="k">
else
</span>
<span class="p">
:
</span>
<span class="n">
value
</span>
<span class="o">
=
</span>
<span class="nb">
int
</span>
<span class="p">
(
</span>
<span class="n">
other
</span>
<span class="p">
)
</span>
<span class="k">
except
</span>
<span class="p">
:
</span>
<span class="k">
pass
</span>
<span class="k">
return
</span>
<span class="nb">
cmp
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
value
</span>
<span class="p">
,
</span>
<span class="n">
value
</span>
<span class="p">
)
</span>
<span class="c">
#요구 사항 1번
</span>
<span class="n">
c
</span>
<span class="o">
=
</span>
<span class="n">
Counter
</span>
<span class="p">
(
</span>
<span class="mi">
10
</span>
<span class="p">
)
</span>
<span class="n">
d
</span>
<span class="o">
=
</span>
<span class="n">
Counter
</span>
<span class="p">
(
</span>
<span class="mi">
10
</span>
<span class="p">
,
</span>
<span class="mi">
2
</span>
<span class="p">
)
</span>
<span class="c">
#요구사항 2번
</span>
<span class="k">
print
</span>
<span class="s">
"요구 사항 2번 출력"
</span>
<span class="k">
print
</span>
<span class="n">
c
</span>
<span class="p">
,
</span>
<span class="n">
d
</span>
<span class="c">
#요구사항 3번
</span>
<span class="n">
c
</span>
<span class="o">
.
</span>
<span class="n">
incr
</span>
<span class="p">
()
</span>
<span class="n">
d
</span>
<span class="o">
.
</span>
<span class="n">
incr
</span>
<span class="p">
()
</span>
<span class="k">
print
</span>
<span class="s">
"요구 사항 3번 출력"
</span>
<span class="k">
print
</span>
<span class="n">
c
</span>
<span class="p">
,
</span>
<span class="n">
d
</span>
<span class="c">
#요구사항 4번
</span>
<span class="n">
c
</span>
<span class="p">
()
</span>
<span class="n">
d
</span>
<span class="p">
()
</span>
<span class="k">
print
</span>
<span class="s">
"요구 사항 4번 출력"
</span>
<span class="k">
print
</span>
<span class="n">
c
</span>
<span class="p">
,
</span>
<span class="n">
d
</span>
<span class="c">
#요구사항 5번
</span>
<span class="n">
c
</span>
<span class="o">
=
</span>
<span class="n">
c
</span>
<span class="o">
+
</span>
<span class="mi">
5
</span>
<span class="n">
d
</span>
<span class="o">
=
</span>
<span class="n">
d
</span>
<span class="o">
-
</span>
<span class="mi">
5
</span>
<span class="k">
print
</span>
<span class="s">
"요구 사항 5번 출력"
</span>
<span class="k">
print
</span>
<span class="n">
c
</span>
<span class="p">
,
</span>
<span class="n">
d
</span>
<span class="c">
#요구사항 6번
</span>
<span class="k">
print
</span>
<span class="s">
"요구 사항 6번 출력"
</span>
<span class="k">
print
</span>
<span class="n">
c
</span>
<span class="o">
&gt;
</span>
<span class="mi">
10
</span>
<span class="k">
print
</span>
<span class="n">
d
</span>
<span class="o">
&gt;
</span>
<span class="mi">
10
</span>
<span class="k">
print
</span>
<span class="n">
c
</span>
<span class="o">
&lt;
</span>
<span class="mi">
10
</span>
<span class="k">
print
</span>
<span class="n">
d
</span>
<span class="o">
&lt;
</span>
<span class="mi">
10
</span>
<span class="k">
print
</span>
<span class="n">
c
</span>
<span class="o">
==
</span>
<span class="s">
"17"
</span>
<span class="k">
print
</span>
<span class="n">
d
</span>
<span class="o">
!=
</span>
<span class="s">
"9"
</span>
<span class="k">
print
</span>
<span class="n">
c
</span>
<span class="o">
&gt;
</span>
<span class="n">
d
</span>
</pre>
</div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>
요구 사항 2번 출력
10 10
요구 사항 3번 출력
11 12
요구 사항 4번 출력
12 14
요구 사항 5번 출력
17 9
요구 사항 6번 출력
True
False
False
True
True
False
True
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
[풀이]
<br>
-Needs1 :
<strong>
init
</strong>
함수에서 매개변수를 default로 1로 초기화 하여 충족시켰다.
<br>
-Needs2 :
<strong>
str
</strong>
함수를 이용하면 java의 toString과 같은 효과를 볼 수 있다.
<br>
-Needs3 : 요구사항대로 값을 증가시켰다.
<br>
-Needs4 :
<strong>
call
</strong>
함수를 사용하여, incr 함수를 인스턴스로 불러냈다.
<br>
-Needs5 :
<strong>
sum
</strong>
,
<strong>
sub
</strong>
함수를 사용하여 개발했다. 확장성을 생각하여, 템플릿 메소드 패턴을 적용하기 위한 operatorHelper() 라는 메소드를 두어, 동적으로 연산자가 결정되도록 진행했다. 연산은 정수뿐이 아닌 다른 type도 들어올 수 있도록 개발했다.
<br>
-Needs6 :
<strong>
cmp
</strong>
함수를 사용했다. 위와 같이 다른 type에 대응할 수 있도록 제작했다. cmp 함수를 사용하면, 별다른 알고리즘 없이 진행할 수 있다.
<br>
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [4번 문제] 다음은 내장 자료형 list를 서브클래싱하여 만든 MySet 클래스 정의 내용이다. 다음 클래스 정의에서
<strong>
init
</strong>
(),
<strong>
str()
</strong>
(), elimicate_duplicate()의 세 개의 메소드 코드 내용을 자신이 다른 사람에게 가르친다고 생각하며 설명해보시오.
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [5번 문제] 4번 문제에 정의된 MySet 클래스에 메소드를 추가하여 다음 각 요구사항 모두를 만족시키는 코딩을 제시하시오 (정답을 각 요구사항별로 입력할 필요 없이 5번 문제에 대해 1개의 MySet 클래스 정의 코드를 제시하면 된다.)
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [6번 문제] 5번 문제에서 정의한 MySet 클래스에 대해 다음 예제를 수행하면 오류없이 올바르게 동작하는 것을 확인할 수 있다. 다음 예제 내에 있는 len(), bool() 내장함수와 in 키워드 사용 예제가 별다른 메소드 정의를 하지 않았는 데도 올바르게 수행되는 이유를 설명하시오. - 해설은 4, 5, 6번 모두 같이 적었다.
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In [1]:
</div>
<div class="inner_cell">
<div class="input_area">
<div class="highlight">
<pre>
<span class="c">
# -*- coding: utf-8 -*-
</span>
<span class="kn">
import
</span>
<span class="nn">
copy
</span>
<span class="k">
class
</span>
<span class="nc">
MySet
</span>
<span class="p">
(
</span>
<span class="nb">
list
</span>
<span class="p">
):
</span>
<span class="k">
def
</span>
<span class="nf">
__init__
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
,
</span>
<span class="n">
l
</span>
<span class="p">
):
</span>
<span class="k">
for
</span>
<span class="n">
e
</span>
<span class="ow">
in
</span>
<span class="n">
l
</span>
<span class="p">
:
</span>
<span class="bp">
self
</span>
<span class="o">
.
</span>
<span class="n">
append
</span>
<span class="p">
(
</span>
<span class="n">
e
</span>
<span class="p">
)
</span>
<span class="n">
MySet
</span>
<span class="o">
.
</span>
<span class="n">
eliminate_duplicate
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
)
</span>
<span class="k">
def
</span>
<span class="nf">
__str__
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
):
</span>
<span class="n">
result
</span>
<span class="o">
=
</span>
<span class="s">
"MySet: {"
</span>
<span class="k">
for
</span>
<span class="n">
e
</span>
<span class="ow">
in
</span>
<span class="bp">
self
</span>
<span class="p">
:
</span>
<span class="n">
result
</span>
<span class="o">
=
</span>
<span class="n">
result
</span>
<span class="o">
+
</span>
<span class="nb">
str
</span>
<span class="p">
(
</span>
<span class="n">
e
</span>
<span class="p">
)
</span>
<span class="o">
+
</span>
<span class="s">
" ,"
</span>
<span class="n">
result
</span>
<span class="o">
=
</span>
<span class="n">
result
</span>
<span class="p">
[
</span>
<span class="mi">
0
</span>
<span class="p">
:
</span>
<span class="nb">
len
</span>
<span class="p">
(
</span>
<span class="n">
result
</span>
<span class="p">
)
</span>
<span class="o">
-
</span>
<span class="mi">
2
</span>
<span class="p">
]
</span>
<span class="o">
+
</span>
<span class="s">
"}"
</span>
<span class="k">
return
</span>
<span class="n">
result
</span>
<span class="k">
def
</span>
<span class="nf">
__or__
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
,
</span>
<span class="n">
other
</span>
<span class="p">
):
</span>
<span class="k">
return
</span>
<span class="n">
MySet
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="o">
+
</span>
<span class="n">
other
</span>
<span class="p">
)
</span>
<span class="k">
def
</span>
<span class="nf">
__and__
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
,
</span>
<span class="n">
other
</span>
<span class="p">
):
</span>
<span class="n">
s
</span>
<span class="o">
=
</span>
<span class="p">
[]
</span>
<span class="k">
for
</span>
<span class="n">
e
</span>
<span class="ow">
in
</span>
<span class="n">
other
</span>
<span class="p">
:
</span>
<span class="k">
if
</span>
<span class="n">
e
</span>
<span class="ow">
in
</span>
<span class="bp">
self
</span>
<span class="p">
:
</span>
<span class="n">
s
</span>
<span class="o">
.
</span>
<span class="n">
append
</span>
<span class="p">
(
</span>
<span class="n">
e
</span>
<span class="p">
)
</span>
<span class="k">
return
</span>
<span class="n">
MySet
</span>
<span class="p">
(
</span>
<span class="n">
s
</span>
<span class="p">
)
</span>
<span class="k">
def
</span>
<span class="nf">
__sub__
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
,
</span>
<span class="n">
other
</span>
<span class="p">
):
</span>
<span class="n">
s
</span>
<span class="o">
=
</span>
<span class="n">
copy
</span>
<span class="o">
.
</span>
<span class="n">
deepcopy
</span>
<span class="p">
(
</span>
<span class="bp">
self
</span>
<span class="p">
)
</span>
<span class="k">
for
</span>
<span class="n">
e
</span>
<span class="ow">
in
</span>
<span class="bp">
self
</span>
<span class="p">
:
</span>
<span class="k">
if
</span>
<span class="n">
e
</span>
<span class="ow">
in
</span>
<span class="n">
other
</span>
<span class="p">
:
</span>
<span class="n">
s
</span>
<span class="o">
.
</span>
<span class="n">
remove
</span>
<span class="p">
(
</span>
<span class="n">
e
</span>
<span class="p">
)
</span>
<span class="k">
return
</span>
<span class="n">
MySet
</span>
<span class="p">
(
</span>
<span class="n">
s
</span>
<span class="p">
)
</span>
<span class="nd">
@staticmethod
</span>
<span class="k">
def
</span>
<span class="nf">
eliminate_duplicate
</span>
<span class="p">
(
</span>
<span class="n">
l
</span>
<span class="p">
):
</span>
<span class="n">
s
</span>
<span class="o">
=
</span>
<span class="p">
[]
</span>
<span class="k">
for
</span>
<span class="n">
e
</span>
<span class="ow">
in
</span>
<span class="n">
l
</span>
<span class="p">
:
</span>
<span class="k">
if
</span>
<span class="n">
e
</span>
<span class="ow">
not
</span>
<span class="ow">
in
</span>
<span class="n">
s
</span>
<span class="p">
:
</span>
<span class="n">
s
</span>
<span class="o">
.
</span>
<span class="n">
append
</span>
<span class="p">
(
</span>
<span class="n">
e
</span>
<span class="p">
)
</span>
<span class="n">
l
</span>
<span class="p">
[:]
</span>
<span class="o">
=
</span>
<span class="p">
[]
</span>
<span class="k">
for
</span>
<span class="n">
e
</span>
<span class="ow">
in
</span>
<span class="n">
s
</span>
<span class="p">
:
</span>
<span class="n">
l
</span>
<span class="o">
.
</span>
<span class="n">
append
</span>
<span class="p">
(
</span>
<span class="n">
e
</span>
<span class="p">
)
</span>
<span class="c">
#요구사항 1번
</span>
<span class="k">
print
</span>
<span class="s">
"요구사항 1번 출력"
</span>
<span class="n">
s
</span>
<span class="o">
=
</span>
<span class="n">
MySet
</span>
<span class="p">
([
</span>
<span class="mi">
1
</span>
<span class="p">
,
</span>
<span class="mi">
2
</span>
<span class="p">
,
</span>
<span class="mi">
2
</span>
<span class="p">
,
</span>
<span class="mi">
3
</span>
<span class="p">
])
</span>
<span class="n">
t
</span>
<span class="o">
=
</span>
<span class="n">
MySet
</span>
<span class="p">
([
</span>
<span class="mi">
2
</span>
<span class="p">
,
</span>
<span class="mi">
3
</span>
<span class="p">
,
</span>
<span class="mi">
4
</span>
<span class="p">
,
</span>
<span class="mi">
5
</span>
<span class="p">
,
</span>
<span class="mi">
6
</span>
<span class="p">
,
</span>
<span class="mi">
7
</span>
<span class="p">
,
</span>
<span class="mi">
8
</span>
<span class="p">
,
</span>
<span class="mi">
8
</span>
<span class="p">
,
</span>
<span class="mi">
8
</span>
<span class="p">
,
</span>
<span class="mi">
8
</span>
<span class="p">
,
</span>
<span class="mi">
8
</span>
<span class="p">
,
</span>
<span class="mi">
9
</span>
<span class="p">
])
</span>
<span class="n">
s
</span>
<span class="o">
=
</span>
<span class="n">
s
</span>


<p>
자 그럼 이제 시작하도록 하겠습니다.
</p>

<p>
순서
</p>

<p>
<strike>
1. HTML 데이터를 받아옵니다.
</strike>
</p>
<p>
<strike>
2. &lt;body&gt; 데이터만 가져옵니다.
</strike>
</p>
<p>
<strike>
3. &lt;script&gt; 데이터 삭제합니다.
</strike>
</p>
<p>
<strike>
4. &lt;img&gt; 태그만 가져옵니다.
</strike>
</p>
<p>
5. 가져온 태그를 이용하여 메인 이미지를 추출한다.
</p>
<p>
&gt; 추출하는 것에 대해 이미지 크기가 큰걸로 추출하려고 합니다.
</p>

<p>
이미지 추출의 경우.
</p>
<p>
위와 같은 순서로 진행을 하려고 했지만 , 제 능력이 되지 않아. 메타태그의 이미지를 가져오는 것으로 돌아갔습니다.
</p>
<p>
시간내에 맞춰야하는 부분도 있고, 알고리즘 공부도 아에 안할 수가 없는게 핑계라면 핑계입니다.
</p>

<p>
없는 기사들에 대해서는 저희 로고를 가운데 박아서 띄워주는 것으로 처리하였습니다.
</p>



<p>
다음과 같은 결과물을 얻을 수 있었습니다.
</p>

<p>
시간이된다면, 정규식을 통해 정리해놓은 img 태그에서 feature 이미지를 추출하는 부분을 진행해볼 예정입니다.
</p>

</div>
<br>

</div>
</div>
</div>
</main>
</div>
