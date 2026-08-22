---
layout: post
title: "[02] 스타일 시트 CSSUntitled Document.md"
description: "Untitled Document.md 3분 : 제 2 장 CSS _04 CSS 란 무엇일까? 스타일시트는 HTML 로 작성한 문서를 실제 표시되는 방식을 기술한 언어입니다. 만일, 여러분이 HTML 을 이용하여 강아지를 그렸다고 생각해보세요. 그 강아지의 꼬리가 얼마나 긴지, 그..."
date: 2016-08-28 01:14:05 +0900
section: blog
category: engineering
lang: ko
ref: 2016-08-28-legacy-192-engineering-02-cssuntitled-document-md
tags:
  - "CSS"
  - "Style"
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
3분 : 제 2 장 CSS
</h1>
<h3>
<a>
</a>
_04 CSS 란 무엇일까?
</h3>
<p>
스타일시트는
<strong>
HTML
</strong>
로 작성한 문서를 실제 표시되는 방식을 기술한 언어입니다. 만일, 여러분이 HTML 을 이용하여 강아지를 그렸다고 생각해보세요.
</p>
<p>
그 강아지의 꼬리가 얼마나 긴지, 그 강아지의 머리가 얼마나 작은지, 그 강아지의 몸집이 어느정도인지. 이런 것들을 기술할 수 있게 만든 언어가 바로
<strong>
CSS
</strong>
입니다.
</p>
<p>
다시말해, 여러분이 뼈다귀를 그려놓고. 그 뼈다귀 위에 옷일 입혔습니다. 여기까지가
<strong>
HTML
</strong>
이라면,  그 옷의 크기가 어느정도인지, 무슨 색인지 등과 같은 속성을 넣어주는 것입니다.
</p>
<p>
자, 정리를 해드리겠습니다.
<strong>
HTML
</strong>
,
<strong>
CSS
</strong>
두가지가 하는 역할은 아래와 같습니다.
</p>
<blockquote>
<p>
HTML
</p>
</blockquote>
<ul>
<li>
뼈다귀에 옷을 입힌다.
</li>
</ul>
<blockquote>
<p>
CSS
</p>
</blockquote>
<ul>
<li>
옷이 어떻게 생겼는지 알려준다.
</li>
</ul>
<p>
그럼 이제, CSS 가 무엇을 하는지 알았습니다. CSS의 기초를 배워봅시다.
</p>
<blockquote>
<p>
CSS 사용방법
</p>
</blockquote>
<ul>
<li>
<strong>
css
</strong>
파일을 작성 후,
<strong>
HTML
</strong>
파일에서 참조하여 사용합니다.
</li>
<li>
<strong>
HTML
</strong>
파일 내에 직접
<strong>
css
</strong>
를 넣어서 사용합니다.
</li>
<li>
<strong>
Javascript
</strong>
를 이용하여 스타일을 적용합니다.
</li>
</ul>
<p>
물론, 또 다른 방법이 있을 수 있습니다. 그러나, 가장 많이 사용하는 방법들을 알려드립니다. 위의 방법들로 여러분은 원하는 데로
<b>
HTML
</b>
이 보이도록 하실 수 있습니다.
</p>
<p>
가령, 예를 들어보겠습니다.
</p>
<p>
아래의 HTML 코드가 있습니다.
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
위의
<strong>
HTML
</strong>
소스에서 ‘Hello’ 라는 글자를 붉게 나오게 하고 싶다. 그렇다면 어떻게 표현하면 될까요?
</p>
<p>
다음과 같은 스타일 코드를 넣어주신다면, 여러분은 붉은 'Hello’를 보실 수 있습니다.
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
CSS 에 대해서 설명해드리면 3분을 넘어갈 것 같습니다. 그러므로, 구구절절 설명대신 여러분을 위해서 정리해드리겠습니다.
</p>
<blockquote>
<p>
HTML 코드에서 CSS 사용하기
</p>
</blockquote>
<ol>
<li>
class 를 만들어서 HTML 태그에 적용을 시켜준다.
</li>
<li>
HTML 태그에 직접적으로 style 을 넣어준다.
</li>
</ol>
<p>
두가지 방법이 있습니다.
</p>
<p>
첫번째는 제가 위에서 사용한 방법입니다. 그렇다면 직접 넣는 방법은 무엇일까요? 다음 예시를 통해서 style 을 직접 넣는 방법을 알려드리도록 하겠습니다.
</p>
<pre>
<code class="language-html">
... 중략 ...
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
... 중략 ...
</code>
</pre>
<p>
이렇게 사용하시면 여러분들은 클래스 없이 해당 태그에 직접적인 스타일을 적용하실 수 있습니다.
</p>
<p>
그렇다면, 왜 클래스를 사용할까요? 만일, 여러분들이 어떤 단어는 빨갛게 하고 싶으실때, 직접적으로 작성을 하시면 매번 일일이 Tag 안에 스타일을 넣으셔야 합니다. 그라나, 제가 처음 사용한 방법을 이용할 경우 여러분들은 한번의 스타일을 ‘해당 클래스, 혹은 id 를 갖고있는’ 태그에 적용시킬 수 있는 장점이있습니다.
</p>
<p>
또한, 스타일을 ‘class’ 로 정리해두면, 추후에 여러 클래스를 조합한 태그도 만들 수도 있습니다.
</p>
<blockquote>
<p>
CSS 중첩
</p>
<ul>
<li>
btn 클래스를 만들고 글씨크기가 20pt 이다.
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
btn-danger 클래스를 만들고 글씨 색상이 red 이다.
</li>
<ul>
<li>
.btn-danger { color:red; }
</li>
</ul>
</ul>
</blockquote>
<p>
만일 위처럼 클래스를 여러개 만들어두고 사용하고 싶은 클래스를 태그에 넣어주시면, 중첩되어 적용됩니다.
만일, 동일한 속성이 클래스에 있다면. 나중에 적용한 클래스의 속성이 덮어씌워집니다.
</p>
<p>
아래는 적용 예시입니다.
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
큰 버튼
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
빨간 버튼
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
크고 빨간 버튼
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
이처럼 스타일을 이용하여 여러분은
<strong>
HTML
</strong>
의 태그들을 원하는 대로 표현할 수 있습니다.
</p>
<h1>
<a>
</a>
정리
</h1>
<h4>
<a>
</a>
- 스타일은 HTML 을 표현하는 방법을 정의해준다.
</h4>
<h4>
<a>
</a>
- 스타일은 클래스를 통해 중첩 적용된다. 단, 동일 속성의 경우 마지막 클래스의 속성이 적용된다.
</h4>
<h4>
<a>
</a>
- 스타일은 직접 태그에 적용할 수도 있다.
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
자 이제, 색깔 옷도 입혔다. 이제 이녀석을 움직이게 하려면 어떻게 하면 좋을까?
</li>
</ul>
