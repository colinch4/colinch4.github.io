---
layout: post
title: "[java] Java Byte Buddy를 사용한 ORM(Object Relational Mapping)"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

## 소개
ORM(Object Relational Mapping)은 객체 지향 프로그래밍 언어와 관계형 데이터베이스 간의 데이터를 변환하기 위한 기술입니다. Java에서는 다양한 ORM 프레임워크가 있지만, 이번에는 Byte Buddy를 사용하여 간단한 ORM을 구현해보겠습니다.

Byte Buddy는 Java에서 사용되는 코드 생성 및 조작 라이브러리로, 동적으로 클래스를 생성하고 수정하는 기능을 제공합니다. 따라서 ORM을 구현하기 위해 필요한 데이터베이스와의 연결, 쿼리 실행 등의 기능을 직접 구현할 수 있습니다.

## 설정
먼저 프로젝트에 Byte Buddy를 추가해야합니다. Maven을 사용하는 경우 다음과 같이 의존성을 추가합니다.

```xml
<dependency>
    <groupId>net.bytebuddy</groupId>
    <artifactId>byte-buddy</artifactId>
    <version>1.11.3</version>
</dependency>
```

## 예제
간단한 회원(Member) 객체와 데이터베이스 테이블(member_table)을 예로 사용하겠습니다.

```java
import net.bytebuddy.ByteBuddy;
import net.bytebuddy.implementation.MethodDelegation;
import net.bytebuddy.matcher.ElementMatchers;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class MemberORM {
    public static void main(String[] args) throws SQLException {
        // 데이터베이스 연결 정보 설정
        String url = "jdbc:mysql://localhost:3306/mydb";
        String username = "username";
        String password = "password";

        // 데이터베이스 연결
        Connection connection = DriverManager.getConnection(url, username, password);

        // 테이블 생성
        String createTableQuery = "CREATE TABLE member_table (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50))";
        PreparedStatement createTableStmt = connection.prepareStatement(createTableQuery);
        createTableStmt.executeUpdate();

        // 회원 정보 추가
        String insertQuery = "INSERT INTO member_table (name) VALUES (?)";
        PreparedStatement insertStmt = connection.prepareStatement(insertQuery);
        insertStmt.setString(1, "John Doe");
        insertStmt.executeUpdate();

        // 회원 정보 조회
        String selectQuery = "SELECT * FROM member_table";
        PreparedStatement selectStmt = connection.prepareStatement(selectQuery);
        ResultSet resultSet = selectStmt.executeQuery();

        while (resultSet.next()) {
            int id = resultSet.getInt("id");
            String name = resultSet.getString("name");
            System.out.println("ID: " + id + ", Name: " + name);
        }

        // 데이터베이스 연결 종료
        connection.close();
    }
}
```

위의 예제는 Byte Buddy를 사용하지 않은 일반적인 JDBC 코드입니다. 이제 Byte Buddy를 사용하여 ORM을 구현해보겠습니다.

```java
import net.bytebuddy.ByteBuddy;
import net.bytebuddy.implementation.MethodDelegation;
import net.bytebuddy.matcher.ElementMatchers;

import java.lang.reflect.InvocationTargetException;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class MemberORM {
    public static void main(String[] args) throws SQLException, NoSuchMethodException, InstantiationException, IllegalAccessException, InvocationTargetException {
        // 동적으로 생성한 클래스의 패키지 및 클래스명 설정
        String packageName = "com.example.orm";
        String className = "Member";

        // 데이터베이스 연결 정보 설정
        String url = "jdbc:mysql://localhost:3306/mydb";
        String username = "username";
        String password = "password";

        // 동적으로 생성한 클래스 생성
        Class<?> dynamicClass = new ByteBuddy()
                .subclass(Object.class)
                .name(packageName + "." + className)
                .make()
                .load(MemberORM.class.getClassLoader())
                .getLoaded();

        // 데이터베이스 연결
        Connection connection = DriverManager.getConnection(url, username, password);

        // 테이블 생성
        String createTableQuery = "CREATE TABLE member_table (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50))";
        PreparedStatement createTableStmt = connection.prepareStatement(createTableQuery);
        createTableStmt.executeUpdate();

        // 회원 정보 추가
        String insertQuery = "INSERT INTO member_table (name) VALUES (?)";
        PreparedStatement insertStmt = connection.prepareStatement(insertQuery);
        insertStmt.setString(1, "John Doe");
        insertStmt.executeUpdate();

        // 동적으로 생성한 클래스에 데이터베이스에서 조회한 데이터 저장
        List<Object> members = new ArrayList<>();
        String selectQuery = "SELECT * FROM member_table";
        PreparedStatement selectStmt = connection.prepareStatement(selectQuery);
        ResultSet resultSet = selectStmt.executeQuery();

        while (resultSet.next()) {
            Object member = dynamicClass.getDeclaredConstructor().newInstance();
            dynamicClass.getMethod("setId", int.class).invoke(member, resultSet.getInt("id"));
            dynamicClass.getMethod("setName", String.class).invoke(member, resultSet.getString("name"));
            members.add(member);
        }

        // 조회한 회원 정보 출력
        for (Object member : members) {
            System.out.println("ID: " + dynamicClass.getMethod("getId").invoke(member) +
                    ", Name: " + dynamicClass.getMethod("getName").invoke(member));
        }

        // 데이터베이스 연결 종료
        connection.close();
    }
}
```

위의 예제에서는 Byte Buddy를 사용하여 동적으로 Member 클래스를 생성하고, 데이터베이스에서 조회한 데이터를 해당 클래스에 저장하여 출력하는 간단한 ORM을 구현하였습니다.

## 결론
Java Byte Buddy를 사용하면 간단한 ORM을 만들 수 있습니다. Byte Buddy를 이용하면 동적으로 클래스를 생성하고 수정할 수 있으므로, 다양한 ORM 프레임워크를 작성하는 데 유용하게 활용할 수 있습니다.

## 참고 자료
- [Byte Buddy 공식 문서](http://bytebuddy.net)
- [Java Object Relational Mapping with Byte Buddy](https://www.baeldung.com/java-byte-buddy-orm)