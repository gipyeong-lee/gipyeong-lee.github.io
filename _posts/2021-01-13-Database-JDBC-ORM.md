---
layout: post
title: "Database - Part3 : JDBC, JPA, Mybatis"
tags: [Database, DBMS, RDBMS, DB, JDBC, JPA, Mybatis]
style: border
color: primary
description: Study JDBC, JPA, Mybatis
lang: ko
ref: 2021-01-13-Database-JDBC-ORM
---

### What is JDBC ?

![JDBC](/assets/images/blog/2021-01-13-Database-JDBC-ORM/jdbc.jpg){: width="60%"}

JDBC is Java DataBase Connectivity. which support connect database in java env by api.

First, you need to establish a connection with the data source you want to use. A data source can be a DBMS, a legacy file system, or some other source of data with a corresponding JDBC driver.

Typically, a JDBC application connects to a target data source using one of two classes

#### Not Preferred connecting by DriverManager

Connecting to your DBMS with the DriverManager class involves calling the method DriverManager.getConnection

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
The method DriverManager.getConnection establishes a database connection. This method requires a database URL, which varies depending on your DBMS. The following are some examples of database URLs

> Example
> 
> MySQL: jdbc:mysql://localhost:3306/, where localhost is the name of the server hosting your database, and 3306 is the port number

hampers the application performance as the connections are created/closed in java classes. and `DriverManager` does not support connection pooling.

#### Preffered connecting by using datasource

Improves application performance as connections are not created/closed within a class, they are managed by the application server and can be fetched while at runtime. and it provides a facility creating a pool of connections.

so we use `DataSource` indstead of a `DriverManager`

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

### What is JPA ?

![JDBC](/assets/images/blog/2021-01-13-Database-JDBC-ORM/jpa.png){: width="60%"}

Java Persistence API is standard specification for Java ORM technology, API provided by JAVA. It is interface that defines how to use relational database in Java application.

> Note: JPA is not the library. it is interface.

Also, JPA is an ORM, it maps Java classes and DB tables. not the sql query.

JPA is more optimized for queries for real-time processing than for complex queries such as statistical processing. Of course, you can use the native query function provided by JPA, but if you need complex and fine query work like statistics, it may be more efficient to use a Mapper method such as Mybatis.

#### Benefit of using JPA ( eg. hibernate )

As object-centered development is carried out, there is less work in the form of directly modifying the query statement, which increases the productivity of development by escaping from database-driven development.

Maintenance is more concise because the database is operated by handling objects that become entity fields without writing SQL directly. This is because if the query is modified, all the DTO fields to contain it must be changed accordingly, but if JPA is used, it is easy to manage by simply changing the entity class information.

It is object-oriented, it can reduce the effort of changing syntax when trying to use databases from different vendors such as Oracle, Mysql, and MariaDB.

Support caching. ( myBatis also support query caching )

#### limit of JPA

Can't optimiazation query manually.

When you look from the outside, you don't know how the query works.

### What is Mybatis ?

MyBatis is a persistence framework that supports developer-specified SQL, stored procedures, and some advanced mapping.

MyBatis replaces most of the code and parameter settings and result mapping that are processed with JDBC. MyBatis can use XML and annotations to map database records by configuring primitive types, Map interfaces, and Java POJOs.

By separating the query statement and business logic, it is easy to separate the work of the data engineer and the developer.

#### Benefit of MyBatis

Independence of SQL and procedure syntax

You can keep clean source code by removing complicated JDBC code in buisness logic

Optimiazaion query manually.

If the RDBMS is Oracle, you do not need to worry about blob and clob substitution.

### Conclusion

If the service you're trying to build doesn't require complex queries, it looks like a good idea to use a framework like hibernates. However, if the complexity of the query is increased, it is thought that it is necessary to use Mybatis.

### Appendix

- [jdbc-oracle](https://docs.oracle.com/javase/tutorial/jdbc/basics/gettingstarted.html)
- [jdbc-1](https://networkencyclopedia.com/java-database-connectivity-jdbc/)
- [jpa](https://velog.io/@adam2/JPA%EB%8A%94-%EB%8F%84%EB%8D%B0%EC%B2%B4-%EB%AD%98%EA%B9%8C-orm-%EC%98%81%EC%86%8D%EC%84%B1-hibernate-spring-data-jpa)