---
layout: post
title: "[java] Guice와 함께하는 Java 서블릿 의존성 주입(Dependency Injection)"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

의존성 주입(Dependency Injection)은 객체 간의 의존 관계를 외부로부터 주입받는 방식으로 관리하는 디자인 패턴입니다. 이를 통해 코드의 유연성과 테스트 용이성을 높일 수 있습니다.  이번 글에서는 Guice를 사용하여 Java 서블릿에서 의존성 주입을 어떻게 구현하는지 알아보겠습니다.

## Guice란?

Guice는 자바의 종속성 주입 프레임워크로, Google에서 개발한 오픈 소스 라이브러리입니다. Guice는 강력한 바인딩 기능을 제공하여 객체의 의존성을 자동으로 해결해줍니다.

## Guice를 사용한 서블릿 의존성 주입

먼저 Guice를 프로젝트에 추가해야 합니다. Maven을 사용하고 있다면 `pom.xml` 파일에 다음과 같이 의존성을 추가합니다.

```xml
<dependency>
    <groupId>com.google.inject</groupId>
    <artifactId>guice</artifactId>
    <version>4.2.3</version>
</dependency>
```

의존성을 추가한 후, 다음과 같이 Guice의 `ServletModule`을 확장한 모듈을 만듭니다.

```java
import com.google.inject.servlet.ServletModule;

public class MyServletModule extends ServletModule {
    @Override
    protected void configureServlets() {
        bind(MyService.class).to(MyServiceImpl.class); // 의존성 바인딩
        serve("/myservlet").with(MyServlet.class); // 서블릿 등록
    }
}
```

`MyServletModule`에서 `configureServlets` 메서드를 오버라이드하여 의존성을 바인딩하고 서블릿을 등록합니다.

다음으로, `MyService`와 `MyServlet` 클래스를 작성합니다.

```java
public interface MyService {
    void doSomething();
}

public class MyServiceImpl implements MyService {
    @Override
    public void doSomething() {
        System.out.println("Doing something...");
    }
}

public class MyServlet extends HttpServlet {
    // MyService 의존성 주입
    @Inject
    private MyService myService;

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        myService.doSomething();
        resp.getWriter().write("MyServlet response");
    }
}
```

`MyServlet` 클래스에서는 `@Inject` 애노테이션을 사용하여 `MyService`를 주입받습니다. 이렇게하면 Guice가 `MyService`의 구현체를 찾아서 자동으로 주입해줍니다.

마지막으로, `web.xml` 파일에 `GuiceServletContextListener`를 등록합니다.

```xml
<listener>
    <listener-class>com.google.inject.servlet.GuiceServletContextListener</listener-class>
</listener>
<context-param>
    <param-name>guice.modules</param-name>
    <param-value>com.example.MyServletModule</param-value>
</context-param>
```

`GuiceServletContextListener`를 등록함으로써 Guice가 서블릿 컨텍스트를 관리하도록 합니다. `guice.modules` 매개변수로 `MyServletModule` 클래스를 지정합니다.

이제 서블릿을 실행하고 `/myservlet` 경로로 요청을 보내면, `MyServlet`에서 `MyService`의 메서드가 호출되고 응답을 받을 수 있습니다.

## 마무리

Guice를 사용하여 Java 서블릿에서 의존성 주입을 구현하는 방법에 대해 알아보았습니다. Guice를 사용하면 복잡한 의존성을 간단하게 주입할 수 있으며, 유지보수와 테스트도 용이해집니다. Guice에 대해 더 자세히 알고 싶다면 [공식 문서](https://github.com/google/guice/wiki/GettingStarted)를 참고해보세요.