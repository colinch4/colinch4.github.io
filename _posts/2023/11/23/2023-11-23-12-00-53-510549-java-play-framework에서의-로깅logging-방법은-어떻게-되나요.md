---
layout: post
title: "[java] Java Play Framework에서의 로깅(logging) 방법은 어떻게 되나요?"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Java Play Framework는 강력하고 다양한 로깅 옵션을 제공합니다. Play Framework의 로깅은 logback을 사용하여 구현되어 있습니다. 로깅을 사용하여 애플리케이션의 동작 상태를 모니터링하고 디버깅하는 것이 좋습니다. 

로깅을 구성하려면 `application.conf` 파일에서 로깅 관련 설정을 변경해야 합니다. 다음은 Play Framework에서 로깅을 사용하는 방법을 보여주는 예제입니다.

1. `application.conf` 파일을 엽니다.
2. 로깅 설정을 찾아 수정합니다.

다음은 로깅 설정을 변경하는 예제입니다.

```properties
# 로깅 레벨 설정
logger.root=INFO
logger.play=INFO

# 로그 패턴 설정
logback.pattern="%date{yyyy-MM-dd HH:mm:ss} [%-5p] [%-20c{0}:%L] - %m%n"

# 로그 저장 위치 설정
logger.fileHandler.path="./logs"
logger.fileHandler.name="application.log"

# 로그 파일 롤링 설정
logger.fileHandler.rotation=zip
logger.fileHandler.maxSize=10MB
logger.fileHandler.cleaner=delete

# 콘솔에 로그 출력 설정
logger.consoleHandler.level=ERROR
logger.consoleHandler.filters=classic

# 추가적인 로거 설정
logger.application=INFO
```

위의 설정은 다음과 같은 기능을 제공합니다.

- `logger.root` : 전역 로깅 레벨을 설정합니다.
- `logger.play` : Play Framework의 로깅 레벨을 설정합니다.
- `logback.pattern` : 로그 메시지가 출력될 때 사용할 패턴을 설정합니다.
- `logger.fileHandler.path` : 로그 파일이 저장될 위치를 설정합니다.
- `logger.fileHandler.name` : 로그 파일의 이름을 설정합니다.
- `logger.fileHandler.rotation` : 로그 파일 롤링(자동으로 새로운 파일로 교체) 설정을 지정합니다.
- `logger.fileHandler.maxSize` : 로그 파일의 최대 크기를 설정합니다.
- `logger.fileHandler.cleaner` : 로그 파일 롤링 시 이전 파일을 삭제할 것인지 여부를 설정합니다.
- `logger.consoleHandler.level` : 콘솔에 출력될 로그 레벨을 설정합니다.
- `logger.consoleHandler.filters` : 콘솔 로그 필터를 설정합니다.
- `logger.application` : 추가적인 로거의 로깅 레벨을 설정합니다.

위의 설정은 필요에 따라 변경할 수 있습니다. 적절한 로깅 레벨과 저장 위치를 선택하여 애플리케이션의 요구 사항에 맞게 수정하십시오.

Play Framework에서 로깅은 애플리케이션의 동작을 모니터링하고 디버깅하는 데 도움을 주는 중요한 도구입니다. 위의 예제를 기반으로 Play Framework에서 로깅을 설정하고 활용하면 애플리케이션 개발과 유지보수가 더욱 용이해질 것입니다.

더 자세한 설정 방법은 Play Framework 공식 문서를 참조하시기 바랍니다.

- [Play Framework 공식 문서 - Logging](https://www.playframework.com/documentation/2.8.x/SettingsLogger)