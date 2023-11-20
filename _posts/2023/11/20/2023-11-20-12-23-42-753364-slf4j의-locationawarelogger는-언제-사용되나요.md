---
layout: post
title: "[java] SLF4J의 locationAwareLogger는 언제 사용되나요?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

locationAwareLogger를 사용하면 로그 메시지에 포함되는 정보를 세심하게 제어할 수 있습니다. 예를 들어, 개발 중인 애플리케이션에서 특정 메서드의 호출 시간을 로그로 남기고 싶을 때 유용합니다.

locationAwareLogger를 사용하여 로그 메시지를 생성하려면 다음 단계를 수행해야 합니다.

1. Logger를 가져옵니다.
```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

Logger logger = LoggerFactory.getLogger(YourClass.class);
```

2. 로그 레벨에 따라 로그를 생성합니다.
```java
import org.slf4j.event.Level;

if (logger.isLevelEnabled(Level.INFO)) {
    String message = "This is a log message with location information";
    logger.log(null, YourClass.class.getName(), LocationAwareLogger.INFO_INT, message, null, null);
}
```

위의 코드에서 logger.log() 메서드의 인자로는 다음과 같은 정보가 전달됩니다:
- 첫 번째 인자인 "null"은 marker 정보를 나타냅니다.
- 두 번째 인자인 "YourClass.class.getName()"은 로그 이벤트가 발생한 클래스의 이름을 나타냅니다.
- 세 번째 인자인 "LocationAwareLogger.INFO_INT"는 로그 레벨을 나타냅니다.
- 네 번째 인자인 "message"는 로그 메시지의 내용입니다.
- 다섯 번째 인자인 "null"은 로그 이벤트와 연관된 Throwable 객체를 나타냅니다.
- 여섯 번째 인자인 "null"은 호출 스택 트레이스 정보를 나타냅니다.

locationAwareLogger를 사용하면 로그 메시지에 포함되는 위치 정보를 자유롭게 제어할 수 있으며, 디버깅 및 성능 최적화에 도움이 됩니다. SLF4J 공식 문서를 참고하면 더 자세한 정보를 얻을 수 있습니다.

참고:
- [SLF4J 공식 문서](http://www.slf4j.org/manual.html)