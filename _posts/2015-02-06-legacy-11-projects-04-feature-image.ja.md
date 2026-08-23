---
layout: post
title: "[短期] 04. Feature IMAGE 抽出"
description: "こんにちは。今回は前回お話しした、URLからfeature画像を取得する機能を実装します。以下は、大田メンターシップのナム・ドゥヒョンさんが作成した正規表現関連の資料です。今回の機能実装に多大な助けをいただきました。続きを読む Python Assignment 5 Author..."
date: 2015-02-06 02:09:08 +0900
section: blog
category: projects
lang: ja
ref: 2015-02-06-legacy-11-projects-04-feature-image
tags:
  - "TJSSM"
  - "projects"
translation_source_hash: a4f7f8024d1a15716e8b11ca6bfc110665fa6af83c4ce20411e96e7cc14178db
---

<p>
こんにちは。
</p>
<p>
今回は前回お話しした、URLからfeature画像を取得する機能を実装します。
</p>
<p>
以下は、大田メンターシップのナム・ドゥヒョンさんが作成した正規表現関連の資料です。
</p>
<p>
今回の機能実装に多大な助けをいただきました。
</p>

<span class="txt_fold">
続きを読む
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
• [問題1] クラスとモジュールの共通点と相違点について説明しなさい。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
クラスとモジュールの共通点は、類似または関連する機能を持つ関数や定数値をまとめて保存することであり、それぞれ独立した名前空間を持っている点です。これを行う理由は、再利用性と保守性に焦点を当てているからです。相違点としては、モジュールはファイル単位で名前空間を定義し、クラスはクラス空間内に名前空間を構成する点です。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [問題2] ポリモーフィズムについて説明し、ポリモーフィズムを示す自分自身のPythonコード例を提示しなさい。
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
"飛ぶ"
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
"飛べない"
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
"ガーガー"
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
"ピヨピヨ"
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
飛ぶ
飛べない
ガーガー
ピヨピヨ
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
[解答] 継承関係にある異なるクラスのインスタンスが、同じメンバー関数呼び出しに対してそれぞれ異なる反応をするようにする機能。演算子オーバーロードもポリモーフィズムをサポートする重要な技術である。
<br>
[例題] デザインパターンの一つであるストラテジーパターンを使用した例である。FlyBehavior、QuackBeHaviorを継承したそれぞれの行動に対して、実行時に各オブジェクトは異なる反応をサポートしている。次の例は、継承されたquackやsquackよりも、これを構成関係に持つduckオブジェクトの方が重要である。duckオブジェクトが初期化されるとき、どのようなオブジェクトを持っているかによって異なる行動を取ることができる。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [問題3] 次の各要件をすべて満たすCounterクラスをコーディングしなさい（正解を各要件ごとに分ける必要はなく、問題3に対して1つのクラス定義コードを提示すればよい）。
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
#要件1
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
#要件2
</span>
<span class="k">
print
</span>
<span class="s">
"要件2出力"
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
#要件3
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
"要件3出力"
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
#要件4
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
"要件4出力"
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
#要件5
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
"要件5出力"
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
#要件6
</span>
<span class="k">
print
</span>
<span class="s">
"要件6出力"
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
要件2出力
10 10
要件3出力
11 12
要件4出力
12 14
要件5出力
17 9
要件6出力
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
-Needs1: __init__関数でパラメーターをデフォルトで1に初期化することで要件を満たした。
<br>
-Needs2: __str__関数を利用すると、JavaのtoStringと同じ効果を得ることができる。
<br>
-Needs3: 要件通りに値を増加させた。
<br>
-Needs4: __call__関数を使用して、incr関数をインスタンスとして呼び出した。
<br>
-Needs5: __add__、__sub__関数を使用して開発した。拡張性を考慮し、テンプレートメソッドパターンを適用するためのoperatorHelper()というメソッドを設け、動的に演算子が決定されるようにした。演算は整数だけでなく、他のタイプが入ってくる可能性も考慮して開発した。
<br>
-Needs6: __cmp__関数を使用した。上記と同様に、異なるタイプに対応できるように作成した。cmp関数を使用すれば、特別なアルゴリズムなしに進めることができる。
<br>
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [問題4] 次は内蔵データ型listをサブクラス化して作成したMySetクラスの定義内容である。次のクラス定義において、__init__()、__str__()、eliminate_duplicate()の3つのメソッドのコード内容について、自分が他人に教えると考えて説明しなさい。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [問題5] 問題4で定義したMySetクラスにメソッドを追加し、次の各要件をすべて満たすコーディングを提示しなさい（正解を各要件ごとに分ける必要はなく、問題5に対して1つのMySetクラス定義コードを提示すればよい）。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [問題6] 問題5で定義したMySetクラスに対して次の例題を実行すると、エラーなく正しく動作することを確認できる。次の例題内にあるlen()、bool()内蔵関数とinキーワードの使用例が、特別なメソッド定義をしていないにもかかわらず正しく実行される理由を説明しなさい。 - 解説は4、5、6番すべてまとめて記述した。
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
not
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
#要件1
</span>
<span class="k">
print
</span>
<span class="s">
"要件1出力"
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
title: "[短期] 04. Feature IMAGE 抽出"
description: "こんにちは。今回は前回お話しした、URLからFeature画像を取得する機能を実装します。以下は、大田メンターシップのナム・ドゥヒョンさんが作成された正規表現に関する資料です。今回の機能実装において多くの助けとなりました。続きを読む Python Assignment 5 著者..."
date: 2015-02-06 02:09:08 +0900
section: blog
category: projects
lang: ja
ref: 2015-02-06-legacy-11-projects-04-feature-image
tags:
  - "TJSSM"
  - "projects"
