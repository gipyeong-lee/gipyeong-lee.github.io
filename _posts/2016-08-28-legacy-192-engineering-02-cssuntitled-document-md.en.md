---
layout: post
title: "[02] Style Sheet CSSUntitled Document.md"
description: "Untitled Document.md 3 minutes: Chapter 2 CSS _04 What is CSS? A style sheet is a language used to describe how a document written in HTML is actually displayed. If you imagined drawing a puppy using HTML, you could use CSS to describe how long its tail is, how small its head is, or what its build is like..."
date: 2016-08-28 01:14:05 +0900
section: blog
category: engineering
lang: en
ref: 2016-08-28-legacy-192-engineering-02-cssuntitled-document-md
tags:
  - "CSS"
  - "Style"
  - "3-Minute Web Study"
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
3 Minutes: Chapter 2 CSS
</h1>
<h3>
<a>
</a>
_04 What is CSS?
</h3>
<p>
A style sheet is a language that describes how a document written in 
<strong>
HTML
</strong>
is actually displayed. Imagine you have drawn a puppy using HTML.
</p>
<p>
The language that allows you to describe how long its tail is, how small its head is, or what its body size is—that is 
<strong>
CSS
</strong>
.
</p>
<p>
In other words, if you draw a skeleton and put clothes on it, HTML is the skeleton, and CSS is what adds properties to those clothes, such as their size or color.
</p>
<p>
Let's summarize. The roles of 
<strong>
HTML
</strong>
 and 
<strong>
CSS
</strong>
 are as follows:
</p>
<blockquote>
<p>
HTML
</p>
</blockquote>
<ul>
<li>
Puts clothes on the skeleton.
</li>
</ul>
<blockquote>
<p>
CSS
</p>
</blockquote>
<ul>
<li>
Tells us what the clothes look like.
</li>
</ul>
<p>
Now that you know what CSS does, let's learn the basics of CSS.
</p>
<blockquote>
<p>
How to use CSS
</p>
</blockquote>
<ul>
<li>
Write a 
<strong>
css
</strong>
 file and reference it in an 
<strong>
HTML
</strong>
 file.
</li>
<li>
Insert 
<strong>
css
</strong>
 directly into an 
<strong>
HTML
</strong>
 file.
</li>
<li>
Apply styles using 
<strong>
Javascript
</strong>
.
</li>
</ul>
<p>
Of course, there may be other methods. However, these are the most commonly used ways. With these methods, you can make your 
<b>
HTML
</b>
 look however you want.
</p>
<p>
Let's look at an example.
</p>
<p>
Consider the following HTML code:
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
In the 
<strong>
HTML
</strong>
 source above, what if you want the text 'Hello' to appear in red? How would you express that?
</p>
<p>
If you include the following style code, you will see a red 'Hello'.
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
Explaining CSS in detail would take more than 3 minutes. Therefore, instead of giving a long-winded explanation, I will summarize it for you.
</p>
<blockquote>
<p>
Using CSS in HTML code
</p>
</blockquote>
<ol>
<li>
Create a class and apply it to an HTML tag.
</li>
<li>
Insert the style directly into an HTML tag.
</li>
</ol>
<p>
There are two ways.
</p>
<p>
The first is the method I used above. Then, what is the method for inserting it directly? I will show you how to insert a style directly through the following example.
</p>
<pre>
<code class="language-html">
... middle section omitted ...
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
... middle section omitted ...
</code>
</pre>
<p>
By using it this way, you can apply styles directly to the tag without needing a class.
</p>
<p>
So, why use classes? If you want certain words to be red, and you write it directly every time, you have to insert the style into the tag one by one. However, by using the method I used first, you have the advantage of being able to apply a style once to tags that 'have the corresponding class or id'.
</p>
<p>
Also, if you organize styles into 'classes', you can later create tags that combine multiple classes.
</p>
<blockquote>
<p>
CSS Nesting
</p>
<ul>
<li>
Create a btn class with a font size of 20pt.
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
Create a btn-danger class with a text color of red.
</li>
<ul>
<li>
.btn-danger { color:red; }
</li>
</ul>
</ul>
</blockquote>
<p>
If you create and store multiple classes like above, and add the classes you want to use into the tag, they will be applied in a nested fashion.
If there are identical properties in the classes, the properties of the class applied later will overwrite the previous ones.
</p>
<p>
Below is an application example.
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
Big Button
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
Red Button
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
Big Red Button
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
As such, you can use styles to represent 
<strong>
HTML
</strong>
 tags however you want.
</p>
<h1>
<a>
</a>
Summary
</h1>
<h4>
<a>
</a>
- Styles define how to represent HTML.
</h4>
<h4>
<a>
</a>
- Styles are applied in a nested manner through classes. However, if properties are the same, the property of the last class is applied.
</h4>
<h4>
<a>
</a>
- Styles can also be applied directly to tags.
</h4>
<blockquote>
<p>
<strong>
3-Minute Spoilers
</strong>
</p>
</blockquote>
<ul>
<li>
Okay, we've put colored clothes on it now. How would we go about making this thing move?
</li>
</ul>