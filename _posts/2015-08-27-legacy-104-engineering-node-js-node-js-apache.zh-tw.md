---
layout: post
title: "[node.js] 同時運行 Node.JS 與 Apache"
description: "Nederlandstalig? U woont in Vlaanderen? Bezoek Vlakbij.me en kom in contact met de beste handelaars in je buurt Hosting A Node.js Site Through Apache I recen..."
date: 2015-08-27 15:45:17 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2015-08-27-legacy-104-engineering-node-js-node-js-apache
tags:
  - "Scrap"
  - "engineering"
noindex: true
translation_source_hash: 96817dcb447eaa9aa5e3607d20679fc0d838653ec6ad5cfb018649b7baef02b6
---

<p>
<small>
Nederlandstalig? U woont in Vlaanderen? Bezoek
<a href="http://vlakbij.me/">
Vlakbij.me
</a>
en kom in contact met de beste handelaars in je buurt
</small>
</p>
<h1>
透過 Apache 託管 Node.js 網站
</h1>
<p>
最近我花了一些時間研究如何透過 Apache 託管 Node.js 網站，所以我想寫一篇文章分享我的做法。當然，這種方法僅在您已經有一台運行 Apache 的伺服器，且希望以最小的影響或變動來新增 Node.js 網站時才有意義。如果您目前沒有使用 Apache，只是想發佈一個 Node.js 網站，直接使用 Node.js 來託管，或是使用 Nginx 作為反向代理會更好，因為它們比 Apache 更輕量。不過，無論如何，以下是透過 Apache 達成目標的方法。
</p>
<p>
首先，您需要一種在系統開機時自動啟動 Node.js 進程，並在系統關機時將其關閉的方法。這取決於您使用的伺服器類型。以我的案例來說，我使用的是 Debian 伺服器，所以我直接使用了
<a href="https://github.com/nicokaiser/node-monit/tree/master/init.d" target="_blank">
Nico Kaiser 的 sysv init 腳本
</a>
。另一個熱門的替代方案是 upstart 工具，如果您使用的是 Ubuntu，它已經預先安裝好了。一旦您設置好了 start|stop|restart 腳本，您就會需要一個工具來監控 Node.js 進程，以便在它掛掉時自動重啟。一個簡單好用的工具是
<a href="http://mmonit.com/monit/" target="_blank">
monit
</a>
。Nico Kaiser 在
<a href="https://github.com/nicokaiser/node-monit/tree/master/monit/conf.d" target="_blank">
Github
</a>
上同樣提供了一個很好的 Node.js 監控範例腳本。
</p>
<p>
一旦您安裝好了 sysv init 或 upstart 腳本以及 monit，您的 Node.js 進程就能在伺服器上持續運行。當然，您很可能將它設置為監聽 80 埠以外的埠號，因為 Apache 伺服器正在佔用 80 埠。因此，現在您唯一需要做的，就是配置 Apache，將所有透過 URL 進入 80 埠的 Node.js 網站請求，代理到您本地的 Node.js 進程。您首先需要安裝
<a href="http://httpd.apache.org/docs/2.1/mod/mod_proxy.html" target="_blank">
mod_proxy
</a>
和
<a href="http://httpd.apache.org/docs/2.0/mod/mod_proxy_http.html" target="_blank">
mod_proxy_http
</a>
。之後，配置過程非常簡單：
</p>
<div class="gist">
<div class="gist-file">
<div class="gist-data">
<div class="js-gist-file-update-container js-task-list-container file-box">
<div class="file">
<div class="blob-wrapper data type-xml">
<table class="highlight tab-size js-file-line-container">
<tbody>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
&lt;
<span class="pl-ent">
VirtualHost
</span>
109.74.199.47:80&gt;
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
ServerAdmin davy.brion@thatextramile.be
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
ServerName thatextramile.be
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
ServerAlias www.thatextramile.be
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
ProxyRequests off
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
&lt;
<span class="pl-ent">
Proxy
</span>
*&gt;
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
Order deny,allow
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
Allow from all
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
&lt;/
<span class="pl-ent">
Proxy
</span>
&gt;
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
&lt;
<span class="pl-ent">
Location
</span>
/&gt;
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
ProxyPass http://localhost:3000/
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
ProxyPassReverse http://localhost:3000/
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
&lt;/
<span class="pl-ent">
Location
</span>
&gt;
</td>
</tr>
<tr>
<td class="blob-num js-line-number">
</td>
<td class="blob-code blob-code-inner js-file-line">
&lt;/
<span class="pl-ent">
VirtualHost
</span>
&gt;
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<div class="gist-meta">
<a href="https://gist.github.com/davybrion/3728871/raw/364f2f0ef2fc3eddc611db8ab2319e2eadcbbbfb/s1.xml">
檢視原始碼
</a>
<a href="https://gist.github.com/davybrion/3728871#file-s1-xml">
s1.xml
</a>
hosted with ❤ by
<a href="https://github.com/">
GitHub
</a>
</div>
</div>
</div>
<p>
就這麼簡單。所有發送到 http://thatextramile.be 或 http://www.thatextramile.be 的請求，都會被轉發到 Node.js 正在監聽的 http://localhost:3000。請注意，ProxyPassReverse 是必須的，以確保所有 HTTP 回應標頭 (response headers) 都會包含代理後的 URL，而不是真實的 URL (localhost)。
</p>
<p>
如果您需要 Node.js 提供的原始吞吐量，這個方案遠非最佳選擇。每個通過 Apache 進來的請求都會導致一個 Apache 線程在 Node.js 進程返回回應之前處於等待/阻塞狀態。這本質上與通過 Apache 託管 PHP 或 Ruby 時相同，所以並不是問題，但它確實消除了使用 Node.js 的好處之一。再次強調，這種方法僅在您已經使用 Apache 託管其他網站，並且只想以對伺服器最小的影響來新增一個 Node.js 網站時才有意義。
</p>
<p>
<em>
作者：Davy Brion，發佈於 2012-01-15 15:23:09
</em>
</p>
<p>
參考資料：
<a href="http://thatextramile.be/blog/2012/01/hosting-a-node-js-site-through-apache/" target="_blank" class="tx-link">
http://thatextramile.be/blog/2012/01/hosting-a-node-js-site-through-apache/
</a>
</p>

<p>
在 Apache 內設定代理，
</p>
<p>
並將所有透過該 ServerName 進入的請求發送到對應的埠號。
</p>