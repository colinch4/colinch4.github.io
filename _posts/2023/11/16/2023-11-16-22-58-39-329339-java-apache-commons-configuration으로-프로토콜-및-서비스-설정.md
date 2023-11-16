---
layout: post
title: "[java] Java Apache Commons Configuration으로 프로토콜 및 서비스 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java에서 구성 파일을 쉽게 읽고 쓸 수 있는 라이브러리입니다. 이를 사용하여 프로토콜과 서비스를 구성하는 방법에 대해 알아보겠습니다.

## Apache Commons Configuration 추가

먼저 Maven 또는 Gradle과 같은 의존성 관리 도구를 사용하여 Apache Commons Configuration을 프로젝트에 추가해야 합니다. Maven을 사용하는 경우 다음과 같이 `pom.xml` 파일에 의존성을 추가할 수 있습니다:

```xml
<dependency>
  <groupId>org.apache.commons</groupId>
  <artifactId>commons-configuration2</artifactId>
  <version>2.7</version>
</dependency>
```

Gradle을 사용하는 경우, `build.gradle` 파일에 다음과 같이 의존성을 추가할 수 있습니다:

```groovy
implementation 'org.apache.commons:commons-configuration2:2.7'
```

## 프로퍼티 파일 생성

프로토콜과 서비스 설정을 위해, 먼저 `.properties` 확장자를 가진 프로퍼티 파일을 생성해야 합니다. 예를 들어, `config.properties`라는 파일을 생성하고 다음과 같이 프로퍼티를 설정할 수 있습니다:

```properties
protocol=https
service.host=example.com
service.port=8080
```

## 구성 파일 로드

Apache Commons Configuration을 사용하여 프로퍼티 파일을 로드하는 방법은 다음과 같습니다:

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.ConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class AppConfig {
    public static void main(String[] args) {
        Configurations configs = new Configurations();
        try {
            Configuration config = configs.properties("config.properties");
            
            // 프로토콜 값 가져오기
            String protocol = config.getString("protocol");
            
            // 서비스 호스트 가져오기
            String serviceHost = config.getString("service.host");
            
            // 서비스 포트 가져오기
            int servicePort = config.getInt("service.port");
            
            System.out.println("프로토콜: " + protocol);
            System.out.println("서비스 호스트: " + serviceHost);
            System.out.println("서비스 포트: " + servicePort);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서, `config.properties` 파일이 현재 디렉토리에 있어야 합니다. 프로퍼티 파일을 읽은 후, `getString()` 및 `getInt()` 메서드를 사용하여 해당 프로퍼티 값을 가져올 수 있습니다.

## 실행

위의 예제 코드를 실행하면 아래와 같은 출력을 얻을 수 있습니다:

```
프로토콜: https
서비스 호스트: example.com
서비스 포트: 8080
```

## 결론

Java Apache Commons Configuration을 사용하면 프로토콜 및 서비스 설정을 쉽게 구성할 수 있습니다. 프로퍼티 파일을 작성하고 관련 값을 가져와서 애플리케이션의 동작을 조정할 수 있습니다. 참고로, Apache Commons Configuration은 XML, JSON 및 YAML과 같은 다른 유형의 구성 파일도 지원합니다.

## 참고 자료

- [Apache Commons Configuration 문서](https://commons.apache.org/proper/commons-configuration/index.html)