---
layout: post
title: "[PHP] 所有 PHP 框架都是垃圾！！！"
description: "PHP Frameworks Day 是去年十月在乌克兰基辅举行的一次活动。这是一个关于不同框架的演讲活动。我只是..."
date: 2015-08-06 15:27:11 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2015-08-06-legacy-69-engineering-php-all-php-framework-suck
tags:
  - "php"
  - "框架"
  - "Rasmus"
  - "Scrap"
  - "engineering"
noindex: true
translation_source_hash: 17bb24f3c1785a8c12e29d3e9b7b2df0a9aeb21863e0beb66b15f9f4526064ab
---

## PHP Frameworks Day
<a href="http://frameworksdays.com/" rel="nofollow">
PHP Frameworks day
</a> 是去年十月在乌克兰基辅举行的一次活动。这是一个关于不同框架的演讲活动。

我之所以现在才了解到它，要感谢 PHPDeveloper.org 的 Chris Cornutt（又名 enygma）所整理的 <a href="https://twitter.com/phpquickfix" rel="nofollow">PHP Quick Fix</a> 新闻流。谢谢你，Chris。

## <span><img src="http://files.phpclasses.org/files/blog/file/Rasmus-Lerdorf.jpg" alt="Rasmus Lerdorf http://en.wikipedia.org/wiki/File:Wikirl.jpg" title="Rasmus Lerdorf http://en.wikipedia.org/wiki/File:Wikirl.jpg" width="120" height="114"></span> 为什么所有 PHP 框架都是垃圾

PHP 的创始人 Rasmus Lerdorf 受邀在 PHP Frameworks Day 会议上发表演讲。他主要谈到了 PHP 的最新发展，但对我来说，最有趣的部分是问答环节。

在其他问题中，有人问了 Rasmus 对 PHP 框架的看法。这是一个关于他观点的直接问题，所以 Rasmus 给出了一个直接的回答（约 31 分 47 秒处）：“它们（PHP 框架）都是垃圾！”

<span class="media-container">
<iframe width="560" height="315" src="http://www.youtube.com/embed/anr7DQnMMs0" frameborder="0" allowfullscreen="">
</iframe>
</span>

嘉宾受邀参加 PHP 框架会议却告诉大家所有框架都是垃圾，这看起来可能有点奇怪。然而，听众似乎很喜欢这个回答。总之，Rasmus 详细说明了他的意思。

### 1. 框架不必要地重复执行相同的代码

Rasmus 澄清说，所有通用框架都没有针对每个人的需求进行优化。

一个更具体的抱怨是，框架提供的解决方案导致在每个 HTTP 请求中不必要地重复执行 PHP 代码。Rasmus 给出的例子是，框架在每个请求中都会检查应用程序正在使用的数据库类型，以加载相应的数据库访问类。由于应用程序部署后数据库类型不会改变，他认为这是一种浪费。

虽然我同意 Rasmus 的观点，但我认为这个例子说服力不足，因为检查配置以决定加载哪个数据库访问类所占用的时间极少，尤其是与执行数据库查询相比——查询通常需要几十毫秒，有时甚至需要几秒钟。

这个问题更好的例子是框架需要读取配置文件来加载实际的配置值。

通常框架从 INI 文件中读取配置。PHP 有内置函数来加载和解析 INI 文件。尽管你可以用一个函数完成所有操作，但读取并解析 INI 文件需要一些时间，这通常远多于检查已解析的配置值所需的时间。

如果你的框架读取和解析的是 PHP 没有内置支持的格式（如 YAML 或 XML）的配置文件，情况会更糟，因为框架必须用纯 PHP 代码进行解析。这比 PHP 引擎用来解析 INI 文件的 C 代码慢得多。

更好的替代方案是在 PHP 脚本文件中定义配置值。只需将配置值放入将值赋给变量的 PHP 脚本中即可。

当你使用 PHP 缓存扩展时，PHP 脚本只会被编译一次。在第二次运行时，编译成操作码（opcode）的 PHP 脚本会从内存（RAM）中加载。这比从文件中加载配置要快得多。

### 2. 框架需要太多相互依赖的类

Rasmus 提到的另一点是，有时你只需要框架的特定部分，但由于框架类之间有太多相互依赖关系，即使你只使用框架的简单功能，也需要加载太多的类。

虽然这在一定程度上是事实，但我看到一些框架开发者正在努力减少不同组件之间的依赖关系。尽管如此，许多框架类之间仍然存在依赖关系，有时这些依赖对于有特定需求的应用程序来说毫无用处。

