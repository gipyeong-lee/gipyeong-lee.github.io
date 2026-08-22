---
layout: post
title: "[PHP] All PHP Framework Suck !!!"
description: "PHP Frameworks Day PHP Frameworks day is an event that took place in Kiev, Ukraine, last October. It is an event with talks about different frameworks. I onl..."
date: 2015-08-06 15:27:11 +0900
section: blog
category: engineering
lang: ko
ref: 2015-08-06-legacy-69-engineering-php-all-php-framework-suck
tags:
  - "php"
  - "프레임웍"
  - "Rasmus"
  - "Scrap"
  - "engineering"
noindex: true
---

<h2>
PHP Frameworks Day
</h2>
<p>
<a href="http://frameworksdays.com/" rel="nofollow">
PHP Frameworks day
</a>
is an event that took place in Kiev, Ukraine, last October. It is an event with talks about different frameworks.
</p>
<p>
I only became aware of it now thanks to
<a href="https://twitter.com/phpquickfix" rel="nofollow">
PHP Quick Fix
</a>
stream of news that Chris Cornutt (AKA enygma) of PHPDeveloper.org fame puts together. Thanks Chris.
</p>
<h2>
<span>
<img src="http://files.phpclasses.org/files/blog/file/Rasmus-Lerdorf.jpg" alt="Rasmus Lerdorf http://en.wikipedia.org/wiki/File:Wikirl.jpg" title="Rasmus Lerdorf http://en.wikipedia.org/wiki/File:Wikirl.jpg" width="120" height="114">
</span>
Why All PHP Frameworks Suck
</h2>
<p>
Rasmus Lerdorf, the PHP creator, was invited to give a talk in PHP Frameworks Day conference. He talked mostly about the latest PHP developments, but for me the most interesting part was the question and answers section.
</p>
<p>
Among other things, somebody asked Rasmus about his opinion on the PHP frameworks. That was as straight question about his opinion, so Rasmus gave a straight answer (near 31m 47s): "They (PHP frameworks) All suck!"
</p>
<p>
<span class="media-container">
<iframe width="560" height="315" src="http://www.youtube.com/embed/anr7DQnMMs0" frameborder="0" allowfullscreen="">
</iframe>
</span>
</p>
<p>
It may seem odd that a guest speaker goes to a PHP frameworks conference telling all of them suck. However, the audience seemed to have enjoyed the answer. Anyway, Rasmus went into more detail about what he meant.
</p>
<h3>
1. Frameworks Execute The Same Code Repeatedly Without Need
</h3>
<p>
Rasmus clarified that all frameworks that are for general purposes are not optimized for everbody's needs.
</p>
<p>
A more specific complaint was that the solutions that frameworks offer lead to executing needless PHP code repeatedly in every HTTP request. The example that Rasmus gave is that in every request frameworks check the database type the application is using to load the respective database access class. Since the database type does not change after an application is deployed, he sees this as a waste.
</p>
<p>
While I agree with Rasmus, I think this example is not very compelling because checking the configuration to decide which database access class to load takes a very small fraction of time, especially when compared for instance with executing database queries, which usually take many milliseconds and sometimes take a few seconds to run.
</p>
<p>
A better example of this problem is when frameworks need to read configuration files to define load the actual configuration values.
</p>
<p>
Often frameworks read configuration from INI files. PHP has built-in functions to load and parse INI files. Despite you can do it all with a single function, reading a INI file and parse it takes some time that is usually way more than checking the parsed configuration values.
</p>
<p>
If your framework reads and parses configuration values from files in other formats that PHP does not have built-in support, like for instance YAML or XML, things get worse because the frameworks have to do the parsing in pure PHP code. That is much slower than the C code of the PHP engine that parses INI files.
</p>
<p>
A better alternative is to have configuration values defined in PHP script files. Just put the configuration values in PHP scripts that assign the values to variables.
</p>
<p>
When you use a PHP caching extension, PHP scripts are only compiled once. On a second run, PHP scripts compiled into opcodes are loaded from RAM. That is much faster than loading configuration from files.
</p>
<h3>
2. Frameworks Require Too Many Interdependent Classes
</h3>
<p>
Another point that Rasmus mentions is that sometimes you need only specific parts of a frameworks, but since the framework classes have too many dependencies between each other, you need to load too many classes even when you use simple features of the framework.
</p>
<p>
While this is true to a certain degree, I have seen efforts from certain framework developers to reduce the dependencies between distinct components. Still there are often dependencies between many frameworks classes that sometimes do not aggregate anything to an application with specific needs.
</p>
<p>
To address this problem some developers need to change the frameworks to strip the needless parts that add overhead. This causes a maintenance nightmare because they need to do that every time they want to upgrade to a newer version of a framework they started to adapt for their needs.
</p>
<p>
Rasmus suggests using frameworks optimized for specific purposes to avoid this problem. He recommends using for instance Wordpress or Drupal if you just want to publish a blog.
</p>
<p>
Alternatively Rasmus suggests that frameworks provide a means to let the developers push to production just a small subset of the components that are needed in each application.
</p>
<p>
This solution is too general. Rasmus did not get to the way certain frameworks implement things and so he did not comment on why certain frameworks need so many components.
</p>
<p>
For instance many frameworks rely on runtime ORMs (Object Relational Mapping). These are components that let developers define how to query databases treating information as objects, rather than tables of records.
</p>
<p>
Object orientation is fine for abstracting problems and encapsulating solutions into classes of objects, but the way certain ORMs work adds too much needless overhead.
</p>
<p>
The developer has to write code to dynamically specify the class variables (tables fields), condition clauses, object relationtionships (table joins), etc... to compose the actual query at runtime. This adds a lot of overhead because the queries that are executed are the same on every request, apart from some parameter values that may vary.
</p>
<p>
There is a better solution that avoids this overhead. Instead of dynamically composing queries at runtime, just have a separate tool that generates PHP code for the ORM classes. The generated classes already have the compiled SQL queries to execute without further overhead at runtime.
</p>
<p>
I have been using this approach since 2002 when I developed a ORM tool named
<a href="http://www.meta-language.net/metastorage.html" rel="nofollow">
Metastorage
</a>
. It does exactly what I described above. I define in project file the objects, variables, relationships and functions that I need to apply on objects.
</p>
<p>
Metastorage processes my objects definitions and generates ORM classes that execute the necessary queries at runtime just by calling the classes functions. No query building is done at runtime.
</p>
<h3>
3. Needlessly Complicated Solutions
</h3>
<p>
One thing that Rasmus did not mention directly is about the complicated solutions that frameworks tend to push.
</p>
<p>
That is the case for instance of application version migrations. Some frameworks have copied the concept of migrations from Ruby On Rails. This means that you have to write code to change your database schema between different application versions.
</p>
<p>
This is another thing that Metastorage addresses in a more efficient and less painful way for developers. Metastorage generates database table schema definitions in a separate file from my object definitions. It generates an installation class that installs the database tables on the first time.
</p>
<p>
If I change the object definitions, the installation class can also upgrade the schema with the newer definitions without destroying any data already inserted in the database tables.
</p>
<p>
This certainly makes development much faster and application upgrades less error prone because the tool always generates correct code to upgrade the database schema. When you write migrations code by hand, you may make mistakes that make you spend more time and effort to fix.
</p>
<h3>
4. Duplicating the Web Server Functionality
</h3>
<p>
Another aspect that Rasmus did not mention directly is related with aspects that frameworks sometimes require that PHP code redoes work that the Web Server already has done.
</p>
<p>
For instance, routing is the processes of assigning some code (a controller) to handle requests with different URL patterns. Many frameworks push applications to use the
<a href="http://en.wikipedia.org/wiki/Front_Controller_pattern" rel="nofollow">
front controller pattern
</a>
. The front controller analyzes the request URL and load a specific controller to actually handle the request.
</p>
<p>
The matter here is that the Web server already does this. It can match the request URL against configuration (for instance of mod_rewrite or similar) and execute the appropriate PHP script.
</p>
<p>
When you make PHP handle the routing process, you are adding needless overhead to perform a task that is the same for every request with the same URL pattern. This falls into Rasmus complaint of frameworks that execute the same code repeatedly to the reach the same outcome.
</p>
<p>
This seems to be yet another bad influence that PHP frameworks got from Ruby On Rails and Java. With those languages the Web server forwards the request to an application server.
</p>
<p>
PHP does not need to work this way because it always runs integrated with the Web server, so there is no point duplicating the Web server functionality in a way that is slower and adds more overhead.
</p>
<h2>
Other Questions
</h2>
<p>
In the same conference Rasmus also answered other interesting questions that I think it is worth commenting.
</p>
<h3>
Dropping APC in Favour of Zend Opcode Cache
</h3>
<p>
This is a topic that we have discussed several times in the
<a href="http://www.phpclasses.org/blog/category/podcast/">
Lately in PHP podcast
</a>
. Rasmus explained that PHP needed to adopt one opcode cache that would follow the latest PHP developments on every new release.
</p>
<p>
There are several opcode caches. Rasmus decided to give up on APC in favour of Zend's solution because it is more mature and faster. That required Zend to make their solution Open Source.
</p>
<p>
Curiously the maintainer of the now official PHP opcode cache is Dmitry Stogov. He was the original developer of the Turck MMCache that Zend hired to work on their on cache extension some years ago.
</p>
<p>
All is well when it ends well. Too bad that PHP took all this time to have an official caching extension. The lack of an official extension made PHP look bad in many benchmarks that in the past favored other languages.
</p>
<h3>
Compiling PHP into Binary Code
</h3>
<p>
Someone asked if PHP will have a solution for protecting code by compiling it into some form of binary.
</p>
<p>
Rasmus stated that PHP will never have that kind of solution built-in. He justifies to the fact that Zend (and other companies) provide solutions for that but it is easy relatively to break them. So he would rather not take part of that game.
</p>
<p>
While this is true, Rasmus is just considering solutions that merely compile PHP into opcodes and encrypt the result. This is a solution that is really not so hard to break by hackers.
</p>
<p>
However there are better solutions that consist in compiling the result code into native assembly machine code. While it is always possible to decompile machine code, it is much hard to reverse engineer it to PHP code that is useful enough to be understood by people that wants to steal work or change it in some useful way.
</p>
<p>
One concern that many developers that look for copy protection solutions of PHP code, is that somebody with access to the servers where the code is installed, changes the code easily.
</p>
<p>
I have seen many times developers that work for customers and those customers just go there and change their code without the knowledge of the developers. This creates maintenance headaches. Sometimes customers complain about code that is not working well because in reality they changed the code. So a solution to make it harder to view or change installed code would help.
</p>
<p>
For those cases, nowadays developers can minimize that problem by creating
<a href="http://www.php.net/phar" rel="nofollow">
PHAR
</a>
archives. These are binary archives that contain one or more PHP scripts. While PHAR archives are not really a copy protection solution, at least they would make it harder for customers that want to poke on the developers code.
</p>
<h3>
$ Dollar Sign in PHP variables
</h3>
<p>
When asked about why variables start with the $ sign, he explained that was meant to be able to insert variables inside literal string values, so a mark would need to be used to distinguish what is a variable from the rest of the string.
</p>
<p>
Since he wanted the variables to look the same inside and outside a string, he has chosen the $ sign to start variables, inspired in the solution that Perl also adopted.
</p>
<h3>
Node.js and Non-Blocking I/O
</h3>
<p>
When asked if PHP would support non-blocking I/O programming, Rasmus explained that you can do that already with the
<a href="http://pecl.php.net/package/libevent" rel="nofollow">
libevent
</a>
extension. But for that kind of programming Rasmus would prefer writing code in the
<a href="http://golang.org/" rel="nofollow">
Go language
</a>
.
</p>
<p>
Anyway, unfortunately asynchronous (non-blocking I/O) programming done with for instance Node.js is not very pleasant because it requires handling everything in nested callbacks.
</p>
<p>
Nested code in callbacks leads to very frustrating problems like for instance not being able to break from a while loop when you are inside a callback function. This is a topic that we discussed several times in the
<a href="http://www.jsclasses.org/blog/post/44-Faster-JavaScript-with-asmjs--Lately-in-JavaScript-podcast-episode-28.html">
Lately in JavaScript podcast
</a>
.
</p>
<h3>
Unicode and JIT on PHP 7
</h3>
<p>
When asked about the plans for future PHP versions, Rasmus commented that he learned from the PHP 6 Unicode support failure that it was a goal that was too ambitious. So he expects that PHP evolves in smaller hops.
</p>
<p>
Two goals he thinks are too ambitious but will eventually be implemented maybe in PHP 7 are the native support to Unicode based on a simpler approach than ICU, and a JIT compilation engine probably based on Google V8 or Facebook HHVM.
</p>
<h2>
Conclusion
</h2>
<p>
Rasmus interview was very interesting because it makes us reflect on the way we are doing things in PHP that may be less than ideal, especially when you use general purpose frameworks.
</p>
<p>
Whether you agree or disagree with the points of view, post a comment here to tell what you think about these topics.
</p>
<div>
<br>
</div>
<div>
<br>
</div>
<div>
출처 :
<a href="http://www.phpclasses.org/blog/post/226-4-Reasons-Why-All-PHP-Frameworks-Suck.html" target="_blank" class="tx-link">
4 Reasons Why All PHP Sucks
</a>
</div>
