---
layout: post
title: "[02] 样式表 CSSUntitled Document.md"
description: "Untitled Document.md 3分钟：第 2 章 CSS _04 什么是 CSS？样式表是一种用于描述 HTML 编写的文档实际显示方式的语言。如果说你利用 HTML 画了一只小狗，那么..."
date: 2016-08-28 01:14:05 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2016-08-28-legacy-192-engineering-02-cssuntitled-document-md
tags:
  - "CSS"
  - "样式"
  - "每日3分钟Web学习"
  - "engineering"
translation_source_hash: 76b7f799565e3fab200960a4baa92ed89a264609a4fca67393948f9e9a22a847
---

<meta>
<title>
Untitled Document.md
</title>
<h1>
<a>
</a>
3分钟：第 2 章 CSS
</h1>
<h3>
<a>
</a>
_04 什么是 CSS？
</h3>
<p>
样式表是一种用于描述 
<strong>
HTML
</strong>
编写的文档实际显示方式的语言。如果说你利用 HTML 画了一只小狗，请想象一下。
</p>
<p>
那只小狗的尾巴有多长、头有多小、体型有多大。能够描述这些属性的语言就是 
<strong>
CSS
</strong>
。
</p>
<p>
换句话说，如果你画好了骨架并给它穿上了衣服。如果说这部分是 
<strong>
HTML
</strong>
的话，那么指定衣服的大小、颜色等属性的过程就是 CSS。
</p>
<p>
好，我来总结一下。
<strong>
HTML
</strong>
和 
<strong>
CSS
</strong>
所扮演的角色如下所示。
</p>
<blockquote>
<p>
HTML
</p>
</blockquote>
<ul>
<li>
给骨架穿上衣服。
</li>
</ul>
<blockquote>
<p>
CSS
</p>
</blockquote>
<ul>
<li>
描述衣服的样子。
</li>
</ul>
<p>
那么，现在我们知道了 CSS 是做什么的了。让我们来学习一下 CSS 的基础知识。
</p>
<blockquote>
<p>
CSS 使用方法
</p>
</blockquote>
<ul>
<li>
编写 
<strong>
css
</strong>
文件后，在 
<strong>
HTML
</strong>
文件中引用使用。
</li>
<li>
直接在 
<strong>
HTML
</strong>
文件内部嵌入 
<strong>
css
</strong>
使用。
</li>
<li>
利用 
<strong>
Javascript
</strong>
应用样式。
</li>
</ul>
<p>
当然，可能还有其他方法。但我为您介绍了最常用的几种。通过上述方法，您可以按照自己想要的方式来显示 
<b>
HTML
</b>
。
</p>
<p>
比如，我们来举个例子。
</p>
<p>
以下是 HTML 代码。
</p>
<pre>
<code class="language-html">
<span class="hljs-tag">
&lt;
<span class="hljs-title">
html
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
head
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
head
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
body
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
p
</span>
&gt;
</span>
Hello
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
p
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
body
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
html
</span>
&gt;
</span>
</code>
</pre>
<p>
在上面的 
<strong>
HTML
</strong>
源码中，如果想让“Hello”这个文字显示为红色。那么该如何表现呢？
</p>
<p>
如果加入如下的样式代码，你就能看到红色的“Hello”了。
</p>
<pre>
<code class="language-html">
<span class="hljs-tag">
&lt;
<span class="hljs-title">
html
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
head
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
style
</span>
&gt;
</span>
<span class="css">
<span class="hljs-class">
.red_hello
</span>
<span class="hljs-rules">
{
<span class="hljs-rule">
<span class="hljs-attribute">
color
</span>
:
<span class="hljs-value">
red
</span>
</span>
;
}
</span>
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
style
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
head
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
body
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
p
</span>
<span class="hljs-attribute">
class
</span>
=
<span class="hljs-value">
"red_hello"
</span>
&gt;
</span>
Hello
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
p
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
body
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
html
</span>
&gt;
</span>
</code>
</pre>
<p>
如果详细说明 CSS，恐怕会超过3分钟。因此，为了方便大家，我直接进行总结。
</p>
<blockquote>
<p>
在 HTML 代码中使用 CSS
</p>
</blockquote>
<ol>
<li>
创建 class 并应用到 HTML 标签上。
</li>
<li>
直接在 HTML 标签中写入 style。
</li>
</ol>
<p>
有两种方法。
</p>
<p>
第一种是我在上面使用的方法。那么直接写入的方法是什么呢？接下来我通过一个示例向大家展示如何直接写入 style。
</p>
<pre>
<code class="language-html">
... 省略 ...
<span class="hljs-tag">
&lt;
<span class="hljs-title">
p
</span>
<span class="hljs-attribute">
style
</span>
=
<span class="hljs-value">
"color:red;"
</span>
&gt;
</span>
Hello
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
p
</span>
&gt;
</span>
... 省略 ...
</code>
</pre>
<p>
像这样使用的话，无需类名即可直接对该标签应用样式。
</p>
<p>
那么，为什么要使用 class（类）呢？如果你想让某些单词变红，如果直接书写，每次都要手动在标签内加入样式。但是，使用我最初使用的方法，您只需应用一次样式，就可以让所有“拥有相应类名或 id”的标签生效，这是它的优点。
</p>
<p>
此外，如果将样式整理为 ‘class’，以后还可以创建组合多个类的标签。
</p>
<blockquote>
<p>
CSS 叠加
</p>
<ul>
<li>
创建 btn 类，字体大小为 20pt。
</li>
<ul>
<li>
.btn { font-size:20pt; }
</li>
</ul>
</ul>
</blockquote>
<blockquote>
<ul>
<li>
创建 btn-danger 类，字体颜色为 red。
</li>
<ul>
<li>
.btn-danger { color:red; }
</li>
</ul>
</ul>
</blockquote>
<p>
如果像上面这样创建多个类，并将想要使用的类放入标签中，样式就会叠加应用。
如果类中存在相同的属性，后应用的类属性会覆盖前面的。
</p>
<p>
以下是应用示例。
</p>
<pre>
<code class="language-html">
<span class="hljs-tag">
&lt;
<span class="hljs-title">
div
</span>
<span class="hljs-attribute">
class
</span>
=
<span class="hljs-value">
"btn"
</span>
&gt;
</span>
大按钮
<span class="hljs-tag">
&lt;
<span class="hljs-title">
div
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
div
</span>
<span class="hljs-attribute">
class
</span>
=
<span class="hljs-value">
"btn-danger"
</span>
&gt;
</span>
红按钮
<span class="hljs-tag">
&lt;
<span class="hljs-title">
div
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
div
</span>
<span class="hljs-attribute">
class
</span>
=
<span class="hljs-value">
"btn btn-danger"
</span>
&gt;
</span>
又大又红的按钮
<span class="hljs-tag">
&lt;
<span class="hljs-title">
div
</span>
&gt;
</span>
</code>
</pre>
<p>
像这样利用样式，您可以随心所欲地表现 
<strong>
HTML
</strong>
标签。
</p>
<h1>
<a>
</a>
总结
</h1>
<h4>
<a>
</a>
- 样式定义了表现 HTML 的方法。
</h4>
<h4>
<a>
</a>
- 样式通过 class 进行叠加应用。但若属性相同，则应用最后定义的类属性。
</h4>
<h4>
<a>
</a>
- 样式也可以直接应用到标签上。
</h4>
<blockquote>
<p>
<strong>
3分钟预告
</strong>
</p>
</blockquote>
<ul>
<li>
好，现在连彩色的衣服都穿上了。那么，如果想让这小家伙动起来，该怎么做才好呢？
</li>
</ul>