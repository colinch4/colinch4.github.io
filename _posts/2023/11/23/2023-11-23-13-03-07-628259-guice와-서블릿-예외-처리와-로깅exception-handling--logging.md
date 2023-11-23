---
layout: post
title: "[java] Guice와 서블릿 예외 처리와 로깅(Exception Handling & Logging)"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

이번 포스트에서는 Guice와 서블릿을 사용하여 예외 처리와 로깅을 어떻게 구현하는지 알아보겠습니다.

## Guice를 이용한 예외 처리

Guice를 사용하면 의존성 주입(Dependency Injection)을 통해 예외 처리를 간단하게 구현할 수 있습니다. 예외 처리를 위한 모듈을 만들고, Guice에서 해당 모듈을 바인딩하면 됩니다.

먼저, 예외 처리를 위한 모듈을 만들어보겠습니다.

```java
public class ExceptionModule extends AbstractModule {
    
    @Override
    protected void configure() {
        bind(ExceptionHandler.class).to(DefaultExceptionHandler.class);
    }
}
```

이 모듈은 ExceptionHandler 인터페이스를 기본 구현체(DefaultExceptionHandler)에 바인딩합니다. 이렇게 함으로써 예외가 발생했을 때 DefaultExceptionHandler가 사용되도록 설정됩니다.

다음으로, 서블릿 모듈을 만들어보겠습니다.

```java
public class ServletModule extends AbstractModule {
    
    @Override
    protected void configure() {
        bind(MyServlet.class);
        bind(MyFilter.class);
    }
    
    @Provides
    public ServletContext provideServletContext() {
        return getServletContext();
    }
}
```

ServletModule은 MyServlet과 MyFilter를 바인딩하고, ServletContext를 제공하는 메서드를 추가합니다.

마지막으로, GuiceFilter를 이용하여 예외 처리를 적용할 서블릿 컨테이너를 설정해야 합니다. web.xml 파일에 다음과 같이 추가합니다.

```xml
<filter>
    <filter-name>guiceFilter</filter-name>
    <filter-class>com.google.inject.servlet.GuiceFilter</filter-class>
</filter>

<filter-mapping>
    <filter-name>guiceFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

이제 예외 처리가 Guice에 의해 처리되는 상황에서 서블릿을 구현할 수 있습니다.

```java
public class MyServlet extends HttpServlet {
    
    private final ExceptionHandler exceptionHandler;
    
    @Inject
    public MyServlet(ExceptionHandler exceptionHandler) {
        this.exceptionHandler = exceptionHandler;
    }
    
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        try {
            // 예외가 발생할 수 있는 로직
        } catch (Exception e) {
            exceptionHandler.handle(e);
        }
    }
}
```

위의 예제에서 MyServlet은 ExceptionHandler 의존성을 주입받아 예외 처리를 합니다. 캐치된 예외는 exceptionHandler의 handle 메서드로 전달됩니다.

## Guice를 이용한 로깅

Guice를 사용하면 로깅을 간편하게 구현할 수 있습니다. 로깅을 위한 모듈을 만들고, 해당 모듈을 Guice에 바인딩하면 됩니다.

먼저, 로깅을 위한 모듈을 만들어보겠습니다.

```java
public class LoggingModule extends AbstractModule {

    @Override
    protected void configure() {
        bind(LoggerFactory.class).toInstance(LoggerFactory.getILoggerFactory());
        bind(Logger.class).toProvider(LoggerProvider.class).in(Singleton.class);
    }
}
```

이 모듈은 LoggerFactory 인스턴스를 제공하는 로거 팩토리를 바인딩하고, LoggerProvider를 사용하여 Logger를 바인딩합니다. LoggerProvider는 Guice가 주입 요청이 있을 때마다 Logger 인스턴스를 생성합니다.

이제 Logger를 사용하여 로그를 기록할 수 있습니다.

```java
public class MyServlet extends HttpServlet {

    private final Logger logger;

    @Inject
    public MyServlet(Logger logger) {
        this.logger = logger;
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        logger.info("Request received.");

        try {
            // 로깅이 필요한 로직
        } catch (Exception e) {
            logger.error("An error occurred", e);
        }

        logger.debug("Request processed.");
    }
}
```

위의 예제에서 Logger 인스턴스는 Guice에 의해 주입됩니다. 로그 메서드를 호출하여 로그를 기록할 수 있습니다.

이렇게 Guice와 서블릿을 사용하여 예외 처리와 로깅을 구현할 수 있습니다.

## 결론

Guice를 사용하면 예외 처리와 로깅을 간편하게 구현할 수 있습니다. 의존성 주입을 통해 필요한 객체를 쉽게 주입받고, 로그를 기록하는데 필요한 Logger 인스턴스를 쉽게 사용할 수 있습니다.