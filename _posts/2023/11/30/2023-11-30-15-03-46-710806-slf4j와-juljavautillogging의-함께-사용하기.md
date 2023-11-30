---
layout: post
title: "[java] SLF4J와 JUL(java.util.logging)의 함께 사용하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

SLF4J(Simple Logging Facade for Java)는 Java에서 많이 사용되는 로깅 라이브러리 중 하나입니다. 그러나 몇몇 Java 프레임워크는 내장된 로깅 라이브러리로 JUL(java.util.logging)을 사용합니다. 이러한 경우 SLF4J와 JUL을 함께 사용해야합니다. 이 글에서는 SLF4J와 JUL의 함께 사용하는 방법에 대해 알아보겠습니다.

## JUL을 SLF4J로 라우팅하기

SLF4J에서는 JUL 로깅을 라우트하는 **jul-to-slf4j** 모듈을 제공합니다. 이 모듈을 사용하면 JUL 로그가 SLF4J로 전달되어 SLF4J을 통해 로그를 출력할 수 있습니다.

의존성 설정 파일(pom.xml 또는 build.gradle)에 다음과 같이 **jul-to-slf4j** 모듈을 추가해주세요.

```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>jul-to-slf4j</artifactId>
        <version>1.7.30</version>
    </dependency>
    ...
</dependencies>
```

## 로깅 설정 변경하기

JUL은 java.util.logging 패키지를 사용하여 로깅을 처리합니다. 로깅 수준(Logging Level)은 JUL 프로퍼티를 통해 설정할 수 있습니다.

로깅 수준을 SLF4J로 라우팅하기 위해서는 **jul-to-slf4j** 모듈을 로드하도록 코드를 변경해야합니다. 애플리케이션의 진입점(main 메소드 등)에서 다음 코드를 추가해주세요.

```java
SLF4JBridgeHandler.removeHandlersForRootLogger();
SLF4JBridgeHandler.install();
```

이 코드는 기존의 JUL 핸들러를 제거하고 SLF4J 핸들러를 설치하여 SLF4J로 로깅을 라우팅합니다.

## 로그 파일 설정하기

SLF4J는 JUL을 통해 로그를 출력하므로, 로그 파일 설정은 JUL 설정 파일을 통해 변경할 수 있습니다. JUL은 **logging.properties** 파일을 사용하여 로깅 설정을 관리합니다.

**logging.properties** 파일에서 로그 파일 경로와 로깅 수준 등의 설정을 변경할 수 있습니다.

## 결론

SLF4J와 JUL을 함께 사용하면 프레임워크가 JUL을 내장하고 있을 때에도 SLF4J를 통해 통합된 로깅 처리를 할 수 있습니다. **jul-to-slf4j** 모듈을 사용하여 JUL 로깅을 SLF4J로 라우팅하고, JUL 설정 파일을 통해 로깅 설정을 관리할 수 있습니다.

JUL과 SLF4J를 함께 사용하여 로깅을 처리함으로써 코드의 유지보수성과 로깅 기능에 대한 통일성을 확보할 수 있습니다.

## 참고 자료

- [SLF4J - bridging API](http://www.slf4j.org/legacy.html#jul-to-slf4j)
- [JUL (java.util.logging) - SLF4J](http://www.slf4j.org/legacy.html#jul-to-slf4j)
- [java.util.logging (JUL) and SLF4J](http://www.slf4j.org/legacy.html#jul-to-slf4j)