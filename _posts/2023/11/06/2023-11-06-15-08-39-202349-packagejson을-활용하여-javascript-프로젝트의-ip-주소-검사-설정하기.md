---
layout: post
title: "Package.json을 활용하여 JavaScript 프로젝트의 IP 주소 검사 설정하기"
description: " "
date: 2023-11-06
tags: [package]
comments: true
share: true
---

JavaScript 프로젝트를 개발할 때, IP 주소 검사는 중요한 보안 요소입니다. 사용자의 IP 주소를 확인하여 액세스를 제한하거나 특정 기능을 제공하는 등의 작업을 수행할 수 있습니다. 이번 블로그 포스트에서는 package.json 파일을 활용하여 JavaScript 프로젝트에서 IP 주소 검사 설정하는 방법을 알아보겠습니다.

## 1. package.json 파일 수정하기

먼저, 프로젝트의 루트 디렉토리에 있는 package.json 파일을 열어야 합니다. 이 파일은 프로젝트의 의존성 및 설정 정보를 포함하고 있습니다. 다음과 같이 "config" 항목을 추가합니다.

```json
"config": {
  "allowedIPs": ["127.0.0.1", "192.168.0.1"]
}
```

위 예시에서는 "allowedIPs" 항목에 접근을 허용할 IP 주소를 배열로 입력하였습니다. 위 예시에서는 로컬 IP 주소인 "127.0.0.1"과 "192.168.0.1"에만 접근을 허용하도록 설정하였습니다. 

## 2. Express 미들웨어 설정하기

이제 package.json 파일을 수정했으니, Express 프레임워크를 사용하여 IP 주소 검사 미들웨어를 설정해보겠습니다. 

```javascript
const express = require('express');
const app = express();

app.use((req, res, next) => {
  const allowedIPs = req.app.get('allowedIPs');

  if (allowedIPs.includes(req.ip)) {
    next(); // 허용된 IP 주소이면 다음 미들웨어로 이동
  } else {
    res.status(403).send('Access denied'); // 허용되지 않은 IP 주소이면 403 에러 반환
  }
});

// 나머지 라우트 핸들러 등록
// ...

app.listen(3000, () => {
  console.log('서버가 3000번 포트에서 실행 중입니다.');
});
```

위 코드에서 app.use() 함수 내에 작성된 미들웨어 함수는 모든 요청에 대해 실행됩니다. 이 함수는 현재 요청의 IP 주소를 검사하여 허용된 IP 주소인 경우 다음 미들웨어로 이동하고, 그렇지 않은 경우 403 에러를 반환합니다. 미들웨어 함수 내에서는 req.app.get() 함수를 사용하여 package.json 파일의 "allowedIPs" 항목을 가져옵니다.

이제 Express 서버를 실행하고 허용된 IP 주소만 접근할 수 있는지 확인할 수 있습니다.

## 결론

이번 블로그 포스트에서는 package.json 파일을 활용하여 JavaScript 프로젝트의 IP 주소 검사 설정하는 방법을 알아보았습니다. package.json 파일을 수정하여 허용할 IP 주소를 설정하고, Express 미들웨어를 사용하여 IP 주소 검사를 수행할 수 있습니다. 이를 통해 프로젝트의 보안을 강화할 수 있습니다.