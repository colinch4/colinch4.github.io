---
layout: post
title: "[java] Log4j의 MDC(Mapped Diagnostic Context) 개요"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Log4j는 다양한 로깅 기능을 제공하는 Java 어플리케이션의 대표적인 로깅 도구입니다. Log4j의 MDC(Mapped Diagnostic Context)는 로깅 시스템에 추가적인 정보를 제공하는데 사용되는 유용한 기능입니다. 이 기능은 로그 이벤트에 대한 컨텍스트 정보를 저장하고 관리할 수 있도록 해줍니다.

## MDC란 무엇인가요?

MDC는 스레드로컬(ThreadLocal)을 사용하여 로그 이벤트와 관련된 추가 정보를 저장하는데 사용되는 Log4j의 기능입니다. MDC를 사용하면 로그 출력에 컨텍스트 정보를 포함할 수 있으며, 이는 디버깅 및 로그 분석을 더욱 효과적으로 수행할 수 있도록 도와줍니다.

## MDC의 사용법 예시

MDC를 사용하기 위해서는 다음과 같은 단계를 따라야 합니다.

1. 필요한 컨텍스트 정보를 MDC에 저장합니다. Log4j에서는 MDC.put() 메소드를 사용하여 정보를 저장할 수 있습니다.

```java
import org.apache.log4j.MDC;

// 필요한 컨텍스트 정보를 MDC에 저장
MDC.put("userId", "john123");
MDC.put("ipAddress", "192.168.0.1");
```

2. 로깅 시 출력에 컨텍스트 정보를 포함하도록 설정합니다. Log4j 설정 파일(`log4j.properties` 또는 `log4j.xml`)에서 `%X{key}` 형식을 사용하여 MDC에 저장된 값을 출력할 수 있습니다.

```properties
log4j.appender.console.layout.ConversionPattern=%d [%X{userId}] [%X{ipAddress}] %p %c - %m%n
```

3. MDC에서 컨텍스트 정보를 제거합니다. 로그 이벤트 이후에는 MDC에서 컨텍스트 정보를 제거하여 메모리 누수를 방지해야 합니다.

```java
MDC.remove("userId");
MDC.remove("ipAddress");
```

## MDC의 활용 예시

MDC는 다양한 상황에서 유용하게 활용될 수 있습니다. 아래는 MDC를 활용한 예시입니다.

1. 사용자의 세션 ID를 MDC에 저장하여 모든 로그에 세션 정보 포함
2. 요청을 처리하는 IP 주소를 MDC에 저장하여 로그에 IP 정보 포함
3. 멀티스레드 환경에서 사용자의 요청을 식별하기 위해 MDC에 고유 식별자 저장

위와 같이 MDC를 활용하면 로그에 추가 정보를 포함하여 디버깅 및 분석 작업을 더욱 수월하게 수행할 수 있습니다.

## 참고 자료

- [Log4j 공식 문서](https://logging.apache.org/log4j/2.x/)
- [MDC Pattern Layout](https://logging.apache.org/log4j/2.x/manual/layouts.html#Pattern_Layout)