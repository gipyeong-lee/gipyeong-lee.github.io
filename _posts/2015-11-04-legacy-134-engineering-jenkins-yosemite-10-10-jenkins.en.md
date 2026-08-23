---
layout: post
title: "[Jenkins] Points to consider when installing Jenkins on Yosemite 10.10"
description: "[Problem] If you download the Jenkins pkg file and run it immediately after installation, you may encounter the following error: localhost:8080 ... error.. When you enter cat /var/log/jenkins/jenkins.log, you can see the following log: JLReques..."
date: 2015-11-04 22:37:53 +0900
section: blog
category: engineering
lang: en
ref: 2015-11-04-legacy-134-engineering-jenkins-yosemite-10-10-jenkins
tags:
  - "Yosemite"
  - "Yosemite"
  - "jenkins"
  - "jenkins"
  - "Server"
  - "engineering"
translation_source_hash: de97e0da2e2c3fbd365b2d74bac8e2d3e72a1ccb527c7adb51e96ad5b2f45aa8
---

<p>
<span>
[Problem]
</span>
</p>

<p>
<span>
If you download the Jenkins pkg file and run it immediately after installation, you may encounter the following error:
</span>
</p>
<p>
<span>
localhost:8080 ... error..
</span>
</p>


<p>
<span>
When you enter
</span>
</p>
<p>
<span>
cat /var/log/jenkins/jenkins.log
</span>
</p>


<p>
<span>
you can see the following log:
</span>
</p>


<p>
<span>
JLRequestRuntimeInstall: Error calling: CFMessagePortCreateRemote
</span>
</p>



<p>
<span>
[Solution]
</span>
</p>
<p>
<b>
<span>
If you install the JDK and then run the pkg file again,
</span>
</b>
</p>
<p>
<b>
<span>
(the script will work normally and you will be able to access the Jenkins page.)
</span>
</b>
</p>




<p>
I have even completed Jenkins auto-build.
</p>

<p>
Below is the procedure I followed:
</p>

<p>
1. Install Jenkins
</p>

<p>
2. Set environment variables in the Unity3d Plugin (Unity app path)
</p>

<p>
3. Download android-sdk and set the path
</p>

<p>
4. Write a shell script for automatic FTP upload of build files (I wrote a separate script as the existing FTP plugin did not work due to in-house system constraints)
</p>

<p>
5. Set the build schedule
</p>

<p>
If you have any questions,
</p>

<p>
please contact me at gipyeong.lee@madorca.com :)
</p>

<p>
I apologize for not having time to organize the related resources (_ _)
</p>





<div>
<hr>
</div>


<p>
The following is for installation using brew.
</p>


<p>
1. Install brew on your Mac.
</p>

<pre>
<code>
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
</code>
</pre>


<p>
2. Install jenkins.
</p>

<p>
brew install jenkins
</p>


<p>
It will install automatically after that.
</p>



<p>
3. Configuration
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
4. Additional configuration (setting it to the current user instead of a separate jenkins user)
</p>
<p>
sudo vim /Library/LaunchDaemons/org.jenkins-ci.plist
</p>

<p>
Change to the content below.
</p>
<p>
(Assuming 'buildpc' is the user)
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
After that:
</p>
<p>
launchctl unload -w /Library/LaunchDaemons/org.jenkins-ci.plist
</p>
<p>
launchctl load -w /Library/LaunchDaemons/org.jenkins-ci.plist
</p>