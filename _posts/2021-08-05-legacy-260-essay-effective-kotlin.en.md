---
layout: post
title: "Effective Kotlin - Closing Used Resources"
description: "Use the 'use' API to close resources once you are finished with them. Among the resources we use, there are those that do not automatically switch their state to stopped after use. We must change their state to 'unused' using methods like 'close'. Kotl..."
date: 2021-08-05 09:12:19 +0900
section: blog
category: essay
lang: en
ref: 2021-08-05-legacy-260-essay-effective-kotlin
tags:
  - "essay"
translation_source_hash: 224281cd2131a66928b2896a739aceb2df24bda36c6a25d2fb22869026f2a98d
---

<h1>
Use the <code>use</code> API to close resources once finished
</h1>
<p>
Among the resources we use, there are some that do not automatically switch their state to stopped after usage is complete. We must change their state to an unused status using methods like <code>close</code>.
</p>
<p>
Standard Java libraries used in Kotlin/JVM contain many such resources. Notably, the following resources do not automatically return themselves:
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
All corresponding resources support the <code>Closeable</code> interface, which inherits from <code>AutoCloseable</code>.
</p>
<p>
Consider the following syntax:
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
The syntax above is complex and incorrect because it cannot handle cases where <code>reader.close()</code> throws an error within the <code>finally</code> block. If we were to handle this, I think it could be changed as follows:
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
While this implementation is long and complex, it is quite common, so it has been extracted into the standard library function <code>use</code>. This has been supported since Kotlin version <code>1.2</code>.
</p>
<p>
I have provided an example to reference, along with the example found in the book.
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
When using <code>use</code>, nesting it might cause issues if using <code>it</code>, so it is recommended to declare and use the variable according to its scope.
</p>
<h1>
try with resources
</h1>

<p>
Handling resources with a familiar <code>try-catch</code> can sometimes make code complex and messy. For this purpose, the <code>try-with-resources</code> feature is supported. In short, it automatically closes the resources used in the <code>try</code> block when the block finishes.
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
Recommended Reading
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

## References