---
layout: post
title: "[Short-term] 03. Chrome Extension and Facebook API"
description: "It has already been 10 days since the short-term project began. A rough outline of the project is out. However, I faced a situation where I couldn't integrate the Facebook API into the Chrome Extension. Ah... I hope this gets resolved... Please save me... I have solved it for now..."
date: 2015-02-05 02:33:56 +0900
section: blog
category: projects
lang: en
ref: 2015-02-05-legacy-10-projects-03-chrome-extension-facebook-api
tags:
  - "TJSSM"
  - "projects"
translation_source_hash: 80338712f51174b212388d9ff4a585d28b8759098ed5ad22d4f4e21259ec3414
---

<p>
It has already been 10 days since the short-term project began.
</p>
<p>
A rough outline of the project is out.
</p>
<p>
However, I faced a situation where I couldn't integrate the Facebook API into the Chrome Extension.
</p>
<p>
Ah... I hope this gets resolved... Please save me...
</p>

<p>
I have solved it for now.
</p>
<p>
I did not do Facebook login separately. (Following a Google search) Someone had analyzed Facebook queries and uploaded them.
</p>
<p>
I only brought in and processed that part.
</p>

<p>
The following is the result of the processing.
</p>

<p>
Additionally, I received information from existing member Nam Doo-hyun regarding extracting thumbnail images from articles.
</p>
<p>
Tomorrow, I plan to work on extracting the thumbnail of an article using the article link.
</p>

<p>
I plan to do it in the following order.
</p>

<p>
1. HTML parsing
</p>
<p>
2. Character set acquisition through meta tag analysis (UTF-8, EUC-KR ... etc)
</p>
<p>
3. Re-parsing with the corresponding character set
</p>
<p>
4. Removing &lt;script&gt; and &lt;style&gt; through regular expressions
</p>
<p>
5. Removing &lt;h2&gt;, &lt;span&gt;, and &lt;p&gt; through regular expressions within &lt;body&gt;
</p>
<p>
6. Saving the length of text bundles and the text bundles within the cleaned body
</p>
<p>
7. Sorting
</p>
<p>
8. Deleting everything from the point where the sorted text suddenly becomes smaller
</p>
<p>
9. Finding img tags around the text-heavy parts and getting the href values
</p>

<p>
That is the theoretical part...
</p>

<p>
I will definitely try it tomorrow...
</p>

<p>
P.s I realized that my understanding of Chrome Extensions is quite low. When trying to just attach an existing Facebook API to an extension, it gets blocked by CSP... I think I spent 2 hours analyzing the following phrase.
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
As a result, I confirmed that it cannot be attached just like that...
</p>
<p>
I still don't know much about Facebook login. If anyone happens to know, please leave a comment. (_ _)
</p>
<p>
Thank you.
</p>

<p>
Oh...
</p>
<span class="txt_fold">
Show more
</span>
<div class="moreless_content">
<p>
I woke up in the morning and reviewed the Google documentation with a blurry mind.
</p>

<p>
<span>
<a href="https://developer.chrome.com/apps/contentSecurityPolicy#H3-1" target="_blank" class="tx-link">
How to comply with CSP
</a>
</span>
</p>
<p>
(How to comply with Content Security Policy)
</p>

<p>
First, to comply, I needed to know what the CSP for Google Extensions is.
</p>
<p>
I hadn't seen what was written right below.
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
Summarizing the above, it is like this.
</p>

<p>
_Content Security Policy for Chrome Apps.
</p>
<p>
1. You cannot use inline scripting. In html pages.
</p>
<p>
2. You cannot reference any external resources. Also, you cannot insert external resources inside an iframe.
</p>
<p>
3. You cannot use functions like eval() that functionalize strings.
</p>

<p>
Ah... In the end, we are forced to use only internal data. There is an effort to fundamentally block XSS vulnerabilities.
</p>
<p>
A lot of information about web hacking appears. When searching for XSS...
</p>

<p>
And looking below...
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
Fortunately..
<span>
It says Chrome extensions allow relaxation, but Chrome Apps will not.
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
It recommends that all JavaScript and all resources be local data.
</p>

<p>
Then, is there really, truly no way to use external sources...
</p>
<p>
Looking below, there is more...
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
There are three ways.
</p>

<p>
1. Interaction between the main page and the sandboxing page using Sandbox and Chrome API
</p>
<p>
2. Referencing external resources via blob, etc., in XMLHttpRequest. (I don't think scripts will work)
</p>
<p>
3. Processing using an iframe.
</p>

<p>
In theory, it says that if you use the 3 methods, you can use external resources.
</p>
<p>
However, it doesn't mention the part about being able to use external scripts, so I'm not sure.
</p>
<p>
If I have an opportunity in the future, I will try to see if I can fetch scripts from the outside using the three methods.
</p>

<p>
For now, there is a next goal, so Pass...
</p>

</div>