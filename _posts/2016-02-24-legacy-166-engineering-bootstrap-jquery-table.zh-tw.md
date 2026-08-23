---
layout: post
title: "[Bootstrap,JQuery] 美化表格"
description: "大家好？這次要為大家介紹在 GMS 工具開發中，前端好用的外掛程式。請參考以下網址確認：https://datatables.net/examples/styling/bootstrap.html 以下是應用（前）與..."
date: 2016-02-24 18:43:22 +0900
section: blog
category: engineering
lang: zh-tw
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
這次要為大家介紹在 GMS 工具開發中，前端好用的外掛程式。
</p>
<p>
請參考以下網址確認：
</p>

<p>
<a href="https://datatables.net/examples/styling/bootstrap.html" target="_blank" class="tx-link">
https://datatables.net/examples/styling/bootstrap.html
</a>
<br>
</p>


<p>
以下是應用（前）與（後）的截圖。
</p>


<p>
<figure class="imageblock alignCenter" width="681" height="416">

<figcaption>
應用前
</figcaption>
</figure>
</p>

<p>
<b>
&lt;應用前&gt;
</b>
</p>




<p>
上圖是目前在測試中，約 2 千筆資料在沒有使用外掛程式時的模樣。
</p>
<p>
（未來如果資料累積得非常多……那場面一定很壯觀吧？）
</p>



<p>
接著是應用外掛程式後的模樣。
</p>







<p>
可以設定以 10、20、50、100 筆為單位進行整理查看，並透過 Search 功能搜尋表格列 (Row)，同時也提供了分頁 (Pagination) 功能。
</p>
<p>
如果您「想要親手實作看看」，或者從未嘗試過實作（分頁、條目、搜尋），我推薦您親自嘗試一次。
</p>

<p>
如果您已經實作過，且覺得這類作業枯燥繁瑣的話，我認為使用該外掛程式來輕鬆處理會是不錯的選擇。
</p>


<p>
使用方法簡述如下。
</p>
<p>
建議使用 jQuery 1.12 版本以上。（我沒有測試過更低的版本。因為範例網站使用的是 1.12 版本，所以特別提及。筆者使用的是 jQuery 2.x 版本。）
</p>

<p>
<b>
1. 下載檔案並應用 &lt;script src=""&gt;&lt;/script&gt; 指令。
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
下載
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
下載
</div>
</div>
</a>
</figure>
</p>


<p>
看起來會像這樣：
</p>

<span class="txt_fold">
展開查看
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
2. 進行 API 呼叫。
</b>
</p>
<p>
如下所示進行呼叫。
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
如果是想要從零開始打造一切的人，我建議嘗試自己開發一次。
</p>
<p>
但是，對於在業界工作時間緊迫的人，我推薦使用這款外掛。
</p>
<p>
（不過，如果您需要更高程度的自訂化功能！那麼我還是建議自己開發。）
</p>

<p>
使用經驗談 —— 非常方便。
</p>

<p>
<b>
只不過，我尚未測試過瀏覽器相容性。在 Chrome 48.0 以上版本可以正常運作。
</b>
</p>