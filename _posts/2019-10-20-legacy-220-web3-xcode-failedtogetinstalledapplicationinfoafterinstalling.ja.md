---
layout: post
title: "Xcodeエラー: failedToGetInstalledApplicationInfoAfterInstalling"
description: "SwiftでのiOSアプリ開発中、さまざまなエラーに遭遇することがあります。その一つが「failedToGetInstalledApplicationInfoAfterInstalling」というエラーです。このエラーは主にアプリのインストール後、Xcodeが該当アプリのインストール情報を取得できない場合に発生します。本記事では、このエラーの原因と解決策を分かりやすく解説します。"
date: 2019-10-20 09:52:28 +0900
section: blog
category: web3
lang: ja
ref: 2019-10-20-legacy-220-web3-xcode-failedtogetinstalledapplicationinfoafterinstalling
tags:
  - "ios"
  - "XCode"
  - "failedtogetinstalledapplicationinfoafterinstalling"
  - "build"
  - "Apple Ecosystem Insights"
  - "web3"
translation_source_hash: 58b13df82e9106e9297822bf555965cec599a3160ce0903a914668188ff95682
---

<p>
SwiftでのiOSアプリ開発中、さまざまなエラーに遭遇することがあります。その一つが
<b>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
</b>
というエラーです。このエラーは主にアプリのインストール後、Xcodeが該当アプリのインストール情報を取得できない場合に発生します。本記事では、このエラーの原因と解決策を分かりやすく解説します。
</p>
<h2>
エラーの説明
</h2>
<p>
エラーメッセージを紐解くと、以下のような意味になります：
</p>
<ul>
<li>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
:
<ul>
<li>
「アプリのインストール後、インストールされたアプリケーションの情報を取得するのに失敗した」という意味です。
</li>
</ul>
</li>
</ul>
<p>
つまり、アプリをデバイス（またはシミュレータ）にインストールしたものの、Xcodeがインストールされたアプリの情報を正しく確認できていない状態です。アプリが正常にインストールされなかったか、Xcodeとデバイス（またはシミュレータ）間の一時的な通信問題によって発生する可能性があります。
</p>
<h2>
発生理由
</h2>
<p>
このエラーが発生する理由はいくつか考えられますが、一般的な原因は以下の通りです：
</p>
<ol>
<li>
<b>
Xcodeのビルドキャッシュの問題
</b>
: Xcodeが以前のビルドキャッシュを保持しており、新しくビルドされたアプリと競合が発生している可能性があります。
</li>
<li>
<b>
インストール失敗
</b>
: アプリがデバイスに正しくインストールされなかったか、インストール後にアプリ情報を取得する過程で問題が発生した場合です。
</li>
<li>
<b>
シミュレータまたはデバイスの問題
</b>
: 時折、シミュレータや接続されたデバイスでエラーが発生し、Xcodeがインストール情報を正しく受け取れないことがあります。
</li>
</ol>
<h2>
解決策: Clean Build
</h2>
<p>
最も簡単で効果的な解決策は
<b>
「ビルドのクリーン（Build Clean）」
</b>
を行うことです。ビルドクリーンを実行すると、Xcodeは以前のキャッシュを削除し、アプリを最初からビルドし直すため、問題を解決できることがあります。
</p>
<h3>
Clean Buildの方法
</h3>
<ol>
<li>
Xcodeのメニューバーから
<b>
<code>
Product
</code>
</b>
を選択します。
</li>
<li>
<b>
<code>
Clean Build Folder
</code>
</b>
をクリックします。（ショートカットキー:
<code>
Shift + Command + K
</code>
）
</li>
<li>
その後、再度
<b>
<code>
Product &gt; Build
</code>
</b>
を選択してアプリをビルドします。（ショートカットキー:
<code>
Command + B
</code>
）
</li>
</ol>
<h3>
その他の解決策
</h3>
<ul>
<li>
<b>
シミュレータの再起動
</b>
: クリーンビルドで解決しない場合は、シミュレータを一度終了して再起動してみてください。
</li>
<li>
<b>
デバイスの再接続
</b>
: 実機にデプロイする場合、ケーブルを繋ぎ直すか、デバイスを再起動してから再度ビルドを試みてください。
</li>
<li>
<b>
Xcodeの再起動
</b>
: まれにXcode自体に問題がある場合があるため、Xcodeを再起動するのも一つの方法です。
</li>
</ul>
<h2>
結論
</h2>
<p>
<b>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
</b>
エラーは、主にXcodeとデバイス間の一時的な通信問題によって発生します。これを解決するには
<b>
ビルドクリーン
</b>
を試し、必要に応じてシミュレータやデバイスを再起動する方法が有効です。この問題は比較的よく発生しますが、解決策が明確なため、過度に心配する必要はありません。
</p>