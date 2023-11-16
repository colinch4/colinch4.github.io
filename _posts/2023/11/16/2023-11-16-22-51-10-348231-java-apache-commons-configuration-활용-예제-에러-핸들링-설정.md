---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 에러 핸들링 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 자바에서 설정 파일을 읽고 파싱하는 데 사용되는 유용한 라이브러리입니다. 이 라이브러리를 사용하면 간단한 설정 파일을 읽어와 애플리케이션에서 사용할 수 있는 속성을 추출하고 조작할 수 있습니다. 이번 예제에서는 Apache Commons Configuration을 사용하여 에러 핸들링 설정을 처리하는 방법을 알아보겠습니다.

## 설정 파일을 읽기

먼저, Apache Commons Configuration을 사용하여 설정 파일을 읽는 방법을 살펴보겠습니다. 다음 예제 코드는 `config.properties`라는 설정 파일에서 값을 읽어옵니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class AppConfig {
    private static final String CONFIG_FILE = "config.properties";
    private static Configuration config;

    static {
        try {
            Configurations configs = new Configurations();
            config = configs.properties(CONFIG_FILE);
        } catch (ConfigurationException e) {
            System.err.println("Failed to read configuration file: " + e.getMessage());
        }
    }

    public static String getProperty(String key) {
        return config.getString(key);
    }
}
```

위의 코드에서 `config.properties` 파일은 클래스패스에 위치하고 있어야 합니다. 이렇게 파일을 읽은 후에는 `getProperty` 메서드를 사용하여 특정 속성을 추출할 수 있습니다.

## 에러 핸들링 설정

이제 설정 파일에서 읽은 값을 기반으로 에러 핸들링을 설정하는 예제를 살펴보겠습니다. 아래 코드는 `AppConfig` 클래스에 추가된 에러 핸들링 설정을 처리하는 코드입니다.

```java
public class ErrorHandling {
    public static void main(String[] args) {
        String logFilePath = AppConfig.getProperty("error.log.file");
        int maxRetryAttempts = Integer.parseInt(AppConfig.getProperty("error.retry.maxAttempts"));

        configureErrorHandling(logFilePath, maxRetryAttempts);
    }

    private static void configureErrorHandling(String logFilePath, int maxRetryAttempts) {
        // 에러 핸들링 설정을 수행하는 코드
        // 예를 들어, 로깅 파일 경로와 최대 재시도 횟수를 설정할 수 있습니다.
    }
}
```

위의 코드에서 `AppConfig.getProperty` 메서드를 사용하여 `config.properties` 파일에서 `error.log.file` 및 `error.retry.maxAttempts`라는 속성 값을 가져옵니다. 이렇게 가져온 값은 `configureErrorHandling` 메서드로 전달하여 실제 에러 핸들링 설정을 수행할 수 있습니다.

## 결론

위의 예제에서는 Apache Commons Configuration을 사용하여 설정 파일을 읽고, 읽은 값을 기반으로 에러 핸들링 설정을 처리하는 방법을 알아보았습니다. 이러한 방법을 활용하면 자바 애플리케이션에서 손쉽게 설정 파일을 관리하고, 애플리케이션 동작에 필요한 속성을 쉽게 가져올 수 있습니다.