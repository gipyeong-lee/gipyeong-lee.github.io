---
layout: post
title: "Effective Kotlin - 사용중인 리소스 닫기"
description: "use api 를 사용해서 사용이 완료된 resource 를 닫자. 우리가 사용하는 자원들 중에서는 사용완료 후 사용상태를 중지로 바꾸지 않는 자원들이 있습니다. 그리고 우리는 close method 등을 통해서 해당 자원의 상태를 사용하지 않는 상태로 바꾸어 줘야합니다. Kotl..."
date: 2021-08-05 09:12:19 +0900
section: blog
category: essay
lang: ko
ref: 2021-08-05-legacy-260-essay-effective-kotlin
tags:
  - "essay"
---

<h1>
<code>
use
</code>
api 를 사용해서 사용이 완료된 resource 를 닫자.
</h1>
<p>
우리가 사용하는 자원들 중에서는 사용완료 후 사용상태를 중지로 바꾸지 않는 자원들이 있습니다. 그리고 우리는
<code>
close
</code>
method 등을 통해서 해당 자원의 상태를 사용하지 않는 상태로 바꾸어 줘야합니다.
</p>
<p>
Kotlin/JVM 에서 사용하는 자바의 표준 라이브러리는 이런 자원들을 많이 포함하고 있습니다. 대표적으로 다음 리소스들의 경우 자동으로 자원의 반환이 이루어지지 않습니다.
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
해당하는 모든 자원들은
<code>
AutoCloseable
</code>
을 상속받는
<code>
Closeable
</code>
인터페이스를 지원합니다.
</p>
<p>
다음 구문을 확인해봅니다.
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
위의 구문은 복잡하고, 올바르지 않습니다. 왜냐하면,
<code>
finally
</code>
블록에서 reader.close() 가 에러를 발생시킬 경우 처리할 수 없기 때문입니다. 이를 처리한다면, 다음처럼 바뀔 수 있다고 생각합니다.
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
이런 구현은 길고 복잡하지만 일반적이기 떄문에 표준라이브러리 함수에서
<code>
use
</code>
로 추출했습니다. 이는 코틀린 버전
<code>
1.2
</code>
이상부터 지원됩니다.
</p>
<p>
책에 있는 예제와 함께 참고할 예제를 실어 봅니다.
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
<code>
use
</code>
사용시 중첩해서 사용하게될 경우
<code>
it
</code>
로 하게되면 문제가 있을 수 있으니, 스콥에 맞추어 선언해 사용하기를 권장합니다.
</p>
<h1>
try with resources
</h1>

<p>
우리가 익숙한 try catch 로 자원을 핸들링하는 것은 코드가 때로는 복잡해지고 지저분해집니다. 이를 위해 지원되는 기능이 try with resources 입니다. 짧게 설명하면, try 에 사용한 자원을
<code>
try
</code>
블록이 종료될때 자동으로 Close 처리해줍니다.
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
읽어보면 좋은 포스팅
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
