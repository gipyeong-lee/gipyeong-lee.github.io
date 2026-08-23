---
layout: post
title: "[Bootstrap,JQuery] テーブルをきれいに整理する"
description: "こんにちは。今回はGMSツール開発において、Frontendで役立つプラグインをご紹介します。以下のURLを参照すると確認できます。https://datatables.net/examples/styling/bootstrap.html 以下は適用（前）と..."
date: 2016-02-24 18:43:22 +0900
section: blog
category: engineering
lang: ja
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
こんにちは。
</p>

<p>
今回はGMSツール開発において、Frontendで役立つプラグインをご紹介します。
</p>
<p>
以下のURLを参照すると確認できます。
</p>

<p>
<a href="https://datatables.net/examples/styling/bootstrap.html" target="_blank" class="tx-link">
https://datatables.net/examples/styling/bootstrap.html
</a>
<br>
</p>


<p>
以下は適用（前）と（後）のスクリーンショットです。
</p>


<p>
<figure class="imageblock alignCenter" width="681" height="416">

<figcaption>
適用前
</figcaption>
</figure>
</p>

<p>
<b>
&lt;適用前&gt;
</b>
</p>




<p>
上の写真は、現在テスト中の約2千件程度のデータをプラグインなしで表示した様子です。
</p>
<p>
（今後、データがものすごく蓄積されたら…大変なことになりそうですよね？）
</p>



<p>
次はプラグインを適用した様子です。
</p>







<p>
10、20、50、100件単位で整理して見ることができ、Searchを通じてテーブルのRowを検索でき、Pagination機能も提供してくれます。
</p>
<p>
「手作業で実装してみたい」という気持ちがある、あるいは一度も実装したことがない場合は（ページネーション、エントリ、検索）、直接実装してみることをお勧めします。
</p>

<p>
実装した経験があり、作業が手間に感じられる場合は、該当プラグインを使って楽に作業することをお勧めします。
</p>


<p>
使用方法は以下に簡単にまとめます。
</p>
<p>
jQuery 1.12バージョン以上で使用することをお勧めします。（それ以下のバージョンはテストしていません。サンプルサイトで使用されたバージョンが1.12なので記載しました。筆者は2.x系のjQueryを使用しました。）
</p>

<p>
<b>
1. ファイルをダウンロードし、&lt;script src=""&gt;&lt;/script&gt;スクリプトを適用してください。
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
ダウンロード
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
ダウンロード
</div>
</div>
</a>
</figure>
</p>


<p>
以下のようになるでしょう。
</p>

<span class="txt_fold">
もっと見る
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
2. apiを呼び出します。
</b>
</p>
<p>
以下のように呼び出します。
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
最初からすべて自分で作りたいという方は、一度作ってみることをお勧めします。
</p>
<p>
しかし、現場で時間に追われている方には、使用してみることをお勧めします。
</p>
<p>
（ただし、より高度なカスタマイズが必要な場合は、自作することをお勧めします。）
</p>

<p>
使用した感想としては、便利です。
</p>

<p>
<b>
ただし、ブラウザの互換性はテストできていません。Chrome 48.0以上のバージョンでは正常に動作します。
</b>
</p>