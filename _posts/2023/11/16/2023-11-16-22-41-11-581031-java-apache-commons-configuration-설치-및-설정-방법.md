---
layout: post
title: "[java] Java Apache Commons Configuration 설치 및 설정 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 프로젝트에서 설정 파일을 읽고 관리하기 위한 유용한 라이브러리입니다. 이 블로그 포스트에서는 Apache Commons Configuration을 설치하고 사용하기 위한 방법에 대해 알아보겠습니다.

## 1. Maven을 통한 의존성 추가

Apache Commons Configuration을 사용하기 위해 먼저 Maven을 이용하여 프로젝트에 의존성을 추가해야 합니다. 

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

위의 코드는 Maven pom.xml 파일에 Commons Configuration의 의존성을 추가하는 예시입니다. 해당 의존성을 추가하면 Maven을 통해 Commons Configuration을 자동으로 다운로드하여 사용할 수 있습니다.

## 2. 설정 파일 생성

Apache Commons Configuration은 XML, Properties, YAML, JSON 등 다양한 형식의 설정 파일을 지원합니다. 이 예제에서는 `config.properties`라는 Properties 파일을 사용할 것입니다.

```properties
database.url = jdbc:mysql://localhost:3306/mydb
database.username = admin
database.password = password123
```

위의 예시는 `database.url`, `database.username`, `database.password` 속성을 가진 `config.properties` 파일입니다.

## 3. 설정 파일 로드 및 사용

이제 Java 프로젝트에서 위에서 생성한 설정 파일을 로드하고 사용하는 방법을 알아보겠습니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilderProperties;

public class AppConfig {
    private static final String CONFIG_FILE = "config.properties";

    public static void main(String[] args) {
        try {
            FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
                new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                    .configure(FileBasedConfigurationBuilderProperties.fileBased().setFileName(CONFIG_FILE));
            Configuration config = builder.getConfiguration();

            // 설정 값 사용 예시
            String dbUrl = config.getString("database.url");
            String dbUsername = config.getString("database.username");
            String dbPassword = config.getString("database.password");

            System.out.println("DB URL: " + dbUrl);
            System.out.println("DB Username: " + dbUsername);
            System.out.println("DB Password: " + dbPassword);
        } catch (ConfigurationException e) {
            // 설정 파일 로드 실패 시 예외 처리
            e.printStackTrace();
        }
    }
}
```

위의 Java 코드는 `config.properties` 파일을 로드하여 `Configuration` 객체를 통해 설정 값을 가져온 후 출력하는 예시입니다.

## 결론

이렇게 Apache Commons Configuration을 설치하고 설정 파일을 로드하여 Java 프로젝트에서 설정 값들을 쉽게 사용할 수 있습니다. Commons Configuration은 유연한 설정 파일 관리를 위한 다양한 기능과 옵션을 제공하므로, 프로젝트의 설정 파일 관리를 편리하게 할 수 있습니다.

참고 자료:
- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)
- [Maven 공식 웹사이트](https://maven.apache.org/)