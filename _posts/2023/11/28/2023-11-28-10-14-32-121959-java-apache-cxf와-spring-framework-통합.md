---
layout: post
title: "[java] Java Apache CXF와 Spring Framework 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Apache CXF는 Java 기반의 웹 서비스 프레임워크로, SOAP 및 RESTful 웹 서비스를 개발하고 배포할 수 있는 강력한 도구입니다. Spring Framework는 Java 기반의 애플리케이션 개발을 위한 유명한 프레임워크로, 의존성 주입 및 애플리케이션 컨텍스트 관리 등을 지원합니다.

이 문서에서는 Apache CXF와 Spring Framework를 함께 사용하여 웹 서비스를 구현하는 방법에 대해 알아보겠습니다.

## 1. Apache CXF와 Spring Framework 연동 설정

먼저, 프로젝트의 의존성 관리 도구인 Maven을 사용해 필요한 라이브러리를 추가합니다. 아래의 의존성을 `pom.xml` 파일에 추가합니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-frontend-jaxws</artifactId>
        <version>{apache_cxf_version}</version>
    </dependency>
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-transports-http</artifactId>
        <version>{apache_cxf_version}</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-web</artifactId>
        <version>{spring_version}</version>
    </dependency>
</dependencies>
```

`{apache_cxf_version}` 및 `{spring_version}`를 사용하고자 하는 버전으로 각각 변경합니다.

## 2. Apache CXF 웹 서비스 개발

먼저, Apache CXF를 사용하여 간단한 웹 서비스를 개발해보겠습니다. `CalculatorService`라는 기본적인 사칙연산을 수행하는 웹 서비스를 만들어보겠습니다.

```java
package com.example;

import javax.jws.WebParam;
import javax.jws.WebResult;
import javax.jws.WebService;

@WebService
public interface CalculatorService {
  
    @WebResult(name = "result")
    int add(@WebParam(name = "x") int x, @WebParam(name = "y") int y);
  
    @WebResult(name = "result")
    int subtract(@WebParam(name = "x") int x, @WebParam(name = "y") int y);
  
    @WebResult(name = "result")
    int multiply(@WebParam(name = "x") int x, @WebParam(name = "y") int y);
  
    @WebResult(name = "result")
    int divide(@WebParam(name = "x") int x, @WebParam(name = "y") int y);
}
```

위의 코드에서 `@WebService` 어노테이션을 사용하여 `CalculatorService`를 웹 서비스로 지정하고, 사칙연산 메서드를 추가합니다.

## 3. Spring Framework 설정

Spring Framework를 사용하여 개발한 웹 서비스를 구동하기 위해, Spring 설정 파일을 작성해야 합니다. 아래의 내용으로 `application-context.xml` 파일을 생성합니다.

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
       
    <bean id="calculatorService" class="com.example.CalculatorServiceImpl"/>
    <jaxws:endpoint
            id="calculatorServiceEndpoint"
            implementor="#calculatorService"
            address="/calculatorService"/>
</beans>
```

위의 설정 파일에서 `calculatorService` 빈을 생성하고 `CalculatorServiceImpl` 클래스를 구현체로 정의합니다. 또한, `jaxws:endpoint`를 사용하여 웹 서비스의 엔드포인트를 설정합니다.

## 4. 웹 서비스 배포

웹 서비스를 배포하기 위해 스프링 라이프사이클 빈이 시작될 때 Apache CXF의 `JaxWsServerFactoryBean`을 사용해 웹 서비스를 등록하도록 설정합니다. 이를 위해 프로젝트의 메인 클래스에 다음과 같은 코드를 추가합니다.

```java
package com.example;

import org.apache.cxf.jaxws.JaxWsServerFactoryBean;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainApplication {

    public static void main(String[] args) {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("application-context.xml");
        CalculatorService calculatorService = context.getBean("calculatorService", CalculatorService.class);

        JaxWsServerFactoryBean jaxWsServerFactoryBean = new JaxWsServerFactoryBean();
        jaxWsServerFactoryBean.setServiceClass(CalculatorService.class);
        jaxWsServerFactoryBean.setAddress("/");

        jaxWsServerFactoryBean.setServiceBean(calculatorService);
        jaxWsServerFactoryBean.create();

        System.out.println("Web service is running...");
    }
}
```

위의 코드에서 `ClassPathXmlApplicationContext`를 사용하여 Spring 컨텍스트를 생성하고 `CalculatorService` 빈을 가져옵니다. 그런 다음, `JaxWsServerFactoryBean`을 사용하여 웹 서비스를 생성하고 등록합니다.

## 5. 웹 서비스 테스트

웹 서비스를 테스트하기 위해, `http://localhost:8080/calculatorService?wsdl` 주소로 접속하여 WSDL 파일을 확인할 수 있습니다. 또한, 다음과 같은 SOAP 요청을 보내 결과를 확인할 수도 있습니다.

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservices.example.com/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:add>
         <x>10</x>
         <y>5</y>
      </web:add>
   </soapenv:Body>
</soapenv:Envelope>
```

이 문서에서는 Apache CXF와 Spring Framework를 사용하여 Java 기반의 웹 서비스를 개발하고 배포하는 방법에 대해 알아보았습니다. 이를 통해 웹 서비스를 손쉽게 개발할 수 있고, Spring Framework의 강력한 기능을 활용하여 자바 애플리케이션을 통합할 수 있습니다.

[Apache CXF 공식 사이트]: http://cxf.apache.org/
[Spring Framework 공식 사이트]: https://spring.io/