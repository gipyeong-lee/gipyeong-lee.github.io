---
layout: post
title: "資料庫 - 第 3 部分：JDBC, JPA, Mybatis"
tags: [Database, DBMS, RDBMS, DB, JDBC, JPA, Mybatis]
style: border
color: primary
description: 學習 JDBC, JPA, Mybatis
lang: zh-tw
ref: 2021-01-13-Database-JDBC-ORM
---

### 什麼是 JDBC？

![JDBC](/assets/images/blog/2021-01-13-Database-JDBC-ORM/jdbc.jpg){: width="60%"}

JDBC 代表 Java 資料庫連線（Java DataBase Connectivity）。它支援在 Java 環境中透過 API 連接資料庫。

首先，你需要與想要使用的資料來源建立連線。資料來源可以是 DBMS、傳統檔案系統，或是其他具有對應 JDBC 驅動程式的資料來源。

通常，JDBC 應用程式會使用以下兩種類別之一來連接目標資料來源：

#### 不推薦：透過 DriverManager 連接

使用 `DriverManager` 類別連接 DBMS 涉及呼叫 `DriverManager.getConnection` 方法。

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
`DriverManager.getConnection` 方法用於建立資料庫連線。此方法需要一個資料庫 URL，具體取決於你的 DBMS。以下是一些資料庫 URL 的範例：

> 範例
> 
> MySQL: `jdbc:mysql://localhost:3306/`，其中 localhost 是託管資料庫的伺服器名稱，3306 是連接埠號。

由於連線是在 Java 類別中建立和關閉的，這會損害應用程式效能。此外，`DriverManager` 不支援連線池（Connection Pooling）。

#### 推薦：使用 DataSource 連接

使用 `DataSource` 可以提高應用程式效能，因為連線不在類別內建立或關閉，而是由應用程式伺服器管理，並可在運行時獲取。此外，它還提供了建立連線池的功能。

因此，我們使用 `DataSource` 而非 `DriverManager`。

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

### 什麼是 JPA？

![JDBC](/assets/images/blog/2021-01-13-Database-JDBC-ORM/jpa.png){: width="60%"}

Java Persistence API（JPA）是 Java ORM 技術的標準規範，是由 Java 提供的 API。它是一個定義如何在 Java 應用程式中使用關聯式資料庫的介面。

> 註：JPA 不是函式庫，而是一個介面。

此外，JPA 是一種 ORM（物件關係對應），它將 Java 類別與資料庫表進行對應，而不是對應 SQL 查詢。

相比於統計處理等複雜查詢，JPA 更針對即時處理的查詢進行優化。當然，你可以使用 JPA 提供的原生查詢（Native Query）功能，但如果你需要像統計那樣複雜且精細的查詢工作，使用 MyBatis 等映射器（Mapper）方法可能會更有效率。

#### 使用 JPA 的優點（例如：Hibernate）

由於開發是以物件為中心進行的，減少了直接修改查詢語句的工作量，藉由擺脫資料庫驅動開發，提高了開發效率。

維護更加簡潔，因為資料庫的操作是透過處理實體欄位的物件來完成，而不需要直接編寫 SQL。這是因為如果修改了查詢，所有包含結果的 DTO 欄位都必須相應更改；但如果使用 JPA，只需更改實體類別資訊即可輕鬆管理。

它是物件導向的，當嘗試使用不同供應商的資料庫（如 Oracle、MySQL 和 MariaDB）時，可以減少更改語法的負擔。

支援快取。（MyBatis 也支援查詢快取）

#### JPA 的限制

無法手動優化查詢。

從外部觀察時，很難得知查詢具體是如何運作的。

### 什麼是 MyBatis？

MyBatis 是一個持久層框架，支援開發者自定義 SQL、儲存程序以及進階映射。

MyBatis 取代了大部分原本需要透過 JDBC 處理的程式碼、參數設置和結果映射。MyBatis 可以透過配置基本類型、Map 介面和 Java POJO，並使用 XML 和註解來對應資料庫記錄。

透過將查詢語句與業務邏輯分離，可以輕鬆拆分資料工程師與開發者的工作。

#### MyBatis 的優點

SQL 與程序語法具有獨立性。

透過在業務邏輯中移除複雜的 JDBC 程式碼，可以保持原始碼整潔。

可以手動優化查詢。

如果 RDBMS 是 Oracle，則不需要擔心 BLOB 和 CLOB 的替換問題。

### 總結

如果你嘗試構建的服務不需要複雜的查詢，使用像 Hibernate 這樣的 JPA 框架似乎是個好主意。然而，如果查詢的複雜度增加，則有必要考慮使用 MyBatis。

### 附錄

- [jdbc-oracle](https://docs.oracle.com/javase/tutorial/jdbc/basics/gettingstarted.html)
- [jdbc-1](https://networkencyclopedia.com/java-database-connectivity-jdbc/)
- [jpa](https://velog.io/@adam2/JPA%EB%8A%94-%EB%8F%84%EB%8D%B0%EC%B2%B4-%EB%AD%98%EA%B9%8C-orm-%EC%98%81%EC%86%8D%EC%84%B1-hibernate-spring-data-jpa)
