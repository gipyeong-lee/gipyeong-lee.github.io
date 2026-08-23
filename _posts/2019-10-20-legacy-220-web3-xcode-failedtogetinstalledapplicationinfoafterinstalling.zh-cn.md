---
layout: post
title: "Xcode 错误: failedToGetInstalledApplicationInfoAfterInstalling"
description: "在开发 Swift iOS 应用时，可能会遇到各种错误。其中之一就是 failedToGetInstalledApplicationInfoAfterInstalling。该错误通常发生在安装应用后，Xcode 无法获取该应用的安装信息..."
date: 2019-10-20 09:52:28 +0900
section: blog
category: web3
lang: zh-cn
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
在开发 Swift iOS 应用时，可能会遇到各种错误。其中之一就是 
<b>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
</b> 
错误。该错误通常发生在安装应用后，Xcode 无法获取该应用的安装信息时。本文将为您简要解释该错误的原因及解决方案。
</p>
<h2>
错误说明
</h2>
<p>
错误信息的含义拆解如下：
</p>
<ul>
<li>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
:
<ul>
<li>
意为“安装应用后，未能获取已安装应用程序的信息”。
</li>
</ul>
</li>
</ul>
<p>
也就是说，尽管应用已安装到设备（或模拟器）上，但 Xcode 未能正确确认已安装应用的信息。这可能是由于应用未完全安装成功，或 Xcode 与设备（或模拟器）之间出现了暂时的通信故障。
</p>
<h2>
产生原因
</h2>
<p>
导致该错误的原因有很多，常见的包括：
</p>
<ol>
<li>
<b>
Xcode 构建缓存问题
</b>
：Xcode 保存了之前构建的缓存，可能导致与新构建的应用产生混淆。
</li>
<li>
<b>
安装失败
</b>
：应用未能在设备上正确安装，或者在安装后获取应用信息的过程中出现了问题。
</li>
<li>
<b>
模拟器或设备问题
</b>
：有时模拟器或所连接的设备出现故障，导致 Xcode 无法正确接收安装信息。
</li>
</ol>
<h2>
解决方案：清理构建 (Clean Build)
</h2>
<p>
最简单且有效的解决方法是进行 
<b>
“清理构建 (Build Clean)”
</b>
。通过清理构建，Xcode 会清除之前的缓存，并从头开始重新构建应用，从而解决问题。
</p>
<h3>
清理构建方法
</h3>
<ol>
<li>
在 Xcode 菜单中前往 
<b>
<code>
Product
</code>
</b>
。
</li>
<li>
点击 
<b>
<code>
Clean Build Folder
</code>
</b>
。（快捷键：
<code>
Shift + Command + K
</code>
）
</li>
<li>
然后选择 
<b>
<code>
Product &gt; Build
</code>
</b>
重新构建应用。（快捷键：
<code>
Command + B
</code>
）
</li>
</ol>
<h3>
其他补充方案
</h3>
<ul>
<li>
<b>
重启模拟器
</b>
：如果清理构建后问题依旧，尝试关闭模拟器并重新启动。
</li>
<li>
<b>
重连设备
</b>
：如果是部署到真实设备，可以尝试重新连接线缆、重启设备后再进行构建。
</li>
<li>
<b>
重启 Xcode
</b>
：有时可能是 Xcode 本身出现了问题，重启 Xcode 也是一种有效的手段。
</li>
</ul>
<h2>
结论
</h2>
<p>
<b>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
</b> 
错误通常是由 Xcode 和设备之间的临时通信问题引起的。要解决该问题，可以尝试执行 
<b>
清理构建
</b>
，必要时重启模拟器或设备。这是一个比较常见的错误，但由于解决方案明确，无需过于担心。
</p>