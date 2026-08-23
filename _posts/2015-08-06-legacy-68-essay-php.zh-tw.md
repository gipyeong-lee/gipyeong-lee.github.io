---
layout: post
title: "[PHP] 網站"
description: "會員註冊 會員註冊首頁載入時 1. [安全] 網域檢查 if ($_SERVER['HTTP_HOST'] != 'domain'){ exit('不允許的網域。'); } 2. 登入 Session 檢查 (若為登入狀態，強制移動至首頁) if($_SESS..."
date: 2015-08-06 10:18:41 +0900
section: blog
category: essay
lang: zh-tw
ref: 2015-08-06-legacy-68-essay-php
tags:
  - "php"
  - "安全"
  - "登入"
  - "網站"
  - "會員註冊"
  - "網站"
translation_source_hash: 78c42afdfff4ca7069c00a9abf58be7d56523bc96f3c5a838a2f88cdd510d0c8
---

<p>
<span>
<b>
會員註冊
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
會員註冊首頁載入時
</span>
</p>

<p>
<b>
<span>
1. [安全] 網域檢查
</span>
</b>
</p>

<pre class="brush: php; toolbar: false;gutter:false;">
if ($_SERVER['HTTP_HOST'] != 'domain'){
  exit('不允許的網域。');
}
</pre>


<p>
<b>
<span>
2. 登入 Session 檢查 (若為登入狀態，強制移動至首頁)
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
3. SSL 相關處理
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
4. i-Pin 認證，本人認證（手機）
</span>
</b>
</p>
<p>
<font>
此部分使用 form 標籤建立相關請求，並處理回傳值。
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
5. 同意使用條款
</span>
</b>
</font>
</p>
<p>
使用 JavaScript 確認該核取方塊是否已勾選後再進行下一步。
</p>



<p>
<span>
<b>
登入
</b>
</span>
</p>

<p>
<b>
1. 傳送登入資料
</b>
</p>
<p>
：使用表單標籤傳送帳號、密碼。
</p>


<p>
<b>
<span>
2. [安全] 網域檢查
</span>
</b>
</p>

<pre class="brush: php; toolbar: false;gutter:false;">
if ($_SERVER['HTTP_HOST'] != 'domain'){
  exit('不允許的網域。');
}
</pre>
<p>
<b>
3. 防止外部產生的表單資料傳送
</span>
</b>
</p>



<pre class="brush: php; toolbar: false; gutter:false;">
function referer(){

	$http_referer = str_replace('http://','',$_SERVER['HTTP_REFERER']);
	$http_referer = str_replace('https://','',$http_referer);

	$referer = explode('/',$http_referer);

	if ($referer[0] &lt;&gt; $_SERVER['HTTP_HOST']) {

		//使用警告視窗指令碼處理較方便 echo '....';
		exit;
	}

}
</pre>

<p>
<b>
4. 確認傳入的值
</b>
</p>

<pre class="brush: php; toolbar: false; gutter:false;">
$user_id = trim( $_POST['userid'] );

$user_id= $mysqli_accountdb_s1-&gt;real_escape_string( $userid );// 防止 SQL Injection

$pw = trim( $_POST['password'] );

$backurl = trim( $_POST['backurl'] );
if (!$backurl) {
	$backurl = trim( $_GET['backurl'] ); // 登入完成後返回的 URL
}
$backurl = xss_replace($backurl); // 透過防止跨站指令碼（XSS）函式處理字串

if (!$backurl) {
	$backurl = '設定主網址'; // 若無返回 URL，則設定為主網址
}
</pre>

<p>
<b>
5.雜湊處理
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
6. 使用 Session 處理連續登入延遲
</b>
</p>
<pre class="brush: php; toolbar: false; gutter:false;">
if($_SESSION['ss_logintime'] != '') {
	$chk_time = mktime(date("H"),date("i"),date("s")-10,date("m"),date("d"),date("Y"));

	if ($chk_time &lt; strtotime($_SESSION['ss_logintime'])) {
		$msg = "正在登入中，請稍候。";
		msg($msg); // 顯示通知
		ob_flush();
		flush();
		sleep(2);
	}
}

$_SESSION['ss_logintime'] = date('Y-m-d H:i:s');
</pre>


<p>
<b>
7. IP 檢查
</b>
</p>
<p>
利用 Cookie 進行 IP 檢查 + 限制登入次數 (10次以下) > 限制 10 分鐘 (將登入時間寫入 Cookie 處理)
</p>

<p>
<b>
8. 登入機器人檢查
</b>
</p>
<p>
防止利用暴力破解法進行駭客攻擊。
</p>

<p>
<b>
9. 實際使用者檢查
</b>
</p>
<p>
確認使用者是否存在、是否為已註冊使用者、密碼是否正確。此部分可透過 Query 檢查，或在 PHP 內部檢查。
</p>

<p>
<b>
10. 海外 IP 封鎖檢查
</b>
</p>
<p>
透過封鎖海外 IP 防止繞道駭客攻擊。
</p>

<p>
<b>
11. 登入失敗次數累計 5 次以上禁止登入 > 引導至忘記密碼
</b>
</p>
<p>
若登入失敗次數超過 5 次，則重新導向至忘記密碼頁面。
</p>

<p>
<b>
12. 開始登入
</b>
</p>
<p>
建立 Session。
</p>

