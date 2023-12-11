---
layout: post
title: "[typescript] 타입스크립트에서 서버에서 Access-Control-Allow-Credentials 헤더를 설정하는 방법"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

먼저, Node.js를 사용하여 서버를 구축하고 있다고 가정하겠습니다.

### CORS 패키지 설치

먼저, CORS(Cross-Origin Resource Sharing) 패키지를 설치해야 합니다. 이를 통해 서버에서 CORS를 손쉽게 구성할 수 있습니다.

```bash
npm install cors
```

### 서버 코드 구성

다음으로, 서버 코드에서 CORS 패키지를 사용하여 `Access-Control-Allow-Credentials` 헤더를 설정할 수 있습니다. 아래는 Express를 사용하는 예제 코드입니다.

```typescript
import express from 'express';
import cors from 'cors';

const app = express();

// CORS 옵션 설정
const corsOptions = {
  origin: 'http://example.com',
  credentials: true, // 필요에 따라 true 또는 false로 설정
};

app.use(cors(corsOptions));

// 기타 라우트 및 미들웨어 설정
// ...

app.listen(3000, () => {
  console.log('서버가 3000번 포트에서 실행 중입니다.');
});
```

### 참고 자료

CORS 패키지 및 TypeScript에서의 적용에 대한 자세한 내용은 [공식 문서](https://github.com/expressjs/cors#readme)를 참조하시기 바랍니다.

위의 방법으로 설정한 후에는 클라이언트에서 해당 서버로 요청을 보낼 때, `withCredentials` 옵션을 `true`로 설정하여 Cross-Origin 요청과 관련된 문제를 해결할 수 있습니다.