---
layout: post
title: "[javascript] Express.js에서의 JWT(Json Web Token) 사용법"
description: " "
date: 2023-12-04
tags: [javascript]
comments: true
share: true
---

## 소개

JSON Web Token (JWT)은 웹 애플리케이션에서 인증 및 데이터 교환을 위한 자주 사용되는 보안 토큰입니다. JWT는 서버와 클라이언트 간의 인증을 위해 사용될 수 있으며, 데이터의 무결성을 검증하고 신뢰할 수 있는 소스를 확인합니다. 이 글에서는 Express.js에서 JWT를 사용하는 방법에 대해 알아보겠습니다.

## Express.js에 JWT 패키지 설치하기

JWT를 Express.js에서 사용하기 위해서는 `jsonwebtoken` 패키지를 설치해야 합니다. 아래 명령어를 사용하여 패키지를 설치할 수 있습니다.

```bash
npm install jsonwebtoken
```

## JWT 생성하기

JWT를 생성하려면 `jsonwebtoken` 패키지를 가져와야 합니다. 아래 예제는 Express.js에서 JWT를 생성하는 코드입니다.

```javascript
const jwt = require('jsonwebtoken');
const secretKey = 'mysecretkey';

const payload = { user_id: 12345 };

// JWT를 생성하고 반환합니다.
const token = jwt.sign(payload, secretKey);

console.log(token);
```

위 코드에서 `jwt.sign()` 함수를 사용하여 JWT를 생성합니다. 첫 번째 매개변수로는 사용자 정의 데이터(payload)를 전달하고, 두 번째 매개변수로는 시크릿 키(secretKey)를 전달합니다. JWT가 생성되면 해당 토큰을 사용하여 클라이언트와 서버 간의 통신에 사용할 수 있습니다.

## JWT 검증하기

JWT를 검증하기 위해서는 클라이언트에서 서버로 전송된 토큰을 검증해야 합니다. 아래 예제는 Express.js에서 JWT를 검증하는 코드입니다.

```javascript
const jwt = require('jsonwebtoken');
const secretKey = 'mysecretkey';

const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjM0NSwiaWF0IjoxNTE2MjM5MDIyfQ.9OUxUyvDiPVMV8Mg2p93XvYONC1-J9pEPY88WSm7WPk';

jwt.verify(token, secretKey, (err, decoded) => {
  if (err) {
    console.error('JWT 검증 실패:', err.message);
  } else {
    console.log('JWT 검증 성공:', decoded);
  }
});
```

위 코드에서 `jwt.verify()` 함수를 사용하여 JWT를 검증합니다. 첫 번째 매개변수로는 검증할 토큰을 전달하고, 두 번째 매개변수로는 시크릿 키(secretKey)를 전달합니다. 검증된 토큰은 `decoded` 객체로 반환되며, 검증에 실패하면 오류 객체가 전달됩니다.

## 결론

이제 Express.js에서 JWT를 사용하는 방법에 대해 알아보았습니다. JWT는 보안 토큰을 생성하고 검증하는 간편한 방법을 제공합니다. Express.js를 사용해서 웹 애플리케이션을 개발한다면, JWT를 사용하여 인증 및 데이터의 무결성을 보장할 수 있습니다.

## 참고 자료

- [jsonwebtoken 패키지](https://www.npmjs.com/package/jsonwebtoken)
- [JWT 공식 사이트](https://jwt.io/)