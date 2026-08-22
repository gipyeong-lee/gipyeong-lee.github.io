---
layout: post
title: "[Bootstrap,JQuery] Table을 이쁘게 정리하기"
description: "안녕하세요? 이번시간에는 GMS 툴 개발에 따른 Frontend에서 유용한 플러그인을 소개해드리고자 합니다. 다음의 URL 을 참조하시면 확인해보실 수 있습니다. https://datatables.net/examples/styling/bootstrap.html 아래는 적용(전) 과..."
date: 2016-02-24 18:43:22 +0900
section: blog
category: engineering
lang: ko
ref: 2016-02-24-legacy-166-engineering-bootstrap-jquery-table
tags:
  - "table"
  - "jquery"
  - "bootstrap"
  - "pagination"
  - "DataTable"
  - "Web"
---

<p>
안녕하세요?
</p>

<p>
이번시간에는 GMS 툴 개발에 따른 Frontend에서 유용한 플러그인을 소개해드리고자 합니다.
</p>
<p>
다음의 URL 을 참조하시면 확인해보실 수 있습니다.
</p>

<p>
<a href="https://datatables.net/examples/styling/bootstrap.html" target="_blank" class="tx-link">
https://datatables.net/examples/styling/bootstrap.html
</a>
<br>
</p>


<p>
아래는 적용(전) 과 (후) 의 스크린샷 입니다.
</p>


<p>
<figure class="imageblock alignCenter" width="681" height="416">

<figcaption>
적용전
</figcaption>
</figure>
</p>

<p>
<b>
&lt;적용전&gt;
</b>
</p>




<p>
위의 사진은 현재 테스트 중인 약 2천개정도의 데이터를 플러그인 없이 보여줄때 모습입니다.
</p>
<p>
( 향후 데이터가 무지무지하게 쌓이면.. 엄청나겠죠 ?)
</p>



<p>
다음은 플러그인을 적용한 모습입니다.
</p>







<p>
10, 20,50, 100 개 들이로 정리해서 볼 수 있으며, Search 를 통해서 테이블 Row 를 검색할 수 있고, Pagination 기능을 제공해줍니다.
</p>
<p>
"손수 구현해보고 싶다" 라는 마음이거나 한번도 구현해본적이 없다면 ( 페이지네이션, 엔트리, 검색 ) 직접 하시길 추천해드리고.
</p>

<p>
구현을 해보았고, 노가다로 느껴질 경우 해당 플러그인으로 편하게 작업을 해보는게 좋다고 생각됩니다.
</p>


<p>
사용방법은 아래 간략하게 정리하도록 하겠습니다.
</p>
<p>
jQuery 1.12 버전 이상으로 사용해주시면 될것 같습니다. ( 그 이하 버전을 테스트 해보지는 않았습니다. 예제 사이트에서 사용한 버전이 1.12 이므로 얘기드렸습니다. 필자는 2버전때 jquery 를 사용하였습니다. )
</p>

<p>
<b>
1. 파일 다운로드 및 &lt;script src=""&gt;&lt;/script&gt; 스크립트를 적용해주세요.
</b>
</p>

<p>
<figure class="fileblock">
<a href="./file/dataTables.bootstrap.min.js" class="">

<div class="desc">
<div class="filename">
<span class="name">
dataTables.bootstrap.min.js
</span>
</div>
<div class="size">
다운로드
</div>
</div>
</a>
</figure>
</p>

<p>
<figure class="fileblock">
<a href="./file/jquery.dataTables.min.js" class="">

<div class="desc">
<div class="filename">
<span class="name">
jquery.dataTables.min.js
</span>
</div>
<div class="size">
다운로드
</div>
</div>
</a>
</figure>
</p>


<p>
아래와 같이 되겠죠?
</p>

<span class="txt_fold">
더보기
</span>
<div class="moreless_content">
<p>
&lt;script src="http://code.jquery.com/jquery-2.1.4.js"&gt;&lt;/script&gt;
</p>
<p>
&lt;script src="dataTables.bootstrap.min.js"&gt;&lt;/script&gt;
</p>
<p>
<span>
&lt;script src="jquery.dataTables.min.js"&gt;&lt;/script&gt;
</span>
<br>
</p>
</div>


<p>
<b>
2. api 호출을 해봅니다.
</b>
</p>
<p>
다음과같이 호출을 해줍니다.
</p>

<p>
<code class="js plain">
$(
</code>
<code class="js string">
'#example'
</code>
<code class="js plain">
).DataTable();
</code>
</p>



<p>
처음부터 모든걸 다 만들어보겠다 싶으신분들은 한번 만들어보시는걸 추천해드립니다.
</p>
<p>
그러나, 현업에서 시간이 없으신분들은 사용해보시는걸 추천합니다.
</p>
<p>
(그러나, 보다 더 커스터마이징이 필요하다! 그렇다면 만드시는걸 추천해드립니다. )
</p>

<p>
사용해본 경험 - 편리합니다.
</p>

<p>
<b>
다만, 브라우저의 호환성은 테스트해보지 못했습니다. 크롬 48.0 이상 버전에서는 정상작동합니다.
</b>
</p>
