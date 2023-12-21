---
layout: post
title: "[nodejs] HTTP 메서드(GET, POST, PUT, DELETE)와 REST API"
description: " "
date: 2023-12-21
tags: [nodejs]
comments: true
share: true
---

REST(Representational State Transfer)는 웹 기술의 아키텍처 원칙 중 하나로, 웹 기반 응용 프로그램과 서비스 간의 통신을 위한 소프트웨어 디자인 스타일이다. REST 아키텍처에서는 **HTTP 메소드**(GET, POST, PUT, DELETE)를 사용하여 자원을 관리하고 상태를 전이시킨다.

## HTTP 메서드

### GET

GET 메서드는 서버로부터 자원을 요청한다. 주로 데이터를 조회할 때 사용되며, 요청한 자원을 응답으로 받아온다.

### POST

POST 메서드는 서버에 새로운 자원을 생성하거나 처리하기 위해 데이터를 제출한다. 예를 들어, 새로운 사용자를 등록하거나 새로운 글을 작성할 때 사용된다.

### PUT

PUT 메서드는 서버의 자원을 갱신할 때 사용된다. 존재하지 않는 경우에는 새로운 자원을 생성하며, 존재할 경우에는 해당 자원을 갱신한다.

### DELETE

DELETE 메서드는 서버에서 자원을 삭제한다. 해당 자원의 삭제를 요청하고 응답으로 삭제 여부를 받아온다.

## REST API에서의 활용

RESTful API는 HTTP 요청을 통해 자원을 관리하고 상태를 전이시킨다. 예를 들어, `/users` 경로에 GET 요청을 보내면 모든 사용자를 조회하고, POST 요청을 보내면 새로운 사용자를 추가할 수 있다.

```javascript
// GET /users: 모든 사용자 조회
// POST /users: 새로운 사용자 추가
// PUT /users/{id}: 특정 사용자 정보 수정
// DELETE /users/{id}: 특정 사용자 삭제
```

이처럼 HTTP 메서드를 활용하여 REST API를 설계하면, 각 요청에 대한 목적을 명확히 하고, 효율적인 자원 관리가 가능하다.

## 결론

HTTP 메서드(GET, POST, PUT, DELETE)는 RESTful API 설계에서 핵심적인 역할을 한다. 각 메서드의 용도를 명확히 이해하여 효과적인 RESTful API를 구현하는 것이 중요하다.

자세한 내용은 [MDN 웹 문서](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods)를 참고할 수 있다.