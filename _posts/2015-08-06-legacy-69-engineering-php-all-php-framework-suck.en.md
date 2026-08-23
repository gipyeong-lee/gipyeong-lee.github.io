---
layout: post
title: "[PHP] All PHP Frameworks Suck !!!"
description: "PHP Frameworks Day PHP Frameworks day is an event that took place in Kiev, Ukraine, last October. It is an event with talks about different frameworks. I onl..."
date: 2015-08-06 15:27:11 +0900
section: blog
category: engineering
lang: en
ref: 2015-08-06-legacy-69-engineering-php-all-php-framework-suck
tags:
  - "php"
  - "framework"
  - "Rasmus"
  - "Scrap"
  - "engineering"
noindex: true
translation_source_hash: 17bb24f3c1785a8c12e29d3e9b7b2df0a9aeb21863e0beb66b15f9f4526064ab
---

## PHP Frameworks Day

[PHP Frameworks day](http://frameworksdays.com/) is an event that took place in Kiev, Ukraine, last October. It is an event with talks about different frameworks.

I only became aware of it now thanks to the [PHP Quick Fix](https://twitter.com/phpquickfix) stream of news that Chris Cornutt (AKA enygma) of PHPDeveloper.org fame puts together. Thanks Chris.

## Why All PHP Frameworks Suck

Rasmus Lerdorf, the PHP creator, was invited to give a talk at the PHP Frameworks Day conference. He talked mostly about the latest PHP developments, but for me the most interesting part was the question and answers section.

Among other things, somebody asked Rasmus about his opinion on PHP frameworks. That was a straight question about his opinion, so Rasmus gave a straight answer (near 31m 47s): "They (PHP frameworks) All suck!"

<span class="media-container">
<iframe width="560" height="315" src="http://www.youtube.com/embed/anr7DQnMMs0" frameborder="0" allowfullscreen="">
</iframe>
</span>

It may seem odd that a guest speaker goes to a PHP frameworks conference telling them all they suck. However, the audience seemed to have enjoyed the answer. Anyway, Rasmus went into more detail about what he meant.

### 1. Frameworks Execute The Same Code Repeatedly Without Need

Rasmus clarified that all frameworks that are for general purposes are not optimized for everybody's needs.

A more specific complaint was that the solutions that frameworks offer lead to executing needless PHP code repeatedly in every HTTP request. The example that Rasmus gave is that in every request, frameworks check the database type the application is using to load the respective database access class. Since the database type does not change after an application is deployed, he sees this as a waste.

While I agree with Rasmus, I think this example is not very compelling because checking the configuration to decide which database access class to load takes a very small fraction of time, especially when compared for instance with executing database queries, which usually take many milliseconds and sometimes take a few seconds to run.

A better example of this problem is when frameworks need to read configuration files to define and load the actual configuration values.

Often frameworks read configuration from INI files. PHP has built-in functions to load and parse INI files. Despite the fact that you can do it all with a single function, reading an INI file and parsing it takes some time that is usually way more than checking the parsed configuration values.

If your framework reads and parses configuration values from files in other formats that PHP does not have built-in support for, like for instance YAML or XML, things get worse because the frameworks have to do the parsing in pure PHP code. That is much slower than the C code of the PHP engine that parses INI files.

A better alternative is to have configuration values defined in PHP script files. Just put the configuration values in PHP scripts that assign the values to variables.

When you use a PHP caching extension, PHP scripts are only compiled once. On a second run, PHP scripts compiled into opcodes are loaded from RAM. That is much faster than loading configuration from files.

### 2. Frameworks Require Too Many Interdependent Classes

Another point that Rasmus mentions is that sometimes you need only specific parts of a framework, but since the framework classes have too many dependencies between each other, you need to load too many classes even when you use simple features of the framework.

While this is true to a certain degree, I have seen efforts from certain framework developers to reduce the dependencies between distinct components. Still, there are often dependencies between many framework classes that sometimes do not aggregate anything to an application with specific needs.

To address this problem, some developers need to change the frameworks to strip the needless parts that add overhead. This causes a maintenance nightmare because they need to do that every time they want to upgrade to a newer version of a framework they started to adapt for their needs.

Rasmus suggests using frameworks optimized for specific purposes to avoid this problem. He recommends using for instance WordPress or Drupal if you just want to publish a blog.

Alternatively, Rasmus suggests that frameworks provide a means to let the developers push to production just a small subset of the components that are needed in each application.

This solution is too general. Rasmus did not get to the way certain frameworks implement things and so he did not comment on why certain frameworks need so many components.

For instance, many frameworks rely on runtime ORMs (Object Relational Mapping). These are components that let developers define how to query databases treating information as objects, rather than tables of records.

Object orientation is fine for abstracting problems and encapsulating solutions into classes of objects, but the way certain ORMs work adds too much needless overhead.

The developer has to write code to dynamically specify the class variables (table fields), condition clauses, object relationships (table joins), etc... to compose the actual query at runtime. This adds a lot of overhead because the queries that are executed are the same on every request, apart from some parameter values that may vary.

There is a better solution that avoids this overhead. Instead of dynamically composing queries at runtime, just have a separate tool that generates PHP code for the ORM classes. The generated classes already have the compiled SQL queries to execute without further overhead at runtime.

I have been using this approach since 2002 when I developed an ORM tool named [Metastorage](http://www.meta-language.net/metastorage.html). It does exactly what I described above. I define in a project file the objects, variables, relationships, and functions that I need to apply on objects.

Metastorage processes my object definitions and generates ORM classes that execute the necessary queries at runtime just by calling the class functions. No query building is done at runtime.

### 3. Needlessly Complicated Solutions

One thing that Rasmus did not mention directly is about the complicated solutions that frameworks tend to push.

That is the case for instance of application version migrations. Some frameworks have copied the concept of migrations from Ruby On Rails. This means that you have to write code to change your database schema between different application versions.

This is another thing that Metastorage addresses in a more efficient and less painful way for developers. Metastorage generates database table schema definitions in a separate file from my object definitions. It generates an installation class that installs the database tables on the first time.

If I change the object definitions, the installation class can also upgrade the schema with the newer definitions without destroying any data already inserted in the database tables.

This certainly makes development much faster and application upgrades less error prone because the tool always generates correct code to upgrade the database schema. When you write migrations code by hand, you may make mistakes that make you spend more time and effort to fix.

### 4. Duplicating the Web Server Functionality

Another aspect that Rasmus did not mention directly is related to aspects that frameworks sometimes require, where PHP code redoes work that the Web Server has already done.

For instance, routing is the process of assigning some code (a controller) to handle requests with different URL patterns. Many frameworks push applications to use the [front controller pattern](http://en.wikipedia.org/wiki/Front_Controller_pattern). The front controller analyzes the request URL and loads a specific controller to actually handle the request.

The matter here is that the Web server already does this. It can match the request URL against configuration (for instance of mod_rewrite or similar) and execute the appropriate PHP script.

When you make PHP handle the routing process, you are adding needless overhead to perform a task that is the same for every request with the same URL pattern. This falls into Rasmus's complaint of frameworks that execute the same code repeatedly to reach the same outcome.

This seems to be yet another bad influence that PHP frameworks got from Ruby On Rails and Java. With those languages, the Web server forwards the request to an application server.

PHP does not need to work this way because it always runs integrated with the Web server, so there is no point duplicating the Web server functionality in a way that is slower and adds more overhead.

## Other Questions

In the same conference, Rasmus also answered other interesting questions that I think it is worth commenting on.

### Dropping APC in Favour of Zend Opcode Cache

This is a topic that we have discussed several times in the [Lately in PHP podcast](http://www.phpclasses.org/blog/category/podcast/). Rasmus explained that PHP needed to adopt one opcode cache that would follow the latest PHP developments on every new release.

There are several opcode caches. Rasmus decided to give up on APC in favour of Zend's solution because it is more mature and faster. That required Zend to make their solution Open Source.

Curiously, the maintainer of the now official PHP opcode cache is Dmitry Stogov. He was the original developer of the Turck MMCache that Zend hired to work on their own cache extension some years ago.

All is well when it ends well. Too bad that PHP took all this time to have an official caching extension. The lack of an official extension made PHP look bad in many benchmarks that in the past favoured other languages.

### Compiling PHP into Binary Code

Someone asked if PHP will have a solution for protecting code by compiling it into some form of binary.

Rasmus stated that PHP will never have that kind of solution built-in. He justifies this by the fact that Zend (and other companies) provide solutions for that but it is relatively easy to break them. So he would rather not take part in that game.

While this is true, Rasmus is just considering solutions that merely compile PHP into opcodes and encrypt the result. This is a solution that is really not so hard to break by hackers.

However, there are better solutions that consist in compiling the result code into native assembly machine code. While it is always possible to decompile machine code, it is much harder to reverse engineer it into PHP code that is useful enough to be understood by people that want to steal work or change it in some useful way.

One concern that many developers have when they look for copy protection solutions for PHP code is that somebody with access to the servers where the code is installed changes the code easily.

I have seen many times developers that work for customers and those customers just go there and change their code without the knowledge of the developers. This creates maintenance headaches. Sometimes customers complain about code that is not working well because in reality they changed the code. So a solution to make it harder to view or change installed code would help.

For those cases, nowadays developers can minimize that problem by creating [PHAR](http://www.php.net/phar) archives. These are binary archives that contain one or more PHP scripts. While PHAR archives are not really a copy protection solution, at least they would make it harder for customers that want to poke at the developers' code.

### $ Dollar Sign in PHP variables

When asked about why variables start with the $ sign, he explained that it was meant to be able to insert variables inside literal string values, so a mark would need to be used to distinguish what is a variable from the rest of the string.

Since he wanted the variables to look the same inside and outside a string, he chose the $ sign to start variables, inspired by the solution that Perl also adopted.

### Node.js and Non-Blocking I/O

When asked if PHP would support non-blocking I/O programming, Rasmus explained that you can do that already with the [libevent](http://pecl.php.net/package/libevent) extension. But for that kind of programming, Rasmus would prefer writing code in the [Go language](http://golang.org/).

Anyway, unfortunately, asynchronous (non-blocking I/O) programming done with for instance Node.js is not very pleasant because it requires handling everything in nested callbacks.

Nested code in callbacks leads to very frustrating problems like for instance not being able to break from a while loop when you are inside a callback function. This is a topic that we discussed several times in the [Lately in JavaScript podcast](http://www.jsclasses.org/blog/post/44-Faster-JavaScript-with-asmjs--Lately-in-JavaScript-podcast-episode-28.html).

### Unicode and JIT on PHP 7

When asked about the plans for future PHP versions, Rasmus commented that he learned from the PHP 6 Unicode support failure that it was a goal that was too ambitious. So he expects that PHP evolves in smaller hops.

Two goals he thinks are too ambitious but will eventually be implemented maybe in PHP 7 are the native support to Unicode based on a simpler approach than ICU, and a JIT compilation engine probably based on Google V8 or Facebook HHVM.

## Conclusion

Rasmus's interview was very interesting because it makes us reflect on the way we are doing things in PHP that may be less than ideal, especially when you use general-purpose frameworks.

Whether you agree or disagree with the points of view, post a comment here to tell what you think about these topics.

<div>
<br>
</div>
<div>
<br>
</div>
<div>
Source :
<a href="http://www.phpclasses.org/blog/post/226-4-Reasons-Why-All-PHP-Frameworks-Suck.html" target="_blank" class="tx-link">
4 Reasons Why All PHP Frameworks Suck
</a>
</div>