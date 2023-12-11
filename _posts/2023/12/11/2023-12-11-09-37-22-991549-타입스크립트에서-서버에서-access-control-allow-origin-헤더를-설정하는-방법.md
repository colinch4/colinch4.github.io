---
layout: post
title: "[typescript] 타입스크립트에서 서버에서 Access-Control-Allow-Origin 헤더를 설정하는 방법"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

## Express.js를 사용하는 경우

Express.js를 사용하여 타입스크립트 서버를 구축하는 경우, CORS 미들웨어를 사용하여 Access-Control-Allow-Origin 헤더를 설정할 수 있습니다. CORS 미들웨어는 요청을 처리하기 전에 브라우저에 응답을 전송하여 허용된 도메인에서의 요청인지를 확인합니다.

아래는 Express.js에서 CORS 미들웨어를 사용하여 Access-Control-Allow-Origin 헤더를 설정하는 예제입니다.

```typescript
import express from 'express';
import cors from 'cors';

const app = express();

app.use(
  cors({
    origin: 'https://allowed-domain.com'
  })
);

// 다른 미들웨어와 라우트 설정
```

위의 예제에서 `allowed-domain.com`은 클라이언트의 도메인으로 대체되어야 합니다.

## 다른 서버와의 통합

다른 서버와 통합하여 데이터를 요청하고자 할 때, Access-Control-Allow-Origin 헤더를 설정해야 할 수 있습니다. 이 경우에는 백엔드에서 해당 헤더를 설정하여 다른 출처의 요청을 허용해야 합니다.

이 방법으로 다른 출처의 서버와의 통합을 지원할 수 있고, 클라이언트 측 코드를 수정하지 않고도 요청을 보낼 수 있습니다.

더 자세한 내용은 [MDN Web Docs](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)를 참조하시기 바랍니다.