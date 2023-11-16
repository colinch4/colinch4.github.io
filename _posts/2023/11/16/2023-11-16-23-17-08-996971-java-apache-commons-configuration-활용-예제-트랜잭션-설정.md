---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 트랜잭션 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 어플리케이션에서 구성 파일을 쉽게 읽고 사용할 수 있게 도와주는 라이브러리입니다. 이번 예제에서는 Apache Commons Configuration을 사용하여 트랜잭션 설정을 관리하는 방법에 대해 알아보겠습니다.

## 1. Apache Commons Configuration 의존성 추가

먼저, Maven 프로젝트에서 Apache Commons Configuration을 사용하려면 의존성을 추가해야 합니다. `pom.xml` 파일에 다음과 같은 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

## 2. 트랜잭션 설정 파일 생성

다음으로, 트랜잭션 설정을 관리할 `transaction-config.properties` 파일을 생성합니다. 이 파일은 프로젝트의 클래스패스에 위치해야 합니다. 예를 들어, `src/main/resources` 디렉토리에 파일을 생성할 수 있습니다. 다음은 `transaction-config.properties` 파일의 내용입니다:

```properties
transaction.timeout.seconds=60
transaction.retry.count=3
transaction.isolation.level=READ_COMMITTED
```

위의 예제에서는 트랜잭션의 타임아웃 시간, 재시도 횟수, 고립 수준을 설정하고 있습니다.

## 3. Apache Commons Configuration으로 트랜잭션 설정 읽기

이제 Java 코드에서 Apache Commons Configuration을 사용하여 트랜잭션 설정을 읽어올 수 있습니다. 다음은 예제 코드입니다:

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.fluent.Configurations;

public class TransactionConfiguration {

    private static final String CONFIG_FILE = "transaction-config.properties";

    private Configuration config;

    public TransactionConfiguration() {
        Configurations configs = new Configurations();
        try {
            config = configs.properties(CONFIG_FILE);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }

    public int getTransactionTimeout() {
        return config.getInt("transaction.timeout.seconds");
    }

    public int getTransactionRetryCount() {
        return config.getInt("transaction.retry.count");
    }

    public String getTransactionIsolationLevel() {
        return config.getString("transaction.isolation.level");
    }

    public static void main(String[] args) {
        TransactionConfiguration transactionConfig = new TransactionConfiguration();
        System.out.println("Transaction Timeout: " + transactionConfig.getTransactionTimeout());
        System.out.println("Transaction Retry Count: " + transactionConfig.getTransactionRetryCount());
        System.out.println("Transaction Isolation Level: " + transactionConfig.getTransactionIsolationLevel());
    }
}
```

위의 코드는 `transaction-config.properties` 파일에서 트랜잭션 설정을 읽어오는 간단한 클래스를 보여줍니다. `Configurations` 객체를 사용하여 `transaction-config.properties` 파일을 로드하고, `Configuration` 객체를 통해 설정값을 가져올 수 있습니다.

위의 코드를 실행하면 다음과 같은 출력결과를 얻을 수 있습니다:

```
Transaction Timeout: 60
Transaction Retry Count: 3
Transaction Isolation Level: READ_COMMITTED
```

## 4. 결론

이번 예제에서는 Apache Commons Configuration을 사용하여 Java 어플리케이션에서 트랜잭션 설정을 관리하는 방법을 알아보았습니다. Apache Commons Configuration은 구성 파일을 쉽게 읽고 사용할 수 있는 유용한 라이브러리입니다. 추가적인 설정이 필요한 경우 Apache Commons Configuration의 문서와 예제를 참고하시기 바랍니다.

## 참고 자료

- [Apache Commons Configuration Documentation](https://commons.apache.org/proper/commons-configuration/userguide/index.html)
- [Apache Commons Configuration GitHub Repository](https://github.com/apache/commons-configuration)