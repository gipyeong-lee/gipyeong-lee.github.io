---
layout: post
title: "Database - Part 3: JDBC, JPA, Mybatis"
style: border
color: primary
description: Study JDBC, JPA, Mybatis
lang: en
ref: 2021-01-13-Database-JDBC-ORM
---

### What is JDBC?

![JDBC](/assets/images/blog/2021-01-13-Database-JDBC-ORM/jdbc.jpg){: width="60%"}

JDBC stands for Java Database Connectivity. It is an API that supports connecting to a database within a Java environment.

First, you need to establish a connection with the data source you want to use. A data source can be a DBMS, a legacy file system, or some other source of data with a corresponding JDBC driver.

Typically, a JDBC application connects to a target data source using one of two classes:

#### Connecting via DriverManager (Not Preferred)

Connecting to your DBMS with the `DriverManager` class involves calling the method `DriverManager.getConnection`.

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

The method `DriverManager.getConnection` establishes a database connection. This method requires a database URL, which varies depending on your DBMS. The following are some examples of database URLs:

> Example
> 
> MySQL: `jdbc:mysql://localhost:3306/`, where `localhost` is the name of the server hosting your database, and `3306` is the port number.

This method hampers application performance because connections are created and closed within Java classes. Additionally, `DriverManager` does not support connection pooling.

#### Connecting via DataSource (Preferred)

This method improves application performance because connections are not created and closed within a class; instead, they are managed by the application server and can be fetched at runtime. It also provides a facility for creating a connection pool.

Therefore, we use `DataSource` instead of `DriverManager`.

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

### What is JPA?

![JDBC](/assets/images/blog/2021-01-13-Database-JDBC-ORM/jpa.png){: width="60%"}

The Java Persistence API (JPA) is the standard specification for Java ORM technology, an API provided by Java. It is an interface that defines how to use relational databases in Java applications.

> Note: JPA is not a library; it is an interface.

Also, since JPA is an ORM, it maps Java classes to DB tables, not SQL queries.

JPA is better optimized for real-time processing queries rather than complex queries used in statistical processing. Of course, you can use the native query function provided by JPA, but if you require complex and granular query work like statistics, it may be more efficient to use a Mapper method such as MyBatis.

#### Benefits of using JPA (e.g., Hibernate)

As object-centered development is adopted, there is less need to directly modify query statements, which increases development productivity by moving away from database-driven development.

Maintenance is simpler because database operations are handled through objects (entity fields) without writing SQL directly. Normally, if a query is modified, all related DTO fields must be changed accordingly. However, with JPA, management is easier as you often only need to update the entity class information.

Since it is object-oriented, it reduces the effort required to change syntax when switching between database vendors such as Oracle, MySQL, and MariaDB.

It supports caching (MyBatis also supports query caching).

#### Limitations of JPA

Manual query optimization is difficult.

From the outside, it is often unclear how the underlying query is executed.

### What is MyBatis?

MyBatis is a persistence framework that supports developer-specified SQL, stored procedures, and some advanced mapping.

MyBatis replaces most of the JDBC code, parameter settings, and result mapping. MyBatis can use XML and annotations to map database records by configuring primitive types, Map interfaces, and Java POJOs.

By separating the query statements and business logic, it is easy to separate the work of the data engineer and the developer.

#### Benefits of MyBatis

Separation of SQL and procedure syntax.

You can maintain clean source code by removing complicated JDBC code from business logic.

Allows for manual query optimization.

If the RDBMS is Oracle, you do not need to worry about blob and clob substitution.

### Conclusion

If the service you are building does not require complex queries, using a framework like Hibernate is a good idea. However, if query complexity increases, it may be necessary to use MyBatis.

### Appendix

- [jdbc-oracle](https://docs.oracle.com/javase/tutorial/jdbc/basics/gettingstarted.html)
- [jdbc-1](https://networkencyclopedia.com/java-database-connectivity-jdbc/)
- [jpa](https://velog.io/ @adam2/JPA%EB%8A%94-%EB%8F%84%EB%8D%B0%EC%B2%B4-%EB%AD%98%EA%B9%8C-orm-%EC%98%81%EC%86%8D%EC%84%B1-hibernate-spring-data-jpa)
