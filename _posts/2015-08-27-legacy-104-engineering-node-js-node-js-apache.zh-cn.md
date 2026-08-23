---
layout: post
title: "[node.js] 同时运行 Node.JS 和 Apache"
description: "Nederlandstalig? U woont in Vlaanderen? Bezoek Vlakbij.me en kom in contact met de beste handelaars in je buurt Hosting A Node.js Site Through Apache I recen..."
date: 2015-08-27 15:45:17 +0900
section: blog
category: engineering
lang: zh-cn
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
通过 Apache 托管 Node.js 网站
</h1>
<p>
我最近花了一些时间研究如何通过 Apache 托管 Node.js 网站，所以我想写一篇文章分享一下我的实现方法。当然，这种方法只有在您已经拥有一台运行 Apache 的服务器，并且希望在对服务器影响/更改最小的情况下添加 Node.js 网站时才有意义。如果您还没有使用 Apache，只是想发布一个 Node.js 网站，最好直接使用 Node.js 来托管，或者在它前面放置 Nginx，因为它比 Apache 更轻量级。但无论如何，这里是如何通过 Apache 实现它的方法。
</p>
<p>
首先，您需要一种在系统启动时自动启动 Node.js 进程，并在系统关闭时将其关闭的方法。这取决于您运行的服务器类型。就我而言，这是一台 Debian 服务器，所以我直接使用了
<a href="https://github.com/nicokaiser/node-monit/tree/master/init.d" target="_blank">
Nico Kaiser 的 sysv init 脚本
</a>
。另一个流行的替代方案是 upstart 实用程序，如果您使用的是 Ubuntu，它已经预装了。一旦您有了 start|stop|restart 脚本，您还需要一些东西来监控 Node.js 进程，以便在它挂掉时重启它。一个易于使用的工具是
<a href="http://mmonit.com/monit/" target="_blank">
monit
</a>
。Nico Kaiser 在
<a href="https://github.com/nicokaiser/node-monit/tree/master/monit/conf.d" target="_blank">
Github
</a>
上也为 Node.js 提供了一个很好的示例脚本。
</p>
<p>
一旦您有了 sysv init 或 upstart 脚本以及 monit，您的 Node.js 进程就可以在服务器上保持运行。当然，您可能将其设置为监听除 80 端口之外的其他端口，因为那是您的 Apache 服务器正在监听的端口。因此，现在您唯一要做的就是配置 Apache，将所有通过 URL 进入 80 端口的 Node.js 网站请求代理到您本地的 Node.js 进程。您首先需要安装
<a href="http://httpd.apache.org/docs/2.1/mod/mod_proxy.html" target="_blank">
mod_proxy
</a>
和
<a href="http://httpd.apache.org/docs/2.0/mod/mod_proxy_http.html" target="_blank">
mod_proxy_http
</a>
。之后，实现它的配置非常简单：
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
view raw
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
就是这样。每个进入 http://thatextramile.be 或 http://www.thatextramile.be 的请求都将转发到 Node.js 正在监听的 http://localhost:3000。请注意，ProxyPassReverse 是必需的，以确保所有 HTTP 响应标头都包含代理 URL 而不是真实 URL (localhost)。
</p>
<p>
如果您需要 Node.js 提供的原始吞吐量，这种解决方案远非最佳。每个通过 Apache 进入的请求都会导致 Apache 线程等待/阻塞，直到从您的 Node.js 进程返回响应。这本质上与通过 Apache 托管 PHP 或 Ruby 时相同，所以这不是问题，但它确实消除了使用 Node.js 的好处之一。同样，这种方法只有在您已经使用 Apache 托管其他网站，并且只想以最小的影响将 Node.js 网站添加到服务器时才适用。
</p>
<p>
<em>
由 Davy Brion 编写，发布于 2012-01-15 15:23:09
</em>
</p>
<p>
参考资料：
<a href="http://thatextramile.be/blog/2012/01/hosting-a-node-js-site-through-apache/" target="_blank" class="tx-link">
http://thatextramile.be/blog/2012/01/hosting-a-node-js-site-through-apache/
</a>
</p>

<p>
在 Apache 内部设置代理，
</p>
<p>
并将以该服务器名称 (ServerName) 进入的所有请求发送到相应的端口。
</p>