<p>
<b>
13. 更新使用者資訊與最終登入資訊
</b>
</p>
<p>
session_id、登入失敗次數、登入日期、登入 IP。
</p>

<p>
<b>
14. 新增登入紀錄
</b>
</p>
<p>
在登入歷史資料表中寫入登入紀錄。
</p>

<p>
<b>
15. 簡易會員、Facebook 會員檢查
</b>
</p>
<p>
強制移動至轉換為正式會員的選單。
</p>

<p>
<b>
16. 檢查密碼變更
</b>
</p>
<p>
確認密碼是否已超過 90 天未變更。
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
1. 即使 Insert 發生錯誤，auto_increment 值仍會增加。
</b>
</p>
<p>
<b>
</b>
實際上，使用 MySQLi 執行 insert 查詢後，即使因為 duplicate 等錯誤導致紀錄未寫入，該 auto_increment 鍵值仍會 +1 增加。
</p>
<p>
在下一篇文章中稱此為 MySQL 臭蟲。
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
若螢幕上顯示以下代碼，且未顯示預期的 echo 值。
<span>
&amp;#65279;
</span>
</p>
<p>
這是「編碼問題」。
</p>
<p>
解決方法是使用 Notepad++ 將該檔案的編碼轉換為 UTF-8 (無 BOM) 即可解決。
</p>

<p>
<b>
<span>
2.
</span>
<span>
若要在 HTML 檔案中執行 PHP 程式碼
</span>
</b>
</p>

<p>
(1) 在 httpd.conf 檔案內輸入以下內容：
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
(2) 在 .htaccess 檔案內輸入以下內容：
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
global 是什麼？
</span>
</b>
<br>
</span>
</p>
<p>
global 是當函數中使用的變數名稱與全域變數相同時，用來存取全域變數的語法。
</p>
<p>
在 iOS 的程式碼中，可以想成類似 self.變數名稱 的感覺。
</p>





<p>
<b>
<span>
參考事項
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
$_SERVER['REQUEST_URI'] = 當前頁面網址中扣除網域的部分 = index.phpuser=&amp;name=
</p>
<p>
$_SERVER['PHP_SELF'] = 當前頁面網址中扣除網域與傳遞參數的部分 = index.php
</p>

<p>
<b>
[required or required_once, include or include_once]
</b>
</p>
<p>
原先使用 required、include，後來改用 required_once、include_once。
</p>
<p>
使用這些 API 的原因是為了避免重複定義函數。
</p>
<p>
不過，據說這些 API 會拖慢速度。
</p>
<p>
因此，據說採取以下方式較好：
</p>


<pre class="brush: php; toolbar: false; gutter:false;">
if (!defined('MyIncludeName')) {
    require('MyIncludeName');
    define('MyIncludeName', 1);
}
</pre>


<p>
以下是測試比較結果：
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
[額外建議 (TIP)]
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
包覆字串時，單引號(') 比雙引號(") 快。
</span>
</font>
</p>

<p>
<font>
<span>
原因是 PHP 會在雙引號中尋找變數，而在單引號中則不會。
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
若字串中沒有變數，請使用單引號。
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
請使用預先計算好的值。在 for 迴圈中設定最大值時，請不要將計算放在迴圈內：
</span>
</p>

<p>
<font>
<span>
請在 for 迴圈開始前先使用 $max = count($array)
</span>
</font>
</p>




<pre class="brush: php; toolbar: false; gutter:false">
for($x=0;$x&lt;count($array);$x++) ==&gt; for($x=0;$x&lt;$max;$x++)
</pre>

<span>


<p>
<span>
為了釋放記憶體，
</span>
<font>
<span>
<span>
大型陣列必須使用
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
處理。
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
str_replace 通常是首選，但
</span>
</span>
<span>
strstr
</span>
<span>
在某些大型字串處理時有時更快。在 str_replace 中使用陣列通常比使用多次 str_replace 更快。
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
else if 語法比 switch 快。
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
使用完後請關閉資料庫連線。
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
如果不使用單引號，系統必須猜測你指的是什麼索引。
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
宣告 PHP 時請使用 &lt;?php ... ?&gt;，其他樣式皆為不規範。
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
請使用嚴格的程式碼，避免隱藏 notice、warning 和 error。這樣能產生更乾淨的程式碼並降低負載。
</span>
<b>
<span>
考慮隨時開啟 error_reporting(E_ALL)。
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
使用 header('location:'.$url); 時，請記得同時使用 exit。
</span>
</b>
<span>
即使位置已切換，指令碼仍會繼續執行。
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
變數請先初始化再使用，否則會非常慢。
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
用來隱藏錯誤的 @ 符號非常慢。
</span>
</b>
</p>



<p>
<b>
<span>
執行單純 SELECT 功能時建議使用 GET 方法，而 UPDATE 功能則建議使用 POST。
</span>
</b>
</p>

<p>
<b>
<span>
因為 GET 會被快取，速度相對較快。（POST 不會被快取）
</span>
</b>
</p>




<p>
<b>
<span>
PHP 5.2.9 不支援將 array() 寫成 '[ ]'，請注意。
</span>
</b>
</p>
<p>
<font>
<span>
<b>
<span>
若現有原始碼使用 '[ ]' 來定義陣列，在 5.2.9 版本中必須改為 array()。
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