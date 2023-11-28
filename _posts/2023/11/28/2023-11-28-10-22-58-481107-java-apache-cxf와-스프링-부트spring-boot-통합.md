---
layout: post
title: "[java] Java Apache CXF와 스프링 부트(Spring Boot) 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

이번 글에서는 Java Apache CXF와 스프링 부트(Spring Boot)를 함께 사용하는 방법에 대해 알아보겠습니다.

## Apache CXF란?

Apache CXF는 Java 기반의 웹 서비스 프레임워크입니다. SOAP 및 RESTful 웹 서비스를 구현하기 위한 여러 기능과 도구를 제공합니다. Apache CXF는 WSDL(Web Services Description Language) 파일을 기반으로 웹 서비스를 생성하고 관리할 수 있습니다.

## 스프링 부트란?

스프링 부트는 스프링 프레임워크 기반의 웹 애플리케이션을 빠르고 쉽게 개발할 수 있도록 도와주는 도구입니다. 스프링 부트는 기본적인 설정을 자동으로 처리해주기 때문에 개발자는 별도의 설정 없이도 웹 애플리케이션을 빠르게 구축할 수 있습니다.

## Apache CXF와 스프링 부트 통합하기

Apache CXF와 스프링 부트를 함께 사용하기 위해서는 다음과 같은 단계를 따라야 합니다.

1. Apache CXF와 스프링 부트 의존성 추가하기

첫 번째로, Apache CXF와 스프링 부트를 사용하기 위해서는 Maven 또는 Gradle 프로젝트에 관련 의존성을 추가해야 합니다. 아래는 Maven을 사용하는 경우의 예시입니다.

```xml
<dependency>
    <groupId>org.apache.cxf</groupId>
    <artifactId>cxf-spring-boot-starter-jaxws</artifactId>
    <version>3.4.4</version>
</dependency>
```

2. 웹 서비스 구현하기

두 번째로, 웹 서비스를 구현해야 합니다. Apache CXF를 사용하여 SOAP 웹 서비스를 개발할 수 있습니다. 아래는 간단한 예시입니다.

```java
@WebService
public class HelloWorldService {

    @WebMethod
    public String sayHello(String name) {
        return "Hello, " + name + "!";
    }
}
```

3. 스프링 부트 설정하기

세 번째로, 스프링 부트를 설정해야 합니다. 스프링 부트는 application.properties 또는 application.yml 파일을 사용하여 설정 정보를 관리합니다. 아래는 스프링 부트의 설정 예시입니다.

```properties
# Apache CXF 필터 설정
cxf.servlet.init.order=1

# WSDL 파일 경로 설정
cxf.path=/ws/*

# 서비스 빈 등록
cxf.jaxws.endpoint.publishableEndpoints=/helloworld
```

4. 실행하기

마지막으로, 애플리케이션을 실행하면 Apache CXF와 스프링 부트가 통합된 웹 서비스가 실행됩니다. 아래는 스프링 부트에서 내장 웹 서버를 실행하는 코드입니다.

```java
@SpringBootApplication
@EnableCxf
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

## 결론

이렇게 Apache CXF와 스프링 부트를 함께 사용하여 웹 서비스를 개발할 수 있습니다. Apache CXF는 강력한 웹 서비스 프레임워크이며, 스프링 부트는 개발 생산성을 향상시켜주는 도구입니다. 두 기술을 통합하여 사용하면 효율적이고 견고한 웹 서비스를 구축할 수 있습니다.

참고 문서:
- [Apache CXF 공식 문서](https://cxf.apache.org/)
- [스프링 부트 공식 문서](https://spring.io/projects/spring-boot)