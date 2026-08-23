---
layout: post
title: "[短期] 04. Feature IMAGE 提取"
description: "大家好？本次我们将实现上次提到的功能，即从 URL 获取 feature 图像。以下是来自大田 Membership 的南斗贤（音译）提供的有关正则表达式的资料。他在本次功能实现中给予了很大帮助。阅读更多 Python Assignment 5 Author..."
date: 2015-02-06 02:09:08 +0900
section: blog
category: projects
lang: zh-cn
ref: 2015-02-06-legacy-11-projects-04-feature-image
tags:
  - "TJSSM"
  - "projects"
translation_source_hash: a4f7f8024d1a15716e8b11ca6bfc110665fa6af83c4ce20411e96e7cc14178db
---

<p>
大家好？
</p>
<p>
本次我们将实现上次提到的功能，即从 URL 获取 feature 图像。
</p>
<p>
以下是来自大田 Membership 的南斗贤提供的有关正则表达式的资料。
</p>
<p>
他在本次功能实现中给予了很大帮助。
</p>

<span class="txt_fold">
阅读更多
</span>
<div class="moreless_content">

<div class="cell border-box-sizing text_cell rendered">
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3>
<br class="Apple-interchange-newline">
Python 作业 5
</h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3>
作者 : 2009135046, 都贤南（音译）
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
• [第1题] 请说明类（Class）和模块（Module）的共同点与区别。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
类和模块的共同点是它们都用于收集并存储相关功能或常量值，且都拥有独立的名字空间（Namespace）。这样做的目的是为了提高代码的可重用性和可维护性。区别在于，模块以文件为单位定义名字空间，而类则在类空间内构建名字空间。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第2题] 请说明多态性（Polymorphism），并给出一段展现多态性的 Python 代码示例。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In [23]:
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
"飞行中"
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
"无法飞行"
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
"呱呱"
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
"唧唧"
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
飞行中
无法飞行
呱呱
唧唧
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
[解答] 指在继承关系内，不同类的实例对同一个成员函数调用作出不同反应的功能。运算符重载也是支持多态的重要技术。
<br>
[示例] 这是使用了设计模式中策略模式（Strategy Pattern）的示例。对于继承了 FlyBehavior 和 QuackBeHavior 的各个行为，在运行时每个对象都支持不同的响应。在上述示例中，相比继承的 quack 或 squack，与之处于组合关系的 duck 对象更为重要。根据 duck 对象初始化时所持有的对象不同，可以采取不同的行动。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第3题] 请编写满足以下所有要求的 Counter 类（不需要针对每个要求输入答案，只需提交一个满足第3题所有要求的类定义代码即可）。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In [21]:
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
#需求 1
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
#需求 2
</span>
<span class="k">
print
</span>
<span class="s">
"需求 2 输出"
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
#需求 3
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
"需求 3 输出"
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
#需求 4
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
"需求 4 输出"
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
#需求 5
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
"需求 5 输出"
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
#需求 6
</span>
<span class="k">
print
</span>
<span class="s">
"需求 6 输出"
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
需求 2 输出
10 10
需求 3 输出
11 12
需求 4 输出
12 14
需求 5 输出
17 9
需求 6 输出
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
[解答]
<br>
- 需求 1：在 __init__ 函数中将参数默认初始化为 1 来实现。
<br>
- 需求 2：使用 __str__ 函数可以达到与 Java 的 toString 相同的效果。
<br>
- 需求 3：按照要求增加了数值。
<br>
- 需求 4：使用 __call__ 函数，通过实例调用 incr 函数。
<br>
- 需求 5：使用 __add__ 和 __sub__ 函数开发。为了考虑到可扩展性，引入了 operatorHelper() 方法来应用模板方法模式（Template Method Pattern），使得运算符可以动态确定。开发时确保了运算不仅支持整数，也支持其他类型。
<br>
- 需求 6：使用了 cmp 函数。同样为了能够兼容不同类型进行了开发。使用 cmp 函数可以无需复杂的算法直接进行处理。
<br>
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第4题] 以下是继承内置数据类型 list 后创建的 MySet 类定义。请尝试以教导他人的方式，解释上述类定义中 __init__(), __str__(), eliminate_duplicate() 这三个方法的代码内容。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第5题] 请为第4题定义的 MySet 类添加方法，以满足以下所有要求（不需要针对每个要求输入答案，只需提交一个满足第5题所有要求的 MySet 类定义代码即可）。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第6题] 对第5题定义的 MySet 类执行以下示例，可以确认其能够正确运行且无错误。请说明为什么示例中 len()、bool() 内置函数和 in 关键字的使用在没有进行特殊方法定义的情况下也能正确执行。 - 解说已将第4、5、6题合并整理。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In [1]:
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
#需求 1
</span>
<span class="k">
print
</span>
<span class="s">
"需求 1 输出"
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
<span---
layout: post
title: "[短期] 04. Feature IMAGE 提取"
description: "大家好？这次我们来实现上次提到的从URL获取feature图片的功能。以下是来自大田Membership的南斗贤（Doohyun Nam）提供的正则表达式相关资料。他对此次功能实现提供了很大帮助。查看更多 Python Assignment 5 作者..."
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
大家好？
</p>
<p>
这次我们来实现上次提到的从 URL 获取 feature 图片的功能。
</p>
<p>
以下是来自大田 Membership 的南斗贤（Doohyun Nam）提供的正则表达式相关资料。
</p>
<p>
他对此次功能实现提供了很大帮助。
</p>

