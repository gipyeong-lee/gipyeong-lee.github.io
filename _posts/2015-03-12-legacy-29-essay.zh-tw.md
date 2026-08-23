---
layout: post
title: "網頁"
description: "你好！我將會記錄在學習 Web 前端過程中遇到的經驗，以及解決問題的方法。測試環境為 ie8、chrome、safari。CSS : Bootstrap ie8 : 顯示效果不佳 > 自行編寫 css 來套用..."
date: 2015-03-12 02:54:19 +0900
section: blog
category: essay
lang: zh-tw
ref: 2015-03-12-legacy-29-essay
tags:
  - "Web"
  - "Location"
  - "網頁"
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
我將會記錄在學習 Web 前端過程中遇到的經驗，以及解決問題的方法。
</span>
<br>
</span>
</span>
</p>
<p>
<span>
<span>
<span>
測試環境為 ie8、chrome、safari。
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
CSS : Bootstrap
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
ie8 : 顯示效果不佳 > 自行編寫 css 來套用。
</span>
<br>
</p>
<p>
<span>
chrome : Good
</span>
</p>
<p>
<span>
Safari : Good
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
JS : addEventListener
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
ie8 : 無法運作。我做了如下處理，在 ie8 中透過 attachEvent 來處理。
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
chrome : Good
</span>
</p>
<p>
<span>
Safari : Good
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
在使用 JQUERY 的 merge 合併陣列時，發現資料會根據 arr1 和 arr2 的順序而有所不同，這是一個很奇怪的體驗。
</span>
</font>
</p>
<p>
<font>
<span>
必須要多加注意... ㅡ,.ㅡ... ;;
</span>
</font>
</p>
<p>
<font>
<span>
因為這個問題花了一整天的時間在處理資料映射... 哈啊....
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
關於使用 Javascript 進行頁面跳轉
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
將目前框架上一層的路徑設定為該 url
</span>

<span>
（頁面跳轉）
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
將最外層 document 的 location 路徑設定為該 url
</span>

<span>
（頁面跳轉）
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
將開啟目前框架的 document 的 location 路徑設定為該 url（頁面跳轉）
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
JQUERY 在頁面跳轉後，想要 onload 特定的 css 或 javascript 時
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
如上例所示，在該 div 內部插入客製化的腳本或樣式程式碼。
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