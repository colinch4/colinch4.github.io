---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 다국어 지원 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

다국어 지원은 현대의 소프트웨어 개발에서 매우 중요한 요소입니다. 사용자는 다양한 언어로 애플리케이션을 사용하고, 이에 따라 애플리케이션은 해당 언어로 텍스트 및 메시지를 표시해야 합니다. Java 개발자는 Apache Commons Configuration을 사용하여 다국어 지원 설정을 간편하게 구현할 수 있습니다.

Apache Commons Configuration은 Apache 소프트웨어 재단에서 개발한 오픈 소스 라이브러리로, 구성 파일을 읽고 쓰는 기능을 제공합니다. 이 라이브러리를 활용하여 애플리케이션의 설정 정보를 다양한 소스로부터 읽어올 수 있으며, 다국어 지원에도 활용할 수 있습니다.

## Apache Commons Configuration 설치

Apache Commons Configuration을 사용하려면 먼저 해당 라이브러리를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우 `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

Gradle을 사용하는 경우 `build.gradle` 파일에 다음 의존성을 추가합니다:

```groovy
dependencies {
    implementation 'org.apache.commons:commons-configuration2:2.7'
}
```

위의 의존성을 추가한 후, Maven 또는 Gradle을 실행하여 라이브러리를 다운로드 받고 프로젝트에 추가합니다.

## 다국어 지원 설정 파일 작성

다국어 지원을 위해 먼저 `resources` 폴더에 `messages.properties` 파일을 작성합니다. 이 파일은 기본 언어인 영어의 텍스트를 제공합니다. 다른 언어의 텍스트는 따로 파일을 생성하여 해당 언어 코드를 파일 이름 뒤에 붙여주면 됩니다. 예를 들어, 한국어의 경우 `messages_ko.properties` 파일을 작성합니다.

`messages.properties` 파일에는 다음과 같이 텍스트를 설정할 수 있습니다:

```properties
greeting=Hello!
farewell=Goodbye!
```

`messages_ko.properties` 파일에는 다음과 같이 한국어로 번역된 텍스트를 설정할 수 있습니다:

```properties
greeting=안녕하세요!
farewell=안녕히 가세요!
```

## 다국어 지원 설정 예제

다음은 Apache Commons Configuration을 활용하여 다국어 지원을 설정하는 Java 예제 코드입니다:

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Parameters;

public class MultilingualSupport {
    private static final String CONFIG_FILE_PATH = "resources/messages.properties";

    public static void main(String[] args) {
        Configuration config = loadConfiguration(CONFIG_FILE_PATH);
        
        String greeting = config.getString("greeting");
        String farewell = config.getString("farewell");
        
        System.out.println(greeting);
        System.out.println(farewell);
    }

    private static Configuration loadConfiguration(String configFilePath) {
        Parameters params = new Parameters();
        FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
                new FileBasedConfigurationBuilder<PropertiesConfiguration>(PropertiesConfiguration.class)
                        .configure(params.fileBased().setFileName(configFilePath));

        try {
            return builder.getConfiguration();
        } catch (ConfigurationException e) {
            e.printStackTrace();
            return null;
        }
    }
}
```

위의 예제 코드는 `messages.properties` 파일을 로드하고, 각각의 텍스트 값을 가져와 출력하는 간단한 예제입니다. `loadConfiguration` 메소드에서는 Apache Commons Configuration을 활용하여 파일 기반의 구성 파일을 로드합니다.

예제를 실행하면 `messages.properties` 파일의 텍스트 값들이 출력됩니다. 다른 언어로 텍스트를 표시하기 위해서는 해당 언어의 `messages` 파일을 작성하고, `loadConfiguration` 메소드에서 해당 파일을 로드하도록 수정하면 됩니다.

## 결론

Java Apache Commons Configuration을 활용하여 다국어 지원 설정을 구현하는 방법에 대해 알아보았습니다. 이를 통해 애플리케이션에서 다국어 지원을 손쉽게 구현할 수 있습니다. Apache Commons Configuration은 다양한 구성 파일 형식을 지원하므로, 사용자의 선호도에 따라 다른 파일 형식을 사용할 수도 있습니다. 다국어 지원은 사용자 경험을 향상시키는 중요한 요소이므로, 이를 신속하게 구현할 수 있는 Apache Commons Configuration을 활용해 보세요.