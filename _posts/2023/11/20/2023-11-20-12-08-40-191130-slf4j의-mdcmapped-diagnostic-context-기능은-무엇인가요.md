---
layout: post
title: "[java] SLF4J의 MDC(Mapped Diagnostic Context) 기능은 무엇인가요?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

SLF4J는 Java 어플리케이션에서 로깅 기능을 제공하는 인기 있는 라이브러리입니다. MDC는 SLF4J의 중요한 기능 중 하나로, 로깅 이벤트에 관련된 추가 정보를 디버깅 목적으로 제공하는 것입니다.

MDC는 스레드로부터 로그 문맥 정보를 이어받아서 사용할 수 있도록 해주는 맵 형태의 구조입니다. 로깅을 수행하는 각 스레드는 자체 MDC 인스턴스를 갖고 있으며, 필요에 따라 값을 설정할 수 있습니다. 이 상태는 로깅 이벤트에 추가 정보로 포함되어 기록됩니다.

MDC는 다양한 상황에서 유용하게 사용될 수 있습니다. 예를 들어, 웹 애플리케이션에서는 각 요청 처리 중에 MDC를 사용하여 요청 ID, 사용자 로그인 정보 등을 할당하고, 해당 정보가 로깅 이벤트와 연결되도록 할 수 있습니다. 이를 통해 디버깅 시 해당 이벤트와 관련된 모든 로그를 추적하기 쉽습니다.

아래는 MDC를 사용하는 예시 코드입니다.

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;

public class ExampleClass {

    private static final Logger LOGGER = LoggerFactory.getLogger(ExampleClass.class);

    public void processRequest(String requestId) {
        MDC.put("requestId", requestId);
        LOGGER.info("Processing request");
        // 요청 처리 로직
        LOGGER.info("Request processed");
        MDC.remove("requestId");
    }

}
```

위의 예시 코드에서는 `processRequest` 메소드에서 MDC를 사용하여 `requestId`를 로깅 문맥에 설정합니다. 로깅 이벤트에서는 해당 값을 사용하여 각 요청에 대한 정보를 기록합니다. `MDC.remove()`를 호출하여 스레드 로컬에서 MDC를 제거해야 합니다.

MDC는 로깅 시 디버그의 용이성을 높여주는 강력한 도구입니다. SLF4J를 사용하는 개발자라면 MDC의 기능과 활용법을 숙지하고, 필요한 경우 로그 문맥 정보를 추가하여 디버깅을 지원할 수 있습니다.

더 자세한 내용은 [SLF4J MDC 문서](https://www.slf4j.org/manual.html#mdc)를 참조하세요.