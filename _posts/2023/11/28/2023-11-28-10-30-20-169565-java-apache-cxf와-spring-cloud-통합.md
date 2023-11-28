---
layout: post
title: "[java] Java Apache CXF와 Spring Cloud 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Spring Cloud는 분산 시스템을 빌드하기 위한 서비스 디스커버리, 로드 밸런싱, 서킷 브레이킹 등의 기능을 제공합니다. Apache CXF는 Java 기반의 오픈 소스 웹 서비스 프레임워크로, SOAP 및 RESTful 웹 서비스를 쉽게 개발할 수 있도록 도와줍니다. 이 두 가지 기술을 함께 사용하면 효과적인 분산 시스템을 구축할 수 있습니다.

## Apache CXF와 Spring Boot 프로젝트 설정

먼저, Apache CXF와 Spring Boot 프로젝트를 설정해야합니다. 

```java
@Configuration
public class CxfConfig {
    
    @Autowired
    private Bus bus;

    @Autowired
    private HelloWorldService helloWorldService;

    @Bean
    public Endpoint endpoint() {
        EndpointImpl endpoint = new EndpointImpl(bus, helloWorldService);
        endpoint.publish("/helloWorld");
        return endpoint;
    }
}
```

위의 코드는 Apache CXF의 설정과 HelloWorldService를 Spring Boot에 연결하기 위한 설정입니다. `/helloWorld` 경로로 HelloWorldService가 퍼블리시되도록 설정되어 있습니다.

## Spring Cloud와 Apache CXF 통합

Spring Cloud와 Apache CXF를 통합하기 위해 다음과 같은 단계를 따를 수 있습니다.

1. Eureka 서비스 디스커버리 클라이언트 설정

```java
@SpringBootApplication
@EnableDiscoveryClient
public class MyApplication {
   
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

위의 코드는 Spring Cloud Eureka 클라이언트를 활성화하는 설정입니다. 

2. Apache CXF 서비스 등록

```java
@Component
public class CxfServiceRegistration {

    @Autowired
    private DiscoveryClient discoveryClient;

    @Value("${spring.application.name}")
    private String applicationName;

    @PostConstruct
    public void registerService() {
        List<ServiceInstance> instances = discoveryClient.getInstances(applicationName);
        if (!instances.isEmpty()) {
            ServiceInstance instance = instances.get(0);
            String url = instance.getUri().toString() + "/helloWorld";
            JaxWsServerFactoryBean factory = new JaxWsServerFactoryBean();
            factory.setAddress(url);
            factory.setServiceClass(HelloWorldService.class);
            factory.setServiceBean(helloWorldService);
            factory.create();
        }
    }
}
```

위의 코드는 Apache CXF 서비스를 Eureka 서버에 등록하는 설정입니다. Eureka 클라이언트를 사용하여 HelloWorldService를 등록하고, 인스턴스의 URL을 가져와 JAX-WS 서버 팩토리 빈을 생성합니다.

3. Apache CXF 서비스 호출

```java
@RestController
public class MyController {

    @Autowired
    private DiscoveryClient discoveryClient;

    @RequestMapping("/helloWorld")
    public String helloWorld() {
        List<ServiceInstance> instances = discoveryClient.getInstances("my-service");
        if (!instances.isEmpty()) {
            ServiceInstance instance = instances.get(0);
            String url = instance.getUri().toString() + "/helloWorld";
            JaxWsProxyFactoryBean factory = new JaxWsProxyFactoryBean();
            factory.setAddress(url);
            factory.setServiceClass(HelloWorldService.class);
            HelloWorldService helloWorldService = (HelloWorldService) factory.create();
            return helloWorldService.sayHello();
        }
        return "Service not available";
    }
}
```

위의 코드는 Spring Boot 컨트롤러입니다. `"/helloWorld"` 경로로 요청이 들어오면 Eureka 서버에서 HelloWorldService 인스턴스 URL을 가져와 JAX-WS 프록시 팩토리 빈을 생성하고, `sayHello()` 메소드를 호출하여 결과를 반환합니다.

## 결론

이렇게 Java Apache CXF와 Spring Cloud를 통합하여 분산 시스템을 구축할 수 있습니다. Apache CXF와 Spring Cloud의 강력한 기능을 함께 사용하여 확장 가능하고 효율적인 분산 시스템을 구축할 수 있습니다.