<span class="txt_fold">
查看更多
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
作者 : 2009135046, Doohyun Nam
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
• [问题 1] 请说明类（Class）和模块（Module）的共同点和区别。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
类和模块的共同点是它们都用于收集并存储功能相似或相关的函数和常量值，并且拥有独立的名字空间（namespace）。其目的主要在于可重用性和维护性。区别在于，模块以文件为单位定义名字空间，而类在类空间中构建名字空间。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [问题 2] 请解释多态性（Polymorphism），并给出一段展现多态性的个人 Python 代码示例。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In [23]:
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
"飞行中"
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
"无法飞行"
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
"嘎嘎"
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
"哔哔"
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
飞行中
无法飞行
嘎嘎
哔哔
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
[解答] 同一继承体系下，不同类的实例对相同的成员函数调用做出不同响应的功能；运算符重载也是支持多态的重要技术。
<br>
[示例] 这是使用设计模式中策略模式（Strategy Pattern）的示例。对于继承了 FlyBehavior 和 QuackBeHavior 的各个行为，对象在运行时支持不同的响应。在以下示例中，相比于被继承的 quack 或 squack，与之处于组合关系的 duck 对象更为重要。Duck 对象初始化时，根据其持有的对象不同，可以采取不同的行为。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [问题 3] 请编写一个满足以下所有要求的 Counter 类（无需按要求分别输入，只需提交 3 题的 1 个类定义代码即可）。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In [21]:
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
#要求 1
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
#要求 2
</span>
<span class="k">
print
</span>
<span class="s">
"要求 2 输出"
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
#要求 3
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
"要求 3 输出"
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
#要求 4
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
"要求 4 输出"
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
#要求 5
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
"要求 5 输出"
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
#要求 6
</span>
<span class="k">
print
</span>
<span class="s">
"要求 6 输出"
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
要求 2 输出
10 10
要求 3 输出
11 12
要求 4 输出
12 14
要求 5 输出
17 9
要求 6 输出
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
[解答]
<br>
-Needs1: 在 `__init__` 函数中将参数默认值设为 1 进行了满足。
<br>
-Needs2: 使用 `__str__` 函数可以达到类似 Java 中 `toString` 的效果。
<br>
-Needs3: 按照要求增加了数值。
<br>
-Needs4: 使用 `__call__` 函数，通过实例调用了 `incr` 函数。
<br>
-Needs5: 使用 `__sum__` 和 `__sub__` 函数开发。考虑到扩展性，设置了 `operatorHelper()` 方法以应用模板方法模式（Template Method Pattern），动态决定运算符。运算开发为不仅支持整数，还支持其他类型。
<br>
-Needs6: 使用了 `cmp` 函数。同样制作了可以响应不同类型的功能。使用 `cmp` 函数即可无需复杂算法。
<br>
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [问题 4] 以下是继承内置数据类型 list 所创建的 MySet 类定义内容。请以教别人的心态，解释类定义中 `__init__()`, `__str__()`, `eliminate_duplicate()` 这三个方法代码的内容。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [问题 5] 请提交满足问题 4 中定义的 MySet 类添加方法后满足以下各要求的代码（无需按要求分别输入，只需提交 5 题的 1 个 MySet 类定义代码即可）。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [问题 6] 对问题 5 中定义的 MySet 类执行以下示例，可以确认其能够正确工作且无错误。请解释为什么在示例中使用的 `len()`, `bool()` 内置函数和 `in` 关键字，即使没有做额外的方法定义也能正确执行。 - 解析写在 4、5、6 题一起。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In [1]:
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
#要求 1
</span>
<span class="k">
print
</span>
<span class="s">
"要求 1 输出"
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
<span