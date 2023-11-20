---
layout: post
title: "[java] Google Guice를 사용한 AOP(Aspect-Oriented Programming)"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

## 소개
AOP(Aspect-Oriented Programming)은 소프트웨어 개발에서 관심사(Concern)를 분리하여 모듈화하는 프로그래밍 패러다임입니다. 관심사는 보안, 로깅, 트랜잭션 관리 등 다양한 것들을 포함할 수 있습니다. 이러한 관심사는 기능 구현과는 분리되어 있으며, 코드의 효율성, 재사용성, 유지 보수성을 개선하는 데 도움이 됩니다.

Google Guice는 자바 기반의 경량 의존성 주입(Dependency Injection) 프레임워크입니다. Guice를 통해 AOP를 적용할 수 있으며, 의존성 주입을 사용하여 관심사를 모듈화할 수 있습니다.

## Guice AOP 사용 방법

### 의존성 추가
Guice AOP를 사용하기 위해서는 다음과 같이 의존성을 추가해야 합니다.

```xml
<dependency>
    <groupId>com.google.inject</groupId>
    <artifactId>guice</artifactId>
    <version>4.2.3</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjrt</artifactId>
    <version>1.8.9</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.6</version>
</dependency>
```

### 모듈 생성
AOP를 적용하기 위해 Guice 모듈을 생성해야 합니다. 다음은 로깅 관심사를 적용하는 예제입니다.

```java
import com.google.inject.AbstractModule;
import org.aspectj.lang.Aspects;

public class LoggingModule extends AbstractModule {

    @Override
    protected void configure() {
        bindInterceptor(Matchers.any(), Matchers.annotatedWith(Loggable.class),
                Aspects.aspectOf(LoggingAspect.class));
    }
}
```

### Aspect 생성
Aspect는 실제로 적용할 관심사를 정의하는 클래스입니다. 다음은 LoggingAspect 클래스의 예제입니다.

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;

@Aspect
public class LoggingAspect {

    @Before("@annotation(Loggable)")
    public void logMethodExecution() {
        System.out.println("Method execution logged.");
    }
}
```

### Application 설정
마지막으로 애플리케이션 설정에서 Guice AOP를 사용하도록 설정해야 합니다.

```java
import com.google.inject.Guice;
import com.google.inject.Injector;

public class MyApp {

    public static void main(String[] args) {
        Injector injector = Guice.createInjector(new LoggingModule());
        MyService myService = injector.getInstance(MyService.class);
        myService.doSomething();
    }
}
```

### 실행 결과
위의 예제를 실행하면 MyService의 doSomething() 메서드가 호출될 때 "Method execution logged."가 출력됩니다.

## 결론
Google Guice를 사용하여 AOP를 적용할 수 있습니다. Guice의 의존성 주입 기능을 활용하여 관심사를 분리하고 모듈화하여 코드의 효율성과 유지 보수성을 향상시킬 수 있습니다. Guice AOP를 사용하는 것은 복잡한 작업이 아니며, 코드의 가독성과 확장성을 개선하는 데 도움이 될 것입니다.

## 참고 자료
- [Google Guice 사용 가이드](https://github.com/google/guice/wiki/Motivation)
- [AspectJ Documentation](https://www.eclipse.org/aspectj/doc/released/progguide/index.html)