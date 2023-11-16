---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: DB 연결 풀 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이번 포스트에서는 Java에서 Apache Commons Configuration 라이브러리를 활용하여 DB 연결 풀 설정을 하는 예제를 소개하겠습니다. 

## Apache Commons Configuration란?

Apache Commons Configuration은 Java에서 설정 파일을 읽고 처리하는 라이브러리입니다. 다양한 설정 파일 형식을 지원하며, 설정 값을 손쉽게 읽고 쓸 수 있는 편리한 기능을 제공합니다. 

## DB 연결 풀 설정 예제

```java
import org.apache.commons.configuration2.*;
import org.apache.commons.configuration2.builder.fluent.Configurations;

public class DBConnectionPoolConfiguration {

    public static void main(String[] args) throws ConfigurationException {
        // 설정 파일 로드
        Configurations configs = new Configurations();
        Configuration config = configs.properties("config.properties");

        // 설정 값 읽기
        String dbUrl = config.getString("db.url");
        String dbUsername = config.getString("db.username");
        String dbPassword = config.getString("db.password");
        int maxConnections = config.getInt("db.maxConnections");

        // DB 연결 풀 구성
        ConnectionPool pool = new ConnectionPool(maxConnections);
        pool.setUrl(dbUrl);
        pool.setUsername(dbUsername);
        pool.setPassword(dbPassword);

        // DB 연결 풀 사용 예시
        Connection conn = pool.getConnection();
        // ...

        // 사용한 자원 반환
        conn.close();
        pool.close();
    }
}
```

위 예제에서는 `config.properties` 파일을 읽어와 DB 연결 풀에 필요한 설정 값을 가져오고, 해당 값들을 사용하여 DB 연결 풀을 구성합니다. `ConnectionPool` 클래스는 실제로 DB 연결을 수행하고, `getConnection()` 메서드를 통해 연결을 얻을 수 있습니다. 

## 설정 파일 예시 (config.properties)

```properties
db.url=jdbc:mysql://localhost:3306/mydb
db.username=myusername
db.password=mypassword
db.maxConnections=10
```

위 설정 파일은 MySQL 데이터베이스에 대한 연결 정보를 포함하고 있습니다. 실제로 사용하는 데이터베이스의 URL, 사용자명, 비밀번호, 최대 연결 수를 설정 파일에 맞게 수정하여 사용해야 합니다.

## 참고 자료

- Apache Commons Configuration 공식 문서: [https://commons.apache.org/proper/commons-configuration/](https://commons.apache.org/proper/commons-configuration/)
- Apache Commons Configuration GitHub 저장소: [https://github.com/apache/commons-configuration](https://github.com/apache/commons-configuration)

이번 포스트에서는 Java에서 Apache Commons Configuration을 사용하여 DB 연결 풀을 설정하는 예제를 살펴보았습니다. 설정 파일로부터 필요한 값을 읽어와 DB 연결 풀을 구성하는 방법을 알아봤습니다. Apache Commons Configuration은 다양한 설정 파일 형식을 지원하므로, 여러 종류의 설정 파일을 사용하는 Java 프로젝트에서 유용하게 활용할 수 있습니다.