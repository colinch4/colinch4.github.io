---
layout: post
title: "[java] Java Apache CXF와 Apache Camel 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

## 서론

이번 포스트에서는 Java에서 Apache CXF와 Apache Camel을 이용하여 통합 서비스를 구축하는 방법에 대해 알아보겠습니다. 

## Apache CXF 소개

Apache CXF는 Java 기반의 웹 서비스 프레임워크로, SOAP 및 RESTful 웹 서비스를 구축할 수 있습니다. CXF는 표준 기반의 웹 서비스 스택인 JAX-WS 및 JAX-RS를 구현하고 있어 개발자가 쉽게 웹 서비스를 작성할 수 있습니다.

## Apache Camel 소개

Apache Camel은 EIP(Enterprise Integration Patterns)을 구현한 오픈소스 통합 프레임워크입니다. Camel은 다양한 프로토콜과 메시징 시스템을 지원하며, 간단한 DSL(Domain Specific Language)을 이용하여 통합 라우팅을 작성할 수 있습니다.

## CXF와 Camel 통합

CXF와 Camel을 함께 사용하면 CXF의 웹 서비스를 Camel의 라우팅과 함께 사용할 수 있습니다. Camel은 CXF에서 받은 요청을 수신하여 다른 서비스로 라우팅하거나 CXF에서 보낸 응답을 가로챌 수 있습니다.

아래는 CXF와 Camel을 통합하는 간단한 예제 코드입니다.

```java
import org.apache.camel.CamelContext;
import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.impl.DefaultCamelContext;
import org.apache.cxf.endpoint.Server;
import org.apache.cxf.jaxws.JaxWsServerFactoryBean;

public class CXFCamelIntegrationExample {

    public static void main(String[] args) throws Exception {
        // CamelContext 생성
        CamelContext camelContext = new DefaultCamelContext();
        // CXF 서버 생성
        JaxWsServerFactoryBean cxfServerFactoryBean = new JaxWsServerFactoryBean();
        cxfServerFactoryBean.setServiceClass(MyWebService.class);
        cxfServerFactoryBean.setAddress("http://localhost:8080/MyWebService");
        // Camel 라우트 생성
        camelContext.addRoutes(new RouteBuilder() {
            public void configure() {
                from("cxfbean:MyWebService").to("direct:processRequest");
                from("direct:processRequest").log("Processing request: ${body}");
            }
        });
        // CamelContext 시작
        camelContext.start();
        // CXF 서버 시작
        Server cxfServer = cxfServerFactoryBean.create();
        cxfServer.start();
        // 애플리케이션 종료 시 CamelContext 및 CXF 서버 종료
        Runtime.getRuntime().addShutdownHook(new Thread() {
            public void run() {
                try {
                    cxfServer.stop();
                    camelContext.stop();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        // 애플리케이션 실행 유지
        Thread.sleep(Long.MAX_VALUE);
    }

    public interface MyWebService {
        String processRequest(String request);
    }
}
```

위의 예제 코드에서는 CXF를 사용하여 MyWebService를 정의하고, Camel을 통해 받은 요청을 `direct:processRequest`라우트로 보내고 요청 내용을 로그에 출력하는 간단한 예제입니다. 

## 결론

이번 포스트에서는 Java에서 Apache CXF와 Apache Camel을 통합하여 사용하는 방법에 대해 알아보았습니다. CXF와 Camel을 함께 사용하면 웹 서비스를 간단하게 구축하고 유연한 라우팅을 적용할 수 있습니다. 더 많은 기능과 사용 방법을 알고 싶다면 Apache CXF 및 Apache Camel 공식 문서를 참고하세요.