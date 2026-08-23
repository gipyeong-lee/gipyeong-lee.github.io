---
layout: post
title: "[PHP] ウェブサイト"
description: "会員登録 会員登録の最初のページ読み込み時 1. [セキュリティ] ドメインチェック if ($_SERVER['HTTP_HOST'] != 'domain'){ exit('許可されていないドメインです。'); } 2. ログインセッションチェック ( ログイン状態の場合はメインページへ強制移動 ) if($_SESS..."
date: 2015-08-06 10:18:41 +0900
section: blog
category: essay
lang: ja
ref: 2015-08-06-legacy-68-essay-php
tags:
  - "php"
  - "セキュリティ"
  - "ログイン"
  - "ウェブ"
  - "会員登録"
  - "サイト"
translation_source_hash: 78c42afdfff4ca7069c00a9abf58be7d56523bc96f3c5a838a2f88cdd510d0c8
---

<p>
<span>
<b>
会員登録
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
会員登録の最初のページ読み込み時
</span>
</p>

<p>
<b>
<span>
1. [セキュリティ] ドメインチェック
</span>
</b>
</p>

<pre class="brush: php; toolbar: false;gutter:false;">
if ($_SERVER['HTTP_HOST'] != 'domain'){
  exit('許可されていないドメインです。');
}
</pre>


<p>
<b>
<span>
2. ログインセッションチェック (ログイン状態の場合はメインページへ強制移動)
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
3. SSL関連処理
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
4. i-Pin認証、本人認証（携帯電話）
</span>
</b>
</p>
<p>
<font>
該当部分についてはformタグを利用して関連リクエストを作成して送信し、返り値を受け取って処理する。
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
5. 利用規約への同意
</b>
</font>
</p>
<p>
JavaScriptを利用して該当チェックボックスがチェックされているか確認後に進める。
</p>



<p>
<span>
<b>
ログイン
</b>
</span>
</p>

<p>
<b>
1. ログインデータの送信
</b>
</p>
<p>
: フォームタグを利用してID、パスワードを送信
</p>


<p>
<b>
<span>
2. [セキュリティ] ドメインチェック
</span>
</b>
</p>

<pre class="brush: php; toolbar: false;gutter:false;">
if ($_SERVER['HTTP_HOST'] != 'domain'){
  exit('許可されていないドメインです。');
}
</pre>
<p>
<b>
3. 外部から生成されたフォームデータの送信防止
</b>
</p>



<pre class="brush: php; toolbar: false; gutter:false;">
function referer(){

	$http_referer = str_replace('http://','',$_SERVER['HTTP_REFERER']);
	$http_referer = str_replace('https://','',$http_referer);

	$referer = explode('/',$http_referer);

	if ($referer[0] &lt;&gt; $_SERVER['HTTP_HOST']) {

		//警告ウィンドウをスクリプトで処理すると便利 echo '....';
		exit;
	}

}
</pre>

<p>
<b>
4. 送信値の確認
</b>
</p>

<pre class="brush: php; toolbar: false; gutter:false;">
$user_id = trim( $_POST['userid'] );

$user_id= $mysqli_accountdb_s1-&gt;real_escape_string( $userid );// SQLインジェクション防止

$pw = trim( $_POST['password'] );

$backurl = trim( $_POST['backurl'] );
if (!$backurl) {
	$backurl = trim( $_GET['backurl'] ); // ログイン完了後に戻るURL
}
$backurl = xss_replace($backurl); // クロスサイトスクリプト防止関数による文字列処理

if (!$backurl) {
	$backurl = 'メインアドレス設定'; // 戻るURLがない場合はメインアドレスに設定
}
</pre>

