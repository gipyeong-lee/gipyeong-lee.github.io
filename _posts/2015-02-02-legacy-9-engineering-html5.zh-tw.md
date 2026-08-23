---
layout: post
title: "HTML5 新功能簡介"
description: "大家好，這裡是我學習 HTML5 時整理筆記的地方。先說明一下，這裡並不會對特定功能進行深入的技術探討。DTD (Document Type Definition) 是文件類型定義的縮寫。DTD 是一個文本文件，用來定義..."
date: 2015-02-02 04:23:29 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2015-02-02-legacy-9-engineering-html5
tags:
  - "Web"
  - "engineering"
translation_source_hash: a389f43501977c62c13d3c611499e7cf5a217c9507339e4ae160383c6ef687cb
---

<p>
<span>
大家好。
</span>
</p>
<p>
<span>
這裡是整理我學習 HTML5 時所學內容的空間。先說明一下，這裡並不會對特定功能進行深入的技術探討。
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
這是「文件類型定義」（Document Type Definition）的縮寫。DTD 是一個文本文件，用來描述哪些標籤、屬性和值在特定的 HTML 文件中是有效的。據說每個 HTML 版本都有相對應的 DTD。通常我們會在 HTML 文件的第一行透過 doctype 宣告來定義，這會告知瀏覽器該文件使用了哪個版本的 HTML 或 XHTML。
</span>
<span>
據說如果遺漏了這個 doctype 宣告，大多數瀏覽器會進入所謂的「怪異模式」（Quirks Mode）狀態。
</span>
</p>
<p>
<span>
當瀏覽器遇到沒有 doctype 宣告的頁面時，會認為：「喔，這是一個很久以前編寫的頁面。」接著就會得出「那我就隨便渲染吧」的結論。
</span>
</p>
<p>
<span>
如果發現自己製作的網頁在瀏覽器中顯示不如預期，建議檢查一下 doctype 宣告。
</span>
</p>
<p>
<span>
以下是各版本的 doctype 宣告方式：
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
應對 IE9 以下版本的策略
</span>
</b>
</p>

<p>
<span>
1. 若想讓 IE8 理解 HTML5：
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
在 &lt;/head&gt; 標籤前插入以下程式碼即可。
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
利用條件式註解，只有比 IE9 更舊的 IE 版本（即 IE 6, 7, 8）能理解並套用這段程式碼。神奇的是測試後發現，Chrome 並不會載入該腳本，看來它能辨識出這僅針對 IE。
</p>

<p>
<span>
2. 避免 IE8 的相容性檢視及相容性檢視清單的方法：
</span>
</p>
<p>
請將下方的程式碼加入 &lt;head&gt; 標籤內：
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
在 HTML 程式碼中連結外部樣式表
</span>
</b>
</p>

<p>
將外部樣式表連結到網頁的方法是使用 &lt;link&gt; 標籤。
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