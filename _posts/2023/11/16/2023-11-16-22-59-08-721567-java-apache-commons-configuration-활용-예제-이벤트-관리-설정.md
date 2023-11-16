---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 이벤트 관리 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 애플리케이션에서 설정 파일을 쉽게 읽고 관리하기 위한 유용한 라이브러리입니다. 이번 예제에서는 Apache Commons Configuration을 사용하여 이벤트 관리 설정을 다루는 방법을 알아보겠습니다.

## 1. Apache Commons Configuration 라이브러리 추가

먼저, 프로젝트의 의존성에 Apache Commons Configuration 라이브러리를 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 아래 의존성을 추가합니다:

```xml
<dependency>
  <groupId>commons-configuration</groupId>
  <artifactId>commons-configuration</artifactId>
  <version>1.10</version>
</dependency>
```

Gradle을 사용하는 경우, `build.gradle` 파일에 아래 의존성을 추가합니다:

```gradle
dependencies {
  implementation 'commons-configuration:commons-configuration:1.10'
}
```

## 2. 이벤트 관리 설정 파일 작성

이벤트 관리 설정을 위한 설정 파일을 작성합니다. 예를 들어, `event.properties` 파일을 생성하고 아래와 같이 내용을 작성합니다:

```properties
event.notification.enabled=true
event.notification.email=admin@example.com
event.notification.sms=1234567890
```

## 3. 설정 파일 로드 및 값 읽기

Java 코드에서 Apache Commons Configuration을 사용하여 설정 파일을 로드하고 값을 읽을 수 있습니다. 아래 예제를 참고하세요:

```java
import org.apache.commons.configuration.Configuration;
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class EventManagementConfig {

  private static final String CONFIG_FILE = "event.properties";

  private Configuration config;

  public EventManagementConfig() throws ConfigurationException {
    config = new PropertiesConfiguration(CONFIG_FILE);
  }

  public boolean isNotificationEnabled() {
    return config.getBoolean("event.notification.enabled", false);
  }

  public String getEmailAddress() {
    return config.getString("event.notification.email");
  }

  public String getPhoneNumber() {
    return config.getString("event.notification.sms");
  }
}
```

위 코드에서 `EventManagementConfig` 클래스는 이벤트 관리 설정을 읽기 위한 클래스입니다. `PropertiesConfiguration` 클래스를 사용하여 설정 파일을 로드하고, `getString` 및 `getBoolean` 메서드를 사용하여 설정 값을 읽을 수 있습니다.

## 4. 설정 값 사용 예제

이제 설정 값을 사용하여 이벤트 관리 로직을 구현할 수 있습니다. 예를 들어, 아래와 같은 코드를 사용하여 이벤트 알림을 특정 조건에 따라 발송할 수 있습니다:

```java
public class EventManagementService {

  private EventManagementConfig config;

  public EventManagementService() throws ConfigurationException {
    config = new EventManagementConfig();
  }

  public void sendNotification() {
    if (config.isNotificationEnabled()) {
      String email = config.getEmailAddress();
      String sms = config.getPhoneNumber();

      // 이벤트 알림 발송 로직 구현
      // ...
    }
  }
}
```

위 예제에서 `EventManagementService` 클래스에서 `EventManagementConfig`를 인스턴스화하여 설정 값을 사용합니다. `isNotificationEnabled` 메서드를 사용하여 알림이 활성화되어 있는지 확인하고, 필요한 알림 정보를 가져옵니다.

이제 `sendNotification` 메서드에서 이벤트 알림을 발송하는 로직을 구현하면 됩니다.

## 결론

Apache Commons Configuration을 활용하여 Java 애플리케이션에서 설정 파일을 쉽게 관리할 수 있습니다. 이번 예제에서는 이벤트 관리 설정을 다루는 방법을 소개했습니다. Apache Commons Configuration의 다양한 기능을 활용하여 애플리케이션 설정을 더욱 편리하게 관리해보세요.

## 참고 자료

- Apache Commons Configuration 공식 문서: [https://commons.apache.org/proper/commons-configuration/](https://commons.apache.org/proper/commons-configuration/)
- Apache Commons Configuration GitHub 리포지토리: [https://github.com/apache/commons-configuration](https://github.com/apache/commons-configuration)