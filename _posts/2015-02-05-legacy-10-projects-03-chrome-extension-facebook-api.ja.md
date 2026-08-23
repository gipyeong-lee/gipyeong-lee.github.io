---
layout: post
title: "[短期] 03. Chrome拡張機能とFacebook API"
description: "短期プロジェクトが始まって早くも10日が経過しました。プロジェクトの大まかな形はできてきましたが、Chrome拡張機能でFacebook APIを連携できないという事態に直面しました。ああ…解決してほしいです…。助けてください…。とりあえず解決はしましたが…"
date: 2015-02-05 02:33:56 +0900
section: blog
category: projects
lang: ja
ref: 2015-02-05-legacy-10-projects-03-chrome-extension-facebook-api
tags:
  - "TJSSM"
  - "projects"
translation_source_hash: 80338712f51174b212388d9ff4a585d28b8759098ed5ad22d4f4e21259ec3414
---

<p>
短期プロジェクトが始まって早くも10日が経過しました。
</p>
<p>
プロジェクトの大まかな形はできてきました。
</p>
<p>
しかし、Chrome拡張機能でFacebook APIを連携できないという事態に直面しました。
</p>
<p>
ああ…解決してほしいです…。助けてください…。
</p>

<p>
とりあえず解決はしました。
</p>
<p>
Facebookログインは別途行っていません。（ググった結果）誰かがFacebookクエリを分析して公開してくれていたので、その部分だけを持ってきて処理しました。
</p>

<p>
次は処理結果です。
</p>







<p>
さらに、既存会員のナム・ドゥヒョン会員から記事内のサムネイル画像抽出に関する情報を得ることができました。
</p>
<p>
明日は記事リンクを利用して記事のサムネイルを抽出する部分を進める予定です。
</p>

<p>
次のような順序で行う予定です。
</p>

<p>
1. HTMLパース
</p>
<p>
2. メタタグ分析による文字コードの取得（UTF-8, EUC-KR... etc）
</p>
<p>
3. その文字コードで再パース
</p>
<p>
4. 正規表現による &lt;script&gt;,&lt;style&gt; の削除
</p>
<p>
5. &lt;body&gt;内で、正規表現による &lt;h2&gt;,&lt;span&gt;,&lt;p&gt; の削除
</p>
<p>
6. きれいになったbody内で、テキスト塊の長さとテキスト塊を保存
</p>
<p>
7. ソート
</p>
<p>
8. ソートされたテキストで、急激に短くなる部分からずっと削除
</p>
<p>
9. テキストが多い部分の周辺にあるimgタグを探してhref値を取得
</p>

<p>
以上は理論的なもので…
</p>

<p>
明日、必ず試してみます…
</p>

<p>
追伸：Chrome拡張機能に対する理解度が低いことを痛感しました。既存のFacebook APIをそのまま拡張機能に組み込もうとすると、CSP（コンテンツセキュリティポリシー）にブロックされてしまい…以下の文言を2時間見つめながら分析していたようです。
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
結果として、その部分はそのままでは組み込めないことが確認できました…。
</p>
<p>
まだFacebookログインについてはよく分かりません。もしご存知の方がいらっしゃれば…コメントをお願いします。(_ _)
</p>
<p>
ありがとうございます。
</p>

<p>
おっと…
</p>
<span class="txt_fold">
もっと見る
</span>
<div class="moreless_content">
<p>
朝起きてぼーっとした頭でGoogleドキュメントを読み返しました。
</p>

<p>
<span>
<a href="https://developer.chrome.com/apps/contentSecurityPolicy#H3-1" target="_blank" class="tx-link">
How to comply with CSP
</a>
</span>
</p>
<p>
（CSPに準拠する方法）
</p>

<p>
まず準拠するためには、Google拡張機能のCSPが何であるかを知る必要がありました。
</p>
<p>
すぐ下に書かれていたことを見落としていました。
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
上記の内容を整理するとこうなります。
</p>

<p>
_Chromeアプリのコンテンツセキュリティポリシー。
</p>
<p>
1. HTMLページでインラインスクリプトを使えません。
</p>
<p>
2. いかなる外部リソースも参照できません。また、iframe内に外部リソースを挿入することもできません。
</p>
<p>
3. 文字列を関数化する eval() などの関数の使用は不可。
</p>

<p>
ああ…結局、内部のデータだけを使うよう強要されています。XSS脆弱性を根本から封じ込めようとする努力が見えます。
</p>
<p>
ウェブハッキングに関する情報が多く出てきますね。XSSで検索すると…。
</p>

<p>
そして下を見ると…
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
幸い…
<span>
Chrome拡張機能は緩和されますが、Chromeアプリはそうなることはないと言っています。
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
すべてのJavaScriptやリソースはローカルにあることを推奨していますね。
</p>

<p>
では、本当に外部ソースを使用する方法はないのか…。
</p>
<p>
下を見るとまたあります…。
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
3つもありますね。
</p>

<p>
1. SandboxとChrome APIを利用したメインページとサンドボックスページの交流
</p>
<p>
2. XMLHttpRequestでの blob 等を通じた外部リソース参照。（スクリプトはダメそうです）
</p>
<p>
3. iframeを使用して処理する。
</p>

<p>
理論上は、この3つを利用すれば外部リソースが使用可能だと書かれています。
</p>
<p>
しかし、外部スクリプトを使える部分については言及されていないのでよく分かりません。
</p>
<p>
後日機会があれば、3つの方式を利用してスクリプトを外部から持ち込めるか試してみます。
</p>

<p>
今は次のゴールがあるのでパス…
</p>

</div>