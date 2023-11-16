---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 푸시 알림 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이 예제에서는 Java에서 Apache Commons Configuration 라이브러리를 사용하여 푸시 알림 설정을 관리하는 방법을 살펴보겠습니다.

## Apache Commons Configuration란?
Apache Commons Configuration은 Java에서 설정 파일을 읽고 관리하기 위한 유용한 라이브러리입니다. 이 라이브러리를 사용하면 다양한 형식의 설정 파일을 쉽게 읽고 변환할 수 있습니다.

## Maven 종속성 추가
먼저 Maven 프로젝트의 pom.xml 파일에 Apache Commons Configuration의 종속성을 추가해야 합니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-configuration2</artifactId>
        <version>2.7</version>
    </dependency>
</dependencies>
```

## 설정 파일 준비
푸시 알림과 관련된 설정을 저장하고 있는 properties 파일을 준비해야 합니다. 아래는 예시입니다.

```properties
# push-notification.properties

# FCM 서버 키
fcm.server.key=your-fcm-server-key

# 푸시 알림 기본 제목
push.notification.default.title=New Notification
```

## 설정 파일 읽기
Java 코드에서 설정 파일을 읽어오기 위해 아래와 같이 Apache Commons Configuration 라이브러리를 사용할 수 있습니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class PushNotificationConfig {
    private static final String CONFIG_FILE = "push-notification.properties";
    private Configuration config;

    public PushNotificationConfig() {
        try {
            config = new PropertiesConfiguration(CONFIG_FILE);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }

    public String getFCMServerKey() {
        return config.getString("fcm.server.key");
    }

    public String getDefaultNotificationTitle() {
        return config.getString("push.notification.default.title");
    }
}
```

위의 코드에서는 `PropertiesConfiguration` 클래스를 사용하여 `push-notification.properties` 파일을 읽어옵니다. `getFCMServerKey()`와 `getDefaultNotificationTitle()` 메소드를 사용하여 필요한 설정 값을 가져올 수 있습니다.

## 설정 값 사용하기
위에서 구현한 `PushNotificationConfig` 클래스를 사용하여 설정 값을 가져오고 활용할 수 있습니다.

```java
public class Main {
    public static void main(String[] args) {
        PushNotificationConfig config = new PushNotificationConfig();
        System.out.println("FCM 서버 키: " + config.getFCMServerKey());
        System.out.println("기본 푸시 알림 제목: " + config.getDefaultNotificationTitle());
    }
}
```

출력 결과는 다음과 같을 것입니다.

```
FCM 서버 키: your-fcm-server-key
기본 푸시 알림 제목: New Notification
```

## 결론
Apache Commons Configuration을 사용하면 Java에서 설정 파일을 쉽게 읽고 관리할 수 있습니다. 이 예제에서는 사용자의 푸시 알림 설정 값을 properties 파일에서 읽어오는 방법을 알아보았습니다.