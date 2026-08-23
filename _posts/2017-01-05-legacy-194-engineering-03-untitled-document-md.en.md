---
layout: post
title: "[03] JavaScript Untitled Document.md"
description: "Untitled Document.md 3 Minutes: Chapter 3 JavaScript _05 What is JavaScript? JavaScript is an object-based script programming language. For more details, please refer to Wikipedia. In the previous chapter, we learned about CSS...."
date: 2017-01-05 21:47:43 +0900
section: blog
category: engineering
lang: en
ref: 2017-01-05-legacy-194-engineering-03-untitled-document-md
tags:
  - "javascript"
  - "javascript"
  - "ecma"
  - "use"
  - "3-minute web study"
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
3 Minutes: Chapter 3 JavaScript
</h1>
<h3>
<a>
</a>
_05
<code>
Javascript
</code>
What is it?
</h3>
<p>
JavaScript is an object-based script programming language. For more detailed information, please refer to 
<a href="https://ko.wikipedia.org/wiki/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8">
Wikipedia
</a>
.
</p>
<p>
In the previous chapter, we learned about 
<code>
CSS
</code>
.
Through 
<code>
CSS
</code>
, we created 
<code>
something with certain properties
</code>
. Now, we are going to tell it 
<code>
what it should do
</code>
.
</p>
<h3>
<a>
</a>
_06 Let's trigger an alert box when a button is clicked.
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
If we put the above together in a 
<code>
.html
</code>
file, it looks like this.
</p>
<pre>
<code>
&lt;!DOCTYPE HTML&gt;
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
The example above shows a string saying 
<code>
'hello world'
</code>
when the corresponding 
<code>
div
</code>
tag is clicked.
</p>
<p>
Using JavaScript, you can assign specific actions to a tag through its 
<code>
id
</code>
, 
<code>
class
</code>
, etc.
<br>
Not just clicks, but you can also assign actions for mouse events such as 
<code>
mouseover
</code>
and 
<code>
mouseout
</code>
.
</p>
<h3>
<a>
</a>
_07 Let's change the button's properties.
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
// Changes the color of id_button to red.
document.getElementById("id_button").style.color="red";
&lt;/script&gt;
</code>
</pre>
<h3>
<a>
</a>
_08 Let's disable the button's stylesheet.
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
// Let's disable the style with the id 'btn_css' applied to the document.
document.getElementById("btn_css").disabled = true;
&lt;/script&gt;
</code>
</pre>
<p>
Today, we briefly looked at JavaScript. Think of the JavaScript I taught you as a 
<code>
vibe
</code>
rather than a 
<code>
learning session
</code>
.
<br>
Below are some simple learning materials for JavaScript.
</p>
<p>
<a href="https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/JavaScript_basics">
MDN JavaScript Learning Materials
</a>
</p>
<p>
In reality, JavaScript is a scripting language that you must 
<code>
study
</code>
to use properly. As you study JavaScript, you will hear the term 
<code>
ECMAScript
</code>
.
<br>
It is easy to think of this term as the 
<code>
standardized
</code>
scripting language for JavaScript.
</p>
<blockquote>
<p>
cf.
<br>
When writing JavaScript in the future, you may see the phrase 
<code>
use strict
</code>
at the top of the script.
<br>
This script indicates that it follows standards, which can be interpreted to mean it is designed to operate identically across various browsers.
</p>
</blockquote>
<h1>
<a>
</a>
Summary
</h1>
<h4>
<a>
</a>
- JavaScript makes HTML move.
</h4>
<h4>
<a>
</a>
- JavaScript can change property values applied to the 
<code>
document
</code>
.
</h4>
<h4>
<a>
</a>
- JavaScript can autonomously change tags in the 
<code>
document
</code>
.
</h4>
<h4>
</h4>
<h4>
<a>
</a>
- What we tasted today is about 1% of JavaScript. The other 99% is truly boundless.
</h4>
<blockquote>
<p>
<strong>
3-Minute Spoiler
</strong>
</p>
</blockquote>
<ul>
<li>
It seems too hard to learn and use JavaScript from scratch, is there a way to use it more easily?
</li>
</ul>