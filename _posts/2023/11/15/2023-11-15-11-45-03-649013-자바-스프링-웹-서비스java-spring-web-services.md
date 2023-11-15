---
layout: post
title: "[java] 자바 스프링 웹 서비스(Java Spring Web Services)"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

이번 블로그에서는 자바 스프링(Spring)을 사용하여 웹 서비스를 개발하는 방법에 대해 알아보겠습니다. 자바 스프링은 많은 기업 및 개발자들이 선호하는 프레임워크 중 하나로, 웹 애플리케이션 개발에 높은 생산성과 유연성을 제공합니다.

## 1. 스프링 프레임워크(Spring Framework)란?

스프링 프레임워크는 자바 애플리케이션 개발을 위한 오픈 소스 프레임워크로, 애플리케이션의 느슨한 결합과 테스트 가능성, 그리고 확장성을 지원합니다. 스프링은 다양한 모듈로 구성되어 있으며, 웹 애플리케이션 개발을 위한 스프링 MVC, 데이터 액세스를 위한 스프링 JDBC, 객체 관계 매핑(O/R Mapping)을 위한 스프링 ORM 등 다양한 기능을 제공합니다.

## 2. 스프링으로 웹 서비스 개발하기

스프링을 사용하여 웹 서비스를 개발하는 방법은 여러 가지가 있지만, 여기에서는 스프링 MVC를 사용하는 방법에 대해 알아보겠습니다. 스프링 MVC는 모델-뷰-컨트롤러(Model-View-Controller) 패턴을 기반으로 한 웹 애플리케이션 개발을 위한 프레임워크로, 요청을 받아 처리하는 컨트롤러, 비즈니스 로직을 처리하는 모델, 그리고 결과를 표현하는 뷰 등이 각각 역할을 수행합니다.

### 2.1 프로젝트 생성 및 의존성 설정

먼저, 스프링 MVC 프로젝트를 생성하고 의존성을 설정해야 합니다. 이를 위해 Maven이나 Gradle과 같은 빌드 도구를 사용할 수 있습니다. 아래는 Maven을 사용하여 스프링 MVC 프로젝트를 생성하는 예시입니다.

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

### 2.2 컨트롤러 작성

다음으로, 웹 요청을 처리하는 컨트롤러를 작성해야 합니다. 스프링 MVC에서는 `@Controller` 어노테이션을 사용하여 컨트롤러를 정의할 수 있습니다. 아래는 간단한 예시입니다.

```java
@Controller
public class MyController {

    @GetMapping("/hello")
    public String hello(Model model) {
        model.addAttribute("message", "Hello, Spring MVC!");
        return "hello";
    }
}
```

### 2.3 뷰 작성

마지막으로, 결과를 표현하는 뷰를 작성해야 합니다. 스프링 MVC는 다양한 뷰 템플릿을 지원하며, 여기에서는 Thymeleaf를 사용하는 예시를 보여드리겠습니다. `hello.html` 파일을 생성하고 아래와 같이 작성합니다.

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<body>
    <h1 th:text="${message}"></h1>
</body>
</html>
```

### 2.4 실행 및 확인

위의 과정을 마친 후, 애플리케이션을 실행하고 웹 브라우저에서 http://localhost:8080/hello에 접속해보세요. "Hello, Spring MVC!"라는 메시지가 출력되는 것을 확인할 수 있습니다.

## 3. 정리

이번 글에서는 자바 스프링을 사용하여 웹 서비스를 개발하는 방법에 대해 알아보았습니다. 스프링의 다양한 기능과 웹 개발에 적합한 스프링 MVC를 통해 효율적이고 유연한 웹 서비스를 개발할 수 있습니다. 스프링 프레임워크에 대해 더 알고 싶다면 공식 문서를 참고해보세요.

- [Spring Framework 공식 문서](https://docs.spring.io/spring-framework/docs/current/reference/html/)
- [Spring MVC 공식 문서](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html)