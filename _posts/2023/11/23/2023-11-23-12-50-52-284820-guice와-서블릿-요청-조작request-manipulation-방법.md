---
layout: post
title: "[java] Guice와 서블릿 요청 조작(Request Manipulation) 방법"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Guice는 자바의 의존성 주입(Dependency Injection) 프레임워크로, 서블릿 기반 애플리케이션 개발에 많이 사용됩니다. Guice를 사용하여 서블릿 요청을 조작하는 방법을 알아보겠습니다.

## Guice 설정

먼저, Guice를 프로젝트에 추가해야 합니다. Maven을 사용한다면, `pom.xml` 파일에 다음 의존성을 추가하세요.

```xml
<dependency>
    <groupId>com.google.inject</groupId>
    <artifactId>guice</artifactId>
    <version>4.3.0</version>
</dependency>
```

Guice를 사용하기 위해 다음과 같이 `GuiceServletModule`을 상속하는 모듈 클래스를 작성합니다.

```java
import com.google.inject.servlet.ServletModule;

public class MyServletModule extends ServletModule {
    @Override
    protected void configureServlets() {
        // 서블릿 설정 및 바인딩
    }
}
```

## 서블릿 요청 조작

Guice를 사용하여 서블릿 요청을 조작하는 방법은 크게 두 가지입니다. 첫 번째는 서블릿 필터를 사용하는 방법이고, 두 번째는 서블릿 요청 핸들러를 사용하는 방법입니다.

### 1. 서블릿 필터 사용하기

서블릿 필터를 사용하여 서블릿 요청을 조작하려면, 다음과 같이 `Filter`를 상속하는 클래스를 작성합니다.

```java
import com.google.inject.Inject;

import javax.servlet.*;
import java.io.IOException;

public class MyFilter implements Filter {

    @Inject
    private MyService myService;

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        // 요청 처리 전 필요한 작업 수행
        myService.doSomething();

        // 다음 필터 또는 서블릿 호출
        chain.doFilter(request, response);

        // 응답 처리 후 필요한 작업 수행
    }

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // 필터 초기화
    }

    @Override
    public void destroy() {
        // 필터 해제
    }
}
```

위 예제에서 `MyService`는 Guice가 주입하는 의존성입니다. `doFilter()` 메서드에서 서블릿 요청 전후에 필요한 작업을 수행할 수 있습니다.

`MyServletModule` 클래스의 `configureServlets()` 메서드에서 서블릿 필터를 바인딩 해야 합니다. 다음과 같이 작성합니다.

```java
import com.google.inject.servlet.ServletModule;

public class MyServletModule extends ServletModule {
    @Override
    protected void configureServlets() {
        // 서블릿 설정 및 바인딩
        filter("/*").through(MyFilter.class);
    }
}
```

### 2. 서블릿 요청 핸들러 사용하기

서블릿 요청 핸들러를 사용하여 서블릿 요청을 조작하려면, 다음과 같이 `HttpServlet`을 상속하는 클래스를 작성합니다.

```java
import com.google.inject.Inject;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class MyServlet extends HttpServlet {

    @Inject
    private MyService myService;

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // GET 요청 처리
        myService.doSomething();
        // 응답 처리
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // POST 요청 처리
        myService.doSomething();
        // 응답 처리
    }
}
```

위 예제에서 `MyService`는 Guice가 주입하는 의존성입니다. `doGet()`과 `doPost()` 메서드에서 GET과 POST 요청을 처리할 수 있습니다.

`MyServletModule` 클래스의 `configureServlets()` 메서드에서 서블릿을 바인딩 해야 합니다. 다음과 같이 작성합니다.

```java
import com.google.inject.servlet.ServletModule;

public class MyServletModule extends ServletModule {
    @Override
    protected void configureServlets() {
        // 서블릿 설정 및 바인딩
        serve("/myServlet").with(MyServlet.class);
    }
}
```

## 결론

Guice를 사용하여 서블릿 요청을 조작하는 방법을 살펴보았습니다. 서블릿 필터를 사용하거나, 서블릿 요청 핸들러를 사용하여 Guice를 통해 의존성을 주입할 수 있습니다. Guice를 사용하면 응용 프로그램의 유연성이 증가하고, 재사용 가능한 코드를 작성할 수 있습니다.

## 참고 자료
- [Guice Documentation](https://github.com/google/guice/wiki)
- [Servlet Filter Tutorial](https://www.baeldung.com/java-servlet-filters)
- [Servlet Tutorial](https://www.tutorialspoint.com/servlets/index.htm)