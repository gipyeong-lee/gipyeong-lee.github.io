---
layout: post
title: "[node.js] Node.JS 와 apache 동시에 돌리기"
description: "Nederlandstalig? U woont in Vlaanderen? Bezoek Vlakbij.me en kom in contact met de beste handelaars in je buurt Hosting A Node.js Site Through Apache I recen..."
date: 2015-08-27 15:45:17 +0900
section: blog
category: engineering
lang: ko
ref: 2015-08-27-legacy-104-engineering-node-js-node-js-apache
tags:
  - "Scrap"
  - "engineering"
noindex: true
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
Hosting A Node.js Site Through Apache
</h1>
<p>
I recently lost some time trying to figure out how to host a Node.js site through Apache, so I figured I might as well write a post about how I got it working. Of course, this approach only makes sense if you already have a server that's running Apache and you want to add your Node.js site with minimal impact/changes on your server. If you're not using Apache already but just want to publish a Node.js site, you're better off using Node.js to host it directly, or to put Nginx in front of it since it's more lightweight than Apache. But anyways, here's how you get it working with Apache.
</p>
<p>
First of all, you need a way to start your Node.js process automatically when your system boots, and to shut it down when the system is shut down. This will depend on the type of server you're running on. In my case, it's a Debian server so I just went with the
<a href="https://github.com/nicokaiser/node-monit/tree/master/init.d" target="_blank">
sysv init script from Nico Kaiser
</a>
. Another popular alternative is the upstart utility, which is already preinstalled if you're using Ubuntu. Once you have a start|stop|restart script in place, you'll want something to monitor the Node.js process to restart it in case it goes down. An easy to use tool for this is
<a href="http://mmonit.com/monit/" target="_blank">
monit
</a>
. Nico Kaiser again has a good example script available for Node.js on
<a href="https://github.com/nicokaiser/node-monit/tree/master/monit/conf.d" target="_blank">
Github
</a>
.
</p>
<p>
Once you have your sysv init or upstart script in place, as well as monit, your Node.js process can stay running on your server. Of course, you probably have it set to listen to connections on some other port than port 80 because that's what your Apache server is listening on. So now, the only thing you have to do is configure Apache to proxy all requests coming in on port 80 through the URL of your Node.js site to your local Node.js process. You'll first need to install
<a href="http://httpd.apache.org/docs/2.1/mod/mod_proxy.html" target="_blank">
mod_proxy
</a>
and
<a href="http://httpd.apache.org/docs/2.0/mod/mod_proxy_http.html" target="_blank">
mod_proxy_http
</a>
. After that, the configuration to make it work is quite easy:
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
And that's it. Every request coming in at http://thatextramile.be or http://www.thatextramile.be will be forwarded to http://localhost:3000 where Node.js is listening. Note that the ProxyPassReverse is required to make sure that all HTTP response headers will contain the proxied URL instead of the real one (localhost).
</p>
<p>
If you need the raw throughput that Node.js offers, this solution is far from optimal. Every request that comes in through Apache will cause an Apache thread to wait/block until the response is returned from your Node.js process. This is essentially the same as when hosting PHP or Ruby through Apache, so it's not a problem, but it does take away one of the benefits of using Node.js. Again, this approach only makes sense if you're already using Apache to host other sites and you just want to add a Node.js site with minimal impact to your server.
</p>
<p>
<em>
Written by Davy Brion, published on 2012-01-15 15:23:09
</em>
</p>
<p>
출처 :
<a href="http://thatextramile.be/blog/2012/01/hosting-a-node-js-site-through-apache/" target="_blank" class="tx-link">
http://thatextramile.be/blog/2012/01/hosting-a-node-js-site-through-apache/
</a>
</p>

<p>
아파치내에서 프록시를 설정하고
</p>
<p>
해당 서버name 으로 들어오는 녀석들을 다 해당 포트로 보내준다.
</p>
