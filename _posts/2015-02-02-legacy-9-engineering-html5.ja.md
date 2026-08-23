---
layout: post
title: "HTML5の新しい内容"
description: "こんにちは。HTML5を学習しながら学んだ内容をまとめるための場所です。特定の機能について深く掘り下げた投稿をする場所ではないことをあらかじめご了承ください。DTD（Document Type Definition）はDocument Type Definitionの略語です。DTDとは、あるタグ、属性、値が特定のHTMLドキュメント内で有効かどうかを記述するテキストファイルです。各HTMLバージョンにはそれに適したDTDがあるそうです。通常、これはHTMLドキュメントの最初の行にdoctype宣言を通じて記述します。これにより、どのバージョンのHTMLまたはXHTMLが使用されているかをブラウザに伝えます。"
date: 2015-02-02 04:23:29 +0900
section: blog
category: engineering
lang: ja
ref: 2015-02-02-legacy-9-engineering-html5
tags:
  - "Web"
  - "engineering"
translation_source_hash: a389f43501977c62c13d3c611499e7cf5a217c9507339e4ae160383c6ef687cb
---

<p>
<span>
こんにちは。
</span>
</p>
<p>
<span>
HTML5を学習しながら学んだ内容をまとめるための場所です。特定の機能について深く掘り下げた投稿をする場所ではないことをあらかじめご了承ください。
</span>
</p>

<p>
<b>
<span>
DTD (Document Type Definition)
</span>
</b>
</p>
<p>
<span>
Document Type Definitionの略語です。DTDとは、あるタグ、属性、値が特定のHTMLドキュメント内で有効かどうかを記述するテキストファイルです。各HTMLバージョンにはそれに適したDTDがあるそうです。通常、これはHTMLドキュメントの最初の行にdoctype宣言を通じて記述します。これにより、どのバージョンのHTMLまたはXHTMLが使用されているかをブラウザに伝えます。
</span>
<span>
このようなdoctype宣言を省略すると、多くのブラウザはQuirks Mode（互換モード）という状態に陥るといいます。
</span>
</p>
<p>
<span>
doctype宣言がされていないページに出会うと、「おや、このページは非常に大昔に書かれたページだな」と判断してしまうそうです。そして「なら適当に表示してやろう」という結論に至るのです。
</span>
</p>
<p>
<span>
もし自分が作成したウェブページがブラウザで意図した通りに表示されない場合は、doctype宣言を確認してみるのが良いでしょう。
</span>
</p>
<p>
<span>
以下は各バージョン別のdoctype宣言です。
</span>
</p>


<div>

<p>
<b>
<span>
HTML5
</span>
</b>
</p>
<p>
<span>
&lt;!doctype html&gt;
</span>
</p>

<p>
<b>
<span>
HTML4
</span>
</b>
</p>
<p>
<span>
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"&gt;
</span>
</p>

<p>
<b>
<span>
XHTML 1.0
</span>
</b>
</p>
<p>
<span>
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 1.010 Transitional//EN" "http://www.w3.org/TR/html1/DTD
</span>
<span>
/xhtml1-transitional.dtd"&gt;
</span>
</p>
<p>
<span>
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
</span>
</p>

</div>

<br>


<div>
<br>
</div>
<p>
<b>
<span>
IE9以下のバージョンに対処する私たちの姿勢
</span>
</b>
</p>

<p>
<span>
1. IE8にHTML5を理解させたい場合。
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
&lt;/head&gt;タグの前に、以下のようなコードを挿入すれば良いです。
</p>

<div>
<p>
&lt;!--[if lt IE 9]&gt;
</p>
<p>
&lt;script src="//html5shiv.googlecode.com/svn/trunk/html5.js"&gt;&lt;/script&gt;
</p>
<p>
&lt;![endif]--&gt;
</p>
</div>

<p>
条件付きコメントを利用して、IE9より古いIEのみ、つまりIE 6,7,8だけがこのコードを理解し、コードが適用されるとのことです。不思議なことにテストしてみたところ、Chromeでは該当スクリプトが読み込まれませんでした。IEのみを判別しているようです。
</p>

<p>
<span>
2. IE8の互換表示および互換表示設定リストを回避する方法
</span>
</p>
<p>
以下のコードを&lt;head&gt;内に入れてください。
</p>

<div>
<p>
&lt;head&gt;
</p>
<p>
&lt;meta http-equiv="X-UA-Compatible" content="IE=edge" /&gt;
</p>
<p>
...
</p>
<p>
&lt;/head&gt;
</p>
</div>


<p>
<b>
<span>
HTMLコードに外部スタイルシートを接続する
</span>
</b>
</p>

<p>
外部スタイルシートをウェブページに接続する方法は、&lt;link&gt;タグを使用することです。
</p>
<p>
以下は各バージョン別の使用方式です。
</p>


<div>
<p>
<b>
<span>
HTML5
</span>
</b>
</p>
<p>
<span>
&lt;link rel="stylesheet" href="css/styles.css"&gt;
</span>
</p>

<p>
<b>
<span>
HTML4
</span>
</b>
</p>
<p>
<span>
&lt;link rel="stylesheet" type="text/css" href = "css/styles.css" &gt;
</span>
</p>

<p>
<b>
<span>
XHTML 1.0
</span>
</b>
</p>
<p>
<font>
&lt;link rel="stylesheet" type="text/css" href="css/styles.css" /&gt;
</font>
</p>
</div>