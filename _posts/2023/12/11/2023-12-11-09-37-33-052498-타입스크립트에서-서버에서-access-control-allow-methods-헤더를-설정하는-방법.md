---
layout: post
title: "[typescript] 타입스크립트에서 서버에서 Access-Control-Allow-Methods 헤더를 설정하는 방법"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

웹 애플리케이션을 개발하다 보면, 웹 브라우저의 보안 정책으로 인해 서버에 거부된 요청이 발생하는 경우가 있습니다. 이때 `Access-Control-Allow-Methods` 헤더를 설정하여 허용된 HTTP 메소드를 명시할 수 있습니다. 

이 게시물에서는 타입스크립트로 서버를 구축하고 `Access-Control-Allow-Methods` 헤더를 설정하는 방법에 대해 살펴보겠습니다.

## 1. CORS 미들웨어 사용하기

첫째로, Express.js와 같은 웹 프레임워크를 사용한다면, `cors` 미들웨어를 사용하여 `Access-Control-Allow-Methods` 헤더를 설정할 수 있습니다. 

먼저 `cors` 미들웨어를 설치합니다.

```bash
npm install cors
```

그런 다음, 서버에서 다음과 같이 `cors`를 사용하여 `Access-Control-Allow-Methods` 헤더를 설정할 수 있습니다.

```typescript
import express from 'express';
import cors from 'cors';

const app = express();

app.use(cors({
  methods: 'GET,POST'
}));

// 이후에 서버 설정과 라우팅을 계속 진행합니다
```

위의 예제에서, `methods` 옵션을 사용하여 서버가 허용하는 HTTP 메소드를 명시적으로 지정하였습니다.

## 2. 직접 헤더를 설정하기

만약 미들웨어를 사용하지 않는다면, 직접 헤더를 설정하여 `Access-Control-Allow-Methods` 헤더를 추가할 수 있습니다.

```typescript
import express from 'express';

const app = express();

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Methods', 'GET,POST');
  next();
});

// 이후에 서버 설정과 라우팅을 계속 진행합니다
```

위의 예제에서는 Express 미들웨어를 사용하여 모든 요청에 대해 `Access-Control-Allow-Methods` 헤더를 추가하고 있습니다.

## 마무리

타입스크립트를 사용하여 서버를 개발할 때, 클라이언트와의 통신에 필요한 CORS(Cross-Origin Resource Sharing) 정책을 준수하기 위해 `Access-Control-Allow-Methods` 헤더를 설정하는 방법에 대해 살펴보았습니다. 이를 통해 안전하고 원활한 웹 애플리케이션을 개발할 수 있습니다.

참고문헌: 
- [MDN Web Docs - CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)