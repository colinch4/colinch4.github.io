---
layout: post
title: "[java] Log4j의 NDC(Nested Diagnostic Context) 개요"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Log4j는 자바 어플리케이션에서 로깅을 관리하기 위한 강력한 도구입니다. Log4j는 로그 이벤트를 캡처하고, 저장하고, 필터링하며, 다양한 출력 형식으로 표시하는 기능을 제공합니다. 이러한 기능 중 하나가 NDC(Nested Diagnostic Context)입니다.

## NDC란 무엇인가요?

NDC는 로그 이벤트의 추가적인 컨텍스트 정보를 제공하기 위해 사용됩니다. 로그에는 메시지 뿐만 아니라 이벤트가 발생한 시간, 장소, 사용자 정보 등과 같은 추가적인 정보가 필요한 경우가 많습니다. NDC를 사용하면 이러한 추가 정보를 로그 이벤트에 손쉽게 추가할 수 있습니다.

## NDC 사용하기

NDC를 사용하려면 Log4j를 설정해야 합니다. 먼저, Log4j 라이브러리를 프로젝트에 추가한 후 설정 파일(log4j.properties 또는 log4j.yml)을 작성해야 합니다. 설정 파일에서는 NDC 패턴을 정의하고, 어떤 정보를 NDC에 추가할 것인지를 결정할 수 있습니다.

다음은 예시 설정 파일(log4j.properties)의 일부입니다.

```properties
log4j.rootLogger=DEBUG, CONSOLE

log4j.appender.CONSOLE=org.apache.log4j.ConsoleAppender
log4j.appender.CONSOLE.layout=org.apache.log4j.PatternLayout
log4j.appender.CONSOLE.layout.ConversionPattern=[%d] [%X{NDC}] [%t] %m%n
```

위의 설정 파일에서 `%X{NDC}`는 NDC의 값을 출력하기 위한 패턴입니다.

NDC를 사용하여 로그에 정보를 추가하려면 다음과 같이 코드를 작성하면 됩니다.

```java
import org.apache.log4j.NDC;

public class ExampleClass {
    public void exampleMethod() {
        // NDC에 값을 추가합니다.
        NDC.push("exampleValue");
        
        // 로그 출력
        Logger.getLogger(ExampleClass.class).debug("Example log message");
        
        // NDC에서 값을 제거합니다.
        NDC.pop();
    }
}
```

위의 예시 코드에서 `NDC.push("exampleValue")`를 사용하여 NDC에 값을 추가하고, `NDC.pop()`를 사용하여 NDC에서 값을 제거하고 있습니다. 로그 이벤트가 발생할 때마다 NDC에 추가된 값이 로그에 함께 출력됩니다.

## 결론

NDC는 Log4j를 사용하여 로그 이벤트에 추가 정보를 포함할 수 있는 유용한 기능입니다. 이를 통해 로그 분석 및 디버깅 작업을 더욱 효율적으로 수행할 수 있습니다. NDC를 사용하여 로그에 필요한 컨텍스트 정보를 쉽게 추가하고, 문제 해결에 도움을 받을 수 있습니다.

## 참고 자료

- [Log4j 1.2 - Nested Diagnostic Context](https://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/NDC.html)