---

<p>
こんにちは。
</p>
<p>
今回は、前回お話ししたURLからFeature画像を取得する機能を実装していきます。
</p>
<p>
以下は、大田メンターシップのナム・ドゥヒョンさんが作成された正規表現に関する資料です。
</p>
<p>
今回の機能実装において多くの助けとなりました。
</p>

<span class="txt_fold">
続きを読む
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
著者 : 2009135046, Nam Doohyun
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
• [問1] クラスとモジュールの共通点と相違点について説明しなさい。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
クラスとモジュールの共通点は、似ている、または関連する関数や定数値を集めて保存する点であり、それぞれ独自の名前空間を持っていることです。これは再利用性と保守性の向上に焦点を当てています。相違点は、モジュールはファイル単位で名前空間を定義するのに対し、クラスはクラス空間内に名前空間を構成する点です。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [問2] ポリモーフィズム（多態性）について説明し、ポリモーフィズムを示す独自のPythonコード例を提示しなさい。
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
"飛ぶ"
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
"飛べない"
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
"ガーガー"
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
"ピーピー"
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
飛ぶ
飛べない
ガーガー
ピーピー
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
[解説] 継承関係にある異なるクラスのインスタンスが、同じメソッド呼び出しに対してそれぞれ異なる反応をする機能。演算子オーバーロードもポリモーフィズムをサポートする重要な技術である。
<br>
[例] デザインパターンのうち「ストラテジーパターン（Strategy Pattern）」を使用した例である。FlyBehavior、QuackBeHaviorを継承したそれぞれの行動に対し、実行時に各オブジェクトは異なる反応をする。この例では、継承されたquackやsquackよりも、それらを構成要素として持つDuckオブジェクトが重要となる。Duckオブジェクトの初期化時にどのオブジェクトを持っているかによって、異なる行動を取ることができる。
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [問3] 次の各要件をすべて満たすCounterクラスをコーディングしなさい（回答は各要件ごとに分ける必要はなく、第3問として1つのクラス定義コードを提示すればよい）。
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
#要件1
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
#要件2
</span>
<span class="k">
print
</span>
<span class="s">
"要件2 出力"
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
#要件3
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
"要件3 出力"
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
#要件4
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
"要件4 出力"
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
#要件5
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
"要件5 出力"
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
#要件6
</span>
<span class="k">
print
</span>
<span class="s">
"要件6 出力"
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
要件2 出力
10 10
要件3 出力
11 12
要件4 出力
12 14
要件5 出力
17 9
要件6 出力
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
[解説]
<br>
- 要件1: <code>__init__</code>関数で引数をデフォルト1で初期化することで満たした。
<br>
- 要件2: <code>__str__</code>関数を利用すると、JavaのtoStringと同様の効果を得られる。
<br>
- 要件3: 要件通りに値を増加させた。
<br>
- 要件4: <code>__call__</code>関数を使用して、incr関数をインスタンスから呼び出せるようにした。
<br>
- 要件5: <code>__add__</code>、<code>__sub__</code>関数を使用して開発した。拡張性を考慮し、「テンプレートメソッドパターン」を適用するためoperatorHelper()というメソッドを設け、動的に演算子が決定されるようにした。演算は整数だけでなく他の型も入り得るようにした。
<br>
- 要件6: <code>__cmp__</code>関数を使用した。上記と同様に他の型に対応できるように制作した。cmp関数を使用すれば、特別なアルゴリズムなしに進めることができる。
<br>
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [問4] 次は内蔵データ型listをサブクラス化して作成したMySetクラス定義の内容である。次のクラス定義から、<code>__init__()</code>、<code>__str__()</code>、<code>eliminate_duplicate()</code>の3つのメソッドコード内容について、自分が他人に教えるつもりで説明しなさい。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [問5] 4番の問題で定義されたMySetクラスにメソッドを追加し、次の各要件すべてを満たすコーディングを提示しなさい（回答は各要件ごとに分ける必要はなく、第5問として1つのMySetクラス定義コードを提示すればよい）。
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [問6] 5番の問題で定義したMySetクラスに対して次の例を実行すると、エラーなく正しく動作することを確認できる。次の例にあるlen()、bool()内蔵関数とinキーワード使用例が、特別なメソッド定義をしなくても正しく実行される理由を説明しなさい。 - 解説は4、5、6番すべてまとめて記述した。
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
#要件1
</span>
<span class="k">
print
</span>
<span class="s">
"要件1 出力"
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