---
layout: post
title: "Web"
description: "Hello? I will be documenting my experiences as I study web front-end development, along with the solutions I've found. The test environment is IE8, Chrome, and Safari. CSS: Bootstrap. IE8: Doesn't apply very nicely > I created and applied my own CSS..."
date: 2015-03-12 02:54:19 +0900
section: blog
category: essay
lang: en
ref: 2015-03-12-legacy-29-essay
tags:
  - "Web"
  - "Location"
  - "Web"
  - "merge"
  - "jquery"
  - "addEventListener"
translation_source_hash: 1460fd73be3c032ed2a9c6c551d1c8e09ea6f19e4807d39aa6b15a0698d1784e
---

<p>
<span>
<span>
<span>
Hello?
</span>
</span>
</span>
</p>
<p>
<span>
<span>
<span>
I will be documenting my experiences as I study web front-end development, along with the solutions I've found.
</span>
<br>
</span>
</span>
</p>
<p>
<span>
<span>
<span>
The test environment is IE8, Chrome, and Safari.
</span>
</span>
</span>
</p>
<p>
<span>
<b>
<span>
<br>
</span>
</b>
</span>
</p>
<p>
<span>
<b>
<span>
CSS: Bootstrap
</span>
</b>
</span>
</p>
<p>
<span>
<b>
<br>
</b>
</span>
</p>
<p>
<span>
IE8: Doesn't apply very nicely > I created and applied my own CSS.
</span>
<br>
</p>
<p>
<span>
Chrome: Good
</span>
</p>
<p>
<span>
Safari: Good
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
<b>
<span>
JS: addEventListener
</span>
</b>
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
IE8: Does not work. I handled it as follows. In IE8, use attachEvent.
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<div>
<p>
if(document.getElementById("btn_login").addEventListener)
</p>
<p>
document.getElementById("btn_login").addEventListener("click",function(){
</p>
<p>

window.location.href = "main.html";
</p>

<p>
});
</p>
<p>
<span>
else
</span>
</p>
<p>
document.getElementById("btn_login").attachEvent("onclick",function(){
</p>
<p>

window.location.href = "main.html";
</p>

<p>
});
</p>
</div>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
Chrome: Good
</span>
</p>
<p>
<span>
Safari: Good
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<font>
<span>
<b>
JQUERY : $.merge(arr1,arr2)
</b>
</span>
</font>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<font>
<span>
When merging arrays using JQUERY's merge, I had a strange experience where the data changed depending on the order of arr1 and arr2.
</span>
</font>
</p>
<p>
<font>
<span>
I'll have to be careful... ㅡ,.ㅡ... ;;
</span>
</font>
</p>
<p>
<font>
<span>
This took me an entire day to map the data... sigh....
</span>
</font>
</p>
<p>
<font>
<span>
Please save me.
</span>
</font>
</p>
<div>
<span>
<br>
</span>
</div>

<p>
<b>
<span>
Regarding page navigation via Javascript
</span>
</b>
</p>

<p>
<span>
<b>
parent.location.href = "url"
</b>
</span>
</p>
<p>
<span>
Sets the path of the frame immediately above the current frame to the specified URL
</span>

<span>
( Page navigated )
</span>
</p>

<p>
<span>
<b>
top.location.href = "url"
</b>
</span>
</p>
<p>
<span>
Sets the location path of the outermost document to the specified URL
</span>

<span>
( Page navigated )
</span>
</p>

<p>
<span>
<b>
opener.location.href = "url"
</b>
</span>
</p>
<p>
<span>
Sets the location path of the document that opened the current frame to the specified URL ( Page navigated )
</span>
</p>
<p>
<span>
<br>
</span>
</p>


<p>
<span>
<b>
<span>
When you want to onload specific CSS or Javascript after JQUERY page navigation
</span>
</b>
</span>
</p>


<p>
<pre class="brush: html; toolbar: false; gutter:false;">
&lt;div data-role = "page"&gt;
    &lt;style&gt; ... &lt;/style&gt; or &lt;script&gt; ... &lt;/script&gt;
&lt;/div&gt;
</pre>
</p>


<p>
<span>
As in the example above, insert custom script or style code inside the relevant div.
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
<br>
</span>
</p>