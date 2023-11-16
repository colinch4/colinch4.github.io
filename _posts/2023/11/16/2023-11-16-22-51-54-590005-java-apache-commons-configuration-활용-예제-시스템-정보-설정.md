---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 시스템 정보 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

## 소개
Apache Commons Configuration은 Java에서 시스템 구성 정보를 처리하기 위한 유용한 라이브러리입니다. 이 라이브러리는 다양한 형식의 구성 파일을 지원하며, 간편한 방법으로 구성 정보를 읽고 쓸 수 있습니다. 이 예제에서는 Apache Commons Configuration을 사용하여 시스템 정보를 설정하는 방법에 대해 살펴보겠습니다.

## 환경 설정
Apache Commons Configuration을 사용하기 위해 먼저 Maven 또는 Gradle과 같은 빌드 도구를 사용하여 프로젝트에 의존성을 추가해야 합니다. 다음은 Maven을 사용하는 경우 `pom.xml` 파일에 추가해야 할 내용입니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

## 예제 코드
다음은 Apache Commons Configuration을 사용하여 시스템 정보를 설정하는 예제 코드입니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilderProperties;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class SystemInfoConfiguration {

    public static void main(String[] args) {
        try {
            // 구성 파일 빌더 생성
            FileBasedConfigurationBuilder<PropertiesConfiguration> builder = new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                    .configure(FileBasedConfigurationBuilderProperties.fileBased()
                            .setFile(new File("system.properties")));

            // 구성 파일 로드
            Configuration configuration = builder.getConfiguration();

            // 시스템 정보 설정
            configuration.setProperty("system.name", "My System");
            configuration.setProperty("system.version", "1.0");

            // 설정된 시스템 정보 저장
            builder.save();
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 예제 코드는 `system.properties`라는 구성 파일을 생성하고, 그 안에 `system.name`과 `system.version`의 키-값 쌍을 설정합니다. 구성 파일 작성이 완료되면 `builder.save()`를 호출하여 변경 사항을 저장합니다.

## 실행 결과
위의 예제 코드를 실행하면 `system.properties` 파일이 생성되고 다음과 같은 내용이 포함됩니다.

```
system.name=My System
system.version=1.0
```

## 결론
Apache Commons Configuration을 사용하면 Java 애플리케이션에서 간단하게 구성 정보를 설정할 수 있습니다. 이 예제를 통해 시스템 정보 설정에 대한 기본적인 사용법을 알아보았습니다. Apache Commons Configuration에 대해 더 자세히 알고 싶다면 [공식 문서](https://commons.apache.org/proper/commons-configuration/)를 참조하세요.