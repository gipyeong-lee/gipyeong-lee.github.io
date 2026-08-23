---
layout: post
title: "[node.js] forever"
description: "最近一直在赶关于 node.js 的文章。因为想整理和分享一下之前构建 Side Effect Studio 网站时使用的一些东西，所以关于 node.js 的文章接连不断地上传了。得赶紧整理完，看看别的东西了。呵。去年..."
date: 2015-08-27 19:29:31 +0900
section: blog
category: engineering
lang: zh-cn
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
最近一直在赶关于 node.js 的文章。因为想整理和分享一下之前构建
</span>
<a href="http://sideeffect.kr/" target="_blank">
Side Effect Studio 网站
</a>
<span>
时使用的一些东西，所以关于 node.js 的文章接连不断地上传了。得赶紧整理完，看看别的东西了。呵。
</span>
<br>
<br>
<span>
去年我曾经发布过一篇名为
</span>
<a href="http://blog.outsider.ne.kr/544" target="_blank">
使用 Upstart 和 Monit 服务 node.js 应用
</a>
<span>
的文章，虽然这相当有用，但在管理层面却相当麻烦。制作 Upstart 脚本、应用 Monit 规则等工作稍微有点繁琐。因为当时不知道别的替代方案，所以一直使用 Upstart 和 Monit，但那篇文章之后，出现了一个能够管理 node 应用实例的工具，名为
</span>
<a href="https://github.com/indexzero/forever" target="_blank">
forever
</a>
<span>
。
</span>
<br>
<br>
<span>
<a href="https://github.com/indexzero/forever" target="_blank">
forever
</a>
可以使用 npm 通过
<span>
npm install forever
</span>
命令轻松安装，它是一个通过非常简单的命令来执行用 node.js 编写的应用程序，并在意外终止时重新运行，或者将 stdout 保存为日志文件进行管理的工具。
</span>
<span>
试用后发现，虽然存在一些 bug，但与现有的 Upstart 和 Monit 组合相比，可用性太方便了，所以 node.js 应用的管理全都换成了 forever。
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
start          start SCRIPT as a daemon
<br>
stop           stop the daemon SCRIPT
<br>
stopall        stop all running forever scripts
<br>
list           list all running forever scripts
<br>
cleanlogs      [CAREFUL] Deletes all historical forever log files
</blockquote>
<p>
<br>
<span>
forever 的使用方法如上所述。
</span>
<span>
将想要注册的脚本使用
<span>
forever start app.js
</span>
这样的方式执行即可。
</span>
<span>
观察进程可以发现，有一个关于 forever 的独立进程，如果执行的 app.js 进程死掉，它会自动重新执行。要查看当前正在运行的脚本，请执行
<span>
forever list
</span>
。
</span>
<br>
<br>
</p>
<div class="imageblock center">
<img src="http://blog.outsider.ne.kr/attach/1/1154848314.gif.pagespeed.ce.t4pwqQMTlL.gif" alt="注册 node 应用到 forever 的界面" height="63" width="550">
</div>
<p>
<br>
<span>
终止进程时，可以使用前面显示的编号，使用
<span>
forever stop 编号
</span>
即可。
</span>
<span>
一眼就能掌握当前正在使用什么进程，并且会自动连接 log 文件，使用起来非常方便。
</span>
<br>
<br>
</p>
<div class="imageblock center">
<img src="http://blog.outsider.ne.kr/attach/1/1122859785.gif.pagespeed.ce.brAyzYu1ox.gif" alt="终止已注册 node 应用的界面" height="57" width="550">
</div>
<p>
<br>
<br>
<br>
<span>
根据我稍微试用过的一些经验，感觉它相当稳定。（因为没有多少访问者，发生致命错误的可能性很小，所以这并不准确，纯粹是心理作用.. ㅡㅡ;;）相反，可能存在一些 bug，虽然用 forever start 注册了应用，进程也正常启动了，但有时没有注册到 forever 中，导致列表中没有显示。虽然测试了很多次，但没能找到任何规律。这种情况下，必须强制终止该脚本及其对应的 forever 进程，然后重新注册。除了这一点之外，管理和使用都非常方便，真的很好。
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
参考资料 :
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