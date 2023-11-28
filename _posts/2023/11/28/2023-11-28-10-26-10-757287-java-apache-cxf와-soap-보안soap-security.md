---
layout: post
title: "[java] Java Apache CXF와 SOAP 보안(SOAP Security)"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Java Apache CXF는 SOAP(간단한 객체 액세스 프로토콜) 웹 서비스를 개발하기 위한 강력한 도구입니다. 하지만 웹 서비스에서 중요한 데이터를 전송할 때 보안 문제가 발생할 수 있습니다.

이 블로그 포스트에서는 Java Apache CXF를 사용하여 SOAP 보안을 적용하는 방법에 대해 살펴보겠습니다.

## 1. 웹 서비스 보안 구성

SOAP 보안을 적용하기 위해 다음과 같은 설정 작업을 수행해야 합니다.

### 1.1. Maven 종속성 추가

먼저, Maven 종속성을 추가해야 합니다. `pom.xml` 파일에 다음 의존성을 추가하세요.

```xml
<dependency>
    <groupId>org.apache.cxf</groupId>
    <artifactId>cxf-rt-ws-security</artifactId>
    <version>3.1.12</version>
</dependency>
```

### 1.2. 보안 설정 파일 작성

다음으로, 보안 설정 파일을 작성해야 합니다. `cxf.xml` 파일을 생성하고 다음 내용을 추가하세요.

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:sec="http://cxf.apache.org/configuration/security"
    xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
    http://cxf.apache.org/configuration/security http://cxf.apache.org/schemas/configuration/security.xsd">

    <!-- 보안 관련 설정 -->
    <sec:bus>
        <sec:features>
            <sec:wss4jGloballyIgnored />
        </sec:features>
    </sec:bus>

    <!-- 웹 서비스 설정 -->
    <import resource="classpath:META-INF/cxf/cxf.xml" />
    <import resource="classpath:META-INF/cxf/cxf-servlet.xml" />

</beans>
```

### 1.3. 보안 정책 추가

보안 정책을 추가해야 합니다. `cxf-beans.xml` 파일을 생성하고 다음 내용을 추가하세요.

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:http="http://cxf.apache.org/transports/http/configuration"
    xmlns:sec="http://cxf.apache.org/configuration/security"
    xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
    http://cxf.apache.org/configuration/security http://cxf.apache.org/schemas/configuration/security.xsd
    http://cxf.apache.org/transports/http/configuration http://cxf.apache.org/schemas/configuration/http-conf.xsd">

    <sec:tract-of-user>
        <!-- 보안 정책에 따른 사용자 ID와 암호를 추가 -->
        <sec:username>your_username</sec:username>
        <sec:password>your_password</sec:password>
        <!-- 보안에 필요한 토큰 정보 및 암호화 방법을 추가 -->
        <sec:authorize>
            <sec:roles>ROLE_ADMIN</sec:roles>
            <sec:usernameToken>
                <sec:passwordCallBackClass>com.mycompany.PasswordCallbackHandler</sec:passwordCallBackClass>
            </sec:usernameToken>
        </sec:authorize>
    </sec:tract-of-user>

    <!-- 서비스에 보안 요구 사항 추가 -->
    <http:conduit name="{http://apache.org/hello_world_soap_http}HelloWorldPort.http-conduit">
        <http:tlsClientParameters>
            <sec:keyManagers keyPassword="your_keystore_password">
                <sec:keyStore type="JKS" password="your_keystore_password" file="your_keystore_file_path"/>
            </sec:keyManagers>
        </http:tlsClientParameters>
    </http:conduit>

</beans>
```

## 2. 보안 적용하기

보안 설정 파일을 작성한 후, 다음과 같이 Java 코드에서 보안을 적용할 수 있습니다.

### 2.1. 보안 설정 파일 로드

```java
import org.apache.cxf.frontend.ClientProxy;

//...

// 보안 설정 파일 로드
Bus bus = BusFactory.newInstance().createBus();
SpringBusFactory.setDefaultBus(bus);
SpringBusFactory.setThreadDefaultBus(bus);

SpringBusFactory bf = new SpringBusFactory();
URL busFile = MyClass.class.getResource("/cxf.xml");
Bus springBus = bf.createBus(busFile);
BusFactory.setDefaultBus(springBus);

URL beansFile = MyClass.class.getResource("/cxf-beans.xml");
SpringBusFactory.setThreadDefaultBus(springBus);
new ApplicationContextResource(beansFile).getApplicationContext();
```

### 2.2. 웹 서비스에 보안 정책 추가

```java
MyService service = new MyService();
MyWebService port = service.getMyWebServicePort();
BindingProvider bindingProvider = (BindingProvider) port;
bindingProvider.getRequestContext().put(SecurityConstants.CALLBACK_HANDLER, new PasswordCallbackHandler());
```

위의 코드에서 `MyService`는 CXF를 사용하여 생성한 웹 서비스의 클라이언트를 나타냅니다. `getMyWebServicePort()` 메서드를 호출하여 포트를 가져온 다음, `BindingProvider`를 통해 보안 정책을 추가할 수 있습니다.

## 3. 결론

이렇게 Java Apache CXF를 사용하여 SOAP 보안을 적용할 수 있습니다. 보안 설정 파일을 작성하고 Java 코드에서 보안 정책을 추가함으로써 웹 서비스의 중요한 데이터를 안전하게 전송할 수 있습니다.

더 자세한 내용은 [Apache CXF Documentation](https://cxf.apache.org/docs/ws-security.html)을 참조하십시오.