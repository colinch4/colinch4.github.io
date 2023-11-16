---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 배치 작업 스케줄링 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java를 위한 유용한 구성 라이브러리입니다. 이 라이브러리를 사용하면 설정 파일을 읽고, 수정하고, 저장하는 등의 구성 작업을 간편하게 처리할 수 있습니다.

이번 예제에서는 Apache Commons Configuration을 사용하여 배치 작업 스케줄링을 설정하는 방법을 알아보겠습니다. 배치 작업 스케줄링은 특정 시간 또는 주기에 따라 자동으로 실행되는 작업 스케줄을 의미합니다.

## Maven 종속성 추가

먼저 Maven 프로젝트의 `pom.xml` 파일에 다음 종속성을 추가해야 합니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

## 설정 파일 작성

배치 작업 스케줄링을 설정하기 위해 먼저 설정 파일을 작성해야 합니다. 아래는 예시로 사용할 설정 파일의 내용입니다.

```properties
# batch.properties

# 작업 실행 주기 (분)
job.interval=5

# 작업 시작 시간
job.start.time=09:00
```

## 스케줄링 설정 코드 작성

Apache Commons Configuration을 사용하여 설정 파일을 읽고, 스케줄링을 설정하는 코드를 작성해 보겠습니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.PropertiesConfiguration;
import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class BatchScheduler {

    public static void main(String[] args) {
        try {
            // 설정 파일 로드
            Configuration config = new PropertiesConfiguration("batch.properties");

            // 스케줄러 생성
            SchedulerFactory schedulerFactory = new StdSchedulerFactory();
            Scheduler scheduler = schedulerFactory.getScheduler();

            // 작업 실행 주기 설정
            int interval = config.getInt("job.interval");
            Trigger trigger = TriggerBuilder.newTrigger()
                    .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                            .withIntervalInMinutes(interval)
                            .repeatForever())
                    .build();

            // 작업 시작 시간 설정
            String startTime = config.getString("job.start.time");
            SimpleDateFormat sdf = new SimpleDateFormat("HH:mm");
            Date startDate = sdf.parse(startTime);
            JobDetail job = JobBuilder.newJob(BatchJob.class)
                    .withIdentity("batchJob", "group1")
                    .build();

            // 작업 실행 스케줄링
            scheduler.scheduleJob(job, trigger);
            scheduler.start();
        } catch (ConfigurationException | SchedulerException | ParseException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서 `Configuration` 객체를 사용하여 설정 파일을 로드하고, 원하는 값을 가져올 수 있습니다. 그리고 Quartz 라이브러리를 사용하여 작업 실행 주기와 작업 시작 시간을 설정한 후, 작업을 스케줄링합니다.

## 배치 작업 코드 작성

위에서 스케줄링한 작업을 실행할 배치 작업 코드를 작성해 보겠습니다.

```java
import org.quartz.Job;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

public class BatchJob implements Job {

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println("Batch job is running.");
        // TODO: 배치 작업 실행 로직 구현
    }
}
```

`BatchJob` 클래스는 `Job` 인터페이스를 구현하여 `execute` 메소드를 오버라이딩합니다. 이 메소드 안에 배치 작업을 실행하는 로직을 구현하면 됩니다.

## 실행 결과 확인

위의 코드를 정상적으로 실행하면, 설정 파일에 지정한 작업 실행 주기와 작업 시작 시간에 맞게 배치 작업이 스케줄링되고 실행됩니다.

이를 확인하기 위해 콘솔에서 다음과 같은 로그가 출력되어야 합니다.

```
Batch job is running.
Batch job is running.
Batch job is running.
...
```

## 마무리

이번 예제에서는 Apache Commons Configuration을 사용하여 Java에서 설정 파일을 읽고, 배치 작업 스케줄링을 설정하는 방법을 알아보았습니다. 이러한 방식으로 스케줄링된 작업을 실행하면 정해진 주기나 시간에 맞게 작업을 자동으로 실행할 수 있습니다.

더 자세한 내용은 [Apache Commons Configuration](https://commons.apache.org/proper/commons-configuration/)과 [Quartz Scheduler](http://www.quartz-scheduler.org/)의 공식 문서를 참고하시기 바랍니다.