---
layout: post
title: "New Features in HTML5"
description: "Hello? This is a space where I organize what I've learned while studying HTML5. Please note in advance that this is not a place for in-depth postings on specific features. DTD (Document Type Definition) is an abbreviation for Document Type Definition. A DTD is a text file that describes which tags, attributes, and values are valid in a specific HTML document..."
date: 2015-02-02 04:23:29 +0900
section: blog
category: engineering
lang: en
ref: 2015-02-02-legacy-9-engineering-html5
tags:
  - "Web"
  - "engineering"
translation_source_hash: a389f43501977c62c13d3c611499e7cf5a217c9507339e4ae160383c6ef687cb
---

<p>
<span>
Hello?
</span>
</p>
<p>
<span>
This is a space where I organize what I've learned while studying HTML5. Please note in advance that this is not a place for in-depth postings on specific features.
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
This is an abbreviation for Document Type Definition. A DTD is a text file that describes which tags, attributes, and values are valid in a specific HTML document. Each HTML version is said to have its own corresponding DTD. Usually, this is done via a doctype declaration on the first line of an HTML document, which informs the browser which version of HTML or XHTML is being used.
</span>
<span>
If this doctype declaration is omitted, most browsers reportedly fall into a state called "Quirks Mode."
</span>
</p>
<p>
<span>
When encountering a page without a doctype declaration, the browser thinks, "Oh, this is a page written a very long time ago," and reaches the conclusion, "Then I should just display it however I want."
</span>
</p>
<p>
<span>
If your webpage doesn't look the way you intended in the browser, it is recommended to check the doctype declaration.
</span>
</p>
<p>
<span>
Below are the doctype declarations for each version.
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
Our attitude toward dealing with IE9 and older versions
</span>
</b>
</p>

<p>
<span>
1. If you want to make IE8 understand HTML5:
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
Insert the following code before the &lt;/head&gt; tag.
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
By using conditional comments, only IE older than version 9—that is, IE 6, 7, and 8—will understand and apply this code. Interestingly, when I tested it, the script was not included in Chrome. It seems it identifies IE specifically.
</p>

<p>
<span>
2. How to avoid IE 8 Compatibility View and Compatibility View list:
</span>
</p>
<p>
Please put the following code inside your &lt;head&gt;.
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
Linking external style sheets to HTML code
</span>
</b>
</p>

<p>
The way to link an external style sheet to a web page is to use the &lt;link&gt; tag.
</p>
<p>
The following is the usage method for each version.
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