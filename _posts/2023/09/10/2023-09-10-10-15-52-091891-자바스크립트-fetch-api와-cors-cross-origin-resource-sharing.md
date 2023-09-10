---
layout: post
title: "자바스크립트 fetch API와 CORS (Cross-Origin Resource Sharing)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 웹 개발에서 매우 중요한 역할을 하는 언어입니다. 이 언어를 사용하여 웹 페이지를 동적으로 조작하고 서버와 데이터를 주고받을 수 있습니다. 자바스크립트의 Fetch API는 웹 개발자들이 네트워크를 통해 데이터를 요청하고 응답을 받을 수 있도록 도와주는 기능을 제공합니다. 하지만, 이 Fetch API를 사용하여 외부 도메인의 데이터를 가져오기 위해서는 CORS (Cross-Origin Resource Sharing)에 대한 이해가 필요합니다.

## CORS (Cross-Origin Resource Sharing)

CORS는 웹 애플리케이션 개발 시 다른 도메인의 리소스를 요청할 때 브라우저의 보안 정책에 따라 제한을 받는 문제를 해결하기 위해 사용되는 메커니즘입니다. 웹 사이트는 동일한 출처(Origin)에서만 리소스를 요청할 수 있습니다. 출처는 프로토콜 (HTTP, HTTPS), 호스트명, 포트번호로 구성됩니다.

만약 웹 애플리케이션이 동일한 출처가 아닌 서버의 데이터를 요청하면, 브라우저는 **Same-Origin Policy**로 인하여 요청이 차단됩니다. 이때 CORS를 사용하여 서버가 다른 도메인에서 오는 요청을 허용할 수 있도록 설정할 수 있습니다.

## Fetch API와 CORS

Fetch API는 비동기 네트워크 요청을 위한 새로운 표준입니다. XMLHttpRequest와 비교하였을 때, Fetch API는 더욱 간단하고 강력한 기능을 제공합니다. 하지만 다른 도메인의 데이터를 요청할 때는 CORS에 대한 처리가 필요합니다.

보통 Fetch API를 사용할 때, 다음과 같은 절차를 따릅니다.

1. fetch() 함수를 사용하여 데이터를 요청합니다.
2. 서버에서 온 응답을 처리하기 위해 promise를 사용합니다.
3. 응답을 가져와서 데이터를 사용합니다.

그러나 만약 다른 도메인의 데이터를 요청할 경우, 브라우저는 먼저 프리플라이팅 (preflighting) 요청을 보내서 서버가 CORS를 지원하는지 확인합니다. 이때 서버는 요청을 허용하기 위한 응답 헤더를 반환해야 합니다.

프리플라이팅 요청이 성공하면, 실제 데이터 요청이 이루어지고 응답을 받게 됩니다. 하지만 서버가 CORS를 지원하지 않는다면, 에러가 발생하게 됩니다.

## CORS 처리하기

서버에서 CORS를 처리하는 방법은 각 언어나 프레임워크마다 다를 수 있습니다. 하지만 일반적으로는 다음과 같은 방법을 사용합니다.

1. Access-Control-Allow-Origin 헤더를 설정하여 요청을 허용할 도메인을 지정합니다.
   - 모든 도메인을 허용: `Access-Control-Allow-Origin: *`
   - 특정 도메인만 허용: `Access-Control-Allow-Origin: https://example.com`
2. 필요한 경우에는 다른 CORS 헤더 (Access-Control-Allow-Methods, Access-Control-Allow-Headers 등)를 설정하여 추가적인 제어를 할 수 있습니다.

```javascript
// CORS 설정 예제 (Node.js, Express)
const express = require('express');
const app = express();

app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', 'https://example.com');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});

// CORS 요청 처리
app.get('/api/data', (req, res) => {
  // 데이터를 반환하는 코드
});

app.listen(3000, () => {
  console.log('서버가 시작되었습니다.');
});
```

위의 예제는 Node.js와 Express 프레임워크를 사용하여 CORS를 처리하는 방법을 보여줍니다. **Access-Control-Allow-Origin** 헤더를 사용하여 요청을 허용할 도메인을 설정하고, 필요한 경우에는 다른 CORS 헤더를 설정할 수 있습니다.

## 결론

자바스크립트 Fetch API는 웹 개발에서 네트워크 요청을 처리하기 위한 강력한 도구입니다. 하지만 다른 도메인의 데이터를 요청할 때는 CORS에 대한 처리가 필요합니다. CORS를 제대로 처리하지 않으면 브라우저에서 요청을 차단하게 되므로, 서버 개발자들은 CORS 설정에 유의해야 합니다.

CORS를 허용하는 방법은 서버마다 다르므로, 각 서버의 문서를 확인하여 설정하는 방법을 알아볼 필요가 있습니다. 자바스크립트 Fetch API를 사용할 때는 CORS에 대한 이해와 처리를 함께 고려하여 안정적인 웹 애플리케이션을 개발할 수 있습니다.