---
layout: post
title: "[PHP] 网站"
description: "会员注册 会员注册首页加载时 1. [安全] 域名检查 if ($_SERVER['HTTP_HOST'] != 'domain'){ exit('不允许的域名。'); } 2. 登录会话检查 (如果是登录状态，强制跳转到主页) if($_SESS..."
date: 2015-08-06 10:18:41 +0900
section: blog
category: essay
lang: zh-cn
ref: 2015-08-06-legacy-68-essay-php
tags:
  - "php"
  - "安全"
  - "登录"
  - "网页"
  - "会员注册"
  - "网站"
translation_source_hash: 78c42afdfff4ca7069c00a9abf58be7d56523bc96f3c5a838a2f88cdd510d0c8
---

<p>
<span>
<b>
会员注册
</b>
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
会员注册首页加载时
</span>
</p>

<p>
<b>
<span>
1. [安全] 域名检查
</span>
</b>
</p>

<pre class="brush: php; toolbar: false;gutter:false;">
if ($_SERVER['HTTP_HOST'] != 'domain'){
  exit('不允许的域名。');
}
</pre>


<p>
<b>
<span>
2. 登录会话检查 (如果处于登录状态，强制跳转到主页)
</span>
</b>
</p>

<pre class="brush: php; toolbar: false; gutter:false;">
if($_SESSION['session_id']){
    header('Location: '.$url);
    exit;
}
</pre>


<p>
<b>
<span>
3. SSL 相关处理
</span>
</b>
</p>

<pre class="brush: c; toolbar: false; gutter:false;">
if(!isset($_SERVER["HTTPS"])){
    $url = 'https://' . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];
header('Location: '.$url);
}
</pre>

<p>
<b>
<span>
<br>
</span>
</b>
</p>
<p>
<b>
<span>
4. i-Pin 认证，本人认证（手机）
</span>
</b>
</p>
<p>
<font>
对于该部分，利用 form 标签创建相关请求，并接收返回值进行处理。
</font>
</p>
<p>
<font>
<br>
</font>
</p>
<p>
<font>
<b>
5. 同意使用条款
</span>
</b>
</font>
</p>
<p>
使用 JavaScript 确认复选框是否被勾选后再进行下一步。
</p>



<p>
<span>
<b>
登录
</b>
</span>
</p>

<p>
<b>
1. 提交登录数据
</b>
</p>
<p>
: 使用表单标签提交 ID 和密码
</p>


<p>
<b>
<span>
2. [安全] 域名检查
</span>
</b>
</p>

<pre class="brush: php; toolbar: false;gutter:false;">
if ($_SERVER['HTTP_HOST'] != 'domain'){
  exit('不允许的域名。');
}
</pre>
<p>
<b>
3. 防止外部生成的表单数据提交
</span>
</b>
</p>



<pre class="brush: php; toolbar: false; gutter:false;">
function referer(){

	$http_referer = str_replace('http://','',$_SERVER['HTTP_REFERER']);
	$http_referer = str_replace('https://','',$http_referer);

	$referer = explode('/',$http_referer);

	if ($referer[0] &lt;&gt; $_SERVER['HTTP_HOST']) {

		//使用脚本显示警告框比较方便 echo '....';
		exit;
	}

}
</pre>

<p>
<b>
4. 验证提交的值
</b>
</p>

<pre class="brush: php; toolbar: false; gutter:false;">
$user_id = trim( $_POST['userid'] );

$user_id= $mysqli_accountdb_s1-&gt;real_escape_string( $userid );// 防止 SQL 注入

$pw = trim( $_POST['password'] );

$backurl = trim( $_POST['backurl'] );
if (!$backurl) {
	$backurl = trim( $_GET['backurl'] ); // 登录完成后跳转回的 URL
}
$backurl = xss_replace($backurl); // 通过跨站脚本攻击(XSS)过滤函数处理字符串

if (!$backurl) {
	$backurl = '设置主页地址'; // 如果没有跳转 URL，则设置为首页地址
}
</pre>

<p>
<b>
5. 哈希处理
</b>
</p>

<pre class="brush: php; toolbar: false; gutter:false;">
$encode_pw = sha1($pw);
</pre>

<p>
<b>
<br>
</b>
</p>
<p>
<b>
6. 利用 Session 处理连续登录延迟
</b>
</p>
<pre class="brush: php; toolbar: false; gutter:false;">
if($_SESSION['ss_logintime'] != '') {
	$chk_time = mktime(date("H"),date("i"),date("s")-10,date("m"),date("d"),date("Y"));

	if ($chk_time &lt; strtotime($_SESSION['ss_logintime'])) {
		$msg = "正在登录中，请稍候。";
		msg($msg); // 显示通知
		ob_flush();
		flush();
		sleep(2);
	}
}

