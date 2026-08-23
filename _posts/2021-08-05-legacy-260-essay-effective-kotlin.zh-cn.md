---
layout: post
title: "Effective Kotlin - 关闭正在使用的资源"
description: "使用 use api 关闭已完成使用的资源。在我们使用的资源中，有些资源在使用完成后不会自动停止状态。我们必须通过 close 方法等将这些资源的状态更改为未使用状态。Kotl..."
date: 2021-08-05 09:12:19 +0900
section: blog
category: essay
lang: zh-cn
ref: 2021-08-05-legacy-260-essay-effective-kotlin
tags:
  - "essay"
translation_source_hash: 224281cd2131a66928b2896a739aceb2df24bda36c6a25d2fb22869026f2a98d
---

<h1>
使用 <code>use</code> api 关闭已完成使用的资源
</h1>
<p>
在我们使用的资源中，有些资源在使用完成后不会自动停止状态。我们需要通过 <code>close</code> 方法等将这些资源的状态更改为未使用状态。
</p>
<p>
Kotlin/JVM 中使用的 Java 标准库包含了许多此类资源。以下是典型的不会自动释放的资源：
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
所有这些资源都支持继承自 <code>AutoCloseable</code> 的 <code>Closeable</code> 接口。
</p>
<p>
请查看以下代码片段：
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
上面的代码既复杂又不严谨。因为如果 <code>finally</code> 块中的 <code>reader.close()</code> 抛出异常，则无法处理。如果要处理这种情况，代码可能会变成这样：
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
这种实现方式既冗长又复杂，但由于它是通用做法，因此被提取到了标准库函数 <code>use</code> 中。该功能从 Kotlin 1.2 版本开始支持。
</p>
<p>
以下是参考书中的示例以及补充示例。
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
使用 <code>use</code> 时，如果存在嵌套情况，使用默认的 <code>it</code> 可能会产生问题，因此建议根据作用域明确声明变量名后再使用。
</p>
<h1>
try-with-resources
</h1>

<p>
我们习惯使用的 try-catch 处理资源的方式有时会使代码变得复杂且混乱。为此，Java 提供了 try-with-resources 功能。简而言之，它会在 <code>try</code> 块结束时自动关闭在该 <code>try</code> 中使用的资源。
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
推荐阅读的文章
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