---
layout: post
title: LAMPスタック構築チュートリアル
style: border
color: info
description: LAMPはLinux、Apache、MySQL、PHPの略です。これは、動的なWebサイトやWebアプリケーションを動かすために広く使用されているWeb開発プラットフォームです。このチュートリアルでは、Linuxマシン上に基本的なLAMPスタックをセットアップする方法を紹介します。
lang: ja
ref: 2023-01-28-LAMP-stack-setup-tutorial
---
## はじめに

LAMPはLinux、Apache、MySQL、PHPの略です。これは、動的なWebサイトやWebアプリケーションを動かすために広く使用されているWeb開発プラットフォームです。このチュートリアルでは、Linuxマシン上に基本的なLAMPスタックをセットアップする方法を紹介します。

## 前提条件

LAMPスタックをセットアップする前に、rootアクセス権を持つLinuxマシンが必要です。また、Webサーバーおよび必要なデータベースソフトウェアがインストールされ、設定されている必要があります。

## Apacheのインストール

LAMPスタック構築の最初のステップは、Apache Webサーバーのインストールです。これは以下のコマンドで実行できます。

```
sudo apt-get update
sudo apt-get install apache2
```

インストールが完了したら、ブラウザでWebサーバーにアクセスして、Apacheが実行されていることを確認できます。デフォルトのApache Webページが表示されるはずです。

## MySQLのインストール

次のステップは、MySQLのインストールです。これは以下のコマンドで実行できます。

```
sudo apt-get install mysql-server
```

インストールが完了したら、データベースにログインしてMySQLが実行されていることを確認できます。ログインするには以下のコマンドを使用します。

```
mysql -u root -p
```

パスワードの入力を求められます。正常にログインできると、MySQLプロンプトが表示されます。

## PHPのインストール

LAMPスタック構築の最後のステップは、PHPのインストールです。これは以下のコマンドで実行できます。

```
sudo apt-get install php
```

インストールが完了したら、簡単なPHPスクリプトを作成して、PHPが実行されていることを確認できます。Webサーバーのルートディレクトリに `test.php` というファイルを作成し、以下のコードをファイルに追加します。

```
<?php
  echo "PHP is working!";
?>
```

ファイルを保存し、ブラウザでアクセスします。「PHP is working!」というメッセージが表示されるはずです。

## LAMPスタックのテスト

Apache Webサーバー、MySQLデータベース、PHPのインストールと設定が完了したら、LAMPスタックが正しく動作していることをテストできます。Webサーバーのルートディレクトリに `test.php` というファイルを作成し、以下のコードをファイルに追加します。

```
<?php
  $mysql_host = 'localhost';
  $mysql_user = 'root';
  $mysql_password = 'password';

  $conn = mysql_connect($mysql_host, $mysql_user, $mysql_password);
  if (!$conn) {
    die('Could not connect: ' . mysql_error());
  }
  echo 'Connected successfully';
  mysql_close($conn);
?>
```

ファイルを保存し、ブラウザでアクセスします。LAMPスタックが正しく動作していれば、「Connected successfully」というメッセージが表示されるはずです。

## まとめ

このチュートリアルでは、Linuxマシン上に基本的なLAMPスタックをセットアップする方法を紹介しました。これで、動作するWebサーバー、データベース、スクリプト言語が整いました。

## 参考文献

- [Apache Web Server](https://httpd.apache.org/)
- [MySQL Database](https://www.mysql.com/)
- [PHP Scripting Language](https://www.php.net/)
