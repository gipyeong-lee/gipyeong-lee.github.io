---
layout: post
title: "Effective Kotlin - 使用済みのリソースを閉じる"
description: "use api を使用して、使用が完了した resource を閉じましょう。私たちが使用するリソースの中には、使用完了後に使用状態を停止に変えないものがあります。そして、close メソッドなどを通じて該当リソースの状態を使用しない状態に変える必要があります。Kotl..."
date: 2021-08-05 09:12:19 +0900
section: blog
category: essay
lang: ja
ref: 2021-08-05-legacy-260-essay-effective-kotlin
tags:
  - "essay"
translation_source_hash: 224281cd2131a66928b2896a739aceb2df24bda36c6a25d2fb22869026f2a98d
---

<h1>
<code>
use
</code>
API を使用して、使用が完了した resource を閉じましょう。
</h1>
<p>
私たちが使用するリソースの中には、使用完了後に使用状態を停止に変えないものがあります。そして、<code>close</code> メソッドなどを通じて、該当リソースの状態を使用しない状態に変える必要があります。
</p>
<p>
Kotlin/JVM で使用する Java の標準ライブラリには、このようなリソースが多く含まれています。代表的に、以下のリソースの場合、自動的にリソースの返却が行われません。
</p>

<pre class="css">
<code>
- InputStream and OutputStream
- Java.sql.Connection
- Java.io.Reader ( FileReader, BufferedReader, CSSParser )
- Java.new.Socket and java.util.Scanner
</code>
</pre>

<p>
該当するすべてのリソースは、<code>AutoCloseable</code> を継承する <code>Closeable</code> インターフェースをサポートしています。
</p>
<p>
次の構文を確認してみます。
</p>

<pre class="kotlin">
<code>
fun countCharactersInFile(path:String):Int{
    val reader = BufferedReader(FileReader(path))
    try {
        return reader.lineSequence().sumBy { it.length }
    }
    finally {
       reader.close()
    }
}
</code>
</pre>

<p>
上記の構文は複雑で、正しくありません。なぜなら、<code>finally</code> ブロックで reader.close() がエラーを発生させた場合、処理できないからです。これを処理するならば、次のように変更できると考えます。
</p>

<pre class="kotlin">
<code>
fun countCharactersInFile(path:String):Int{
    val reader = BufferedReader(FileReader(path))
    try {
        return reader.lineSequence().sumBy { it.length }
    }
    finally {
       try { reader.close() } catch (e: Exception) {}
    }
}
</code>
</pre>

<p>
このような実装は長く複雑ですが一般的であるため、標準ライブラリ関数から <code>use</code> として抽出しました。これは Kotlin バージョン <code>1.2</code> 以上からサポートされます。
</p>
<p>
本にある例と一緒に参考にできる例を載せます。
</p>

<pre class="rust">
<code>
try {
    Socket("open", 80).use { socket -&gt;
        socket.getInputStream().use { inputStream -&gt;
            InputStreamReader(inputStream).use { reader -&gt;
                println(reader.readLines())
            }
        }
    }
} catch (e: Exception) {
        // ...
}
</code>
</pre>

<p>
<code>use</code> 使用時にネストして使用する場合、<code>it</code> を使用すると問題が発生する可能性があるため、スコープに合わせて宣言して使用することを推奨します。
</p>
<h1>
try with resources
</h1>

<p>
私たちが慣れ親しんでいる try catch でリソースをハンドリングすることは、コードが時として複雑になり、汚くなります。そのためにサポートされている機能が try with resources です。短く説明すると、try で使用したリソースを <code>try</code> ブロックが終了する時に自動的に Close 処理してくれます。
</p>

<pre class="reasonml">
<code>
public static String getHtml(String url) throws IOException {

    val targetUrl = URL(url);

    try (val inputSR = new InputStreamReader(targetUrl.openStream());val bufferReader =  BufferedReader(inputSR)){
        val html = StringBuffer();
        var tmp;

        while ((tmp = reader.readLine()) != null) {
            html.append(tmp);
        }
        return html.toString();
    }
}
</code>
</pre>
<h1>
</h1>
<h1>
読んでおくと良いブログ記事
</h1>
<ul>
<li>
<a href="https://multifrontgarden.tistory.com/192">
https://multifrontgarden.tistory.com/192
</a>
</li>
<li>
<a href="https://ryan-han.com/post/java/try_with_resources/">
https://ryan-han.com/post/java/try_with_resources/
</a>
</li>
</ul>