$_SESSION['ss_logintime'] = date('Y-m-d H:i:s');
</pre>


<p>
<b>
7. IP 检查
</b>
</p>
<p>
利用 Cookie 进行 IP 检查 + 限制登录次数（10次以下） > 限制 10 分钟（将登录时间存入 Cookie 后处理）
</p>

<p>
<b>
8. 登录宏（自动化脚本）检查
</b>
</p>
<p>
防止暴力破解攻击
</p>

<p>
<b>
9. 真实用户检查
</b>
</p>
<p>
检查用户是否存在、是否为注销用户、密码是否正确 > 该部分可以通过查询检查，也可以在 PHP 内部检查。
</p>

<p>
<b>
10. 海外 IP 拦截用户检查
</b>
</p>
<p>
通过拦截海外 IP 防止绕过黑客攻击。
</p>

<p>
<b>
11. 登录失败次数累计 5 次以上禁止登录 > 引导至找回密码
</b>
</p>
<p>
如果登录失败次数超过 5 次，重定向到找回密码页面
</p>

<p>
<b>
12. 开始登录
</b>
</p>
<p>
创建 Session。
</p>

<p>
<b>
13. 更新用户最后登录信息
</b>
</p>
<p>
session_id、登录失败次数、登录日期、登录 IP
</p>

<p>
<b>
14. 添加登录历史
</b>
</p>
<p>
在登录历史表中记录登录日志。
</p>

<p>
<b>
15. 简易会员、Facebook 会员检查
</b>
</p>
<p>
强制跳转到转为正式会员的菜单。
</p>

<p>
<b>
16. 密码修改检查
</b>
</p>
<p>
检查是否距离上次修改密码已超过 90 天。
</p>

<p>
<span>
<b>
MySQL
</b>
</span>
</p>

