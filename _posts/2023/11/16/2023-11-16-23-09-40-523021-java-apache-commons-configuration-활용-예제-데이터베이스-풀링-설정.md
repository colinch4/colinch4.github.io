---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 데이터베이스 풀링 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java에서 데이터베이스 풀링을 구현하기 위해 Apache Commons Configuration 라이브러리를 사용할 수 있습니다. 이 라이브러리는 XML, Properties, JSON 등 다양한 형식의 설정 파일을 읽고 처리하는 기능을 제공합니다. 이번 예제에서는 Apache Commons Configuration을 사용하여 데이터베이스 풀링 설정을 구현하는 방법을 설명하겠습니다.

## 1. Apache Commons Configuration 라이브러리 추가하기

먼저, 프로젝트의 의존성에 Apache Commons Configuration 라이브러리를 추가해야 합니다. Maven을 사용하는 경우, pom.xml 파일에 다음과 같이 의존성을 추가합니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-configuration2</artifactId>
        <version>2.7</version>
    </dependency>
</dependencies>
```

Gradle을 사용하는 경우 build.gradle 파일에 다음과 같이 의존성을 추가합니다.

```groovy
dependencies {
    implementation 'org.apache.commons:commons-configuration2:2.7'
}
```

의존성을 추가한 후 프로젝트를 빌드하면 Apache Commons Configuration 라이브러리가 사용 가능해집니다.

## 2. 데이터베이스 풀링 설정 파일 작성하기

Apache Commons Configuration에서는 다양한 형식의 설정 파일을 사용할 수 있습니다. 이 예제에서는 XML 형식의 설정 파일을 사용하도록 하겠습니다.

풀링 설정을 저장하기 위해 `db-pool.xml` 파일을 작성합니다. 다음은 예시입니다.

```xml
<configuration>
    <datasource>
        <name>my-pool</name>
        <url>jdbc:mysql://localhost:3306/mydatabase</url>
        <username>username</username>
        <password>password</password>
        <maxConnections>10</maxConnections>
        <minConnections>2</minConnections>
        <idleTimeout>30000</idleTimeout>
    </datasource>
</configuration>
```

위 XML 파일은 `my-pool`이라는 이름의 데이터베이스 풀을 구성하는 설정을 포함하고 있습니다. URL, 사용자명, 비밀번호, 최대 연결 수, 최소 연결 수, 유휴 시간 등의 설정이 포함되어 있습니다.

## 3. 데이터베이스 풀 생성 및 설정 로드하기

이제 Java 코드에서 Apache Commons Configuration을 사용하여 데이터베이스 풀을 생성하고 설정 파일을 로드하는 방법을 알아보겠습니다.

```java
import org.apache.commons.configuration2.XMLConfiguration;
import org.apache.commons.dbcp2.BasicDataSource;

public class DbPoolExample {
    public static void main(String[] args) {
        try {
            XMLConfiguration config = new XMLConfiguration("db-pool.xml");
            BasicDataSource dataSource = new BasicDataSource();

            String name = config.getString("datasource.name");
            String url = config.getString("datasource.url");
            String username = config.getString("datasource.username");
            String password = config.getString("datasource.password");
            int maxConnections = config.getInt("datasource.maxConnections");
            int minConnections = config.getInt("datasource.minConnections");
            int idleTimeout = config.getInt("datasource.idleTimeout");

            dataSource.setDriverClassName("com.mysql.jdbc.Driver");
            dataSource.setUrl(url);
            dataSource.setUsername(username);
            dataSource.setPassword(password);
            dataSource.setMaxTotal(maxConnections);
            dataSource.setMinIdle(minConnections);
            dataSource.setMaxIdle(idleTimeout);

            // 획득한 DataSource를 사용하여 데이터베이스 작업 수행

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위 코드에서는 `XMLConfiguration`을 사용하여 `db-pool.xml`의 설정을 로드하고, `BasicDataSource`를 생성합니다. 설정 파일에서 각 항목의 값을 가져와 데이터베이스 풀의 속성을 설정합니다.

## 4. 데이터베이스 작업 수행하기

이제 `dataSource`를 사용하여 실제 데이터베이스 작업을 수행할 수 있습니다. 예를 들어, 연결된 데이터베이스에서 데이터를 가져오기 위한 코드는 다음과 같습니다.

```java
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

// ...

try (Connection connection = dataSource.getConnection();
     Statement statement = connection.createStatement();
     ResultSet resultSet = statement.executeQuery("SELECT * FROM mytable")) {
    while (resultSet.next()) {
        String data = resultSet.getString("data");
        // 데이터 처리 로직 수행
    }
} catch (Exception e) {
    e.printStackTrace();
}
```

위 코드에서는 `dataSource`에서 `Connection`을 획득하고, `Statement`을 생성하여 데이터베이스에서 데이터를 가져옵니다. 각각의 예외 처리가 포함되어 있으므로 안전하게 데이터베이스 작업을 수행할 수 있습니다.

## 결론

Apache Commons Configuration을 사용하여 Java에서 데이터베이스 풀링 설정을 구현하는 방법을 살펴보았습니다. 이러한 구성을 사용하면 XML, Properties, JSON 등 다양한 형식의 설정 파일을 사용하여 데이터베이스 풀을 설정할 수 있습니다. 이를 통해 데이터베이스 작업을 효율적이고 안정적으로 수행할 수 있습니다.

## 참고 자료

- [Apache Commons Configuration 문서](https://commons.apache.org/proper/commons-configuration/)
- [Apache Commons Configuration GitHub 저장소](https://github.com/apache/commons-configuration)