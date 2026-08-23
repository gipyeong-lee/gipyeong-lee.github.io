---
layout: post
title: "[03] JavaScript 未命名文件.md"
description: "未命名文件.md 3分鐘：第 3 章 Javascript _05 什麼是 Javascript？JavaScript 是一種基於物件的腳本程式語言。更詳細的內容請參考維基百科。我們在上一章了解了 CSS……"
date: 2017-01-05 21:47:43 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2017-01-05-legacy-194-engineering-03-untitled-document-md
tags:
  - "JavaScript"
  - "javascript"
  - "emca"
  - "use"
  - "每日 3 分鐘網頁學習"
  - "engineering"
translation_source_hash: bc529d6c729f934c74b32c482334a01c4f52f86f471efa9bf59bb87503828863
---

<meta>
<title>
未命名文件.md
</title>
<h1>
<a>
</a>
3分鐘：第 3 章 Javascript
</h1>
<h3>
<a>
</a>
_05
<code>
Javascript
</code>
是什麼？
</h3>
<p>
JavaScript 是一種基於物件的腳本程式語言。更詳細的內容請參考
<a href="https://ko.wikipedia.org/wiki/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8">
維基百科
</a>
。
</p>
<p>
我們在上一章了解了
<code>
CSS
</code>
。透過
<code>
CSS
</code>
，我們製作出了
<code>
具有特定屬性的事物
</code>
。現在，我們要告訴這個傢伙
<code>
該做些什麼
</code>
。
</p>
<h3>
<a>
</a>
_06 當點擊按鈕時，顯示提示視窗。
</h3>
<blockquote>
<p>
HTML
</p>
</blockquote>
<pre>
<code>
&lt;div class="button" id="id_button"&gt;Button&lt;/div&gt;
</code>
</pre>
<blockquote>
<p>
CSS
</p>
</blockquote>
<pre>
<code>
&lt;style&gt;
.button {
    background-color:green;
    color:white;
    width:auto;
    height:auto;
}
&lt;/style&gt;
</code>
</pre>
<blockquote>
<p>
Javascript
</p>
</blockquote>
<pre>
<code>
&lt;script&gt;
document.getElementById("id_button").addEventListener("click",function(){
alert("hello world");
});
&lt;/script&gt;
</code>
</pre>
<p>
將上述內容匯集到
<code>
.html
</code>
檔案中，如下所示：
</p>
<pre>
<code>
&lt;!Documen HTML&gt;
&lt;html&gt;
&lt;head&gt;
&lt;style&gt;
.button {
    background-color:green;
    color:white;
    width:auto;
    height:auto;
}
&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div class="button" id="id_button"&gt;Button&lt;/div&gt;
&lt;script&gt;
document.getElementById("id_button").addEventListener("click",function(){
    alert("hello world");
});
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code>
</pre>
<p>
上述內容是一個範例，當點擊該
<code>
div
</code>
標籤時，會顯示
<code>
'hello world'
</code>
字串。
</p>
<p>
使用 JavaScript，可以透過特定標籤的
<code>
id
</code>
、
<code>
class
</code>
等，賦予該標籤特定的動作。
<br>
不僅是點擊，還可以賦予
<code>
mouseover
</code>
、
<code>
mouseout
</code>
等滑鼠事件的動作。
</p>
<h3>
<a>
</a>
_07 更改按鈕的屬性。
</h3>
<blockquote>
<p>
HTML
</p>
</blockquote>
<pre>
<code>
&lt;div class="button" id="id_button"&gt;Button&lt;/div&gt;
</code>
</pre>
<blockquote>
<p>
CSS
</p>
</blockquote>
<pre>
<code>
&lt;style&gt;
.button {
    background-color:green;
    color:white;
    width:auto;
    height:auto;
}
&lt;/style&gt;
</code>
</pre>
<blockquote>
<p>
Javascript
</p>
</blockquote>
<pre>
<code>
&lt;script&gt;
// 將 id_button 的顏色變更為紅色。
document.getElementById("id_button").style.color="red";
&lt;/script&gt;
</code>
</pre>
<h3>
<a>
</a>
_08 停用按鈕的樣式表。
</h3>
<blockquote>
<p>
HTML
</p>
</blockquote>
<pre>
<code>
&lt;div class="button" id="id_button"&gt;Button&lt;/div&gt;
</code>
</pre>
<blockquote>
<p>
CSS
</p>
</blockquote>
<pre>
<code>
&lt;style id="btn_css"&gt;
.button {
    background-color:green;
    color:white;
    width:auto;
    height:auto;
}
&lt;/style&gt;
</code>
</pre>
<blockquote>
<p>
Javascript
</p>
</blockquote>
<pre>
<code>
&lt;script&gt;
// 停用文件中 ID 為 btn_css 的樣式。
document.getElementById("btn_css").disabled = true;
&lt;/script&gt;
</code>
</pre>
<p>
今天我們簡單地了解了 JavaScript。我所介紹的 JavaScript，您可以將其視為一種
<code>
氛圍
</code>
而非
<code>
學習
</code>
。
<br>
以下是關於 JavaScript 的簡單學習資源：
</p>
<p>
<a href="https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/JavaScript_basics">
MDN Javascript 學習資料
</a>
</p>
<p>
事實上，JavaScript 確實是一種需要
<code>
學習
</code>
才能正確使用的腳本語言。當您學習 JavaScript 時，會聽到
<code>
ECMAScript
</code>
這個詞。
<br>
將該詞理解為 JavaScript 的
<code>
標準化
</code>
腳本語言會比較容易。
</p>
<blockquote>
<p>
cf.
<br>
之後編寫 JavaScript 時，可能會在腳本開頭看到
<code>
use strict
</code>
這句話。
<br>
這表示該腳本遵循標準，而遵循標準意味著該腳本設計為在多種瀏覽器中都能以相同方式運作。
</p>
</blockquote>
<h1>
<a>
</a>
總結
</h1>
<h4>
<a>
</a>
- JavaScript 讓 HTML 變得生動。
</h4>
<h4>
<a>
</a>
- JavaScript 可以更改套用到
<code>
document
</code>
的屬性值。
</h4>
<h4>
<a>
</a>
- JavaScript 可以自主更改
<code>
document
</code>
的標籤。
</h4>
<h4>
<a>
</a>
- 今天稍微體驗到的 JavaScript 大約只佔 1%。其餘 99% 真的無窮無盡。
</h4>
<blockquote>
<p>
<strong>
3 分鐘預告
</strong>
</p>
</blockquote>
<ul>
<li>
如果從頭開始學習所有 JavaScript 再來使用似乎太困難了，有沒有更簡單的使用方法呢？
</li>
</ul>