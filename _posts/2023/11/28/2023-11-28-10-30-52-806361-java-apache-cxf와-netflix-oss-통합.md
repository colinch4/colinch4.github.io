---
layout: post
title: "[java] Java Apache CXF와 Netflix OSS 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Java Apache CXF와 Netflix OSS는 각각 웹 서비스 개발 및 분산 시스템 구축을 위한 인기있는 오픈 소스 프레임워크입니다. 이 두 가지 기술을 통합하여 사용하면 더 강력하고 유연한 시스템을 개발할 수 있습니다. 이 글에서는 Java Apache CXF와 Netflix OSS를 통합하는 방법에 대해 알아보겠습니다.

## Apache CXF란?

Apache CXF는 Java로 작성된 오픈 소스 웹 서비스 프레임워크입니다. 이 프레임워크를 사용하면 간단하고 강력한 웹 서비스를 개발할 수 있으며, SOAP 및 RESTful 서비스를 모두 지원합니다. Apache CXF는 WSDL 기반의 웹 서비스 개발에 매우 적합하며, 다양한 프로토콜과 데이터 형식을 지원합니다.

## Netflix OSS란?

Netflix OSS(Open Source Software)는 Netflix에서 개발한 오픈 소스 프로젝트의 집합체입니다. 이 프로젝트들은 클라우드 기반의 분산 시스템을 구축하는 데 도움이 되는 다양한 기술을 제공합니다. Netflix OSS는 높은 가용성, 확장성, 견고성 등의 요구 사항을 충족하는 시스템을 구현할 수 있도록 도와줍니다.

## CXF와 Netflix OSS 통합하기

CXF와 Netflix OSS의 통합을 위해서는 주로 Netflix OSS의 유레카(Eureka) 서비스 디스커버리와 CXF의 주소 라우팅 기능을 연동해야 합니다. 유레카는 마이크로서비스 아키텍처에서 각 서비스 인스턴스의 위치를 추적하고 관리하는 데 사용됩니다. CXF의 주소 라우팅 기능은 클라이언트 요청을 올바른 서비스 인스턴스로 전달하는 데 사용됩니다.

CXF와 Netflix OSS를 통합하는 예제 코드는 다음과 같습니다.

```java
import org.apache.cxf.clustering.FailoverFeature;
import org.apache.cxf.endpoint.Client;
import org.apache.cxf.jaxws.JaxWsProxyFactoryBean;
import org.apache.cxf.transport.http.HTTPConduit;
import com.netflix.client.ClientFactory;
import com.netflix.client.config.ClientConfig;
import com.netflix.discovery.DiscoveryClient;
import com.netflix.discovery.shared.Application;

public class CXFAndNetflixOSSIntegration {
    public static void main(String[] args) {
        // Eureka Client 초기화
        DiscoveryClient discoveryClient = ClientFactory.getDiscoveryClient("default", new ClientConfig());

        // Eureka 서버에서 서비스 정보 조회
        Application application = discoveryClient.getApplication("my-service");

        // CXF 프록시 팩토리 생성
        JaxWsProxyFactoryBean factory = new JaxWsProxyFactoryBean();
        factory.setAddress(application.getInstances().get(0).getHomePageUrl() + "/service");
        factory.setServiceClass(MyService.class);

        // CXF 클라이언트 생성
        MyService service = (MyService) factory.create();

        // CXF 클라이언트에 FailoverFeature 추가
        FailoverFeature failoverFeature = new FailoverFeature();
        failoverFeature.setStrategy(FailoverFeature.FAIL_OVER);

        Client client = ClientProxy.getClient(service);
        client.getEndpoint().getFeatures().add(failoverFeature);

        // CXF 클라이언트에 Netflix OSS HTTPConduit 설정
        HTTPConduit conduit = (HTTPConduit) client.getConduit();
        conduit.getClient().setConnectionTimeout(10000);
        conduit.getClient().setReceiveTimeout(20000);

        // CXF 클라이언트 사용
        System.out.println(service.sayHello());
    }
}
```

위의 코드에서는 먼저 Eureka 클라이언트를 초기화하고, Eureka 서버에서 "my-service"라는 이름의 서비스 정보를 조회합니다. 그런 다음 CXF의 프록시 팩토리를 생성하여 해당 서비스의 첫 번째 인스턴스의 주소를 설정합니다. 마지막으로 CXF 클라이언트에 FailoverFeature를 추가하고, Netflix OSS의 HTTPConduit를 설정하여 CXF 클라이언트를 사용합니다.

## 결론

Java Apache CXF와 Netflix OSS를 통합하여 더 강력하고 유연한 서비스를 개발할 수 있습니다. 이 통합을 통해 웹 서비스 개발과 분산 시스템 구축을 더 쉽게 할 수 있으며, 다양한 기능과 성능을 제공할 수 있습니다. 위에서 제시한 방법을 참고하여 프로젝트에 적용해 보시기 바랍니다.