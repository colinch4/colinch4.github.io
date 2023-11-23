---
layout: post
title: "[java] Log4j의 Rolling File Appender"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Log4j은 자바 기반의 로깅 프레임워크로, 개발자들이 애플리케이션의 로그를 관리하고 추적할 수 있도록 도와줍니다. Log4j의 Rolling File Appender는 로그 파일을 관리하기 위한 유용한 기능을 제공합니다.

## 1. 로깅 레벨 설정하기
먼저, 로깅 레벨을 설정해야 합니다. Log4j은 TRACE, DEBUG, INFO, WARN, ERROR 등 다양한 로깅 레벨을 제공합니다. 이 중에서 필요한 로깅 레벨을 지정하여 설정 파일에 추가할 수 있습니다.

```java
log4j.rootLogger=INFO, FILE
```

위의 코드에서 `INFO`는 로깅 레벨을 의미하며, `FILE`은 로그를 기록할 appender 이름입니다.

## 2. Rolling File Appender 설정하기
Rolling File Appender를 사용하여 로그 파일을 일정 크기나 기간에 따라 자동으로 롤링할 수 있습니다. 다음과 같이 설정 파일에 추가할 수 있습니다.

```java
log4j.appender.FILE=org.apache.log4j.RollingFileAppender
log4j.appender.FILE.File=/logs/application.log
log4j.appender.FILE.MaxFileSize=10MB
log4j.appender.FILE.MaxBackupIndex=5
log4j.appender.FILE.layout=org.apache.log4j.PatternLayout
log4j.appender.FILE.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} %5p %c{1}:%L - %m%n
```

위의 설정에서 `FILE`은 appender 이름으로 설정되어 있으며, `File` 속성을 사용하여 로그 파일의 경로를 지정할 수 있습니다. `MaxFileSize` 속성은 로그 파일의 최대 크기를 설정하고, `MaxBackupIndex` 속성은 생성된 로그 파일의 최대 백업 수를 설정합니다.

## 3. 로그 기록하기
위의 설정이 완료되면, 애플리케이션 코드에서 Log4j를 사용하여 로그를 기록할 수 있습니다. 다음은 예시 코드입니다.

```java
import org.apache.log4j.Logger;

public class MyApp {
    private static final Logger logger = Logger.getLogger(MyApp.class);
    
    public static void main(String[] args) {
        // 로그 기록
        logger.debug("Debug log message");
        logger.info("Info log message");
        logger.warn("Warn log message");
        logger.error("Error log message");
    }
}
```

위의 예시 코드에서는 Log4j의 `Logger` 클래스를 사용하여 로그를 기록하고 있습니다. 각 로깅 레벨에 따라 적절한 메소드를 사용하여 로그 메시지를 기록할 수 있습니다.

## 4. 참고 자료
- [Log4j 공식 문서](https://logging.apache.org/log4j/1.2/)
- [Log4j로 로그 관리하기(블로그 포스트)](https://www.google.com) (예시 참고)