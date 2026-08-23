---
layout: post
title: "[Bootstrap,JQuery] 美化表格"
description: "大家好？今天我想向大家介绍一款在开发 GMS 工具时非常实用的前端插件。您可以通过访问以下 URL 进行查看：https://datatables.net/examples/styling/bootstrap.html 以下是应用（前）与..."
date: 2016-02-24 18:43:22 +0900
section: blog
category: engineering
lang: zh-cn
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
大家好？
</p>

<p>
今天我想向大家介绍一款在开发 GMS 工具时非常实用的前端插件。
</p>
<p>
您可以通过访问以下 URL 进行查看：
</p>

<p>
<a href="https://datatables.net/examples/styling/bootstrap.html" target="_blank" class="tx-link">
https://datatables.net/examples/styling/bootstrap.html
</a>
<br>
</p>


<p>
以下是应用（前）与（后）的截图。
</p>


<p>
<figure class="imageblock alignCenter" width="681" height="416">

<figcaption>
应用前
</figcaption>
</figure>
</p>

<p>
<b>
&lt;应用前&gt;
</b>
</p>




<p>
上图是目前在测试中，大约 2000 条数据在没有插件的情况下显示的样子。
</p>
<p>
（未来如果数据堆积得非常多……那场面应该很壮观吧？）
</p>



<p>
以下是应用插件后的效果。
</p>







<p>
可以按 10、20、50、100 条进行整理查看，通过 Search 可以搜索表格行，并提供了分页（Pagination）功能。
</p>
<p>
如果抱着“想亲手实现看看”的想法，或者从来没有实现过（分页、条目显示、搜索），我建议还是亲自尝试一下。
</p>

<p>
如果已经实现过，觉得是在做重复劳动的话，我认为使用这个插件来处理工作会更加轻松。
</p>


<p>
使用方法简要整理如下。
</p>
<p>
建议使用 jQuery 1.12 或更高版本。（我没有测试过更低版本。因为示例网站使用的是 1.12 版本，所以在此告知。笔者使用的是 jQuery 2.x 版本。）
</p>

<p>
<b>
1. 下载文件并应用 &lt;script src=""&gt;&lt;/script&gt; 脚本。
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
下载
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
下载
</div>
</div>
</a>
</figure>
</p>


<p>
配置如下所示：
</p>

<span class="txt_fold">
查看更多
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
2. 调用 API。
</b>
</p>
<p>
按如下方式进行调用。
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
如果您想从零开始制作所有功能，建议尝试亲手实现。
</p>
<p>
但是，如果您在实际工作中没有时间，推荐使用这个插件。
</p>
<p>
（不过，如果需要进行更深度的定制，还是建议自己制作。）
</p>

<p>
使用体验——非常方便。
</p>

<p>
<b>
不过，我没有测试过浏览器的兼容性。在 Chrome 48.0 及以上版本中运行正常。
</b>
</p>