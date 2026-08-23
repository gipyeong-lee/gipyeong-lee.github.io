---
layout: post
title: "[node.js] forever"
description: "node.jsに関する投稿が続いていますね。先日構築したSide Effect Studioサイトで使用したものを整理・共有しようとすると、node.js関連の投稿ばかり続いてしまいます。早く整理して他の内容も見ていかなければなりません。昨年のUpst..."
date: 2015-08-27 19:29:31 +0900
section: blog
category: engineering
lang: ja
ref: 2015-08-27-legacy-105-engineering-node-js-forever
tags:
  - "Forever"
  - "node.js"
  - "npm"
  - "Scrap"
  - "engineering"
noindex: true
translation_source_hash: ac81f4b878a4bcd35cf582e2d4364fcb94198723d58aa84d87dfeb3b0d2991ea
---

<p>
<span>
node.jsに関する投稿が続いていますね。先日構築した
</span>
<a href="http://sideeffect.kr/" target="_blank">
Side Effect Studioサイト
</a>
<span>
で使用したものを整理・共有しようとすると、node.js関連の投稿ばかり続いてしまいます。早く整理して他の内容も見ていかなければなりません。
</span>
<br>
<br>
<span>
昨年、
</span>
<a href="http://blog.outsider.ne.kr/544" target="_blank">
UpstartとMonitでnode.js Applicationをサービスする
</a>
<span>
という投稿をしたことがありますが、これはかなり有用である一方、管理面で非常に面倒な点があります。upstartスクリプトを作成したり、monitにルールを適用したりする作業は少し手間がかかります。他に代わりとなる手段を知らなかったのでUpstartとMonitを使用していましたが、その投稿以降、nodeアプリのインスタンスを管理してくれる
</span>
<a href="https://github.com/indexzero/forever" target="_blank">
forever
</a>
<span>
というツールが公開されました。
</span>
<br>
<br>
<span>
<a href="https://github.com/indexzero/forever" target="_blank">
forever
</a>
はnpmを使用して
<span>
npm install forever
</span>
コマンドで簡単にインストールが可能であり、非常にシンプルなコマンドでnode.jsで作成したアプリを実行し、予期せず終了した際に再実行したり、stdoutをログファイルとして残したりといった管理をしてくれるツールです。
</span>
<span>
使用してみると多少のバグはありますが、既存のUpstartとMonitの組み合わせに比べて操作性が非常に便利で、node.jsアプリの管理はすべてforeverに切り替えました。
</span>
<br>
<br>
</p>
<blockquote>
usage: forever [start | stop | stopall | list | cleanlogs] [options] SCRIPT [script options]
<br>
<br>
options:
<br>
start          start SCRIPT as a daemon
<br>
stop           stop the daemon SCRIPT
<br>
stopall        stop all running forever scripts
<br>
list           list all running forever scripts
<br>
cleanlogs      [CAREFUL] Deletes all historical forever log files
</blockquote>
<p>
<br>
<span>
foreverの使い方は上記の通りです。
</span>
<span>
登録したいスクリプトを
<span>
forever start app.js
</span>
のように実行すれば完了です。プロセスを確認するとforeverに関するプロセスが別個に存在し、実行したapp.jsプロセスが終了した場合、自動的に再実行してくれます。現在動作しているスクリプトを確認するには
<span>
forever list
</span>
を実行します。
</span>
<br>
<br>
</p>
<div class="imageblock center">
<img src="http://blog.outsider.ne.kr/attach/1/1154848314.gif.pagespeed.ce.t4pwqQMTlL.gif" alt="foreverにnodeアプリを登録した画面" height="63" width="550">
</div>
<p>
<br>
<span>
プロセスを終了する場合は、先に表示された番号を使用して
<span>
forever stop 番号
</span>
を使えば良いです。
</span>
<span>
一目でどのプロセスを現在使用しているか把握でき、ログファイルを自動的に接続してくれるため、非常に便利です。
</span>
<br>
<br>
</p>
<div class="imageblock center">
<img src="http://blog.outsider.ne.kr/attach/1/1122859785.gif.pagespeed.ce.brAyzYu1ox.gif" alt="登録されたnodeアプリを終了した画面" height="57" width="550">
</div>
<p>
<br>
<br>
<br>
<span>
少し使用してみた経験では、ある程度安定しているようです。（アクセス者がそれほど多くないため、致命的なエラーが発生する確率が低く、正確な判断ではありませんが、なんとなく...）ただ、バグがあるのか、forever startでアプリを登録した際、プロセスは正常に起動したにもかかわらずforeverに登録されず、リストに表示されないケースがあります。何度かテストを行いましたが、規則性は見つけられませんでした。そのような場合は、該当スクリプトとそのforeverに対するプロセスを強制終了してから再度登録する必要があります。この点以外は、管理・使用ともに便利で非常に優れていると思います。
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
参考資料 :
<a href="http://blog.outsider.ne.kr/590" target="_blank" class="tx-link">
</a>
</span>
<font>
<span>
<a href="http://blog.outsider.ne.kr/590" target="_blank" class="tx-link">
http://blog.outsider.ne.kr/590
</a>
</span>
</font>
</p>