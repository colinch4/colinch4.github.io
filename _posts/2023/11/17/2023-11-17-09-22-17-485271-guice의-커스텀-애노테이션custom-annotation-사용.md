---
layout: post
title: "[java] Guice의 커스텀 애노테이션(Custom Annotation) 사용"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

Guice는 의존성 주입(Dependency Injection) 프레임워크로, 개발자가 클래스나 메서드에 애노테이션을 부여하여 의존성을 주입받을 수 있도록 지원합니다. 이러한 애노테이션은 Guice에서 제공하는 기본 애노테이션 외에도, 개발자가 직접 만들어 사용할 수도 있습니다.

이번 포스트에서는 Guice의 커스텀 애노테이션을 만들고 사용하는 방법에 대해 알아보겠습니다.

## 애노테이션 정의하기

애노테이션은 `@interface` 키워드를 사용하여 정의할 수 있습니다. Guice에서 사용할 커스텀 애노테이션을 만들기 위해서는, `@BindingAnnotation` 애노테이션을 추가해야 합니다.

```java
import com.google.inject.BindingAnnotation;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
@BindingAnnotation
public @interface CustomAnnotation {
    // 애노테이션 멤버 정의
}
```

위의 예제에서는 `@CustomAnnotation`이라는 커스텀 애노테이션을 정의하였습니다. 기본적으로 `@Retention(RetentionPolicy.RUNTIME)` 애노테이션을 추가하여, 런타임 시에 애노테이션 정보를 유지하도록 설정하였습니다.

## 애노테이션 사용하기

정의한 애노테이션을 사용하기 위해서는, 애노테이션을 사용하고자 하는 필드나 메서드에 해당 애노테이션을 부여해야 합니다. 

다음은 커스텀 애노테이션을 사용하여 의존성 주입을 받는 예제입니다.

```java
import com.google.inject.Inject;

public class MyService {

    @Inject
    @CustomAnnotation
    private MyDependency myDependency;

    // ...

}
```

위의 예제에서는 `@CustomAnnotation` 애노테이션을 `@Inject` 애노테이션과 함께 사용하여 `myDependency` 필드에 의존성 주입을 받도록 설정하였습니다.

## 커스텀 애노테이션 바인딩하기

커스텀 애노테이션을 사용하기 위해서는, Guice 모듈에서 애노테이션과 바인딩할 구현체를 설정해야 합니다.

```java
import com.google.inject.AbstractModule;

public class MyModule extends AbstractModule {

    @Override
    protected void configure() {
        bind(MyDependency.class).to(MyDependencyImpl.class).in(Singleton.class);
        bind(MyService.class);
    }
}
```

위의 예제에서는 `MyDependency` 인터페이스를 `MyDependencyImpl` 클래스에 바인딩하고, `MyService` 클래스를 바인딩하였습니다. 필요에 따라 애노테이션과 바인딩할 클래스나 인터페이스를 지정해주면 됩니다.

## 결론

이번 포스트에서는 Guice의 커스텀 애노테이션을 만들고 사용하는 방법에 대해 알아보았습니다. 커스텀 애노테이션을 사용하면 의존성 주입을 더욱 효율적으로 관리할 수 있으며, 깔끔하고 가독성 있는 코드를 작성할 수 있습니다. 자세한 내용은 Guice 공식 문서를 참고하시기 바랍니다.

- Guice 공식 문서: [https://github.com/google/guice](https://github.com/google/guice)