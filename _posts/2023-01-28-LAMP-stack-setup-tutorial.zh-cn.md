---
layout: post
title: LAMP 栈安装教程
tags: [lamp stack, setup tutorial, server configuration]
style: border
color: info
description: LAMP 代表 Linux、Apache、MySQL 和 PHP。它是一个广泛使用的 Web 开发平台，用于驱动动态网站和 Web 应用程序。本教程将向您展示如何在 Linux 机器上搭建基础的 LAMP 栈。
lang: zh-cn
ref: 2023-01-28-LAMP-stack-setup-tutorial
---

## 引言

LAMP 代表 Linux、Apache、MySQL 和 PHP。它是一个广泛使用的 Web 开发平台，用于驱动动态网站和 Web 应用程序。本教程将向您展示如何在 Linux 机器上搭建基础的 LAMP 栈。

## 前提条件

在搭建 LAMP 栈之前，您需要一台拥有 root 权限的 Linux 机器。您还需要安装并配置 Web 服务器以及必要的数据库软件。

## 安装 Apache

搭建 LAMP 栈的第一步是安装 Apache Web 服务器。可以通过以下命令完成：

```
sudo apt-get update
sudo apt-get install apache2
```

安装完成后，您可以通过在浏览器中访问该 Web 服务器来验证 Apache 是否正在运行。您应该能看到 Apache 的默认网页。

## 安装 MySQL

下一步是安装 MySQL。可以通过以下命令完成：

```
sudo apt-get install mysql-server
```

安装完成后，您可以通过登录数据库来验证 MySQL 是否正在运行。您可以使用以下命令登录：

```
mysql -u root -p
```

系统会提示您输入密码。成功登录后，您应该能看到 MySQL 提示符。

## 安装 PHP

搭建 LAMP 栈的最后一步是安装 PHP。可以通过以下命令完成：

```
sudo apt-get install php
```

安装完成后，您可以通过创建一个简单的 PHP 脚本来验证 PHP 是否正在运行。在 Web 服务器的根目录中创建一个名为 `test.php` 的文件，并在文件中添加以下代码：

```php
<?php
  echo "PHP is working!";
?>
```

保存文件，然后在浏览器中访问它。您应该会看到消息 “PHP is working!”。

## 测试 LAMP 栈

在安装并配置好 Apache Web 服务器、MySQL 数据库和 PHP 之后，您可以测试 LAMP 栈是否正常工作。在 Web 服务器的根目录中创建一个名为 `test.php` 的文件，并在文件中添加以下代码：

```php
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

保存文件，然后在浏览器中访问它。如果 LAMP 栈正常工作，您应该会看到消息 “Connected successfully”。

## 结论

本教程向您展示了如何在 Linux 机器上搭建基础的 LAMP 栈。现在您应该已经拥有了一个可以工作的 Web 服务器、数据库和脚本语言环境。

## 参考资料

- [Apache Web 服务器](https://httpd.apache.org/)
- [MySQL 数据库](https://www.mysql.com/)
- [PHP 脚本语言](https://www.php.net/)
