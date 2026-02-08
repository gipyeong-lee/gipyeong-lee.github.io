---
layout: post
title: LAMP stack setup tutorial
tags: [lamp stack, setup tutorial, server configuration]
style: border
color: info
description: LAMP stands for Linux, Apache, MySQL and PHP. It is a widely used web development platform that is used to power dynamic websites and web applications. This tutorial will show you how to set up a basic LAMP stack on a Linux machine.
lang: en
ref: 2023-01-28-LAMP-stack-setup-tutorial
---
## Introduction

LAMP stands for Linux, Apache, MySQL and PHP. It is a widely used web development platform that is used to power dynamic websites and web applications. This tutorial will show you how to set up a basic LAMP stack on a Linux machine.

## Prerequisites

Before you can set up a LAMP stack, you will need to have a Linux machine with root access. You will also need to have a web server installed and configured, as well as the necessary database software.

## Installing Apache

The first step in setting up a LAMP stack is to install the Apache web server. This can be done using the following commands:

```
sudo apt-get update
sudo apt-get install apache2
```

Once the installation is complete, you can verify that Apache is running by accessing the web server in a browser. You should see the default Apache web page.

## Installing MySQL

The next step is to install MySQL. This can be done with the following command:

```
sudo apt-get install mysql-server
```

Once the installation is complete, you can verify that MySQL is running by logging in to the database. You can use the following command to log in:

```
mysql -u root -p
```

You will be prompted to enter a password. Once you have successfully logged in, you should see the MySQL prompt.

## Installing PHP

The final step in setting up a LAMP stack is to install PHP. This can be done with the following command:

```
sudo apt-get install php
```

Once the installation is complete, you can verify that PHP is running by creating a simple PHP script. Create a file called `test.php` in the web server’s root directory, and add the following code to the file:

```
<?php
  echo "PHP is working!";
?>
```

Save the file, then access it in a browser. You should see the message “PHP is working!”.

## Testing the LAMP Stack

Once you have installed and configured the Apache web server, MySQL database, and PHP, you can test that the LAMP stack is working correctly. Create a file called `test.php` in the web server’s root directory, and add the following code to the file:

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

Save the file, then access it in a browser. If the LAMP stack is working correctly, you should see the message “Connected successfully”.

## Conclusion

This tutorial has shown you how to set up a basic LAMP stack on a Linux machine. You should now have a working web server, database, and scripting language.

## References

- [Apache Web Server](https://httpd.apache.org/)
- [MySQL Database](https://www.mysql.com/)
- [PHP Scripting Language](https://www.php.net/)
