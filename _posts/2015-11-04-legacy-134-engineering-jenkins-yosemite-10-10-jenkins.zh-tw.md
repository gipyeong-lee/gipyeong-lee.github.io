---
layout: post
title: "[Jenkins] 在 Yosemite 10.10 安裝 Jenkins 的注意事項"
description: "[問題] 當您下載 Jenkins pkg 檔案並安裝後立即執行，可能會遇到以下錯誤：localhost:8080 ... error.. 輸入 cat /var/log/jenkins/jenkins.log 時，可以看到如下日誌：JLReques..."
date: 2015-11-04 22:37:53 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2015-11-04-legacy-134-engineering-jenkins-yosemite-10-10-jenkins
tags:
  - "優勝美地"
  - "Yosemite"
  - "jenkins"
  - "詹金斯"
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
當您下載 Jenkins pkg 檔案並安裝後立即執行，可能會遇到以下錯誤：
</span>
</p>
<p>
<span>
localhost:8080 ... error..
</span>
</p>


<p>
<span>
輸入
</span>
</p>
<pre><code>cat /var/log/jenkins/jenkins.log</code></pre>
<p>
<span>
時，可以看到如下日誌：
</span>
</p>


<p>
<span>
JLRequestRuntimeInstall: Error calling: CFMessagePortCreateRemote
</span>
</p>



<p>
<span>
[解決方案]
</span>
</p>
<p>
<b>
<span>
安裝 JDK 後，重新執行 pkg 檔案，
</span>
</b>
</p>
<p>
<b>
<span>
(腳本將可正常運作，您即可存取 Jenkins 頁面。)
</span>
</b>
</p>




<p>
目前已完成 Jenkins 自動建置設定。
</p>

<p>
以下是處理流程：
</p>

<p>
1. 安裝 Jenkins
</p>

<p>
2. 在 Unity3D Plugin 中設定環境變數（Unity 應用程式路徑）
</p>

<p>
3. 下載 android-sdk 並設定路徑
</p>

<p>
4. 編寫建置檔案 FTP 自動上傳 shell 腳本（由於現有的 ftp 外掛在公司系統中無法運作，因此另外編寫了腳本）
</p>

<p>
5. 設定建置週期
</p>

<p>
如有任何疑問，
</p>

<p>
請透過 gipyeong.lee@madorca.com 聯繫我 :)
</p>

<p>
很抱歉沒時間整理相關資源 (_ _)
</p>





<div>
<hr>
</div>


<p>
以下是使用 brew 安裝的方法。
</p>


<p>
1. 在 Mac 上安裝 brew。
</p>

<pre>
<code>
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
</code>
</pre>


<p>
2. 安裝 jenkins。
</p>

<p>
brew install jenkins
</p>


<p>
之後將會自動進行安裝。
</p>



<p>
3. 設定
</p>


<ul>
<li>
若要於登入時自動啟動 Jenkins：
<pre>
<code>
mkdir -p ~/Library/LaunchAgents
 ln -sfv /usr/local/opt/jenkins/*.plist ~/Library/LaunchAgents
</code>
</pre>
</li>
<li>
若要立即載入 Jenkins：
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
4. 額外設定（不設定獨立的 jenkins 使用者，改為以目前使用者設定）
</p>
<p>
sudo vim /Library/LaunchDaemons/org.jenkins-ci.plist
</p>

<p>
修改為以下內容：
</p>
<p>
（假設 buildpc 為使用者名稱）
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
之後執行：
</p>
<p>
launchctl unload -w /Library/LaunchDaemons/org.jenkins-ci.plist
</p>
<p>
launchctl load -w /Library/LaunchDaemons/org.jenkins-ci.plist
</p>