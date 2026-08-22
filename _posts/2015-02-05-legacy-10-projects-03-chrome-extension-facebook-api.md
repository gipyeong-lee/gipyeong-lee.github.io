---
layout: post
title: "[단기] 03. Chrome Extension 과 Facebook API"
description: "단기 프로젝트 진행이 벌써 10일이 지나가고 있습니다. 대강의 프로젝트 와꾸는 나왔습니다. 그러나 Chrome Extension 에서 Facebook API 를 연동하지 못하게 되는 사태를 맞이하였습니다. 아.. 제발 해결되었으면 합니다... 살려주세요... 일단은 해결을 하였습니..."
date: 2015-02-05 02:33:56 +0900
section: blog
category: projects
lang: ko
ref: 2015-02-05-legacy-10-projects-03-chrome-extension-facebook-api
tags:
  - "TJSSM"
  - "projects"
---

<p>
단기 프로젝트 진행이 벌써 10일이 지나가고 있습니다.
</p>
<p>
대강의 프로젝트 와꾸는 나왔습니다.
</p>
<p>
그러나 Chrome Extension 에서 Facebook API 를 연동하지 못하게 되는 사태를 맞이하였습니다.
</p>
<p>
아.. 제발 해결되었으면 합니다... 살려주세요...
</p>

<p>
일단은 해결을 하였습니다.
</p>
<p>
페이스북 로그인은 따로 하지 않았습니다. ( 구글링을 한결과 ) facebook 쿼리를 분석해서 누군가 올려놨더라구요.
</p>
<p>
해당 부분만 가져와서 처리하였습니다.
</p>

<p>
다음은 처리결과입니다.
</p>







<p>
추가로 기존 회원님이신 남두현 회원님께 기사내 썸네일 이미지 추출에 대해서 정보를 얻게 됐습니다.
</p>
<p>
내일은 기사 링크를 이용해 기사의 썸네일을 추출하는 부분을 진행할 예정입니다.
</p>

<p>
다음과 같은 순서로 할 예정입니다.
</p>

<p>
1. HTML 파싱
</p>
<p>
2. 메타태그 분석을 통한 캐릭터셋 취득 ( UTF-8,EUC-KR ... etc )
</p>
<p>
3. 해당 캐릭터셋으로 재 파싱
</p>
<p>
4. 정규식을 통한 &lt;script&gt;,&lt;style&gt; 제거
</p>
<p>
5. &lt;body&gt;내에서 정규식을 통한 &lt;h2&gt;,&lt;span&gt;,&lt;p&gt; 제거
</p>
<p>
6. 깨끗해진 body 내에서 , 텍스트 묶음들의 길이와 텍스트 묶음 저장
</p>
<p>
7. 정렬
</p>
<p>
8. 정렬된 텍스트에서 갑자기 적어지는 부분부터 쭉 삭제
</p>
<p>
9. 텍스트가 많은 녀석들 주변의 img 태그 찾아서 href 값 가져오기
</p>

<p>
이상 이론적인거고...
</p>

<p>
내일 꼭 해보겠습니다...
</p>

<p>
P.s Chrome Extension 에 대한 이해도가 많이 떨어진다는 점을 알았습니다. 기존 facebook api 를 그냥 extension 에 붙이려고 시도하는 경우 CSP 에 막혀서.. 다음과 같은 문구를 2시간동안 보며 분석했던것 같습니다.
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
Content Security Policy directive: "script-src 'self' chrome-extension-resource:".
</span>
</p>

<p>
결과적으로는 해당부분은 그냥은 못 붙이는걸로 확인하였습니다...
</p>
<p>
아직도 페이스북 로그인은 잘 모르겠습니다. 혹시 누군가 알게 되신다면 ... 댓글 부탁드립니다. (_ _)
</p>
<p>
감사드립니다.
</p>

<p>
어엇...
</p>
<span class="txt_fold">
더보기
</span>
<div class="moreless_content">
<p>
아침에 일어나서 흐리멍텅한 정신으로 구글 도큐멘트를 다시 보았습니다.
</p>

<p>
<span>
<a href="https://developer.chrome.com/apps/contentSecurityPolicy#H3-1" target="_blank" class="tx-link">
How to comply with CSP
</a>
</span>
</p>
<p>
( Content Security Policy 를 준수하는 방법 )
</p>

