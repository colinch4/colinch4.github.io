---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 로그파일 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 어플리케이션에서 설정 파일을 관리하기 위한 유용한 라이브러리입니다. 이 라이브러리를 사용하면 설정 파일의 값을 쉽게 읽고 변경할 수 있습니다. 이 예제에서는 Apache Commons Configuration을 사용하여 로그 파일의 경로와 크기를 설정하는 방법에 대해 알아보겠습니다.

## Apache Commons Configuration 추가하기

먼저, Maven을 사용하여 프로젝트에 Apache Commons Configuration을 추가해야 합니다. `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-configuration2</artifactId>
        <version>2.7</version>
    </dependency>
</dependencies>
```

의존성을 추가한 후, Maven을 사용하여 라이브러리를 다운로드하고 프로젝트를 빌드합니다.

## 설정 파일 생성하기

로그 파일의 경로와 크기를 설정하기 위해 설정 파일을 생성해야 합니다. 예를 들어, `config.properties`라는 이름의 파일을 생성하고 다음과 같이 작성합니다:

```properties
log.path=/var/log/app.log
log.size=10MB
```

로그 파일의 경로는 `log.path`라는 키로 설정되고, 크기는 `log.size`라는 키로 설정됩니다.

## 설정 파일 읽기

이제 Java 코드에서 Apache Commons Configuration을 사용하여 설정 파일을 읽어와서 값을 가져올 수 있습니다. 다음은 로그 파일의 경로와 크기를 읽는 예제 코드입니다:

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Parameters;

public class LogConfiguration {

    private static final String CONFIG_FILE = "config.properties";

    private static Configuration config;

    public static void loadConfiguration() throws Exception {
        Parameters params = new Parameters();
        FileBasedConfigurationBuilder<FileBasedConfiguration> builder =
            new FileBasedConfigurationBuilder<FileBasedConfiguration>(PropertiesConfiguration.class).configure(params.properties()
                .setFileName(CONFIG_FILE));
        
        config = builder.getConfiguration();
    }

    public static String getLogPath() {
        return config.getString("log.path");
    }

    public static String getLogSize() {
        return config.getString("log.size");
    }

    public static void main(String[] args) {
        try {
            loadConfiguration();
            System.out.println("Log Path: " + getLogPath());
            System.out.println("Log Size: " + getLogSize());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드는 `config.properties` 파일을 로드하고 `log.path`와 `log.size`의 값을 가져오는 간단한 예제입니다. `loadConfiguration()` 메서드에서 설정 파일을 로드하는 부분을 주목해주세요. 이 메서드는 `FileBasedConfigurationBuilder`를 사용하여 설정 파일을 읽으며, `config` 객체에 저장된 설정 값을 얻을 수 있습니다.

위의 예제 코드를 실행하면 설정 파일에 저장된 로그 파일의 경로와 크기가 출력됩니다.

## 결론

이 예제에서는 Java 어플리케이션에서 Apache Commons Configuration을 사용하여 로그 파일의 경로와 크기를 설정하는 방법에 대해 알아보았습니다. 설정 파일을 로드하고 값을 가져오는 간단한 예제를 통해 Apache Commons Configuration의 기능을 활용할 수 있습니다. 이러한 기능은 설정 파일을 관리하는데 큰 도움을 줄 수 있으며, 다양한 유형의 설정 값을 읽고 변경하는데 유용합니다.