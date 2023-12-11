---
layout: post
title: "[typescript] CORS(Cross-Origin Resource Sharing)를 설정하려면 어떻게 해야 하나요?"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

웹 애플리케이션을 개발하다보면 CORS(Cross-Origin Resource Sharing) 문제를 마주칠 수 있습니다. 웹 브라우저는 보안상의 이유로 한 도메인에서 로드된 리소스가 다른 도메인으로의 요청을 제한하는데, 이를 우회하기 위해 CORS를 설정해야 합니다.

CORS 설정을 위해 다음과 같은 단계를 따릅니다.

## 1. 서버 측 CORS 설정

서버 측에서 CORS를 활성화하려면 다음과 같이 설정 파일이나 미들웨어를 통해 관련 헤더를 추가해야 합니다.

```typescript
import * as express from 'express';
import * as cors from 'cors';

const app = express();
app.use(cors());
```

위의 예제에서 `express`와 `cors` 라이브러리를 사용하여 CORS를 활성화하는 방법을 보여줍니다.

## 2. 클라이언트 측 CORS 설정

클라이언트 측에서는 일반적으로 별도의 설정이 필요하지 않지만, `fetch`나 `XMLHttpRequest`를 사용하여 CORS 요청을 보낼 때에는 올바른 헤더를 설정해야 합니다.

```typescript
fetch('https://api.example.com/data')
  .then(response => {
    // 처리
  })
  .catch(error => {
    // 에러 처리
  });
```

위의 예제는 `fetch`를 사용하여 CORS를 허용하는 서버로 요청을 보내는 방법을 보여줍니다.

## 결론

CORS 문제는 웹 개발 시 자주 마주치게 되는 문제 중 하나입니다. 그러나 서버 측과 클라이언트 측에서 각각 올바른 설정을 해주면 CORS 문제를 우회하고 안전하게 리소스에 접근할 수 있습니다.

더 많은 정보를 원하시면 아래 참고 자료를 확인해보세요.

## 참고 자료
- [MDN Web Docs - Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)