---
layout: post
title: "[PHP] 웹사이트"
description: "회원가입 회원가입 첫 페이지 로드시 1. [보안] 도메인 체크 if ($_SERVER['HTTP_HOST'] != 'domain'){ exit('허용되지 않은 도메인 입니다.'); } 2. 로그인 세션 체크 ( 만일, 로그인 상태일 경우 메인페이지로 강제 이동 ) if($_SESS..."
date: 2015-08-06 10:18:41 +0900
section: blog
category: essay
lang: ko
ref: 2015-08-06-legacy-68-essay-php
tags:
  - "php"
  - "보안"
  - "로그인"
  - "웹"
  - "회원가입"
  - "사이트"
---

<p>
<span>
<b>
회원가입
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
회원가입 첫 페이지 로드시
</span>
</p>

<p>
<b>
<span>
1. [보안] 도메인 체크
</span>
</b>
</p>

<pre class="brush: php; toolbar: false;gutter:false;">
if ($_SERVER['HTTP_HOST'] != 'domain'){
  exit('허용되지 않은 도메인 입니다.');
}
</pre>


<p>
<b>
<span>
2. 로그인 세션 체크 ( 만일, 로그인 상태일 경우 메인페이지로 강제 이동 )
</span>
</b>
</p>

<pre class="brush: php; toolbar: false; gutter:false;">
if($_SESSION['session_id']){
    header('Location: '.$url);
    exit;
}
</pre>


<p>
<b>
<span>
3. SSL 관련 처리
</span>
</b>
</p>

<pre class="brush: c; toolbar: false; gutter:false;">
if(!isset($_SERVER["HTTPS"])){
    $url = 'https://' . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];
header('Location: '.$url);
}
</pre>

<p>
<b>
<span>
<br>
</span>
</b>
</p>
<p>
<b>
<span>
4. i-Pin 인증 , 본인인증(휴대폰)
</span>
</b>
</p>
<p>
<font>
해당 부분의 경우 form 태그를 이용하여 관련 리퀘스트를 만들어 요청하고, 반환값을 갖고 처리한다.
</font>
</p>
<p>
<font>
<br>
</font>
</p>
<p>
<font>
<b>
5. 이용약관 동의
</b>
</font>
</p>
<p>
자바스크립트를 이용하여 해당 체크박스가 체크되어 있는지 확인 후 진행한다.
</p>



<p>
<span>
<b>
로그인
</b>
</span>
</p>

<p>
<b>
1. 로그인 데이터 넘기기
</b>
</p>
<p>
: 폼 태그를 이용하여 아이디, 패스워드 넘김
</p>


<p>
<b>
<span>
2. [보안] 도메인 체크
</span>
</b>
</p>

<pre class="brush: php; toolbar: false;gutter:false;">
if ($_SERVER['HTTP_HOST'] != 'domain'){
  exit('허용되지 않은 도메인 입니다.');
}
</pre>
<p>
<b>
3. 외부로부터 생성된 폼 데이터 전송 방지
</b>
</p>



<pre class="brush: php; toolbar: false; gutter:false;">
function referer(){

	$http_referer = str_replace('http://','',$_SERVER['HTTP_REFERER']);
	$http_referer = str_replace('https://','',$http_referer);

	$referer = explode('/',$http_referer);

	if ($referer[0] &lt;&gt; $_SERVER['HTTP_HOST']) {

		//경고창 띄우기 스크립트로 처리하면 편함 echo '....';
		exit;
	}

}
</pre>

<p>
<b>
4. 넘어온값 확인
</b>
</p>

<pre class="brush: php; toolbar: false; gutter:false;">
$user_id = trim( $_POST['userid'] );

$user_id= $mysqli_accountdb_s1-&gt;real_escape_string( $userid );// sql injection 방지

$pw = trim( $_POST['password'] );

