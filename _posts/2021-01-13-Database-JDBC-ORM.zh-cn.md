---
layout: post
title: "数据库 - 第三部分：JDBC, JPA, Mybatis"
tags: [Database, DBMS, RDBMS, DB, JDBC, JPA, Mybatis]
style: border
color: primary
description: 学习 JDBC, JPA, Mybatis
lang: zh-cn
ref: 2021-01-13-Database-JDBC-ORM
---

### 什么是 JDBC ？

![JDBC](/assets/images/blog/2021-01-13-Database-JDBC-ORM/jdbc.jpg){: width="60%"}

JDBC 即 Java 数据库连接（Java DataBase Connectivity）。它支持通过 API 在 Java 环境中连接数据库。

首先，你需要与想要使用的数据源建立连接。数据源可以是 DBMS、遗留文件系统或其他具有相应 JDBC 驱动程序的数据源。

通常，JDBC 应用程序使用以下两个类之一连接到目标数据源：

#### 不推荐：通过 DriverManager 连接

使用 `DriverManager` 类连接到 DBMS 涉及调用 `DriverManager.getConnection` 方法。

```java
public Connection getConnection() throws SQLException {

    Connection conn = null;
    Properties connectionProps = new Properties();
    connectionProps.put("user", this.userName);
    connectionProps.put("password", this.password);

    if (this.dbms.equals("mysql")) {
        conn = DriverManager.getConnection(
                   "jdbc:" + this.dbms + "://" +
                   this.serverName +
                   ":" + this.portNumber + "/",
                   connectionProps);
    } else if (this.dbms.equals("derby")) {
        conn = DriverManager.getConnection(
                   "jdbc:" + this.dbms + ":" +
                   this.dbName +
                   ";create=true",
                   connectionProps);
    }
    System.out.println("Connected to database");
    return conn;
}
```
`DriverManager.getConnection` 方法用于建立数据库连接。此方法需要一个数据库 URL，该 URL 因 DBMS 而异。以下是一些数据库 URL 的示例：

> 示例
> 
> MySQL: `jdbc:mysql://localhost:3306/`，其中 `localhost` 是托管数据库的服务器名称，`3306` 是端口号。

这种方式会阻碍应用程序性能，因为连接是在 Java 类中创建/关闭的。而且 `DriverManager` 不支持连接池。

#### 推荐：通过使用 DataSource 连接

通过 DataSource 连接可以提高应用程序性能，因为连接不在类内部创建/关闭，而是由应用服务器管理，并可以在运行时获取。它还提供了创建连接池的功能。

因此，我们使用 `DataSource` 而不是 `DriverManager`。

```java
import java.sql.*;
import javax.sql.*;
import javax.ejb.*;
import javax.naming.*;

public class ConnectionPoolingBean implements SessionBean {

    // ...

    public void ejbCreate() throws CreateException {
        ctx = new InitialContext();
        ds = (DataSource)ctx.lookup("jdbc/fastCoffeeDB");
    }

    public void updatePrice(float price, String cofName,
                            String username, String password)
        throws SQLException{

        Connection con;
        PreparedStatement pstmt;
        try {
            con = ds.getConnection(username, password);
            con.setAutoCommit(false);
            pstmt = con.prepareStatement("UPDATE COFFEES " +
                        "SET PRICE = ? " +
                        "WHERE COF_NAME = ?");
            pstmt.setFloat(1, price);
            pstmt.setString(2, cofName);
            pstmt.executeUpdate();

            con.commit();
            pstmt.close();

        } finally {
            if (con != null) con.close();
        }
    }

    private DataSource ds = null;
    private Context ctx = null;
}
```

### 什么是 JPA ？

![JDBC](/assets/images/blog/2021-01-13-Database-JDBC-ORM/jpa.png){: width="60%"}

Java Persistence API（JPA）是 Java ORM 技术的标准规范，由 Java 提供 API。它是一个定义了如何在 Java 应用程序中使用关系数据库的接口。

> 注意：JPA 不是一个库，而是一个接口。

此外，JPA 是一个 ORM，它映射 Java 类和数据库表，而不是 SQL 查询。

相比于统计处理等复杂查询，JPA 更针对实时处理查询进行了优化。当然，你可以使用 JPA 提供的原生查询（Native Query）功能，但如果需要像统计这样复杂且精细的查询工作，使用 MyBatis 等 Mapper 方法可能会更高效。

#### 使用 JPA 的好处（例如 Hibernate）

随着以对象为中心开发的进行，直接修改查询语句的工作减少，通过摆脱数据库驱动开发提高了开发效率。

维护更加简便，因为通过处理作为实体字段的对象来操作数据库，而无需直接编写 SQL。这是因为如果修改了查询，所有包含它的 DTO 字段都必须相应更改，但如果使用 JPA，只需更改实体类信息即可轻松管理。

它是面向对象的，在尝试使用不同供应商（如 Oracle、MySQL 和 MariaDB）的数据库时，可以减少更改语法的精力。

支持缓存。（MyBatis 也支持查询缓存）

#### JPA 的局限性

无法手动优化查询。

从外部看，你不知道查询是如何运作的。

### 什么是 MyBatis ？

MyBatis 是一个持久层框架，支持开发者自定义 SQL、存储过程以及一些高级映射。

MyBatis 替换了几乎所有的 JDBC 代码、参数设置和结果映射。MyBatis 可以通过配置原始类型、Map 接口和 Java POJO，使用 XML 和注解来映射数据库记录。

通过将查询语句与业务逻辑分离，可以轻松地将数据工程师和开发者的工作分开。

#### MyBatis 的好处

SQL 和存储过程语法的独立性。

通过在业务逻辑中移除复杂的 JDBC 代码，可以保持源码整洁。

可以手动优化查询。

如果 RDBMS 是 Oracle，你不需要担心 BLOB 和 CLOB 的替换。

### 结论

如果你打算构建的服务不需要复杂的查询，使用像 Hibernate 这样的框架似乎是个好主意。然而，如果查询的复杂度增加，则认为有必要使用 MyBatis。

### 附录

- [jdbc-oracle](https://docs.oracle.com/javase/tutorial/jdbc/basics/gettingstarted.html)
- [jdbc-1](https://networkencyclopedia.com/java-database-connectivity-jdbc/)
- [jpa](https://velog.io/@adam2/JPA%EB%8A%94-%EB%8F%84%EB%8D%B0%EC%B2%B4-%EB%AD%98%EA%B9%8C-orm-%EC%98%81%EC%86%8D%EC%84%B1-hibernate-spring-data-jpa)
