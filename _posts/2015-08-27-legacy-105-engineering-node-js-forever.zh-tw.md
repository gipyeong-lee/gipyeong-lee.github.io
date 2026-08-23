---
layout: post
title: "[node.js] forever"
description: "最近一直在趕關於 node.js 的文章。因為想整理並分享在之前構建的 Side Effect Studio 網站中所使用的技術，所以關於 node.js 的內容一直在連續發布。得趕快整理完，然後去看看其他的東西才行。呵。去年曾經發過一篇..."
date: 2015-08-27 19:29:31 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2015-08-27-legacy-105-engineering-node-js-forever
tags:
  - "Forever"
  - "node.js"
  - "npm"
  - "Scrap"
  - "engineering"
noindex: true
translation_source_hash: ac81f4b878a4bcd35cf582e2d4364fcb94198723d58aa84d87dfeb3b0d2991ea
---

<p>
<span>
最近一直在趕關於 node.js 的文章。因為想整理並分享在之前構建的
</span>
<a href="http://sideeffect.kr/" target="_blank">
Side Effect Studio 網站
</a>
<span>
中所使用的技術，所以關於 node.js 的內容一直在連續發布。得趕快整理完，然後去看看其他的東西才行。呵。
</span>
<br>
<br>
<span>
去年曾經發過一篇名為
</span>
<a href="http://blog.outsider.ne.kr/544" target="_blank">
使用 Upstart 和 Monit 服務 node.js 應用程式
</a>
<span>
的文章，這雖然相當實用，但在管理層面上卻相當麻煩。建立 Upstart 腳本、將規則套用到 Monit 等工作，其實有點瑣碎。由於當時不知道其他替代方案，所以一直使用 Upstart 和 Monit，但在那篇文章之後，出現了一個名為
</span>
<a href="https://github.com/indexzero/forever" target="_blank">
forever
</a>
<span>
的工具，它可以管理 node 應用程式的實例。
</span>
<br>
<br>
<span>
<a href="https://github.com/indexzero/forever" target="_blank">
forever
</a>
可以使用 npm 透過
<span>
npm install forever
</span>
指令輕鬆安裝。它是一個非常方便的工具，可以透過極簡單的指令執行 node.js 建立的應用程式，並在意外終止時重新啟動，或是將 stdout 儲存為日誌檔案來進行管理。
</span>
<span>
使用之後發現，雖然有一點小 Bug，但與原本的 Upstart 和 Monit 組合相比，其易用性實在太好，所以我已經將所有 node.js 應用程式的管理都遷移到 forever 了。
</span>
<br>
<br>
</p>
<blockquote>
usage: forever [start | stop | stopall | list | cleanlogs] [options] SCRIPT [script options]
<br>
<br>
options:
<br>
start          以 daemon 方式啟動 SCRIPT
<br>
stop           停止 daemon SCRIPT
<br>
stopall        停止所有正在執行的 forever 腳本
<br>
list           列出所有正在執行的 forever 腳本
<br>
cleanlogs      [小心使用] 刪除所有歷史 forever 日誌檔案
</blockquote>
<p>
<br>
<span>
forever 的用法如上所示。
</span>
<span>
想要註冊的腳本，只需執行
<span>
forever start app.js
</span>
即可。查看處理程序時，會發現有一個獨立的 forever 處理程序，若執行的 app.js 處理程序死亡，它會自動重新啟動。若想查看目前正在執行的腳本，可以執行
<span>
forever list
</span>
。
</span>
<br>
<br>
</p>
<div class="imageblock center">
<img src="http://blog.outsider.ne.kr/attach/1/1154848314.gif.pagespeed.ce.t4pwqQMTlL.gif" alt="使用 forever 註冊 node 應用程式的畫面" height="63" width="550">
</div>
<p>
<br>
<span>
結束處理程序時，可以使用前面的編號執行
<span>
forever stop 編號
</span>
。
</span>
<span>
因為一眼就能掌握目前使用了哪些處理程序，並且會自動連接 log 檔案，所以使用起來非常方便。
</span>
<br>
<br>
</p>
<div class="imageblock center">
<img src="http://blog.outsider.ne.kr/attach/1/1122859785.gif.pagespeed.ce.brAyzYu1ox.gif" alt="結束已註冊 node 應用程式的畫面" height="57" width="550">
</div>
<p>
<br>
<br>
<br>
<span>
就目前短暫的使用經驗來看，它似乎相當穩定。（雖然因為沒什麼連線數，導致 fatal 的機率很低，所以不見得準確，純粹是感覺.. ㅡㅡ;;）不過，偶爾會出現小 Bug，比如使用 forever start 註冊應用程式時，處理程序雖然正常啟動，但卻沒有註冊到 forever 中，導致在列表中看不到。儘管測試了多次，但還是沒找到規律。這種時候，必須強制終止該腳本及其對應的 forever 處理程序後重新註冊。除了這點之外，無論是管理還是使用都非常方便，真的很好。
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
出處 :
<a href="http://blog.outsider.ne.kr/590" target="_blank" class="tx-link">
</a>
</span>
<font>
<span>
<a href="http://blog.outsider.ne.kr/590" target="_blank" class="tx-link">
http://blog.outsider.ne.kr/590
</a>
</span>
</font>
</p>