---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 로깅 수준 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java에서 로깅을 구현하기 위해 다양한 라이브러리를 사용할 수 있지만, Apache Commons Configuration은 설정 파일을 통해 로깅 수준을 동적으로 설정하는 간단하고 강력한 방법을 제공합니다. 이번 예제에서는 이러한 기능을 활용하는 방법을 살펴보겠습니다.

## Apache Commons Configuration이란?

Apache Commons Configuration은 JVM 어플리케이션에서 설정 파일을 읽고 쓰는 데 사용되는 라이브러리입니다. 이 라이브러리는 다양한 형식의 설정 파일을 지원하며, 설정을 로드하고 변경하는 API를 제공합니다.

## 로깅 수준 설정 예제

우리는 보통 로그 메시지의 수준을 조정하여 어떤 메시지들을 기록할지 결정합니다. 로그 수준은 TRACE, DEBUG, INFO, WARN, ERROR 등으로 구성되어 있으며, 각각은 다양한 상황에서 해당 로그를 기록할지 여부를 결정합니다.

Apache Commons Configuration을 사용하여 로깅 수준을 동적으로 변경하는 예제를 살펴보겠습니다.

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;
import org.apache.log4j.Level;
import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

public class LoggingLevelExample {

    private static final Logger logger = Logger.getLogger(LoggingLevelExample.class);
    private static final String CONFIG_FILE = "log4j.properties";
    private static final String LOG_LEVEL_KEY = "log.level";

    public static void main(String[] args) {
        try {
            PropertiesConfiguration configuration = new PropertiesConfiguration(CONFIG_FILE);
            
            String logLevel = configuration.getString(LOG_LEVEL_KEY);
            Level level = Level.toLevel(logLevel);
            
            LogManager.getRootLogger().setLevel(level);
            
            logger.info("This is an INFO level log message.");
            logger.debug("This is a DEBUG level log message.");
            
        } catch (ConfigurationException e) {
            logger.error("Error loading configuration file", e);
        }
    }
}
```

위 예제에서는 Apache Commons Configuration을 사용하여 로그 수준을 설정 파일(`log4j.properties`)에서 동적으로 가져와서 적용합니다. 설정 파일에는 `log.level` 키를 사용하여 원하는 로그 수준을 지정할 수 있습니다.

위 예제에서는 `main` 메서드에서 설정 파일을 로드한 후, `log.level` 값을 가져옵니다. 해당 값을 `Level.toLevel()` 메서드를 사용하여 `Level` 객체로 변환한 후, `LogManager.getRootLogger().setLevel()` 메서드를 통해 전체 로거의 수준을 설정합니다.

마지막으로, 로그 메시지를 기록하기 위해 `logger` 객체를 사용하며, 각 로그 메시지의 수준에 따라 출력됩니다.

## 참고 자료

- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)
- [Apache Log4j 공식 문서](https://logging.apache.org/log4j/1.2/)
- [Log4j 설정 파일 예제](https://logging.apache.org/log4j/1.2/manual.html#Default Initialization Procedure)