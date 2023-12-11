---
layout: post
title: "[typescript] 타입스크립트에서 서버에서 Access-Control-Expose-Headers 헤더를 설정하는 방법"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

크로스 도메인 요청을 처리할 때, 브라우저는 다음 세 가지의 HTTP 헤더를 사용하여 요청을 제어합니다 : 

1. **Access-Control-Allow-Origin**
2. **Access-Control-Allow-Headers**
3. **Access-Control-Expose-Headers**

우리는 타입스크립트와 Node.js를 사용하여 서버를 구축할 때, 클라이언트에서 접근할 수 있는 헤더를 설정해야 합니다. Access-Control-Expose-Headers 헤더는 서버가 클라이언트에게 노출하고자 하는 헤더 목록을 정의합니다.

## Access-Control-Expose-Headers 헤더 설정하기

우리는 Node.js 서버에서 Express 프레임워크를 사용한다고 가정하고, 다음과 같이 Access-Control-Expose-Headers 헤더를 설정할 수 있습니다.

```typescript
import express from 'express';

const app = express();

app.use((req, res, next) => {
  res.header('Access-Control-Expose-Headers', 'Authorization');
  next();
});

// 다른 미들웨어와 라우트 코드들...

app.listen(3000, () => {
  console.log('서버가 3000번 포트에서 실행 중입니다.');
});
```

위의 코드에서, 우리는 Express 앱에 미들웨어를 추가하여 모든 응답에 Access-Control-Expose-Headers 헤더를 "Authorization"로 설정했습니다. 이렇게 함으로써 클라이언트에서 이 헤더에 접근할 수 있게 됩니다.

## 결론

Access-Control-Expose-Headers 헤더를 설정함으로써, 우리는 서버에서 클라이언트로 노출하고자 하는 헤더를 명시적으로 정의할 수 있습니다. 이것은 크로스 도메인 요청을 처리하는 과정에서 보안을 유지하면서 필요한 정보에 대한 접근을 허용하는 데 도움이 됩니다.

참고 문헌 :
- [MDN Web Docs - HTTP access control (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)