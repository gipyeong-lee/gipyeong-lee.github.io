---
layout: post
title: "[Bootstrap, JQuery] Beautifying Tables"
description: "Hello? This time, I would like to introduce a useful frontend plugin for GMS tool development. You can check it out by visiting the following URL: https://datatables.net/examples/styling/bootstrap.html Below is a comparison before and after..."
date: 2016-02-24 18:43:22 +0900
section: blog
category: engineering
lang: en
ref: 2016-02-24-legacy-166-engineering-bootstrap-jquery-table
tags:
  - "table"
  - "jquery"
  - "bootstrap"
  - "pagination"
  - "DataTable"
  - "Web"
translation_source_hash: 0c9b2527bb2bdde31e94804994245a3f56b49f1be2fc4f84e116c6dacc8f8a00
---

<p>
Hello!
</p>

<p>
In this post, I would like to introduce a useful frontend plugin for GMS tool development.
</p>
<p>
You can refer to the following URL to check it out:
</p>

<p>
<a href="https://datatables.net/examples/styling/bootstrap.html" target="_blank" class="tx-link">
https://datatables.net/examples/styling/bootstrap.html
</a>
<br>
</p>


<p>
Below are screenshots from before and after applying it.
</p>


<p>
<figure class="imageblock alignCenter" width="681" height="416">

<figcaption>
Before application
</figcaption>
</figure>
</p>

<p>
<b>
&lt;Before application&gt;
</b>
</p>




<p>
The photo above shows how about 2,000 test data points look when displayed without the plugin.
</p>
<p>
(If data keeps piling up in the future... it will be huge, right?)
</p>



<p>
Here is how it looks after applying the plugin.
</p>







<p>
You can organize and view data in sets of 10, 20, 50, or 100, search table rows using the Search function, and it provides pagination features.
</p>
<p>
If you have the desire to "implement it by hand" or have never implemented (pagination, entry limits, search) before, I recommend doing it yourself.
</p>

<p>
However, if you have already implemented it and it feels like repetitive grunt work, I think it is better to work comfortably using this plugin.
</p>


<p>
I will briefly summarize how to use it below.
</p>
<p>
I recommend using jQuery version 1.12 or higher. (I haven't tested lower versions. I mention this because the example site uses version 1.12. I personally used jQuery version 2.x.)
</p>

<p>
<b>
1. Download the files and apply the &lt;script src=""&gt;&lt;/script&gt; tags.
</b>
</p>

<p>
<figure class="fileblock">
<a href="./file/dataTables.bootstrap.min.js" class="">

<div class="desc">
<div class="filename">
<span class="name">
dataTables.bootstrap.min.js
</span>
</div>
<div class="size">
Download
</div>
</div>
</a>
</figure>
</p>

<p>
<figure class="fileblock">
<a href="./file/jquery.dataTables.min.js" class="">

<div class="desc">
<div class="filename">
<span class="name">
jquery.dataTables.min.js
</span>
</div>
<div class="size">
Download
</div>
</div>
</a>
</figure>
</p>


<p>
It should look like this:
</p>

<span class="txt_fold">
Show more
</span>
<div class="moreless_content">
<p>
&lt;script src="http://code.jquery.com/jquery-2.1.4.js"&gt;&lt;/script&gt;
</p>
<p>
&lt;script src="dataTables.bootstrap.min.js"&gt;&lt;/script&gt;
</p>
<p>
<span>
&lt;script src="jquery.dataTables.min.js"&gt;&lt;/script&gt;
</span>
<br>
</p>
</div>


<p>
<b>
2. Try calling the API.
</b>
</p>
<p>
Call it as follows:
</p>

<p>
<code class="js plain">
$(
</code>
<code class="js string">
'#example'
</code>
<code class="js plain">
).DataTable();
</code>
</p>



<p>
If you want to build everything from scratch, I recommend doing it at least once.
</p>
<p>
However, for those working in the industry who are short on time, I recommend using this.
</p>
<p>
(However, if you need more customization, then I recommend building it yourself.)
</p>

<p>
Experience using it — it is convenient.
</p>

<p>
<b>
Note: I have not tested browser compatibility. It works normally in Chrome 48.0 and above.
</b>
</p>