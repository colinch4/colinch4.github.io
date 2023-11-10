---
layout: post
title: "CORS(Cross-Origin Resource Sharing)란 무엇인가요?"
description: " "
date: 2023-10-12
tags: [CORS]
comments: true
share: true
---

출처란 프로토콜, 호스트, 포트번호로 구성되며, 동일 출처(same-origin) 정책은 같은 출처에서 실행 중인 리소스끼리만 자유롭게 상호작용할 수 있도록 허용합니다. 예를 들어, abc.com 도메인에서 실행 중인 JavaScript 코드는 abc.com 도메인의 리소스에 자유롭게 접근할 수 있지만, xyz.com 도메인의 리소스에는 제한이 있습니다.

이 때, CORS 정책은 서로 다른 출처 간의 리소스 요청을 허용하기 위한 메커니즘입니다. 웹 애플리케이션 개발자는 서버 측에서 CORS 정책을 구성하여 특정 출처에서의 요청을 허용하도록 설정해야 합니다. 이렇게 설정된 서버에서는 요청에 대한 응답 헤더에 `Access-Control-Allow-Origin`과 같은 CORS 관련 헤더를 포함하여 브라우저에게 해당 요청이 허용된 출처에서 온 것임을 알려줍니다.

CORS 정책은 웹 애플리케이션의 보안을 강화하기 위해 존재하지만, 외부 API 호출이나 다른 도메인의 리소스 요청 등을 위해 CORS를 구성해야 할 때도 있습니다. 이때는 서버 측에서 출처를 허용해주는 설정을 해주어야 합니다.

```javascript
// Express.js에서 CORS 구성 예제
const express = require('express');
const app = express();

// 특정 출처에서의 요청을 허용
app.use(function(req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', 'https://allowed-origin.com');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    next();
});

// 다른 라우트에서 API 응답을 구현
app.get('/api/data', function(req, res) {
    res.json({ message: 'API Response' });
});

// 서버 실행
app.listen(3000, function() {
    console.log('Server listening on port 3000');
});
```

위 예제에서는 `https://allowed-origin.com` 출처에서의 요청만 허용하고, GET, POST, OPTIONS 메서드와 Content-Type 헤더도 허용하도록 설정되어 있습니다. 이렇게 설정된 서버는 허용된 출처에서의 요청에 대해 CORS 정책을 우회하여 응답을 반환할 수 있습니다.

CORS는 웹 개발에서 자주 접하게 되는 보안 정책 중 하나이며, 잘 이해하고 올바르게 구성함으로써 웹 애플리케이션의 확장성과 상호운용성을 높일 수 있습니다.