为了解决这个问题，一些开发者需要修改框架，剔除那些增加开销的不必要部分。这导致了一场维护噩梦，因为他们每次想要升级到已开始适应其需求的框架的新版本时，都需要重新做一遍。

Rasmus 建议使用针对特定目的优化的框架来避免这个问题。例如，如果你只是想发布一个博客，他建议使用 WordPress 或 Drupal。

或者，Rasmus 建议框架应提供一种方式，让开发者只需将每个应用程序所需的组件的一小部分推送到生产环境。

这个解决方案太笼统了。Rasmus 没有深入探讨某些框架实现事物的方式，因此他没有评论为什么某些框架需要这么多组件。

例如，许多框架依赖于运行时 ORM（对象关系映射）。这些组件让开发者能够通过将信息视为对象而不是记录表来定义如何查询数据库。

面向对象对于抽象问题并将解决方案封装到对象类中是很好的，但某些 ORM 的工作方式增加了太多不必要的开销。

开发者必须编写代码来动态指定类变量（表字段）、条件子句、对象关系（表连接）等，以便在运行时组成实际查询。这增加了很多开销，因为除了少数可能变化的参数值外，每次请求执行的查询都是相同的。

有一个更好的解决方案可以避免这种开销。与其在运行时动态组成查询，不如使用一个单独的工具为 ORM 类生成 PHP 代码。生成的类已经包含了编译好的 SQL 查询，在运行时执行时不再有额外的开销。

自从 2002 年我开发了一个名为 <a href="http://www.meta-language.net/metastorage.html" rel="nofollow">Metastorage</a> 的 ORM 工具以来，我就一直在使用这种方法。它完全实现了我上面描述的功能。我在项目文件中定义对象、变量、关系以及我需要对对象应用的功能。

Metastorage 处理我的对象定义，并生成 ORM 类，通过调用类函数在运行时执行必要的查询。运行时不进行任何查询构建。

### 3. 不必要地复杂的解决方案

Rasmus 没有直接提到的一点是框架倾向于推崇复杂的解决方案。

以应用程序版本迁移为例。一些框架从 Ruby On Rails 中复制了迁移的概念。这意味着你必须编写代码来在不同的应用程序版本之间更改数据库架构。

这是 Metastorage 以更高效、对开发者痛苦更少的方式解决的另一件事。Metastorage 将数据库表架构定义与我的对象定义保存在不同的文件中。它生成一个安装类，在第一次运行时安装数据库表。

如果我更改了对象定义，安装类也可以在不破坏数据库表中已插入的任何数据的情况下，使用更新后的定义升级架构。

这无疑使开发速度更快，应用程序升级也不那么容易出错，因为该工具总是生成正确的代码来升级数据库架构。当你手动编写迁移代码时，你可能会犯错，导致需要花费更多时间和精力去修复。

### 4. 重复 Web 服务器的功能

Rasmus 没有直接提到的另一个方面是框架有时要求 PHP 代码重做 Web 服务器已经完成的工作。

例如，路由是将代码（控制器）分配给处理具有不同 URL 模式的请求的过程。许多框架推崇应用程序使用 <a href="http://en.wikipedia.org/wiki/Front_Controller_pattern" rel="nofollow">前端控制器模式</a>。前端控制器分析请求 URL 并加载特定的控制器来实际处理请求。

这里的问题是 Web 服务器已经做了这些。它可以将请求 URL 与配置（例如 mod_rewrite 或类似配置）匹配，并执行相应的 PHP 脚本。

当你让 PHP 处理路由过程时，你是在为每个具有相同 URL 模式的请求执行相同任务的过程中增加了不必要的开销。这属于 Rasmus 对框架的抱怨，即框架为了达到相同的结果而反复执行相同的代码。

这似乎是 PHP 框架从 Ruby On Rails 和 Java 那里学到的又一个坏影响。在那些语言中，Web 服务器将请求转发给应用程序服务器。

PHP 不需要以这种方式工作，因为它总是与 Web 服务器集成运行，所以以一种更慢且增加更多开销的方式重复 Web 服务器的功能是没有意义的。

## 其他问题

在同一次会议上，Rasmus 还回答了其他一些我认为值得评论的有趣问题。

### 放弃 APC 转而使用 Zend Opcode Cache

这是我们在 <a href="http://www.phpclasses.org/blog/category/podcast/">Lately in PHP 播客</a> 中讨论过多次的话题。Rasmus 解释说，PHP 需要采用一个能够跟上最新 PHP 开发进度并随每个新版本更新的操作码缓存。

