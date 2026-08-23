---
layout: post
title: "[Jenkins] Yosemite 10.10 でJenkinsをインストールする際の注意点"
description: "[問題] 젠킨스 pkg 파일을 다운로드 받아서 설치를 하시고 바로 실행하시면 아래와 같은 에러를 볼 수 있습니다. localhost:8080 ... error.. cat /var/log/jenkins/jenkins.log 입력시에 아래와 같은 로그를 볼 수 있어요. JLReques..."
date: 2015-11-04 22:37:53 +0900
section: blog
category: engineering
lang: ja
ref: 2015-11-04-legacy-134-engineering-jenkins-yosemite-10-10-jenkins
tags:
  - "ヨセミテ"
  - "Yosemite"
  - "jenkins"
  - "ジェンキンス"
  - "Server"
  - "engineering"
translation_source_hash: de97e0da2e2c3fbd365b2d74bac8e2d3e72a1ccb527c7adb51e96ad5b2f45aa8
---

<p>
<span>
[問題]
</span>
</p>

<p>
<span>
Jenkinsのpkgファイルをダウンロードしてインストールし、すぐに実行すると以下のようなエラーが発生します。
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
と入力すると、以下のようなログが確認できます。
</span>
</p>


<p>
<span>
JLRequestRuntimeInstall: Error calling: CFMessagePortCreateRemote
</span>
</p>



<p>
<span>
[解決策]
</span>
</p>
<p>
<b>
<span>
JDKをインストールした後にpkgファイルを再度実行すると
</span>
</b>
</p>
<p>
<b>
<span>
（スクリプトが正常に動作し、Jenkinsページにアクセスできるようになります。）
</span>
</b>
</p>




<p>
Jenkinsのオートビルドまで完了した状態です。
</p>

<p>
以下は進行手順でした。
</p>

<p>
1. Jenkinsのインストール
</p>

<p>
2. Unity3D Pluginでの環境変数設定（Unityアプリのパス）
</p>

<p>
3. android-sdkのダウンロードおよびパス設定
</p>

<p>
4. ビルドファイルFTP自動アップロードシェルスクリプト作成（既存のFTPプラグインの場合、社内システム上で動作しなかったため、別途スクリプトを作成）
</p>

<p>
5. ビルド周期の設定
</p>

<p>
ご質問等ございましたら、
</p>

<p>
gipyeong.lee@madorca.com までお問い合わせください :)
</p>

<p>
関連リソースを整理する時間がなく、申し訳ありません (_ _)
</p>





<div>
<hr>
</div>


<p>
ここからはbrewを使用したインストール手順です。
</p>


<p>
1. Macにbrewをインストールします。
</p>

<pre>
<code>
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
</code>
</pre>


<p>
2. Jenkinsをインストールします。
</p>

<p>
brew install jenkins
</p>


<p>
これ以降は自動的にインストールされます。
</p>



<p>
3. 設定
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
4. 追加設定（別途Jenkinsユーザーを設定せず、現在のユーザーで設定する場合）
</p>
<p>
sudo vim /Library/LaunchDaemons/org.jenkins-ci.plist
</p>

<p>
以下の内容に変更
</p>
<p>
（buildpcをユーザーと仮定）
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
これ以降、以下を実行
</p>
<p>
launchctl unload -w /Library/LaunchDaemons/org.jenkins-ci.plist
</p>
<p>
launchctl load -w /Library/LaunchDaemons/org.jenkins-ci.plist
</p>