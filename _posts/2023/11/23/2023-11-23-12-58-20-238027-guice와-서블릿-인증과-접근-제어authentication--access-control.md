---
layout: post
title: "[java] Guice와 서블릿 인증과 접근 제어(Authentication & Access Control)"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

서블릿 기반의 웹 애플리케이션을 개발할 때, 보안은 매우 중요한 요소입니다. 특히 인증과 접근 제어는 사용자의 권한에 따라 특정 페이지 또는 기능에 접근을 허용 또는 제한하는데 사용됩니다. 이번 글에서는 Guice와 서블릿을 함께 사용하여 간단한 인증 및 접근 제어 시스템을 구현하는 방법을 알아보겠습니다.

## 1. Guice 소개

Guice는 구글에서 개발한 의존성 주입(Dependency Injection) 프레임워크입니다. Guice를 사용하면 객체 간의 의존성을 자동으로 주입해주어 코드의 유지보수성과 테스트 용이성을 높일 수 있습니다.

## 2. 서블릿 인증 필터 구현

서블릿 인증은 사용자의 신원을 확인하는 작업을 의미합니다. Guice의 `Filter` 기능을 사용하면 서블릿 인증 필터를 구현할 수 있습니다.

```java
import com.google.inject.Inject;
import com.google.inject.Singleton;
import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Singleton
public class AuthenticationFilter implements Filter {

    private final AuthenticationService authService;

    @Inject
    public AuthenticationFilter(AuthenticationService authService) {
        this.authService = authService;
    }

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // 초기화 작업
    }

    @Override
    public void doFilter(ServletRequest servletRequest,
                         ServletResponse servletResponse, 
                         FilterChain filterChain)
            throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse response = (HttpServletResponse) servletResponse;

        // 인증 로직 작성
        if (authService.isAuthenticated(request)) {
            // 인증된 사용자일 경우 다음 필터로 이동
            filterChain.doFilter(request, response);
        } else {
            // 인증되지 않은 사용자일 경우 인증 실패 처리
            response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
        }
    }

    @Override
    public void destroy() {
        // 필터 종료 시 호출되는 메소드
    }
}
```

위 코드에서 `AuthenticationFilter`는 Guice의 `@Singleton` 애노테이션을 사용하여 싱글톤 객체로 만들어지고, `AuthenticationService`를 주입받아 사용합니다. `doFilter` 메소드에서는 요청된 URL의 인증 여부를 확인하고, 인증된 사용자일 경우 다음 필터로 이동하도록 처리합니다.

## 3. 서블릿 접근 제어 필터 구현

서블릿 접근 제어는 인증된 사용자의 권한에 따라 특정 페이지 또는 기능에 대한 접근을 허용 또는 제한하는 작업입니다. Guice의 `Filter` 기능을 사용하여 서블릿 접근 제어 필터를 구현할 수 있습니다.

```java
import com.google.inject.Inject;
import com.google.inject.Singleton;
import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Singleton
public class AccessControlFilter implements Filter {

    private final AccessControlService accessControlService;

    @Inject
    public AccessControlFilter(AccessControlService accessControlService) {
        this.accessControlService = accessControlService;
    }

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // 초기화 작업
    }

    @Override
    public void doFilter(ServletRequest servletRequest,
                         ServletResponse servletResponse,
                         FilterChain filterChain)
            throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse response = (HttpServletResponse) servletResponse;

        String requestedUrl = request.getRequestURI();

        // 접근 제어 로직 작성
        if (accessControlService.isAccessAllowed(requestedUrl)) {
            // 권한이 허용된 경우 다음 필터로 이동
            filterChain.doFilter(request, response);
        } else {
            // 권한이 제한된 경우 접근 거부 처리
            response.setStatus(HttpServletResponse.SC_FORBIDDEN);
        }
    }

    @Override
    public void destroy() {
        // 필터 종료 시 호출되는 메소드
    }
}
```

위 코드에서 `AccessControlFilter`는 `AccessControlService`를 주입받아 사용하며, `doFilter` 메소드에서는 요청된 URL의 접근 권한을 확인하고, 허용된 경우 다음 필터로 이동하도록 처리합니다.

## 4. Guice 모듈 구성

위에서 작성한 인증 필터와 접근 제어 필터를 Guice 모듈에 등록하여 사용할 수 있습니다.

```java
import com.google.inject.AbstractModule;

public class AppInjector extends AbstractModule {

    @Override
    protected void configure() {
        bind(AuthenticationService.class).to(AuthenticationServiceImpl.class);
        bind(AccessControlService.class).to(AccessControlServiceImpl.class);
        
        filter("/*").through(AuthenticationFilter.class);
        filter("/*").through(AccessControlFilter.class);
    }
}
```

위 코드에서 `AppInjector` 클래스는 `AbstractModule`을 상속받아 Guice 모듈을 정의합니다. `configure` 메소드에서 `AuthenticationService`, `AccessControlService`를 실제 구현체와 매핑하고, `filter` 메소드를 사용하여 필터를 등록합니다.

## 5. 서블릿 컨테이너 구성

마지막으로, 서블릿 컨테이너에 Guice 모듈을 등록하여 인증과 접근 제어 기능을 사용할 수 있도록 설정해야 합니다. 아래는 예시로 Apache Tomcat에서 Guice를 사용하는 방법입니다.

1. `web.xml` 파일에 Guice `Listener`와 `Filter`를 등록합니다.

```xml
<listener>
    <listener-class>com.google.inject.servlet.GuiceServletContextListener</listener-class>
</listener>

<filter>
    <filter-name>GuiceFilter</filter-name>
    <filter-class>com.google.inject.servlet.GuiceFilter</filter-class>
</filter>

<filter-mapping>
    <filter-name>GuiceFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

2. `GuiceServletContextListener`를 구현하여 `AppInjector`를 등록합니다.

```java
import com.google.inject.Guice;
import com.google.inject.Injector;
import com.google.inject.servlet.GuiceServletContextListener;

public class MyGuiceServletContextListener extends GuiceServletContextListener {

    @Override
    protected Injector getInjector() {
        return Guice.createInjector(new AppInjector());
    }
}
```

위 설정을 통해 Guice와 서블릿을 함께 사용하여 인증과 접근 제어 기능을 구현할 수 있습니다.

## 결론

이번 글에서는 Guice와 서블릿을 사용하여 간단한 인증과 접근 제어 시스템을 구현하는 방법을 알아보았습니다. Guice의 의존성 주입 기능을 통해 코드의 유지보수성과 테스트 용이성을 높일 수 있으며, 서블릿 필터를 이용하여 보안을 강화할 수 있습니다.

더 자세한 내용은 다음 참고 자료를 참고하시기 바랍니다.

- Guice 공식 문서: [https://github.com/google/guice/wiki](https://github.com/google/guice/wiki)
- 서블릿 필터에 대한 자세한 내용: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Controlling_access_to_content](https://developer.mozilla.org/en-US/docs/Web/HTTP/Controlling_access_to_content)