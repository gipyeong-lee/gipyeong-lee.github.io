---
layout: post
title: "Web"
description: "你好！我将在这里记录未来学习 Web 前端过程中遇到的经历，以及解决这些问题的方案。测试环境为 IE8、Chrome、Safari。CSS：Bootstrap IE8：应用效果不够美观 > 我直接编写并应用了 CSS..."
date: 2015-03-12 02:54:19 +0900
section: blog
category: essay
lang: zh-cn
ref: 2015-03-12-legacy-29-essay
tags:
  - "Web"
  - "Location"
  - "网页"
  - "merge"
  - "jquery"
  - "addEventListener"
translation_source_hash: 1460fd73be3c032ed2a9c6c551d1c8e09ea6f19e4807d39aa6b15a0698d1784e
---

<p>
<span>
<span>
<span>
你好！
</span>
</span>
</span>
</p>
<p>
<span>
<span>
<span>
我将在这里记录未来学习 Web 前端过程中遇到的经历，以及解决这些问题的方案。
</span>
<br>
</span>
</span>
</p>
<p>
<span>
<span>
<span>
测试环境为 IE8、Chrome、Safari。
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
CSS：Bootstrap
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
IE8：应用效果不够美观 &gt; 我直接编写并应用了 CSS。
</span>
<br>
</p>
<p>
<span>
Chrome：良好
</span>
</p>
<p>
<span>
Safari：良好
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
JS：addEventListener
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
IE8：无法正常工作。按如下方式进行了处理。在 IE8 中通过 attachEvent 进行处理。
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
Chrome：良好
</span>
</p>
<p>
<span>
Safari：良好
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
JQUERY：$.merge(arr1,arr2)
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
在使用 JQUERY 的 merge 合并数组时，我发现数据会根据 arr1 和 arr2 的顺序而产生变化，这是一种奇怪的经历。
</span>
</font>
</p>
<p>
<font>
<span>
必须多加注意…… 唉…… ;;
</span>
</font>
</p>
<p>
<font>
<span>
因为这个浪费了一整天的时间来处理数据映射…… 哈啊……
</span>
</font>
</p>
<p>
<font>
<span>
救救我。
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
关于通过 Javascript 进行页面跳转
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
将当前框架的上一级路径设置为指定的 URL
</span>

<span>
（页面已跳转）
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
将最外层 document 的 location 路径设置为指定的 URL
</span>

<span>
（页面已跳转）
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
将打开当前框架的 document 的 location 路径设置为指定的 URL（页面已跳转）
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
当希望在 JQUERY 页面跳转后 onload 触发特定的 CSS 或 Javascript 时
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
如上例所示，将自定义的脚本或样式代码插入到该 div 内部即可。
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