$backurl = trim( $_POST['backurl'] );
if (!$backurl) {
	$backurl = trim( $_GET['backurl'] ); // 로그인이 완료되면 되돌아갈 url
}
$backurl = xss_replace($backurl); // 크로스 사이트 스크립트 방지 함수를 통한 문자열 처리

if (!$backurl) {
	$backurl = '메인주소 설정'; // 만일 돌아갈 url 없으면 메인 주소로 설정
}
</pre>

<p>
<b>
5. 해싱
</b>
</p>

<pre class="brush: php; toolbar: false; gutter:false;">
$encode_pw = sha1($pw);
</pre>

<p>
<b>
<br>
</b>
</p>
<p>
<b>
6. 세션을 이용한 연속 로그인 딜레이 처리
</b>
</p>
<pre class="brush: php; toolbar: false; gutter:false;">
if($_SESSION['ss_logintime'] != '') {
	$chk_time = mktime(date("H"),date("i"),date("s")-10,date("m"),date("d"),date("Y"));

	if ($chk_time &lt; strtotime($_SESSION['ss_logintime'])) {
		$msg = "로그인이 진행 중 입니다. 잠시 기다려 주십시오.";
		msg($msg); // 알림 띄우기
		ob_flush();
		flush();
		sleep(2);
	}
}

$_SESSION['ss_logintime'] = date('Y-m-d H:i:s');
</pre>


<p>
<b>
7.IP 체크
</b>
</p>
<p>
쿠키를 이용한 IP 체크 + 로그인 횟수 제한 ( 10회 이하 ) &gt; 10분간 제한둠 ( 쿠키에 로그인 시간 담고 처리 )
</p>

<p>
<b>
8. 로그인 매크로 체크
</b>
</p>
<p>
무작위 대입법을 이용한 해킹 방지
</p>

<p>
<b>
9. 실제 유저 체크
</b>
</p>
<p>
유저가 존재하는지 , 탈퇴유저가 아닌지 ,비밀번호가 맞는지 _ 해당부분은 query 로 체크해도 되고, php 내부에서 체크해도 됨.
</p>

<p>
<b>
10. 해외 IP 차단 유저 체크
</b>
</p>
<p>
해외 IP 차단을 통한 우회 해킹 방지.
</p>

<p>
<b>
11. 로그인 실패 횟수 누적 5회 이상 로그인 불가 &gt; 비번찾기로 유도
</b>
</p>
<p>
로그인 실패 횟수가 5회 이상일 경우 , 비번찾기 페이지로 리다이렉트
</p>

<p>
<b>
12. 로그인 시작
</b>
</p>
<p>
세션 생성.
</p>

<p>
<b>
13. 유저 정보 최종 로그인 정보 업데이트
</b>
</p>
<p>
session_id , 로그인 실패 횟수, 로그인 날짜, 로그인 ip
</p>

<p>
<b>
14. 로그인 히스토리 추가
</b>
</p>
<p>
로그인 히스토리 테이블에 로그인 기록을 남깁니다.
</p>

<p>
<b>
15. 간편회원,페이스북회원 체크
</b>
</p>
<p>
정회원 전환 메뉴로 강제 이동.
</p>

<p>
<b>
16. 비밀번호 변경 체크
</b>
</p>
<p>
비밀번호 변경 후 90일이 지났는지 확인합니다.
</p>

<p>
<span>
<b>
MySQL
</b>
</span>
</p>

