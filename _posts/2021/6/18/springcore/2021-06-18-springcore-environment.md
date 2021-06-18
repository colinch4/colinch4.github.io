---
layout: post
title: "[springcore] Environment"
description: " "
date: 2021-06-18
tags: [springcore]
comments: true
share: true
---


# Environment
- applicationContext가 BeanFactory 역할만 하는 것은 아님
- 다른 것 중 하나가 EnvironmentCapable
- Environment는 프로파일과 프로퍼티를 다루는 인터페이스

- ApplicationContext extends EnvironmentCapable
  - getEnvironment()
- 프로파일
  - 빈들의 그룹
  - Environment의 역할은 활성화할 프로파일 확인 및 설정 

- 프로파일 유스케이스
  - 테스트환경에서는 A라는 빈을 사용하고, 배포 환경에서는 B라는 빈을 쓰고싶을 때
  - 이 빈은 모니터링 용도니 테스트할 때는 필요없고 배포할 때만 필요한 경우 

- 프로파일 정의하기
  - 클래스에 정의
    - @Configuration @Pofile("test")
    - @Component @Profile("test")
  - 메소드에 정의
    - @Bean @Profile("test")

- 프로파일 설정하기
  - -Dspring.profiles.active="test"
  - @ActiveProfiles (테스트용)

- 프로파일 표현식
  - ! (not)
  - & (and)
  - | (or)
  
#### Property
- 다양한 방법으로 설정할 수 있는 설정 값
- `Environment`의 역할은 프로퍼티 소스 설정 및 값 가져오기

- Property 우선순위
  - ServletConfig 매개변수
  - ServletContext 매개변수
  - JNDI(java:comp/env/);
  - JVM 시스템 프로퍼티 (-Dkey=value)
  - JVM 시스템 환경변수 (운영체제 환경변수)

- @PropertySource
  - `Environment`를 통해 프로퍼티를 추가하는 방법
  - app.properties
  ```properties
  app.name=hello
  ```
  - DemoAppRunner.java
  ```java
  @Component
  @PropertySource("classpath:/app.properties")
  public class DemoAppRunner implements ApplicationRunner {
    @Autowired
    EnvironmentCapable ctx;

    @Override
    public void run(ApplicationArguments args) {
      Environment environment = ctx.getEnvironment();
      System.out.println(environment.getProperty("app.name"));
    }
  }
  ```

- 기본 프로퍼티 소스 지원(application.properties)
- 프로파일까지 고려한 계층형 프로퍼티 우선 순위 제공
