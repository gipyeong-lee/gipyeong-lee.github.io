---
layout: post
title: "[Unity] 4.6.9p2ビルド時のエラー体験"
description: "こんにちは。今日は、私をずっと悩ませている「あいつ」を紹介しようと思います... [あいつ] 0. 4.6.9f1, 4.6.9p2, 4.7.0 すべてダメ。 1. Editorでのビルド時、プレイは問題なし。 2. Android Galaxy 2でも問題なく動作する。 3. iOS 9.1, 9.2で動作しない。 4. Backendをmono 2.xでビルドするとうまくいく。 5. IL2CPPでのビルド時、動作しない。（loadLevel処理時）"
date: 2015-12-18 17:22:03 +0900
section: blog
category: essay
lang: ja
ref: 2015-12-18-legacy-145-essay-unity-4-6-9p2
tags:
  - "体験談"
  - "essay"
translation_source_hash: 11ca00f61b368cba51d4ad348f1bd1eb64385a82b27cbc41c0b7c7cf9d6cf591
---

<p>
こんにちは。
</p>

<p>
今日は、私をずっと悩ませている「あいつ」を紹介しようと思います...
</p>

<p>
[あいつ]
</p>

<p>
0. 4.6.9f1, 4.6.9p2, 4.7.0 すべてダメ。
</p>
<p>
1. Editorでのビルド時、プレイは問題なし。
</p>
<p>
2. Android Galaxy 2でも問題なく動作する。
</p>
<p>
3. iOS 9.1, 9.2で動作しない。
</p>
<p>
4. Backendをmono 2.xでビルドするとうまくいく。
</p>
<p>
<b>
<span>
5. IL2CPPでのビルド時、動作しない。 ㅡ,.ㅡ (loadLevel処理時)
</span>
</b>
</p>


<p>
[あいつと仲良くなろうと試みた努力]
</p>
<p>
1. 次のシーンのDebug.Log()をすべてのAwakeに挿入した。(かえって遠ざかった気がする...)
</p>


<p>
追伸：隣で開発中のユンギュさん。「コードを叩けるものなら叩きたい(?)」(笑)
</p>



<p>
[現在、あいつとの関係]
</p>

<p>
_ Unityに技術サポートメールを送った... 以下はメールの内容です OTL。
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
title: "[Unity] 4.6.9p2 ビルド時のエラー体験。"
description: "こんにちは。今日は引き続き……私を苦しめている『あいつ』を紹介します…… [ あいつ ] 0. 4.6.9f1、4.6.9p2、4.7.0 すべてダメ。 1. Editorでのビルドではプレイがうまくいく。 2. Android Galaxy 2でも問題なく動作する。 3. iO..."
date: 2015-12-18 17:22:03 +0900
section: blog
category: essay
lang: ja
ref: 2015-12-18-legacy-145-essay-unity-4-6-9p2
tags:
  - "体験談"
  - "essay"
---

<p>
こんにちは。
</p>

<p>
今日は引き続き……私を苦しめている『あいつ』を紹介します……。
</p>

<p>
[ あいつ ]
</p>

<p>
0. 4.6.9f1、4.6.9p2、4.7.0 すべてダメ。
</p>
<p>
1. Editorでのビルドではプレイがうまくいく。
</p>
<p>
2. Android Galaxy 2でも問題なく動作する。
</p>
<p>
3. iOS 9.1、9.2で動作しない。
</p>
<p>
4. バックエンドをmono 2.xでビルドした場合はうまくいく。
</p>
<p>
<b>
<span>
5. IL2CPPでビルドすると動作しない。ㅡ,.ㅡ (loadLevel処理時)
</span>
</b>
</p>


<p>
[ あいつと仲良くなろうと試みた努力 ]
</p>
<p>
1. 次のシーンのDebug.Log()をすべてのAwakeに書き込みました。（余計に遠ざかったような……）
</p>


<p>
追伸：隣で開発中のユンギュさん。「コードを叩けるなら叩きたい(?)(笑)」
</p>



<p>
[ 現在のあいつとの関係 ]
</p>

<p>
_ Unityに技術サポートメールを送りました……以下はメールの内容です OTL。
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
</