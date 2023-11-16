---
layout: post
title: "[java] Java Apache Commons Configuration을 활용한 스케줄링 구현 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이번 포스트에서는 **Java Apache Commons Configuration** 라이브러리를 사용하여 스케줄링을 구현하는 방법에 대해 알아보겠습니다.

## Apache Commons Configuration 소개

**Apache Commons Configuration**은 Java 애플리케이션에서 구성 파일을 읽고 처리하는 데 도움이되는 라이브러리입니다. 이 라이브러리를 사용하면 간단하게 XML, 프로퍼티, YAML 등 다양한 유형의 구성 파일을 읽을 수 있습니다.

## 스케줄링 구현 방법

1. 먼저, Maven 또는 Gradle을 사용하여 Apache Commons Configuration 라이브러리를 프로젝트에 추가해야합니다.

2. 구성 파일을 작성합니다. 예를 들어, 아래와 같이 `schedule.properties` 파일을 작성합니다.

```properties
job.email.enabled=true
job.email.time=07:00
job.email.recipients=user1@example.com,user2@example.com
```

3. Java 코드에서 `Configuration` 객체를 생성하고, 구성 파일을 로드합니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.fluent.Configurations;

public class Scheduler {

    private static final String CONFIG_FILE = "schedule.properties";

    public static void main(String[] args) {
        try {
            Configurations configs = new Configurations();
            Configuration config = configs.properties(CONFIG_FILE);
            
            // 스케줄링 작업 수행
            if (config.getBoolean("job.email.enabled")) {
                String time = config.getString("job.email.time");
                String[] recipients = config.getStringArray("job.email.recipients");
                
                // 작업 로직 추가
                sendEmail(time, recipients);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    private static void sendEmail(String time, String[] recipients) {
        // 이메일을 보내는 작업 로직
    }
}
```

4. 위 코드에서 `Configuration` 객체를 사용하여 구성 파일의 값을 가져올 수 있습니다. 예를 들어, `config.getBoolean("job.email.enabled")`는 `job.email.enabled` 프로퍼티의 값을 가져옵니다.

5. `Scheduler` 클래스의 메인 메서드에서 필요한 스케줄링 작업을 수행합니다. 위 예제에서는 `job.email.enabled` 값이 `true`인 경우에만 이메일을 보내는 작업이 수행됩니다.

## 결론

이번 포스트에서는 **Java Apache Commons Configuration** 라이브러리를 사용하여 스케줄링을 구현하는 방법에 대해 알아보았습니다. 이 라이브러리를 사용하면 손쉽게 구성 파일을 읽고 처리할 수 있으며, 이를 통해 애플리케이션에 유연한 스케줄링 기능을 추가할 수 있습니다.

## 참고 자료
- [Apache Commons Configuration 문서](https://commons.apache.org/proper/commons-configuration/userguide/index.html)