<p>
<b>
5. ハッシュ化
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
6. セッションを利用した連続ログイン遅延処理
</b>
</p>
<pre class="brush: php; toolbar: false; gutter:false;">
if($_SESSION['ss_logintime'] != '') {
	$chk_time = mktime(date("H"),date("i"),date("s")-10,date("m"),date("d"),date("Y"));

	if ($chk_time &lt; strtotime($_SESSION['ss_logintime'])) {
		$msg = "ログイン中です。しばらくお待ちください。";
		msg($msg); // 通知表示
		ob_flush();
		flush();
		sleep(2);
	}
}

$_SESSION['ss_logintime'] = date('Y-m-d H:i:s');
</pre>


<p>
<b>
7. IPチェック
</b>
</p>
<p>
クッキーを利用したIPチェック + ログイン回数制限（10回以下） > 10分間制限を設ける（クッキーにログイン時間を保存して処理）
</p>

<p>
<b>
8. ログインマクロチェック
</b>
</p>
<p>
総当たり攻撃（ブルートフォース）によるハッキング防止
</p>

<p>
<b>
9. 実際のユーザーチェック
</b>
</p>
<p>
ユーザーが存在するか、退会済みユーザーではないか、パスワードが合っているか。該当部分はクエリでチェックしても良いし、PHP内部でチェックしても良い。
</p>

<p>
<b>
10. 海外IP遮断ユーザーチェック
</b>
</p>
<p>
海外IP遮断による迂回ハッキング防止。
</p>

<p>
<b>
11. ログイン失敗回数累積5回以上でログイン不可 > パスワード検索へ誘導
</b>
</p>
<p>
ログイン失敗回数が5回以上の場合、パスワード検索ページへリダイレクト
</p>

<p>
<b>
12. ログイン開始
</b>
</p>
<p>
セッション生成。
</p>

<p>
<b>
13. ユーザー情報の最終ログイン情報更新
</b>
</p>
<p>
session_id、ログイン失敗回数、ログイン日付、ログインIP
</p>

<p>
<b>
14. ログイン履歴追加
</b>
</p>
<p>
ログイン履歴テーブルにログイン記録を残します。
</p>

<p>
<b>
15. かんたん会員、Facebook会員チェック
</b>
</p>
<p>
正会員転換メニューへ強制移動。
</p>

<p>
<b>
16. パスワード変更チェック
</b>
</p>
<p>
パスワード変更後、90日が経過したか確認します。
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
1. Insertがエラーになった場合でもauto_increment値は増加している。
</b>
</p>
<p>
<b>
</b>
実際、MySQLiを利用してinsertクエリを投げた後、duplicateなどのエラーでレコードが追加されなくても、該当auto_incrementキー値は+1増加している。
</p>
<p>
次のarticleでは、これをMySQLのバグとして言及している。
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
もし、出力された画面にこのようなコードが表示され、意図したecho値が出ない場合。
<span>
&amp;#65279;
</span>
</p>
<p>
該当部分は「エンコーディングの問題」である。
</p>
<p>
解決策として、Notepad++を利用して該当ファイルのエンコーディングをUTF-8（BOMなし）でエンコードすれば解決する。
</p>

<p>
<b>
<span>
2. HTMLファイルでPHPコードを実行するには
</span>
</b>
</p>

<p>
(1) httpd.confファイル内に以下の内容を入力する。
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
(2) .htaccessファイル内に以下の内容を入力する。
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
3. globalとは何ですか？
</span>
</b>
<br>
</span>
</p>
<p>
globalは、関数内で使用する変数がグローバル変数と同じ名前の時に、グローバル変数を使えるようにしてくれるものです。
</p>
<p>
iOS側のコードにおけるself.変数名のような感覚だと考えると分かりやすいです。
</p>





<p>
<b>
<span>
参考資料
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
$_SERVER['REQUEST_URI'] = 現在のページのURLからドメインを除外したもの = index.phpuser=&amp;name=
</p>
<p>
$_SERVER['PHP_SELF'] = 現在のページのURLからドメインと送信値を除外したもの = index.php
</p>

