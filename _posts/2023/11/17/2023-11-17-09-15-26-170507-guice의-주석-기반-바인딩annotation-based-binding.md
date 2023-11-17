---
layout: post
title: "[java] Guice의 주석 기반 바인딩(Annotation-based Binding)"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

Guice는 주석 기반 바인딩을 사용하여 의존성 주입을 구성하는 강력한 프레임워크입니다. 주석 기반 바인딩을 사용하면 특정 어노테이션과 바인딩된 클래스의 인스턴스를 Guice가 자동으로 찾아서 의존성을 주입합니다.

## 주석 기반 바인딩의 장점

- 코드베이스를 더욱 명확하게 만들어줍니다. 주석을 통해 어떤 클래스가 어떤 인터페이스와 바인딩되는지 명확하게 알 수 있습니다.
- 구성이 더욱 유연해집니다. 어노테이션을 사용하여 특정 인터페이스에 대한 다양한 구현 클래스를 바인딩할 수 있습니다.
- 컴파일 타임에 오류를 검출할 수 있습니다. 어노테이션에 오타가 있거나 바인딩이 잘못되었을 경우 컴파일 타임에 오류가 발생하여 빠르게 수정할 수 있습니다.

## 주석 기반 바인딩의 사용 방법

주석 기반 바인딩을 사용하려면 먼저 `@BindingAnnotation` 어노테이션을 만들어야 합니다. 이 어노테이션은 바인딩에 사용될 특정 어노테이션을 나타냅니다.

``` java
import com.google.inject.BindingAnnotation;

@BindingAnnotation
@Retention(RetentionPolicy.RUNTIME)
public @interface MyAnnotation {
}
```

그런 다음 바인딩할 클래스에 `@MyAnnotation` 어노테이션을 추가합니다.

``` java
import javax.inject.Inject;

public class MyService {
    private final MyDependency dependency;

    @Inject
    public MyService(@MyAnnotation MyDependency dependency) {
        this.dependency = dependency;
    }
}
```

마지막으로 Guice 구성 파일에서 `@MyAnnotation` 어노테이션과 바인딩될 클래스를 설정합니다.

```java
import com.google.inject.AbstractModule;
import com.google.inject.Guice;
import com.google.inject.Injector;

public class MyAppModule extends AbstractModule {
    @Override
    protected void configure() {
        bind(MyDependency.class).annotatedWith(MyAnnotation.class).to(MyDependencyImpl.class);
    }
}

public class MyApp {
    public static void main(String[] args) {
        Injector injector = Guice.createInjector(new MyAppModule());
        MyService myService = injector.getInstance(MyService.class);
    }
}
```

위의 예제에서는 `MyDependency` 인터페이스와 `MyDependencyImpl` 클래스를 `@MyAnnotation` 어노테이션과 바인딩하여 `MyService`에 주입했습니다. Guice는 `MyService`를 인스턴스화 할 때 `MyDependencyImpl` 인스턴스를 자동으로 주입합니다.

## 결론

Guice의 주석 기반 바인딩은 의존성 주입을 명확하게 표현하고 유연하게 구성할 수 있는 강력한 방법입니다. 주석 기반 바인딩을 사용하면 코드의 가독성과 유지보수성을 향상시키는 동시에 개발 생산성을 향상시킬 수 있습니다.

## 참고 자료

- [Guice 사용자 가이드](https://github.com/google/guice/wiki/GettingStarted)
- [Guice 공식 문서](https://github.com/google/guice)