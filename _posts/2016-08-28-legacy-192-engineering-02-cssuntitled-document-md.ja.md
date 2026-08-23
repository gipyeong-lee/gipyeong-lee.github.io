---
layout: post
title: "[02] スタイルシート CSSUntitled Document.md"
description: "Untitled Document.md 3分 : 第2章 CSS _04 CSSとは何か？ スタイルシートは、HTMLで作成したドキュメントが実際にどのように表示されるかを記述するための言語です。もし、皆さんがHTMLを使って子犬を描いたと想像してみてください。その子犬の尻尾がどれくらい長いか、頭がどれくらい小さいか、体格はどれくらいか。このようなことを記述できるようにした言語が、まさにCSSです。"
date: 2016-08-28 01:14:05 +0900
section: blog
category: engineering
lang: ja
ref: 2016-08-28-legacy-192-engineering-02-cssuntitled-document-md
tags:
  - "CSS"
  - "Style"
  - "3分WEB勉強"
  - "engineering"
translation_source_hash: 76b7f799565e3fab200960a4baa92ed89a264609a4fca67393948f9e9a22a847
---

<meta>
<title>
Untitled Document.md
</title>
<h1>
<a>
</a>
3分 : 第2章 CSS
</h1>
<h3>
<a>
</a>
_04 CSSとは何か？
</h3>
<p>
スタイルシートは、
<strong>
HTML
</strong>
で作成したドキュメントが実際にどのように表示されるかを記述するための言語です。もし、皆さんがHTMLを使って子犬を描いたと想像してみてください。
</p>
<p>
その子犬の尻尾がどれくらい長いか、頭がどれくらい小さいか、体格はどれくらいか。このようなことを記述できるようにした言語が、まさに
<strong>
CSS
</strong>
です。
</p>
<p>
言い換えれば、皆さんが骨組みを描いて、その上に服を着せたとします。ここまでの作業が
<strong>
HTML
</strong>
だとすれば、その服のサイズはどれくらいか、何色かといった属性を加えていくのがCSSの役割です。
</p>
<p>
では、整理してみましょう。
<strong>
HTML
</strong>
と
<strong>
CSS
</strong>
の役割は以下の通りです。
</p>
<blockquote>
<p>
HTML
</p>
</blockquote>
<ul>
<li>
骨組みに服を着せる。
</li>
</ul>
<blockquote>
<p>
CSS
</p>
</blockquote>
<ul>
<li>
服がどのような見た目か（サイズや色など）を指定する。
</li>
</ul>
<p>
さて、CSSの役割がわかりましたね。それではCSSの基礎を学んでみましょう。
</p>
<blockquote>
<p>
CSSの使用方法
</p>
</blockquote>
<ul>
<li>
<strong>
css
</strong>
ファイルを作成後、
<strong>
HTML
</strong>
ファイルで参照して使用します。
</li>
<li>
<strong>
HTML
</strong>
ファイル内に直接
<strong>
css
</strong>
を記述して使用します。
</li>
<li>
<strong>
Javascript
</strong>
を利用してスタイルを適用します。
</li>
</ul>
<p>
もちろん他にも方法はありますが、最も一般的に使われる方法を紹介しました。これらの方法を使えば、皆さんは思い通りに
<b>
HTML
</b>
の見た目を整えることができます。
</p>
<p>
例を挙げてみましょう。
</p>
<p>
以下のようなHTMLコードがあります。
</p>
<pre>
<code class="language-html">
<span class="hljs-tag">
&lt;
<span class="hljs-title">
html
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
head
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
head
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
body
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
p
</span>
&gt;
</span>
Hello
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
p
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
body
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
html
</span>
&gt;
</span>
</code>
</pre>
<p>
上記の
<strong>
HTML
</strong>
ソースにある「Hello」という文字を赤く表示したい場合、どうすればよいでしょうか？
</p>
<p>
以下のようなスタイルコードを追加すれば、赤い「Hello」が表示されます。
</p>
<pre>
<code class="language-html">
<span class="hljs-tag">
&lt;
<span class="hljs-title">
html
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
head
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
style
</span>
&gt;
</span>
<span class="css">
<span class="hljs-class">
.red_hello
</span>
<span class="hljs-rules">
{
<span class="hljs-rule">
<span class="hljs-attribute">
color
</span>
:
<span class="hljs-value">
red
</span>
</span>
;
}
</span>
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
style
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
head
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
body
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
p
</span>
<span class="hljs-attribute">
class
</span>
=
<span class="hljs-value">
"red_hello"
</span>
&gt;
</span>
Hello
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
p
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
body
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
html
</span>
&gt;
</span>
</code>
</pre>
<p>
CSSについて詳しく説明していると3分を過ぎてしまいそうです。ですので、くどい説明は抜きにして、ポイントを整理します。
</p>
<blockquote>
<p>
HTMLコードでCSSを使用する
</p>
</blockquote>
<ol>
<li>
classを作成し、HTMLタグに適用する。
</li>
<li>
HTMLタグに直接styleを記述する。
</li>
</ol>
<p>
この2つの方法があります。
</p>
<p>
1つ目は上で使用した方法です。では、直接記述する方法はどうするのでしょうか？ 次の例で紹介します。
</p>
<pre>
<code class="language-html">
... 中略 ...
<span class="hljs-tag">
&lt;
<span class="hljs-title">
p
</span>
<span class="hljs-attribute">
style
</span>
=
<span class="hljs-value">
"color:red;"
</span>
&gt;
</span>
Hello
<span class="hljs-tag">
&lt;/
<span class="hljs-title">
p
</span>
&gt;
</span>
... 中略 ...
</code>
</pre>
<p>
このように記述すれば、クラスを作らずにそのタグに対して直接スタイルを適用できます。
</p>
<p>
では、なぜクラスを使うのでしょうか？ もし特定の単語をすべて赤くしたい場合、直接記述する方法だとタグごとに一つずつスタイルを書き込む必要があります。しかし、最初に紹介した方法を使えば、そのクラス（またはid）を持つすべてのタグに対して一度でスタイルを適用できるという利点があります。
</p>
<p>
また、スタイルを「class」として整理しておけば、後から複数のクラスを組み合わせたタグを作ることも可能です。
</p>
<blockquote>
<p>
CSSの重ね合わせ（継承・組み合わせ）
</p>
<ul>
<li>
btnクラスを作成し、文字サイズを20ptにする。
</li>
<ul>
<li>
.btn { font-size:20pt; }
</li>
</ul>
</ul>
</blockquote>
<blockquote>
<ul>
<li>
btn-dangerクラスを作成し、文字色をredにする。
</li>
<ul>
<li>
.btn-danger { color:red; }
</li>
</ul>
</ul>
</blockquote>
<p>
上記のようにクラスを複数作っておき、タグに必要なクラスを並べて記述すると、スタイルが重ね合わせて適用されます。
なお、同じ属性が重複している場合は、後に適用されたクラスの属性が上書きします。
</p>
<p>
適用例は以下の通りです。
</p>
<pre>
<code class="language-html">
<span class="hljs-tag">
&lt;
<span class="hljs-title">
div
</span>
<span class="hljs-attribute">
class
</span>
=
<span class="hljs-value">
"btn"
</span>
&gt;
</span>
大きなボタン
<span class="hljs-tag">
&lt;
<span class="hljs-title">
div
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
div
</span>
<span class="hljs-attribute">
class
</span>
=
<span class="hljs-value">
"btn-danger"
</span>
&gt;
</span>
赤いボタン
<span class="hljs-tag">
&lt;
<span class="hljs-title">
div
</span>
&gt;
</span>
<span class="hljs-tag">
&lt;
<span class="hljs-title">
div
</span>
<span class="hljs-attribute">
class
</span>
=
<span class="hljs-value">
"btn btn-danger"
</span>
&gt;
</span>
大きくて赤いボタン
<span class="hljs-tag">
&lt;
<span class="hljs-title">
div
</span>
&gt;
</span>
</code>
</pre>
<p>
このように、スタイルを使えば
<strong>
HTML
</strong>
のタグを思い通りに表現できます。
</p>
<h1>
<a>
</a>
まとめ
</h1>
<h4>
<a>
</a>
- スタイルはHTMLの表現方法を定義する。
</h4>
<h4>
<a>
</a>
- スタイルはクラスを通じて重ね合わせて適用できる。ただし、同じ属性の場合は後に適用したクラスが優先される。
</h4>
<h4>
<a>
</a>
- スタイルはタグに直接適用することもできる。
</h4>
<blockquote>
<p>
<strong>
3分予告
</strong>
</p>
</blockquote>
<ul>
<li>
さて、服を着せることはできました。次は、これを動かすにはどうすればいいでしょうか？
</li>
</ul>