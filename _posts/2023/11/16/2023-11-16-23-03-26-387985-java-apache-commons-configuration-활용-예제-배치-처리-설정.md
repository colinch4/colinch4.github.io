---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 배치 처리 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 자바에서 설정 파일을 읽고 관리할 수 있는 유용한 라이브러리입니다. 이 라이브러리를 사용하면 배치 처리 설정과 같은 복잡한 설정을 간편하게 처리할 수 있습니다.

## Apache Commons Configuration 설치

Apache Commons Configuration은 Maven을 통해 간편하게 설치할 수 있습니다. 아래의 의존성을 `pom.xml` 파일에 추가하여 라이브러리를 가져옵니다:

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>2.7</version>
</dependency>
```

## 배치 처리 설정 파일 만들기

먼저, 배치 처리 설정 파일을 만들어보겠습니다. 예를 들어, 아래와 같은 설정 파일을 작성하겠습니다:

```properties
# batch.properties

batch.size=100
batch.delay=5000
database.url=jdbc:mysql://localhost:3306/mydb
database.username=admin
database.password=secret
```

이 설정 파일은 배치 처리에서 사용할 배치 크기, 딜레이, 그리고 데이터베이스 접속 정보를 포함하고 있습니다.

## 설정 파일 읽기

이제 Java 코드에서 설정 파일을 읽어와서 처리해보겠습니다:

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.ConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Configurations;

public class BatchConfiguration {
    private int batchSize;
    private int batchDelay;
    private String databaseUrl;
    private String databaseUsername;
    private String databasePassword;

    public BatchConfiguration() {
        try {
            Configurations configs = new Configurations();
            Configuration config = configs.properties("batch.properties");

            batchSize = config.getInt("batch.size");
            batchDelay = config.getInt("batch.delay");
            databaseUrl = config.getString("database.url");
            databaseUsername = config.getString("database.username");
            databasePassword = config.getString("database.password");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public int getBatchSize() {
        return batchSize;
    }

    public int getBatchDelay() {
        return batchDelay;
    }

    public String getDatabaseUrl() {
        return databaseUrl;
    }

    public String getDatabaseUsername() {
        return databaseUsername;
    }

    public String getDatabasePassword() {
        return databasePassword;
    }
}
```

위의 코드는 `batch.properties` 파일을 읽어와서 설정 값을 가져오는 간단한 예제입니다. 이때, `Configurations` 객체를 사용하여 설정 파일을 읽어오고, `Configuration` 객체를 통해 설정 값을 가져옵니다.

## 설정 값 사용하기

이제 설정 값을 사용하는 예제를 보겠습니다:

```java
public class BatchProcessor {
    private BatchConfiguration configuration;

    public BatchProcessor() {
        configuration = new BatchConfiguration();
    }
    
    public void processBatch() {
        int batchSize = configuration.getBatchSize();
        int batchDelay = configuration.getBatchDelay();
        String databaseUrl = configuration.getDatabaseUrl();
        String databaseUsername = configuration.getDatabaseUsername();
        String databasePassword = configuration.getDatabasePassword();

        // 배치 처리 로직 구현
    }
}
```

위의 코드는 `BatchConfiguration` 객체를 생성하여 설정 값을 가져온 다음, 해당 설정 값을 사용하여 배치 처리를 수행하는 예제입니다.

## 결론

Java Apache Commons Configuration을 활용하면 복잡한 설정 파일을 쉽게 읽고 처리할 수 있습니다. 이를 통해 배치 처리와 같은 작업에서 유연성과 편리성을 높일 수 있습니다.

---

참고 문서:
- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/userguide/index.html)