---
layout: post
title: "[java] Google Guice와 이벤트 드리븐 아키텍처(Ev erDriven Architecture) 사용하기"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

## 소개

이번 블로그 포스트에서는 Google Guice와 이벤트 드리븐 아키텍처의 사용법에 대해 알아보겠습니다. Google Guice는 자바 의존성 주입(Dependency Injection) 프레임워크로, 객체 간의 의존성을 자동으로 관리할 수 있도록 도와줍니다. 이벤트 드리븐 아키텍처는 시스템의 이벤트를 중심으로 설계될 때 발생하는 이점을 제공하는 소프트웨어 아키텍처입니다.

## Google Guice 설치 및 설정

먼저, Google Guice를 사용하기 위해 프로젝트에 의존성을 추가해야 합니다. Maven을 사용하는 경우 `pom.xml` 파일에 다음과 같은 의존성을 추가합니다:

```xml
<dependency>
    <groupId>com.google.inject</groupId>
    <artifactId>guice</artifactId>
    <version>4.2.3</version>
</dependency>
```

의존성을 추가한 후에는 Guice 모듈을 구현하여 객체들의 의존성을 정의해야 합니다. 다음은 Guice 모듈의 예입니다:

```java
import com.google.inject.AbstractModule;

public class MyModule extends AbstractModule {
    @Override
    protected void configure() {
        bind(Service.class).to(ServiceImpl.class);
    }
}
```

위 예제에서는 `Service` 인터페이스를 `ServiceImpl` 클래스에 바인딩하였습니다.

Guice를 설정한 후에는 `Injector`를 생성하고 필요한 의존성을 주입받을 수 있습니다. 다음은 Guice를 사용하여 의존성을 주입받는 예입니다:

```java
import com.google.inject.Guice;
import com.google.inject.Injector;

public class MyApp {
    public static void main(String[] args) {
        Injector injector = Guice.createInjector(new MyModule());
        Service service = injector.getInstance(Service.class);
        service.doSomething();
    }
}
```

위 예제에서는 `Service` 인터페이스를 구현한 객체를 `Injector`를 통해 주입받아 사용하였습니다.

## 이벤트 드리븐 아키텍처

이제 Google Guice를 사용하여 이벤트 드리븐 아키텍처를 구현하는 방법에 대해 알아보겠습니다. 이벤트 드리븐 아키텍처는 이벤트가 시스템 전체에 흐르는 중앙 집중화된 컴포넌트를 기반으로 구성됩니다. 이러한 컴포넌트를 이벤트 버스라고도 부릅니다.

첫 번째 단계는 이벤트를 정의하는 것입니다. 다음과 같은 예제를 통해 이벤트를 정의해 보겠습니다:

```java
public class MyEvent {
    private String data;

    public MyEvent(String data) {
        this.data = data;
    }

    public String getData() {
        return data;
    }
}
```

위 예제에서는 `MyEvent` 클래스를 정의하고 데이터를 담을 수 있는 필드와 접근자를 추가하였습니다.

다음 단계는 이벤트 핸들러를 구현하는 것입니다. 이벤트 핸들러는 특정 이벤트를 처리하는 로직을 포함합니다. 다음은 이벤트 핸들러의 예입니다:

```java
import com.google.inject.Singleton;

@Singleton
public class MyEventHandler {

    public void handleEvent(MyEvent event) {
        // 이벤트 처리 로직
    }
}
```

위 예제에서는 `@Singleton` 애노테이션을 사용하여 이벤트 핸들러를 싱글톤으로 만들었습니다. `handleEvent` 메서드는 `MyEvent` 객체를 매개변수로 받아 이벤트를 처리하는 로직을 포함하도록 구현합니다.

마지막 단계는 이벤트를 발송하는 것입니다. Guice의 `EventBus`를 사용하여 이벤트를 발송할 수 있습니다. 다음은 이벤트를 발송하는 예입니다:

```java
import com.google.inject.Inject;

public class MyService {

    private final EventBus eventBus;

    @Inject
    public MyService(EventBus eventBus) {
        this.eventBus = eventBus;
    }

    public void doSomething() {
        // 이벤트 발송
        eventBus.post(new MyEvent("Hello world!"));
    }
}
```

위 예제에서는 `MyService` 클래스에서 `EventBus`를 주입받고, `doSomething` 메서드에서 `EventBus`를 사용하여 `MyEvent` 객체를 발송하였습니다.

## 결론

이번 포스트에서는 Google Guice와 이벤트 드리븐 아키텍처의 사용법에 대해 알아보았습니다. Google Guice를 사용하여 의존성 주입을 효과적으로 관리하고, 이벤트 드리븐 아키텍처를 구현하여 시스템을 유연하고 확장 가능하게 만들 수 있습니다. Google Guice와 이벤트 드리븐 아키텍처는 모두 잘 구성된 소프트웨어 시스템을 구축하는 데 도움이 됩니다.

**참고자료:**
- [Google Guice 공식 문서](https://github.com/google/guice)
- [이벤트 드리븐 아키텍처 소개](https://martinfowler.com/articles/agsd-evolve-ems.html)