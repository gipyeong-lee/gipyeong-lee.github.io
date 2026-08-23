---
layout: post
title: "[Short-term] 04. Extracting Feature IMAGE"
description: "Hello? This time, we will implement the feature we decided to work on last time: extracting a feature image from a URL. Below are materials on regular expressions from Doohyun Nam of the Daejeon Membership. They were a great help in implementing this feature. Read more Python Assignment 5 Author..."
date: 2015-02-06 02:09:08 +0900
section: blog
category: projects
lang: en
ref: 2015-02-06-legacy-11-projects-04-feature-image
tags:
  - "TJSSM"
  - "projects"
translation_source_hash: a4f7f8024d1a15716e8b11ca6bfc110665fa6af83c4ce20411e96e7cc14178db
---

<p>
Hello?
</p>
<p>
This time, we will implement the feature we decided to work on last time: extracting a feature image from a URL.
</p>
<p>
Below are materials on regular expressions from Doohyun Nam of the Daejeon Membership.
</p>
<p>
They were a great help in implementing this feature.
</p>

<span class="txt_fold">
Read more
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
• [Problem 1] Explain the similarities and differences between classes and modules.
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
The commonality between classes and modules is that they both aggregate and store functions or constant values that perform similar or related tasks, and they have separate namespaces. The reason for this is to focus on reusability and maintainability. The difference is that modules define namespaces at the file level, while classes construct namespaces within the class scope.
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [Problem 2] Explain polymorphism and provide your own Python code example that demonstrates it.
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
"Flying"
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
"Cannot fly"
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
"Quack"
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
"Squeak"
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
Flying
Cannot fly
Quack
Squeak
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
[Solution] The ability for instances of different classes within an inheritance relationship to react differently to the same member function call; operator overloading is also an important technique supporting polymorphism.
<br>
[Example] This is an example using the Strategy Pattern among design patterns. For each behavior inheriting from FlyBehavior or QuackBeHavior, the objects support different reactions at runtime. In this example, the Duck object containing them is more important than the inherited quack or squack. Depending on what object the Duck object holds when initialized, it can exhibit different behaviors.
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [Problem 3] Code a Counter class that satisfies all the following requirements (You don't need to enter answers for each requirement; just provide one class definition code for Problem 3).
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
#Requirement 1
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
#Requirement 2
</span>
<span class="k">
print
</span>
<span class="s">
"Requirement 2 output"
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
#Requirement 3
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
"Requirement 3 output"
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
#Requirement 4
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
"Requirement 4 output"
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
#Requirement 5
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
"Requirement 5 output"
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
#Requirement 6
</span>
<span class="k">
print
</span>
<span class="s">
"Requirement 6 output"
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
Requirement 2 output
10 10
Requirement 3 output
11 12
Requirement 4 output
12 14
Requirement 5 output
17 9
Requirement 6 output
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
[Solution]
<br>
-Needs1 : Initialized the parameter as default to 1 in the __init__ function.
<br>
-Needs2 : Using the __str__ function produces the same effect as java's toString.
<br>
-Needs3 : Increased the value according to the requirements.
<br>
-Needs4 : Used the __call__ function to call the incr function as an instance.
<br>
-Needs5 : Developed using __sum__ and __sub__ functions. Thinking of extensibility, I included a method called operatorHelper() to apply the Template Method pattern, allowing operators to be determined dynamically. I developed it so that types other than integers can also be input.
<br>
-Needs6 : Used the __cmp__ function. Fabricated it to handle other types similarly to the above. Using the cmp function allows it to proceed without a special algorithm.
<br>
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [Problem 4] The following is the definition content of the MySet class created by subclassing the built-in list data type. Explain the code content of the three methods: __init__(), __str__(), and eliminate_duplicate() in the following class definition as if you were teaching it to someone else.
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [Problem 5] Add methods to the MySet class defined in Problem 4 to provide coding that satisfies all the following requirements (You don't need to enter answers for each requirement; just provide one MySet class definition code for Problem 5).
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [Problem 6] When the following example is executed for the MySet class defined in Problem 5, it can be confirmed that it operates correctly without errors. Explain why the use examples of len(), bool() built-in functions and the in keyword within the following example are performed correctly even though no special method definitions were made. - The explanation was written for problems 4, 5, and 6 together.
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
#Requirement 1
</span>
<span class="k">
print
</span>
<span class="s">
"Requirement 1 output"
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
,---
layout: post
title: "[Short-term] 04. Feature IMAGE Extraction"
description: "Hello? This time, we will implement the feature of extracting a feature image from a URL, which we decided to do last time. Below is the material on regular expressions by Doohyun Nam from the Daejeon Membership. He helped a lot with this feature implementation. See more Python Assignment 5 Author..."
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
Hello?
</p>
<p>
In this session, we will implement the feature of extracting a feature image from a URL, which we planned to do last time.
</p>
<p>
Below is the material regarding regular expressions provided by Doohyun Nam from the Daejeon Membership.
</p>
<p>
He provided a great deal of help in implementing this feature.
</p>

<span class="txt_fold">
See more
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
• [Question 1] Explain the similarities and differences between classes and modules.
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
The commonality between classes and modules is that they both collect and store functions or constant values that perform similar or related tasks, and they each have their own separate namespace. The reason for this focus is on reusability and maintainability. The difference is that a module defines a namespace at the file level, while a class constructs a namespace within its own class space.
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [Question 2] Explain polymorphism and provide your own Python code example that demonstrates polymorphism.
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
"Flying"
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
"Cannot fly"
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
"Quack"
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
"Squeak"
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
Flying
Cannot fly
Quack
Squeak
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
[Solution] The ability that allows instances of different classes within an inheritance relationship to respond differently to the same member function call; operator overloading is also an important technique that supports polymorphism.
<br>
[Example] This is an example using the Strategy Pattern among design patterns. For each behavior inheriting from FlyBehavior and QuackBeHavior, each object supports a different response at runtime. In the following example, the Duck object, which contains these as part of its composition, is more important than the inherited quack or squack methods. Depending on which object it holds when initialized, the Duck object can exhibit different behaviors.
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [Question 3] Code a Counter class that satisfies all of the following requirements (You don't need to enter the answer for each requirement separately; you can provide one class definition code for Question 3).
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
#Requirement 1
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
#Requirement 2
</span>
<span class="k">
print
</span>
<span class="s">
"Requirement 2 output"
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
#Requirement 3
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
"Requirement 3 output"
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
#Requirement 4
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
"Requirement 4 output"
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
#Requirement 5
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
"Requirement 5 output"
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
#Requirement 6
</span>
<span class="k">
print
</span>
<span class="s">
"Requirement 6 output"
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
Requirement 2 output
10 10
Requirement 3 output
11 12
Requirement 4 output
12 14
Requirement 5 output
17 9
Requirement 6 output
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
[Solution]
<br>
-Needs1: Initialized the parameter as 1 by default in the __init__ function.
<br>
-Needs2: Using the __str__ function produces the same effect as toString in Java.
<br>
-Needs3: Increased the value as per the requirement.
<br>
-Needs4: Used the __call__ function to invoke the incr function as an instance.
<br>
-Needs5: Developed using the __add__ and __sub__ functions. Considering scalability, I included a method called operatorHelper() to apply the Template Method Pattern, allowing the operator to be determined dynamically. The operations were developed to accept other types as well, not just integers.
<br>
-Needs6: Used the cmp function. Similar to above, it was built to handle other types as well. Using the cmp function allows processing without special algorithms.
<br>
</p>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [Question 4] The following is the definition of a MySet class created by subclassing the built-in list type. Explain the code content of the three methods __init__(), __str__(), and eliminate_duplicate() in this class definition, thinking as if you are teaching someone else.
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [Question 5] Present coding that satisfies all the requirements by adding methods to the MySet class defined in Question 4 (You don't need to enter the answer for each requirement separately; you can provide one MySet class definition code for Question 5).
</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>
• [Question 6] If you perform the following example on the MySet class defined in Question 5, you can confirm that it works correctly without errors. Explain why the len() and bool() built-in functions and the 'in' keyword usage example in the following example perform correctly even though no separate method definitions were made. - The commentary was written for questions 4, 5, and 6 together.
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
<span class="e">
e
</span>
<span class="p">
)
</span>
<span class="c">
#Requirement 1
</span>
<span class="k">
print
</span>
<span class="s">
"Requirement 1 output"
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