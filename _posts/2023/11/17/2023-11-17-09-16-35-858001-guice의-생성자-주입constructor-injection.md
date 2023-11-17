---
layout: post
title: "[java] Guice의 생성자 주입(Constructor Injection)"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

Guice는 자바 의존성 주입(Dependency Injection) 프레임워크로서, 의존성을 주입하는 방법 중 하나로 생성자 주입(Constructor Injection)을 지원합니다. 생성자 주입은 객체를 생성할 때 해당 객체의 의존성을 생성자를 통해 전달하는 방식입니다. Guice를 사용하여 생성자 주입을 수행하면 코드의 가독성과 유지보수성을 높일 수 있습니다.

## 생성자 주입의 장점

1. 유연성: 생성자 주입은 의존성을 명시적으로 선언하므로, 코드의 의존성 관리를 개선할 수 있습니다. 인터페이스에 대한 의존성을 가지므로, 다른 구현체로의 교체가 용이합니다.

2. 테스트 용이성: 생성자 주입을 사용하면 의존성을 모킹(Mocking) 또는 스텁(Stub) 객체와 교체할 수 있습니다. 이는 단위 테스트를 작성할 때 매우 유용합니다.

3. 컴파일 타임 의존성 검사: 생성자 주입은 컴파일 타임에 의존성을 검사하므로, 런타임에 의존성이 누락되는 오류를 방지할 수 있습니다.

## Guice를 사용한 생성자 주입 예제

```java
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;

    @Inject
    public UserServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    // UserService 인터페이스 메소드 구현
    // ...
}
```

위의 예제에서는 UserServiceImpl 클래스의 생성자에 @Inject 어노테이션을 사용하여 UserRepository 객체의 주입을 요청합니다. Guice는 UserRepository의 인스턴스를 알맞게 주입하여 UserServiceImpl 객체를 생성하고 반환합니다.

## Guice Module 설정

위의 예제에서는 Guice의 Module을 설정하지 않았습니다. Guice Module을 사용하면 객체 간의 의존성을 자동으로 주입할 수 있습니다. 아래는 Guice Module을 사용하여 UserRepository 객체를 바인딩하는 예제입니다.

```java
public class MyModule extends AbstractModule {

    @Override
    protected void configure() {
        bind(UserRepository.class).to(UserRepositoryImpl.class);
    }
}
```

위의 예제에서는 UserRepository 인터페이스를 UserRepositoryImpl 클래스에 바인딩하였습니다. Guice는 이 바인딩 정보를 기반으로 생성자 주입을 수행합니다.

## 결론

Guice의 생성자 주입(Constructor Injection)을 사용하면 코드의 가독성과 유지보수성을 개선할 수 있습니다. 의존성을 명시적으로 선언하므로 유연하게 코드를 확장하고 테스트하기 쉽습니다. Guice Module을 사용하면 객체 간의 의존성을 자동으로 주입할 수 있어 더욱 효율적인 개발이 가능합니다. Guice를 사용하여 의존성 주입을 구현하는 방법을 익히면, 더욱 풍부한 애플리케이션을 구현할 수 있을 것입니다.

## 참고 자료

- Guice Documentation: [https://github.com/google/guice](https://github.com/google/guice)
- Dependency Injection in Java with Guice Tutorial: [https://www.baeldung.com/guice](https://www.baeldung.com/guice)