---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 알림 서비스 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration 라이브러리는 Java 어플리케이션에서 설정을 관리하는 데 도움을 주는 유용한 라이브러리입니다. 이 예제에서는 알림 서비스에 대한 설정을 어떻게 관리하는지 살펴보겠습니다.

## 1. 의존성 추가

Apache Commons Configuration 을 사용하기 위해서는 이를 프로젝트에 추가해야 합니다. Maven 프로젝트의 경우, `pom.xml` 파일에 다음 의존성을 추가합니다.

```xml
<dependencies>
  ...
  <dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>2.7</version>
  </dependency>
  ...
</dependencies>
```

Gradle 프로젝트의 경우, `build.gradle` 파일에 다음 의존성을 추가합니다.

```gradle
dependencies {
  ...
  implementation 'commons-configuration:commons-configuration:2.7'
  ...
}
```

## 2. 설정 파일 작성

알림 서비스의 설정을 관리하기 위해 외부 설정 파일을 사용할 것입니다. 해당 설정 파일을 작성하고 필요한 설정을 추가합니다. 예를 들어, `notification.properties` 파일을 다음과 같이 만들 수 있습니다.

```properties
# 알림 서비스 설정
notification.enabled=true
notification.mode=production
notification.maxRetries=3
notification.retryInterval=5000
notification.timeout=10000
```

## 3. 설정 파일 로드

Java 코드에서 설정 파일을 로드하기 위해 다음과 같은 코드를 사용합니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class NotificationService {

    private static final String CONFIG_FILE_PATH = "notification.properties";
    private static Configuration config;

    public static void main(String[] args) {
        try {
            config = new PropertiesConfiguration(CONFIG_FILE_PATH);
        } catch (ConfigurationException e) {
            // 설정 파일 로드 실패 시 예외 처리
            e.printStackTrace();
        }

        // 설정 사용 예
        boolean notificationEnabled = config.getBoolean("notification.enabled");
        String notificationMode = config.getString("notification.mode");
        int maxRetries = config.getInt("notification.maxRetries");

        // 설정 값 출력
        System.out.println("Notification Enabled: " + notificationEnabled);
        System.out.println("Notification Mode: " + notificationMode);
        System.out.println("Max Retries: " + maxRetries);
    }
}
```

위 코드에서 `notification.properties` 파일의 경로 (`CONFIG_FILE_PATH`)를 필요에 따라 수정해야 합니다.

## 4. 설정 값 사용

설정 파일을 로드한 후, `Configuration` 객체를 통해 설정 값을 사용할 수 있습니다. 위 예제에서는 알림 서비스에 대한 설정 값을 출력하는 것으로 예시를 들었지만, 실제 알림 서비스의 설정을 사용하는 코드를 추가하여 적절한 액션을 취할 수 있습니다.

## 결론

이 예제에서는 Apache Commons Configuration 라이브러리를 사용하여 알림 서비스 설정을 관리하는 방법을 살펴보았습니다. 이를 통해 복잡한 설정을 외부 파일로 분리하여 개발자가 유연하게 설정을 관리할 수 있습니다. 추가로 해당 라이브러리를 사용하면 다양한 설정 파일 형식 (프로퍼티, XML 등)을 지원하여 다양한 환경에서의 설정 관리에도 용이합니다.

## 참고 자료

- [Apache Commons Configuration Documentation](http://commons.apache.org/proper/commons-configuration/index.html)