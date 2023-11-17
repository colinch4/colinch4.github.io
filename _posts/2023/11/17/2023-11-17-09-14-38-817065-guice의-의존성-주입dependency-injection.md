---
layout: post
title: "[java] Guice의 의존성 주입(Dependency Injection)"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

Guice는 Java 개발자들이 의존성 주입(Dependency Injection)을 사용하여 애플리케이션을 구축할 수 있도록 도와주는 경량급 의존성 주입 프레임워크입니다. Guice는 Google에 의해 개발되었으며, 자바의 기본적인 의존성 주입 프레임워크인 Spring Framework와 비교하여 더 가벼운 솔루션을 제공합니다.

의존성 주입은 객체 간의 의존 관계를 외부에서 주입하는 디자인 패턴입니다. 이를 통해 애플리케이션의 결합도를 낮추고 재사용 가능한 코드를 작성할 수 있습니다. Guice를 사용하면 객체 생성 및 관리 작업을 자동으로 처리할 수 있으며, 코드의 가독성과 유지보수성을 향상시킬 수 있습니다.

## Guice의 기본 개념

Guice에서는 다음과 같은 주요 개념을 사용합니다:

### 바인딩(Binding)

Guice에서 바인딩은 의존성을 정의하는 방법입니다. 바인딩은 인터페이스와 그에 해당하는 구현체를 매핑하는 역할을 합니다. 이를 통해 Guice는 애플리케이션에서 해당 인터페이스를 필요로 하는 객체를 자동으로 생성하고 주입합니다.

### 모듈(Module)

Guice는 모듈을 통해 바인딩을 구성합니다. 모듈은 의존성을 관리하는 단위로서, 애플리케이션에서 사용되는 바인딩을 정의합니다. 모듈은 `AbstractModule` 클래스를 확장하여 정의하며, `configure()` 메서드에서 바인딩을 설정합니다.

### 주입(Injection)

Guice는 주입을 통해 의존성을 자동으로 주입합니다. 주입은 컨테이너가 애플리케이션의 객체에 필요한 의존성을 자동으로 주입하는 과정을 말합니다. Guice는 `@Inject` 어노테이션을 사용하여 주입할 대상을 표시합니다.

## Guice를 사용한 의존성 주입 예제

다음은 Guice를 사용하여 의존성 주입을 구현하는 간단한 예제입니다.

```java
public interface UserService {
  void addUser(String username);
}

public class UserServiceImpl implements UserService {
  @Override
  public void addUser(String username) {
    System.out.println("Adding user: " + username);
  }
}

public class MyModule extends AbstractModule {
  @Override
  protected void configure() {
    bind(UserService.class).to(UserServiceImpl.class);
  }
}

public class MyApp {
  @Inject
  private UserService userService;

  public void addUser(String username) {
    userService.addUser(username);
  }
}

public class Main {
  public static void main(String[] args) {
    Injector injector = Guice.createInjector(new MyModule());
    MyApp app = injector.getInstance(MyApp.class);

    app.addUser("john_doe");
  }
}
```

위의 예제에서 `UserService` 인터페이스와 `UserServiceImpl` 클래스는 Guice의 바인딩을 통해 연결됩니다. `MyApp` 클래스에서 `@Inject` 어노테이션을 사용하여 `UserService` 의존성이 주입됩니다. 마지막으로 `Main` 클래스에서 Guice 컨테이너를 생성하고 `MyApp` 인스턴스를 가져와서 사용합니다.

## Guice의 장점

- 가벼운 프레임워크로서 애플리케이션의 시작 시간과 메모리 사용량을 줄일 수 있습니다.
- 코드의 가독성이 용이하고 유지보수성이 높습니다.
- 컴파일 시점에 의존성 주입 에러를 검출할 수 있습니다.
- 테스트 용이성을 제공하여 모의 객체(Mock Object) 등을 사용한 단위 테스트를 수행할 수 있습니다.

## 결론

Guice는 Java 개발자들이 의존성 주입을 편리하게 사용할 수 있는 경량급 프레임워크입니다. 의존성 주입을 통해 코드의 유지보수성과 테스트 용이성을 향상시킬 수 있으며, Guice의 가벼운 성격은 애플리케이션의 성능과 메모리 사용을 개선해 줄 수 있습니다.

더 자세한 내용은 [Guice 공식 문서](https://github.com/google/guice/wiki/GettingStarted)를 참조하세요.