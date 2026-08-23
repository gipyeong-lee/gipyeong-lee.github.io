---
layout: post
title: "[node.js] Node.jsとApacheを同時に動かす"
description: "Apache経由でNode.jsサイトをホスティングする方法について。すでにApacheで運用しているサーバーに、Node.jsサイトを最小限の変更で追加する方法を解説します。"
date: 2015-08-27 15:45:17 +0900
section: blog
category: engineering
lang: ja
ref: 2015-08-27-legacy-104-engineering-node-js-node-js-apache
tags:
  - "Scrap"
  - "engineering"
noindex: true
translation_source_hash: 96817dcb447eaa9aa5e3607d20679fc0d838653ec6ad5cfb018649b7baef02b6
---

<p>
<small>
オランダ語話者ですか？フランダース地方にお住まいですか？<a href="http://vlakbij.me/">Vlakbij.me</a>にアクセスして、お近くの優良店とつながりましょう。
</small>
</p>
<h1>
Apache経由でNode.jsサイトをホスティングする
</h1>
<p>
最近、Node.jsサイトをApache経由でホスティングする方法を調べるのに少し時間を費やしたので、その設定方法について記事にまとめました。もちろん、このアプローチが理にかなっているのは、すでにApacheが動作しているサーバーがあり、そのサーバーへの影響や変更を最小限に抑えつつNode.jsサイトを追加したい場合のみです。もし現在Apacheを使っておらず、単にNode.jsサイトを公開したいだけであれば、Node.jsで直接ホスティングするか、Apacheよりも軽量なNginxをフロントに置く方が良いでしょう。とはいえ、Apacheを使って実現する方法は以下の通りです。
</p>
<p>
まず、システムの起動時にNode.jsプロセスを自動的に開始し、シャットダウン時に停止させる方法が必要です。これは動作しているサーバーの種類によって異なります。私の場合、Debianサーバーだったので、<a href="https://github.com/nicokaiser/node-monit/tree/master/init.d" target="_blank">Nico Kaiser氏のsysv initスクリプト</a>を採用しました。もう一つの一般的な選択肢として、Ubuntuであればプリインストールされているupstartユーティリティがあります。start|stop|restartスクリプトが用意できたら、Node.jsプロセスがダウンした場合に再起動できるよう監視ツールが必要です。簡単に使えるツールとして<a href="http://mmonit.com/monit/" target="_blank">monit</a>があります。これもNico Kaiser氏が<a href="https://github.com/nicokaiser/node-monit/tree/master/monit/conf.d" target="_blank">Github</a>でNode.js用の優れた設定スクリプト例を公開しています。
</p>
<p>
sysv initまたはupstartスクリプトとmonitを導入すれば、Node.jsプロセスをサーバー上で常駐させることができます。もちろん、通常Apacheはポート80でリッスンしているため、Node.jsはそれとは別のポートで接続を待ち受けるように設定しているはずです。あとは、ポート80に入ってくるNode.jsサイト宛のリクエストを、ローカルのNode.jsプロセスへプロキシするようにApacheを設定するだけです。最初に<a href="http://httpd.apache.org/docs/2.1/mod/mod_proxy.html" target="_blank">mod_proxy</a>と<a href="http://httpd.apache.org/docs/2.0/mod/mod_proxy_http.html" target="_blank">mod_proxy_http</a>をインストールする必要があります。その後の設定は非常に簡単です。
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
以上です。http://thatextramile.be または http://www.thatextramile.be に来るすべてのリクエストは、Node.jsが待ち受けている http://localhost:3000 に転送されます。ProxyPassReverseは、すべてのHTTPレスポンスヘッダーに実際のURL（localhost）ではなくプロキシされたURLが含まれるようにするために必要な点に注意してください。
</p>
<p>
もしNode.jsが提供する生のパフォーマンス（スループット）を必要とする場合、この解決策は最適とは言えません。Apacheを介してくるすべてのリクエストは、Node.jsプロセスからレスポンスが返されるまでApacheのスレッドが待機/ブロックされることになるためです。これは基本的にPHPやRubyをApache経由でホスティングする場合と同じなので問題ではありませんが、Node.jsを使用する利点の一つが失われてしまいます。重ねて言いますが、このアプローチはすでにApacheを使って他のサイトをホスティングしており、サーバーへの影響を最小限に抑えてNode.jsサイトを追加したいという場合にのみ理にかなっています。
</p>
<p>
<em>
執筆：Davy Brion、公開日時：2012-01-15 15:23:09
</em>
</p>
<p>
参照元 :
<a href="http://thatextramile.be/blog/2012/01/hosting-a-node-js-site-through-apache/" target="_blank" class="tx-link">
http://thatextramile.be/blog/2012/01/hosting-a-node-js-site-through-apache/
</a>
</p>

<p>
Apache内でプロキシを設定し、
</p>
<p>
該当するServerNameへのリクエストをすべて指定のポートに送信する。
</p>