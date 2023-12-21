---
layout: post
title: "[nodejs] REST API를 위한 요청 처리 방법(Routing, Middleware)"
description: " "
date: 2023-12-21
tags: [nodejs]
comments: true
share: true
---

Node.js를 사용하여 REST API를 개발할 때는 요청 처리를 위한 Routing과 Middleware 기능을 적절히 구현해야 합니다. Routing은 클라이언트 요청을 해당하는 핸들러 함수로 연결해주는 과정이고, Middleware는 요청과 응답 사이의 공통 기능을 처리합니다. 

이 블로그 포스트에서는 Node.js의 Express 프레임워크를 사용하여 REST API의 요청 처리를 구현하는 방법을 다룰 것입니다.

## 1. Routing

Routing은 클라이언트로부터 오는 요청의 URL을 해당하는 핸들러 함수로 연결해주는 역할을 합니다. Express 프레임워크에서는 `app.get`, `app.post`, `app.put`, `app.delete` 등의 메서드를 사용하여 각각의 HTTP 메서드에 따른 라우팅을 설정할 수 있습니다. 

```javascript
// GET 요청에 대한 라우팅 설정 예시
app.get('/api/users', (req, res) => {
  // 유저 목록을 반환
});

// POST 요청에 대한 라우팅 설정 예시
app.post('/api/users', (req, res) => {
  // 새로운 유저를 추가
});
```

## 2. Middleware

Middleware는 요청과 응답의 중간에 위치하여 요청의 전처리나 응답의 후처리 등을 수행하는 기능을 합니다. 인증, 로깅, 에러 처리 등의 공통 기능들을 Middleware로 구현하여 코드의 재사용성과 유지보수성을 높일 수 있습니다.

```javascript
// 로깅 미들웨어 설정 예시
app.use((req, res, next) => {
  console.log(`[${new Date().toLocaleString()}] ${req.method} ${req.url}`);
  next();
});

// 인증 미들웨어 설정 예시
app.use((req, res, next) => {
  if (req.isAuthenticated()) {
    next();
  } else {
    res.status(401).send('Unauthorized');
  }
});
```

## 마무리

Node.js의 Express 프레임워크를 이용하여 REST API의 요청 처리를 위한 Routing과 Middleware 설정에 대해 알아보았습니다. 이러한 기능들을 적절히 활용하여 보다 효율적이고 안전한 REST API를 개발할 수 있습니다.

참고문헌:
- [Express 공식 문서](https://expressjs.com/)

다음 포스트에서는 보다 심도있는 내용을 다루어 보겠습니다.