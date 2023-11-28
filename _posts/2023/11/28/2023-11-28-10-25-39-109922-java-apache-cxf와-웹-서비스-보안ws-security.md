---
layout: post
title: "[java] Java Apache CXF와 웹 서비스 보안(WS-Security)"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

웹 서비스를 개발할 때, 보안은 매우 중요한 요소입니다. Apache CXF는 Java 기반의 오픈 소스 프레임워크로, 웹 서비스와 관련된 다양한 보안 기능을 제공합니다. 이 중에서도 WS-Security는 웹 서비스 보안을 구현하는 데 사용되는 표준이며, CXF에서 이를 지원하고 있습니다.

이번 포스트에서는 Java Apache CXF를 사용하여 웹 서비스에 WS-Security를 적용하는 방법에 대해 알아보겠습니다.

## 1. Maven 의존성 추가

먼저, Maven을 사용하여 Apache CXF를 프로젝트에 추가해야 합니다. `pom.xml` 파일에 다음 의존성을 추가합니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-ws-security</artifactId>
        <version>3.3.6</version>
    </dependency>
</dependencies>
```

## 2. 보안 구성 설정

웹 서비스의 보안 구성은 `cxf.xml` 파일을 통해 설정할 수 있습니다. 아래는 간단한 예제입니다.

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:sec="http://cxf.apache.org/configuration/security"
       xmlns:http="http://cxf.apache.org/transports/http/configuration"
       xmlns:cxf="http://cxf.apache.org/core"
       xmlns:wssec="http://cxf.apache.org/configuration/security"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
       http://cxf.apache.org/configuration/security http://cxf.apache.org/schemas/configuration/security.xsd
       http://cxf.apache.org/transports/http/configuration http://cxf.apache.org/schemas/configuration/http-conf.xsd
       http://cxf.apache.org/core http://cxf.apache.org/schemas/core.xsd">

    <!-- WS-Security 설정 -->
    <wssec:WSSConfig>
        <wssec:config>
            <wssec:security>
                <wssec:usernameToken name="MyUsernameToken"
                                    created="false" nonce="false"/>
            </wssec:security>
        </wssec:config>
    </wssec:WSSConfig>

    <!-- 웹 서비스 빈 등록 -->
    <bean id="helloService" class="com.example.HelloServiceImpl"/>

    <!-- CXF 서블릿 등록 -->
    <bean id="cxfServlet" class="org.apache.cxf.transport.servlet.CXFServlet">
        <property name="bus">
            <bean class="org.apache.cxf.bus.spring.SpringBus"/>
        </property>
    </bean>

    <!-- Spring MVC 디스패처 서블릿 등록 -->
    <bean id="dispatcherServlet" class="org.springframework.web.servlet.DispatcherServlet">
        <property name="contextConfigLocation" value="classpath:applicationContext.xml"/>
    </bean>

    <!-- URL 매핑 -->
    <http:conduit name="*.http-conduit">
        <http:tlsClientParameters>
            <sec:keyManagers keyPassword="password">
                <sec:keyStore type="JKS" password="password" file="client.jks"/>
            </sec:keyManagers>
            <sec:trustManagers>
                <sec:keyStore type="JKS" password="password" file="client-truststore.jks"/>
            </sec:trustManagers>
            <sec:cipherSuitesFilter>
                <sec:include>.*_WITH_3DES_.*</sec:include>
                <sec:include>.*_WITH_DES_.*</sec:include>
                <sec:include>.*_EXPORT_.*</sec:include>
                <sec:exclude>.*_WITH_NULL_.*</sec:exclude>
                <sec:exclude>.*_DH_anon_.*</sec:exclude>
            </sec:cipherSuitesFilter>
        </http:tlsClientParameters>
    </http:conduit>

    <!-- 서블릿 매핑 -->
    <http:destination name="http://localhost:8080/api/hello">
        <http:server>
            <http:service>
                <http:handlers>
                    <ref bean="helloService"/>
                </http:handlers>
            </http:service>
        </http:server>
    </http:destination>

    <!-- 보안 설정 -->
    <sec:bus>
        <sec:authorization>
            <sec:policy>
                <sec:exactlyOne>
                    <sec:all>
                        <sec:authenticated/>
                    </sec:all>
                </sec:exactlyOne>
            </sec:policy>
        </sec:authorization>
    </sec:bus>

</beans>
```

## 3. 서비스 구현

보안을 적용할 웹 서비스를 구현합니다. 예를 들어, Hello 웹 서비스를 구현한다면 다음과 같이 작성할 수 있습니다.

```java
@WebService(endpointInterface = "com.example.HelloService")
public class HelloServiceImpl implements HelloService {

    @Override
    public String sayHello(String name) {
        return "Hello, " + name + "!";
    }
}
```

## 4. 웹 서비스 배포

위에서 구현한 웹 서비스를 배포하기 위해 서블릿 컨테이너에 배포합니다. 예를 들어, Apache Tomcat을 사용한다면 `web.xml` 파일에 다음과 같이 추가합니다.

```xml
<servlet>
    <servlet-name>helloService</servlet-name>
    <servlet-class>com.example.HelloService</servlet-class>
    <load-on-startup>1</load-on-startup>
</servlet>

<servlet-mapping>
    <servlet-name>helloService</servlet-name>
    <url-pattern>/api/hello</url-pattern>
</servlet-mapping>
```

## 5. 웹 서비스 호출

보안이 적용된 웹 서비스를 호출하려면 클라이언트 측에서도 보안 설정을 해주어야 합니다. 아래는 보안 설정된 클라이언트 코드 예제입니다.

```java
public class HelloClient {

    public static void main(String[] args) {
        try {
            // 웹 서비스 클라이언트 생성
            HelloService service = new HelloService();
            HelloPortType port = service.getHelloPort();

            // 보안 헤더 설정
            Map<String, Object> requestContext = ((BindingProvider) port).getRequestContext();
            requestContext.put(SecurityConstants.USERNAME, "username");
            requestContext.put(SecurityConstants.PASSWORD, "password");

            // 웹 서비스 호출
            String response = port.sayHello("John");
            System.out.println(response);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위의 예제에서, `USERNAME`과 `PASSWORD`는 해당 웹 서비스에서 사용하는 인증 정보로 대체되어야 합니다.

이렇게 Java Apache CXF와 WS-Security를 사용하여 보안이 적용된 웹 서비스를 개발할 수 있습니다. CXF는 다양한 보안 기능을 지원하므로, 필요에 따라 해당 기능을 추가로 구성할 수 있습니다.

더 자세한 내용은 [Apache CXF 공식 문서](https://cxf.apache.org/docs/ws-security.html)를 참조하세요.