<p>
<b>
1. Insert 가 에러가 났을 경우에도 auto_increment 값은 증가해있다.
</b>
</p>
<p>
<b>
</b>
실제, MySQLi 를 이용하여 insert 쿼리문을 날린 후 duplicate 등의 에러로 레코드가 쌓이지 않아도. 해당 auto_increment key 값은 +1 증가되어 있다.
</p>
<p>
다음 article 에서는 이를 MySQL 버그라고 얘기한다.
</p>
<p>
(http://desmart.com/blog/be-careful-with-mysqls-auto-increment-how-we-ended-up-losing-data)
<br>
</p>
<p>
<b>
<span>
QA
</span>
</b>
</p>

<p>
<b>
1. &amp;#65279
</b>
</p>
<p>
만일, 출력된 화면에 다음과 같은 코드가 표시되고 의도했던 echo 값이 안나올 경우.
<span>
&amp;#65279;
</span>
</p>
<p>
해당 부분은 'encoding 문제이다'
</p>
<p>
해결책으로는 notepad++ 를 이용하여 해당 파일의 인코딩을 UFT-8 (BOM 없음) 으로 해당 소스를 인코딩해주면 해결이 된다.
</p>

<p>
<b>
<span>
2.
</span>
<span>
HTML 파일에서 PHP 코드를 실행시키려면
</span>
</b>
</p>

<p>
(1) httpd.conf 파일내 아래의 내용을 입력한다.
</p>

<pre class="brush: c; toolbar: false; gutter:false;">
AddHandler application/x-httpd-php .html
</pre>

<p>
<font>
<span>
<br>
</span>
</font>
</p>
<p>
<font>
<span>
(2) .htaccess 파일안에 아래의 내용을 입력한다.
</span>
</font>
</p>
<p>
<font>
<br>
</font>
</p>

<pre class="brush: php; toolbar: false; gutter:false;">
AddType application/x-httpd-php .html
</pre>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<span>
<b>
<span>
3. global 이 뭔가욤?
</span>
</b>
<br>
</span>
</p>
<p>
global 은 함수에서 사용하는 변수가 전역변수와 이름이 같을때, 전역변수를 가져다 쓸 수 있도록 해주는 녀석입니다.
</p>
<p>
ios 쪽 코드에서는 self.변수명 이런 느낌이라고 생각하면 편합니다.
</p>





<p>
<b>
<span>
참고사항
</span>
</b>
</p>
<p>
<b>
<span>
<br>
</span>
</b>
</p>
<p>
<span>
<b>
[SERVER]
</b>
</span>
</p>
<p>
$_SERVER['REQUEST_URI'] = 현재페이지의 주소에서 도메인 제외 =  index.phpuser=&amp;name=
</p>
<p>
$_SERVER['PHP_SELF'] = 현재페이지의 주소에서 도메인과 넘겨지는 값 제외 = index.php
</p>

<p>
<b>
[required or required_once , include or include_once ]
</b>
</p>
<p>
본래 required , include  대신 required_once , include_once 를 사용하였다.
</p>
<p>
해당 api 를 쓰는 이유는 중복 함수를 피하기 위해서다.
</p>
<p>
그러나, 해당 api 는 속도를 떨어뜨린다고 한다.
</p>
<p>
그러므로 다음과 같이 사용하는게 더 좋다고 한다.
</p>


<pre class="brush: php; toolbar: false; gutter:false;">
if (!defined('MyIncludeName')) {
    require('MyIncludeName');
    define('MyIncludeName', 1);
}
</pre>


<p>
아래는 비교한 결과이다.
</p>

<pre class="lang-php prettyprint prettyprinted">
<code>
<span class="pln">
php                  hhvm
</span>
<span class="kwd">
if
</span>

<span class="kwd">
defined
</span>

<span class="lit">
0.18587779998779
</span>

<span class="lit">
0.046600103378296
</span>
<span class="pln">
require_once
</span>
<span class="lit">
1.2219581604004
</span>

<span class="lit">
3.2908599376678
</span>
</code>
</pre>


<p>
<span>
[추가 TIP]
</span>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
echo가 print 보다 빠르다.
</span>
</b>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
string을 감싸는데 있어서 작은따옴표(') 가 큰따옴표(")보다 빠르다.
</span>
</font>
</p>

<p>
<font>
<span>
그 이유는 PHP는 큰따옴표안에서 변수를 찾고 작은 따옴표에서는 변수를 찾지 않기 때문이다.
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
string에 변수가 없다면 작은따옴표를 사용해라.
</span>
</b>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<span>
미리 계산한 값을 사용해라. for루프를 위해서 가장큰값을 지정할때 루프에 넣지말고
</span>
</p>

<p>
<font>
<span>
$max = count($array)를 for 루프가 시작하기 전에 사용해라
</span>
</font>
</p>




<pre class="brush: php; toolbar: false; gutter:false">
for($x=0;$x&lt;count($array);$x++) ==&gt; for($x=0;$x&lt;$max;$x++)
</pre>

<span>


<p>
<span>
메모리 해제를 위해서
</span>
<font>
<span>
<span>
크기가 큰 배열은
</span>
<b>
<u>
<span>
unset
</span>
</u>
</b>
<span>
or
</span>
<b>
<u>
<span>
null
</span>
</u>
</b>
<span>
처리를 해야한다.
</span>
</span>
</font>
</p>



<p>
<span>
<b>
<span>
str_replace가 preg_replace보다 빠르다.
</span>
</b>
<span>
str_replace는 왠만하면 최고고, 그러나
</span>
</span>
<span>
strstr
</span>
<span>
이 때대로 큰 string에서 좀더 빠르다. str_prelace안에 배열을 사용하는 것이 보통 여러개의 str_replace를 쓰는 것보다 빠르다.
</span>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
else if 구문이 switch보다 빠르다
</span>
</b>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
사용하고 데이터베이스 connection을 닫아라
</span>
</b>

</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
$row['id']가 $row[id]보다 7배가 빠르다.
</span>
</b>
<span>
작은따옴표를 사용하지 않으면, 시스템이 무엇이 당신이 의미한 인덱스인지 추측해야한다.
</span>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
php를 선언할때는 &lt;?php ... ?&gt; 을 사용하자. 다른 스타일은 모두 불량
</span>
</b>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<span>
엄격한 코드를 사용하자, notice와 warning, error를 안보이게 하는것을 피하자. 좀더 깨끗한 코드와 덜 부하가 되는 결과를 나타낸다.
</span>
<b>
<span>
error_reporting(E_ALL) 을 항상 켜놓는 것을 고려하자.
</span>
</b>

</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
header('location:'.$url);을 사용할때는 exit를 함께 사용
</span>
</b>
<span>
하는것을 기억해라
</span>
</span>
</font>
</p>

<p>
<font>
<span>
<u>
<span>
location이 바뀌었음에도 불구하고 스크립트는 계속 진행된다.
</span>
</u>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
변수는 미리 초기화하여 사용하자. 그렇지 않으면 매우 느리다.
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<b>
<span>
에러를 보이지 않게 하는 @는 매우느리다
</span>
</b>
</p>



<p>
<b>
<span>
단순 SELECT 기능을 사용할때는 GET 메소드를, UPDATE 기능을 사용할때는 POST 를 이용하여 통신하는게 좋다
</span>
</b>
</p>

<p>
<b>
<span>
왜냐면, GET 의 경우 캐싱이되어 속도가 상대적으로 빠르다. ( POST  는 캐싱 되지 않는다. )
</span>
</b>
</p>




<p>
<b>
<span>
PHP 5.2.9 에서는 array() 녀석이 '[ ]' 를 해석하지 못합니다. 주의
</span>
</b>
</p>
<p>
<font>
<span>
<b>
<span>
만일, 기존 소스가 '[ ]' 를 이용하여 배열을 쓰고 있다면 이를 5.2.9 버전에서는 array() 로 바꾸어주어야 합니다.
</span>
</b>
</span>
</font>
</p>



<p>
<font>
<span>
<b>
<span>
Do not use preg_match()
</span>
</b>
</span>
</font>
</p>
<p>
<font>
<span>
if you only want to check if one string is contained in another string.
</span>
</font>
</p>
<p>
<font>
<span>
Use
<u>
strpos()
</u>
or
<u>
strstr()
</u>
instead as they will be faster.
</span>
</font>
</p>
</span>
