---
layout: post
title: "[短期] 03. Chrome Extension 與 Facebook API"
description: "短期專案進行已經過 10 天了。專案的大致架構已經出來。但是，卻面臨了在 Chrome Extension 中無法串接 Facebook API 的情況。啊... 真希望趕快解決... 救救我... 總算暫時解決了..."
date: 2015-02-05 02:33:56 +0900
section: blog
category: projects
lang: zh-tw
ref: 2015-02-05-legacy-10-projects-03-chrome-extension-facebook-api
tags:
  - "TJSSM"
  - "projects"
translation_source_hash: 80338712f51174b212388d9ff4a585d28b8759098ed5ad22d4f4e21259ec3414
---

<p>
短期專案進行已經過 10 天了。
</p>
<p>
專案的大致架構已經出來。
</p>
<p>
但是，卻面臨了在 Chrome Extension 中無法串接 Facebook API 的情況。
</p>
<p>
啊... 真希望趕快解決... 救救我...
</p>

<p>
總算暫時解決了。
</p>
<p>
並沒有另外進行 Facebook 登入。（根據 Google 搜尋的結果）有人分析了 Facebook 查詢並上傳了內容。
</p>
<p>
我只抓取了該部分進行處理。
</p>

<p>
以下是處理結果。
</p>







<p>
另外，從既有成員南斗鉉（音譯）先生那裡獲得了關於提取文章內縮圖資訊的方法。
</p>
<p>
明天打算進行利用文章連結提取文章縮圖的部分。
</p>

<p>
預計按照以下順序進行。
</p>

<p>
1. HTML 解析
</p>
<p>
2. 透過 Meta 標籤分析獲取字元編碼 ( UTF-8, EUC-KR ... etc )
</p>
<p>
3. 使用該字元編碼重新解析
</p>
<p>
4. 透過正規表示式移除 &lt;script&gt;、&lt;style&gt;
</p>
<p>
5. 透過正規表示式移除 &lt;body&gt; 內的 &lt;h2&gt;、&lt;span&gt;、&lt;p&gt;
</p>
<p>
6. 在乾淨的 body 內，儲存文字區塊與其長度
</p>
<p>
7. 排序
</p>
<p>
8. 從排序後的文字中，將突然變少的部分開始全部刪除
</p>
<p>
9. 尋找文字較多的區塊附近的 img 標籤並取得 href 值
</p>

<p>
以上是理論上...
</p>

<p>
明天一定要試試看...
</p>

<p>
P.S. 我發現自己對 Chrome Extension 的理解度非常不足。嘗試直接將既有的 Facebook API 貼到 Extension 時，被 CSP 擋住了... 感覺我盯著下面這段話分析了兩個小時。
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
Content Security Policy directive: "script-src 'self' chrome-extension-resource:".
</span>
</p>

<p>
結果確認該部分無法直接使用...
</p>
<p>
關於 Facebook 登入，我現在還是不太清楚。如果有誰知道的話... 麻煩留言指教。 (_ _)
</p>
<p>
非常感謝。
</p>

<p>
咦...
</p>
<span class="txt_fold">
展開
</span>
<div class="moreless_content">
<p>
早上起床後，帶著渾渾噩噩的精神重新看了 Google 文件。
</p>

<p>
<span>
<a href="https://developer.chrome.com/apps/contentSecurityPolicy#H3-1" target="_blank" class="tx-link">
How to comply with CSP
</a>
</span>
</p>
<p>
（如何遵守內容安全政策）
</p>

<p>
首先為了遵守規定，必須了解 Google 擴充功能的 CSP 是什麼。
</p>
<p>
我竟然沒看到就寫在下面。
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
What is the CSP for Chrome Apps?
</span>
</p>
<div>
<br>
</div>
<p>
The content security policy for Chrome Apps restricts you from doing the following:
</p>
<ul>
<li>
You can’t use inline scripting in your Chrome App pages. The restriction bans both &lt;script&gt; blocks and event handlers (&lt;button onclick="..."&gt;).
</li>
<li>
You can’t reference any external resources in any of your app files (except for video and audio resources). You can’t embed external resources in an iframe.
</li>
<li>
You can’t use string-to-JavaScript methods like
<code>
eval()
</code>
and
<code>
new Function()
</code>
.
</li>
</ul>

<p>
整理以上內容如下：
</p>

<p>
_Chrome App 的內容安全政策。
</p>
<p>
1. 不能在 HTML 頁面使用 inline scripting。
</p>
<p>
2. 不能參照任何外部資源。此外，也不能在 iframe 內插入外部資源。
</p>
<p>
3. 無法使用將字串函數化的 eval() 等函數。
</p>

<p>
啊... 結果是被強制要求只能使用內部數據。看得出有從根源上封鎖 XSS 漏洞的努力。
</p>
<p>
搜尋 XSS 時，出現了很多關於網頁駭客攻擊的資訊。
</p>

<p>
然後看下面...
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
Your Chrome App can only refer to scripts and objects within your app, with the exception of media files (apps can refer to video and audio outside the package). Chrome extensions will let you relax the default Content Security Policy; Chrome Apps won’t.
</span>
</p>

<p>
幸好...
<span>
雖然說 Chrome 擴充功能可以放寬，但 Chrome App 卻說沒這種事。
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
All JavaScript and all resources should be local (everything gets packaged in your Chrome App).
</span>
</p>

<p>
建議所有 JavaScript 或所有資源都應該是本地數據。
</p>

<p>
那麼真的真的沒有方法可以使用外部資源嗎...
</p>
<p>
往下看還有...
</p>


<h3 class="has-permalink">
Use templating libraries
</h3>
<p>
Use a library that offers precompiled templates and you’re all set. You can still use a library that doesn’t offer precompilation, but it will require some work on your part and there are restrictions.
</p>
<p>
You will need to use sandboxing to isolate any content that you want to do ‘eval’ things to. Sandboxing lifts CSP on the content that you specify. If you want to use the very powerful Chrome APIs in your Chrome App, your sandboxed content can't directly interact with these APIs (see
<a href="https://developer.chrome.com/apps/app_external#sandboxing">
Sandbox local content
</a>
).
</p>
<h3 class="has-permalink">
Access remote resources
</h3>
<p>
You can fetch remote resources via
<code>
XMLHttpRequest
</code>
and serve them via
<code>
blob:
</code>
,
<code>
data:
</code>
, or
<code>
filesystem:
</code>
URLs (see
<a href="https://developer.chrome.com/apps/app_external#external">
Referencing external resources
</a>
).
</p>
<p>
Video and audio can be loaded from remote services because they have good fallback behavior when offline or under spotty connectivity.
</p>
<h3 class="has-permalink">
Embed web content
</h3>
<p>
Instead of using an iframe, you can call out to an external URL using a webview tag (see
<a href="https://developer.chrome.com/apps/app_external#webview">
Embed external web pages
</a>
).
</p>

<p>
竟然有三種方法。
</p>

<p>
1. 利用 Sandbox 與 Chrome API 進行主頁面與沙盒頁面的交流
</p>
<p>
2. 透過 XMLHttpRequest 使用 blob 等參照外部資源。（腳本似乎不行）
</p>
<p>
3. 使用 iframe 處理。
</p>

<p>
理論上寫著利用這三種方法可以進行外部資源參照。
</p>
<p>
不過，關於能否使用外部腳本的部分沒有提到，所以我不太清楚。
</p>
<p>
以後有機會的話，會試著利用這三種方式嘗試是否能從外部匯入腳本。
</p>

<p>
現在因為還有下一個目標，所以 Pass...
</p>

</div>