有几种操作码缓存。Rasmus 决定放弃 APC 转而使用 Zend 的解决方案，因为后者更成熟、更快。这要求 Zend 将其解决方案开源。

有趣的是，现在官方 PHP 操作码缓存的维护者是 Dmitry Stogov。他曾是 Turck MMCache 的原始开发者，几年前被 Zend 聘请来开发他们自己的缓存扩展。

结局好，一切都好。可惜 PHP 花了这么长时间才拥有官方的缓存扩展。缺少官方扩展使得 PHP 在过去 favoring 其他语言的许多基准测试中看起来很糟糕。

### 将 PHP 编译成二进制代码

有人问 PHP 是否会有通过将其编译成某种二进制形式来保护代码的解决方案。

Rasmus 表示 PHP 永远不会内置那种解决方案。他解释说，Zend（和其他公司）提供了这样的解决方案，但它们相对容易破解。所以他宁愿不参与那个游戏。

虽然这是事实，但 Rasmus 只是考虑了仅仅将 PHP 编译成操作码并加密结果的解决方案。这种解决方案对于黑客来说确实不难破解。

然而，有更好的解决方案，即把结果代码编译成原生汇编机器码。虽然反编译机器码总是可能的，但要将其逆向工程为对那些想要窃取工作成果或以有用方式修改它的人来说足够有用的 PHP 代码要困难得多。

许多寻找 PHP 代码拷贝保护解决方案的开发者关心的一个问题是，有权限访问安装了代码的服务器的人可以轻易地更改代码。

我多次见到过为客户工作的开发者，那些客户在开发者不知情的情况下直接去更改他们的代码。这造成了维护上的麻烦。有时客户抱怨代码运行不正常，因为实际上是他们更改了代码。因此，一种使查看或更改已安装代码变得更困难的解决方案会有所帮助。

对于这些情况，如今开发者可以通过创建 <a href="http://www.php.net/phar" rel="nofollow">PHAR</a> 归档来最小化该问题。这些是包含一个或多个 PHP 脚本的二进制归档。虽然 PHAR 归档并不是真正的拷贝保护解决方案，但至少它们会使那些想要窥探开发者代码的客户变得更困难。

### PHP 变量中的 $ 符号

当被问及为什么变量以 $ 符号开头时，他解释说这是为了能够在字面字符串值中插入变量，因此需要一个标记来区分什么是变量，什么是字符串的其余部分。

由于他希望变量在字符串内外看起来一样，他选择了 $ 符号来开始变量，这受到了 Perl 所采用的解决方案的启发。

### Node.js 和非阻塞 I/O

当被问及 PHP 是否会支持非阻塞 I/O 编程时，Rasmus 解释说你已经可以通过 <a href="http://pecl.php.net/package/libevent" rel="nofollow">libevent</a> 扩展做到这一点。但对于那种编程，Rasmus 更喜欢用 <a href="http://golang.org/" rel="nofollow">Go 语言</a> 编写代码。

总之，不幸的是，使用 Node.js 等工具进行的异步（非阻塞 I/O）编程并不是很愉快，因为它需要在嵌套回调中处理所有事情。

回调中的嵌套代码会导致非常令人沮丧的问题，例如当你位于回调函数中时，无法跳出 while 循环。这是我们在 <a href="http://www.jsclasses.org/blog/post/44-Faster-JavaScript-with-asmjs--Lately-in-JavaScript-podcast-episode-28.html">Lately in JavaScript 播客</a> 中讨论过多次的话题。

### PHP 7 中的 Unicode 和 JIT

当被问及 PHP 未来版本的计划时，Rasmus 评论说他从 PHP 6 Unicode 支持的失败中吸取了教训，即这是一个太过于雄心勃勃的目标。因此，他希望 PHP 能以更小的步伐进化。

他认为有两个目标过于雄心勃勃，但最终可能会在 PHP 7 中实现：一个是基于比 ICU 更简单的方法对 Unicode 进行原生支持，另一个是可能基于 Google V8 或 Facebook HHVM 的 JIT 编译引擎。

## 总结

Rasmus 的采访非常有趣，因为它促使我们反思在 PHP 中做事的方式，这些方式可能不够理想，特别是在使用通用框架时。

无论你同意还是不同意这些观点，请在这里发表评论，告诉我们你对这些主题的看法。

<div>
<br>
</div>
<div>
<br>
</div>
<div>
参考资料：
<a href="http://www.phpclasses.org/blog/post/226-4-Reasons-Why-All-PHP-Frameworks-Suck.html" target="_blank" class="tx-link">
4 Reasons Why All PHP Sucks
</a>
</div>