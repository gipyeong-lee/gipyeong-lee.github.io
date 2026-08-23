---
layout: post
title: "Xcode Error: failedToGetInstalledApplicationInfoAfterInstalling"
description: "When developing iOS apps with Swift, you may encounter various errors. One such error is failedToGetInstalledApplicationInfoAfterInstalling. This error typically occurs when, after installing the app, Xcode fails to retrieve the installation information for that app..."
date: 2019-10-20 09:52:28 +0900
section: blog
category: web3
lang: en
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
When developing iOS apps with Swift, you may encounter various errors. One such error is 
<b>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
</b>
. This error typically occurs when, after installing the app, Xcode fails to retrieve the installation information for that app. In this post, we will explain the causes and solutions for this error in simple terms.
</p>
<h2>
Error Explanation
</h2>
<p>
Breaking down the error message reveals the following meaning:
</p>
<ul>
<li>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
:
<ul>
<li>
It means "Failed to retrieve information about the installed application after installation."
</li>
</ul>
</li>
</ul>
<p>
In other words, while the app was installed on the device (or simulator), Xcode is unable to correctly verify the information of the installed app. This can happen if the app was not installed properly or due to a temporary communication issue between Xcode and the device (or simulator).
</p>
<h2>
Causes
</h2>
<p>
This error can occur for several reasons, but common causes include:
</p>
<ol>
<li>
<b>
Xcode Build Cache Issues
</b>
: Xcode may be storing cache from a previous build, creating confusion with the newly built app.
</li>
<li>
<b>
Improper Installation
</b>
: The app may not have been installed correctly on the device, or an issue may have occurred during the process of retrieving app information after installation.
</li>
<li>
<b>
Simulator or Device Issues
</b>
: Sometimes, an error in the simulator or the connected device can prevent Xcode from receiving the installation information properly.
</li>
</ol>
<h2>
Solution: Clean Build
</h2>
<p>
The simplest and most effective solution is to perform a 
<b>
"Clean Build"
</b>
. By performing a clean build, Xcode removes old caches and builds the app from scratch, which can resolve the problem.
</p>
<h3>
How to Clean Build
</h3>
<ol>
<li>
In the Xcode menu, go to 
<b>
<code>
Product
</code>
</b>
.
</li>
<li>
Click 
<b>
<code>
Clean Build Folder
</code>
</b>
. (Shortcut: 
<code>
Shift + Command + K
</code>
)
</li>
<li>
Then, select 
<b>
<code>
Product > Build
</code>
</b>
to rebuild the app from scratch. (Shortcut: 
<code>
Command + B
</code>
)
</li>
</ol>
<h3>
Additional Solutions
</h3>
<ul>
<li>
<b>
Restart Simulator
</b>
: If the clean build does not resolve the issue, try turning the simulator off and back on again.
</li>
<li>
<b>
Reconnect Device
</b>
: If deploying to a physical device, try reconnecting the cable or rebooting the device before attempting the build again.
</li>
<li>
<b>
Restart Xcode
</b>
: Occasionally, there may be an issue with Xcode itself, so restarting Xcode is also a viable option.
</li>
</ul>
<h2>
Conclusion
</h2>
<p>
The 
<b>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
</b>
error is mainly caused by a temporary communication issue between Xcode and the device. To resolve it, you can try a 
<b>
Clean Build
</b>
, and if necessary, restart the simulator or the device. While this issue occurs relatively frequently, there is no need to worry as the solutions are clear and straightforward.
</p>