---
layout: post
title: "HTML5 新特性"
description: "你好！这是一个整理我在学习 HTML5 过程中所学知识的空间。提前说明，这里不会对特定功能进行深入探讨。DTD (Document Type Definition) 是 Document Type Definition 的缩写。DTD 是一种文本文件..."
date: 2015-02-02 04:23:29 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2015-02-02-legacy-9-engineering-html5
tags:
  - "Web"
  - "engineering"
translation_source_hash: a389f43501977c62c13d3c611499e7cf5a217c9507339e4ae160383c6ef687cb
---

<p>
<span>
你好！
</span>
</p>
<p>
<span>
这是一个整理我在学习 HTML5 过程中所学知识的空间。提前说明，这里不会对特定功能进行深入探讨。
</span>
</p>

<p>
<b>
<span>
DTD (Document Type Definition)
</span>
</b>
</p>
<p>
<span>
这是 Document Type Definition 的缩写。DTD 是一种文本文件，用于描述哪些标签、属性和值在特定的 HTML 文档中是有效的。据说每个 HTML 版本都有对应的 DTD。通常我们会在 HTML 文档的第一行通过 doctype 声明来定义它，以此告知浏览器使用了哪个版本的 HTML 或 XHTML。
</span>
<span>
如果漏掉这种 doctype 声明，大多数浏览器会进入一种被称为“怪异模式 (Quirks Mode)”的状态。
</span>
</p>
<p>
<span>
当浏览器遇到没有 doctype 声明的页面时，它会认为：“噢，这个页面是非常久远以前写的。”并得出“那就随便显示吧”的结论。
</span>
</p>
<p>
<span>
如果自己制作的网页在浏览器中显示效果与预期不符，检查一下 doctype 声明是很有必要的。
</span>
</p>
<p>
<span>
以下是各版本的 doctype 声明：
</span>
</p>


<div>

<p>
<b>
<span>
HTML5
</span>
</b>
</p>
<p>
<span>
&lt;!doctype html&gt;
</span>
</p>

<p>
<b>
<span>
HTML4
</span>
</b>
</p>
<p>
<span>
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"&gt;
</span>
</p>

<p>
<b>
<span>
XHTML 1.0
</span>
</b>
</p>
<p>
<span>
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 1.010 Transitional//EN" "http://www.w3.org/TR/html1/DTD
</span>
<span>
/xhtml1-transitional.dtd"&gt;
</span>
</p>
<p>
<span>
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
</span>
</p>

</div>

<br>


<div>
<br>
</div>
<p>
<b>
<span>
应对 IE9 及以下版本的指南
</span>
</b>
</p>

<p>
<span>
1. 如果想让 IE8 理解 HTML5：
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
在 &lt;/head&gt; 标签前插入以下代码即可。
</p>

<div>
<p>
&lt;!--[if lt IE 9]&gt;
</p>
<p>
&lt;script src="//html5shiv.googlecode.com/svn/trunk/html5.js"&gt;&lt;/script&gt;
</p>
<p>
&lt;![endif]--&gt;
</p>
</div>

<p>
通过使用条件注释，只有比 IE9 更老的 IE 版本（即 IE 6、7、8）能够理解并应用这段代码。神奇的是经过测试，在 Chrome 中该脚本不会被加载，看来它能够专门识别 IE。
</p>

<p>
<span>
2. 如何避开 IE8 的“兼容性视图”及“兼容性视图列表”：
</span>
</p>
<p>
请将以下代码放入 &lt;head&gt; 中：
</p>

<div>
<p>
&lt;head&gt;
</p>
<p>
&lt;meta http-equiv="X-UA-Compatible" content="IE=edge" /&gt;
</p>
<p>
...
</p>
<p>
&lt;/head&gt;
</p>
</div>


<p>
<b>
<span>
在 HTML 代码中连接外部样式表
</span>
</b>
</p>

<p>
将外部样式表连接到网页的方法是使用 &lt;link&gt; 标签。
</p>
<p>
以下是各版本的使用方式：
</p>


<div>
<p>
<b>
<span>
HTML5
</span>
</b>
</p>
<p>
<span>
&lt;link rel="stylesheet" href="css/styles.css"&gt;
</span>
</p>

<p>
<b>
<span>
HTML4
</span>
</b>
</p>
<p>
<span>
&lt;link rel="stylesheet" type="text/css" href = "css/styles.css" &gt;
</span>
</p>

<p>
<b>
<span>
XHTML 1.0
</span>
</b>
</p>
<p>
<font>
&lt;link rel="stylesheet" type="text/css" href="css/styles.css" /&gt;
</font>
</p>
</div>