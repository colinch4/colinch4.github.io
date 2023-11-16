---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 시스템 로그 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 어플리케이션에서 구성 파일을 쉽게 로드하고 사용할 수 있는 라이브러리입니다. 이번 예제에서는 Apache Commons Configuration을 활용하여 시스템 로그 설정을 구성하는 방법을 살펴보겠습니다.

## 필요한 의존성 추가

먼저, Apache Commons Configuration을 사용하기 위해 Maven 또는 Gradle 프로젝트에 다음 의존성을 추가해야 합니다.

```java
// Maven
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>

// Gradle
implementation 'commons-configuration:commons-configuration:1.10'
```

## 구성 파일 작성

시스템 로그 설정을 위한 구성 파일을 작성해야 합니다. 예를 들어, `system-logs.properties`라는 파일에 다음과 같은 내용을 작성할 수 있습니다.

```properties
log.level=debug
log.file=application.log
```

## Java 코드 작성

위에서 작성한 구성 파일을 로드하고 사용하기 위해 Java 코드를 작성해보겠습니다.

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class SystemLogConfig {

    private static final String CONFIG_FILE = "system-logs.properties";
    private static final String LOG_LEVEL_KEY = "log.level";
    private static final String LOG_FILE_KEY = "log.file";

    private String logLevel;
    private String logFile;

    public SystemLogConfig() {
        loadConfig();
    }

    private void loadConfig() {
        try {
            PropertiesConfiguration config = new PropertiesConfiguration(CONFIG_FILE);
            logLevel = config.getString(LOG_LEVEL_KEY);
            logFile = config.getString(LOG_FILE_KEY);
        } catch (ConfigurationException e) {
            e.printStackTrace();
            // 구성 파일을 로드할 수 없을 경우 기본값으로 설정
            logLevel = "info";
            logFile = "application.log";
        }
    }

    public String getLogLevel() {
        return logLevel;
    }

    public String getLogFile() {
        return logFile;
    }
}
```

## 로그 설정 사용하기

위에서 작성한 `SystemLogConfig` 클래스를 사용하여 로그 설정을 사용할 수 있습니다. 다음은 예시입니다.

```java
public class MyApp {
    private static Logger logger = LoggerFactory.getLogger(MyApp.class);

    public static void main(String[] args) {
        SystemLogConfig logConfig = new SystemLogConfig();
        
        // 로그 레벨 설정
        String logLevel = logConfig.getLogLevel();
        switch (logLevel) {
            case "debug":
                logger.setLevel(Level.DEBUG);
                break;
            case "info":
                logger.setLevel(Level.INFO);
                break;
            case "error":
                logger.setLevel(Level.ERROR);
                break;
            default:
                logger.setLevel(Level.INFO);
                break;
        }
        
        // 로그 파일 설정
        String logFile = logConfig.getLogFile();
        logger.addAppender(new FileAppender(new PatternLayout(), logFile));

        // 로그 출력
        logger.debug("This is a debug message");
        logger.info("This is an info message");
        logger.error("This is an error message");
    }
}
```

위의 예제에서는 `SystemLogConfig` 클래스를 사용하여 구성 파일에서 로그 레벨과 로그 파일을 가져온 후, 해당 내용에 맞게 로깅을 설정합니다. 마지막으로, 각각의 로그 레벨에 따라 예시 메시지를 로그에 출력합니다.

이제 Apache Commons Configuration을 사용하여 시스템 로그 설정을 쉽게 구성할 수 있는 예제를 살펴보았습니다. Apache Commons Configuration의 다양한 기능을 활용하여 프로젝트에 맞는 구성 파일을 사용해보세요.

## 참고 자료

- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)
- [Apache Commons Configuration GitHub 저장소](https://github.com/apache/commons-configuration)