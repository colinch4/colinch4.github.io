---
layout: post
title: "[java] SLF4J와 JUL(java.util.logging) 사용하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

## 개요
SLF4J와 JUL(java.util.logging)은 자바 어플리케이션에서 로깅(logging) 기능을 제공하기 위한 라이브러리입니다. 로깅은 어플리케이션의 동작 상태 정보를 기록하고, 디버깅 및 문제 해결에 도움을 줍니다. 이 글에서는 SLF4J와 JUL의 사용법을 간단히 설명하고, 이 둘을 함께 사용하는 방법을 알아보겠습니다.

## SLF4J 사용하기
SLF4J는 로깅 인터페이스를 제공하며, 실제 로깅 기능은 백엔드(logging backend)인 Logback, Log4j 등과 같은 다른 로깅 구현체에서 제공합니다. 아래는 SLF4J를 사용하여 로깅하는 예제 코드입니다.

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MyLogger {
    private static final Logger LOGGER = LoggerFactory.getLogger(MyLogger.class);

    public void myMethod() {
        LOGGER.debug("This is a debug message.");
        LOGGER.info("This is an info message.");
        LOGGER.warn("This is a warning message.");
        LOGGER.error("This is an error message.");
    }
}
```

위 코드에서는 `org.slf4j.Logger` 인터페이스를 사용하여 로깅 메시지를 기록하고 있습니다. `LoggerFactory.getLogger()` 메서드를 사용하여 로거(Logger) 인스턴스를 가져올 수 있습니다. 로거 인스턴스를 통해 로그 레벨(debug, info, warn, error)에 따라 메시지를 기록할 수 있습니다.

## JUL(JUL(java.util.logging)) 사용하기
JUL은 자바 표준 라이브러리인 java.util.logging의 약자입니다. JUL을 사용하려면 Logger 클래스를 사용해야 합니다. 아래는 JUL을 사용하여 로깅하는 예제 코드입니다.

```java
import java.util.logging.Logger;

public class MyLogger {
    private static final Logger LOGGER = Logger.getLogger(MyLogger.class.getName());

    public void myMethod() {
        LOGGER.severe("This is a severe message.");
        LOGGER.warning("This is a warning message.");
        LOGGER.info("This is an info message.");
        LOGGER.config("This is a config message.");
        LOGGER.fine("This is a fine message.");
        LOGGER.finer("This is a finer message.");
        LOGGER.finest("This is a finest message.");
    }
}
```

위 코드에서는 `java.util.logging.Logger` 클래스를 사용하여 로깅 메시지를 기록하고 있습니다. `Logger.getLogger()` 메서드를 사용하여 로거 인스턴스를 가져올 수 있습니다. 로거 인스턴스를 통해 로그 레벨(severe, warning, info, config, fine, finer, finest)에 따라 메시지를 기록할 수 있습니다.

## SLF4J와 JUL 함께 사용하기
만약 SLF4J와 JUL을 함께 사용하고 싶다면, JUL을 SLF4J의 백엔드(logging backend)로 설정해야 합니다. 이를 위해 `jul-to-slf4j`라는 어댑터를 사용할 수 있습니다. 아래는 Maven을 사용하여 `jul-to-slf4j` 어댑터를 추가하는 예제 코드입니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>jul-to-slf4j</artifactId>
        <version>1.7.32</version>
    </dependency>
</dependencies>
```

위 코드에 따르면 SLF4J의 버전 1.7.32 이후로 `jul-to-slf4j` 어댑터를 의존성으로 추가할 수 있습니다. 이렇게 하면 JUL이 SLF4J를 통해 로깅되게 됩니다.

## 참고 자료
- [SLF4J 공식 사이트](http://www.slf4j.org/)
- [JUL(JUL(java.util.logging)) 공식 문서](https://docs.oracle.com/en/java/javase/14/docs/api/java.logging/java/util/logging/package-summary.html)

SLF4J와 JUL은 자바 어플리케이션에서 로깅 기능을 효율적으로 사용할 수 있도록 도와줍니다. 적절한 라이브러리 선택과 설정을 통해 로그 메시지를 통해 어플리케이션의 동작 상태를 파악하고, 문제를 해결하는 데 도움을 받을 수 있습니다.