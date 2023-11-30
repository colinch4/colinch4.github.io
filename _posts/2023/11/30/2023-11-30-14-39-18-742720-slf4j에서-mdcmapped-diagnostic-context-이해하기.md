---
layout: post
title: "[java] SLF4J에서 MDC(Mapped Diagnostic Context) 이해하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

MDC (Mapped Diagnostic Context)는 SLF4J (Simple Logging Facade for Java)에서 제공하는 기능으로, 로깅 이벤트에 대한 추가적인 컨텍스트 정보를 제공합니다. MDC를 사용하면 각각의 로그 이벤트에 고유한 식별자 및 사용자 정의 정보를 추가할 수 있어 디버깅 및 로그 분석에 유용합니다.

## MDC란 무엇인가요?

Mapped Diagnostic Context (MDC)는 쉽게 말해 로그 이벤트의 컨텍스트 정보를 담는 맵이라고 생각할 수 있습니다. 이 맵은 스레드로컬(ThreadLocal) 변수를 사용하여 각각의 스레드에서 독립적으로 관리됩니다. MDC에서는 문자열 키와 그에 해당하는 값들을 저장할 수 있습니다.

예를 들어, 사용자의 세션 ID, 요청 ID, 사용자 이름 등과 같은 정보를 MDC에 저장할 수 있습니다. 이 정보들은 로그 이벤트와 함께 출력되어 해당 이벤트와 관련된 추가 정보를 확인할 수 있게 됩니다.

## MDC 사용 방법

MDC를 사용하려면 다음과 같은 단계를 따라야 합니다.

1. MDC에 값을 설정합니다. 값을 설정하기 위해서는 MDC 클래스의 `put` 메서드를 사용합니다.

   ```java
   import org.slf4j.MDC;
   
   // MDC에 세션 ID 설정
   MDC.put("sessionId", "123456");
   ```

   위의 예제에서는 "sessionId"라는 키에 "123456"이라는 값이 설정되었습니다.

2. 로그 메시지에서 MDC 값을 참조할 수 있습니다. MDC 값은 중괄호로 둘러 싸여 있는 특별한 패턴을 사용하여 참조할 수 있습니다.

   ```java
   import org.slf4j.Logger;
   import org.slf4j.LoggerFactory;
   
   public class MyLogger {
   
       private static final Logger logger = LoggerFactory.getLogger(MyLogger.class);
   
       public void logMyEvent() {
           // MDC 값을 로그 메시지에서 참조
           logger.info("My event occurred. Session ID: {}", MDC.get("sessionId"));
       }
   }
   ```

   위의 예제에서는 로그 메시지 내에 `{}` 패턴을 사용하여 MDC에 설정된 "sessionId" 값을 참조하고 있습니다.

3. MDC 값을 삭제합니다. 값을 삭제하기 위해서는 MDC 클래스의 `remove` 메서드를 사용합니다.

   ```java
   MDC.remove("sessionId");
   ```

   위의 예제에서는 "sessionId" 값을 MDC에서 삭제하여 해당 값에 대한 참조를 제거했습니다.

## MDC 사용 예시

MDC를 사용하여 세션 ID를 로그에 포함하는 예제를 보겠습니다.

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;

public class MyLogger {

    private static final Logger logger = LoggerFactory.getLogger(MyLogger.class);

    public void logMyEvent(String sessionId) {
        MDC.put("sessionId", sessionId);
        logger.info("My event occurred. Session ID: {}", sessionId);
        MDC.remove("sessionId");
    }
}
```

위의 예제에서는 `logMyEvent` 메서드에서 세션 ID를 받아와 MDC에 설정하고, 로그 메시지에서 MDC 값을 참조하여 출력합니다. 마지막으로 MDC에서 세션 ID 값을 삭제합니다.

## 결론

SLF4J의 MDC 기능을 사용하면 로깅 이벤트에 대한 추가 정보를 제공하는 것이 가능합니다. 이를 통해 로그를 분석하거나 디버깅할 때 더 많은 컨텍스트 정보를 확인할 수 있습니다. MDC는 다중 스레드 환경에서 안전하게 사용할 수 있도록 설계되어 있으므로, 복잡한 애플리케이션에서도 신뢰성 있게 활용할 수 있습니다.

---

참고 자료:

- SLF4J MDC documentation: [https://www.slf4j.org/manual.html#mdc](https://www.slf4j.org/manual.html#mdc)
- SLF4J API documentation: [https://www.slf4j.org/api/](https://www.slf4j.org/api/)