---
layout: post
title: "[java] Java Apache CXF와 트랜스포트(Transport) 프로토콜"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Java Apache CXF는 웹 서비스 개발을 위한 자바 프레임워크입니다. CXF는 SOAP(Simple Object Access Protocol) 및 REST(Representational State Transfer) 스타일의 웹 서비스를 지원하며, 여러 가지 트랜스포트 프로토콜을 사용할 수 있습니다.

## Apache CXF의 트랜스포트 프로토콜

CXF는 여러 가지 트랜스포트 프로토콜을 사용하여 웹 서비스를 처리할 수 있습니다. 주요 트랜스포트 프로토콜로는 HTTP, HTTPS, JMS(Java Message Service), SMTP(Simple Mail Transfer Protocol) 등이 있습니다. 이러한 다양한 프로토콜을 사용하여 CXF를 통해 웹 서비스를 구현할 수 있습니다.

## HTTP 및 HTTPS 트랜스포트 프로토콜

HTTP와 HTTPS는 가장 일반적으로 사용되는 웹 통신 프로토콜입니다. CXF를 사용하여 HTTP 또는 HTTPS 트랜스포트를 설정하려면 다음과 같이 설정 파일에서 프로토콜을 정의해야 합니다.

```java
<http:conduit name="*.http-conduit">
    <http:tlsClientParameters disableCNCheck="true">
        <sec:keyManagers keyPassword="password">
            <sec:keyStore type="JKS" password="password" file="client.keystore"/>
        </sec:keyManagers>
        <sec:trustManagers>
            <sec:keyStore type="JKS" password="password" file="client.truststore"/>
        </sec:trustManagers>
    </http:tlsClientParameters>
</http:conduit>
```

위의 예제에서는 `https://localhost:8080`로 시작하는 URL에 대한 HTTP conduit를 설정하고 있습니다. 이 설정에서는 클라이언트의 키 저장소와 신뢰 저장소를 지정하고 있으며, CN(Certificate Name) 검사를 해제하도록 설정되어 있습니다.

## JMS 트랜스포트 프로토콜

JMS(Java Message Service)는 메시지 전송을 위한 자바 API입니다. CXF를 사용하여 JMS 트랜스포트를 설정하려면 다음과 같이 설정 파일에서 프로토콜을 정의해야 합니다.

```java
<jms:conduit name="*.jms-conduit" username="guest" password="guest" destinationName="queue:testQueue">
    <jms:target destinationStyle="queue" replyDestinationName="queue:replyQueue"/>
    <jms:features>
        <jms:customConnector>
            <bean class="org.apache.activemq.pool.PooledConnectionFactory">
                <property name="brokerURL" value="tcp://localhost:61616"/>
            </bean>
        </jms:customConnector>
    </jms:features>
</jms:conduit>
```

위의 예제에서는 `queue:testQueue`로 메시지를 보내기 위한 JMS conduit를 설정하고 있습니다. 이 설정에서는 ActiveMQ의 연결 팩토리를 사용하여 JMS 연결을 관리하고 있습니다.

## SMTP 트랜스포트 프로토콜

SMTP(Simple Mail Transfer Protocol)는 전자 메일을 보내기 위한 프로토콜입니다. CXF를 사용하여 SMTP 트랜스포트를 설정하려면 다음과 같이 설정 파일에서 프로토콜을 정의해야 합니다.

```java
<mail:conduit name="*.smtp-conduit">
    <mail:tlsSender>
        <mail:tlsClientParameters disableCNCheck="true">
            <sec:keyManagers keyPassword="password">
                <sec:keyStore type="JKS" password="password" file="client.keystore"/>
            </sec:keyManagers>
            <sec:trustManagers>
                <sec:keyStore type="JKS" password="password" file="client.truststore"/>
            </sec:trustManagers>
        </mail:tlsClientParameters>
    </mail:tlsSender>
    <mail:smtpsHostnameVerifier>strict</mail:smtpsHostnameVerifier>
    <mail:smtpsPort>465</mail:smtpsPort>
</mail:conduit>
```

위의 예제에서는 SMTPS(SMTP over SSL) 프로토콜을 사용하여 안전한 이메일 전송을 설정하고 있습니다. 이 설정에서는 클라이언트의 키 저장소와 신뢰 저장소를 지정하고 있으며, CN 검사를 해제하고 포트 번호를 465로 설정하고 있습니다.

## 결론

Java Apache CXF는 다양한 트랜스포트 프로토콜을 지원하여 웹 서비스 개발을 더욱 유연하게 할 수 있습니다. 위에서 소개한 HTTP, HTTPS, JMS, SMTP와 같은 프로토콜을 사용하여 CXF를 통해 안전하고 효율적인 웹 서비스를 구현할 수 있습니다. CXF 문서를 참조하여 자세한 설정 방법을 확인할 수 있습니다.

## 참고 자료
- [Apache CXF 공식 문서](https://cxf.apache.org/docs/)
- [Java Message Service(JMS) 개요](https://www.oracle.com/technical-resources/articles/java/jms1.html)
- [SMTP 프로토콜 개요](https://tools.ietf.org/html/rfc821)