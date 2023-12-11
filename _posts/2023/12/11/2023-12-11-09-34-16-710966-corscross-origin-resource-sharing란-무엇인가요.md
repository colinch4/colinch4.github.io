---
layout: post
title: "[typescript] CORS(Cross-Origin Resource Sharing)란 무엇인가요?"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

일반적으로 브라우저는 같은 출처 정책(same-origin policy)을 따라, 다른 출처의 리소스에 직접적인 접근을 허용하지 않습니다. 하지만 CORS는 서버 측에서 응답 헤더를 구성하여 브라우저에게 다른 출처의 애플리케이션에서 해당 자원에 접근할 수 있는 권한이 있다는 것을 알려줍니다.

이를 실제로 TypeScript 애플리케이션에서 구현하려면, 서버 측에서 CORS 정책을 구성해야 합니다. 보통 Express와 같은 Node.js 웹 프레임워크에서 middleware를 사용하여 CORS를 구성합니다.

아래는 Express에서 CORS를 활성화하는 간단한 TypeScript 코드의 예시입니다.

```typescript
import express from 'express';
import cors from 'cors';

const app = express();

app.use(cors());
```

이렇게 함으로써 Express 애플리케이션이 다른 출처의 리소스에 대한 요청을 수락하도록 설정할 수 있습니다.

CORS를 구성할 때 주의해야 할 점은 보안을 유지하는 것입니다. 모든 출처의 요청을 허용하는 것은 보안상 위험이 있을 수 있으므로 최소한의 권한만 부여하는 것이 중요합니다.

더 많은 정보를 원하시면 MDN 웹 문서(https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)를 참고하시기 바랍니다.