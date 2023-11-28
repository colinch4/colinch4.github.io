---
layout: post
title: "[java] ActiveMQ와 Java API for Message Service (JMS)의 차이점"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

## 소개
ActiveMQ와 Java API for Message Service (JMS)은 메시지 지향 미들웨어(MOM)를 구현하기 위한 두 가지 여러 옵션 중에 두 가지입니다. 두 기술 모두 자바 기반의 메시지 시스템이며, 애플리케이션 간에 비동기적으로 메시지를 교환하는 데 사용됩니다. 하지만 ActiveMQ와 JMS 사이에는 몇 가지 차이점이 있습니다.

## ActiveMQ
ActiveMQ는 Apache 소프트웨어 재단에서 개발한 오픈 소스 메시징 미들웨어 중 하나입니다. ActiveMQ는 AMQP, MQTT, OpenWire 등 다양한 프로토콜을 지원하며, 신뢰성, 확장성, 안정성 등 다양한 기능을 제공합니다.

또한 ActiveMQ는 잘 정의된 클라이언트-브로커 통신 모델을 가지고 있으며, 클러스터링 및 고가용성 구성을 지원합니다. 이를 통해 높은 처리량과 안정성을 제공할 수 있습니다. ActiveMQ는 메시지 브로커로서 작동하며, JMS 호환 프로토콜을 통해 Java 개발자가 쉽게 사용할 수 있습니다.

## Java API for Message Service (JMS)
Java API for Message Service (JMS)는 자바 기반의 메시지 지향 미들웨어를 사용하기 위한 공식 표준 API입니다. JMS는 자바 언어로 작성된 애플리케이션 간에 메시지를 교환할 수 있는 표준 방법을 제공합니다. JMS를 사용하면 클라이언트 애플리케이션은 JMS API를 통해 메시지를 생성, 송신, 수신 및 처리할 수 있습니다.

JMS는 여러 가지 메시징 모델을 지원합니다. P2P(점대점) 모델과 Pub/Sub(게시-구독) 모델을 통해 다양한 메시지 패턴을 구현할 수 있습니다. 또한 JMS는 Transaction 및 Message Listener와 같은 고급 기능을 제공하여 안정성과 유연성을 보장합니다.

## 차이점
ActiveMQ와 JMS 모두 메시지 지향 미들웨어를 구현하기 위한 도구이지만, 몇 가지 중요한 차이점이 있습니다.

1. **ActiveMQ는 메시지 브로커**입니다. ActiveMQ는 메시지를 송수신하는 중간 역할을 하는 브로커로서 동작합니다. 반면, JMS는 자바 애플리케이션 간에 메시지를 교환하기 위한 API입니다.

2. **ActiveMQ는 JMS API의 구현체**입니다. ActiveMQ는 JMS 표준에 따라 구현된 메시징 시스템입니다. 따라서 ActiveMQ는 JMS API를 사용하여 메시지를 작성, 전송 및 수신할 수 있습니다.

3. **ActiveMQ는 다양한 프로토콜을 지원**합니다. ActiveMQ는 AMQP, MQTT, OpenWire 등 다양한 프로토콜을 지원하여 다양한 애플리케이션 및 기기 간에 메시지를 교환할 수 있습니다. JMS는 자바 기반의 표준 API이기 때문에 다른 프로토콜을 직접 지원하지는 않습니다.

4. **ActiveMQ는 높은 확장성과 안정성을 제공**합니다. ActiveMQ는 클러스터링 및 고가용성 구성을 지원하여 높은 처리량과 안정성을 제공할 수 있습니다. JMS는 표준 API이기 때문에 이러한 기능을 직접 제공하지는 않습니다.

## 결론
ActiveMQ와 JMS는 모두 메시지 지향 미들웨어를 구현하는데 사용되는 도구입니다. ActiveMQ는 JMS 표준에 따라 구현된 메시징 시스템으로 다양한 프로토콜을 지원하며 높은 확장성과 안정성을 제공합니다. 반면, JMS는 자바 기반의 표준 API로 메시지 교환을 위한 일반적인 방법을 제공합니다. 두 기술은 각각의 장점과 사용 사례에 따라 선택될 수 있습니다.

## 참고 자료
- [ActiveMQ Documentation](http://activemq.apache.org/documentation.html)
- [Java API for Message Service (JMS) Documentation](https://docs.oracle.com/javaee/7/api/javax/jms/package-summary.html)