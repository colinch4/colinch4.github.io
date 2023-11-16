---
layout: post
title: "[java] Java Apache Commons Configuration 예외 처리 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java에서 Apache Commons Configuration 라이브러리를 사용하여 구성 파일을 읽고 처리할 때 예외 처리는 중요합니다. 이 글에서는 Apache Commons Configuration에서 발생할 수 있는 예외를 처리하는 방법에 대해 알아보겠습니다.

## 예외 처리 방법

Apache Commons Configuration에서는 `ConfigurationException`이라는 예외 클래스를 사용합니다. `ConfigurationException`은 Apache Commons Configuration 라이브러리에서 발생하는 모든 예외의 부모 클래스입니다.

### 1. 예외 처리를 위한 try-catch 블록

Apache Commons Configuration을 사용할 때는 항상 예외 처리를 위한 try-catch 블록을 작성해야 합니다. 다음은 기본적인 예외 처리 방법의 예시입니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.ConfigurationException;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Configurations;

public class ConfigReader {

    public static void main(String[] args) {
        try {
            Configurations configs = new Configurations();
            Configuration config = configs.properties("config.properties"); // 예시로 properties 파일을 읽어옴
            // configuration 사용
        } catch (ConfigurationException e) {
            // 예외 처리 로직
        }
    }
}
```

try-catch 블록 내에서 발생하는 `ConfigurationException`을 캐치하여 예외 처리 로직을 작성할 수 있습니다.

### 2. 예외 발생 시 로그 출력

Apache Commons Configuration에서는 예외 발생 시 로그를 출력하는 기능을 제공합니다. 이를 활용하여 예외 메시지와 스택 트레이스를 로그로 출력할 수 있습니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.ConfigurationException;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ConfigReader {

    private static final Logger LOGGER = LoggerFactory.getLogger(ConfigReader.class);

    public static void main(String[] args) {
        try {
            Configurations configs = new Configurations();
            Configuration config = configs.properties("config.properties"); // 예시로 properties 파일을 읽어옴
            // configuration 사용
        } catch (ConfigurationException e) {
            LOGGER.error("Error reading configuration file: {}", e.getMessage());
            LOGGER.error("Stack trace:", e);
        }
    }
}
```

위 예시에서는 SLF4J와 같은 로깅 라이브러리를 사용하여 예외 발생 시 로그를 출력하고 있습니다. `LOGGER.error`를 사용하여 예외 메시지와 스택 트레이스를 출력하고 있습니다.

## 참고 자료

- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)
- [SLF4J 공식 문서](http://www.slf4j.org/)