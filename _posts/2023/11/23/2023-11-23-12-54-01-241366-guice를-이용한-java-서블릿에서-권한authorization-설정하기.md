---
layout: post
title: "[java] Guice를 이용한 Java 서블릿에서 권한(Authorization) 설정하기"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Guice는 Java 언어를 위한 경량의 의존성 주입(Dependency Injection) 프레임워크입니다. 이 프레임워크를 사용하여 Java 서블릿에서 권한(Authorization)을 설정하는 방법을 소개하겠습니다.

## Guice와 Servlet 모듈 추가하기
먼저 프로젝트에 Guice와 Servlet 모듈을 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음 의존성을 추가합니다.

```xml
<dependencies>
    <dependency>
        <groupId>com.google.inject</groupId>
        <artifactId>guice</artifactId>
        <version>4.2.3</version>
    </dependency>
    <dependency>
        <groupId>com.google.inject.extensions</groupId>
        <artifactId>guice-servlet</artifactId>
        <version>4.2.3</version>
    </dependency>
</dependencies>
```

Gradle을 사용하는 경우, `build.gradle` 파일에 의존성을 추가합니다.

```groovy
dependencies {
    implementation 'com.google.inject:guice:4.2.3'
    implementation 'com.google.inject.extensions:guice-servlet:4.2.3'
}
```

## 권한 설정을 위한 모듈 생성하기
Guice를 사용하여 권한을 설정하기 위한 모듈을 생성합니다. 아래는 `AuthorizationModule`이라는 이름의 모듈 예시입니다.

```java
import com.google.inject.servlet.ServletModule;

public class AuthorizationModule extends ServletModule {

    @Override
    protected void configureServlets() {
        serve("/auth/*").with(AuthorizationServlet.class);
    }
}
```

`AuthorizationModule`은 `ServletModule`을 상속받아 구현하며, `configureServlets()` 메소드를 오버라이딩하여 서블릿 매핑을 설정합니다. 위 예시에서는 `/auth/*` 경로로 들어오는 요청을 `AuthorizationServlet`으로 처리하도록 설정하였습니다.

## 권한 처리를 위한 서블릿 구현하기
`AuthorizationServlet`은 권한 처리를 위해 구현한 서블릿입니다. 다음은 간단한 예시입니다.

```java
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class AuthorizationServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String userId = req.getParameter("userId");
        
        // TODO: 권한 체크 로직 구현
        
        resp.getWriter().println("Authorization success!");
    }
}
```

`AuthorizationServlet`은 `HttpServlet`을 상속받아 구현되었습니다. `doGet()` 메소드를 오버라이딩하여 GET 요청을 처리하며, 예시에서는 `userId` 파라미터를 받아서 권한 체크 로직을 구현하지 않고 간단히 "Authorization success!"를 출력하는 예시입니다.

## Guice에 모듈 등록하기
마지막으로 `AuthorizationModule`을 Guice에 등록하여 사용합니다. 예를 들어, `Main` 클래스에서 Guice를 초기화하고 모듈을 등록하는 방법은 다음과 같습니다.

```java
import com.google.inject.Guice;
import com.google.inject.Injector;

public class Main {

    public static void main(String[] args) {
        Injector injector = Guice.createInjector(new AuthorizationModule());
    }
}
```

위 예제에서는 `AuthorizationModule`을 `Guice.createInjector()` 메소드의 매개변수로 전달하여 Guice를 초기화합니다.

## 결론
Guice를 이용하여 Java 서블릿에서 권한(Authorization)을 설정하는 방법을 알아보았습니다. Guice를 사용하면 유연하고 확장 가능한 서블릿 애플리케이션을 만들 수 있으며, 권한 처리와 같은 공통적인 기능을 모듈화할 수 있습니다.

## 참고 자료
- [Guice 공식 웹사이트](https://github.com/google/guice)
- [Guice - 구글 개발자 가이드](https://github.com/google/guice/wiki/Motivation)
- [Servlet 공식 문서](https://jcp.org/aboutJava/communityprocess/final/jsr369/index.html)