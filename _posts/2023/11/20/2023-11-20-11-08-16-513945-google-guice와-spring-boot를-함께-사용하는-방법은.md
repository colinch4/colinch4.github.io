---
layout: post
title: "[java] Google Guice와 Spring Boot를 함께 사용하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

Java 개발자들은 의존성 주입(Dependency Injection)을 적용해 컴포넌트들을 느슨하게 연결하여 유연하고 테스트 가능한 코드를 작성하는 것에 관심을 가지고 있습니다. Google Guice와 Spring Boot는 두 가지 인기있는 프레임워크로, 각각 독립적으로 의존성 주입을 제공합니다. 이번 포스트에서는 Google Guice와 Spring Boot를 함께 사용하는 방법을 알아보겠습니다.

## Dependencies 설정

먼저, Maven이나 Gradle과 같은 빌드 도구를 사용하여 프로젝트의 dependencies를 설정해야 합니다. 아래의 예시는 이를 위한 Maven의 `pom.xml` 파일입니다.

```xml
<dependencies>
    <!-- Spring Boot dependencies -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>

    <!-- Google Guice dependency -->
    <dependency>
        <groupId>com.google.inject</groupId>
        <artifactId>guice</artifactId>
        <version>4.2.3</version>
    </dependency>
</dependencies>
```

## Guice 설정하기

다음으로는 Guice의 설정을 제공해야 합니다. 아래 예시에서는 `MyModule` 클래스를 만들어 Guice 모듈을 구성합니다.

```java
import com.google.inject.AbstractModule;

public class MyModule extends AbstractModule {
    @Override
    protected void configure() {
        // Guice 바인딩 설정
        // ...
    }
}
```

## Spring Boot와 Guice 통합하기

Spring Boot에서 Guice를 사용하기 위해서는 `@EnableGuiceModules` 애노테이션을 사용하여 Guice 모듈을 활성화해야 합니다. 아래의 예시는 Spring Boot 애플리케이션 클래스에 `@EnableGuiceModules` 애노테이션을 추가한 것입니다.

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import com.google.inject.Module;
import com.google.inject.Guice;

@SpringBootApplication
@EnableGuiceModules
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }

    @Autowired
    private Module guiceModule;

    @Bean
    public Injector injector() {
        return Guice.createInjector(guiceModule);
    }
}
```

위의 코드에서 `Module guiceModule`은 `MyModule` 클래스의 인스턴스로 초기화됩니다.

## Guice와 Spring Boot 함께 사용하기

이제 Guice와 Spring Boot가 함께 작동합니다. Guice를 사용하여 의존성을 주입하면 Spring Boot의 기능을 그대로 사용할 수 있습니다. 예를 들어, 아래 코드에서는 `MyService` 클래스에 `@Inject` 애노테이션을 사용하여 의존성을 주입하고 있습니다.

```java
import javax.inject.Inject;

public class MyService {
    private final MyDependency myDependency;

    @Inject
    public MyService(MyDependency myDependency) {
        this.myDependency = myDependency;
    }

    // ...
}
```

## 결론

Google Guice와 Spring Boot를 함께 사용하는 방법에 대해 알아보았습니다. 이를 통해 Guice를 사용하여 의존성 주입을 적용하고, Spring Boot의 편리한 기능을 활용할 수 있습니다. 이러한 조합은 유연한 애플리케이션 개발과 테스트를 도와줍니다.

## 참고 자료
- [Google Guice 공식 문서](https://github.com/google/guice/wiki)
- [Spring Boot 공식 문서](https://spring.io/projects/spring-boot)