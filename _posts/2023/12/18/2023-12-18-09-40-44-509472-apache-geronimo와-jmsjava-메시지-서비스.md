---
layout: post
title: "[java] Apache Geronimo와 JMS(Java 메시지 서비스)"
description: " "
date: 2023-12-18
tags: [java]
comments: true
share: true
---

Apache Geronimo는 **오픈소스** **자바 에디션 애플리케이션 서버**로, **Java EE** 애플리케이션을 실행하는 데 사용됩니다. **JMS**(Java 메시지 서비스)는 분산 시스템 간 메시지 전송을 지원하는 자바 API입니다. **이 블로그**에서는 Apache Geronimo에서 JMS를 구성하는 방법을 살펴보겠습니다.

## Apache Geronimo 설정
Apache Geronimo를 설치하고 실행한 후, **애플리케이션 서버**에 JMS 리소스를 구성해야 합니다. 이를 위해 Geronimo의 관리 콘솔을 사용할 수 있습니다. 올바른 권한을 갖는 사용자로 로그인하여 관리 콘솔에 액세스합니다.

## JMS 리소스 구성
1. 관리 콘솔에서 "Resources" 섹션을 선택합니다.
2. "JMS Resources"를 선택하고 "New JMS Resource" 버튼을 클릭합니다.
3. 필요한 JMS 리소스를 설정합니다. 예를 들어, 연결 팩토리, 대기열, 토픽 등을 정의할 수 있습니다.
4. 각 리소스에 필요한 세부 정보, 예를 들어 연결 팩토리의 호스트, 포트, 대기열 이름 등을 입력합니다.

## JMS 애플리케이션 개발
JMS 리소스가 구성된 후에는 Java 애플리케이션에서 해당 리소스를 활용할 수 있습니다. 아래는 간단한 JMS 애플리케이션의 예시입니다.

```java
import javax.jms.*;

public class JMSExample {
    public static void main(String[] args) {
        try {
            // JNDI를 사용하여 연결 팩토리 및 대기열을 찾습니다.
            InitialContext ctx = new InitialContext();
            ConnectionFactory connectionFactory = (ConnectionFactory) ctx.lookup("jms/MyConnectionFactory");
            Destination destination = (Destination) ctx.lookup("jms/MyQueue");

            // 연결을 만들고 메시지를 보냅니다.
            Connection connection = connectionFactory.createConnection();
            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            MessageProducer producer = session.createProducer(destination);
            TextMessage message = session.createTextMessage("Hello, JMS!");
            producer.send(message);

            // 정리 작업을 수행합니다.
            session.close();
            connection.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

이제 Apache Geronimo에서 JMS를 구성하고 Java 애플리케이션에서 이를 활용하는 기본적인 방법을 살펴보았습니다. JMS를 사용하면 여러 애플리케이션 간에 안정적이고 효율적인 메시지 통신이 가능해지며, Apache Geronimo의 지원을 받아 더욱 편리하게 활용할 수 있습니다.

## 참고 자료
- [Apache Geronimo 공식 웹사이트](http://geronimo.apache.org/)
- [Java Message Service (JMS)](https://docs.oracle.com/javaee/7/tutorial/jms.htm)