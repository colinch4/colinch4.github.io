---
layout: post
title: "[java] Guice의 Aspect-Oriented Programming(AOP)"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

Guice는 Java를 위한 경량 DI(Dependency Injection) 프레임워크입니다. Guice는 AOP(Aspect-Oriented Programming)를 지원하여, 애플리케이션에서 간단하게 관점 지향 프로그래밍을 구현할 수 있습니다.

## AOP란?

AOP는 소프트웨어 개발에서 관점 지향 프로그래밍을 의미합니다. 어플리케이션의 핵심 비즈니스 로직 외에도, 로깅, 트랜잭션 관리, 보안 등과 같은 공통된 기능을 모듈화하는 프로그래밍 기법입니다. 이렇게 모듈화된 관심사를 관점(Aspect)이라고 합니다.

## Guice와 AOP

Guice는 AOP 기능을 제공하기 위해 `com.google.inject.matcher.Matcher`와 `com.google.inject.Module` 인터페이스를 제공합니다. `Matcher`는 특정 클래스나 메서드에 대한 매칭을 수행하고, `Module`은 Guice의 바인딩 구성을 담당합니다.

아래는 Guice에서 AOP를 구현하는 예제입니다.

```java
public class LoggingAspect implements MethodInterceptor {

    @Override
    public Object invoke(MethodInvocation methodInvocation) throws Throwable {
        // 해당 메서드 실행 이전에 수행할 로직
        System.out.println("Before invoking method: " + methodInvocation.getMethod().getName());

        try {
            // 원본 메서드 호출
            Object result = methodInvocation.proceed();

            // 해당 메서드 실행 이후에 수행할 로직
            System.out.println("After invoking method: " + methodInvocation.getMethod().getName());

            return result;
        } catch (Exception e) {
            // 예외 처리 로직
            System.out.println("Exception occurred: " + e.getMessage());
            throw e;
        }
    }
}

public class MyAppModule extends AbstractModule {

    @Override
    protected void configure() {
        // LoggingAspect를 사용하여 Service 클래스에 AOP 적용
        LoggingAspect loggingAspect = new LoggingAspect();
        bindInterceptor(Matchers.subclassesOf(Service.class), Matchers.any(), loggingAspect);
    }
}

public class MyApp {

    public static void main(String[] args) {
        Injector injector = Guice.createInjector(new MyAppModule());
        Service service = injector.getInstance(Service.class);

        service.doSomething();
    }
}
```

위의 예제에서 `LoggingAspect`는 `MethodInterceptor` 인터페이스를 구현합니다. `invoke` 메서드는 원본 메서드의 실행 이전, 이후, 예외 발생 등의 시점에서 로직을 적용할 수 있습니다.

`MyAppModule`에서는 `LoggingAspect`를 사용하여 `Service` 클래스에 AOP를 적용합니다. `Matchers.subclassesOf(Service.class)`를 사용하여 `Service` 클래스와 그 서브 클래스에 대한 매칭을 설정하고, `LoggingAspect`를 바인딩합니다.

`MyApp` 클래스에서는 Guice의 `Injector`를 사용하여 `Service` 객체를 주입받고, `doSomething` 메서드를 실행합니다.

## 결론

Guice를 사용하면 AOP를 쉽게 구현할 수 있습니다. Guice의 `Matcher`와 `Module` 인터페이스를 활용하여 관심사를 분리하고, 코드의 재사용성과 유지보수성을 향상시킬 수 있습니다.

더 자세한 내용은 Guice의 공식 문서를 참조하시기 바랍니다.

- Guice 공식 문서: [https://github.com/google/guice](https://github.com/google/guice)