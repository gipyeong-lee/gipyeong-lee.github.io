---
layout: post
title: "[03] 자바스크립트Untitled Document.md"
description: "Untitled Document.md 3분 : 제 3 장 Javascript _05 Javascript 란 무엇일까? 자바스크립트는 객체 기반의 스크립트 프로그래밍 언어입니다. 보다 더 자세한 내용은 위키피디아 를 참조해주세요. 우리는 이전 장에서 CSS 에 대해서 알아보았습니다...."
date: 2017-01-05 21:47:43 +0900
section: blog
category: engineering
lang: ko
ref: 2017-01-05-legacy-194-engineering-03-untitled-document-md
tags:
  - "자바스크립트"
  - "javascript"
  - "emca"
  - "use"
  - "하루 3분 웹 공부"
  - "engineering"
---

<meta>
<title>
Untitled Document.md
</title>
<h1>
<a>
</a>
3분 : 제 3 장 Javascript
</h1>
<h3>
<a>
</a>
_05
<code>
Javascript
</code>
란 무엇일까?
</h3>
<p>
자바스크립트는 객체 기반의 스크립트 프로그래밍 언어입니다. 보다 더 자세한 내용은
<a href="https://ko.wikipedia.org/wiki/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8">
위키피디아
</a>
를 참조해주세요.
</p>
<p>
우리는 이전 장에서
<code>
CSS
</code>
에 대해서 알아보았습니다.
<code>
CSS
</code>
를 통해서 우리는
<code>
어떤 속성을 지닌 무언가
</code>
를 만들었습니다. 이제 우리는 이 녀석에게
<code>
어떤 것을 해야하는 것
</code>
인지 알려줄 것입니다.
</p>
<h3>
<a>
</a>
_06 버튼을 클릭했을 때, 알림창이 뜨게 해주자.
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
Javascript
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
위의 녀석들을
<code>
.html
</code>
파일에 모아보면 다음과 같다.
</p>
<pre>
<code>
&lt;!Documen HTML&gt;
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
위의 내용은 해당
<code>
div
</code>
태그를 클릭할 경우,
<code>
'hello world'
</code>
라는 문자열을 보여주는 예제입니다.
</p>
<p>
자바 스크립트를 이용하면 특정 태그의
<code>
id
</code>
,
<code>
class
</code>
등을 통해서 해당 태그에 특정 액션을 부여할 수 있습니다.
<br>
클릭뿐만이 아니라,
<code>
mouseover
</code>
,
<code>
mouseout
</code>
등 마우스 이벤트에 대한 액션 또한 부여할 수 있습니다.
</p>
<h3>
<a>
</a>
_07 버튼의 속성을 바꾸어주자.
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
Javascript
</p>
</blockquote>
<pre>
<code>
&lt;script&gt;
// id_button 의 색상을 빨갛게 바꾸어준다.
document.getElementById("id_button").style.color="red";
&lt;/script&gt;
</code>
</pre>
<h3>
<a>
</a>
_08 버튼의 스타일시트를 비활성화시키자.
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
Javascript
</p>
</blockquote>
<pre>
<code>
&lt;script&gt;
// 도큐먼트에 적용되어 있는 스타일 에서 btn_css 라는 아이디를 갖는 스타일을 비활성화시키자.
document.getElementById("btn_css").disabled = true;
&lt;/script&gt;
</code>
</pre>
<p>
오늘 우리는 간단하게 자바스크립트에 대해서 알아보았습니다. 제가 알려드린 자바스크립트는
<code>
학습
</code>
이 아닌
<code>
분위기
</code>
라고 생각하시면 됩니다.
<br>
다음은 자바스크립트에 대한 간단한 학습 자료입니다.
</p>
<p>
<a href="https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/JavaScript_basics">
MDN Javascript 학습자료
</a>
</p>
<p>
실제로 자바스크립트는
<code>
학습
</code>
을 해야만 제대로 사용할 수 있는 스크립트 언어입니다. 여러분이 자바스크립트를 공부하시다보면
<code>
ECMA스크립트
</code>
라는 말을 듣게 되실 겁니다.
<br>
해당 단어는 자바스크립트의
<code>
표준화
</code>
된 스크립트언어라고 생각하시면 편합니다.
</p>
<blockquote>
<p>
cf.
<br>
추후 자바스크립트를 작성시에 스크립트의 머리에
<code>
use strict
</code>
라는 문구를 볼 경우가 있을 겁니다.
<br>
해당 스크립트는 표준을 따른다는 말이고, 표준을 따른다는 말은 여러 브라우저에서 동일하게 작동하도록 설계된 스크립트라는 뜻으로 해석될 수 있습니다.
</p>
</blockquote>
<h1>
<a>
</a>
정리
</h1>
<h4>
<a>
</a>
- 자바스크립트는 Html 이 움직이게 해준다.
</h4>
<h4>
<a>
</a>
- 자바스크립트는
<code>
document
</code>
에 적용되어 있는 속성값을 변경할 수 있다.
</h4>
<h4>
<a>
</a>
- 자바스크립트는
<code>
document
</code>
의 태그를 자율적으로 변경할 수 있다.
</h4>
<h4>
<a>
</a>
- 오늘 잠시나마 맛본 자바스크립트는 1% 정도 된다. 99% 는 정말 무궁무진하다.
</h4>
<blockquote>
<p>
<strong>
3분 스포
</strong>
</p>
</blockquote>
<ul>
<li>
자바스크립트를 처음부터 다 배워서 사용하려면 너무 힘들 것 같은데, 좀 더 쉽게 사용할 수는 없을까?
</li>
</ul>
