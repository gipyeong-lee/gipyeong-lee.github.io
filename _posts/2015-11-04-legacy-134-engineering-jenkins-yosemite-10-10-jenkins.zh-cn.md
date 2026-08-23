---
layout: post
title: "[Jenkins] 在 Yosemite 10.10 上安装 Jenkins 的注意事项"
description: "[问题] 下载并安装 Jenkins pkg 文件后立即运行，可能会遇到以下错误：localhost:8080 ... error.. 输入 cat /var/log/jenkins/jenkins.log 后可以看到如下日志：JLReques..."
date: 2015-11-04 22:37:53 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2015-11-04-legacy-134-engineering-jenkins-yosemite-10-10-jenkins
tags:
  - "Yosemite"
  - "jenkins"
  - "Server"
  - "engineering"
translation_source_hash: de97e0da2e2c3fbd365b2d74bac8e2d3e72a1ccb527c7adb51e96ad5b2f45aa8
---

<p>
<span>
[问题]
</span>
</p>

<p>
<span>
下载并安装 Jenkins pkg 文件后立即运行，可能会遇到以下错误：
</span>
</p>
<p>
<span>
localhost:8080 ... error..
</span>
</p>


<p>
<span>
输入
</span>
</p>
<p>
<span>
cat /var/log/jenkins/jenkins.log
</span>
</p>


<p>
<span>
后可以看到如下日志：
</span>
</p>


<p>
<span>
JLRequestRuntimeInstall: Error calling: CFMessagePortCreateRemote
</span>
</p>



<p>
<span>
[解决方法]
</span>
</p>
<p>
<b>
<span>
安装 JDK 后重新运行 pkg 文件即可。
</span>
</b>
</p>
<p>
<b>
<span>
( 脚本将正常运行，您可以访问 Jenkins 页面。 )
</span>
</b>
</p>




<p>
Jenkins 自动构建部分也已完成。
</p>

<p>
以下是进行顺序：
</p>

<p>
1. 安装 Jenkins
</p>

<p>
2. 在 Unity3d 插件中设置环境变量 ( Unity 应用路径 )
</p>

<p>
3. 下载 android-sdk 并设置路径
</p>

<p>
4. 编写自动上传构建文件至 FTP 的 shell 脚本 ( 由于原有的 FTP 插件无法在公司内部系统运行，因此单独编写了脚本 )
</p>

<p>
5. 设置构建周期
</p>

<p>
如有疑问，
</p>

<p>
请发送邮件至 gipyeong.lee@madorca.com 进行咨询 :)
</p>

<p>
非常抱歉没有时间整理相关资源 (_ _)
</p>





<div>
<hr>
</div>


<p>
以下是通过 brew 进行安装的方法。
</p>


<p>
1. 在 Mac 上安装 brew。
</p>

<pre>
<code>
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
</code>
</pre>


<p>
2. 安装 jenkins。
</p>

<p>
brew install jenkins
</p>


<p>
之后会自动进行安装
</p>



<p>
3. 设置
</p>


<ul>
<li>
若要在登录时启动 jenkins：
<pre>
<code>
mkdir -p ~/Library/LaunchAgents
 ln -sfv /usr/local/opt/jenkins/*.plist ~/Library/LaunchAgents
</code>
</pre>
</li>
<li>
若要立即加载 jenkins：
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
4. 附加设置 ( 不设置单独的 jenkins 用户，而是设置为当前用户 )
</p>
<p>
sudo vim /Library/LaunchDaemons/org.jenkins-ci.plist
</p>

<p>
修改为以下内容
</p>
<p>
( 假设 buildpc 为用户名 )
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
之后执行
</p>
<p>
launchctl unload -w /Library/LaunchDaemons/org.jenkins-ci.plist
</p>
<p>
launchctl load -w /Library/LaunchDaemons/org.jenkins-ci.plist
</p>