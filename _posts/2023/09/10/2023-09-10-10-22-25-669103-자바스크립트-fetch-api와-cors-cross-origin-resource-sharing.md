---
layout: post
title: "자바스크립트 fetch API와 CORS (Cross-Origin Resource Sharing)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트의 fetch API는 웹 애플리케이션에서 서버로 데이터를 요청하고 응답을 받을 수 있는 기능을 제공합니다. 하지만, 이러한 요청과 응답이 다른 도메인에서 온 경우 문제가 발생할 수 있습니다. 이 문제를 해결하기 위해 CORS (Cross-Origin Resource Sharing)라는 메커니즘이 사용됩니다.

## CORS란 무엇인가요?

CORS는 웹 애플리케이션이 다른 도메인에서 리소스를 요청할 수 있도록 해주는 메커니즘입니다. 기본적으로 브라우저는 [동일 출처 정책(Same Origin Policy)](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)에 따라 다른 도메인 간의 요청을 차단하는데, CORS는 이러한 제약을 우회할 수 있도록 해줍니다.

## fetch API와 CORS

fetch API는 서버로 HTTP 요청을 보내고 응답을 받을 수 있는 간편한 인터페이스를 제공합니다. 하지만 다른 도메인의 리소스를 요청할 때는 서버 측에서 CORS를 지원해야 합니다.

다음은 fetch API를 사용하여 다른 도메인의 데이터를 가져오는 예제입니다.

```javascript
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => {
    // 데이터를 처리하는 로직
  })
  .catch(error => {
    // 에러 처리하는 로직
  });
```

위 예제에서 `fetch` 함수를 호출할 때, 브라우저는 해당 도메인이 CORS를 지원하는지 확인합니다. 만약 해당 도메인이 CORS를 지원하지 않는다면, 브라우저는 요청을 차단하고 에러를 발생시킵니다.

## 서버에서 CORS 활성화하기

서버 측에서 CORS를 활성화하기 위해서는 응답 헤더에 CORS 관련 정보를 추가해야 합니다. 일반적으로 `Access-Control-Allow-Origin` 응답 헤더를 사용하여 특정 도메인에서의 요청을 허용합니다. 다음은 Node.js와 Express를 사용하여 CORS를 활성화하는 예제입니다.

```javascript
const express = require('express');
const app = express();

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', 'https://www.example.com');
  res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  next();
});

app.get('/data', (req, res) => {
  // 데이터를 응답하는 로직
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

위 예제에서는 모든 요청에 대해 `Access-Control-Allow-Origin` 헤더를 설정하고, 특정 도메인인 `https://www.example.com`에서의 요청을 허용하도록 설정했습니다. 또한 애플리케이션이 허용하는 HTTP 메서드와 헤더도 명시적으로 설정하였습니다.

## 요약

자바스크립트의 fetch API는 다른 도메인에서 리소스를 요청하고 응답을 받을 수 있는 편리한 기능을 제공합니다. 하지만 CORS 메커니즘을 이용하여 다른 도메인 간의 통신을 가능하도록 서버 측에서 처리해야 합니다. 서버에서 CORS를 활성화하기 위해서는 응답 헤더를 설정해야 하며, 일반적으로 `Access-Control-Allow-Origin` 헤더를 사용하여 요청을 허용하는 도메인을 지정합니다.

CORS는 웹 애플리케이션의 보안을 강화하면서도, 웹 개발자에게 다른 도메인 간의 통신을 가능하게 해주는 중요한 메커니즘입니다. 자바스크립트 fetch API와 함께 적절히 사용하면 다양한 도메인 간의 데이터 통신에 유용하게 활용할 수 있습니다.

참고: [MDN Web Docs - Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)