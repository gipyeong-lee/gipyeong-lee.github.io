---
layout: post
title: "Xcode 오류: failedToGetInstalledApplicationInfoAfterInstalling"
description: "Swift로 iOS 앱을 개발하다 보면 다양한 오류를 마주칠 수 있습니다. 그중 하나가 바로 failedToGetInstalledApplicationInfoAfterInstalling 라는 오류입니다. 이 오류는 주로 앱을 설치한 후에, Xcode가 해당 앱의 설치 정보를 가져오지..."
date: 2019-10-20 09:52:28 +0900
section: blog
category: web3
lang: ko
ref: 2019-10-20-legacy-220-web3-xcode-failedtogetinstalledapplicationinfoafterinstalling
tags:
  - "ios"
  - "XCode"
  - "failedtogetinstalledapplicationinfoafterinstalling"
  - "build"
  - "Apple Ecosystem Insights"
  - "web3"
---

<p>
Swift로 iOS 앱을 개발하다 보면 다양한 오류를 마주칠 수 있습니다. 그중 하나가 바로
<b>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
</b>
라는 오류입니다. 이 오류는 주로 앱을 설치한 후에, Xcode가 해당 앱의 설치 정보를 가져오지 못할 때 발생합니다. 이 글에서는 오류의 원인과 해결책을 쉽게 설명하겠습니다.
</p>
<h2>
오류 설명
</h2>
<p>
오류 메시지를 풀어보면 다음과 같은 의미입니다:
</p>
<ul>
<li>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
:
<ul>
<li>
"앱을 설치한 후 설치된 애플리케이션의 정보를 가져오는 데 실패했다"는 뜻입니다.
</li>
</ul>
</li>
</ul>
<p>
즉, 앱을 기기(또는 시뮬레이터)에 설치했지만, Xcode가 설치된 앱의 정보를 제대로 확인하지 못하고 있는 상황입니다. 이는 앱이 제대로 설치되지 않았거나, Xcode와 기기(또는 시뮬레이터) 간의 일시적인 통신 문제로 인해 발생할 수 있습니다.
</p>
<h2>
발생하는 이유
</h2>
<p>
이 오류는 여러 가지 이유로 발생할 수 있지만, 일반적인 원인은 다음과 같습니다:
</p>
<ol>
<li>
<b>
Xcode 빌드 캐시 문제
</b>
: Xcode가 이전 빌드의 캐시를 저장하고 있어 새롭게 빌드된 앱과 혼동이 생길 수 있습니다.
</li>
<li>
<b>
잘못된 설치
</b>
: 앱이 기기에 제대로 설치되지 않았거나, 설치 후 앱 정보를 가져오는 과정에서 문제가 발생한 경우입니다.
</li>
<li>
<b>
시뮬레이터 또는 기기 문제
</b>
: 가끔 시뮬레이터나 연결된 기기에서 오류가 발생하여 Xcode가 설치 정보를 제대로 받지 못할 수 있습니다.
</li>
</ol>
<h2>
해결책: Clean Build
</h2>
<p>
가장 간단하면서도 효과적인 해결책은
<b>
"빌드 클린(Build Clean)"
</b>
을 하는 것입니다. 빌드 클린을 통해 Xcode는 이전의 캐시를 제거하고, 앱을 처음부터 새롭게 빌드하여 문제를 해결할 수 있습니다.
</p>
<h3>
Clean Build 방법
</h3>
<ol>
<li>
Xcode의 메뉴에서
<b>
<code>
Product
</code>
</b>
로 이동합니다.
</li>
<li>
<b>
<code>
Clean Build Folder
</code>
</b>
를 클릭합니다. (단축키:
<code>
Shift + Command + K
</code>
)
</li>
<li>
그런 다음 다시
<b>
<code>
Product &gt; Build
</code>
</b>
를 선택하여 앱을 새롭게 빌드합니다. (단축키:
<code>
Command + B
</code>
)
</li>
</ol>
<h3>
추가적인 해결책
</h3>
<ul>
<li>
<b>
시뮬레이터 재시작
</b>
: 만약 클린 빌드로도 해결되지 않는다면, 시뮬레이터를 껐다가 다시 실행해보세요.
</li>
<li>
<b>
기기 재연결
</b>
: 실제 기기에 배포할 경우, 케이블 연결을 다시 시도하거나 기기를 재부팅한 후 다시 빌드를 시도할 수 있습니다.
</li>
<li>
<b>
Xcode 재시작
</b>
: 간혹 Xcode 자체에 문제가 있을 수 있으므로, Xcode를 재시작하는 것도 하나의 방법입니다.
</li>
</ul>
<h2>
결론
</h2>
<p>
<b>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
</b>
오류는 주로 Xcode와 기기 간의 일시적인 통신 문제로 발생하는 오류입니다. 이를 해결하기 위해서는
<b>
빌드 클린
</b>
을 시도하고, 필요에 따라 시뮬레이터나 기기를 재시작하는 등의 방법을 사용할 수 있습니다. 이 문제는 비교적 흔하게 발생하지만, 해결책이 명확하기 때문에 걱정할 필요는 없습니다.
</p>
