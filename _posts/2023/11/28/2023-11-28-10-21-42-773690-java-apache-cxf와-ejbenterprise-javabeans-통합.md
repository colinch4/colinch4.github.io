---
layout: post
title: "[java] Java Apache CXF와 EJB(Enterprise JavaBeans) 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

## 소개
Apache CXF는 Java 프로그래밍 언어를 사용하여 웹 서비스를 구축하고 통합하기 위한 프레임워크입니다. EJB(Enterprise JavaBeans)는 Java Enterprise Edition(Java EE)의 일부로서, 분산 애플리케이션을 개발하기 위한 컴포넌트 모델입니다. 이 두 기술은 많은 Java 기업 애플리케이션에서 함께 사용될 수 있습니다. 이 글에서는 Java Apache CXF와 EJB를 통합하는 방법에 대해 알아보겠습니다.

## CXF 및 EJB 의존성 추가하기
CXF와 EJB를 통합하려면 먼저 Maven이나 Gradle과 같은 빌드 도구를 사용하여 프로젝트에 CXF 및 EJB 의존성을 추가해야 합니다. 다음은 Maven을 사용하는 경우 `pom.xml` 파일에 추가할 의존성의 예입니다.

```xml
<dependencies>
    <!-- CXF dependencies -->
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-frontend-jaxws</artifactId>
        <version>3.3.7</version>
    </dependency>
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-transports-http</artifactId>
        <version>3.3.7</version>
    </dependency>
    
    <!-- EJB dependency -->
    <dependency>
        <groupId>javax.ejb</groupId>
        <artifactId>ejb-api</artifactId>
        <version>3.2</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

위의 예제에서는 Apache CXF의 JAX-WS 및 HTTP 전송 모듈에 대한 의존성을 추가하고, EJB의 API를 추가하였습니다.

## CXF로 EJB 서비스 노출하기
CXF를 사용하여 EJB 서비스를 웹 서비스로 노출시키기 위해, CXF의 JAX-WS 기능을 사용할 수 있습니다. 먼저, EJB에 `@WebService` 애너테이션을 추가하여 웹 서비스로 노출할 클래스를 표시해야 합니다.

```java
import javax.ejb.Stateless;
import javax.jws.WebMethod;
import javax.jws.WebService;

@Stateless
@WebService
public class MyEjbService {
    
    @WebMethod
    public String sayHello(String name) {
        return "Hello, " + name + "!";
    }
}
```

위의 예제에서는 `MyEjbService` 클래스에 `@WebService` 애너테이션을 추가하여 이 클래스를 웹 서비스로 표시하였습니다. `@WebMethod` 애너테이션은 웹 서비스에서 노출시킬 메서드를 표시하는데 사용됩니다.

## CXF 서버 구성하기
CXF 서버를 구성하여 EJB 서비스를 배치하고 실행할 수 있습니다. 다음은 CXF 서버 구성 파일의 예입니다.

```java
import javax.xml.ws.Endpoint;
import org.apache.cxf.jaxws.JaxWsServerFactoryBean;

public class CxfServer {
    
    public static void main(String[] args) {
        // EJB 서비스 객체 생성
        MyEjbService ejbService = new MyEjbService();
        
        // CXF 서버 팩토리 빈 생성
        JaxWsServerFactoryBean serverFactory = new JaxWsServerFactoryBean();
        serverFactory.setAddress("http://localhost:8080/myEjbService");
        serverFactory.setServiceBean(ejbService);
        
        // CXF 서버 시작
        Endpoint endpoint = serverFactory.create();
        endpoint.publish();
        
        System.out.println("CXF Server started");
    }
}
```

위의 예제에서는 `JaxWsServerFactoryBean`을 사용하여 CXF 서버를 구성하고, EJB 서비스 객체를 서버에 등록합니다. `setAddress` 메서드를 사용하여 서비스의 엔드포인트 URL을 설정할 수 있습니다. `create` 메서드를 호출하여 서버를 시작하고, `publish` 메서드를 호출하여 서비스를 노출시킵니다.

## CXF 클라이언트 생성하기
CXF를 사용하여 EJB 서비스에 접근하는 클라이언트를 생성할 수 있습니다. 다음은 CXF 클라이언트의 예입니다.

```java
import org.apache.cxf.jaxws.JaxWsProxyFactoryBean;

public class CxfClient {

    public static void main(String[] args) {
        // CXF 클라이언트 팩토리 빈 생성
        JaxWsProxyFactoryBean clientFactory = new JaxWsProxyFactoryBean();
        clientFactory.setAddress("http://localhost:8080/myEjbService");
        clientFactory.setServiceClass(MyEjbService.class);
        
        // CXF 클라이언트 생성
        MyEjbService ejbService = (MyEjbService) clientFactory.create();
        
        // EJB 메서드 호출
        String response = ejbService.sayHello("John");
        System.out.println(response);
    }
}
```

위의 예제에서는 `JaxWsProxyFactoryBean`을 사용하여 CXF 클라이언트를 생성합니다. `setAddress` 메서드를 사용하여 서비스의 엔드포인트 URL을 설정하고, `setServiceClass` 메서드를 사용하여 서비스 인터페이스를 지정합니다. `create` 메서드를 호출하여 클라이언트를 생성하고, 서비스의 메서드를 호출하여 결과를 받을 수 있습니다.

## 결론
이 글에서는 Java Apache CXF와 EJB를 통합하는 방법에 대해 알아보았습니다. Apache CXF를 사용하여 EJB 서비스를 웹 서비스로 노출시키고, CXF 클라이언트를 사용하여 EJB 서비스에 접근하는 방법을 다루었습니다. 이를 통해 Java 기업 애플리케이션에서 CXF와 EJB를 함께 사용할 수 있습니다.

## 참고 자료
- [Apache CXF Documentation](https://cxf.apache.org/docs/)
- [Java EE Tutorials - Enterprise JavaBeans](https://docs.oracle.com/javaee/7/tutorial/ejb-intro.htm)