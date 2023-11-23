---
layout: post
title: "[java] Guice를 활용한 서블릿 요청 로깅과 통계(Logging & Statistics)"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

## 개요
서블릿 애플리케이션에서는 요청 로깅과 통계를 수행하는 것이 중요합니다. 이를 통해 애플리케이션의 동작을 모니터링하고 성능 및 사용 통계를 수집할 수 있습니다. 이번 글에서는 Guice 프레임워크를 활용하여 서블릿 요청 로깅과 통계를 구현하는 방법을 알아보겠습니다.

## Guice 소개
Guice는 Google에서 제공하는 경량의 의존성 주입(Dependency Injection) 프레임워크입니다. 의존성 주입은 객체들 간의 의존 관계를 설정할 때 사용하는 디자인 패턴이며, 이를 통해 코드의 유연성과 테스트 용이성을 향상시킬 수 있습니다.

## Guice를 사용하여 서블릿 요청 로깅 구현하기
아래는 Guice를 사용하여 서블릿 요청 로깅을 수행하는 예제 코드입니다.

```java
import com.google.inject.AbstractModule;
import com.google.inject.Guice;
import com.google.inject.Inject;
import com.google.inject.Injector;
import lombok.extern.slf4j.Slf4j;

import javax.servlet.*;
import java.io.IOException;

@Slf4j
public class LoggingFilter implements Filter {

    @Inject
    private RequestLogService requestLogService;

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        Injector injector = Guice.createInjector(new LoggingModule());
        injector.injectMembers(this);
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        long startTime = System.currentTimeMillis();
        chain.doFilter(request, response);
        long duration = System.currentTimeMillis() - startTime;
        requestLogService.logRequest(request, duration);
    }

    @Override
    public void destroy() {
        // Cleanup logic
    }

    private static class LoggingModule extends AbstractModule {
        @Override
        protected void configure() {
            bind(RequestLogService.class).to(DefaultRequestLogService.class);
        }
    }
}

@Slf4j
public class DefaultRequestLogService implements RequestLogService {

    @Override
    public void logRequest(ServletRequest request, long duration) {
        log.info("Request: {}, Duration: {}ms", request.getRemoteAddr(), duration);
    }

}

public interface RequestLogService {
    void logRequest(ServletRequest request, long duration);
}
```

위 예제 코드에서는 Guice의 의존성 주입을 사용하여 `LoggingFilter`가 `RequestLogService`를 주입받도록 구현되어 있습니다. `LoggingFilter`는 `Filter` 인터페이스를 구현하며, `doFilter` 메소드를 통해 요청 로깅을 수행합니다. `RequestLogService`는 실제 로깅을 처리하는 서비스 인터페이스이며, `DefaultRequestLogService`는 이를 구현한 구현체입니다.

## Guice를 사용하여 서블릿 요청 통계 구현하기
아래는 Guice를 사용하여 서블릿 요청 통계를 수행하는 예제 코드입니다.

```java
import com.google.inject.AbstractModule;
import com.google.inject.Guice;
import com.google.inject.Inject;
import com.google.inject.Injector;
import lombok.extern.slf4j.Slf4j;

import javax.servlet.*;
import java.io.IOException;
import java.util.concurrent.atomic.AtomicLong;

@Slf4j
public class StatisticsFilter implements Filter {

    @Inject
    private RequestStatisticsService requestStatisticsService;

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        Injector injector = Guice.createInjector(new StatisticsModule());
        injector.injectMembers(this);
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        requestStatisticsService.incrementRequestCount();
        chain.doFilter(request, response);
    }

    @Override
    public void destroy() {
        // Cleanup logic
    }

    private static class StatisticsModule extends AbstractModule {
        @Override
        protected void configure() {
            bind(RequestStatisticsService.class).to(DefaultRequestStatisticsService.class);
        }
    }
}

@Slf4j
public class DefaultRequestStatisticsService implements RequestStatisticsService {

    private AtomicLong requestCount = new AtomicLong(0);

    @Override
    public void incrementRequestCount() {
        requestCount.incrementAndGet();
        log.info("Request count: {}", requestCount.get());
    }
}

public interface RequestStatisticsService {
    void incrementRequestCount();
}
```

위 예제 코드에서는 Guice의 의존성 주입을 사용하여 `StatisticsFilter`가 `RequestStatisticsService`를 주입받도록 구현되어 있습니다. `StatisticsFilter`는 `Filter` 인터페이스를 구현하며, `doFilter` 메소드를 통해 요청 통계를 수행합니다. `RequestStatisticsService`는 실제 통계를 처리하는 서비스 인터페이스이며, `DefaultRequestStatisticsService`는 이를 구현한 구현체입니다.

## Guice를 통한 모니터링 및 로깅 설정
위에서 구현한 `LoggingFilter`와 `StatisticsFilter`를 사용하여 서블릿 애플리케이션에서 요청 로깅과 통계를 수행할 수 있습니다. Guice의 모듈을 통해 필요한 의존성 주입 설정을 하고, `web.xml` 파일에서 필터를 등록해주면 됩니다.

```xml
<web-app>
    <filter>
        <filter-name>loggingFilter</filter-name>
        <filter-class>com.example.LoggingFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>loggingFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
    
    <filter>
        <filter-name>statisticsFilter</filter-name>
        <filter-class>com.example.StatisticsFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>statisticsFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
    
    <!-- servlets and other configurations -->
    
</web-app>
```

위 설정을 통해 모든 서블릿 요청에 대해 로깅과 통계가 수행되도록 구현할 수 있습니다.

## 결론
Guice를 사용하여 서블릿 애플리케이션에서 요청 로깅과 통계를 구현할 수 있습니다. Guice의 의존성 주입을 통해 유연하고 확장 가능한 코드를 작성할 수 있으며, 모니터링 및 로깅 설정을 통해 애플리케이션의 동작을 체계적으로 관리할 수 있습니다.

## 참고 자료
- [Guice User Guide](https://github.com/google/guice/wiki/GettingStarted)