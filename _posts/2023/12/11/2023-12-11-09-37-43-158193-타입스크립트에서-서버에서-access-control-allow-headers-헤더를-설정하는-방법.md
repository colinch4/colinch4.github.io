---
layout: post
title: "[typescript] 타입스크립트에서 서버에서 Access-Control-Allow-Headers 헤더를 설정하는 방법"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

크로스 도메인 요청 처리를 위해 서버에서 `Access-Control-Allow-Headers` 헤더를 설정해야 하는데, 타입스크립트에서는 어떻게 이를 수행할 수 있을까요?

## Node.js 서버의 경우

Node.js 서버에서 Express를 사용한다고 가정해봅시다. `Access-Control-Allow-Headers` 헤더를 설정하기 위해 `cors` 패키지를 사용할 수 있습니다.

```typescript
import express from 'express';
import cors from 'cors';

const app = express();

const corsOptions = {
  allowedHeaders: ['Content-Type', 'Authorization'], // 허용할 헤더를 지정
};

app.use(cors(corsOptions));

// ...이하 코드 생략
```

위의 예제에서, `corsOptions` 객체를 사용하여 허용하고자 하는 헤더를 지정할 수 있습니다. 이렇게 함으로써 서버는 해당 헤더에 대한 권한을 부여하게 됩니다.

## 참고 자료
- CORS 설정 관련 Express 공식 문서: [Express CORS Middleware](https://expressjs.com/en/resources/middleware/cors.html)
- `cors` 패키지의 자세한 사용법: [npm cors 패키지](https://www.npmjs.com/package/cors)