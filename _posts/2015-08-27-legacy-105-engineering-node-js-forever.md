---
layout: post
title: "[node.js] forever"
description: "node.js에 대한 포스팅을 몰아치고 있군요. 얼마전에 구축했던 Side Effect Studio사이트 에서 사용했던 것들을 좀 정리하고 공유하려다 보니까 node.js에 대해서만 좀 연속적으로 올라가고 있네요. 빨리 다 정리하고 다른 것들도 좀 봐야겠습니다. ㅎ 작년에 Upst..."
date: 2015-08-27 19:29:31 +0900
section: blog
category: engineering
lang: ko
ref: 2015-08-27-legacy-105-engineering-node-js-forever
tags:
  - "Forever"
  - "node.js"
  - "npm"
  - "Scrap"
  - "engineering"
noindex: true
---

<p>
<span>
node.js에 대한 포스팅을 몰아치고 있군요. 얼마전에 구축했던
</span>
<a href="http://sideeffect.kr/" target="_blank">
Side Effect Studio사이트
</a>
<span>
에서 사용했던 것들을 좀 정리하고 공유하려다 보니까 node.js에 대해서만 좀 연속적으로 올라가고 있네요. 빨리 다 정리하고 다른 것들도 좀 봐야겠습니다. ㅎ
</span>
<br>
<br>
<span>
작년에
</span>
<a href="http://blog.outsider.ne.kr/544" target="_blank">
Upstart와 Monit으로 node.js Application 서비스 하기
</a>
<span>
라는 포스팅을 올린적이 있는데 이는 꽤 유용하긴 하지만 관리차원에서 꽤나 귀찮은 점이 있습니다. upstart스크립트 만들고 monit에 룰 적용하고 하는 등의 일은 약간 귀찮은 일입니다. 딱히 다른 대안을 모르겠어서 Upstart와 Monit을 쓰고 있었는데 저 포스팅 이후 node앱의 인스턴스를 관리해 주는
</span>
<a href="https://github.com/indexzero/forever" target="_blank">
forever
</a>
<span>
라는 툴이 공개되었습니다.
</span>
<br>
<br>
<span>
<a href="https://github.com/indexzero/forever" target="_blank">
forever
</a>
는 npm을 사용해서
<span>
npm install forever
</span>
명령어로 간단히 설치가 가능하며 아주 간단한 명령어를 통해서 node.js로 만든 앱을 실행시켜주고 예기치 않게 종료되었을때 다시 실행해주거나 stdout을 로그파일로 남겨주는 등의 관리를 해주는 툴입니다
</span>
<span>
. 사용해 보니 약간의 버그가 있기는 한데 기존 Upstart와 Monit조합에 비해서 사용성이 너무 편리해서 node.js앱의 관리는 모두 forever로 갈아탔습니다.
</span>
<br>
<br>
</p>
<blockquote>
usage: forever [start | stop | stopall | list | cleanlogs] [options] SCRIPT [script options]
<br>
<br>
options:
<br>
start          start SCRIPT as a daemon
<br>
stop           stop the daemon SCRIPT
<br>
stopall        stop all running forever scripts
<br>
list           list all running forever scripts
<br>
cleanlogs      [CAREFUL] Deletes all historical forever log files
</blockquote>
<p>
<br>
<span>
forever의 사용법은 위와 같습니다.
</span>
<span>
등록하고자 하는 스크립트를
<span>
forever start app.js
</span>
와 같이 실행하면
</span>
<span>
됩니다. 프로세스를 보면 forever에 대한 프로세스가 따로 있어서 실행한 app.js 프로세스가 죽을 경우 자동으로 다시 실행을 시켜주게 됩니다. 현재 돌아가고 있는 스크립트를 보려면
<span>
forever list
</span>
를 실행시키면 됩니다.
</span>
<br>
<br>
</p>
<div class="imageblock center">
<img src="http://blog.outsider.ne.kr/attach/1/1154848314.gif.pagespeed.ce.t4pwqQMTlL.gif" alt="forever로 node앱을 등록한 화면 " height="63" width="550">
</div>
<p>
<br>
<span>
프로세스를 종료할때는 앞에 나온 번호를 이용해서
<span>
forever stop 번호
</span>
를 사용하면 됩니다.
</span>
<span>
한눈에 어떤 프로세스를 현재 사용하고 있는지 파악이 되고 log파일을 자동으로 연결해 주기 때문에 사용하기가 무척 편리합니다.
</span>
<br>
<br>
</p>
<div class="imageblock center">
<img src="http://blog.outsider.ne.kr/attach/1/1122859785.gif.pagespeed.ce.brAyzYu1ox.gif" alt="등록된 node앱을 종료한 화면" height="57" width="550">
</div>
<p>
<br>
<br>
<br>
<span>
약간 사용해본 경험으로는 어느정도 안정적인것 같습니다.(별로 접속차가 없어서 fatal이 날 확률이 적기 때문에 정확한건 아니지만 그냥 기분상.. ㅡㅡ;;) 대신 약간의 버그가 있는지  forever start로 앱을 등록했는데 프로세스는 정상적으로 떴는데 forever에는 등록이 되지 않아 리스트에 나타나지 않는 경우가 있습니다. 여러번 테스트를 해보았지만 어떤 규칙성은 못찾았습니다. 이럴때는 해당 스크립트와 그에대한 forever에 대한 프로세스를 강제로 종료하고 다시 등록해주어야 합니다. 이부분 외에는 관리나 사용 모두가 편리해서 참 좋군요.
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
출처 :
<a href="http://blog.outsider.ne.kr/590" target="_blank" class="tx-link">
</a>
</span>
<font>
<span>
<a href="http://blog.outsider.ne.kr/590" target="_blank" class="tx-link">
http://blog.outsider.ne.kr/590
</a>
</span>
</font>
</p>
