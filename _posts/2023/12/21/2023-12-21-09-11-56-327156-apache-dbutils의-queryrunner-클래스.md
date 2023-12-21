---
layout: post
title: "[java] Apache DbUtils의 QueryRunner 클래스"
description: " "
date: 2023-12-21
tags: [java]
comments: true
share: true
---

Apache DbUtils는 간단하고 간결한 JDBC 코드 작성을 도와주는 라이브러리입니다. 이 라이브러리는 JDBC를 사용하여 데이터베이스와 상호 작용하는 데 도움을 줍니다.

QueryRunner 클래스는 Apache DbUtils 라이브러리에서 제공하는 중요한 클래스 중 하나입니다. 이 클래스는 PreparedStatement와 ResultSet의 열이름 매핑 및 처리를 처리해준다.

## QueryRunner 클래스의 기능

QueryRunner 클래스는 JDBC 문의 실행, 결과 집합의 반복, 파라미터화된 쿼리 실행 등을 단순화합니다.

### 주요 기능:
- SQL 쿼리 실행
- PreparedStatement와 ResultSet의 처리 
- SQLException 처리

## QueryRunner의 장점

QueryRunner는 JDBC 코드를 간결하게 작성할 수 있도록 도와줍니다. 

### 간단한 예제
```java
import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanListHandler;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.List;

public class Example {
    public List<User> getUsers() {
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "username", "password");
        QueryRunner queryRunner = new QueryRunner();

        List<User> userList = queryRunner.query(conn, "SELECT * FROM users", new BeanListHandler<>(User.class));
        conn.close();

        return userList;
    }
}
```

위의 예제에서는 QueryRunner 클래스를 사용하여 데이터베이스에서 사용자 목록을 가져오는 간단한 코드를 볼 수 있습니다.

Apache DbUtils의 QueryRunner 클래스를 사용하면 JDBC 코드를 작성하는 과정을 단순화하고 생산성을 향상시킬 수 있습니다.

더 많은 정보를 원하시면 [공식 Apache DbUtils 웹사이트](https://commons.apache.org/proper/commons-dbutils/)를 참조하세요.

이상입니다. 감사합니다!