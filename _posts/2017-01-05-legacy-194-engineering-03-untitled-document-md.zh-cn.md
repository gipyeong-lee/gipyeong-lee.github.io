---
layout: post
title: "[03] JavaScript Untitled Document.md"
description: "Untitled Document.md 3分钟：第 3 章 Javascript _05 什么是 Javascript？JavaScript 是一种基于对象的脚本编程语言。更多详细内容请参考维基百科。我们在上一章中了解了 CSS……"
date: 2017-01-05 21:47:43 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2017-01-05-legacy-194-engineering-03-untitled-document-md
tags:
  - "JavaScript"
  - "javascript"
  - "emca"
  - "use"
  - "每日 3 分钟 Web 学习"
  - "engineering"
translation_source_hash: bc529d6c729f934c74b32c482334a01c4f52f86f471efa9bf59bb87503828863
---

<meta>
<title>
Untitled Document.md
</title>
<h1>
<a>
</a>
3分钟：第 3 章 Javascript
</h1>
<h3>
<a>
</a>
_05
<code>
Javascript
</code>
是什么？
</h3>
<p>
JavaScript 是一种基于对象的脚本编程语言。更多详细内容请参考
<a href="https://ko.wikipedia.org/wiki/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%ED%86%A0%ED%94%84%ED%8A%B8">
维基百科
</a>
。
</p>
<p>
我们在上一章中了解了
<code>
CSS
</code>
。通过
<code>
CSS
</code>
，我们创建了
<code>
具有某种属性的某样东西
</code>
。现在，我们将告诉这个家伙
<code>
应该做些什么
</code>
。
</p>
<h3>
<a>
</a>
_06 点击按钮时，弹出提示框。
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
将以上内容集合在一个
<code>
.html
</code>
文件中，如下所示。
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
上述内容是一个示例，点击该
<code>
div
</code>
标签时，会显示
<code>
'hello world'
</code>
字符串。
</p>
<p>
使用 JavaScript，可以通过特定标签的
<code>
id
</code>
、
<code>
class
</code>
等为该标签赋予特定的动作。
<br>
不仅是点击，还可以赋予
<code>
mouseover
</code>
、
<code>
mouseout
</code>
等鼠标事件的动作。
</p>
<h3>
<a>
</a>
_07 修改按钮的属性。
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
// 将 id_button 的颜色改为红色。
document.getElementById("id_button").style.color="red";
&lt;/script&gt;
</code>
</pre>
<h3>
<a>
</a>
_08 停用按钮的样式表。
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
// 停用文档中 ID 为 btn_css 的样式。
document.getElementById("btn_css").disabled = true;
&lt;/script&gt;
</code>
</pre>
<p>
今天我们简单地了解了 JavaScript。请认为我所介绍的 JavaScript 并不是
<code>
学习
</code>
，而是一种
<code>
氛围
</code>
。
<br>
以下是关于 JavaScript 的简单学习资料。
</p>
<p>
<a href="https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/JavaScript_basics">
MDN JavaScript 学习资料
</a>
</p>
<p>
实际上，JavaScript 是一种只有通过
<code>
学习
</code>
才能正确使用的脚本语言。当您学习 JavaScript 时，会听到
<code>
ECMAScript
</code>
这个词。
<br>
可以将该词简单理解为 JavaScript 的
<code>
标准化
</code>
脚本语言。
</p>
<blockquote>
<p>
cf.
<br>
以后在编写 JavaScript 时，有时会看到脚本开头有
<code>
use strict
</code>
字样。
<br>
这表示该脚本遵循标准，遵循标准意味着它是为在多个浏览器中相同地运行而设计的脚本。
</p>
</blockquote>
<h1>
<a>
</a>
总结
</h1>
<h4>
<a>
</a>
- JavaScript 让 HTML 动起来。
</h4>
<h4>
<a>
</a>
- JavaScript 可以更改应用在
<code>
document
</code>
上的属性值。
</h4>
<h4>
<a>
</a>
- JavaScript 可以自主更改
<code>
document
</code>
的标签。
</h4>
<h4>
<a>
</a>
- 今天稍微体验到的 JavaScript 仅占 1%。剩下的 99% 非常广阔。
</h4>
<blockquote>
<p>
<strong>
3 分钟剧透
</strong>
</p>
</blockquote>
<ul>
<li>
如果想从头到尾学完 JavaScript 再使用的话，感觉太辛苦了，有没有更简单的使用方法呢？
</li>
</ul>