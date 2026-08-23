---
layout: post
title: "[03] JavaScriptの概要"
description: "Untitled Document.md 3分間：第3章 JavaScript _05 JavaScriptとは何か？ JavaScriptはオブジェクトベースのスクリプトプログラミング言語です。詳細はWikipediaを参照してください。前回はCSSについて学びました…。"
date: 2017-01-05 21:47:43 +0900
section: blog
category: engineering
lang: ja
ref: 2017-01-05-legacy-194-engineering-03-untitled-document-md
tags:
  - "JavaScript"
  - "javascript"
  - "emca"
  - "use"
  - "1日3分ウェブ学習"
  - "engineering"
translation_source_hash: bc529d6c729f934c74b32c482334a01c4f52f86f471efa9bf59bb87503828863
---

<meta>
<title>
Untitled Document.md
</title>
<h1>
<a>
</a>
3分間：第3章 JavaScript
</h1>
<h3>
<a>
</a>
_05
<code>
JavaScript
</code>
とは何か？
</h3>
<p>
JavaScriptはオブジェクトベースのスクリプトプログラミング言語です。より詳細な内容は
<a href="https://ko.wikipedia.org/wiki/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8">
Wikipedia
</a>
を参照してください。
</p>
<p>
私たちは前章で
<code>
CSS
</code>
について学びました。
<code>
CSS
</code>
を通じて、私たちは
<code>
特定の属性を持つ何か
</code>
を作りました。今度は、この要素に対して
<code>
何をすべきか
</code>
を指示します。
</p>
<h3>
<a>
</a>
_06 ボタンをクリックしたとき、アラートを表示させる
</h3>
<blockquote>
<p>
HTML
</p>
</blockquote>
<pre>
<code>
&lt;div class="button" id="id_button"&gt;Button&lt;/div&gt;
</code>
</pre>
<blockquote>
<p>
CSS
</p>
</blockquote>
<pre>
<code>
&lt;style&gt;
.button {
    background-color:green;
    color:white;
    width:auto;
    height:auto;
}
&lt;/style&gt;
</code>
</pre>
<blockquote>
<p>
JavaScript
</p>
</blockquote>
<pre>
<code>
&lt;script&gt;
document.getElementById("id_button").addEventListener("click",function(){
alert("hello world");
});
&lt;/script&gt;
</code>
</pre>
<p>
上記のコードを
<code>
.html
</code>
ファイルにまとめると以下のようになります。
</p>
<pre>
<code>
&lt;!DOCTYPE HTML&gt;
&lt;html&gt;
&lt;head&gt;
&lt;style&gt;
.button {
    background-color:green;
    color:white;
    width:auto;
    height:auto;
}
&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div class="button" id="id_button"&gt;Button&lt;/div&gt;
&lt;script&gt;
document.getElementById("id_button").addEventListener("click",function(){
    alert("hello world");
});
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code>
</pre>
<p>
上記の内容は、該当する
<code>
div
</code>
タグをクリックした場合、
<code>
'hello world'
</code>
という文字列を表示する例です。
</p>
<p>
JavaScriptを利用すれば、特定のタグの
<code>
id
</code>
や
<code>
class
</code>
などを通じて、そのタグに特定の動作を付与できます。
<br>
クリックだけでなく、
<code>
mouseover
</code>
、
<code>
mouseout
</code>
といったマウスイベントに対するアクションも付与可能です。
</p>
<h3>
<a>
</a>
_07 ボタンの属性を変更する
</h3>
<blockquote>
<p>
HTML
</p>
</blockquote>
<pre>
<code>
&lt;div class="button" id="id_button"&gt;Button&lt;/div&gt;
</code>
</pre>
<blockquote>
<p>
CSS
</p>
</blockquote>
<pre>
<code>
&lt;style&gt;
.button {
    background-color:green;
    color:white;
    width:auto;
    height:auto;
}
&lt;/style&gt;
</code>
</pre>
<blockquote>
<p>
JavaScript
</p>
</blockquote>
<pre>
<code>
&lt;script&gt;
// id_button の文字色を赤色に変更する
document.getElementById("id_button").style.color="red";
&lt;/script&gt;
</code>
</pre>
<h3>
<a>
</a>
_08 ボタンのスタイルシートを無効化する
</h3>
<blockquote>
<p>
HTML
</p>
</blockquote>
<pre>
<code>
&lt;div class="button" id="id_button"&gt;Button&lt;/div&gt;
</code>
</pre>
<blockquote>
<p>
CSS
</p>
</blockquote>
<pre>
<code>
&lt;style id="btn_css"&gt;
.button {
    background-color:green;
    color:white;
    width:auto;
    height:auto;
}
&lt;/style&gt;
</code>
</pre>
<blockquote>
<p>
JavaScript
</p>
</blockquote>
<pre>
<code>
&lt;script&gt;
// ドキュメントに適用されているスタイルのうち、btn_css というIDを持つスタイルを無効化する
document.getElementById("btn_css").disabled = true;
&lt;/script&gt;
</code>
</pre>
<p>
今日は簡単にJavaScriptについて学びました。今回お伝えしたJavaScriptは、
<code>
学習
</code>
というより
<code>
雰囲気を感じる
</code>
程度だと思ってください。
<br>
以下はJavaScriptに関する簡単な学習資料です。
</p>
<p>
<a href="https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/JavaScript_basics">
MDN JavaScript 学習資料
</a>
</p>
<p>
実際、JavaScriptは
<code>
学習
</code>
をして初めて本格的に使用できるスクリプト言語です。JavaScriptを勉強していると
<code>
ECMAScript
</code>
という言葉を耳にするでしょう。
<br>
この言葉は、JavaScriptの
<code>
標準化
</code>
された仕様だと考えると分かりやすいです。
</p>
<blockquote>
<p>
cf.
<br>
今後JavaScriptを書く際、スクリプトの冒頭に
<code>
use strict
</code>
という記述を見かけることがあります。
<br>
これは標準に従うことを意味し、複数のブラウザで同じように動作するように設計されたスクリプトであると解釈できます。
</p>
</blockquote>
<h1>
<a>
</a>
まとめ
</h1>
<h4>
<a>
</a>
- JavaScriptはHTMLに動きを与える。
</h4>
<h4>
<a>
</a>
- JavaScriptは
<code>
document
</code>
に適用されている属性値を変更できる。
</h4>
<h4>
<a>
</a>
- JavaScriptは
<code>
document
</code>
のタグを動的に変更できる。
</h4>
<h4>
<a>
</a>
- 今日少しだけ触れたJavaScriptは全体の1%程度に過ぎない。残りの99%は本当に無限に広がっている。
</h4>
<blockquote>
<p>
<strong>
3分間予告
</strong>
</p>
</blockquote>
<ul>
<li>
JavaScriptを一からすべて学ぶのは大変そうだが、もっと簡単に使える方法はないだろうか？
</li>
</ul>