<p>
<b>
1. 即使 Insert 报错，auto_increment 的值也会增加。
</b>
</p>
<p>
<b>
</b>
实际上，使用 MySQLi 发送 insert 查询语句后，即使因为 duplicate 等错误导致记录未插入，该 auto_increment 键值也会 +1 增加。
</p>
<p>
下一篇文章称这为 MySQL 的一个 Bug。
</p>
<p>
(http://desmart.com/blog/be-careful-with-mysqls-auto-increment-how-we-ended-up-losing-data)
<br>
</p>
<p>
<b>
<span>
QA
</span>
</b>
</p>

<p>
<b>
1. &amp;#65279
</b>
</p>
<p>
如果屏幕上显示了以下代码，并且没有显示预期的 echo 值时。
<span>
&amp;#65279;
</span>
</p>
<p>
这是“编码问题”。
</p>
<p>
解决方法是使用 Notepad++ 将该文件的编码转换为 UTF-8（无 BOM 格式）重新编码即可解决。
</p>

<p>
<b>
<span>
2.
</span>
<span>
如何在 HTML 文件中运行 PHP 代码
</span>
</b>
</p>

<p>
(1) 在 httpd.conf 文件中输入以下内容。
</p>

<pre class="brush: c; toolbar: false; gutter:false;">
AddHandler application/x-httpd-php .html
</pre>

<p>
<font>
<span>
<br>
</span>
</font>
</p>
<p>
<font>
<span>
(2) 在 .htaccess 文件中输入以下内容。
</span>
</font>
</p>
<p>
<font>
<br>
</font>
</p>

<pre class="brush: php; toolbar: false; gutter:false;">
AddType application/x-httpd-php .html
</pre>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<span>
<b>
<span>
global 是什么？
</span>
</b>
<br>
</span>
</p>
<p>
global 是当函数内使用的变量名与全局变量相同时，允许引用全局变量的关键字。
</p>
<p>
可以理解为类似于 iOS 代码中的 self.变量名 的感觉。
</p>





<p>
<b>
<span>
参考资料
</span>
</b>
</p>
<p>
<b>
<span>
<br>
</span>
</b>
</p>
<p>
<span>
<b>
[SERVER]
</b>
</span>
</p>
<p>
$_SERVER['REQUEST_URI'] = 当前页面地址（除去域名部分） = index.phpuser=&name=
</p>
<p>
$_SERVER['PHP_SELF'] = 当前页面地址（除去域名和传递参数部分） = index.php
</p>

<p>
<b>
[required 或 required_once，include 或 include_once]
</b>
</p>
<p>
原本使用 required、include，后来改用了 required_once、include_once。
</p>
<p>
使用这些 API 的目的是为了避免函数重定义错误。
</p>
<p>
然而，据说这些 API 会降低速度。
</p>
<p>
因此，建议按下述方式使用。
</p>


<pre class="brush: php; toolbar: false; gutter:false;">
if (!defined('MyIncludeName')) {
    require('MyIncludeName');
    define('MyIncludeName', 1);
}
</pre>


<p>
以下是对比结果。
</p>

<pre class="lang-php prettyprint prettyprinted">
<code>
<span class="pln">
php                  hhvm
</span>
<span class="kwd">
if
</span>

<span class="kwd">
defined
</span>

<span class="lit">
0.18587779998779
</span>

<span class="lit">
0.046600103378296
</span>
<span class="pln">
require_once
</span>
<span class="lit">
1.2219581604004
</span>

<span class="lit">
3.2908599376678
</span>
</code>
</pre>


<p>
<span>
[额外提示]
</span>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
echo 比 print 快。
</span>
</b>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
包裹字符串时，单引号(') 比双引号(") 快。
</span>
</font>
</p>

<p>
<font>
<span>
原因是 PHP 会在双引号中查找变量，而单引号中则不会。
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
如果字符串中没有变量，请使用单引号。
</span>
</b>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<span>
使用预先计算好的值。为了使用 for 循环，确定最大值时不要将其放在循环中。
</span>
</p>

<p>
<font>
<span>
请在 for 循环开始前使用 $max = count($array)。
</span>
</font>
</p>




<pre class="brush: php; toolbar: false; gutter:false">
for($x=0;$x&lt;count($array);$x++) ==&gt; for($x=0;$x&lt;$max;$x++)
</pre>

<span>


<p>
<span>
为了释放内存，
</span>
<font>
<span>
<span>
大型数组应使用
</span>
<b>
<u>
<span>
unset
</span>
</u>
</b>
<span>
或
</span>
<b>
<u>
<span>
null
</span>
</u>
</b>
<span>
进行处理。
</span>
</span>
</font>
</p>



<p>
<span>
<b>
<span>
str_replace 比 preg_replace 快。
</span>
</b>
<span>
通常情况下 str_replace 是最好的，但
</span>
</span>
<span>
strstr
</span>
<span>
有时在处理大数据字符串时更快。在 str_replace 中使用数组通常比多次使用 str_replace 更快。
</span>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
else if 语句比 switch 快。
</span>
</b>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
用完后请关闭数据库连接。
</span>
</b>

</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
$row['id'] 比 $row[id] 快 7 倍。
</span>
</b>
<span>
如果不使用单引号，系统必须猜测你指的是哪个索引。
</span>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
声明 PHP 时使用 &lt;?php ... ?&gt;。其他风格统统是不良习惯。
</span>
</b>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<span>
请使用严格代码，避免隐藏 notice、warning 和 error。这能带来更整洁的代码和更低的负荷。
</span>
<b>
<span>
考虑始终开启 error_reporting(E_ALL)。
</span>
</b>

</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
使用 header('location:'.$url); 时，请记得配合 exit 使用。
</span>
</b>
<span>
否则即使 location 已经改变，脚本仍会继续运行。
</span>
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<font>
<span>
请提前初始化变量。否则运行非常缓慢。
</span>
</font>
</p>

<p>
<font>
<span>
<br>
</span>
</font>
</p>

<p>
<b>
<span>
用来隐藏错误的 @ 符号速度非常慢。
</span>
</b>
</p>



<p>
<b>
<span>
进行简单 SELECT 操作时推荐使用 GET 方法，进行 UPDATE 操作时推荐使用 POST 通信。
</span>
</b>
</p>

<p>
<b>
<span>
因为 GET 有缓存机制，速度相对更快。（POST 不会被缓存）
</span>
</b>
</p>




<p>
<b>
<span>
PHP 5.2.9 中 array() 无法解析 '[ ]'。请注意。
</span>
</b>
</p>
<p>
<font>
<span>
<b>
<span>
如果现有源码在使用 '[ ]' 定义数组，在 5.2.9 版本中必须将其更改为 array()。
</span>
</b>
</span>
</font>
</p>



<p>
<font>
<span>
<b>
<span>
不要使用 preg_match()
</span>
</b>
</span>
</font>
</p>
<p>
<font>
<span>
如果你只是想检查一个字符串是否包含在另一个字符串中。
</span>
</font>
</p>
<p>
<font>
<span>
请改用
<u>
strpos()
</u>
或
<u>
strstr()
</u>
，因为它们速度更快。
</span>
</font>
</p>
</span>