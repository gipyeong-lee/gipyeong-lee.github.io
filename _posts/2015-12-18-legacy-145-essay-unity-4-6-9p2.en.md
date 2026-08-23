---
layout: post
title: "[Unity] Error experience during 4.6.9p2 build."
description: "Hello? Today I am going to introduce 'that guy'... who keeps giving me a hard time. [ That guy ] 0. 4.6.9f1, 4.6.9p2, 4.7.0 none of them work. 1. Plays well when building in Editor. 2. Runs well on Android Galaxy 2. 3. iO..."
date: 2015-12-18 17:22:03 +0900
section: blog
category: essay
lang: en
ref: 2015-12-18-legacy-145-essay-unity-4-6-9p2
tags:
  - "Experience"
  - "essay"
translation_source_hash: 11ca00f61b368cba51d4ad348f1bd1eb64385a82b27cbc41c0b7c7cf9d6cf591
---

<p>
Hello?
</p>

<p>
Today I am going to introduce 'that guy'... who keeps giving me a hard time.
</p>

<p>
[ That guy ]
</p>

<p>
0. 4.6.9f1, 4.6.9p2, 4.7.0 none of them work.
</p>
<p>
1. Plays well when building in Editor.
</p>
<p>
2. Runs well on Android Galaxy 2.
</p>
<p>
3. Does not run on iOS 9.1, 9.2.
</p>
<p>
4. Runs well when building backend with mono 2.x.
</p>
<p>
<b>
<span>
5. Does not run when building with IL2CPP. ㅡ,.ㅡ ( during loadLevel process )
</span>
</b>
</p>


<p>
[ Efforts made to get along with that guy ]
</p>
<p>
1. Added Debug.Log() to every Awake in the next scene. ( Seems like it got even further away... )
</p>


<p>
P.s. Yun-gyu, who is developing next to me. "If I could type the code, I would(?)" lol
</p>



<p>
[ Current relationship with that guy ]
</p>

<p>
_ Sent a technical support email to Unity.. Below is the content of the email OTL.
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
and, when i debug stack. that show---
layout: post
title: "[Unity] Error experience during 4.6.9p2 build."
description: "Hello? Today, I'm going to introduce 'that guy' who keeps... making my life difficult.. [ That guy ] 0. 4.6.9f1, 4.6.9p2, 4.7.0, none of them work. 1. It plays well when building in the Editor. 2. It runs fine on the Android Galaxy 2 as well. 3. iO..."
date: 2015-12-18 17:22:03 +0900
section: blog
category: essay
lang: en
ref: 2015-12-18-legacy-145-essay-unity-4-6-9p2
tags:
  - "Experience"
  - "essay"
---

<p>
Hello?
</p>

<p>
Today, I'm going to introduce 'that guy' who keeps... making my life difficult..
</p>

<p>
[ That guy ]
</p>

<p>
0. 4.6.9f1, 4.6.9p2, 4.7.0, none of them work.
</p>
<p>
1. It plays well when building in the Editor.
</p>
<p>
2. It runs fine on the Android Galaxy 2 as well.
</p>
<p>
3. It doesn't run on iOS 9.1, 9.2.
</p>
<p>
4. It runs fine when building the backend with mono 2.x.
</p>
<p>
<b>
<span>
5. It doesn't run when building with IL2CPP. ㅡ,.ㅡ ( during loadLevel processing )
</span>
</b>
</p>


<p>
[ Efforts to get closer to that guy ]
</p>
<p>
1. I added Debug.Log() to every Awake in the next scene. (It seems like we've drifted even further apart..)
</p>



<p>
P.s. Yun-gyu, who is developing next to me: "If I could just code, I would code(?)" Haha.
</p>



<p>
[ Current relationship with that guy ]
</p>

<p>
_ I sent a technical support email to Unity.. The email content is below, OTL.
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
and, when i debug stack. that show me . 'GC_LOCK' last