<p>
먼저 준수하기 위해서는 구글 확장프로그램의 CSP 가 무엇인지를 알아야했습니다.
</p>
<p>
바로 밑에 쓰여있던걸 못봤었습니다.
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
What is the CSP for Chrome Apps?
</span>
</p>
<div>
<br>
</div>
<p>
The content security policy for Chrome Apps restricts you from doing the following:
</p>
<ul>
<li>
You can’t use inline scripting in your Chrome App pages. The restriction bans both &lt;script&gt; blocks and event handlers (&lt;button onclick="..."&gt;).
</li>
<li>
You can’t reference any external resources in any of your app files (except for video and audio resources). You can’t embed external resources in an iframe.
</li>
<li>
You can’t use string-to-JavaScript methods like
<code>
eval()
</code>
and
<code>
new Function()
</code>
.
</li>
</ul>

<p>
위 내용을 정리해보면 이렇습니다.
</p>

<p>
_크롬앱의 컨텐츠 보안 정책.
</p>
<p>
1. inline 스크립팅을 쓸수 없습니다. html 페이지에서.
</p>
<p>
2. 어떤 외부 리소스도 참조할 수 없습니다. 또한, 아이프레임 안에 외부 리소스를 삽입할수도 없습니다.
</p>
<p>
3. 스트링을 함수화 시키는 eval() 과 같은 함수 사용 불가.
</p>

<p>
아.. 결국 내부의 데이터만 사용하도록 강요받고 있습니다.  xss 취약점을 원천봉쇠하고자 하는 노력이 보입니다.
</p>
<p>
웹 해킹에 대한 정보가 많이 나오는군요. XSS 검색시...
</p>

<p>
그리고 아래를 보면...
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
Your Chrome App can only refer to scripts and objects within your app, with the exception of media files (apps can refer to video and audio outside the package). Chrome extensions will let you relax the default Content Security Policy; Chrome Apps won’t.
</span>
</p>

<p>
다행히..
<span>
크롬 확장프로그램은 완화된다고 하지만, Chrome App 은 그럴일은없을거라고 얘기를 해주네요.
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
All JavaScript and all resources should be local (everything gets packaged in your Chrome App).
</span>
</p>

<p>
모든 자바스크립트나 모든 리소스들은 로컬 데이터이기를 권장하는군요.
</p>

<p>
그렇다면 정말 정말 외부 소스를 사용할 수 있는 방법은 없는가...
</p>
<p>
아래를 보면 또 있습니다..
</p>


<h3 class="has-permalink">
Use templating libraries
</h3>
<p>
Use a library that offers precompiled templates and you’re all set. You can still use a library that doesn’t offer precompilation, but it will require some work on your part and there are restrictions.
</p>
<p>
You will need to use sandboxing to isolate any content that you want to do ‘eval’ things to. Sandboxing lifts CSP on the content that you specify. If you want to use the very powerful Chrome APIs in your Chrome App, your sandboxed content can't directly interact with these APIs (see
<a href="https://developer.chrome.com/apps/app_external#sandboxing">
Sandbox local content
</a>
).
</p>
<h3 class="has-permalink">
Access remote resources
</h3>
<p>
You can fetch remote resources via
<code>
XMLHttpRequest
</code>
and serve them via
<code>
blob:
</code>
,
<code>
data:
</code>
, or
<code>
filesystem:
</code>
URLs (see
<a href="https://developer.chrome.com/apps/app_external#external">
Referencing external resources
</a>
).
</p>
<p>
Video and audio can be loaded from remote services because they have good fallback behavior when offline or under spotty connectivity.
</p>
<h3 class="has-permalink">
Embed web content
</h3>
<p>
Instead of using an iframe, you can call out to an external URL using a webview tag (see
<a href="https://developer.chrome.com/apps/app_external#webview">
Embed external web pages
</a>
).
</p>

<p>
세가지나 있군요.
</p>

<p>
1. Sandbox와 Chrome API 를 이용한 메인 페이지와 샌드박싱페이지의 교류
</p>
<p>
2. XMLHttpRequest 에서 blob 등을 통한 외부 리소스 참조. ( 스크립트는 안될것 같습니다)
</p>
<p>
3. iframe 을 사용해서 처리한다.
</p>

<p>
이론상으로는 3개를 이용하면 외부 리소스를 사용가능하다고 적혀있습니다.
</p>
<p>
그러나, 외부 스크립트를 쓸 수 있는 부분에 대해서는 언급이 안되어 있어서 잘모르겠습니다.
</p>
<p>
추후에 기회가 되면 세가지 방식을 이용하여 스크립트를 외부로부터 가져 올 수 이는지 시도해보도록 하겠습니다.
</p>

<p>
지금은 다음 골이 있어서 Pass...
</p>

</div>
