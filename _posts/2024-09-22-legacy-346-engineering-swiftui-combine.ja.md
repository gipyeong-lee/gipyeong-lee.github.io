---
layout: post
title: "[SwiftUI] Combineを利用したリアルタイムデータ購読と更新"
description: "SwiftUIとCombineは、iOSアプリ開発における非同期データ処理を非常にシンプルかつ効率的にします。特に@PublishedとCombineの購読機能を活用すれば、データがリアルタイムで更新されるたびにビューを自動的に更新できます。本稿では、ProfileViewModelの例を通じて、SwiftUIでCombineを活用してデータをリアルタイムに更新し、効率的に管理する方法を紹介します。"
date: 2024-09-22 01:43:29 +0900
section: blog
category: engineering
lang: ja
ref: 2024-09-22-legacy-346-engineering-swiftui-combine
tags:
  - "Combine"
  - "SwiftUI"
  - "@Published"
  - "ObservableObject"
  - "swift"
  - "Apple Ecosystem Insights"
translation_source_hash: 26c4f698cc23d8e77414996800e645740657f52bc01baf206d502ad82874766a
---

<blockquote>
<span>
SwiftUIとCombineは、iOSアプリ開発における非同期データ処理を非常にシンプルかつ効率的にします。特に@PublishedとCombineの購読機能を活用すれば、データがリアルタイムで更新されるたびにビューを自動的に更新できます。本稿では、ProfileViewModelの例を通じて、SwiftUIでCombineを活用してデータをリアルタイムに更新し、効率的に管理する方法を紹介します。
</span>
</blockquote>

<h3>
<span>
コード例:
<code>
ProfileViewModel
</code>
</span>
</h3>
<pre class="bash">
<code>
class ProfileViewModel: ObservableObject {
    @Published var currentUser: User?
    private var cancellables = Set&lt;AnyCancellable&gt;()

    init() {
        setupSubscribers()
    }

    private func setupSubscribers() {
        UserService.shared.$currentUser.sink { [weak self] user in
            self?.currentUser = user
        }.store(in: &amp;cancellables)
    }
}
</code>
</pre>
<p>
<span>
このコードは、ユーザーのプロフィールデータをリアルタイムで更新してSwiftUIビューに反映させる
<code>
ProfileViewModel
</code>
を定義しています。Combineを活用したデータ購読と
<code>
@Published
</code>
プロパティを使用することで、SwiftUIとの状態連動を簡単に設定できます。
</span>
</p>

<h3>
<span>
コード解析
</span>
</h3>
<h4>
<span>
1.
<code>
class ProfileViewModel: ObservableObject
</code>
</span>
</h4>
<p>
<span>
<code>
ProfileViewModel
</code>
は
<code>
ObservableObject
</code>
プロトコルを採用しています。これにより、
<b>
ViewModel
</b>
がSwiftUIビューにデータを提供し、データ変更時にビューが自動的に更新されるようになります。
</span>
</p>

<h4>
<span>
2.
<code>
@Published var currentUser: User?
</code>
</span>
</h4>
<p>
<span>
<code>
@Published
</code>
属性ラッパーは、
<code>
currentUser
</code>
が更新されるたびに
<b>
SwiftUI
</b>
がその変更を検知し、ビューを再描画させます。これによりデータフローを
<b>
リアクティブ
</b>
に管理でき、ユーザー情報変更時にビューへ即時反映されます。
</span>
</p>

<h4>
<span>
3.
<code>
private var cancellables = Set&lt;AnyCancellable&gt;()
</code>
</span>
</h4>
<p>
<span>
Combineでデータを購読する際、購読をキャンセルできるオブジェクトである
<code>
AnyCancellable
</code>
を格納するコレクションです。Swiftにおいてメモリリークを防ぎ、必要に応じて購読を解除するために
<b>
Cancellable
</b>
を管理することは重要です。
</span>
</p>

<h4>
<span>
4.
<code>
init()
</code>
と
<code>
setupSubscribers()
</code>
</span>
</h4>
<p>
<span>
<code>
init
</code>
メソッドは
<code>
ProfileViewModel
</code>
オブジェクト生成時に呼び出され、
<code>
setupSubscribers()
</code>
メソッドを介してCombineの購読設定を初期化します。
</span>
</p>

<h4>
<span>
5.
<code>
UserService.shared.$currentUser.sink { [weak self] user in ... }
</code>
</span>
</h4>
<p>
<span>
ここは
<b>
Combine
</b>
の核心部分です。
<code>
UserService
</code>
内で
<code>
@Published
</code>
として宣言された
<code>
currentUser
</code>
を購読(subscribe)し、データ変更のたびにクロージャが実行されます。
<code>
[weak self]
</code>
は循環参照を防ぐために使用され、
<code>
self
</code>
を弱参照として保持することでメモリ管理に配慮しています。
</span>
</p>

<h4>
<span>
6.
<code>
self?.currentUser = user
</code>
</span>
</h4>
<p>
<span>
データストリームから渡された
<code>
user
</code>
オブジェクトをビューモデルの
<code>
currentUser
</code>
に割り当てます。これにより
<b>
SwiftUIビューは変更されたデータを検知
</b>
し、該当ビューが再描画されます。
</span>
</p>

<h4>
<span>
7.
<code>
print("DEBUG: User in view model from combine is \(user)")
</code>
</span>
</h4>
<p>
<span>
デバッグ用にCombine経由で渡されたデータを出力します。リアルタイムのデータフローを確認する際に有用です。
</span>
</p>

<h4>
<span>
8.
<code>
.store(in: &amp;cancellables)
</code>
</span>
</h4>
<p>
<span>
購読完了後、
<b>
cancellables
</b>
に格納して
<b>
メモリリーク防止
</b>
と購読管理を可能にします。このメソッドにより、Combineの購読が不要になった時点でメモリから自動的に解放されることが保証されます。
</span>
</p>

<hr>
<h3>
<b>
<span>
なぜこのコードが必要なのか？
</span>
</b>
</h3>
<ol>
<li>
<span>
<b>
リアルタイムなデータ反映
</b>
: アプリ内でユーザー情報が変更された際、それをリアルタイムに反映させるのに非常に有用です。例えば、ユーザーのログイン・ログアウト時にビューモデルから自動的に更新できます。
</span>
</li>
<li>
<span>
<b>
メモリ管理
</b>
: 購読終了時にメモリを効率的に管理するには、購読解除が不可欠です。Combineの
<code>
AnyCancellable
</code>
を使用すれば、不要な購読を解除してメモリリークを防げます。
</span>
</li>
<li>
<span>
<b>
リアクティブなアプリ設計
</b>
: SwiftUIの強みの1つは、データとビュー間の
<b>
リアクティブなフロー
</b>
です。Combineを使えばデータ変化に応じてビューが自動更新されるため、自然かつリアルタイムに更新されるUIをユーザーに体験させることができます。
</span>
</li>
</ol>

<hr>
<h3>
<span>
結論
</span>
</h3>
<p>
<span>
Combineを使えばデータフローを簡単に購読でき、状態変更時にリアルタイムでビューを簡単に更新できます。SwiftUIと組み合わせたこのメカニズムは、現代のiOSアプリ開発における非常に強力な武器となります。特に
<code>
@Published
</code>
とCombineの購読パターンは、データフローを効率的に管理し、メモリ管理まで考慮したアプリ開発に不可欠です。
</span>
</p>