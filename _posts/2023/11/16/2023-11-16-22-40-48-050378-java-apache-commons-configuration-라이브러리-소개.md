---
layout: post
title: "[java] Java Apache Commons Configuration 라이브러리 소개"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java 개발에서 설정 파일을 읽고 파싱하는 작업은 일반적이고 반복적으로 수행되는 작업입니다. Apache Commons Configuration은 이러한 작업을 간편하게 처리할 수 있는 유용한 라이브러리입니다. 이 라이브러리는 다양한 종류의 설정 파일을 지원하며, 설정 값을 읽고 쓰기 위한 다양한 API를 제공합니다.

## Apache Commons Configuration 설치

Apache Commons Configuration을 사용하기 위해 먼저 해당 라이브러리를 프로젝트에 추가해야 합니다. Maven 프로젝트를 사용하는 경우, `pom.xml` 파일에 다음 의존성을 추가할 수 있습니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

Gradle 프로젝트를 사용하는 경우, `build.gradle` 파일에 다음 의존성을 추가할 수 있습니다.

```groovy
implementation 'org.apache.commons:commons-configuration2:2.7'
```

위의 예시는 `2.7` 버전의 Apache Commons Configuration을 사용하겠다는 의미입니다. 필요에 따라 최신 버전을 사용하실 수 있습니다.

## Apache Commons Configuration 사용법

Apache Commons Configuration을 사용하는 방법은 간단합니다. 먼저, 설정 파일을 로드하고 `Configuration` 객체를 생성해야 합니다. Apache Commons Configuration은 다양한 설정 파일 형식을 지원하며, 예를 들어 `properties`, `xml`, `yaml`, `ini` 등을 사용할 수 있습니다.

아래는 `properties` 파일을 사용하는 예시입니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class ConfigurationExample {
    public static void main(String[] args) {
        Configurations configs = new Configurations();
        try {
            Configuration config = configs.properties("config.properties");
            String value = config.getString("key");
            System.out.println("Value: " + value);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 예시에서 `config.properties` 파일에서 `key`라는 설정 값을 읽어와 출력합니다.

## 추가 기능

Apache Commons Configuration은 설정 파일을 읽을 뿐만 아니라 설정 값을 변경하고 저장할 수 있는 다양한 기능을 제공합니다. 예를 들어, `setProperty(String key, Object value)`를 사용하여 설정 값을 변경하고, `save()`를 사용하여 변경사항을 설정 파일에 저장할 수 있습니다.

자세한 내용은 [공식 문서](https://commons.apache.org/proper/commons-configuration/)에서 확인할 수 있습니다.

## 마무리

Apache Commons Configuration은 Java 개발에서 설정 파일을 관리하는 작업을 간편하게 처리하기 위한 유용한 라이브러리입니다. 다양한 설정 파일 형식을 지원하며, 설정 값의 읽기와 쓰기를 간편하게 처리할 수 있습니다. 개발자들은 Apache Commons Configuration을 활용하여 설정 파일 관리 작업을 보다 효율적으로 처리할 수 있습니다.