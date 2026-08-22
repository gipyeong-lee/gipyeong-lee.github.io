---
layout: post
title: "[Jenkins] Yosemite 10.10 에서 Jenkins설치시 유의점"
description: "[문제] 젠킨스 pkg 파일을 다운로드 받아서 설치를 하시고 바로 실행하시면 아래와 같은 에러를 볼 수 있습니다. localhost:8080 ... error.. cat /var/log/jenkins/jenkins.log 입력시에 아래와 같은 로그를 볼 수 있어요. JLReques..."
date: 2015-11-04 22:37:53 +0900
section: blog
category: engineering
lang: ko
ref: 2015-11-04-legacy-134-engineering-jenkins-yosemite-10-10-jenkins
tags:
  - "요세미티"
  - "Yosemite"
  - "jenkins"
  - "젠킨스"
  - "Server"
  - "engineering"
---

<p>
<span>
[문제]
</span>
</p>

<p>
<span>
젠킨스 pkg 파일을 다운로드 받아서 설치를 하시고 바로 실행하시면 아래와 같은 에러를 볼 수 있습니다.
</span>
</p>
<p>
<span>
localhost:8080 ... error..
</span>
</p>


<p>
<span>
cat /var/log/jenkins/jenkins.log
</span>
</p>


<p>
<span>
입력시에 아래와 같은 로그를 볼 수 있어요.
</span>
</p>


<p>
<span>
JLRequestRuntimeInstall: Error calling: CFMessagePortCreateRemote
</span>
</p>



<p>
<span>
[해결책]
</span>
</p>
<p>
<b>
<span>
JDK 를 설치한 후 pkg 파일을 다시 실행하시면
</span>
</b>
</p>
<p>
<b>
<span>
( 스크립트가 정상 동작하면서 젠킨스 페이지에 접속할 수 있습니다. )
</span>
</b>
</p>




<p>
젠킨스 오토 빌드까지 완료한 상태입니다.
</p>

<p>
아래는 진행 순서 였습니다.
</p>

<p>
1. 젠킨스 설치
</p>

<p>
2. 유니티3d Plugin 에서 환경변수 설정 ( 유니티 앱 경로 )
</p>

<p>
3. android-sdk 다운로드 및 경로 설정
</p>

<p>
4. 빌드 파일 FTP 자동 업로드 shell 스크립트 작성 ( 기존의 ftp 플러그인의 경우 사내 시스템상 동작하지 않아 별도로 스크립트 작성 )
</p>

<p>
5. 언제 빌드 할것인지 주기 설정
</p>

<p>
궁금하신 사항은
</p>

<p>
gipyeong.lee@madorca.com 으로 문의주세용 :)
</p>

<p>
관련 리소스를 정리할 시간이 없어서 죄송합니다 (_ _)
</p>





<div>
<hr>
</div>


<p>
여기서부터는 brew 를 이용한 설치 입니다.
</p>


<p>
1. mac에 brew 를 설치해줍니다.
</p>

<pre>
<code>
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
</code>
</pre>


<p>
2. jenkins 를 설치해줍니다.
</p>

<p>
brew install jenkins
</p>


<p>
이후 자동으로 설치가 되고
</p>



<p>
3. 설정
</p>


<ul>
<li>
To launch, start jenkins at login:
<pre>
<code>
mkdir -p ~/Library/LaunchAgents
 ln -sfv /usr/local/opt/jenkins/*.plist ~/Library/LaunchAgents
</code>
</pre>
</li>
<li>
To load jenkins now:
<pre>
<code>
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.jenkins.plist
</code>
</pre>
<div>
<code>
<br>
</code>
</div>
</li>
</ul>

<p>
4. 추가 설정 ( 별도의 jenkins 유저 셋안하고 현재 user 로 설정 하기 )
</p>
<p>
sudo vim /Library/LaunchDaemons/org.jenkins-ci.plist
</p>

<p>
아래 내용으로 변경
</p>
<p>
( buildpc 를 user 라 가정 )
</p>

<p>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
</p>
<p>
&lt;!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt;
</p>
<p>
&lt;plist version="1.0"&gt;
</p>
<p>
&lt;dict&gt;
</p>
<p>
&lt;key&gt;Label&lt;/key&gt;
</p>
<p>
&lt;string&gt;Jenkins&lt;/string&gt;
</p>
<p>
&lt;key&gt;ProgramArguments&lt;/key&gt;
</p>
<p>
&lt;array&gt;
</p>
<p>
&lt;string&gt;/usr/bin/java&lt;/string&gt;
</p>
<p>
&lt;string&gt;-jar&lt;/string&gt;
</p>
<p>
&lt;string&gt;/usr/local/Cellar/jenkins/1.636/libexec/jenkins.war&lt;/string&gt;
</p>
<p>
&lt;/array&gt;
</p>
<p>
&lt;key&gt;OnDemand&lt;/key&gt;
</p>
<p>
&lt;false/&gt;
</p>
<p>
&lt;key&gt;RunAtLoad&lt;/key&gt;
</p>
<p>
&lt;true/&gt;
</p>
<p>
&lt;key&gt;UserName&lt;/key&gt;
</p>
<p>
&lt;string&gt;buildpc&lt;/string&gt;
</p>
<p>
&lt;/dict&gt;
</p>

<p>
&lt;/plist&gt;
</p>


<p>
이후 launchctl unload -w /Library/LaunchDaemons/org.jenkins-ci.plist
</p>
<p>
launchctl load -w /Library/LaunchDaemons/org.jenkins-ci.plist
</p>
