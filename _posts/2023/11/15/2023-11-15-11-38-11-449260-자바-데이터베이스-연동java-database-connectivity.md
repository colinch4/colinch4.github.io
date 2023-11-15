---
layout: post
title: "[java] 자바 데이터베이스 연동(Java database connectivity)"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

자바는 데이터베이스와의 연결과 상호작용을 하는데에 널리 사용되는 언어입니다. 이를 가능하게 하는 기술이 **Java Database Connectivity** 또는 **JDBC** 입니다. JDBC는 자바 프로그램 내에서 데이터베이스와의 통신을 위한 일련의 API와 명세를 제공합니다. 이를 통해 자바 애플리케이션에서 데이터베이스와의 연결, 데이터 검색 및 조작, 트랜잭션 처리 등을 수행할 수 있습니다.

## JDBC 드라이버 설치

먼저, JDBC를 사용하기 위해서는 해당 데이터베이스와 연동할 수 있는 JDBC 드라이버를 설치해야 합니다. 대부분의 데이터베이스 제조사들은 공식 JDBC 드라이버를 제공하고 있습니다. 이 드라이버는 해당 데이터베이스에 접속하고 데이터를 처리하기 위한 기능들을 구현한 라이브러리입니다. 각 데이터베이스 제조사의 공식 웹사이트에서 JDBC 드라이버를 다운로드할 수 있습니다.

## 데이터베이스 연결

JDBC를 사용하여 데이터베이스와 연결하기 위해서는 아래와 같은 단계를 따라야 합니다.

1. JDBC 드라이버를 클래스패스에 추가합니다.
2. 데이터베이스에 연결하기 위한 URL과 사용자 인증 정보를 지정합니다.
3. JDBC 드라이버를 로드합니다.
4. Connection 객체를 생성하여 데이터베이스에 연결합니다.

예시 코드는 다음과 같습니다.

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/mydatabase";
        String username = "myusername";
        String password = "mypassword";

        try {
            // JDBC 드라이버 로드
            Class.forName("com.mysql.jdbc.Driver");

            // 데이터베이스 연결
            Connection connection = DriverManager.getConnection(url, username, password);

            // 연결 성공
            System.out.println("데이터베이스에 연결되었습니다.");
            
            // 연결 종료
            connection.close();
        } catch (ClassNotFoundException e) {
            System.out.println("JDBC 드라이버를 찾을 수 없습니다.");
        } catch (SQLException e) {
            System.out.println("데이터베이스 연결에 실패했습니다.");
            e.printStackTrace();
        }
    }
}
```

위의 코드에서, `url` 변수에는 데이터베이스의 URL을, `username` 변수에는 사용자명, `password` 변수에는 비밀번호를 입력합니다. `Class.forName()` 메소드를 사용하여 JDBC 드라이버를 로드한 후, `DriverManager.getConnection()` 메소드를 호출하여 데이터베이스에 연결합니다. 연결에 성공하면 "데이터베이스에 연결되었습니다."라는 메시지가 출력되고, 연결을 종료합니다.

## 데이터베이스 작업

데이터베이스에 연결한 후, JDBC를 사용하여 데이터 조회, 삽입, 수정, 삭제 등의 작업을 할 수 있습니다. 이를 위해서는 SQL 쿼리를 사용하게 됩니다. 예를 들어, 데이터베이스에서 학생들의 정보를 조회하는 코드는 아래와 같습니다.

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DatabaseQuery {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/mydatabase";
        String username = "myusername";
        String password = "mypassword";

        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection connection = DriverManager.getConnection(url, username, password);

            // SQL 쿼리 실행
            String sql = "SELECT * FROM students";
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(sql);

            // 결과 출력
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                int age = resultSet.getInt("age");

                System.out.println("ID: " + id + ", 이름: " + name + ", 나이: " + age);
            }

            resultSet.close();
            statement.close();
            connection.close();
        } catch (ClassNotFoundException e) {
            System.out.println("JDBC 드라이버를 찾을 수 없습니다.");
        } catch (SQLException e) {
            System.out.println("데이터베이스 연결에 실패했습니다.");
            e.printStackTrace();
        }
    }
}
```

위의 코드는 `students` 테이블의 모든 레코드를 조회하여 결과를 출력하는 예시입니다. SQL 쿼리는 `Statement.executeQuery()` 메소드를 통해 실행하고, 결과는 `ResultSet` 객체에 저장됩니다. 결과를 가져와서 필요한 정보를 추출한 후 출력합니다.

## 결론

JDBC는 자바 애플리케이션과 데이터베이스 간의 효율적인 통신을 가능하게 해주는 중요한 기술입니다. 위에서 제시한 예시 코드를 기반으로 자신의 데이터베이스에 연결하고 다양한 작업을 수행해 보세요. JDBC의 자세한 사용법은 [공식 문서](https://docs.oracle.com/javase/tutorial/jdbc/index.html) 를 참조하시기 바랍니다.