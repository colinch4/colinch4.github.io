---
layout: post
title: "[java] Log4j의 Daily Rolling File Appender"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Log4j는 자바 기반의 로깅 도구로, 로깅 정보를 파일이나 콘솔 등에 기록하는 용도로 사용됩니다. Log4j의 Daily Rolling File Appender는 일일 단위로 로그 파일을 생성하고 기록하는 기능을 제공합니다.

## Daily Rolling File Appender 설정

Log4j의 Daily Rolling File Appender를 사용하기 위해서는 먼저 log4j.properties 파일에 다음과 같이 설정해야 합니다.

```java
log4j.appender.file=org.apache.log4j.DailyRollingFileAppender
log4j.appender.file.DatePattern='.'yyyy-MM-dd
log4j.appender.file.File=/path/to/logfile.log
log4j.appender.file.layout=org.apache.log4j.PatternLayout
log4j.appender.file.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m%n
```

- **log4j.appender.file**: Daily Rolling File Appender 사용을 설정합니다.
- **log4j.appender.file.DatePattern**: 로그 파일 이름에 날짜 패턴을 설정합니다. '.' 뒤에 패턴을 지정할 수 있으며, 여기서는 `yyyy-MM-dd`로 설정했습니다.
- **log4j.appender.file.File**: 로그 파일의 경로와 이름을 설정합니다.
- **log4j.appender.file.layout**: 로그 레이아웃을 설정합니다. 여기서는 PatternLayout을 사용했습니다.
- **log4j.appender.file.layout.ConversionPattern**: 로그의 출력 형식을 지정합니다. `ConversionPattern`을 사용하여 원하는 형식을 설정할 수 있습니다. 여기서는 날짜, 로그 레벨, 클래스 이름, 라인 번호, 로그 메시지를 포함한 형식을 사용했습니다.

## Daily Rolling File Appender 동작

위의 설정을 통해 Daily Rolling File Appender는 매일 새로운 로그 파일을 생성하고 로그를 기록합니다. 예를 들어, 2021년 1월 1일에는 `logfile.log.2021-01-01` 파일에 로그가 기록되고, 2021년 1월 2일에는 `logfile.log.2021-01-02` 파일에 로그가 기록됩니다.

이렇게 Daily Rolling File Appender를 사용하면 로그 파일이 너무 커지는 것을 방지할 수 있으며, 각 날짜별로 로그를 관리하고 분석하기에 편리합니다.

## 참고 자료

- [Log4j - Apache Logging Services Project](https://logging.apache.org/log4j/)
- [Apache Log4j - DailyRollingFileAppender](https://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/DailyRollingFileAppender.html)