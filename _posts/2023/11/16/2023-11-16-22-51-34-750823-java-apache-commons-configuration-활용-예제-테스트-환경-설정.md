---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 테스트 환경 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 자바 애플리케이션에서 구성 파일을 읽고 쓰기 위한 유용한 라이브러리입니다. 이 블로그 포스트에서는 Apache Commons Configuration을 사용하여 테스트 환경 설정을 구성하는 예제를 소개하려고 합니다.

## 필요한 의존성 추가하기

먼저, Maven 또는 Gradle과 같은 빌드 도구를 사용하여 프로젝트에 Apache Commons Configuration 의존성을 추가해야 합니다. Maven을 사용하는 경우 `pom.xml` 파일에 다음을 추가합니다:

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-configuration2</artifactId>
        <version>2.7</version>
    </dependency>
</dependencies>
```

Gradle을 사용하는 경우 `build.gradle` 파일에 다음을 추가합니다:

```groovy
dependencies {
    implementation 'org.apache.commons:commons-configuration2:2.7'
}
```

의존성을 추가 한 후에는 빌드 도구를 사용하여 의존성을 다운로드하고 프로젝트를 컴파일해야 합니다.

## 테스트 환경 설정 파일 생성하기

테스트 환경 설정을 위해 `config.properties`라는 구성 파일을 생성합니다. 이 파일에는 테스트에 필요한 구성 값들을 저장합니다. 예를 들어, 다음과 같은 설정 값을 사용한다고 가정해봅시다:

```properties
database.host=localhost
database.port=5432
database.username=admin
database.password=secret
```

## 구성 파일 로드하기

이제 Java 코드에서 구성 파일을 로드하여 테스트 환경을 구성해 봅시다. 다음은 Apache Commons Configuration을 사용하여 구성 파일을 로드하는 예제입니다:

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilderParameters;
import org.apache.commons.configuration2.builder.fluent.Parameters;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class TestConfig {

    private static final String CONFIG_FILE_PATH = "config.properties";

    public static void main(String[] args) {
        Parameters params = new Parameters();
        FileBasedConfigurationBuilder<FileBasedConfiguration> builder =
                new FileBasedConfigurationBuilder<FileBasedConfiguration>(PropertiesConfiguration.class)
                        .configure(params.fileBased()
                                .setFile(new File(CONFIG_FILE_PATH)));

        try {
            Configuration configuration = builder.getConfiguration();

            // 구성 값들을 사용하여 테스트 환경을 설정하는 로직을 추가합니다.
            String databaseHost = configuration.getString("database.host");
            int databasePort = configuration.getInt("database.port");
            String databaseUsername = configuration.getString("database.username");
            String databasePassword = configuration.getString("database.password");

            // 테스트 환경 설정 로직 추가...

        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서는 `config.properties` 파일을 로드하고 필요한 구성 값을 가져오는 로직을 보여줍니다. 여기에서는 간단히 구성 값들을 출력하는 대신에 해당 값을 사용하여 테스트 환경을 설정하는 로직을 추가하면 됩니다.

## 결론

이번 포스트에서는 Apache Commons Configuration을 활용하여 테스트 환경을 구성하는 예제를 소개했습니다. Apache Commons Configuration은 다양한 종류의 구성 파일을 지원하고 간단한 API를 제공하기 때문에 자바 애플리케이션에서 구성을 관리해야 할 때 유용합니다.

더 자세한 내용은 [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)를 참조하시기 바랍니다.