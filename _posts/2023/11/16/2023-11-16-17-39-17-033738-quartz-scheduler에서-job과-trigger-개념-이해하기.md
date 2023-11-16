---
layout: post
title: "[java] Quartz Scheduler에서 job과 trigger 개념 이해하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Quartz Scheduler는 Java 기반으로 개발된 오픈 소스 작업 스케줄링 라이브러리입니다. 이 라이브러리를 사용하여 작업을 예약하고 실행할 수 있습니다. Quartz Scheduler에서는 두 가지 핵심 개념인 job과 trigger가 사용됩니다. 이번 글에서는 job과 trigger의 개념을 자세히 알아보겠습니다.

## 1. Job
Job은 Quartz Scheduler에서 실행되어야 하는 작업을 나타냅니다. Job은 일련의 코드 또는 실행 가능한 명령어로 구성됩니다. Quartz Scheduler가 작업을 실행할 때는 Job 클래스의 execute 메서드가 호출됩니다. 개발자는 Job 인터페이스를 구현하여 자신만의 Job 클래스를 작성할 수 있습니다.

```java
public class MyJob implements Job {
    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        // 작업을 수행할 코드 작성
    }
}
```

Job 클래스에는 execute 메서드 외에도 다양한 메서드와 속성이 존재할 수 있으며, 이를 통해 작업 실행 시 필요한 다양한 설정을 할 수 있습니다.

## 2. Trigger
Trigger는 Quartz Scheduler에게 작업이 언제 실행되어야 하는지를 알려주는 역할을 합니다. Trigger는 작업이 실행되는 주기나 일정 시간 동안 얼마나 자주 실행되어야 하는지를 지정할 수 있습니다. Quartz Scheduler는 설정된 주기나 시간에 따라 Trigger에 의해 작업을 실행합니다.

Trigger에는 여러 종류가 있으며, 가장 일반적인 종류는 `SimpleTrigger`와 `CronTrigger`입니다. `SimpleTrigger`는 주기적으로 작업을 실행하기 위해 사용되며, 정해진 시간 간격에 따라 반복됩니다. `CronTrigger`는 Cron 표현식을 사용하여 작업 실행 시간을 지정하는데, 특정 일 또는 요일에 작업을 실행하거나 특정 시간에 매일 작업을 실행할 수 있습니다.

```java
Trigger trigger = TriggerBuilder.newTrigger()
    .withIdentity("myTrigger", "triggerGroup")
    .withSchedule(SimpleScheduleBuilder.repeatHourlyForever(2))
    .build();
```

이렇게 작성된 Trigger는 매 2시간마다 작업을 실행하도록 설정됩니다. 다양한 Trigger 설정 옵션을 사용하여 실행 주기와 작업의 수행 시간을 세밀하게 조정할 수 있습니다.

## 결론
Quartz Scheduler에서는 job과 trigger를 사용하여 작업을 예약하고 실행할 수 있습니다. Job은 실행되어야 하는 작업을 나타내는 클래스로, 개발자가 직접 구현해야 합니다. Trigger는 작업이 언제 실행되어야 하는지를 지정하는데, 다양한 설정 옵션을 사용하여 실행 주기와 시간을 조정할 수 있습니다.

자세한 내용과 예제 코드는 [Quartz Scheduler 공식 문서](https://www.quartz-scheduler.org/documentation/)를 참고하시기 바랍니다.