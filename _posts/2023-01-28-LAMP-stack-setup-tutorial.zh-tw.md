---
layout: post
title: LAMP 堆疊安裝教學
tags: [lamp stack, setup tutorial, server configuration]
style: border
color: info
description: LAMP 代表 Linux、Apache、MySQL 和 PHP。它是一個廣泛使用的網頁開發平台，用於驅動動態網站和網頁應用程式。本教學將向您展示如何在 Linux 機器上設置基本的 LAMP 堆疊。
lang: zh-tw
ref: 2023-01-28-LAMP-stack-setup-tutorial
---
## 簡介

LAMP 代表 Linux、Apache、MySQL 和 PHP。它是一個廣泛使用的網頁開發平台，用於驅動動態網站和網頁應用程式。本教學將向您展示如何在 Linux 機器上設置基本的 LAMP 堆疊。

## 先決條件

在設置 LAMP 堆疊之前，您需要有一台具有 root 權限的 Linux 機器。您還需要安裝並配置網頁伺服器，以及必要的資料庫軟體。

## 安裝 Apache

設置 LAMP 堆疊的第一步是安裝 Apache 網頁伺服器。可以使用以下命令完成：

```
sudo apt-get update
sudo apt-get install apache2
```

安裝完成後，您可以透過瀏覽器存取網頁伺服器來驗證 Apache 是否正在運行。您應該會看到預設的 Apache 網頁。

## 安裝 MySQL

下一步是安裝 MySQL。可以使用以下命令完成：

```
sudo apt-get install mysql-server
```

安裝完成後，您可以透過登入資料庫來驗證 MySQL 是否正在運行。您可以使用以下命令登入：

```
mysql -u root -p
```

系統會提示您輸入密碼。成功登入後，您應該會看到 MySQL 提示字元。

## 安裝 PHP

設置 LAMP 堆疊的最後一步是安裝 PHP。可以使用以下命令完成：

```
sudo apt-get install php
```

安裝完成後，您可以透過建立一個簡單的 PHP 腳本來驗證 PHP 是否正在運行。在網頁伺服器的根目錄中建立一個名為 `test.php` 的檔案，並將以下程式碼添加到檔案中：

```
<?php
  echo "PHP is working!";
?>
```

儲存檔案，然後在瀏覽器中存取它。您應該會看到「PHP is working!」的訊息。

## 測試 LAMP 堆疊

安裝並配置好 Apache 網頁伺服器、MySQL 資料庫和 PHP 後，您可以測試 LAMP 堆疊是否運作正常。在網頁伺服器的根目錄中建立一個名為 `test.php` 的檔案，並將以下程式碼添加到檔案中：

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

儲存檔案，然後在瀏覽器中存取它。如果 LAMP 堆疊運作正常，您應該會看到「Connected successfully」的訊息。

## 結論

本教學已向您展示如何在 Linux 機器上設置基本的 LAMP 堆疊。您現在應該擁有一個可以運作的網頁伺服器、資料庫和腳本語言。

## 參考資料

- [Apache 網頁伺服器](https://httpd.apache.org/)
- [MySQL 資料庫](https://www.mysql.com/)
- [PHP 腳本語言](https://www.php.net/)
