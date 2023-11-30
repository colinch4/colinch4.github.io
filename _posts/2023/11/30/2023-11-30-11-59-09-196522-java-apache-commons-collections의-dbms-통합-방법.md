---
layout: post
title: "[java] Java Apache Commons Collections의 DBMS 통합 방법"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 자바에서 다양한 데이터 구조, 컬렉션, 맵 등을 제공하는 라이브러리입니다. 이 라이브러리는 DBMS와의 통합을 통해 데이터를 편리하게 다룰 수 있도록 도와줍니다.

이 글에서는 Java에서 Apache Commons Collections를 활용하여 DBMS와의 통합을 어떻게 수행할 수 있는지 알아보겠습니다. 예를 들어, MySQL 데이터베이스와의 통합을 기준으로 설명하겠습니다.

### 1. MySQL 데이터베이스 연결

첫 번째로 해야 할 일은 MySQL 데이터베이스에 연결하는 것입니다. Apache Commons Collections에서는 `DBUtils` 클래스를 사용하여 데이터베이스 연결을 쉽게 수행할 수 있습니다. 다음은 MySQL 데이터베이스에 연결하는 예제 코드입니다.

```java
import org.apache.commons.dbutils.DbUtils;

public class MySQLDatabaseConnector {

    private static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
    private static final String DB_URL = "jdbc:mysql://localhost/mydatabase";
    private static final String USER = "username";
    private static final String PASS = "password";

    public static void main(String[] args) {
        Connection conn = null;
        try {
            // 데이터베이스 드라이버 클래스 로드
            Class.forName(JDBC_DRIVER);

            // 데이터베이스에 연결
            conn = DriverManager.getConnection(DB_URL, USER, PASS);

            // 연결 성공 시 추가적인 작업 수행
            // ...

        } catch (SQLException se) {
            se.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 연결 종료
            DbUtils.closeQuietly(conn);
        }
    }
}
```

위 코드에서 `DB_URL`, `USER`, `PASS` 변수는 본인의 MySQL 데이터베이스에 맞게 설정해주어야 합니다.

### 2. 데이터 쿼리 및 조작

데이터베이스에 연결한 후에는 Apache Commons Collections의 `QueryRunner` 클래스를 사용하여 데이터 쿼리 및 조작 작업을 수행할 수 있습니다. `QueryRunner`는 SQL 쿼리를 실행하고 결과를 반환하는 역할을 합니다. 다음은 데이터를 조회하는 예제 코드입니다.

```java
import org.apache.commons.dbutils.DbUtils;
import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.ResultSetHandler;

public class MySQLDataQuery {

    private static final String SELECT_QUERY = "SELECT * FROM mytable";

    public static void main(String[] args) {
        Connection conn = null;
        try {
            // 데이터베이스 연결
            conn = DriverManager.getConnection(DB_URL, USER, PASS);

            // QueryRunner 객체 생성
            QueryRunner queryRunner = new QueryRunner();

            // 쿼리 실행 및 결과 반환
            ResultSetHandler<List<MyTable>> resultSetHandler = new BeanListHandler<>(MyTable.class);
            List<MyTable> results = queryRunner.query(conn, SELECT_QUERY, resultSetHandler);

            // 결과 출력 또는 추가 작업 수행
            // ...

        } catch (SQLException se) {
            se.printStackTrace();
        } finally {
            // 연결 종료
            DbUtils.closeQuietly(conn);
        }
    }
}
```

위 코드에서 `SELECT_QUERY`는 자신이 실행할 쿼리문에 맞게 설정해주어야 합니다. 또한 `MyTable` 클래스는 DB의 테이블과 매핑되는 Java Bean 클래스입니다.

### 3. 데이터 삽입 및 갱신

데이터를 삽입하거나 갱신하는 작업은 `QueryRunner`의 `update()` 메소드를 사용하여 수행할 수 있습니다. 다음은 데이터를 삽입하는 예제 코드입니다.

```java
import org.apache.commons.dbutils.DbUtils;
import org.apache.commons.dbutils.QueryRunner;

public class MySQLDataInsert {

    private static final String INSERT_QUERY = "INSERT INTO mytable (column1, column2) VALUES (?, ?)";

    public static void main(String[] args) {
        Connection conn = null;
        try {
            // 데이터베이스 연결
            conn = DriverManager.getConnection(DB_URL, USER, PASS);

            // QueryRunner 객체 생성
            QueryRunner queryRunner = new QueryRunner();

            // 쿼리 실행
            queryRunner.update(conn, INSERT_QUERY, "value1", "value2");

            // 삽입 완료 메시지 출력 또는 추가 작업 수행
            // ...

        } catch (SQLException se) {
            se.printStackTrace();
        } finally {
            // 연결 종료
            DbUtils.closeQuietly(conn);
        }
    }
}
```

위 코드에서 `INSERT_QUERY`는 자신이 실행할 쿼리문에 맞게 설정해주어야 합니다. 또한 `value1`, `value2`는 삽입할 데이터에 맞게 설정해주어야 합니다.

### 결론

Apache Commons Collections를 사용하면 Java에서 DBMS와의 통합을 간편하게 수행할 수 있습니다. 이 글에서는 MySQL 데이터베이스와의 통합을 예로 들었지만, 다른 데이터베이스와의 통합도 유사한 방식으로 수행할 수 있습니다. 자세한 내용은 Apache Commons Collections 공식 문서 및 예제를 참고하시기 바랍니다.

참고 자료:
- [Apache Commons Collections 공식 웹사이트](https://commons.apache.org/proper/commons-collections/)
- [Apache Commons Collections GitHub 저장소](https://github.com/apache/commons-collections)
- [Apache Commons DBUtils 공식 웹사이트](https://commons.apache.org/proper/commons-dbutils/)
- [Apache Commons DBUtils GitHub 저장소](https://github.com/apache/commons-dbutils)