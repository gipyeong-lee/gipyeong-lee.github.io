---
layout: post
title: "[Unity] 4.6.9p2 빌드시 오류 경험."
description: "안녕하세요 ? 오늘은 계속... 저를 힘들게 하는 '그 녀석' 소개를 하도록 하겠습니다.. [ 그 녀석 ] 0. 4.6.9f1, 4.6.9p2, 4.7.0 다 안됨. 1. Editor 에서 빌드시 플레이가 잘된다. 2. Android Galaxy 2 에서도 잘 돌아간다. 3. iO..."
date: 2015-12-18 17:22:03 +0900
section: blog
category: essay
lang: ko
ref: 2015-12-18-legacy-145-essay-unity-4-6-9p2
tags:
  - "경험담"
  - "essay"
---

<p>
안녕하세요 ?
</p>

<p>
오늘은 계속... 저를 힘들게 하는 '그 녀석' 소개를 하도록 하겠습니다..
</p>

<p>
[ 그 녀석 ]
</p>

<p>
0. 4.6.9f1, 4.6.9p2, 4.7.0 다 안됨.
</p>
<p>
1. Editor 에서 빌드시 플레이가 잘된다.
</p>
<p>
2. Android Galaxy 2 에서도 잘 돌아간다.
</p>
<p>
3. iOS 9.1,9.2 안돌아간다.
</p>
<p>
4. Backend를 mono 2.x 로 빌드할 경우 잘돌아간다.
</p>
<p>
<b>
<span>
5. IL2CPP 로 빌드시 안돌아간다. ㅡ,.ㅡ ( loadLevel 처리시 )
</span>
</b>
</p>


<p>
[ 그녀석과 친해지려고 한 노력들 ]
</p>
<p>
1. 다음씬의 Debug.Log() 를 모든 Awake 에 찍었습니다. ( 더 멀어진것 같음.. )
</p>


<p>
P.s 옆에서 개발중인 윤규님. "코드를 칠수 있다면 치고 싶다(?)" ㅋㅋ
</p>



<p>
[ 현재 그녀석과의 관계 ]
</p>

<p>
_ Unity 에 기술지원 메일을 보냄.. 아래는 메일 내용입니다 OTL.
</p>

<p>
Hi.
</p>
<p>
I'm developing on Unity3d pro 4.6.9f1, 4.6.9p2, 4.7.0
</p>
<p>
When I checked backend scripts using by 'IL2CPP'. app freezing with GC_LOCK when call the 'LoadLevel'.
</p>
<p>
i don't know why. cause. it is well running before.
</p>
<p>
and it is strange. that when i choose backend scripts 'mono 2.x' it run well on device. no freeze !
</p>

<p>
my application called 'Application.LoadLevel' in coroutine method.
</p>

<p>
My Testing iOS Version is 9.1,9.2.
</p>
<p>
below is my log. after that log it is freezing.
</p>
<p>
and, when i debug stack. that show me . 'GC_LOCK' last trace of stack.
</p>

<p>
============================================================ LOG ============================================================
</p>
<p>
2015-12-18 21:37:45.253 loadevtest[1793:694646] -&gt; registered mono modules 0x101405dd0
</p>
<p>
-&gt; applicationDidFinishLaunching()
</p>
<p>
-&gt; applicationDidBecomeActive()
</p>
<p>
Requesting Resolution: 1334x750
</p>
<p>
Init: screen size 1334x750
</p>
<p>
Initializing Metal device caps
</p>
<p>
Initialize engine version: 4.7.0f1 (9c73fd3cda99)
</p>
<p>
UnloadTime: 6.725333 ms
</p>
<p>
Unloading 4 Unused Serialized files (Serialized files now loaded: 0 / Dirty serialized files: 0)
</p>

<p>
Unloading 662 unused Assets to reduce memory usage. Loaded Objects now: 1131.
</p>
<p>
Total: 15.516417 ms (FindLiveObjects: 0.092416 ms CreateObjectMapping: 0.133583 ms MarkObjects: 0.916791 ms DeleteObjects: 14.206583 ms)
</p>

<p>
UnloadTime: 32.123333 ms
</p>
<p>
==============================================================================================================================
</p>

<p>
I need your help as soon as possible u can... thanks.
</p>
