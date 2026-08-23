---
layout: post
title: "[PHP] Website"
description: "User Registration First page load: 1. [Security] Domain check if ($_SERVER['HTTP_HOST'] != 'domain'){ exit('Disallowed domain.'); } 2. Login session check (Force redirect to main page if already logged in) if($_SESS..."
date: 2015-08-06 10:18:41 +0900
section: blog
category: essay
lang: en
ref: 2015-08-06-legacy-68-essay-php
tags:
  - "php"
  - "security"
  - "login"
  - "web"
  - "registration"
  - "site"
translation_source_hash: 78c42afdfff4ca7069c00a9abf58be7d56523bc96f3c5a838a2f88cdd510d0c8
---

<p>
<span>
<b>
User Registration
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
On first page load of user registration:
</span>
</p>

<p>
<b>
<span>
1. [Security] Domain check
</span>
</b>
</p>

<pre class="brush: php; toolbar: false;gutter:false;">
if ($_SERVER['HTTP_HOST'] != 'domain'){
  exit('Disallowed domain.');
}
</pre>


<p>
<b>
<span>
2. Login session check (Force redirect to main page if logged in)
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
3. SSL-related handling
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
4. i-PIN authentication, Identity verification (mobile phone)
</span>
</b>
</p>
<p>
<font>
In this case, use a form tag to generate the related request and process the returned value.
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
5. Terms of Service agreement
</b>
</font>
</p>
<p>
Use JavaScript to verify if the corresponding checkbox is checked before proceeding.
</p>



<p>
<span>
<b>
Login
</b>
</span>
</p>

<p>
<b>
1. Submit login data
</b>
</p>
<p>
: Use a form tag to submit ID and password.
</p>


<p>
<b>
<span>
2. [Security] Domain check
</span>
</b>
</p>

<pre class="brush: php; toolbar: false;gutter:false;">
if ($_SERVER['HTTP_HOST'] != 'domain'){
  exit('Disallowed domain.');
}
</pre>
<p>
<b>
3. Prevent submission of form data generated externally
</b>
</p>



<pre class="brush: php; toolbar: false; gutter:false;">
function referer(){

	$http_referer = str_replace('http://','',$_SERVER['HTTP_REFERER']);
	$http_referer = str_replace('https://','',$http_referer);

	$referer = explode('/',$http_referer);

	if ($referer[0] &lt;&gt; $_SERVER['HTTP_HOST']) {

		// Easier to process with a script that triggers a warning popup echo '....';
		exit;
	}

}
</pre>

<p>
<b>
4. Verify submitted values
</b>
</p>

<pre class="brush: php; toolbar: false; gutter:false;">
$user_id = trim( $_POST['userid'] );

$user_id= $mysqli_accountdb_s1-&gt;real_escape_string( $userid );// SQL injection prevention

$pw = trim( $_POST['password'] );

$backurl = trim( $_POST['backurl'] );
if (!$backurl) {
	$backurl = trim( $_GET['backurl'] ); // URL to return to after login completion
}
$backurl = xss_replace($backurl); // String processing via XSS prevention function

if (!$backurl) {
	$backurl = 'Set main address'; // If no return URL, set to main address
}
</pre>

<p>
<b>
5. Hashing
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
6. Handle sequential login delay using sessions
</b>
</p>
<pre class="brush: php; toolbar: false; gutter:false;">
if($_SESSION['ss_logintime'] != '') {
	$chk_time = mktime(date("H"),date("i"),date("s")-10,date("m"),date("d"),date("Y"));

	if ($chk_time &lt; strtotime($_SESSION['ss_logintime'])) {
		$msg = "Login is in progress. Please wait a moment.";
		msg($msg); // Display notification
		ob_flush();
		flush();
		sleep(2);
	}
}

$_SESSION['ss_logintime'] = date('Y-m-d H:i:s');
</pre>


<p>
<b>
7. IP check
</b>
</p>
<p>
IP check using cookies + login count limit (under 10 times) > 10-minute restriction (process by storing login time in cookie).
</p>

<p>
<b>
8. Login macro check
</b>
</p>
<p>
Prevent hacking using brute-force attacks.
</p>

<p>
<b>
9. Real user check
</b>
</p>
<p>
Check if the user exists, is not a withdrawn member, and the password is correct — this part can be checked via query or within PHP.
</p>

<p>
<b>
10. Overseas IP block user check
</b>
</p>
<p>
Prevent circumvented hacking via overseas IP blocking.
</p>

<p>
<b>
11. Login failure count accumulation: block login after 5 or more failures > redirect to password recovery
</b>
</p>
<p>
Redirect to password recovery page if login failure count is 5 or more.
</p>

<p>
<b>
12. Begin login
</b>
</p>
<p>
Create session.
</p>

<p>
<b>
13. Update user's final login information
</b>
</p>
<p>
session_id, login failure count, login date, login IP.
</p>

<p>
<b>
14. Add to login history
</b>
</p>
<p>
Record login history in the login history table.
</p>

<p>
<b>
15. Check for simple members/Facebook members
</b>
</p>
<p>
Forced redirect to the full membership conversion menu.
</p>