<p>
<b>
[required or required_once, include or include_once]
</b>
</p>
<p>
本来はrequired、includeの代わりにrequired_once、include_onceを使用した。
</p>
<p>
このAPIを使う理由は、関数の重複を避けるためである。
</p>
<p>
しかし、該当APIは速度を低下させるという。
</p>
<p>
そのため、以下のように使用する方が良いとのことだ。
</p>


<pre class="brush: php; toolbar: false; gutter:false;">
if (!defined('MyIncludeName')) {
    require('MyIncludeName');
    define('MyIncludeName', 1);
}
</pre>


<p>
以下は比較した結果である。
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
[追加TIP]
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
echoの方がprintよりも速い。
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
文字列を囲む際、シングルクォーテーション(')がダブルクォーテーション(")よりも速い。
</span>
</font>
</p>

<p>
<font>
<span>
その理由は、PHPはダブルクォーテーション内では変数を検索するが、シングルクォーテーションでは検索しないからである。
</span>
</font>
</p>

<p>
<font>
<span>
<b>
<span>
文字列に変数がない場合はシングルクォーテーションを使おう。
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
計算済みの値を使おう。forループのために最大の値を指定する時は、ループの中に入れないで
</span>
</p>

<p>
<font>
<span>
$max = count($array)をforループが始まる前に使用しよう。
</span>
</font>
</p>




<pre class="brush: php; toolbar: false; gutter:false">
for($x=0;$x&lt;count($array);$x++) ==&gt; for($x=0;$x&lt;$max;$x++)
</pre>

<span>


<p>
<span>
メモリ解放のために
</span>
<font>
<span>
<span>
サイズの大きい配列は
</span>
<b>
<u>
<span>
unset
</span>
</u>
</b>
<span>
または
</span>
<b>
<u>
<span>
null
</span>
</u>
</b>
<span>
処理をしなければならない。
</span>
</span>
</font>
</p>



<p>
<span>
<b>
<span>
str_replaceがpreg_replaceよりも速い。
</span>
</b>
<span>
str_replaceは基本的に最強だが、
</span>
</span>
<span>
strstr
</span>
<span>
が、大きな文字列の中では速い場合がある。str_replace内で配列を使うのが、通常は複数のstr_replaceを使うよりも速い。
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
else if構文がswitchよりも速い
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
使った後はデータベース接続を閉じよう
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
$row['id']の方が$row[id]よりも7倍速い。
</span>
</b>
<span>
シングルクォーテーションを使わないと、システムがあなたが意図したインデックスは何なのかを推測しなければならないからである。
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
phpを宣言する時は&lt;?php ... ?&gt;を使おう。他のスタイルはすべて推奨されない。
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
厳格なコードを使おう。noticeやwarning、errorを見えなくするのは避けよう。よりきれいなコードになり、負荷も抑えられる。
</span>
<b>
<span>
error_reporting(E_ALL)を常にオンにしておくことを検討しよう。
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
header('location:'.$url);を使う時はexitを一緒に使う
</span>
</b>
<span>
ことを忘れないようにしよう。
</span>
</span>
</font>
</p>

<p>
<font>
<span>
<u>
<span>
locationが変わったにもかかわらず、スクリプトはそのまま進行してしまう。
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
変数は事前に初期化して使用しよう。そうしないと非常に遅い。
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
エラーを見えなくする@は非常に遅い
</span>
</b>
</p>



<p>
<b>
<span>
単純なSELECT機能を使う時はGETメソッドを、UPDATE機能を使う時はPOSTを使って通信するのが良い
</span>
</b>
</p>

<p>
<b>
<span>
なぜなら、GETの場合はキャッシュされるため速度が相対的に速い。（POSTはキャッシュされない）
</span>
</b>
</p>




<p>
<b>
<span>
PHP 5.2.9ではarray()が'[]'を解釈できない。注意。
</span>
</b>
</p>
<p>
<font>
<span>
<b>
<span>
もし、既存のソースが'[]'を使って配列を書いている場合は、これを5.2.9バージョンではarray()に変更しなければならない。
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