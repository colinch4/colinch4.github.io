---
layout: post
title: "[java] Google Guice와 객체 인식(Object Recognition) 구현하기"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

Google Guice는 Java 개발자들을 위한 의존성 주입(Dependency Injection) 프레임워크로, 객체 인식(Object Recognition) 기능도 제공합니다. 객체 인식은 Guice의 핵심 기능 중 하나로, 클래스와 인터페이스를 기반으로 자동으로 구현체를 찾아 의존성을 주입해줍니다.

이 글에서는 Google Guice를 사용하여 객체 인식 기능을 구현하는 방법에 대해 알아보겠습니다.

## Guice 설정하기

Google Guice를 사용하기 위해서는 먼저 프로젝트에 Guice 라이브러리를 추가해야 합니다. Maven을 사용한다면 `pom.xml` 파일에 다음과 같이 의존성을 추가하세요:

```xml
<dependency>
    <groupId>com.google.inject</groupId>
    <artifactId>guice</artifactId>
    <version>4.2.3</version>
</dependency>
```

Gradle을 사용한다면 `build.gradle` 파일에 다음과 같이 의존성을 추가하세요:

```groovy
implementation 'com.google.inject:guice:4.2.3'
```

## 인터페이스와 구현체 정의하기

Guice를 사용하여 객체 인식을 구현하려면 먼저 인터페이스와 구현체를 정의해야 합니다. 예를 들어, `UserService` 인터페이스와 `UserServiceImpl` 구현체를 만들어보겠습니다.

```java
public interface UserService {
    void createUser(String username);
}

public class UserServiceImpl implements UserService {
    @Override
    public void createUser(String username) {
        // 사용자 생성 로직
    }
}
```

## 모듈 생성하기

Guice에서 객체 인식을 위해 모듈을 생성해야 합니다. 모듈은 `AbstractModule` 클래스를 상속받아 구현할 수 있습니다. 모듈 내에서 인터페이스와 구현체를 바인딩하고 Guice에게 의존성을 주입받을 방법을 알려줍니다.

```java
public class AppModule extends AbstractModule {
    @Override
    protected void configure() {
        bind(UserService.class).to(UserServiceImpl.class);
    }
}
```

## Guice 초기화하기

마지막으로 애플리케이션에서 Guice를 초기화해야 합니다. `Main` 클래스에서 다음과 같이 Guice를 초기화하고 의존성을 주입받아 사용할 수 있습니다.

```java
public class Main {
    public static void main(String[] args) {
        Injector injector = Guice.createInjector(new AppModule());
        UserService userService = injector.getInstance(UserService.class);

        userService.createUser("John");
    }
}
```

위 코드에서 `Injector` 인스턴스를 생성하고, `getInstance()` 메서드를 이용하여 `UserService` 인터페이스의 구현체를 가져올 수 있습니다. 이후 `userService` 인스턴스를 사용하여 `createUser()` 메서드를 호출할 수 있습니다.

## 결론

Google Guice를 사용하여 객체 인식을 구현하는 방법에 대해 알아보았습니다. Guice를 사용하면 의존성 주입을 통해 객체 인식을 쉽게 구현할 수 있고, 코드의 유지보수성과 확장성을 높일 수 있습니다.

더 자세한 내용은 [Google Guice 문서](https://github.com/google/guice/wiki)를 참고하시기 바랍니다.