---
layout: post
title: "ウェブ"
description: "こんにちは。今後、ウェブフロントエンドの学習中に経験したことや、解決した方法を書き留めておこうと思います。テスト環境はie8、chrome、safariです。CSS : Bootstrap ie8 : あまり綺麗に適用されません > 直接cssを作成して適用..."
date: 2015-03-12 02:54:19 +0900
section: blog
category: essay
lang: ja
ref: 2015-03-12-legacy-29-essay
tags:
  - "Web"
  - "Location"
  - "ウェブ"
  - "merge"
  - "jquery"
  - "addEventListener"
translation_source_hash: 1460fd73be3c032ed2a9c6c551d1c8e09ea6f19e4807d39aa6b15a0698d1784e
---

<p>
<span>
<span>
<span>
こんにちは。
</span>
</span>
</span>
</p>
<p>
<span>
<span>
<span>
今後、ウェブフロントエンドの学習中に経験したことや、解決した方法を書き留めておこうと思います。
</span>
<br>
</span>
</span>
</p>
<p>
<span>
<span>
<span>
テスト環境はie8、chrome、safariです。
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
ie8 : あまり綺麗に適用されません > 直接cssを作成して適用させました。
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
ie8 : 動作しません。以下のように処理しました。ie8ではattachEventを通じて処理します。
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
JQUERYのmergeを通じて配列を結合する場合、arr1、arr2の順序によってデータが変わるという不思議な経験をしました。
</span>
</font>
</p>
<p>
<font>
<span>
注意しなければ... ㅡ,.ㅡ... ;;
</span>
</font>
</p>
<p>
<font>
<span>
これのせいでデータマッピングに一日を費やしました... はぁ....
</span>
</font>
</p>
<p>
<font>
<span>
助けてください。
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
Javascriptによるページ遷移関連
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
現在のフレームのすぐ上の階層のパスを該当urlに設定
</span>

<span>
( ページ遷移される )
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
最も外側に位置するdocumentのlocationパスを該当urlに設定
</span>

<span>
( ページ遷移される )
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
現在のフレームを開いたdocumentのlocationパスを該当urlに設定 ( ページ遷移される )
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
JQUERYでページ遷移後、特定のcssやjavascriptをonloadさせたい場合
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
上記の例のように、該当divの中にカスタマイズしたスクリプトやスタイルコードを挿入します。
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