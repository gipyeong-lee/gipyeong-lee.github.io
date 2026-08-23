---
layout: post
title: "Xcode 錯誤：failedToGetInstalledApplicationInfoAfterInstalling"
description: "在開發 iOS App 的過程中，開發者可能會遇到各種錯誤。其中之一就是 failedToGetInstalledApplicationInfoAfterInstalling。這個錯誤通常發生在 App 安裝後，Xcode 無法獲取該 App 的安裝資訊時..."
date: 2019-10-20 09:52:28 +0900
section: blog
category: web3
lang: zh-tw
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
在開發 iOS App 的過程中，開發者可能會遇到各種錯誤。其中之一就是 
<b>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code>
</b> 
這個錯誤。該錯誤通常發生在 App 安裝後，Xcode 無法獲取該 App 的安裝資訊時。本文將為您簡單說明此錯誤的原因與解決方法。
</p>
<h2>
錯誤說明
</h2>
<p>
若拆解該錯誤訊息，其含義如下：
</p>
<ul>
<li>
<code>
failedToGetInstalledApplicationInfoAfterInstalling
</code> 
：
<ul>
<li>
意指「安裝 App 後，在獲取已安裝應用程式資訊的過程中失敗」。
</li>
</ul>
</li>
</ul>
<p>
換句話說，儘管 App 已安裝至裝置（或模擬器）上，Xcode 卻無法正確確認該已安裝 App 的資訊。這可能是由於 App 未能正確安裝，或是 Xcode 與裝置（或模擬器）之間存在臨時性的通訊問題所導致。
</p>
<h2>
發生原因
</h2>
<p>
此錯誤可能由多種原因引起，常見的起因如下：
</p>
<ol>
<li>
<b>
Xcode 建置快取問題
</b>
：Xcode 保留了舊的建置快取，可能與新編譯的 App 產生混淆。
</li>
<li>
<b>
安裝錯誤
</b>
：App 未能正確安裝至裝置，或是在安裝後讀取 App 資訊的過程中發生問題。
</li>
<li>
<b>
模擬器或裝置問題
</b>
：模擬器或連接的實體裝置偶爾會發生錯誤，導致 Xcode 無法正常接收安裝資訊。
</li>
</ol>
<h2>
解決方案：清除建置 (Clean Build)
</h2>
<p>
最簡單且有效的解決方案是進行 
<b>
「清除建置 (Build Clean)」
</b>
。透過執行清除建置，Xcode 會移除舊有的快取，並重新從零開始編譯 App，藉此解決問題。
</p>
<h3>
清除建置的方法
</h3>
<ol>
<li>
前往 Xcode 選單中的 
<b>
<code>
Product
</code>
</b>
。
</li>
<li>
點擊 
<b>
<code>
Clean Build Folder
</code>
</b>
。（快捷鍵：
<code>
Shift + Command + K
</code>
）
</li>
<li>
接著再次選擇 
<b>
<code>
Product > Build
</code>
</b> 
重新編譯 App。（快捷鍵：
<code>
Command + B
</code>
）
</li>
</ol>
<h3>
其他補充解決方案
</h3>
<ul>
<li>
<b>
重新啟動模擬器
</b>
：如果執行清除建置後問題依舊，請嘗試關閉並重新啟動模擬器。
</li>
<li>
<b>
重新連接裝置
</b>
：若是部署至實體裝置，可以嘗試重新插拔傳輸線，或是重啟裝置後再次執行建置。
</li>
<li>
<b>
重新啟動 Xcode
</b>
：有時問題出在 Xcode 本身，重新啟動 Xcode 也是一個解決方法。
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
錯誤主要是由 Xcode 與裝置之間的臨時通訊問題所引起。要解決此問題，可以嘗試 
<b>
清除建置
</b>
，必要時重啟模擬器或裝置。雖然這個問題相對常見，但由於解決方法很明確，無需過度擔憂。
</p>