<p>
<b>
16. Password change check
</b>
</p>
<p>
Check if 90 days have passed since the last password change.
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
1. auto_increment value increases even when an Insert fails.
</b>
</p>
<p>
<b>
</b>
In reality, even if records are not stored due to errors like duplicates after executing an insert query using MySQLi, the corresponding auto_increment key value increases by +1.
</p>
<p>
The following article refers to this as a MySQL bug.
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
If the following code appears on the output screen and the intended echo value is not displayed:
<span>
&amp;#65279;
</span>
</p>
<p>
This is an 'encoding issue'.
</p>
<p>
The solution is to use Notepad++ to re-encode the file to UTF-8 (without BOM).
</p>

<p>
<b>
<span>
2. How to execute PHP code in HTML files
</span>
</b>
</p>

<p>
(1) Enter the following in the httpd.conf file:
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
(2) Enter the following in the .htaccess file:
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
3. What is 'global'?
</span>
</b>
<br>
</span>
</p>
<p>
'global' allows you to use a global variable when a variable used in a function has the same name as the global variable.
</p>
<p>
You can think of it as similar to 'self.variableName' in iOS code.
</p>





<p>
<b>
<span>
Reference Notes
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
$_SERVER['REQUEST_URI'] = Current page address excluding the domain = index.phpuser=&name=
</p>
<p>
$_SERVER['PHP_SELF'] = Current page address excluding domain and passed values = index.php
</p>

<p>
<b>
[require or require_once, include or include_once]
</b>
</p>
<p>
Originally, require_once and include_once were used instead of require and include.
</p>
<p>
The reason for using this API is to avoid duplicate functions.
</p>
<p>
However, it is said that this API slows down performance.
</p>
<p>
Therefore, it is recommended to use it as follows:
</p>


<pre class="brush: php; toolbar: false; gutter:false;">
if (!defined('MyIncludeName')) {
    require('MyIncludeName');
    define('MyIncludeName', 1);
}
</pre>


<p>
Below are the comparison results:
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
[Additional TIP]
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
echo is faster than print.
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
Single quotes (') are faster than double quotes (") for wrapping strings.
</span>
</font>
</p>

<p>
<font>
<span>
This is because PHP looks for variables within double quotes, but not within single quotes.
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
Use single quotes if the string does not contain variables.
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
Use pre-calculated values. When specifying the largest value for a for-loop, don't put it in the loop.
</span>
</p>

<p>
<font>
<span>
Use $max = count($array) before the for-loop starts.
</span>
</font>
</p>




<pre class="brush: php; toolbar: false; gutter:false">
for($x=0;$x&lt;count($array);$x++) ==&gt; for($x=0;$x&lt;$max;$x++)
</pre>

<span>


<p>
<span>
To free memory,
</span>
<font>
<span>
<span>
large arrays should be handled with
</span>
<b>
<u>
<span>
unset
</span>
</u>
</b>
<span>
or
</span>
<b>
<u>
<span>
null
</span>
</u>
</b>
<span>
processing.
</span>
</span>
</font>
</p>



<p>
<span>
<b>
<span>
str_replace is faster than preg_replace.
</span>
</b>
<span>
str_replace is generally the best, but
</span>
</span>
<span>
strstr
</span>
<span>
is sometimes faster for large strings. Using an array inside str_replace is usually faster than using multiple str_replace calls.
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
else if is faster than switch.
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
Close database connection after use.
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
$row['id'] is 7 times faster than $row[id].
</span>
</b>
<span>
If you don't use single quotes, the system has to guess what index you meant.
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
Use &lt;?php ... ?&gt; when declaring PHP. All other styles are bad practice.
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
Use strict code; avoid hiding notices, warnings, and errors. It leads to cleaner code and less overhead.
</span>
<b>
<span>
Consider always keeping error_reporting(E_ALL) on.
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
Remember to use exit along with header('location:'.$url);
</span>
</b>
<span>
.
</span>
</span>
</font>
</p>

<p>
<font>
<span>
<u>
<span>
Even if the location has changed, the script continues to run.
</span>
</u>
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
Initialize variables before use. Otherwise, it is very slow.
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
The @ symbol, which suppresses errors, is very slow.
</span>
</b>
</p>



<p>
<b>
<span>
It is better to use the GET method for simple SELECT functions, and POST for UPDATE functions.
</span>
</b>
</p>

<p>
<b>
<span>
This is because GET requests are cached and relatively faster (POST requests are not cached).
</span>
</b>
</p>




<p>
<b>
<span>
PHP 5.2.9 cannot interpret the '[ ]' syntax for arrays. Be careful.
</span>
</b>
</p>
<p>
<font>
<span>
<b>
<span>
If existing source code uses '[ ]' for arrays, it must be changed to array() for version 5.2.9.
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
Do not use preg_match()
</span>
</b>
</span>
</font>
</p>
<p>
<font>
<span>
if you only want to check if one string is contained in another string.
</span>
</font>
</p>
<p>
<font>
<span>
Use
<u>
strpos()
</u>
or
<u>
strstr()
</u>
instead as they will be faster.
</span>
</font>
</p>
</span>