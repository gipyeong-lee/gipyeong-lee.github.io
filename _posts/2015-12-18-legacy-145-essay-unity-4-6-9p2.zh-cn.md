---
layout: post
title: "[Unity] 4.6.9p2 构建时遇到的错误。"
description: "你好？今天我要介绍一下那个一直……折磨我的“家伙”…… [ 那家伙 ] 0. 4.6.9f1, 4.6.9p2, 4.7.0 全部不行。 1. 在 Editor 中构建时运行良好。 2. 在 Android Galaxy 2 上也能正常运行。 3. iO..."
date: 2015-12-18 17:22:03 +0900
section: blog
category: essay
lang: zh-cn
ref: 2015-12-18-legacy-145-essay-unity-4-6-9p2
tags:
  - "经验谈"
  - "essay"
translation_source_hash: 11ca00f61b368cba51d4ad348f1bd1eb64385a82b27cbc41c0b7c7cf9d6cf591
---

<p>
你好？
</p>

<p>
今天我要介绍一下那个一直……折磨我的“家伙”……
</p>

<p>
[ 那家伙 ]
</p>

<p>
0. 4.6.9f1, 4.6.9p2, 4.7.0 全部不行。
</p>
<p>
1. 在 Editor 中构建时运行良好。
</p>
<p>
2. 在 Android Galaxy 2 上也能正常运行。
</p>
<p>
3. iOS 9.1, 9.2 无法运行。
</p>
<p>
4. 当使用 mono 2.x 后端进行构建时运行良好。
</p>
<p>
<b>
<span>
5. 使用 IL2CPP 构建时无法运行。 ㅡ,.ㅡ ( 处理 loadLevel 时 )
</span>
</b>
</p>


<p>
[ 为了和那家伙搞好关系所做的努力 ]
</p>
<p>
1. 在下一个场景的所有 Awake 中都添加了 Debug.Log()。（感觉反而离得更远了……）
</p>


<p>
附言：在旁边开发的尹奎（音译）。“如果能修改代码，真想修改一下（？）” 哈哈
</p>



<p>
[ 目前与那家伙的关系 ]
</p>

<p>
_ 给 Unity 发了技术支持邮件……以下是邮件内容 OTL。
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
and, when i debug stack.---
layout: post
title: "[Unity] 4.6.9p2 构建时的错误经历。"
description: "你好？今天我要介绍一下那个一直……折磨着我的“那家伙”…… [ 那家伙 ] 0. 4.6.9f1, 4.6.9p2, 4.7.0 全部不行。 1. 在 Editor 中构建时运行良好。 2. 在 Android Galaxy 2 上也能正常运行。 3. iOS……"
date: 2015-12-18 17:22:03 +0900
section: blog
category: essay
lang: ko
ref: 2015-12-18-legacy-145-essay-unity-4-6-9p2
tags:
  - "经历"
  - "随笔"
---

<p>
你好？
</p>

<p>
今天我要介绍一下那个一直……折磨着我的“那家伙”。
</p>

<p>
[ 那家伙 ]
</p>

<p>
0. 4.6.9f1, 4.6.9p2, 4.7.0 全部不行。
</p>
<p>
1. 在 Editor 中构建时运行良好。
</p>
<p>
2. 在 Android Galaxy 2 上也能正常运行。
</p>
<p>
3. iOS 9.1, 9.2 无法运行。
</p>
<p>
4. 如果将后端 (Backend) 构建为 mono 2.x，则运行良好。
</p>
<p>
<b>
<span>
5. 使用 IL2CPP 构建时无法运行。（处理 loadLevel 时）
</span>
</b>
</p>


<p>
[ 为了与那家伙变亲近所做的努力 ]
</p>
<p>
1. 在所有 Awake 中记录了下一个场景的 Debug.Log()。（感觉反而离得更远了……）
</p>


<p>
附言：在我旁边开发的尹圭。他说：“如果能写代码的话真想写代码（？）” 哈哈。
</p>



<p>
[ 目前与那家伙的关系 ]
</p>

<p>
_ 向 Unity 发送了技术支持邮件……以下是邮件内容 OTL。
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