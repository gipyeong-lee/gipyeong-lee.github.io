---
layout: post
title: "[短期] 03. Chrome Extension 与 Facebook API"
description: "短期项目进展已经过去10天了。项目的基本框架已经出来了。但是，却遇到了无法在 Chrome Extension 中连接 Facebook API 的情况。啊... 真希望能解决... 救命啊... 暂时是先解决了..."
date: 2015-02-05 02:33:56 +0900
section: blog
category: projects
lang: zh-cn
ref: 2015-02-05-legacy-10-projects-03-chrome-extension-facebook-api
tags:
  - "TJSSM"
  - "projects"
translation_source_hash: 80338712f51174b212388d9ff4a585d28b8759098ed5ad22d4f4e21259ec3414
---

<p>
短期项目进展已经过去10天了。
</p>
<p>
项目的基本框架已经出来了。
</p>
<p>
但是，却遇到了无法在 Chrome Extension 中连接 Facebook API 的情况。
</p>
<p>
啊... 真希望能解决... 救命啊...
</p>

<p>
暂时是先解决了。
</p>
<p>
我没有单独做 Facebook 登录。（通过谷歌搜索）发现有人分析并上传了 Facebook 查询。
</p>
<p>
我只提取并处理了那一部分。
</p>

<p>
以下是处理结果。
</p>







<p>
另外，从现有的会员南斗贤（音译）会员那里获得了关于提取文章内缩略图图像的信息。
</p>
<p>
明天计划进行利用文章链接提取文章缩略图的部分。
</p>

<p>
计划按以下顺序进行。
</p>

<p>
1. HTML 解析
</p>
<p>
2. 通过分析 Meta 标签获取字符集（UTF-8, EUC-KR ... 等）
</p>
<p>
3. 使用相应的字符集重新解析
</p>
<p>
4. 通过正则表达式删除 &lt;script&gt; 和 &lt;style&gt;
</p>
<p>
5. 在 &lt;body&gt; 内通过正则表达式删除 &lt;h2&gt;、&lt;span&gt;、&lt;p&gt;
</p>
<p>
6. 在变得干净的 body 内，保存文本块的长度和文本块
</p>
<p>
7. 排序
</p>
<p>
8. 从排序后的文本中，从突然变少的部分开始一直删除
</p>
<p>
9. 查找文本较多的部分周围的 img 标签并获取 href 值
</p>

<p>
以上是理论上的东西...
</p>

<p>
明天一定要尝试一下...
</p>

<p>
P.s 我发现我对 Chrome Extension 的理解程度很低。如果试图直接在 Extension 中附加现有的 Facebook API，会被 CSP 拦截... 我盯着下面的文字分析了2个小时。
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
结果确认了该部分不能直接附加...
</p>
<p>
关于 Facebook 登录我还不怎么清楚。如果有人知道的话... 请留言评论。 (_ _)
</p>
<p>
非常感谢。
</p>

<p>
哎呀...
</p>
<span class="txt_fold">
查看更多
</span>
<div class="moreless_content">
<p>
早上起床后，带着模糊的头脑重新看了谷歌文档。
</p>

<p>
<span>
<a href="https://developer.chrome.com/apps/contentSecurityPolicy#H3-1" target="_blank" class="tx-link">
How to comply with CSP
</a>
</span>
</p>
<p>
（遵守 Content Security Policy 的方法）
</p>

<p>
首先，为了遵守它，需要了解谷歌扩展程序的 CSP 是什么。
</p>
<p>
刚才没看到写在下面的内容。
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
总结一下上面的内容如下：
</p>

<p>
_Chrome App 的内容安全策略。
</p>
<p>
1. 不能在 HTML 页面中使用内联脚本（inline scripting）。
</p>
<p>
2. 不能引用任何外部资源。此外，也不能在 iframe 中插入外部资源。
</p>
<p>
3. 不能使用将字符串函数化的 eval() 等函数。
</p>

<p>
啊... 最终被强制只能使用内部数据。能看出想要从根本上封锁 XSS 漏洞的努力。
</p>
<p>
搜索 XSS 时会出现很多关于 Web 黑客攻击的信息...
</p>

<p>
然后看下面...
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
幸运的是...
<span>
虽然说 Chrome 扩展程序可以放宽，但 Chrome App 是绝对不会的。
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
建议所有 JavaScript 或所有资源都应该是本地数据。
</p>

<p>
那么，真的真的没有使用外部资源的方法吗...
</p>
<p>
看下面还有...
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
看来有三种方法。
</p>

<p>
1. 利用 Sandbox 和 Chrome API 进行主页面与沙盒页面的交流
</p>
<p>
2. 通过 XMLHttpRequest 中的 blob 等引用外部资源。（脚本好像不行）
</p>
<p>
3. 使用 iframe 进行处理。
</p>

<p>
理论上写着利用这三种方式可以使用外部资源。
</p>
<p>
但是，关于可以使用外部脚本的部分没有提及，所以不太清楚。
</p>
<p>
以后有机会的话，我会尝试利用这三种方式看看是否能从外部获取脚本。
</p>

<p>
现在有下一个目标，所以先跳过...
</p>

</div>