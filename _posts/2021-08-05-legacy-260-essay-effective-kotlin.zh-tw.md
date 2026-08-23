---
layout: post
title: "Effective Kotlin - 關閉正在使用的資源"
description: "使用 use API 來關閉已完成使用的資源。在我們使用的資源中，有些資源在使用完成後不會自動停止使用狀態。因此，我們必須透過 close 等方法將這些資源的狀態更改為未使用。Kotl..."
date: 2021-08-05 09:12:19 +0900
section: blog
category: essay
lang: zh-tw
ref: 2021-08-05-legacy-260-essay-effective-kotlin
tags:
  - "essay"
translation_source_hash: 224281cd2131a66928b2896a739aceb2df24bda36c6a25d2fb22869026f2a98d
---

<h1>
使用 
<code>
use
</code>
 API 來關閉已完成使用的資源。
</h1>
<p>
在我們使用的資源中，有些資源在使用完成後不會自動停止使用狀態。因此，我們必須透過 
<code>
close
</code>
 等方法將這些資源的狀態更改為未使用。
</p>
<p>
Kotlin/JVM 所使用的 Java 標準函式庫中包含了許多這類資源。以下是代表性的資源，它們不會自動歸還：
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
所有對應的資源都支援繼承自 
<code>
AutoCloseable
</code>
 的 
<code>
Closeable
</code>
 介面。
</p>
<p>
請檢查以下語法。
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
上述語法既複雜又不正確。因為如果在 
<code>
finally
</code>
 區塊中 
<code>
reader.close()
</code>
 發生錯誤，則無法處理。如果考慮到這點，我認為可以改成如下：
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
這樣的實作雖然冗長且複雜，但因為很常見，所以標準函式庫將其提取為 
<code>
use
</code>
 函式。Kotlin 1.2 版本以上支援此功能。
</p>
<p>
以下提供除了書中範例之外，可供參考的範例。
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
使用 
<code>
use
</code>
 時，如果進行巢狀使用，直接使用 
<code>
it
</code>
 可能會產生問題，因此建議根據作用域（Scope）進行宣告使用。
</p>
<h1>
try with resources
</h1>

<p>
我們習慣用 try-catch 來處理資源，但程式碼有時會變得複雜且雜亂。為了解決這個問題，提供了 try-with-resources 功能。簡單來說，它會在 
<code>
try
</code>
 區塊結束時，自動對在 
<code>
try
</code>
 中使用的資源執行 
<code>
close
</code>
 處理。
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
值得一讀的文章
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