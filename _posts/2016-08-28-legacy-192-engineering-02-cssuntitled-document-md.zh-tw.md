---
layout: post
title: "[02] 樣式表 CSSUntitled Document.md"
description: "Untitled Document.md 3分鐘：第 2 章 CSS _04 什麼是 CSS？樣式表是用來描述 HTML 文件實際顯示方式的語言。假設你們用 HTML 畫了一隻小狗，這隻小狗的尾巴有多長、頭有多小、身軀有多大。能夠描述這些細節的語言就是 CSS。"
date: 2016-08-28 01:14:05 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2016-08-28-legacy-192-engineering-02-cssuntitled-document-md
tags:
  - "CSS"
  - "Style"
  - "每日 3 分鐘網頁學習"
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
3分鐘：第 2 章 CSS
</h1>
<h3>
<a>
</a>
_04 什麼是 CSS？
</h3>
<p>
樣式表（Style Sheet）是用來描述 <strong>HTML</strong> 所編寫的文件實際顯示方式的語言。假設你們用 HTML 畫了一隻小狗，那麼這隻小狗的尾巴有多長、頭有多小、身軀有多大，這種用來描述這些細節的語言就是 <strong>CSS</strong>。
</p>
<p>
換句話說，如果你畫好了骨架並幫它穿上衣服。到這裡為止如果是 <strong>HTML</strong> 的話，設定那件衣服的大小、是什麼顏色等屬性，就是 CSS 的工作。
</p>
<p>
那麼，來總結一下 <strong>HTML</strong> 和 <strong>CSS</strong> 各自扮演的角色如下：
</p>
<blockquote>
<p>
HTML
</p>
</blockquote>
<ul>
<li>
幫骨架穿上衣服。
</li>
</ul>
<blockquote>
<p>
CSS
</p>
</blockquote>
<ul>
<li>
說明衣服長什麼樣子。
</li>
</ul>
<p>
現在我們知道了 CSS 的作用，接著來學習 CSS 的基礎吧。
</p>
<blockquote>
<p>
CSS 使用方法
</p>
</blockquote>
<ul>
<li>
撰寫 <strong>css</strong> 檔案後，在 <strong>HTML</strong> 檔案中引用來使用。
</li>
<li>
直接在 <strong>HTML</strong> 檔案中寫入 <strong>css</strong> 來使用。
</li>
<li>
利用 <strong>Javascript</strong> 來套用樣式。
</li>
</ul>
<p>
當然，還有其他方法。不過，這裡介紹的是最常使用的方式。透過上述方法，你們可以讓 <strong>HTML</strong> 呈現出你們想要的樣子。
</p>
<p>
舉個例子。
</p>
<p>
請看以下的 HTML 程式碼。
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
在上述的 <strong>HTML</strong> 原始碼中，如果想讓「Hello」這個文字變成紅色，該怎麼表示呢？
</p>
<p>
只要加入以下的樣式代碼，你們就能看到紅色的「Hello」了。
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
如果針對 CSS 詳細解釋的話，恐怕會超過 3 分鐘。因此，與其長篇大論，我為各位整理如下。
</p>
<blockquote>
<p>
在 HTML 代碼中使用 CSS
</p>
</blockquote>
<ol>
<li>
建立 class 並套用到 HTML 標籤上。
</li>
<li>
直接在 HTML 標籤中加入 style。
</li>
</ol>
<p>
有這兩種方法。
</p>
<p>
第一種是我上面使用的方法。那麼，直接加入的方法是什麼呢？透過下方的範例來介紹如何直接加入 style。
</p>
<pre>
<code class="language-html">
... 中略 ...
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
... 中略 ...
</code>
</pre>
<p>
像這樣使用，你們可以在不使用 class 的情況下，直接對該標籤套用樣式。
</p>
<p>
那麼，為什麼要使用 class 呢？如果你們想要讓某些詞彙變紅，如果採用直接撰寫的方式，每次都必須逐一在標籤內加入樣式。但若使用我一開始介紹的方法，就有一次將樣式套用到「擁有該 class 或 id」的所有標籤上的優點。
</p>
<p>
此外，若將樣式整理成「class」，日後還可以製作結合多個 class 的標籤。
</p>
<blockquote>
<p>
CSS 疊加（巢狀/多重套用）
</p>
<ul>
<li>
建立 btn class，字體大小為 20pt。
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
建立 btn-danger class，文字顏色為 red。
</li>
<ul>
<li>
.btn-danger { color:red; }
</li>
</ul>
</ul>
</blockquote>
<p>
若像上面這樣建立多個 class，並將想使用的 class 加入標籤中，樣式就會疊加套用。
若 class 中有相同的屬性，後套用的 class 屬性會覆蓋掉前面的。
</p>
<p>
下方是套用範例：
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
大按鈕
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
紅色按鈕
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
又大又紅的按鈕
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
像這樣，利用樣式，你們可以隨心所欲地呈現 <strong>HTML</strong> 的標籤。
</p>
<h1>
<a>
</a>
總結
</h1>
<h4>
<a>
</a>
- 樣式定義了呈現 HTML 的方式。
</h4>
<h4>
<a>
</a>
- 樣式可透過 class 疊加套用。但若有相同屬性，則套用最後一個 class 的屬性。
</h4>
<h4>
<a>
</a>
- 樣式也可以直接套用到標籤上。
</h4>
<blockquote>
<p>
<strong>
3分鐘預告
</strong>
</p>
</blockquote>
<ul>
<li>
好，現在已經幫它穿上顏色的衣服了。那麼，要讓這個傢伙動起來該怎麼做呢？
</li>
</ul>