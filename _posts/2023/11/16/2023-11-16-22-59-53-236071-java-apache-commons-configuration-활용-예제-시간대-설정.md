---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 시간대 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이번 예제에서는 Java에서 Apache Commons Configuration 라이브러리를 사용하여 시간대 설정을 처리하는 방법을 살펴보겠습니다. Apache Commons Configuration은 XML, Properties, YAML 등 다양한 형식의 설정 파일을 다루기 위한 유용한 도구입니다.

## Apache Commons Configuration 라이브러리 추가

먼저, 프로젝트에 Apache Commons Configuration 라이브러리를 추가해야 합니다. 이를 위해 Maven을 사용한다면 `pom.xml`에 다음 종속성을 추가합니다.

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

Gradle을 사용한다면 `build.gradle`에 다음 의존성을 추가합니다.

```groovy
implementation 'commons-configuration:commons-configuration:1.10'
```

## 설정 파일 준비

다음으로, 시간대를 설정하기 위한 설정 파일을 준비해야 합니다. 예를 들어, `config.properties`라는 파일을 만들고 다음과 같이 시간대 값을 설정합니다.

```properties
timezone=Asia/Seoul
```

## 설정 파일 로드

이제 Java 코드에서 설정 파일을 로드하고 시간대 값을 가져오는 방법을 살펴보겠습니다. 다음은 예제 코드입니다.

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class TimezoneExample {

    public static void main(String[] args) {
        try {
            PropertiesConfiguration config = new PropertiesConfiguration("config.properties");
            String timezone = config.getString("timezone");
            System.out.println("시간대: " + timezone);
            // 여기에서 시간대를 적용하는 추가적인 작업을 수행할 수 있습니다.
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드는 Apache Commons Configuration을 사용하여 `config.properties` 파일을 로드하고, `"timezone"` 키에 해당하는 값을 가져오는 예제입니다. 이 값을 사용하여 시간대 설정을 적용하거나 추가 작업을 수행할 수 있습니다.

## 실행 결과 확인

위의 코드를 실행하면 `config.properties` 파일에서 "timezone" 키에 설정된 값을 가져와서 출력합니다. 예제 파일에는 "Asia/Seoul"이 설정되어 있으므로, 다음과 같은 출력을 얻을 수 있습니다.

```
시간대: Asia/Seoul
```

이제 Java 애플리케이션에서 Apache Commons Configuration을 사용하여 시간대 설정을 처리하는 방법을 알았습니다. 이를 응용하여 다양한 설정 값을 처리할 수 있습니다. 자세한 내용은 [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)를 참조하시기 바랍니다.