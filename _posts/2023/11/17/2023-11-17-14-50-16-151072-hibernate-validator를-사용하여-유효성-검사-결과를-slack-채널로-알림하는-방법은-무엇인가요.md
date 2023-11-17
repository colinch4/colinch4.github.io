---
layout: post
title: "[java] Hibernate Validator를 사용하여 유효성 검사 결과를 Slack 채널로 알림하는 방법은 무엇인가요?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

이번 포스트에서는 Hibernate Validator를 사용하여 유효성 검사 결과를 Slack 채널로 알림하는 방법에 대해 소개하겠습니다.

## 1. Hibernate Validator 설정

먼저, Hibernate Validator를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, 프로젝트의 `pom.xml` 파일에 다음 의존성을 추가해주세요:

```xml
<dependency>
    <groupId>org.hibernate.validator</groupId>
    <artifactId>hibernate-validator</artifactId>
    <version>6.2.0.Final</version>
</dependency>
```

Gradle을 사용하는 경우, 프로젝트의 `build.gradle` 파일에 다음 의존성을 추가해주세요:

```groovy
implementation 'org.hibernate.validator:hibernate-validator:6.2.0.Final'
```

## 2. Slack Incoming Webhooks 설정

다음으로, Slack Incoming Webhooks를 설정해야 합니다. Slack 앱 디렉토리에서 "Incoming Webhooks"를 검색하고, Slack 워크스페이스에 Incoming Webhooks 앱을 추가하세요. 웹훅 URL을 생성하고, 이 URL을 통해 Slack 채널로 알림을 전송할 것입니다. 웹훅 URL을 복사해두세요.

## 3. 유효성 검사 결과 알림 기능 추가

유효성 검사 결과를 Slack에 알리기 위해 다음 순서대로 진행하세요:

### 3.1. Slack 알림 전송 클래스 만들기

Slack 알림을 전송할 클래스를 만들어 주세요. 새로운 Java 클래스를 생성하고, 다음과 같이 작성하세요:

```java
import org.springframework.web.client.RestTemplate;

public class SlackNotifier {

    private static final String WEBHOOK_URL = "your-slack-webhook-url";
    private RestTemplate restTemplate;

    public SlackNotifier() {
        restTemplate = new RestTemplate();
    }

    public void notify(String message) {
        restTemplate.postForEntity(WEBHOOK_URL, message, String.class);
    }
}
```

`WEBHOOK_URL` 상수에 앞서 생성한 Slack Incoming Webhooks의 웹훅 URL을 넣어주세요.

### 3.2. Hibernate Validator 이벤트 리스너 생성

이제 Hibernate Validator 이벤트 리스너를 만들어서 유효성 검사 결과를 Slack으로 전송해주는 기능을 추가해보겠습니다. 새로운 Java 클래스를 생성하고, 다음과 같이 작성하세요:

```java
import org.hibernate.validator.event.spi.Validated;

public class SlackValidationEventListener {
  
    private SlackNotifier slackNotifier;

    public SlackValidationEventListener() {
        slackNotifier = new SlackNotifier();
    }

    @EventListener
    public void onValidationEvent(Validated validated) {
        String validationResult = validated.toSring(); // 우리의 프로젝트에 맞게 유효성 검사 결과 문자열을 생성하는 로직을 구현해야 합니다.
        slackNotifier.notify(validationResult);
    }
}
```

`onValidationEvent` 메소드에서는 `validated` 객체를 통해 유효성 검사 결과를 가져와서 Slack으로 전송하도록 합니다. 이 때, `validated` 객체를 문자열로 변환하여 Slack 알림으로 전달하는 로직을 구현해야 합니다.

## 4. 하이버네이트 설정 파일에 이벤트 리스너 등록

마지막으로, 하이버네이트 설정 파일에 앞서 생성한 이벤트 리스너를 등록해야 합니다. `application.yaml` 또는 `application.properties` 파일에서 다음과 같이 설정해주세요:

```yaml
spring:
  jpa:
    properties:
      javax:
        persistence:
          validation:
            factory:
              validation:
                with:
                  hibernate:
                    event:
                      listener:
                        orm:
                          validate: com.example.SlackValidationEventListener
```

위의 설정을 통해 유효성 검사가 수행될 때마다 `SlackValidationEventListener`가 호출되어 Slack으로 알림이 전송됩니다.

## 결론

이렇게 하면 Hibernate Validator를 사용하여 유효성 검사 결과를 Slack 채널로 알림하는 기능을 구현할 수 있습니다. Slack Incoming Webhooks를 이용하여 알림을 전송하고, Hibernate Validator 이벤트 리스너를 사용하여 유효성 검사 결과를 처리합니다. 예제 코드를 참고하여 프로젝트에 맞게 구현해보세요.

참고자료:
- [Hibernate Validator 공식 문서](https://docs.jboss.org/hibernate/stable/validator/reference/en-US/html_single/#validator-hibernatevalidator)