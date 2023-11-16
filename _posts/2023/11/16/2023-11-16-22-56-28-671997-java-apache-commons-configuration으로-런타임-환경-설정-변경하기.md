---
layout: post
title: "[java] Java Apache Commons Configuration으로 런타임 환경 설정 변경하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

애플리케이션을 개발하다보면 런타임 환경 설정을 동적으로 변경해야 하는 경우가 생길 수 있습니다. 이러한 상황에서는 Apache Commons Configuration 라이브러리를 사용하여 런타임 환경 설정을 손쉽게 변경할 수 있습니다. 이번 포스트에서는 Java Apache Commons Configuration을 사용하여 런타임 환경 설정을 변경하는 방법에 대해 알아보겠습니다.

## Apache Commons Configuration이란?

Apache Commons Configuration은 Apache 소프트웨어 재단에서 개발한 오픈 소스 라이브러리로, 다양한 형식의 설정 파일을 읽고 쓰는 기능을 제공합니다. XML, Properties, JSON 등 다양한 형식의 설정 파일을 지원하며, 동적으로 설정을 추가하거나 변경할 수 있는 기능도 제공합니다.

## Maven 설정

먼저 Apache Commons Configuration을 사용하기 위해 Maven 프로젝트에 다음과 같이 종속성을 추가해야 합니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-configuration2</artifactId>
        <version>2.7</version>
    </dependency>
</dependencies>
```

## 런타임 환경 설정 파일 작성

Apache Commons Configuration을 사용하기 위해 먼저 런타임 환경 설정 파일을 작성해야 합니다. 아래는 예시로 `config.properties` 파일을 작성한 것입니다.

```properties
database.url=jdbc:mysql://localhost:3306/mydb
database.username=admin
database.password=secret
```

## 런타임 환경 설정 변경하기

이제 Java 코드에서 Apache Commons Configuration을 사용하여 런타임 환경 설정을 변경할 수 있습니다. 아래는 `config.properties` 파일에서 `database.username` 값을 변경하는 예제 코드입니다.

```java
import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Parameters;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class ConfigurationExample {
    public static void main(String[] args) {
        try {
            Parameters params = new Parameters();
            FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
                    new FileBasedConfigurationBuilder<PropertiesConfiguration>(PropertiesConfiguration.class)
                            .configure(params.properties().setFileName("config.properties"));
            PropertiesConfiguration config = builder.getConfiguration();
            
            config.setProperty("database.username", "new_username");
            builder.save();
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서는 `PropertiesConfiguration` 객체를 생성하고, `setProperty()` 메소드를 사용하여 `database.username` 값을 변경한 후, `builder.save()` 메소드를 호출하여 변경된 설정을 저장합니다.

위의 예시 코드를 실행하면 `config.properties` 파일의 `database.username` 값이 `new_username`으로 변경됩니다.

## 마무리

이번 포스트에서는 Java Apache Commons Configuration을 사용하여 런타임 환경 설정을 변경하는 방법에 대해 알아보았습니다. Apache Commons Configuration을 사용하면 설정 파일의 값을 동적으로 변경할 수 있으므로, 애플리케이션의 환경에 따라 유연하게 설정을 조정할 수 있습니다.

참고 문서: [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)