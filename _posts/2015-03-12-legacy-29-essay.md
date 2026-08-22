---
layout: post
title: "웹"
description: "안녕하세요? 향후 웹 프론트단 공부를 하면서 겪는 경험담들. 추가로 해결을 했던 방식들을 쭈욱 써놓도록 하겠습니다. 테스트 환경은 ie8 , chrome, safari 입니다. CSS : Bootstrap ie8 : 그렇게 이쁘게 적용되지 않는다 > 직접 css 를 만들어서 적용시..."
date: 2015-03-12 02:54:19 +0900
section: blog
category: essay
lang: ko
ref: 2015-03-12-legacy-29-essay
tags:
  - "Web"
  - "Location"
  - "웹"
  - "merge"
  - "jquery"
  - "addEventListener"
---

<p>
<span>
<span>
<span>
안녕하세요?
</span>
</span>
</span>
</p>
<p>
<span>
<span>
<span>
향후 웹 프론트단 공부를 하면서 겪는 경험담들. 추가로 해결을 했던 방식들을 쭈욱 써놓도록 하겠습니다.
</span>
<br>
</span>
</span>
</p>
<p>
<span>
<span>
<span>
테스트 환경은 ie8 , chrome, safari 입니다.
</span>
</span>
</span>
</p>
<p>
<span>
<b>
<span>
<br>
</span>
</b>
</span>
</p>
<p>
<span>
<b>
<span>
CSS : Bootstrap
</span>
</b>
</span>
</p>
<p>
<span>
<b>
<br>
</b>
</span>
</p>
<p>
<span>
ie8 : 그렇게 이쁘게 적용되지 않는다 &gt; 직접 css 를 만들어서 적용시켰습니다.
</span>
<br>
</p>
<p>
<span>
chrome : Good
</span>
</p>
<p>
<span>
Safari : Good
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
<b>
<span>
JS : addEventListener
</span>
</b>
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
ie8 : 작동 하지 않는다. 아래와 같이 처리해주었다. ie8 에서는 attachEvent 를 통해 처리
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<div>
<p>
if(document.getElementById("btn_login").addEventListener)
</p>
<p>
document.getElementById("btn_login").addEventListener("click",function(){
</p>
<p>

window.location.href = "main.html";
</p>

<p>
});
</p>
<p>
<span>
else
</span>
</p>
<p>
document.getElementById("btn_login").attachEvent("onclick",function(){
</p>
<p>

window.location.href = "main.html";
</p>

<p>
});
</p>
</div>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
chrome : Good
</span>
</p>
<p>
<span>
Safari : Good
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<font>
<span>
<b>
JQUERY : $.merge(arr1,arr2)
</b>
</span>
</font>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<font>
<span>
JQUERY 의 merge 를 통해 배열을 합칠경우 arr1, arr2 의 순서에 따라 데이터가 달라지는 이상한 경험을 하였다.
</span>
</font>
</p>
<p>
<font>
<span>
주의해야하겠다... ㅡ,.ㅡ... ;;
</span>
</font>
</p>
<p>
<font>
<span>
이것때문에 데이터 맵핑 하루를 잡아먹음.. 하아....
</span>
</font>
</p>
<p>
<font>
<span>
살려주세요.
</span>
</font>
</p>
<div>
<span>
<br>
</span>
</div>

<p>
<b>
<span>
Javascript 을 통한 페이지 이동관련
</span>
</b>
</p>

<p>
<span>
<b>
parent.location.href = "url"
</b>
</span>
</p>
<p>
<span>
현 프레임의 바로 위의 경로를 해당 url 로 설정
</span>

<span>
( 페이지 이동됨 )
</span>
</p>

<p>
<span>
<b>
top.location.href = "url"
</b>
</span>
</p>
<p>
<span>
가장 바깥에 위치한 document의 location 경로를 해당 url 로 설정
</span>

<span>
( 페이지 이동됨 )
</span>
</p>

<p>
<span>
<b>
opener.location.href = "url"
</b>
</span>
</p>
<p>
<span>
현 프레임을 열어 놓은 document 의 location 경로를 해당 url 로 설정 ( 페이지 이동됨 )
</span>
</p>
<p>
<span>
<br>
</span>
</p>


<p>
<span>
<b>
<span>
JQUERY 페이지 이동 후 특정 css, 혹은 javascript 를 onload 시키고 싶을 때
</span>
</b>
</span>
</p>


<p>
<pre class="brush: html; toolbar: false; gutter:false;">
&lt;div data-role = "page"&gt;
    &lt;style&gt; ... &lt;/style&gt; or &lt;script&gt; ... &lt;/script&gt;
&lt;/div&gt;
</pre>
</p>


<p>
<span>
위의 예처럼 해당 div 의 속에다가 커스텀화시킨 스크립트나 스타일 코드를 삽입해준다.
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
<br>
</span>
</p>
