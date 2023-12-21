---
layout: post
title: "[java] Apache DbUtils의 ORM(Object-Relational Mapping) 지원"
description: " "
date: 2023-12-21
tags: [java]
comments: true
share: true
---

Apache DbUtils는 데이터베이스와의 상호작용을 쉽게 하기 위한 유틸리티 라이브러리이다. 하지만 기본적으로 ORM(Object-Relational Mapping)을 제공하지는 않는다. 그러나 Apache DbUtils를 사용하여 ORM을 구현하는 것은 가능하다. 

이 블로그에서는 Apache DbUtils를 사용하여 Java 어플리케이션에서 간단한 ORM을 구현하는 방법에 대해 다루고자 한다.

## Apache DbUtils 소개

Apache DbUtils는 Apache Commons 프로젝트의 일부로, JDBC 코드의 반복을 최소화하고 조회 및 업데이트를 간편하게 만들기 위한 간단한 JDBC 유틸리티 라이브러리이다. 

## ORM (Object-Relational Mapping) 이란?

ORM은 객체 지향 프로그래밍 언어와 관계형 데이터베이스 사이의 데이터를 변환하는 프로그래밍 기술이다. 이를 통해 객체와 데이터베이스 간의 데이터 변환 문제를 해결할 수 있으며, SQL 쿼리를 직접 작성하지 않고도 데이터를 쉽게 조작할 수 있다.

## Apache DbUtils를 사용한 간단한 ORM 구현

Apache DbUtils는 JDBC 코드를 간소화하기 위한 유틸리티이므로 ORM을 지원하지 않는다. 그러나 Apache Commons 프로젝트 내에는 Apache DBCP(DataBase Connection Pool)와 Apache JDBC Transaction Pool 라이브러리 중 하나를 사용하여 ORM을 구현할 수 있는 여러 방법이 제공된다.

아래는 Apache DbUtils에서 ORM을 구현하는 간단한 예제이다.

### 예제 코드

```java
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.dbutils.DbUtils;
import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;
import org.apache.commons.dbutils.handlers.BeanListHandler;

public class UserDao {

    private Connection connection;

    public UserDao(Connection connection) {
        this.connection = connection;
    }

    public User getUser(int id) throws SQLException {
        QueryRunner queryRunner = new QueryRunner();
        String sql = "SELECT * FROM users WHERE id = ?";
        User user = queryRunner.query(connection, sql, new BeanHandler<>(User.class), id);
        return user;
    }

    public List<User> getAllUsers() throws SQLException {
        QueryRunner queryRunner = new QueryRunner();
        String sql = "SELECT * FROM users";
        List<User> users = queryRunner.query(connection, sql, new BeanListHandler<>(User.class));
        return users;
    }

    public void saveUser(User user) throws SQLException {
        QueryRunner queryRunner = new QueryRunner();
        String sql = "INSERT INTO users (name, email) VALUES (?, ?)";
        queryRunner.update(connection, sql, user.getName(), user.getEmail());
    }

    public void updateUser(User user) throws SQLException {
        QueryRunner queryRunner = new QueryRunner();
        String sql = "UPDATE users SET name = ?, email = ? WHERE id = ?";
        queryRunner.update(connection, sql, user.getName(), user.getEmail(), user.getId());
    }

    public void deleteUser(int id) throws SQLException {
        QueryRunner queryRunner = new QueryRunner();
        String sql = "DELETE FROM users WHERE id = ?";
        queryRunner.update(connection, sql, id);
    }
}
```

위의 코드에서 사용된 `User` 클래스는 데이터베이스의 테이블 구조와 매핑되는 자바 빈(Java Bean) 클래스이다.

### 결과

위의 예제는 Apache DbUtils를 사용하여 데이터베이스에서 User 객체를 조회하고 저장하는 간단한 ORM을 구현한 것이다. 이러한 방식으로 Apache DbUtils를 사용하여 ORM을 구현할 수 있다.

## 결론

Apache DbUtils는 기본적으로 ORM을 지원하지 않지만, Apache Commons 프로젝트의 다른 라이브러리와의 결합을 통해 ORM을 구현할 수 있다. 위의 예제처럼 Apache DbUtils와 BeanHandler, BeanListHandler를 사용하여 데이터베이스와의 상호작용을 간편하게 구현할 수 있다.

Apache Commons DbUtils 공식 문서를 참조하여 더 많은 정보를 얻을 수 있다.

이상으로 Apache DbUtils의 ORM 지원에 대한 블로그 포스트를 마치겠다.

[Apache Commons DbUtils 공식 문서](https://commons.apache.org/proper/commons-dbutils/)