---
layout: post
title: "[java] Quartz Scheduler와 REST API 통신하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

많은 애플리케이션에서는 주기적으로 작업을 실행하기 위해 Quartz Scheduler를 사용합니다. 하지만 때로는 Quartz 스케줄러가 실행해야하는 작업이 외부 REST API와 통신해야 할 수도 있습니다. 이 블로그 포스트에서는 Quartz Scheduler와 REST API를 통신하는 방법에 대해 알아보겠습니다.

## 1. Maven 종속성 추가하기

먼저 Quartz Scheduler와 REST API 클라이언트를 사용하기 위해 Maven 종속성을 추가해야 합니다. 아래와 같이 `pom.xml` 파일에 다음 종속성을 추가하세요.

```xml
<dependencies>
    <dependency>
        <groupId>org.quartz-scheduler</groupId>
        <artifactId>quartz</artifactId>
        <version>2.3.2</version>
    </dependency>
    <dependency>
        <groupId>org.apache.httpcomponents</groupId>
        <artifactId>httpclient</artifactId>
        <version>4.5.12</version>
    </dependency>
</dependencies>
```

Quartz Scheduler와 Apache HttpClient 종속성을 추가했습니다.

## 2. Quartz Job 작성하기

다음으로 Quartz 스케줄러를 사용하여 REST API를 호출하는 작업을 만들어 보겠습니다. Quartz Job은 `org.quartz.Job` 인터페이스를 구현해야 합니다. 아래는 예제 Quartz Job 클래스입니다.

```java
public class RestApiJob implements Job {

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        // REST API 호출 코드 작성
    }
}
```

`execute` 메서드에서는 REST API를 호출하는 코드를 작성합니다. 실제 호출하는 로직은 여기에 작성되어야 합니다.

## 3. Quartz Job 스케줄링하기

다음으로 작성한 Quartz Job을 스케줄링하여 주기적으로 실행되도록 설정해야 합니다. Quartz 스케줄링을 위해 `org.quartz.Scheduler`를 사용합니다. 아래는 예제 스케줄링 코드입니다.

```java
public class QuartzSchedulerExample {

    public static void main(String[] args) throws SchedulerException {
        // 스케줄러 생성
        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();

        // 스케줄러 시작
        scheduler.start();

        // Quartz Job 생성
        JobDetail jobDetail = JobBuilder.newJob(RestApiJob.class)
                .withIdentity("restApiJob", "group1")
                .build();

        // 스케줄 생성 (매 분마다 실행됨)
        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("restApiTrigger", "group1")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.repeatMinutelyForever())
                .build();

        // 스케줄러에 Job과 Trigger 등록
        scheduler.scheduleJob(jobDetail, trigger);
    }
}
```

위 예제 코드는 매 분마다 `RestApiJob`을 실행합니다. 필요에 따라 `withSchedule` 메서드를 사용하여 스케줄링 시간을 조정할 수 있습니다.

## 4. REST API 호출하기

Quartz Job의 `execute` 메서드에서는 REST API를 호출해야 합니다. Java에서는 Apache HttpClient를 사용하여 간단하게 REST API를 호출할 수 있습니다. 아래는 예제 코드입니다.

```java
HttpClient client = HttpClientBuilder.create().build();
HttpGet request = new HttpGet("http://api.example.com/data");
HttpResponse response = client.execute(request);

// 응답 처리 로직 작성
```

위 예제 코드에서는 `http://api.example.com/data`에 GET 요청을 보내고, 응답을 받아 처리합니다. 필요에 따라 POST, PUT, DELETE 등의 다른 HTTP 메서드를 사용할 수도 있습니다.

## 마무리

위에서 설명한 방법을 따라 직접 Quartz 스케줄러를 사용하여 REST API를 호출하는 애플리케이션을 개발할 수 있습니다. 이러한 방식을 사용하면 특정 시간 간격으로 작업을 실행하면서 외부 REST API와 통신할 수 있습니다.

더 자세한 정보를 원하시면 Quartz Scheduler와 Apache HttpClient의 공식 문서를 참조해 주세요.

- Quartz Scheduler 문서: [https://www.quartz-scheduler.org/documentation/](https://www.quartz-scheduler.org/documentation/)
- Apache HttpClient 문서: [https://hc.apache.org/httpcomponents-client-ga/](https://hc.apache.org/httpcomponents-client-ga/)

**참고 자료:**
- [https://www.baeldung.com/quartz](https://www.baeldung.com/quartz)
- [https://www.baeldung.com/httpclient-guide](https://www.baeldung.com/httpclient-guide)