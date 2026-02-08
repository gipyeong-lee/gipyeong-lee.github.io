---
layout: post
title: "データベース - Part3 : JDBC, JPA, Mybatis"
tags: [Database, DBMS, RDBMS, DB, JDBC, JPA, Mybatis]
style: border
color: primary
description: JDBC, JPA, Mybatis についての学習
lang: ja
ref: 2021-01-13-Database-JDBC-ORM
---

### JDBCとは？

![JDBC](/assets/images/blog/2021-01-13-Database-JDBC-ORM/jdbc.jpg){: width="60%"}

JDBCは Java DataBase Connectivity の略で、Java環境においてAPIを通じてデータベースへの接続をサポートするものです。

まず、使用したいデータソースとの接続を確立する必要があります。データソースには、DBMS、レガシーファイルシステム、または対応するJDBCドライバを持つその他のデータソースがあります。

通常、JDBCアプリケーションは以下の2つのクラスのいずれかを使用してターゲットデータソースに接続します。

#### DriverManagerによる接続（非推奨）

DriverManagerクラスを使用してDBMSに接続するには、`DriverManager.getConnection`メソッドを呼び出します。

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
`DriverManager.getConnection`メソッドはデータベース接続を確立します。このメソッドにはデータベースURLが必要で、これはDBMSによって異なります。以下はデータベースURLのいくつかの例です。

> 例
> 
> MySQL: jdbc:mysql://localhost:3306/ (ここで localhost はデータベースをホストしているサーバーの名前、3306 はポート番号です)

Javaクラス内で接続の作成・閉鎖が行われるため、アプリケーションのパフォーマンスが低下します。また、`DriverManager` はコネクションプーリングをサポートしていません。

#### DataSourceを使用した接続（推奨）

クラス内で接続を作成・閉鎖せず、アプリケーションサーバーによって管理され、実行時に取得できるため、アプリケーションのパフォーマンスが向上します。また、コネクションプールを作成する機能も提供します。

そのため、`DriverManager` の代わりに `DataSource` を使用します。

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

### JPAとは？

![JDBC](/assets/images/blog/2021-01-13-Database-JDBC-ORM/jpa.png){: width="60%"}

Java Persistence API は、Java ORM技術の標準仕様であり、JAVAによって提供されるAPIです。これはJavaアプリケーションでリレーショナルデータベースをどのように使用するかを定義したインターフェースです。

> 注: JPAはライブラリではありません。インターフェースです。

また、JPAはORMであり、SQLクエリではなく、JavaクラスとDBテーブルをマッピングします。

JPAは、統計処理のような複雑なクエリよりも、リアルタイム処理のためのクエリに最適化されています。もちろん、JPAが提供するネイティブクエリ機能を使用することもできますが、統計のように複雑で細かいクエリ作業が必要な場合は、MybatisのようなMapperメソッドを使用する方が効率的かもしれません。

#### JPAを使用するメリット（例：Hibernate）

オブジェクト中心の開発が行われるため、クエリ文を直接修正するような作業が減り、データベース駆動開発から脱却することで開発の生産性が向上します。

SQLを直接記述せず、エンティティフィールドとなるオブジェクトを扱うことでデータベースを操作するため、保守がより簡潔になります。クエリが修正された場合、それを含むすべてのDTOフィールドを変更する必要がありますが、JPAを使用すればエンティティクラスの情報を変更するだけで管理が容易になるためです。

オブジェクト指向であるため、Oracle、Mysql、MariaDBなどの異なるベンダーのデータベースを使用しようとする際に、構文を変更する手間を減らすことができます。

キャッシングをサポートしています。（myBatisもクエリキャッシングをサポートしています）

#### JPAの制限

クエリを手動で最適化することができません。

外部から見たとき、クエリがどのように動作しているかがわかりません。

### Mybatisとは？

MyBatisは、開発者が指定したSQL、ストアドプロシージャ、およびいくつかの高度なマッピングをサポートする永続化フレームワークです。

MyBatisは、JDBCで処理されるコードやパラメータ設定、結果マッピングのほとんどを置き換えます。MyBatisはXMLやアノテーションを使用して、プリミティブ型、Mapインターフェース、Java POJOを設定することでデータベースレコードをマッピングできます。

クエリ文とビジネスロジックを分離することで、データエンジニアと開発者の作業を容易に分けることができます。

#### MyBatisのメリット

SQLとプロシージャ構文の独立性。

ビジネスロジック内の複雑なJDBCコードを排除することで、ソースコードをきれいに保つことができます。

クエリを手動で最適化できます。

RDBMSがOracleの場合、blobやclobの置換について心配する必要がありません。

### 結論

構築しようとしているサービスが複雑なクエリを必要としない場合は、Hibernateのようなフレームワークを使用するのが良いアイデアのように思えます。しかし、クエリの複雑さが増す場合は、Mybatisを使用する必要があると考えられます。

### 参考文献

- [jdbc-oracle](https://docs.oracle.com/javase/tutorial/jdbc/basics/gettingstarted.html)
- [jdbc-1](https://networkencyclopedia.com/java-database-connectivity-jdbc/)
- [jpa](https://velog.io/ @adam2/JPA%EB%8A%94-%EB%8F%84%EB%8D%B0%EC%B2%B4-%EB%AD%98%EA%B9%8C-orm-%EC%98%81%EC%86%8D%EC%84%B1-hibernate-spring-data-jpa)
