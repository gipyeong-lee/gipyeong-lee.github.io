---
layout: post
title: "[短期] 04. Feature IMAGE 擷取"
description: "你好？這次我們要來實作上次預定要做的...從 URL 擷取 feature 圖片的功能。下方是大田 Membership 南斗賢提供的正規表示式相關資料。這次的功能實作得到了許多幫助。顯示更多 Python Assignment 5 Author..."
date: 2015-02-06 02:09:08 +0900
section: blog
category: projects
lang: zh-tw
ref: 2015-02-06-legacy-11-projects-04-feature-image
tags:
  - "TJSSM"
  - "projects"
translation_source_hash: a4f7f8024d1a15716e8b11ca6bfc110665fa6af83c4ce20411e96e7cc14178db
---

<p>
你好？
</p>
<p>
這次我們要來實作上次預定要做的...從 URL 擷取 feature 圖片的功能。
</p>
<p>
下方是大田 Membership 南斗賢提供的正規表示式相關資料。
</p>
<p>
這次的功能實作得到了許多幫助。
</p>

<span class="txt_fold">
顯示更多
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
• [第 1 題] 請解釋類別 (Class) 與模組 (Module) 的共同點與差異。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
類別與模組的共同點在於，它們都是將功能相似或相關的函式與常數值收集起來儲存，並擁有獨立的命名空間。這麼做是為了專注於程式碼的再利用性與維護性。若要說差異，模組是以檔案為單位定義命名空間，而類別則是在類別空間中構成命名空間。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第 2 題] 請解釋多型 (Polymorphism)，並提出一個你自己撰寫的 Python 程式碼範例來展示多型。
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
"飛行中"
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
"無法飛行"
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
飛行中
無法飛行
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
[解答] 指的是在繼承關係中，不同類別的實例對於相同的成員函式呼叫能做出不同的反應。運算子多載 (Operator Overloading) 也是支援多型的重要技術。
<br>
[範例] 這是使用設計模式中策略模式 (Strategy Pattern) 的範例。對於繼承自 FlyBehavior 與 QuackBeHavior 的各個行為，在執行時期各個物件都能支援不同的反應。在下方的範例中，比起繼承來的 quack 或 squack，由它們組成的 duck 物件更為重要。當 duck 物件初始化時，可以根據它持有的物件而採取不同的行動。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第 3 題] 請撰寫一個 Counter 類別，滿足以下所有需求。（不需要針對每個需求分別輸入答案，只需針對第 3 題提供一個定義類別的程式碼即可。）
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
"需求 2 輸出"
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
"需求 3 輸出"
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
"需求 4 輸出"
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
"需求 5 輸出"
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
"需求 6 輸出"
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
需求 2 輸出
10 10
需求 3 輸出
11 12
需求 4 輸出
12 14
需求 5 輸出
17 9
需求 6 輸出
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
-Needs1 : 在 **init** 函式中將參數預設初始化為 1 來達成。
<br>
-Needs2 : 使用 **str** 函式可以達到與 Java 的 toString 相同的效果。
<br>
-Needs3 : 依照需求增加了數值。
<br>
-Needs4 : 使用 **call** 函式，以實例形式呼叫了 incr 函式。
<br>
-Needs5 : 使用 **sum**, **sub** 函式來開發。考慮到擴充性，設定了一個名為 operatorHelper() 的方法，以便應用模板方法模式，讓運算子動態決定。開發時不僅支援整數，還支援其他類型的運算。
<br>
-Needs6 : 使用了 **cmp** 函式。同樣地，為了應對其他類型，這樣設計了。使用 cmp 函式可以無需額外的演算法即可進行。
<br>
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第 4 題] 下面是將內建資料型態 list 進行子類別化 (Subclassing) 所製成的 MySet 類別定義。請嘗試以教導他人的方式，解釋該類別定義中 **init**(), **str()**(), eliminate_duplicate() 這三個方法的程式碼內容。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第 5 題] 請為第 4 題定義的 MySet 類別新增方法，並提供滿足以下所有需求的程式碼（不需要針對每個需求分別輸入答案，只需針對第 5 題提供一個 MySet 類別定義程式碼即可。）
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第 6 題] 針對第 5 題定義的 MySet 類別，若執行下方的範例，可以確認其能正確運作且無錯誤。請解釋為何範例中的 len(), bool() 內建函式以及 in 關鍵字在使用時，即便沒有定義額外的方法也能正確執行。 - 解析的部分將 4、5、6 題寫在一起。
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
#需求 1
</span>
<span class="k">
print
</span>
<span class="s">
"需求 1 輸出"
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
<span---
layout: post
title: "[短期] 04. Feature IMAGE 擷取"
description: "大家好？這次要來實作上次預定要做的功能.. 從 URL 取得 feature 圖片。以下是大田 Membership 南斗賢（Doohyun Nam）提供的正規表示式相關資料。這次功能實作中得到了很多幫助。展開 Python Assignment 5 Author..."
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
這次要來實作上次預定要做的功能.. 從 URL 取得 feature 圖片。
</p>
<p>
以下是大田 Membership 南斗賢（Doohyun Nam）提供的正規表示式相關資料。
</p>
<p>
這次功能實作中得到了很多幫助。
</p>

