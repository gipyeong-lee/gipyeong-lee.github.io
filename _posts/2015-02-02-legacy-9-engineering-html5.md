---
layout: post
title: "HTML5 새로운 내용들"
description: "안녕하세요? HTML5 를 공부하며 알게된 내용들을 정리하는 공간입니다. 특정한 기능에 대해 깊이 있는 포스팅을 하는 곳이 아님을 미리 알려드립니다. DTD (Document Type Definition) Document Type Definition 의 약자입니다. DTD는 어떤..."
date: 2015-02-02 04:23:29 +0900
section: blog
category: engineering
lang: ko
ref: 2015-02-02-legacy-9-engineering-html5
tags:
  - "Web"
  - "engineering"
---

<p>
<span>
안녕하세요?
</span>
</p>
<p>
<span>
HTML5 를 공부하며 알게된 내용들을 정리하는 공간입니다. 특정한 기능에 대해 깊이 있는 포스팅을 하는 곳이 아님을 미리 알려드립니다.
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
Document Type Definition 의 약자입니다. DTD는 어떤 태그, 속성, 값이 특정한 HTML문서에서 유효한지를 설명하는 텍스트 파일입니다. 각 HTML 버전에는 그에 맞는 DTD가 있다고 합니다. 대게는 이를 HTML 문서의 첫줄에 doctype 선언을 통해서 하는데요, 어떤 버전의 HTML 혹은 XHTML이 사용되었는지를 브라우저에 알립니다.
</span>
<span>
이런 doctype 선언을 빼먹을시 대다수의 브라우저는 쿽스 모드 (Quirks Mode)라는 상태에 빠진다고 합니다.
</span>
</p>
<p>
<span>
doctype 선언을 하지 않은 페이지를 만날시 "어라, 이 페이지는 아주 오랜 옛날에 작성된 페이지이구나" 라고 생각해 버린다고 합니다. "그럼 아무렇게나 표시해야지" 라는 결론을 내리게 되고요.
</span>
</p>
<p>
<span>
만일 자신이 만든 웹페이지가 브라우저에서 의도한대로 보이지 않는다면 doctype 선언을 확인해보는게 좋다고 합니다.
</span>
</p>
<p>
<span>
아래는 각 버전별 doctype 선언입니다.
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
IE9 이하 버전에 대처하는 우리들의 자세
</span>
</b>
</p>

<p>
<span>
1. IE8 이 HTML5를 이해하도록 만들고 싶다면.
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
&lt;/head&gt; 태그 앞에 다음과 같은 코드를 삽입하면 됩니다.
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
조건 주석을 이용하여 IE9보다 오래된 IE만 , 즉 IE 6,7,8 만이 이 코드를 이해하며 코드가 적용된다고 합니다. 신기하게 테스트를 해보니, 크롬에서는 해당 스크립트가 안들어가더군요. IE 만 판별을 하나봅니다.
</p>

<p>
<span>
2. IE 8 의 호환성 보기 및 호환성 보기 목록을 회피하는법
</span>
</p>
<p>
아래 코드를 &lt;head&gt; 한에 넣어주세용
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
HTML 코드에 외부 스타일 시트 연결하기
</span>
</b>
</p>

<p>
외부 스타일 시트를 웹 페이지에 연결하는 방법은 &lt;link&gt; 태그를 사용하는 것이다.
</p>
<p>
다음은 각 버전별 사용방식이다.
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
