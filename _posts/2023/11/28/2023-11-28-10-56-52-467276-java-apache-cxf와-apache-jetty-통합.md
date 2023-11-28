---
layout: post
title: "[java] Java Apache CXF와 Apache Jetty 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

이번 블로그에서는 Java를 사용하여 Apache CXF와 Apache Jetty를 통합하는 방법에 대해 알아보겠습니다.

## Apache CXF

Apache CXF는 Java 기반의 오픈 소스 웹 서비스 프레임워크입니다. CXF는 JAX-RS(Java API for RESTful Web Services)와 JAX-WS(Java API for XML Web Services)를 지원하여 웹 서비스 개발을 용이하게 해줍니다.

## Apache Jetty

Apache Jetty는 경량화된 웹 애플리케이션 서버입니다. Jetty는 자바로 작성되어있으며, 내장형 서버로서 단독으로 실행될 수 있습니다. Jetty는 많은 기능과 풍부한 확장성을 제공하며, 동시에 가볍고 빠른 성능을 가지고 있습니다.

## CXF와 Jetty 통합하기

CXF와 Jetty를 통합하여 웹 서비스를 제공하는 방법은 매우 간단합니다. 우선, Maven을 사용하여 Java 프로젝트를 생성합니다. 그리고 아래와 같이 필요한 의존성을 추가합니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-frontend-jaxws</artifactId>
        <version>3.4.0</version>
    </dependency>
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-transports-http-jetty</artifactId>
        <version>3.4.0</version>
    </dependency>
</dependencies>
```

의존성을 추가한 뒤, 서비스를 개발하고 Jetty 서버에 배포하기 위한 코드를 작성합니다.

```java
import org.apache.cxf.jaxws.EndpointImpl;
import org.apache.cxf.transport.http.jetty.JettyHTTPServerEngineFactory;

public class MainApp {
    public static void main(String[] args) {
        // CXF Service 객체 생성
        MyService service = new MyService();

        // CXF Endpoint 생성
        EndpointImpl endpoint = new EndpointImpl(service);
        endpoint.publish("/myservice");

        // Jetty 서버 설정
        JettyHTTPServerEngineFactory factory = new JettyHTTPServerEngineFactory();
        factory.setPort(8080);
        factory.setContinuationsEnabled(true);

        // Jetty 서버 시작
        JettyHTTPServerEngine serverEngine = factory.createJettyHTTPServerEngine();
        serverEngine.addServant(endpoint);

        serverEngine.start();
    }
}
```

위의 코드에서 `MyService`는 사용자가 구현한 서비스 클래스를 의미합니다. `EndpointImpl` 객체를 사용하여 CXF 서비스를 생성하고, `publish()` 메서드를 통해 경로를 설정합니다. 그리고 Jetty 서버를 설정하고 시작하는 코드를 작성합니다.

이제 프로젝트를 빌드하고 실행하면, CXF와 Jetty가 통합된 웹 서비스가 실행됩니다.

## 마무리

이번 블로그에서는 Java Apache CXF와 Apache Jetty를 통합하는 방법에 대해 알아보았습니다. CXF와 Jetty는 각자 강력한 기능을 가지고 있지만, 함께 사용하여 웹 서비스를 개발하고 실행하는 것은 매우 쉽고 효율적입니다. 추가적인 설정과 기능 확장은 공식 문서를 참고하시기 바랍니다.

**참고 자료**
- [Apache CXF 공식 문서](https://cxf.apache.org/)
- [Apache Jetty 공식 문서](https://www.eclipse.org/jetty/documentation/current/index.html)