<span class="txt_fold">
展開
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
• [第 1 題] 請說明類別（class）與模組（module）的共同點與差異。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
類別與模組的共同點在於，它們都是將執行相似或相關工作的函式或常數值收集並儲存起來，並擁有獨立的命名空間。這樣做的原因是為了專注於重複使用性與維護性。差異在於，模組是以檔案為單位定義命名空間，而類別則是在類別空間中構成命名空間。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第 2 題] 請說明多型（polymorphism），並提供您自己編寫的 Python 程式碼範例來展示多型。
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
"飛行"
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
"無法飛行"
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
"嗶嗶"
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
飛行
無法飛行
呱呱
嗶嗶
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
[解析] 這是一種功能，讓繼承關係內不同類別的實例，對於相同的成員函式呼叫做出不同的反應；運算子多載（operator overloading）也是支援多型的關鍵技術。
<br>
[範例] 這是使用設計模式中策略模式（Strategy Pattern）的範例。針對繼承自 FlyBehavior、QuackBeHavior 的各個行為，在執行時期各個物件支援不同的反應。此範例中，比起繼承來的 quack 或 squack，組成這些關係的 duck 物件更為重要。根據 duck 物件初始化時所持有的物件，可以採取不同的行為。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第 3 題] 請編寫一個滿足以下所有要求的 Counter 類別（不需要針對每個要求分別輸入答案，只需針對第 3 題提供一個類別定義程式碼即可）。
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
"需求 2 輸出"
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
"需求 3 輸出"
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
"需求 4 輸出"
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
"需求 5 輸出"
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
"需求 6 輸出"
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
需求 2 輸出
10 10
需求 3 輸出
11 12
需求 4 輸出
12 14
需求 5 輸出
17 9
需求 6 輸出
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
[解析]
<br>
-Needs1 : 在 `__init__` 函式中將參數預設初始化為 1 來滿足。
<br>
-Needs2 : 使用 `__str__` 函式，即可達到與 Java 的 `toString` 相同的效果。
<br>
-Needs3 : 依照需求增加了數值。
<br>
-Needs4 : 使用 `__call__` 函式，將 incr 函式以實例呼叫出來。
<br>
-Needs5 : 使用 `__add__`、`__sub__` 函式進行開發。為了考慮擴充性，設置了名為 `operatorHelper()` 的方法來應用模板方法模式（Template Method Pattern），讓運算子動態決定。開發時不僅考慮了整數，也考慮了其他類型進來的可能。
<br>
-Needs6 : 使用 `__cmp__` 函式。如同上述，製作成能夠應對其他類型。使用 `cmp` 函式的話，無需額外的演算法即可進行。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第 4 題] 以下是將內建資料型態 list 進行子類別化（subclassing）所製作的 MySet 類別定義內容。請試著向別人解說該類別定義中的 `__init__()`、`__str__()`、`eliminate_duplicate()` 這三個方法代碼的內容。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第 5 題] 請針對第 4 題中定義的 MySet 類別新增方法，並提供滿足以下各項要求的編碼（不需要針對每個要求分別輸入答案，只需針對第 5 題提供一個 MySet 類別定義程式碼即可）。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [第 6 題] 針對第 5 題定義的 MySet 類別執行以下範例，可以確認其能正確運作而無錯誤。請說明為什麼在範例中使用的內建函式 `len()`、`bool()` 與 `in` 關鍵字，在沒有特別定義方法的情況下也能正確執行。 - 解析已將 4、5、6 題寫在一起。
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
"需求 1 輸出"
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
<span class