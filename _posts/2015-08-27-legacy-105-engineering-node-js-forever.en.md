---
layout: post
title: "[node.js] forever"
description: "I've been posting a lot about node.js lately. As I was organizing and sharing some of the things I used on the Side Effect Studio site that I built a while ago, it seems like the posts have been focused exclusively on node.js. I need to finish organizing everything quickly and look into other things as well. Haha. Last year..."
date: 2015-08-27 19:29:31 +0900
section: blog
category: engineering
lang: en
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
I've been posting a lot about node.js lately. As I was organizing and sharing some of the things I used on the
</span>
<a href="http://sideeffect.kr/" target="_blank">
Side Effect Studio
</a>
<span>
site that I built a while ago, it seems like the posts have been focused exclusively on node.js. I need to finish organizing everything quickly and look into other things as well. Haha.
</span>
<br>
<br>
<span>
Last year, I posted an article titled 
</span>
<a href="http://blog.outsider.ne.kr/544" target="_blank">
Serving node.js Applications with Upstart and Monit
</a>
<span>
, which is quite useful, but it can be rather annoying from a management perspective. Tasks like creating Upstart scripts and applying rules in Monit are a bit tedious. Since I wasn't aware of any other alternatives, I had been using Upstart and Monit, but after that post, a tool called 
</span>
<a href="https://github.com/indexzero/forever" target="_blank">
forever
</a>
<span>
, which manages instances of node apps, was released.
</span>
<br>
<br>
<span>
<a href="https://github.com/indexzero/forever" target="_blank">
forever
</a>
can be easily installed using npm with the command 
<span>
npm install forever
</span>
, and it is a tool that manages node.js apps by running them with very simple commands, restarting them if they unexpectedly terminate, and saving stdout to log files.
</span>
<span>
Having used it, while it does have some minor bugs, it is so much more convenient than the existing Upstart and Monit combination that I have switched entirely to 
forever
 for managing all my node.js apps.
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
The usage of 
forever
 is as shown above.
</span>
<span>
To register a script you want to run, simply execute it like 
<span>
forever start app.js
</span>
.
</span>
<span>
If you check the processes, you will see a separate process for 
forever
, which will automatically restart the 
app.js
 process if it dies. To see the scripts currently running, you can execute 
<span>
forever list
</span>
.
</span>
<br>
<br>
</p>
<div class="imageblock center">
<img src="http://blog.outsider.ne.kr/attach/1/1154848314.gif.pagespeed.ce.t4pwqQMTlL.gif" alt="Screen showing a node app registered with forever" height="63" width="550">
</div>
<p>
<br>
<span>
To terminate a process, you can use 
<span>
forever stop [index]
</span>
using the index shown in the list.
</span>
<span>
It is very convenient to use because you can grasp which processes are currently running at a glance, and it automatically connects log files.
</span>
<br>
<br>
</p>
<div class="imageblock center">
<img src="http://blog.outsider.ne.kr/attach/1/1122859785.gif.pagespeed.ce.brAyzYu1ox.gif" alt="Screen showing a registered node app terminated" height="57" width="550">
</div>
<p>
<br>
<br>
<br>
<span>
Based on my brief experience, it seems fairly stable. (Since I don't have that much traffic, the probability of a fatal error is low, so this isn't definitive, just a feeling.. ㅡㅡ;;) However, there seems to be a minor bug where an app registered with 
forever start
 successfully spawns the process, but it isn't registered in 
forever
 and doesn't appear in the list. I tested this several times but couldn't find a pattern. In such cases, you must forcibly terminate the corresponding script and the 
forever
 process and register it again. Other than this, it's really great because both management and usage are very convenient.
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
Source :
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