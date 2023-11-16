---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 데이터베이스 연결 풀 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

## 소개

Apache Commons Configuration은 자바 프로젝트에서 구성 파일을 읽고 쓰는 데 사용되는 라이브러리입니다. 이를 활용하여 데이터베이스 연결 풀 설정을 예제로 살펴보겠습니다.

## 설정 파일 작성

먼저 `database.properties`라는 이름의 설정 파일을 작성합니다. 이 파일은 다음과 같은 형식으로 작성됩니다:

```properties
# 데이터베이스 연결 정보
db.host=localhost
db.port=3306
db.name=testdb
db.username=testuser
db.password=testpassword

# 데이터베이스 연결 풀 설정
db.pool.maxIdle=10
db.pool.minIdle=5
db.pool.maxTotal=20
```

위에서 설정한 값들은 데이터베이스 연결 정보와 데이터베이스 연결 풀 설정을 위한 값들입니다.

## 코드 작성

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilderProperties;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class DatabaseConfigExample {
    public static void main(String[] args) {
        // 설정 파일 빌더 생성
        FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
                new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                        .configure(FileBasedConfigurationBuilderProperties.fileBased()
                                .setFile(new File("database.properties")));

        try {
            // 설정 파일 로딩
            Configuration config = builder.getConfiguration();

            // 데이터베이스 연결 정보 가져오기
            String host = config.getString("db.host");
            int port = config.getInt("db.port");
            String dbName = config.getString("db.name");
            String username = config.getString("db.username");
            String password = config.getString("db.password");

            // 데이터베이스 연결 풀 설정 가져오기
            int maxIdle = config.getInt("db.pool.maxIdle");
            int minIdle = config.getInt("db.pool.minIdle");
            int maxTotal = config.getInt("db.pool.maxTotal");

            // 설정 값 출력
            System.out.println("Database Connection Info:");
            System.out.println("Host: " + host);
            System.out.println("Port: " + port);
            System.out.println("Database Name: " + dbName);
            System.out.println("Username: " + username);
            System.out.println("Password: " + password);

            System.out.println("\nDatabase Connection Pool Configuration:");
            System.out.println("Max Idle Connections: " + maxIdle);
            System.out.println("Min Idle Connections: " + minIdle);
            System.out.println("Max Total Connections: " + maxTotal);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위 코드는 Apache Commons Configuration을 사용하여 `database.properties` 파일에서 데이터베이스 연결 정보와 데이터베이스 연결 풀 설정을 읽어오는 예제입니다. 설정 파일로부터 값을 읽어온 후, 해당 값을 출력합니다.

## 실행 결과

위 코드를 실행하면 다음과 같은 결과를 얻을 수 있습니다:

```
Database Connection Info:
Host: localhost
Port: 3306
Database Name: testdb
Username: testuser
Password: testpassword

Database Connection Pool Configuration:
Max Idle Connections: 10
Min Idle Connections: 5
Max Total Connections: 20
```

위 결과는 설정 파일에 저장된 값들을 정상적으로 읽어와 출력한 것입니다.

## 결론

Apache Commons Configuration을 사용하면 자바 프로젝트에서 구성 파일을 쉽게 읽고 쓸 수 있습니다. 이 예제를 통해 데이터베이스 연결 풀 설정을 읽어오는 방법을 살펴보았습니다. 이와 유사한 방법으로 다른 설정 값을 읽어올 수도 있습니다. 자세한 내용은 [Apache Commons Configuration 문서](https://commons.apache.org/proper/commons-configuration/)를 참조하십시오.