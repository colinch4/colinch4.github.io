---
layout: post
title: "[java] Java Apache CXF와 JAX-RS(Java API for RESTful Web Services)"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Java Apache CXF와 JAX-RS는 자바 언어를 사용하여 RESTful 웹 서비스를 개발하는 데 도움을 주는 프레임워크입니다. 이 프레임워크는 간편하게 RESTful 웹 서비스를 구축하고 통합하는 데 사용됩니다. 

## Apache CXF

Apache CXF는 다양한 웹 서비스 표준과 프로토콜을 지원하는 오픈 소스 웹 서비스 프레임워크입니다. CXF는 서비스 개발자와 소비자를 더 쉽고 간편하게 연결하여 웹 서비스 개발 및 배포를 지원합니다. 

### 주요 기능

- JAX-RS와 JAX-WS 지원
- 다양한 웹 서비스 표준 및 프로토콜 지원 (SOAP, REST, JSON, XML 등)
- 다양한 서비스 포맷 및 프로토콜 변환
- 보안 및 인증 기능 제공
- 클라이언트와 서비스 간 상호 작용을 간편하게 만들어줌

## JAX-RS (Java API for RESTful Web Services)

JAX-RS는 Java 언어의 RESTful 웹 서비스를 개발하기 위한 API입니다. 이 API는 HTTP 프로토콜을 사용하는 RESTful 웹 애플리케이션을 구축하는 데 사용됩니다. 

### 주요 기능

- 자원의 생성, 업데이트, 삭제 및 조회를 위한 HTTP 메서드 지원 (GET, POST, PUT, DELETE)
- 자원 경로 지정을 위한 어노테이션 지원
- 다양한 데이터 포맷 지원 (JSON, XML 등)
- 인터셉터 및 필터 기능 제공
- 서비스 프로바이더와의 통합을 간편하게 지원

## Apache CXF와 JAX-RS 함께 사용하기

Apache CXF와 JAX-RS를 함께 사용하면 강력한 RESTful 웹 서비스를 구축하고 통합할 수 있습니다. Apache CXF를 사용하여 서버 측 서비스를 개발하고, JAX-RS를 사용하여 클라이언트 측에서 해당 서비스와 상호 작용할 수 있습니다.

아래는 Apache CXF와 JAX-RS를 함께 사용하는 간단한 예제 코드입니다.

```java
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import org.apache.cxf.jaxrs.JAXRSServerFactoryBean;

@Path("/hello")
public class HelloService {

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String sayHello() {
        return "Hello, world!";
    }

    public static void main(String[] args) {
        JAXRSServerFactoryBean sf = new JAXRSServerFactoryBean();
        sf.setResourceClasses(HelloService.class);
        sf.setAddress("http://localhost:8080/");
        sf.create();
    }
}
```

이 코드는 간단한 "Hello, world!" 문자열을 반환하는 RESTful 웹 서비스를 개발하는 예제입니다. 이 예제에서는 Apache CXF의 `JAXRSServerFactoryBean`을 사용하여 서비스를 생성하고, `@Path`와 `@GET` 어노테이션을 사용하여 자원 경로와 HTTP 메서드를 지정합니다.

## 참고 자료

- Apache CXF 공식 홈페이지: [http://cxf.apache.org](http://cxf.apache.org)
- JAX-RS 스펙 문서: [https://docs.oracle.com/javaee/7/api/javax/ws/rs/package-summary.html](https://docs.oracle.com/javaee/7/api/javax/ws/rs/package-summary.html)