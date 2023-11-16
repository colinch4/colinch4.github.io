---
layout: post
title: "[java] Quartz Scheduler와 Spring Framework의 통합"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Quartz Scheduler는 자바 기반의 오픈 소스 작업 스케줄러이며, Spring Framework는 자바 기반의 애플리케이션 개발을 위한 프레임워크입니다. 이 두 기술을 함께 사용하면 스케줄링 작업을 효율적으로 관리하고 실행할 수 있습니다.

## 1. 의존성 추가

먼저, Spring에서 Quartz Scheduler를 사용하기 위해 의존성을 추가해야 합니다. `pom.xml` 파일에 아래의 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-quartz</artifactId>
</dependency>
```

## 2. Scheduler 생성

Quartz Scheduler를 사용하기 위해서는 스케줄러를 생성해야 합니다. Spring Framework에서는 `SchedulerFactoryBean` 클래스를 사용하여 스케줄러를 생성할 수 있습니다. 아래는 스케줄러를 생성하는 예시입니다.

```java
@Configuration
public class SchedulerConfig {

    @Autowired
    private JobFactory jobFactory;

    @Bean
    public SchedulerFactoryBean schedulerFactoryBean() throws IOException {
        SchedulerFactoryBean factory = new SchedulerFactoryBean();
        factory.setJobFactory(jobFactory);
        factory.setQuartzProperties(quartzProperties());
        factory.setSchedulerName("MyScheduler");
        factory.setApplicationContextSchedulerContextKey("applicationContext");
        factory.setAutoStartup(true);
        return factory;
    }

    @Bean
    public Properties quartzProperties() throws IOException {
        PropertiesFactoryBean propertiesFactoryBean = new PropertiesFactoryBean();
        propertiesFactoryBean.setLocation(new ClassPathResource("quartz.properties"));
        propertiesFactoryBean.afterPropertiesSet();
        return propertiesFactoryBean.getObject();
    }
}
```

## 3. Job과 Trigger 정의

스케줄링 작업은 Job과 Trigger로 구성됩니다. Job은 실제로 실행되어야 할 작업이고, Trigger는 작업의 실행 조건을 정의합니다. 아래는 Job과 Trigger를 정의하는 예시입니다.

```java
@Component
public class MyJob implements Job {

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        // 스케줄링 작업 실행 로직 작성
    }
}

@Configuration
public class SchedulerConfig {

    @Autowired
    private MyJob myJob;

    @Bean
    public JobDetailFactoryBean jobDetail() {
        JobDetailFactoryBean jobDetailFactoryBean = new JobDetailFactoryBean();
        jobDetailFactoryBean.setJobClass(MyJob.class);
        jobDetailFactoryBean.setDurability(true);
        return jobDetailFactoryBean;
    }

    @Bean
    public SimpleTriggerFactoryBean trigger(JobDetail jobDetail) {
        SimpleTriggerFactoryBean triggerFactory = new SimpleTriggerFactoryBean();
        triggerFactory.setJobDetail(jobDetail);
        triggerFactory.setStartDelay(1000L);
        triggerFactory.setRepeatInterval(5000L);
        return triggerFactory;
    }
}
```

## 4. 스케줄러 실행

스케줄러를 실행하기 위해 Spring 애플리케이션을 시작할 때 스케줄러를 자동으로 시작하도록 설정해야 합니다. 이를 위해 `@EnableScheduling` 어노테이션을 사용하여 스케줄링 기능을 활성화시킬 수 있습니다. 아래는 스케줄링을 활성화하는 예시입니다.

```java
@SpringBootApplication
@EnableScheduling
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

## 5. 스케줄링 작업 실행 확인

위의 설정을 마친 뒤에는 정의한 스케줄링 작업이 설정된 주기에 맞게 실행되는지 확인할 수 있습니다. 이를 위해 로그를 출력하거나 작업이 수행되는 부분에 디버깅을 추가할 수 있습니다.

## 결론

이번 글에서는 Quartz Scheduler와 Spring Framework의 통합 방법에 대해 알아보았습니다. 이를 통해 스케줄링 작업을 효율적으로 관리하고 실행하는 방법을 배웠습니다. Quartz Scheduler와 Spring Framework를 함께 사용하여 시간에 따라 반복되는 작업을 스케줄링할 수 있습니다.

## 참고 자료

- [Quartz Scheduler Documentation](http://www.quartz-scheduler.org/documentation/quartz-2.x/)
- [Spring Framework Documentation](https://docs.spring.io/spring/docs/current/spring-framework-reference/index.html)