---
layout: post
title: "[Unity] 4.6.9p2 建置時錯誤經驗。"
description: "您好？今天我要介紹那個一直……讓我很頭痛的「傢伙」。[ 那個傢伙 ] 0. 4.6.9f1、4.6.9p2、4.7.0 全部都不行。 1. 在 Editor 裡建置時運作良好。 2. 在 Android Galaxy 2 上也能正常執行。 3. iOS 9.1、9.2 無法運作。 4. 若將後端 (Backend) 建置為 mono 2.x 則可正常執行。 5. 以 IL2CPP 建置時無法執行 (處理 loadLevel 時)。"
date: 2015-12-18 17:22:03 +0900
section: blog
category: essay
lang: zh-tw
ref: 2015-12-18-legacy-145-essay-unity-4-6-9p2
tags:
  - "經驗談"
  - "essay"
translation_source_hash: 11ca00f61b368cba51d4ad348f1bd1eb64385a82b27cbc41c0b7c7cf9d6cf591
---

<p>
您好？
</p>

<p>
今天我要介紹那個一直……讓我很頭痛的「傢伙」。
</p>

<p>
[ 那個傢伙 ]
</p>

<p>
0. 4.6.9f1、4.6.9p2、4.7.0 全部都不行。
</p>
<p>
1. 在 Editor 裡建置時運作良好。
</p>
<p>
2. 在 Android Galaxy 2 上也能正常執行。
</p>
<p>
3. iOS 9.1、9.2 無法運作。
</p>
<p>
4. 若將後端 (Backend) 建置為 mono 2.x 則可正常執行。
</p>
<p>
<b>
<span>
5. 以 IL2CPP 建置時無法執行。 ㅡ,.ㅡ ( 處理 loadLevel 時 )
</span>
</b>
</p>


<p>
[ 為了與他變熟所做的努力 ]
</p>
<p>
1. 在所有下一個場景 (Scene) 的 Awake 中都加入了 Debug.Log()。(感覺反而離得更遠了……)
</p>


<p>
P.s 旁邊正在開發的潤奎 (Yun-gyu)。「如果能敲出程式碼，我還真想敲敲看呢 (？)」哈哈
</p>



<p>
[ 目前與他的關係 ]
</p>

<p>
_ 寄送了技術支援信給 Unity……以下是信件內容 OTL。
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
and, when i debug stack. that show me .---
layout: post
title: "[Unity] 4.6.9p2 建置時的錯誤經驗。"
description: "您好？今天我想介紹那個一直折磨我的「傢伙」…… [ 那個傢伙 ] 0. 4.6.9f1、4.6.9p2、4.7.0 全部不行。 1. 在 Editor 中建置執行順暢。 2. 在 Android Galaxy 2 上也能正常運作。 3. iOS 9.1、9.2 無法運作..."
date: 2015-12-18 17:22:03 +0900
section: blog
category: essay
lang: ko
ref: 2015-12-18-legacy-145-essay-unity-4-6-9p2
tags:
  - "經驗談"
  - "essay"
---

<p>
您好？
</p>

<p>
今天我想介紹那個一直折磨我的「傢伙」……
</p>

<p>
[ 那個傢伙 ]
</p>

<p>
0. 4.6.9f1、4.6.9p2、4.7.0 全部不行。
</p>
<p>
1. 在 Editor 中建置執行順暢。
</p>
<p>
2. 在 Android Galaxy 2 上也能正常運作。
</p>
<p>
3. iOS 9.1、9.2 無法運作。
</p>
<p>
4. 若將 Backend 建置為 mono 2.x，則可正常運作。
</p>
<p>
<b>
<span>
5. 以 IL2CPP 建置時無法運作。 ㅡ,.ㅡ ( 處理 loadLevel 時 )
</span>
</b>
</p>


<p>
[ 為了與那傢伙變熟所做的努力 ]
</p>
<p>
1. 在所有下一個場景的 Awake 中都加入 Debug.Log()。（感覺距離反而更遠了……）
</p>


<p>
附註：在旁邊開發的潤奎（Yun-gyu）說：「如果能寫程式碼的話，真想寫寫看（？）」哈哈。
</p>



<p>
[ 目前與那傢伙的關係 ]
</p>

<p>
_ 發送了技術支援郵件給 Unity…… 下面是郵件內容 OTL。
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
================================