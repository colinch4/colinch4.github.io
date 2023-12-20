---
layout: post
title: "[nodejs] 마이크로서비스 아키텍처에서의 이벤트 소싱과 CQRS (Command Query Responsibility Segregation) 패턴 적용"
description: " "
date: 2023-12-20
tags: [nodejs]
comments: true
share: true
---

마이크로서비스 아키텍처에서 이벤트 소싱과 CQRS 패턴을 적용하는 것은 서비스 간의 결합도를 줄이고 확장성과 유연성을 높일 수 있는 중요한 요소입니다. 이번 글에서는 Node.js 기반의 마이크로서비스 아키텍처에서 이벤트 소싱과 CQRS 패턴의 적용 방법에 대해 살펴보겠습니다.

## 이벤트 소싱 (Event Sourcing)

이벤트 소싱은 모든 상태 변경을 이벤트의 시퀀스로 표현하는 패턴입니다. 각각의 상태 변경은 이벤트 형태로 저장되며, 시간 순서대로 저장된 이벤트들을 재생하면 현재 상태를 얻을 수 있습니다. Node.js에서는 [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter)를 사용하여 이벤트 소싱을 구현할 수 있습니다.

예를 들어, 주문 서비스에서 주문 생성, 주문 취소 등의 이벤트를 정의하고 발생시킨 후에 이를 이벤트 스토어에 저장합니다. 이후에는 해당 이벤트를 재생하여 언제든지 시스템의 상태를 알 수 있습니다.

```javascript
const EventEmitter = require('events');
class OrderService extends EventEmitter {
  createOrder(orderData) {
    // 주문 생성 로직 수행
    this.emit('orderCreated', { orderId: '123', ...orderData });
  }
}
```

## CQRS (Command Query Responsibility Segregation)

CQRS는 명령(Command)과 조회(Query)를 분리하는 패턴으로, 데이터의 업데이트를 처리하는 명령 모델과 데이터를 조회하는 조회 모델을 분리합니다. Node.js에서는 [Express](https://expressjs.com/)나 [Fastify](https://www.fastify.io/)와 같은 웹 프레임워크를 사용하여 CQRS를 구현할 수 있습니다.

예를 들어, 주문 서비스에서 주문 생성 명령에 대한 핸들러와 주문 조회에 대한 핸들러를 분리하여 구현할 수 있습니다.

```javascript
const express = require('express');
const app = express();

app.post('/orders', async (req, res) => {
  // 주문 생성 명령 처리
});

app.get('/orders', async (req, res) => {
  // 주문 조회 처리
});
```

## 마무리

Node.js를 사용한 마이크로서비스 아키텍처에서 이벤트 소싱과 CQRS 패턴을 적용하는 것은 서비스 간의 결합도를 낮추고 확장성을 높일 수 있는 중요한 기술적 선택입니다. 이러한 패턴을 적절히 활용하여 안정적이고 확장 가능한 서비스를 구축할 수 있습니다.

참고: [Martin Fowler의 CQRS 패턴 소개](https://martinfowler.com/bliki/CQRS.html)

이상으로 마이크로서비스 아키텍처에서의 이벤트 소싱과 CQRS 패턴 적용에 대해 알아보았습니다. 어떠한 피드백이라도 환영합니다!