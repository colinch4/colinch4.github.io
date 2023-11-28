---
layout: post
title: "[java] Tomcat과 Spring Framework의 통합 사용 방법"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Spring Framework는 자바 기반의 오픈 소스 애플리케이션 프레임워크로, 웹 애플리케이션 개발에 널리 사용됩니다. 이에 따라 Tomcat과 Spring Framework의 통합은 많은 개발자들에게 중요한 주제입니다. 이번 블로그에서는 Tomcat과 Spring Framework를 함께 사용하는 방법에 대해 알아보겠습니다.

## 1. Spring MVC 설정

먼저, Spring Framework의 Web 모듈인 Spring MVC를 사용하기 위해 프로젝트에 해당 모듈을 추가해야 합니다. 

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.2.8.RELEASE</version>
</dependency>
```

위와 같이 Maven 또는 Gradle을 통해 의존성을 추가할 수 있습니다. 이렇게 하면 Spring MVC의 필수 라이브러리가 프로젝트에 추가됩니다.

## 2. DispatcherServlet 설정

Spring MVC는 DispatcherServlet을 통해 클라이언트의 요청을 처리합니다. 이를 위해 web.xml 파일에 DispatcherServlet을 등록해야 합니다.

```xml
<web-app>
    <servlet>
        <servlet-name>dispatcher</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>/WEB-INF/spring-servlet.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>
    
    <servlet-mapping>
        <servlet-name>dispatcher</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
</web-app>
```

위의 예시는 DispatcherServlet을 "/WEB-INF/spring-servlet.xml" 파일을 기반으로 등록한 것입니다. 실제 파일 경로는 프로젝트 구조에 맞게 수정해야 합니다.

## 3. 스프링 설정 파일

DispatcherServlet은 스프링 설정 파일을 필요로 합니다. 이 설정 파일에서 Spring Bean을 정의하고, 요청을 처리할 컨트롤러를 매핑하는 작업을 수행합니다.

```xml
<!-- spring-servlet.xml -->
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/mvc http://www.springframework.org/schema/mvc/spring-mvc.xsd">
        
    <mvc:annotation-driven/>
    
    <!-- 컨트롤러 패키지를 스캔하여 자동으로 빈을 등록합니다 -->
    <context:component-scan base-package="com.example.controller"/>
    
    <!-- View Resolver 설정 -->
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/views/"/>
        <property name="suffix" value=".jsp"/>
    </bean>
</beans>
```

위의 예시는 스프링 설정 파일의 일부입니다. 여기서는 `<mvc:annotation-driven>`을 통해 애노테이션 기반의 요청 처리를 활성화하고, 컨트롤러 패키지를 스캔하여 자동으로 빈을 등록하는 작업을 수행하고 있습니다.

## 4. 컨트롤러 작성

스프링 MVC에서는 컨트롤러 클래스를 작성하여 클라이언트의 요청을 처리합니다.

```java
@Controller
public class HomeController {
    
    @RequestMapping("/")
    public String home() {
        return "home";
    }
    
    @RequestMapping("/hello")
    public String hello(Model model) {
        model.addAttribute("message", "Hello, world!");
        return "hello";
    }
}
```

위의 예시는 HomeController라는 컨트롤러 클래스를 정의한 것입니다. `@Controller` 애노테이션을 통해 해당 클래스가 컨트롤러임을 명시하고, `@RequestMapping` 애노테이션을 통해 요청 URL과 매핑되는 메소드를 정의하고 있습니다.

## 5. JSP View 작성

컨트롤러에서 반환된 뷰 이름에 따라 실제로 보여질 JSP 파일을 작성해야 합니다.

```jsp
<!-- home.jsp -->
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the home page!</h1>
</body>
</html>

<!-- hello.jsp -->
<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>${message}</h1>
</body>
</html>
```

위의 예시는 home.jsp와 hello.jsp라는 두 개의 JSP 파일을 작성한 것입니다. 컨트롤러에서 `return "home"`과 `return "hello"`와 같은 뷰 이름을 반환하면 해당 JSP 파일이 클라이언트에게 보여집니다.

Tomcat과 Spring Framework의 통합 사용 방법을 알아보았습니다. 이를 통해 효과적인 웹 애플리케이션 개발을 진행할 수 있습니다. 더 자세한 내용은 [공식 Spring Framework 문서](https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/web.html)를 참조하시기 바랍니다.