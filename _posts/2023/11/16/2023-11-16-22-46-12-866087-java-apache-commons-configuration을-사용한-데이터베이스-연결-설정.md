---
layout: post
title: "[java] Java Apache Commons Configuration을 사용한 데이터베이스 연결 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이 블로그 포스트에서는 Java 언어와 Apache Commons Configuration 라이브러리를 사용하여 데이터베이스 연결 설정을하는 방법을 알아보겠습니다.

## Apache Commons Configuration 소개

Apache Commons Configuration은 Java 언어에서 구성 파일을 로드하고 처리하는 데 도움이되는 라이브러리입니다. 이 라이브러리를 사용하면 다양한 형식의 구성 파일을 읽고 쓸 수 있으며, 손쉽게 구성 데이터를 사용할 수 있습니다.

## 데이터베이스 연결 설정

데이터베이스 연결을 설정하기 위해 먼저 Apache Commons Configuration을 프로젝트에 추가해야합니다. Maven을 사용하는 경우 Maven 종속성 파일에 다음 종속성을 추가하십시오.

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

이제 데이터베이스 연결 정보를 저장하는 구성 파일을 작성해야합니다. 예를 들어, `db.properties`라는 파일을 생성하고 다음과 같은 형식으로 연결 정보를 작성합니다.

```properties
db.url=jdbc:mysql://localhost:3306/mydatabase
db.username=myusername
db.password=mypassword
```

위의 예제에서는 MySQL 데이터베이스에 연결하기 위한 URL, 사용자 이름 및 암호를 설정합니다.

이제 Java 코드에서 구성 파일을 로드하고 설정 값을 사용하여 데이터베이스에 연결할 수 있습니다. 다음은 이 작업을 수행하는 예제 코드입니다.

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBConnectionUtil {
    private static Connection connection;

    public static Connection getConnection() throws ConfigurationException, SQLException {
        if (connection != null && !connection.isClosed()) {
            return connection;
        }

        PropertiesConfiguration config = new PropertiesConfiguration("db.properties");
        String url = config.getString("db.url");
        String username = config.getString("db.username");
        String password = config.getString("db.password");

        connection = DriverManager.getConnection(url, username, password);
        return connection;
    }
}
```

위의 코드에서는 `db.properties` 파일을 로드하여 데이터베이스 URL, 사용자 이름 및 암호를 가져온 다음 `DriverManager`를 사용하여 데이터베이스에 연결합니다. `getConnection` 메서드를 호출하면 이미 연결이 열려있는 경우 기존 연결을 반환하며, 그렇지 않은 경우 새로운 연결을 만듭니다.

이제 다음과 같이 코드에서 `DBConnectionUtil.getConnection()`을 호출하여 데이터베이스 연결을 가져올 수 있습니다.

```java
try {
    Connection connection = DBConnectionUtil.getConnection();
    // 데이터베이스 작업 수행
} catch (ConfigurationException | SQLException e) {
    e.printStackTrace();
}
```

위의 코드에서 예외 처리를 추가하여 구성 파일 로드 또는 데이터베이스 연결 오류에 대비해야합니다.

## 마무리

이 블로그 포스트에서는 Java 언어와 Apache Commons Configuration을 사용하여 데이터베이스 연결 설정하는 방법을 살펴보았습니다. 이를 통해 데이터베이스 연결 정보를 외부 구성 파일로 이동시키고 코드에서 유연하게 사용할 수 있습니다. 이를 통해 코드의 유지 보수성과 재사용성을 향상시킬 수 있습니다.

데이터베이스 연결 설정에 대한 추가 정보를 찾으려면 [공식 Apache Commons Configuration 문서](https://commons.apache.org/proper/commons-configuration/)를 참조하십시오.